#!/usr/bin/env python3
"""
Generate HTML glossary from jargon analysis results.
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def generate_html(data, template_path, output_path):
    """Generate HTML from template and data."""

    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Generate summary section
    summary = data.get('summary', '暂无摘要')

    # Generate glossary sections
    difficulty_levels = [
        ('beginner', '入门级', 'difficulty-beginner'),
        ('intermediate', '进阶级', 'difficulty-intermediate'),
        ('professional', '专业级', 'difficulty-professional'),
        ('advanced', '资深级', 'difficulty-advanced'),
        ('expert', '专家级', 'difficulty-expert'),
    ]

    glossary_html = []

    for level_key, level_name, level_class in difficulty_levels:
        terms = data.get('terms', {}).get(level_key, [])
        if not terms:
            continue

        section_html = f'''
        <div class="difficulty-section">
            <div class="difficulty-header">
                <span class="difficulty-badge {level_class}">{level_name}</span>
                <span class="difficulty-title">{level_name}术语</span>
            </div>
        '''

        for term in terms:
            term_html = generate_term_card(term)
            section_html += term_html

        section_html += '</div>'
        glossary_html.append(section_html)

    # Replace placeholders
    html = template.replace('{{SUMMARY}}', summary)
    html = html.replace('{{GLOSSARY_SECTIONS}}', '\n'.join(glossary_html))

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return output_path


def generate_term_card(term):
    """Generate HTML for a single term card."""

    name = term.get('name', '')
    is_english = term.get('is_english', False)

    card_html = '<div class="term-card">'

    # Term name
    if is_english:
        card_html += f'<div class="term-name"><span class="english">{name}</span></div>'
    else:
        card_html += f'<div class="term-name">{name}</div>'

    # Pronunciation (for English terms)
    if is_english and term.get('ipa'):
        card_html += f'<div class="pronunciation">{term["ipa"]}</div>'

    if is_english and term.get('chinese_pronunciation'):
        card_html += f'<div class="pronunciation-help">{term["chinese_pronunciation"]}</div>'

    # Explanation
    explanation = term.get('explanation', '')
    if explanation:
        card_html += f'<div class="term-explanation">{explanation}</div>'

    # What it is (for products/people)
    if term.get('what_is'):
        card_html += f'''
        <div class="term-section">
            <div class="term-label">是什么：</div>
            <div class="term-content">{term["what_is"]}</div>
        </div>
        '''

    # Why important (for products/people)
    if term.get('why_important'):
        card_html += f'''
        <div class="term-section">
            <div class="term-label">为什么重要：</div>
            <div class="term-content">{term["why_important"]}</div>
        </div>
        '''

    # Historical context
    if term.get('history'):
        card_html += f'''
        <div class="history">
            <div class="term-label">历史背景：</div>
            <div class="term-content">{term["history"]}</div>
        '''

        if term.get('timeline'):
            card_html += f'<div class="timeline">⏰ {term["timeline"]}</div>'

        card_html += '</div>'

    # Learn more
    card_html += '<div class="learn-more">💬 想了解更多，可以继续对话</div>'

    card_html += '</div>'

    return card_html


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_glossary.py <data.json> <output.html>")
        sys.exit(1)

    data_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    # Get template path
    script_dir = Path(__file__).parent
    template_path = script_dir.parent / 'assets' / 'glossary_template.html'

    # Load data
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Generate HTML
    result = generate_html(data, template_path, output_path)
    print(f"Generated: {result}")


if __name__ == '__main__':
    main()
