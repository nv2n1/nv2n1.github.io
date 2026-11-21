#!/usr/bin/env python3
"""
Fix man page markdown files by removing NAME/SYNOPSIS/DESCRIPTION headings
that are redundant with the page title and header structure.
"""
import os
import re

def fix_man_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    front_matter = parts[1]
    body = parts[2].lstrip('\n')

    # Remove the first occurrence of each heading
    # Pattern: <h2 class="name">NAME</h2>\n<p>...</p> -> <p>...</p>
    # Pattern: <h2>SYNOPSIS</h2> -> (remove)
    # Pattern: <h2>DESCRIPTION</h2> -> (remove)

    original_body = body

    # Remove NAME heading (with class="name") - keep the following paragraph
    body = re.sub(r'<h2 class="name">NAME</h2>\s*', '', body, count=1)

    # Remove SYNOPSIS heading (first occurrence) - keep following content
    body = re.sub(r'<h2>SYNOPSIS</h2>\s*', '', body, count=1)

    # Remove DESCRIPTION heading (first occurrence) - keep following content
    body = re.sub(r'<h2>DESCRIPTION</h2>\s*', '', body, count=1)

    if body != original_body:
        new_content = f'---\n{front_matter}---\n\n{body}'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    man_src_dir = 'man-src'
    fixed_count = 0

    for root, dirs, files in os.walk(man_src_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if fix_man_page(filepath):
                    fixed_count += 1
                    print(f"Fixed: {filepath}")

    print(f"\nTotal fixed: {fixed_count}")

if __name__ == '__main__':
    main()