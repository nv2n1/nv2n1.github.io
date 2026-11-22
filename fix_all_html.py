#!/usr/bin/env python3
"""
Fix all HTML issues across all markdown files:
1. <br /> -> <br/> (self-closing BR tags)
2. <FONT SIZE="...">text</FONT> -> text (remove FONT tags, keep content)
3. <font SIZE="...">text</font> -> text (case insensitive)
"""
import os
import re
import sys

BR_PATTERN = re.compile(r'<br\s*/\s*>', re.IGNORECASE)
FONT_PATTERN = re.compile(r'<font\s+size\s*=\s*["\']?[^"\'>\s]+["\']?\s*>(.*?)</font>', re.IGNORECASE | re.DOTALL)
FONT_SIMPLE = re.compile(r'<font\s+size\s*=\s*["\']?[^"\'>\s]+["\']?\s*>', re.IGNORECASE)

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    # Fix <br /> -> <br/>
    br_matches = list(BR_PATTERN.finditer(content))
    if br_matches:
        content = BR_PATTERN.sub('<br/>', content)
        changes += len(br_matches)
    
    # Fix <FONT SIZE="...">text</FONT> -> text
    font_matches = list(FONT_PATTERN.finditer(content))
    if font_matches:
        content = FONT_PATTERN.sub(r'\1', content)
        changes += len(font_matches)
    
    # Also remove any stray <font> or </font> tags that weren't caught
    # (in case they're not paired properly)
    stray_open = len(re.findall(r'<font\s+[^>]*>', content, re.IGNORECASE))
    stray_close = len(re.findall(r'</font>', content, re.IGNORECASE))
    if stray_open > 0:
        content = re.sub(r'<font\s+[^>]*>', '', content, flags=re.IGNORECASE)
        changes += stray_open
    if stray_close > 0:
        content = re.sub(r'</font>', '', content, flags=re.IGNORECASE)
        changes += stray_close
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return 0

def main():
    if len(sys.argv) > 1:
        # Process specific files
        total_changes = 0
        for filepath in sys.argv[1:]:
            if os.path.exists(filepath):
                c = fix_file(filepath)
                if c > 0:
                    print(f"Fixed {c} issues in {filepath}")
                total_changes += c
        print(f"\nTotal changes: {total_changes}")
    else:
        # Process all markdown files
        total_files = 0
        total_changes = 0
        fixed_files = 0
        
        for root in ['man-src', 'content/posts', 'content', 'content/redirects', 'content/archive']:
            if not os.path.exists(root):
                continue
            for dirpath, dirnames, filenames in os.walk(root):
                for filename in filenames:
                    if filename.endswith('.md'):
                        filepath = os.path.join(dirpath, filename)
                        total_files += 1
                        c = fix_file(filepath)
                        if c > 0:
                            fixed_files += 1
                            total_changes += c
                            print(f"Fixed {c} issues in {filepath}")
        
        print(f"\nTotal files: {total_files}")
        print(f"Files fixed: {fixed_files}")
        print(f"Total changes: {total_changes}")

if __name__ == '__main__':
    main()