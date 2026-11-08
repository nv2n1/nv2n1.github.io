---
title: "Converting HTML to Plain Text in PHP"
date: 2018-03-24 11:53:54 +0000
modified: 2026-04-12 16:36:28 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-convert-a-piece-of-html-code-to-plain-text-in-php/
---

HTML to plain text conversion is a common task in PHP applications — whether you’re sanitizing user input, preparing content for email, generating text previews, or creating searchable indexes. Here are the practical approaches.

## Using strip_tags()

The simplest method is PHP’s built-in `strip_tags()` function:

``` php
$html = '<p>Hello <strong>world</strong>!</p>';
$text = strip_tags($html);
echo $text; // Output: Hello world!
```

You can preserve specific tags by passing them as a second argument:

``` php
$html = '<p>Hello <strong>world</strong>!</p>';
$text = strip_tags($html, '<strong>');
echo $text; // Output: Hello <strong>world</strong>!
```

This works for simple cases, but has limitations. It removes HTML tags without handling entities, whitespace collapsing, or nested structures intelligently.

## Using DOM Methods

For more control, use PHP’s DOM extension to parse and traverse HTML properly:

``` php
$html = '<div><p>First paragraph</p><p>Second paragraph</p></div>';
$dom = new DOMDocument();
$dom->loadHTML($html);
$text = $dom->textContent;
echo $text; // Output: First paragraphSecond paragraph
```

This preserves the document structure but loses whitespace between elements. To maintain readability:

``` php
$html = '<div><p>First paragraph</p><p>Second paragraph</p></div>';
$dom = new DOMDocument();
$dom->loadHTML($html);

$xpath = new DOMXPath($dom);
$text = '';

foreach ($xpath->query('//text()') as $node) {
    $text .= trim($node->textContent) . ' ';
}

$text = trim($text);
echo $text; // Output: First paragraph Second paragraph
```

## Using strip_tags() with HTML Entities

When HTML contains special characters, combine `strip_tags()` with `html_entity_decode()`:

``` php
$html = '<p>Price: &pound;50 &amp; free shipping</p>';
$text = html_entity_decode(strip_tags($html), ENT_QUOTES | ENT_HTML5, 'UTF-8');
echo $text; // Output: Price: £50 & free shipping
```

## Using Regular Expressions

For quick conversions on simple HTML, regex works but is fragile for complex documents:

``` php
$html = '<p>Hello</p><br><span>world</span>';
$text = preg_replace('/<[^>]*>/', '', $html);
echo $text; // Output: Helloworld
```

This doesn’t handle entities or whitespace preservation.

## Using Third-Party Libraries

For production code handling untrusted HTML, use established libraries:

**PHP Simple HTML DOM Parser:**

``` php
require_once 'simple_html_dom.php';
$html = file_get_html('<p>Test content</p>');
$text = $html->plaintext;
echo $text;
```

**Symfony DomCrawler:**

``` php
use Symfony\Component\DomCrawler\Crawler;

$crawler = new Crawler('<p>Test content</p>');
$text = $crawler->text();
echo $text;
```

**LeagueHTML to Markdown:**

``` php
use League\HTMLToMarkdown\HtmlConverter;

$converter = new HtmlConverter();
$markdown = $converter->convert('<p>Bold <strong>text</strong></p>');
```

## Handling Edge Cases

**Removing extra whitespace:**

``` php
$text = preg_replace('/\s+/', ' ', strip_tags($html));
$text = trim($text);
```

**Preserving line breaks:**

``` php
$html = '<p>Line one</p><p>Line two</p>';
$text = str_replace('</p>', "\n", strip_tags($html));
$text = trim($text);
// Output: Line one\nLine two
```

**Scripts and styles:**

``` php
$html = '<p>Content</p><script>alert("hi")</script>';
$text = preg_replace('/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/i', '', $html);
$text = strip_tags($text);
```

## Choosing Your Approach

Use `strip_tags()` for simple, trusted HTML. Use the DOM extension or third-party libraries when handling complex documents or untrusted input. Always validate and sanitize user-provided HTML before processing, especially if it will be displayed elsewhere.

## 2026 Best Practices and Advanced Techniques

For Converting HTML to Plain Text in PHP, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
