#!/usr/bin/env python3
"""Generate category pages, redirect stubs, and the categories index from
_data/topics.yml and the current post tags.

Usage: python3 scripts/gen-category-pages.py
"""

import collections
import glob
import os
import re

import yaml  # pip: pyyaml


def post_count_by_category():
    counts = collections.Counter()
    for path in glob.glob('_posts/*.md'):
        with open(path, encoding='utf-8') as f:
            m = re.search(r'^categories: \[([a-z0-9-]+)', f.read(), re.M)
        if m:
            counts[m.group(1)] += 1
    return counts


def category_page(cat, meta, parents, n):
    title = meta['title']
    lines = [
        '---',
        'layout: home',
        f'title: "{title}"',
        f'category: {cat}',
        f'permalink: /category/{cat}/',
        '---',
        '',
        f'# {title}',
        '',
        'Part of ' + ' > '.join(f'[{p["title"]}]({p["url"]})' for p in parents) + '.',
        '',
        f'{n} posts.',
        '',
        '{% assign posts = site.categories[page.category] | sort: date | reverse %}',
        '<ul class="posts">',
        '{% for post in posts %}',
        '  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>',
        '{% endfor %}',
        '</ul>',
        '',
    ]
    with open(f'category/{cat}.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def redirect_page(old_slug, title, target):
    lines = [
        '---',
        'layout: redirect',
        f'title: "{title}"',
        f'permalink: /category/{old_slug}/',
        f'redirect_to: {target}',
        '---',
        '',
    ]
    with open(f'category/{old_slug}.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


REDIRECTS = {
    'languages-frameworks': ('Languages & Frameworks', '/category/programming-languages/'),
    'object-oriented-programming': ('Object-Oriented Programming', '/category/programming-languages/'),
    'functional-programming': ('Functional Programming', '/category/programming-languages/'),
    'code-optimization': ('Code Optimization', '/category/algorithms-data-structures/'),
    'design-patterns-architecture': ('Design Patterns & Architecture', '/category/software-design/'),
    'development-best-practices': ('Development Best Practices', '/category/software-design/'),
    'systems-architecture': ('Systems Architecture', '/advanced-systems-path/'),
    'scripting-utilities': ('Scripting & Utilities', '/category/shell-scripting/'),
    'security-cryptography-2': ('Security & Cryptography', '/security-cryptography-path/'),
    'blockchain-cryptocurrency': ('Blockchain & Cryptocurrency', '/web3-crypto-academy/'),
    'ai-engineering': ('AI Engineering', '/ai-engineering-hub/'),
    'linux-systems-administration': ('Linux Systems Administration', '/linux-sysadmin-path/'),
    'linux-system-configuration': ('Linux System Configuration', '/linux-essentials-path/'),
    'system-administration-cloud': ('System Administration & Cloud', '/linux-sysadmin-path/'),
}


def main():
    with open('_data/topics.yml', encoding='utf-8') as f:
        topics = yaml.safe_load(f)
    counts = post_count_by_category()

    # every category must exist in the map, and have a parent
    for cat in counts:
        assert cat in topics['categories'], f'category not in topics.yml: {cat}'

    os.makedirs('category', exist_ok=True)

    # category pages for categories with posts
    for cat, meta in topics['categories'].items():
        n = counts.get(cat, 0)
        if n == 0:
            continue
        parents = []
        path = topics['paths'].get(meta.get('path'))
        if path:
            parents.append(topics['academies'][path['academy']])
            parents.append(path)
        else:
            parents.append(topics['academies'][meta['academy']])
        category_page(cat, meta, parents, n)
        print(f'category/{cat}.md  ({n} posts)')

    # redirects for retired category slugs
    for old, (title, target) in REDIRECTS.items():
        redirect_page(old, title, target)
        print(f'category/{old}.md -> {target}')


if __name__ == '__main__':
    main()
