---
title: "URL-Encoding Spaces in curl GET Requests"
date: 2018-03-24 11:47:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-encode-spaces-in-curl-get-request-url-on-linux/
---

When you run a curl GET request with spaces in the query string, the shell interprets the space as a separator and truncates the URL:

``` bash
curl "http://example.com/send?msg=hello world"
```

The space causes the shell to treat `world` as a separate argument, so only `hello` gets sent. You need to properly URL-encode the space (and other special characters) as `%20`.

## Using –data-urlencode with -G

The cleanest approach is combining `-G` (GET request) with `--data-urlencode`:

``` bash
curl -G "http://example.com/send" --data-urlencode "msg=hello world"
```

The `-G` flag tells curl to append the encoded data to the URL as query parameters instead of sending it as POST data. The `--data-urlencode` option handles the URL encoding automatically.

## –data-urlencode Syntax

The `--data-urlencode` option supports several formats:

**Simple value encoding:**

``` bash
curl -G "http://example.com/search" --data-urlencode "query=linux sysadmin"
```

**Multiple parameters:**

``` bash
curl -G "http://example.com/api" \
  --data-urlencode "name=John Doe" \
  --data-urlencode "role=Senior Admin"
```

**With special characters:**

``` bash
curl -G "http://example.com/post" --data-urlencode "text=Hello & goodbye!"
```

All special characters (`&`, `=`, `+`, `#`, etc.) get properly encoded.

**Loading from a file:**

``` bash
curl -G "http://example.com/upload" --data-urlencode "@data.txt"
```

## Manual URL Encoding

If you prefer to manually encode the URL, use `%20` for spaces:

``` bash
curl "http://example.com/send?msg=hello%20world"
```

For complex queries with multiple special characters, this gets tedious and error-prone. Use `--data-urlencode` instead.

## Alternative: URL Encoding with printf

You can also use shell utilities to encode the string before passing it to curl:

``` bash
encoded=$(printf '%s\n' "hello world" | jq -sRr @uri)
curl "http://example.com/send?msg=${encoded}"
```

Or with `sed` for a lighter approach:

``` bash
msg="hello world"
encoded=$(echo "$msg" | sed 's/ /%20/g')
curl "http://example.com/send?msg=${encoded}"
```

These manual approaches are useful in scripts, but `--data-urlencode` remains the most reliable and readable method.

## Real-World Example

Suppose you’re querying an API that requires multiple parameters with spaces:

``` bash
curl -G "https://api.example.com/search" \
  --data-urlencode "q=kubernetes deployment best practices" \
  --data-urlencode "category=DevOps" \
  --data-urlencode "limit=10"
```

This produces: `https://api.example.com/search?q=kubernetes%20deployment%20best%20practices&category=DevOps&limit=10`

## Key Takeaways

- Always quote your URLs to prevent shell interpretation
- Use `-G` with `--data-urlencode` for reliable GET request parameter handling
- `--data-urlencode` handles all special character encoding automatically
- This approach is cleaner and less error-prone than manual URL encoding in scripts

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
