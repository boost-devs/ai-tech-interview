#!/usr/bin/env python3
"""Convert GitHub markdown syntax to GitBook-compatible syntax.

Transformations:
1. Inline math: $...$ → $$...$$
2. Callouts: > [!TIP/WARNING/...] → {% hint style="..." %}
3. TOC anchors: (#N) → (#id-N)
"""

import re
import os


def convert_inline_math(content):
    """Convert $...$ inline math to $$...$$ for GitBook.
    Skips code blocks and already-converted $$...$$ expressions.
    """
    # Split by fenced code blocks and inline code to avoid modifying them
    parts = re.split(r'(```[\s\S]*?```|`[^`\n]+`)', content)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Non-code section
            part = re.sub(
                r'(?<!\$)\$(?!\$)([^\n$]+?)(?<!\$)\$(?!\$)',
                r'$$\1$$',
                part
            )
        result.append(part)
    return ''.join(result)


def convert_callouts(content):
    """Convert GitHub [!TYPE] callouts to GitBook hint blocks.

    GitHub:
        > [!TIP]
        > content

    GitBook:
        {% hint style="info" %}
        content
        {% endhint %}
    """
    style_map = {
        'TIP': 'info',
        'NOTE': 'info',
        'WARNING': 'warning',
        'IMPORTANT': 'warning',
        'CAUTION': 'danger',
    }

    def replace_callout(match):
        callout_type = match.group(1).upper()
        body = match.group(2)
        lines = re.sub(r'^> ?', '', body, flags=re.MULTILINE).strip()
        style = style_map.get(callout_type, 'info')
        return f'{{% hint style="{style}" %}}\n{lines}\n{{% endhint %}}'

    pattern = r'> \[!(\w+)\]\s*\n((?:>[ \t]?[^\n]*\n)*)'
    return re.sub(pattern, replace_callout, content)


def convert_toc_anchors(content):
    """Convert (#N) TOC links to (#id-N) for GitBook anchor compatibility.

    GitBook generates 'id-N' anchors for headings like '## #N'.
    """
    return re.sub(r'\(#(\d+)\)', r'(#id-\1)', content)


def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = convert_inline_math(content)
    content = convert_callouts(content)
    content = convert_toc_anchors(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Converted: {filepath}')


def main():
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in files:
            if filename.endswith('.md'):
                convert_file(os.path.join(root, filename))


if __name__ == '__main__':
    main()
