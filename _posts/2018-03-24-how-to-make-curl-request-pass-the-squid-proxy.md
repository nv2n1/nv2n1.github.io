---
title: "Squid Proxy Blocking curl POST Requests With Expect: 100-continue"
date: 2018-03-24 11:47:11 +0000
modified: 2026-04-12 16:57:50 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-curl-request-pass-the-squid-proxy/
---

When sending POST requests through a Squid proxy with curl, you may encounter a proxy error that blocks the request, even though the same request works fine with GET. The issue typically appears as:

    ERROR
    The requested URL could not be retrieved

The root cause is the `Expect: 100-continue` header that curl automatically adds to POST requests with a body. Many Squid proxy configurations don’t support this header, causing the request to be rejected before it even reaches your destination server.

## Why GET works but POST doesn’t

When you switch from POST to GET:

``` bash
# This fails (POST with body)
curl http://example.com/send --data-urlencode "data=hello"

# This works (GET with query string)
curl -G http://example.com/send --data-urlencode "data=hello"
```

The difference is that GET requests don’t include the `Expect: 100-continue` header. curl adds this header to POST requests with a body to ask the server “should I send this large request?” before transmitting it. Squid doesn’t handle this negotiation properly and blocks the request.

## Solution: Remove the Expect header

The simplest fix is to explicitly remove the `Expect` header from your curl command:

``` bash
curl http://example.com/send -H "Expect:" --data-urlencode "data=hello"
```

The empty `Expect:` header tells curl to remove that header entirely from the request.

## Using curl options instead of -H

For better clarity, you can also use curl’s built-in option:

``` bash
curl http://example.com/send --data-urlencode "data=hello" -H "Expect:"
```

Or if you want to handle multiple headers, keep them grouped:

``` bash
curl http://example.com/send \
  --data-urlencode "data=hello" \
  -H "Expect:" \
  -H "User-Agent: MyApp/1.0"
```

## In libcurl C code

If you’re using libcurl in your application:

``` c
CURL *curl = curl_easy_init();
struct curl_slist *headers = NULL;

// Remove the Expect header
headers = curl_slist_append(headers, "Expect:");
curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

// Set your POST data
curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "data=hello");
curl_easy_setopt(curl, CURLOPT_URL, "http://example.com/send");

// Perform the request
curl_perform(curl);

// Clean up
curl_slist_free_all(headers);
curl_easy_cleanup(curl);
```

## In Python with requests

If you’re using the Python `requests` library, you can set headers similarly:

``` python
import requests

headers = {"Expect": ""}
response = requests.post(
    "http://example.com/send",
    data={"data": "hello"},
    headers=headers,
    proxies={"http": "http://proxy-server:3128"}
)
```

Or with urllib:

``` python
import urllib.request

req = urllib.request.Request(
    "http://example.com/send",
    data=b"data=hello",
    headers={"Expect": ""}
)

proxy_handler = urllib.request.ProxyHandler(
    {"http": "http://proxy-server:3128"}
)
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(req)
```

## Additional Squid proxy configuration considerations

If you control the Squid proxy, you can also configure it to handle Expect headers properly. Add this to your `squid.conf`:

    # Allow 100-continue for proper handling
    ignore_expect_100 off

However, for most users on corporate networks, modifying proxy settings isn’t an option, so removing the header from your client is the practical solution.

## When to use this workaround

This fix is necessary when:

- You’re behind a corporate or ISP Squid proxy
- POST requests are being blocked but GET requests work
- You see 407 Proxy Authentication Required or similar errors with POST
- You don’t have control over the proxy configuration

The `Expect:` header removal has no negative side effects for most modern servers and is safe to apply universally to requests going through proxies.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Squid Proxy Blocking curl POST Requests With Expect: 100-continue with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Squid Proxy Blocking curl POST Requests With Expect: 100-continue. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
