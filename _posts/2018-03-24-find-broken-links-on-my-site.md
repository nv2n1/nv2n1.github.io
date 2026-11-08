---
title: "Check Your Site for Broken Links"
date: 2018-03-24 08:19:46 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /find-broken-links-on-my-site/
---

Over time, internal and external links on your site inevitably break — pages get deleted, domains expire, content moves. Finding and fixing these broken links improves user experience and helps with SEO, since search engines penalize sites with dead links.

## Automated Checking Tools

Several web-based tools can scan your site and report broken links:

- **<a href="https://www.brokenlinkcheck.com/" rel="nofollow noopener" target="_blank">https://www.brokenlinkcheck.com/</a>** — Free tool that crawls your site and identifies dead links. Works well for small to medium sites.
- **<a href="https://www.deadlinkchecker.com/" rel="nofollow noopener" target="_blank">https://www.deadlinkchecker.com/</a>** — Another straightforward checker with a simple interface.
- **Google Search Console** — If your site is indexed, check the Coverage report for crawl errors that indicate unreachable pages.

These tools are convenient if you want a quick scan without setup, but they have limitations: they may timeout on large sites, can’t check authenticated content, and may be throttled if you have many pages.

## Command-Line Approach with wget

For more control, use `wget` locally to crawl your site and identify broken links:

``` bash
wget --spider -r -o /tmp/wget.log http://yoursite.com
grep "HTTP request sent, awaiting response" /tmp/wget.log | grep -E "40[34]|50[0-9]"
```

The `--spider` flag doesn’t actually download files, just checks headers. Broken links return 4xx or 5xx status codes.

For a more detailed report, parse the log more thoroughly:

``` bash
grep "ERROR\|broken link" /tmp/wget.log
```

## Using curl in a Loop

For sites with a known structure, you can script checks with `curl`:

``` bash
#!/bin/bash
urls=(
  "http://yoursite.com/page1"
  "http://yoursite.com/page2"
  "http://yoursite.com/external-link"
)

for url in "${urls[@]}"; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [[ $status =~ ^[45] ]]; then
    echo "BROKEN: $url ($status)"
  else
    echo "OK: $url ($status)"
  fi
done
```

For larger lists, add a timeout and parallel processing:

``` bash
cat urls.txt | parallel -j 4 'curl -s -m 5 -o /dev/null -w "{} %{http_code}\n" {}'
```

This requires `gnu-parallel` but processes 4 URLs concurrently, cutting runtime significantly.

## Checking Links in HTML with mawk or grep

Extract all links from your HTML and test them:

``` bash
grep -oP 'href="\K[^"]+' index.html | while read url; do
  curl -s -m 3 -o /dev/null -w "$url: %{http_code}\n" "$url"
done
```

## Better: Use linkchecker

For comprehensive local checking, install `linkchecker`:

``` bash
# Debian/Ubuntu
sudo apt install linkchecker

# Fedora/RHEL
sudo dnf install linkchecker
```

Then run it against your site:

``` bash
linkchecker -r 10 http://yoursite.com
```

The `-r 10` limits recursion depth. Output shows broken links, timeouts, and redirects. You can generate an HTML report:

``` bash
linkchecker -r 5 --output=html http://yoursite.com > report.html
```

`linkchecker` respects `robots.txt`, handles authentication, and can check FTP links too. It’s slower than `wget` but more thorough.

## Monitoring Redirects and Status Codes

Watch for redirect chains, which can slow your site:

``` bash
curl -w "Redirects: %{num_redirects}\n" -L http://yoursite.com
```

Check for mixed content warnings:

``` bash
curl -I https://yoursite.com | grep -i "upgrade-insecure"
```

## Integration with CI/CD

For ongoing monitoring, add link checking to your deployment pipeline. A simple GitHub Actions example:

``` yaml
name: Check Links
on: [push, pull_request]
jobs:
  linkcheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: |
          sudo apt install linkchecker
          linkchecker -r 3 http://localhost &
          sleep 2
          linkchecker --output=json http://localhost > report.json
```

## Best Practices

- **Automate regularly** — Schedule checks weekly or monthly depending on how often you add content.
- **Test before publishing** — Use `linkchecker` locally on staged content to catch broken links before going live.
- **Update external links** — External links break due to third-party changes. Audit these annually.
- **Set up monitoring** — Tools like Uptime Robot can monitor critical pages for 404s.
- **Use redirects wisely** — When moving pages, 301 redirect old URLs rather than letting them break.

For most sysadmins managing web infrastructure, combining `wget` or `linkchecker` with periodic automated checks provides reliable broken link detection without external dependencies.
