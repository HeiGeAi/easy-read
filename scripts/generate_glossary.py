#!/usr/bin/env python3
"""
Generate HTML glossary from jargon analysis results.

Usage:
    python3 generate_glossary.py <data.json> <output.html>
    python3 generate_glossary.py - <output.html>          # read JSON from stdin
    python3 generate_glossary.py --help

Arguments:
    data.json    Path to the JSON analysis file, or "-" to read from stdin.
    output.html  Path for the generated HTML output.
"""

import html
import json
import re
import sys
from pathlib import Path


USAGE = """\
Usage: python3 generate_glossary.py <data.json> <output.html>
       python3 generate_glossary.py - <output.html>          # read JSON from stdin

Arguments:
    data.json    Path to the JSON analysis file, or "-" to read from stdin.
    output.html  Path for the generated HTML output.

Options:
    --help, -h   Show this help message and exit.
"""


def esc(text):
    """HTML-escape user content to prevent XSS."""
    return html.escape(str(text)) if text is not None else ''


def validate_data(data):
    """Validate the loaded JSON data, return a list of error messages (empty = OK)."""
    errors = []
    if not isinstance(data, dict):
        errors.append("JSON 顶层必须是对象（dict），实际类型: %s" % type(data).__name__)
        return errors

    if 'summary' in data and data['summary'] is not None and not isinstance(data['summary'], str):
        errors.append("'summary' 字段必须是字符串（str），实际类型: %s"
                      % type(data['summary']).__name__)

    if 'terms' not in data:
        errors.append("JSON 中缺少 'terms' 字段")
    elif not isinstance(data['terms'], dict):
        errors.append("'terms' 字段必须是对象（dict），实际类型: %s" % type(data['terms']).__name__)
    else:
        valid_levels = {'beginner', 'intermediate', 'professional', 'advanced', 'expert'}
        unknown = set(data['terms'].keys()) - valid_levels
        if unknown:
            errors.append("'terms' 含未知等级键，这些术语不会被渲染: %s（合法等级: %s）"
                          % (', '.join(sorted(unknown)), ', '.join(sorted(valid_levels))))
        for level_key, terms in data['terms'].items():
            if not isinstance(terms, list):
                errors.append("'terms.%s' 必须是列表（list），实际类型: %s"
                              % (level_key, type(terms).__name__))
                continue
            for i, term in enumerate(terms, start=1):
                if not isinstance(term, dict):
                    errors.append("'terms.%s' 第 %d 项必须是对象（dict），实际类型: %s"
                                  % (level_key, i, type(term).__name__))
                    continue
                name = term.get('name')
                if not isinstance(name, str):
                    errors.append("'terms.%s' 第 %d 项的 'name' 字段必须是字符串（str），实际类型: %s"
                                  % (level_key, i, type(name).__name__))
                # Strip zero-width chars too, so a visually invisible name is rejected.
                elif not re.sub(r'[​‌‍﻿]', '', name).strip():
                    errors.append("'terms.%s' 第 %d 项缺少非空 'name' 字段" % (level_key, i))
                if 'is_english' in term and not isinstance(term['is_english'], bool):
                    errors.append("'terms.%s' 第 %d 项的 'is_english' 字段必须是布尔值（bool），实际类型: %s"
                                  % (level_key, i, type(term['is_english']).__name__))
                for field in ('ipa', 'chinese_pronunciation', 'explanation'):
                    value = term.get(field)
                    if value is not None and not isinstance(value, str):
                        errors.append("'terms.%s' 第 %d 项的 '%s' 字段必须是字符串（str），实际类型: %s"
                                      % (level_key, i, field, type(value).__name__))

    if 'domains' in data and data['domains'] is not None:
        domains = data['domains']
        if not isinstance(domains, list):
            errors.append("'domains' 字段必须是列表（list），实际类型: %s" % type(domains).__name__)
        else:
            for i, d in enumerate(domains, start=1):
                if not isinstance(d, dict):
                    errors.append("'domains' 第 %d 项必须是对象（dict），实际类型: %s"
                                  % (i, type(d).__name__))

    return errors


def generate_html(data, template_path, output_path):
    """Generate HTML from template and data."""

    # Read template — friendly error instead of a bare traceback
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print("错误: 找不到模板文件 — %s" % template_path, file=sys.stderr)
        print("请确认脚本位于 easy-read 仓库的 scripts/ 目录下运行，"
              "且 assets/glossary_template.html 存在。", file=sys.stderr)
        sys.exit(1)

    # Generate summary section — catch empty strings, not just missing keys
    summary = data.get('summary', '') or ''
    summary = summary.strip()
    if not summary:
        summary = '暂无摘要'

    # Generate glossary sections — each difficulty level is an editorial "chapter"
    difficulty_levels = [
        ('beginner',     '入门级', 'level-beginner',     '01', '谁都能懂'),
        ('intermediate', '进阶级', 'level-intermediate', '02', '关注就会遇到'),
        ('professional', '专业级', 'level-professional', '03', '从业者常用'),
        ('advanced',     '专家级', 'level-advanced',     '04', '深度专业'),
        ('expert',       '大师级', 'level-expert',       '05', '前沿 / 极专业'),
    ]

    glossary_html = []

    for level_key, level_name, level_class, level_no, level_desc in difficulty_levels:
        terms = data.get('terms', {}).get(level_key, [])
        if not terms:
            continue

        entries = ''.join(generate_term_card(t) for t in terms)
        section_html = (
            '<section class="chapter {cls}">'
            '<div class="chapter__head reveal">'
            '<span class="chapter__no">{no}</span>'
            '<h2 class="chapter__title">{name}</h2>'
            '<span class="chapter__meta">{desc} · {count} 个词</span>'
            '</div>'
            '{entries}'
            '</section>'
        ).format(cls=level_class, no=level_no, name=esc(level_name),
                 desc=esc(level_desc), count=len(terms), entries=entries)
        glossary_html.append(section_html)

    # Generate domain index strip
    domains = data.get('domains', [])
    domain_html = ''
    if domains:
        items = []
        for d in domains:
            emoji = esc(d.get('emoji', '📖'))
            name = esc(d.get('name', ''))
            try:
                count = int(d.get('count', 0))
            except (TypeError, ValueError):
                count = 0
            item = ('<li class="domain">'
                    '<span class="domain__emoji" aria-hidden="true">%s</span>'
                    '<span class="domain__name">%s</span>' % (emoji, name))
            if count > 0:
                item += '<span class="domain__count">%d</span>' % count
            item += '</li>'
            items.append(item)
        domain_html = (
            '<section class="domains reveal">'
            '<p class="domains__label kicker">本文涉及领域 · Fields</p>'
            '<ul class="domain-list">%s</ul>'
            '</section>'
        ) % ''.join(items)

    # Replace placeholders — escape summary to prevent XSS.
    # Single-pass replacement: only placeholders in the template itself get
    # expanded, so literal "{{XXX}}" inside user data is preserved as-is
    # instead of being expanded a second time.
    replacements = {
        'DOMAIN_OVERVIEW': domain_html,
        'SUMMARY': esc(summary),
        'GLOSSARY_SECTIONS': '\n'.join(glossary_html),
    }
    output_html = re.sub(
        r'\{\{(DOMAIN_OVERVIEW|SUMMARY|GLOSSARY_SECTIONS)\}\}',
        lambda m: replacements[m.group(1)],
        template,
    )

    # Write output — friendly errors instead of a bare traceback
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_html)
    except PermissionError:
        print("错误: 没有写入权限 — %s" % output_path, file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print("错误: 写入文件失败 — %s（%s）" % (output_path, e), file=sys.stderr)
        sys.exit(1)

    return output_path


def generate_term_card(term):
    """Generate HTML for a single term, styled as a dictionary entry."""

    name = esc(term.get('name', ''))
    is_english = term.get('is_english', False)

    parts = ['<article class="entry reveal">']

    # Head: headword + phonetics
    parts.append('<div class="entry__head">')
    if is_english:
        # lang="en" so screen readers use English TTS for the word
        parts.append('<span class="entry__name"><span class="en" lang="en">%s</span></span>' % name)
    else:
        parts.append('<span class="entry__name is-cn">%s</span>' % name)

    # Strip first so a whitespace-only value doesn't produce an empty visible node
    ipa = (term.get('ipa') or '').strip()
    cn_pron = (term.get('chinese_pronunciation') or '').strip()
    if ipa or cn_pron:
        phon = '<span class="entry__phon">'
        if ipa:
            phon += '<span class="ipa" lang="en">%s</span>' % esc(ipa)
        if cn_pron:
            phon += '<span class="cn-phon">%s</span>' % esc(cn_pron)
        phon += '</span>'
        parts.append(phon)
    parts.append('</div>')

    # Explanation — fallback to "暂无解释" when missing or empty
    explanation = (term.get('explanation', '') or '').strip()
    if not explanation:
        explanation = '暂无解释'
    parts.append('<p class="entry__explain">%s</p>' % esc(explanation))

    # What it is (for products/people)
    if term.get('what_is'):
        parts.append('<div class="entry__note"><span class="note__label">是什么</span>'
                     '<span class="note__body">%s</span></div>' % esc(term['what_is']))

    # Why important (for products/people)
    if term.get('why_important'):
        parts.append('<div class="entry__note"><span class="note__label">为什么重要</span>'
                     '<span class="note__body">%s</span></div>' % esc(term['why_important']))

    # Historical context
    if term.get('history'):
        parts.append('<div class="entry__note entry__note--history"><span class="note__label">历史背景</span>'
                     '<span class="note__body">%s</span></div>' % esc(term['history']))

    # Timeline — independent optional field (per SKILL.md schema)
    if term.get('timeline'):
        parts.append('<div class="entry__time"><span aria-hidden="true">⏰</span> %s</div>' % esc(term['timeline']))

    # Learn more
    parts.append('<div class="entry__more"><span aria-hidden="true">💬</span> 想了解更多，继续问我</div>')

    parts.append('</article>')
    return ''.join(parts)


def main():
    # --help / -h
    if '--help' in sys.argv or '-h' in sys.argv:
        print(USAGE)
        sys.exit(0)

    if len(sys.argv) < 3:
        print(USAGE, file=sys.stderr)
        sys.exit(1)

    data_arg = sys.argv[1]
    output_path = Path(sys.argv[2])

    # Get template path — resolve() so a symlinked skill dir still finds assets/
    script_dir = Path(__file__).resolve().parent
    template_path = script_dir.parent / 'assets' / 'glossary_template.html'

    # Load data — support stdin via "-"
    try:
        if data_arg == '-':
            # Guard against non-UTF-8 stdin locales (Windows legacy codepages)
            # producing silent mojibake; utf-8-sig also strips a BOM if present.
            try:
                sys.stdin.reconfigure(encoding='utf-8-sig')
            except (AttributeError, ValueError):
                pass
            data = json.load(sys.stdin)
        else:
            data_path = Path(data_arg)
            # utf-8-sig transparently handles BOM-prefixed files (Windows editors)
            with open(data_path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
    except json.JSONDecodeError as e:
        source = 'stdin' if data_arg == '-' else data_arg
        print("错误: JSON 解析失败 (%s) — %s" % (source, e), file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("错误: 文件不存在 — %s" % data_arg, file=sys.stderr)
        sys.exit(1)

    # Validate data
    errors = validate_data(data)
    if errors:
        for err in errors:
            print("错误: %s" % err, file=sys.stderr)
        sys.exit(1)

    # Generate HTML
    result = generate_html(data, template_path, output_path)
    print("Generated: %s" % result)


if __name__ == '__main__':
    main()
