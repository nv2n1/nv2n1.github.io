#!/usr/bin/env python3
"""Tag blog posts as short or long by body word count.

Usage: python3 scripts/gen-post-page-length.py <content-dir> <output-dir>

Writes <output-dir>/post-page-length.json mapping each post's `url`
front matter path (e.g. "/how-to-make-tee-catch-the-stderr-only-in-linux/") to:

    "short"  body has fewer than SHORT_MAX words
    "long"   body has SHORT_MAX words or more

The posts single.html layout reads this file through Hugo's .Site.Data and
skips the ad-after-content unit on short pages. Data file is generated at
build time (.github/workflows/pages.yml), not committed.

Run locally: python3 scripts/gen-post-page-length.py content/posts data
"""
import html
import json
import os
import re
import sys

SHORT_MAX = 300  # pages below this many body words count as short

TAG_RE = re.compile(r"<[^>]+>")
URL_RE = re.compile(r'^url:\s*"?([^"\n]+)"?\s*$', re.M)


def page_length(path):
    """Return (url slug, body word count) for one post."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return None, 0
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, 0
    front, body = parts[1], parts[2]
    m = URL_RE.search(front)
    if not m:
        return None, 0
    words = len(TAG_RE.sub(" ", html.unescape(body)).split())
    return m.group(1).strip(), words


def main():
    src_dir, out_dir = sys.argv[1], sys.argv[2]
    tags = {}
    short = long_count = 0
    for dirpath, _, files in os.walk(src_dir):
        for name in sorted(files):
            if not name.endswith(".md") or name == "_index.md":
                continue
            slug, words = page_length(os.path.join(dirpath, name))
            if not slug:
                continue
            if words < SHORT_MAX:
                tags[slug] = "short"
                short += 1
            else:
                tags[slug] = "long"
                long_count += 1
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "post-page-length.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(tags, f, sort_keys=True, separators=(",", ":"))
    print(f"{len(tags)} posts: {short} short, {long_count} long -> {out}")


if __name__ == "__main__":
    main()