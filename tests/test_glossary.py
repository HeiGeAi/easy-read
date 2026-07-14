#!/usr/bin/env python3
"""
Regression tests for generate_glossary.py.

Run standalone (no pytest needed):
    python3 tests/test_glossary.py

Or with pytest:
    pytest tests/
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = str(ROOT / 'scripts' / 'generate_glossary.py')

BASE = {
    "summary": "测试摘要",
    "domains": [{"emoji": "🏥", "name": "医学", "count": 1}],
    "terms": {
        "beginner": [{
            "name": "CRISPR", "is_english": True,
            "ipa": "/ˈkrɪs.pər/", "chinese_pronunciation": "克里斯珀",
            "explanation": "一把精准修改基因的分子剪刀。",
        }]
    },
}


def _run(data=None, raw_bytes=None, stdin_mode=False):
    """Run the generator, return (returncode, stderr, html)."""
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, 'out.html')
        if stdin_mode:
            payload = raw_bytes if raw_bytes is not None else json.dumps(data).encode('utf-8')
            p = subprocess.run([sys.executable, SCRIPT, '-', out], input=payload, capture_output=True)
        else:
            inp = os.path.join(tmp, 'in.json')
            if raw_bytes is not None:
                with open(inp, 'wb') as f:
                    f.write(raw_bytes)
            else:
                with open(inp, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)
            p = subprocess.run([sys.executable, SCRIPT, inp, out], capture_output=True)
        html = Path(out).read_text(encoding='utf-8') if os.path.exists(out) else ''
        return p.returncode, p.stderr.decode(), html


def _clone():
    return json.loads(json.dumps(BASE))


def test_normal_render():
    rc, err, html = _run(BASE)
    assert rc == 0
    assert "克里斯珀" in html
    assert "/ˈkrɪs.pər/" in html
    assert 'lang="en"' in html          # a11y language marking
    assert "医学" in html               # domain index strip
    assert 'class="entry' in html       # dictionary-entry markup
    assert 'class="chapter' in html     # editorial chapter markup
    assert 'chapter__no' in html        # difficulty numeral


def test_utf8_bom_file():
    """A UTF-8 BOM used to crash json.load; utf-8-sig must strip it."""
    bom = ('﻿' + json.dumps(BASE, ensure_ascii=False)).encode('utf-8')
    rc, err, html = _run(raw_bytes=bom)
    assert rc == 0
    assert "克里斯珀" in html


def test_unknown_level_key_warns():
    """Terms under an unknown level must not vanish silently."""
    d = _clone()
    d["terms"] = {"guru": [{"name": "X"}]}
    rc, err, html = _run(d)
    assert rc == 1
    assert "guru" in err


def test_whitespace_ipa_no_empty_div():
    """A whitespace-only IPA must not emit an empty phonetic node."""
    d = _clone()
    d["terms"]["beginner"][0]["ipa"] = "   "
    rc, err, html = _run(d)
    assert rc == 0
    assert '<span class="ipa"' not in html   # stripped away, only cn-phon remains


def test_string_is_english_reports_validation_error():
    """Schema declares a JSON boolean, so string lookalikes must not be guessed."""
    d = _clone()
    d["terms"]["beginner"][0]["is_english"] = "false"
    d["terms"]["beginner"][0]["name"] = "中文词"
    rc, err, html = _run(d)
    assert rc == 1
    assert "is_english" in err
    assert "bool" in err
    assert html == ''


def test_stdin_mode():
    rc, err, html = _run(BASE, stdin_mode=True)
    assert rc == 0
    assert "克里斯珀" in html


def test_xss_escaped():
    d = _clone()
    d["summary"] = '<script>alert(1)</script>'
    rc, err, html = _run(d)
    assert rc == 0
    assert "&lt;script&gt;" in html
    assert "<script>alert(1)" not in html


def test_default_html_is_static_and_print_ready():
    """默认交付物打开即可读可打印，不依赖滚动脚本或动效。"""
    rc, err, html = _run(BASE)
    assert rc == 0
    lower = html.lower()
    assert '<script' not in lower
    for marker in ('transition:', '@keyframes', 'animation:', 'scroll-behavior:'):
        assert marker not in lower


def test_skill_fallback_uses_current_css_contract():
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    for css_class in ('entry', 'chapter', 'level-beginner', 'ipa', 'cn-phon'):
        assert css_class in skill
    for stale_class in ('term-card', 'difficulty-section', 'difficulty-badge'):
        assert stale_class not in skill


def test_decorative_emoji_aria_hidden():
    d = _clone()
    d["terms"]["beginner"][0]["timeline"] = "2023"
    rc, err, html = _run(d)
    assert rc == 0
    assert '<span aria-hidden="true">⏰</span>' in html


def test_help_flag():
    p = subprocess.run([sys.executable, SCRIPT, '--help'], capture_output=True)
    assert p.returncode == 0
    assert "Usage" in p.stdout.decode()


def test_no_args_exits_nonzero():
    p = subprocess.run([sys.executable, SCRIPT], capture_output=True)
    assert p.returncode == 1


def test_bad_json_reports_source():
    rc, err, html = _run(raw_bytes=b'{not json}')
    assert rc == 1
    assert "JSON" in err


def test_non_string_summary_reports_validation_error_without_traceback():
    """AI 生成的字段类型不稳定时，应给出契约错误而不是 Python traceback。"""
    d = _clone()
    d["summary"] = ["不是字符串"]
    rc, err, html = _run(d)
    assert rc == 1
    assert "summary" in err
    assert "Traceback" not in err


def test_non_string_phonetic_field_reports_validation_error_without_traceback():
    """会调用 strip() 的可选文本字段也必须先校验类型。"""
    d = _clone()
    d["terms"]["beginner"][0]["ipa"] = {"value": "bad"}
    rc, err, html = _run(d)
    assert rc == 1
    assert "ipa" in err
    assert "Traceback" not in err


def test_non_string_name_reports_validation_error_without_rendering_repr():
    """Object-shaped names must not be silently stringified into a glossary."""
    d = _clone()
    d["terms"]["beginner"][0]["name"] = {"unexpected": "object"}
    rc, err, html = _run(d)
    assert rc == 1
    assert "name" in err
    assert "str" in err
    assert "Traceback" not in err
    assert html == ''


def test_non_boolean_is_english_reports_validation_error():
    """Truthy arrays or numbers must not change the language markup."""
    for bad_value in (["false"], 1, None):
        d = _clone()
        d["terms"]["beginner"][0]["is_english"] = bad_value
        rc, err, html = _run(d)
        assert rc == 1
        assert "is_english" in err
        assert "bool" in err
        assert html == ''


if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    failed = 0
    for t in tests:
        try:
            t()
            print("  ✅ %s" % t.__name__)
        except AssertionError as e:
            failed += 1
            print("  ❌ %s  %s" % (t.__name__, e))
    print("\n%d passed, %d failed" % (len(tests) - failed, failed))
    sys.exit(1 if failed else 0)
