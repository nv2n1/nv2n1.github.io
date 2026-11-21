#!/usr/bin/env python3
"""
Fix man page markdown files by removing a leading subtitle heading.

Rule: drop the first h2 heading ONLY if
  1. its text is one of NAME, INTRO, INTRODUCTION, DESCRIPTION, SYNOPSIS
     (case-insensitive), and
  2. the page body does not already start with meaningful text before it —
     i.e. the heading is the very first content, so removing it makes the
     page start with text instead of a redundant subtitle.

Pages whose body already begins with a text paragraph keep all their
headings: the leading paragraph is the (unheaded) name/subtitle, and the
following h2s are informative section headers that must stay.
"""
import os
import re
import sys

TARGET_HEADINGS = {'NAME', 'INTRO', 'INTRODUCTION', 'DESCRIPTION', 'SYNOPSIS'}

H2_TARGET_PATTERN = re.compile(
    r'<h2[^>]*>\s*(NAME|INTRO|INTRODUCTION|DESCRIPTION|SYNOPSIS)\s*</h2>',
    re.IGNORECASE,
)
FIRST_H2_PATTERN = re.compile(r'<h2[^>]*>')


def _has_meaningful_text(html: str) -> bool:
    """Return True if html contains meaningful visible text (not just tags,
    whitespace, entities like <br/>, or stray closing tags)."""
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'&[a-zA-Z0-9#]+;', ' ', text)
    # Remove slashes left from self-closing tags like "<br/>" -> "br/"
    text = text.replace('/', ' ')
    return len(re.sub(r'\s+', '', text)) > 3


def fix_man_page(filepath, verbose=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split front matter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    front_matter = parts[1]
    body = parts[2].lstrip('\n')

    original_body = body

    # Remove stray </p> at the beginning of body (after front matter)
    body = re.sub(r'^\s*</p>\s*', '', body, count=1)

    match = H2_TARGET_PATTERN.search(body)
    if match:
        heading_text = match.group(1)

        # Must be the FIRST h2 in the body
        first_h2_match = FIRST_H2_PATTERN.search(body)
        if first_h2_match and first_h2_match.start() == match.start():
            # Only remove when the page does NOT already start with text:
            # a leading paragraph means the subtitle content is already
            # visible and this heading is an informative section header.
            if not _has_meaningful_text(body[:match.start()]):
                body = body[:match.start()] + body[match.end():]
                # Trim leading whitespace/newlines after the removed tag
                body = re.sub(r'^\s+', '', body, count=1)
                if verbose:
                    print(f"  Removed leading h2: {heading_text}")

    if body != original_body:
        new_content = f'---\n{front_matter}---\n\n{body}'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def main():
    quiet = '-q' in sys.argv
    paths = [a for a in sys.argv[1:] if a != '-q']

    if paths:
        # Process specific files
        fixed_count = 0
        for filepath in paths:
            if fix_man_page(filepath, verbose=not quiet):
                fixed_count += 1
                if not quiet:
                    print(f"Fixed: {filepath}")
        print(f"\nTotal fixed: {fixed_count}")
    else:
        # Process all man-src files
        man_src_dir = 'man-src'
        fixed_count = 0
        total = 0

        for root, dirs, files in os.walk(man_src_dir):
            for file in files:
                if file.endswith('.md'):
                    total += 1
                    filepath = os.path.join(root, file)
                    if fix_man_page(filepath, verbose=not quiet):
                        fixed_count += 1
                        if not quiet and fixed_count % 500 == 0:
                            print(f"... {fixed_count} fixed so far")

        print(f"\nTotal fixed: {fixed_count} out of {total} files")


if __name__ == '__main__':
    main()
