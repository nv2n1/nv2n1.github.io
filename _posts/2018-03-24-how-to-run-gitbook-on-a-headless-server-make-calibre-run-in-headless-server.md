---
title: "Running Calibre\u2019s ebook-convert on Headless Servers with Xvfb"
date: 2018-03-24 11:43:34 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-run-gitbook-on-a-headless-server-make-calibre-run-in-headless-server/
---

When GitBook or other tools call Calibre’s `ebook-convert` command on a headless server, you’ll hit this error:

    RuntimeError: X server required. If you are running on a headless machine, use xvfb

This happens because Calibre needs an X11 display server, even though you’re just converting files. The solution is to wrap `ebook-convert` with `xvfb-run`, which provides a virtual framebuffer.

## Why xvfb alone doesn’t work

Simply installing xvfb isn’t enough. Tools like GitBook call `ebook-convert` directly without `xvfb-run`, so Calibre still can’t find a display. You need to intercept those calls.

## The wrapper approach

Create a wrapper script at `/usr/local/bin/ebook-convert` that sits ahead of the real binary in your PATH. When anything calls `ebook-convert`, it’ll actually invoke `xvfb-run` instead.

First, confirm the real `ebook-convert` location:

``` bash
which ebook-convert
```

This is typically `/usr/bin/ebook-convert`. Now create the wrapper:

``` bash
sudo tee /usr/local/bin/ebook-convert > /dev/null << 'EOF'
#!/bin/bash
xvfb-run /usr/bin/ebook-convert "$@"
EOF
```

Make it executable:

``` bash
sudo chmod +x /usr/local/bin/ebook-convert
```

Verify your PATH order puts `/usr/local/bin` first:

``` bash
echo $PATH
```

Test it works:

``` bash
ebook-convert --version
```

## Why this works better than patching GitBook directly

GitBook (or any other tool) has no idea it’s using a wrapper — it just calls `ebook-convert` normally. When you upgrade GitBook, your changes persist because you’re not modifying the application itself. The wrapper is transparent to all callers.

## For containerized deployments

If you’re running in Docker, you can bake this into your image. Add to your Dockerfile:

``` dockerfile
RUN apt-get update && apt-get install -y calibre xvfb

# Create wrapper
RUN mkdir -p /usr/local/bin && \
    echo '#!/bin/bash' > /usr/local/bin/ebook-convert && \
    echo 'xvfb-run /usr/bin/ebook-convert "$@"' >> /usr/local/bin/ebook-convert && \
    chmod +x /usr/local/bin/ebook-convert
```

## Alternative: systemd user service

For more complex scenarios, you could run a persistent xvfb instance via systemd. However, the wrapper approach is simpler for most use cases and avoids managing an additional service.

## Troubleshooting

If `ebook-convert` still complains about X server:

- Confirm `/usr/local/bin` comes before `/usr/bin` in PATH: `echo $PATH`
- Verify the wrapper is being called: `which -a ebook-convert`
- Check wrapper permissions: `ls -l /usr/local/bin/ebook-convert` (should show `x`)
- Test xvfb directly: `xvfb-run glxinfo` (if it works, xvfb is functional)
- Check Calibre installation: `apt list --installed | grep calibre` on Debian/Ubuntu

## Performance notes

Each `xvfb-run` invocation creates and tears down a virtual X server. For batch processing large numbers of files, consider running xvfb once in the background and pointing `DISPLAY` to it, but for typical GitBook workflows, the wrapper overhead is negligible.

## 2026 Best Practices and Advanced Techniques

For Running Calibre’s ebook-convert on Headless Servers with Xvfb, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
