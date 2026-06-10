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

    if 'terms' not in data:
        errors.append("JSON 中缺少 'terms' 字段")
    elif not isinstance(data['terms'], dict):
        errors.append("'terms' 字段必须是对象（dict），实际类型: %s" % type(data['terms']).__name__)
    else:
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
                if name is None or not str(name).strip():
                    errors.append("'terms.%s' 第 %d 项缺少非空 'name' 字段" % (level_key, i))

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

    # Generate glossary sections
    difficulty_levels = [
        ('beginner', '入门级', 'difficulty-beginner'),
        ('intermediate', '进阶级', 'difficulty-intermediate'),
        ('professional', '专业级', 'difficulty-professional'),
        ('advanced', '专家级', 'difficulty-advanced'),
        ('expert', '大师级', 'difficulty-expert'),
    ]

    glossary_html = []

    for level_key, level_name, level_class in difficulty_levels:
        terms = data.get('terms', {}).get(level_key, [])
        if not terms:
            continue

        section_html = '''
        <div class="difficulty-section">
            <div class="difficulty-header">
                <span class="difficulty-badge {cls}">{name}</span>
                <span class="difficulty-title">{name}术语</span>
            </div>
        '''.format(cls=level_class, name=level_name)

        for term in terms:
            term_html = generate_term_card(term)
            section_html += term_html

        section_html += '</div>'
        glossary_html.append(section_html)

    # Generate domain overview bar
    domains = data.get('domains', [])
    domain_html = ''
    if domains:
        tags = []
        for d in domains:
            emoji = esc(d.get('emoji', '📖'))
            name = esc(d.get('name', ''))
            try:
                count = int(d.get('count', 0))
            except (TypeError, ValueError):
                count = 0
            tag = '<div class="domain-tag">'
            tag += '<span class="domain-emoji">%s</span>' % emoji
            tag += '<span>%s</span>' % name
            if count > 0:
                tag += '<span class="domain-count">%d</span>' % count
            tag += '</div>'
            tags.append(tag)
        domain_html = '<div class="domain-overview">%s</div>' % ''.join(tags)

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

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_html)

    return output_path


def generate_term_card(term):
    """Generate HTML for a single term card."""

    name = esc(term.get('name', ''))
    is_english = term.get('is_english', False)

    card_html = '<div class="term-card">'

    # Term name
    if is_english:
        card_html += '<div class="term-name"><span class="english">%s</span></div>' % name
    else:
        card_html += '<div class="term-name">%s</div>' % name

    # Pronunciation — render whenever provided; is_english only controls name styling
    if term.get('ipa'):
        card_html += '<div class="pronunciation">%s</div>' % esc(term["ipa"])

    if term.get('chinese_pronunciation'):
        card_html += '<div class="pronunciation-help">%s</div>' % esc(term["chinese_pronunciation"])

    # Explanation — fallback to "暂无解释" when missing or empty
    explanation = (term.get('explanation', '') or '').strip()
    if not explanation:
        explanation = '暂无解释'
    card_html += '<div class="term-explanation">%s</div>' % esc(explanation)

    # What it is (for products/people)
    if term.get('what_is'):
        card_html += '''
        <div class="term-section">
            <div class="term-label">是什么：</div>
            <div class="term-content">%s</div>
        </div>
        ''' % esc(term["what_is"])

    # Why important (for products/people)
    if term.get('why_important'):
        card_html += '''
        <div class="term-section">
            <div class="term-label">为什么重要：</div>
            <div class="term-content">%s</div>
        </div>
        ''' % esc(term["why_important"])

    # Historical context
    if term.get('history'):
        card_html += '''
        <div class="history">
            <div class="term-label">历史背景：</div>
            <div class="term-content">%s</div>
        </div>
        ''' % esc(term["history"])

    # Timeline — independent optional field (per SKILL.md schema),
    # rendered even when history is absent
    if term.get('timeline'):
        card_html += '<div class="timeline">⏰ %s</div>' % esc(term["timeline"])

    # Learn more
    card_html += '<div class="learn-more">💬 想了解更多，可以继续对话</div>'

    card_html += '</div>'

    return card_html


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

    # Get template path
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / 'assets' / 'glossary_template.html'

    # Load data — support stdin via "-"
    try:
        if data_arg == '-':
            data = json.load(sys.stdin)
        else:
            data_path = Path(data_arg)
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
    except json.JSONDecodeError as e:
        print("错误: JSON 解析失败 — %s" % e, file=sys.stderr)
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
