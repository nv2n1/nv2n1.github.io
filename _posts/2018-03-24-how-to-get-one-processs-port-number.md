---
title: "How to Get a Process\u2019s Port Number"
date: 2018-03-24 11:54:46 +0000
modified: 2026-04-12 16:33:10 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /how-to-get-one-processs-port-number/
---

Identifying which ports a specific process is using comes up regularly in debugging, security audits, and infrastructure management. Here are the practical methods.

## Using ss

The `ss` command is the modern standard for socket inspection:

``` bash
ss -tlnp | grep <PID>
```

This shows listening TCP sockets (`-t` for TCP, `-l` for listening). Add `-u` if you need UDP ports too:

``` bash
ss -tlnup | grep <PID>
```

The flags break down as:

- `-t` / `-u`: TCP / UDP protocols
- `-l`: listening sockets only
- `-n`: numeric output (no service name lookups)
- `-p`: show the process name and PID

If you know the process name but not the PID, combine it with `pgrep`:

``` bash
ss -tlnp | grep $(pgrep -f nginx)
```

For all sockets (not just listening), drop the `-l`:

``` bash
ss -tnp | grep <PID>
```

## Using lsof

`lsof` (list open files) also works, though it’s typically slower on systems with many connections:

``` bash
lsof -i -P -n | grep <PID>
```

Flags:

- `-i`: show network sockets
- `-P`: numeric ports (no service names)
- `-n`: numeric addresses (no DNS lookups)

You can also be more specific with protocol and port:

``` bash
lsof -i :8080
lsof -i TCP:3306
```

This approach is useful when you know the port and want to find what’s using it.

## Checking Ports by Name

If you only have the process name:

``` bash
ss -tlnp | grep nginx
```

Or with lsof:

``` bash
lsof -i -P -n | grep postgres
```

## In Containers

For Docker containers, inspect port mappings with:

``` bash
docker port <container_id>
docker inspect <container_id> | grep -A 5 PortBindings
```

In Kubernetes, check service-to-pod port mappings:

``` bash
kubectl get svc <service_name> -o wide
kubectl get pods <pod_name> -o jsonpath='{.spec.containers[*].ports}'
```

If you need to see ports from inside a container, the same `ss` and `lsof` commands work—just exec in:

``` bash
docker exec <container_id> ss -tlnp
kubectl exec <pod_name> -- ss -tlnp
```

## Common Scenarios

**Find what’s using a specific port:**

``` bash
ss -tlnp | grep :8080
lsof -i :8080
```

**List all listening ports for a service:**

``` bash
systemctl show -p MainPID <service_name> | cut -d= -f2 | xargs -I {} ss -tlnp | grep {}
```

Or simpler, if systemd integration is enabled:

``` bash
ss -tlnp | grep <service_name>
```

**Monitor connections to a port in real-time:**

``` bash
watch -n 1 'ss -tnp | grep :8080'
```

## Why ss Over netstat

`ss` is significantly faster than the deprecated `netstat` on systems with thousands of connections. It queries `/proc` directly and scales better with modern workloads. If you’re still using `netstat`, migrate to `ss`—the command syntax is nearly identical.

## 2026 Best Practices and Advanced Techniques

For How to Get a Process’s Port Number, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
