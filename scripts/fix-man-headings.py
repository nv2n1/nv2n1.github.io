#!/usr/bin/env python3
"""
Fix man page markdown files by removing first h2 heading if it's
one of: NAME, INTRO, INTRODUCTION, DESCRIPTION, SYNOPSIS
"""
import os
import re
import sys

TARGET_HEADINGS = {'NAME', 'INTRO', 'INTRODUCTION', 'DESCRIPTION', 'SYNOPSIS'}

def fix_man_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    front_matter = parts[1]
    body = parts[2].lstrip('\n')

    original_body = body

    # Find the first h2 heading in the body
    # Pattern matches <h2 ...>NAME</h2> or <h2>SYNOPSIS</h2> etc.
    h2_pattern = r'(<h2[^>]*>\s*(NAME|INTRO|INTRODUCTION|DESCRIPTION|SYNOPSIS)\s*</h2>)'
    
    match = re.search(h2_pattern, body)
    if match:
        full_tag = match.group(1)
        heading_text = match.group(2)
        
        if heading_text in TARGET_HEADINGS:
            # Check if this is the FIRST h2 in the body
            first_h2_match = re.search(r'<h2[^>]*>', body)
            if first_h2_match and first_h2_match.start() == match.start():
                # This is the first h2 and it's a target heading - remove it
                body = body[:match.start()] + body[match.end():]
                # Also remove any trailing whitespace/newlines after the removed tag
                body = re.sub(r'^\s+', '', body, count=1)
                print(f"  Removed first h2: {heading_text}")

    if body != original_body:
        new_content = f'---\n{front_matter}---\n\n{body}'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    if len(sys.argv) > 1:
        # Process specific files
        fixed_count = 0
        for filepath in sys.argv[1:]:
            if fix_man_page(filepath):
                fixed_count += 1
                print(f"Fixed: {filepath}")
        print(f"\nTotal fixed: {fixed_count}")
    else:
        # Process all man-src files
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