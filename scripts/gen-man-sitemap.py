#!/usr/bin/env python3
"""Generate a chunked sitemap for the Hugo-built man pages.

Usage: python3 scripts/gen-man-sitemap.py <built-docs-dir> <output-dir>

The man site has ~56k pages, over the 50k URL sitemap limit, so this writes
a sitemap index plus chunk files:

    <output-dir>/sitemap.xml       index of the chunks
    <output-dir>/sitemap-N.xml     <=40k URLs each

Run after `hugo` and before uploading the Pages artifact; the workflow wires
it as: python3 scripts/gen-man-sitemap.py _man_out/docs _site/docs
"""
import os, sys

BASE = "https://www.systutorials.com/docs"
MAX_URLS = 40000

def main():
    docs_dir, out_dir = sys.argv[1], sys.argv[2]
    urls = []
    for dirpath, _, files in os.walk(docs_dir):
        if "index.html" in files:
            rel = os.path.relpath(dirpath, docs_dir).replace(os.sep, "/")
            urls.append("/" if rel == "." else "/" + rel + "/")
    urls.sort()

    os.makedirs(out_dir, exist_ok=True)
    chunks = [urls[i:i + MAX_URLS] for i in range(0, len(urls), MAX_URLS)]
    for n, chunk in enumerate(chunks, 1):
        with open(os.path.join(out_dir, f"sitemap-{n}.xml"), "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            for u in chunk:
                f.write(f"  <url><loc>{BASE}{u}</loc></url>\n")
            f.write("</urlset>\n")
    with open(os.path.join(out_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for n in range(1, len(chunks) + 1):
            f.write(f"  <sitemap><loc>{BASE}/docs/sitemap-{n}.xml</loc></sitemap>\n")
        f.write("</sitemapindex>\n")
    print(f"man sitemap: {len(urls)} URLs in {len(chunks)} chunks -> {out_dir}")

if __name__ == "__main__":
    main()
