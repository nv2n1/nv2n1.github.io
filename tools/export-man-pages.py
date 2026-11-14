#!/usr/bin/env python3
"""Export Linux man pages from the systutorials WordPress DB dump to Hugo MD.

Usage: python3 tools/export-man-pages.py <dump.sql> <man-src-dir>

Reads `wp_posts` INSERT statements from a MariaDB dump, filters the man page
posts (post_name LIKE 'linux-manual-page-<sec>-<name>'), and writes one MD
file per page, sharded by section and first letter:

    <man-src>/<sec>/<letter>/<name>.md

Each file has front matter (title, name, section, url, description) and the
original HTML body with internal systutorials man page links rewritten to the
new /docs/linux/man/<sec>-<name>/ scheme. Also writes _index.md files for the
root and each section, and manifest.jsonl (one JSON object per page) used to
verify the export.
"""

import html
import json
import os
import re
import sys

INSERT_RE = re.compile(r'^INSERT INTO `wp_posts` VALUES (.+);$')
PREFIX = 'linux-manual-page-'
# internal man page links, absolute (with or without www, http or https).
# href names may contain dots or colons while the slugs use dashes; section
# can also be 'n' (tcl/tk) for pages not in this collection.
LINK_RE = re.compile(
    r'https?://(?:www\.)?systutorials\.com/linux-manual-page-([0-9]+[a-z]?|[a-z])-([A-Za-z0-9_.:-]+)/'
)
NAME_RE = re.compile(r'<h2[^>]*>\s*NAME\s*</h2>\s*<p[^>]*>(.*?)</p>', re.S | re.I)
TAG_RE = re.compile(r'<[^>]+>')
H2_RE = re.compile(r'<h2', re.I)

MAN_SECTIONS = {
    '1': 'User commands',
    '2': 'System calls',
    '3': 'Library functions',
    '4': 'Special files',
    '5': 'File formats',
    '6': 'Games',
    '7': 'Miscellaneous',
    '8': 'Administration and privileged commands',
    '9': 'Kernel routines',
}


def parse_rows(s):
    """Parse extended INSERT values into rows of raw string fields."""
    rows = []
    i, n = 0, len(s)
    while i < n:
        if s[i] != '(':
            i += 1
            continue
        i += 1
        row, buf, in_str, k = [], [], False, i
        while k < n:
            c = s[k]
            if in_str:
                if c == '\\':
                    nxt = s[k + 1]
                    esc = {'n': '\n', 'r': '\r', 't': '\t', '0': '\0',
                           'b': '\b', 'Z': '\x1a', '\\': '\\', "'": "'", '"': '"'}
                    buf.append(esc.get(nxt, nxt))
                    k += 2
                    continue
                if c == "'":
                    if k + 1 < n and s[k + 1] == "'":
                        buf.append("'")
                        k += 2
                        continue
                    in_str = False
                    k += 1
                    continue
                buf.append(c)
                k += 1
                continue
            if c == "'":
                in_str = True
                k += 1
                continue
            if c == ',':
                row.append(''.join(buf))
                buf = []
                k += 1
                continue
            if c == ')':
                row.append(''.join(buf))
                break
            buf.append(c)
            k += 1
        i = k
        rows.append(row)
    return rows


def extract_description(content):
    m = NAME_RE.search(content)
    if not m:
        # fallback: the first paragraph before the first heading
        head = content[:H2_RE.search(content).start()] if H2_RE.search(content) else content[:500]
        m = re.match(r'\s*(?:<h1[^>]*>.*?</h1>\s*)?<p[^>]*>(.*?)</p>', head, re.S)
        if not m:
            return ''
    text = html.unescape(TAG_RE.sub('', m.group(1)))
    text = ' '.join(text.split())
    if len(text) > 200:
        text = text[:197] + '...'
    return text


def yaml_str(value):
    return json.dumps(value, ensure_ascii=False)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    dump, out_root = sys.argv[1], sys.argv[2]
    os.makedirs(out_root, exist_ok=True)
    manifest = open(os.path.join(out_root, 'manifest.jsonl'), 'w', encoding='utf-8')
    counts = {}
    written = 0
    skipped = 0

    with open(dump, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            if not line.startswith('INSERT INTO `wp_posts`'):
                continue
            m = INSERT_RE.match(line.rstrip('\n'))
            if not m:
                continue
            for r in parse_rows(m.group(1)):
                if len(r) < 23:
                    continue
                post_name, post_status, post_type = r[11], r[7], r[20]
                if post_type != 'post' or post_status != 'publish' \
                        or not post_name.startswith(PREFIX):
                    continue
                slug = post_name[len(PREFIX):]
                m2 = re.match(r'^([0-9]+[a-z]?)-([a-z0-9_-]+)$', slug)
                if not m2:
                    skipped += 1
                    continue
                sec, name = m2.group(1), m2.group(2)
                content = r[4]
                title = f'{name}({sec})'
                desc = extract_description(content)
                def rewrite(mm):
                    name = mm.group(2).lower().replace('.', '-').replace(':', '-')
                    return f'/docs/linux/man/{mm.group(1)}-{name}/'
                body = LINK_RE.sub(rewrite, content)
                # '{{' in bodies (C++ templates, linker scripts) would be parsed
                # as Hugo shortcodes; entity-encode it, rendering is unchanged.
                body = body.replace('{{', '&#123;&#123;')

                letter = name[0].lower() if name[:1].isalnum() else '0'
                directory = os.path.join(out_root, sec, letter)
                os.makedirs(directory, exist_ok=True)
                path = os.path.join(directory, name + '.md')
                with open(path, 'w', encoding='utf-8') as out:
                    out.write('---\n')
                    out.write(f'title: {yaml_str(title)}\n')
                    out.write(f'name: {yaml_str(name)}\n')
                    out.write(f'section: {yaml_str(sec)}\n')
                    out.write(f'letter: {yaml_str(letter)}\n')
                    out.write(f'url: {yaml_str(f"/docs/linux/man/{sec}-{name}/")}\n')
                    if desc:
                        out.write(f'description: {yaml_str(desc)}\n')
                    out.write('---\n\n')
                    out.write(body)
                    out.write('\n')

                manifest.write(json.dumps({
                    'id': int(r[0] or 0), 'section': sec, 'name': name,
                    'url': f'/docs/linux/man/{sec}-{name}/',
                    'title': title, 'description': desc,
                }, ensure_ascii=False) + '\n')
                counts[sec] = counts.get(sec, 0) + 1
                written += 1
                if written % 10000 == 0:
                    print(f'wrote {written}...', file=sys.stderr, flush=True)

    manifest.close()

    # root index: the man pages landing page
    with open(os.path.join(out_root, '_index.md'), 'w', encoding='utf-8') as out:
        out.write('---\n')
        out.write(f'title: {yaml_str("Linux man pages")}\n')
        out.write('url: /docs/linux/man/\n')
        out.write(f'description: {yaml_str("Online Linux man pages: user commands, system calls, library functions, file formats, and administration commands.")}\n')
        out.write('outputs: [HTML, SearchJSON]\n')
        out.write('layout: man-landing\n')
        out.write('---\n')

    # per-section index pages
    for sec in sorted(counts):
        label = MAN_SECTIONS.get(sec, 'Man pages')
        with open(os.path.join(out_root, sec, '_index.md'), 'w', encoding='utf-8') as out:
            out.write('---\n')
            out.write(f'title: {yaml_str(f"Section {sec}: {label}")}\n')
            out.write(f'sec: {yaml_str(sec)}\n')
            out.write(f'section_label: {yaml_str(label)}\n')
            out.write(f'url: {yaml_str(f"/docs/linux/man/{sec}/")}\n')
            out.write('layout: man-section\n')
            out.write('---\n')

    print(f'done: wrote {written} pages, skipped {skipped}', file=sys.stderr)
    for sec in sorted(counts):
        print(f'  section {sec}: {counts[sec]}', file=sys.stderr)


if __name__ == '__main__':
    main()
