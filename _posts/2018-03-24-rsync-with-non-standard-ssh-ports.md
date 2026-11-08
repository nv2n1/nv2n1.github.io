---
title: "Using Rsync with Non-Standard SSH Ports"
date: 2018-03-24 08:19:58 +0000
layout: post
canonical: https://www.systutorials.com/rsync-with-non-standard-ssh-ports/
---

When you need to rsync against hosts behind NAT gateways or port-forwarded SSH services, the standard port 22 won’t work. The solution is the `-e` flag, which lets you specify a custom SSH command with your desired port.

### Basic usage

Use `-e` to pass custom SSH arguments:

``` bash
rsync -avxP --delete -e "ssh -p 13022" username@example.com:/remote/path/ /local/path/
```

Breaking this down:

- `-a` — archive mode (preserves permissions, timestamps, symlinks)
- `-v` — verbose output
- `-x` — don’t cross filesystem boundaries
- `-P` — show progress and keep partial files
- `--delete` — delete files in destination that don’t exist in source
- `-e "ssh -p 13022"` — use SSH with port 13022 instead of default 22

### Pushing vs pulling

The example above pulls (downloads) from a remote host. To push (upload) instead:

``` bash
rsync -avxP --delete -e "ssh -p 13022" /local/path/ username@example.com:/remote/path/
```

### Additional SSH options

You can pass multiple SSH arguments through the `-e` flag. Common scenarios:

**Using a specific SSH key:**

``` bash
rsync -avxP -e "ssh -p 13022 -i ~/.ssh/custom_key" username@example.com:/remote/path/ /local/path/
```

**Disabling host key verification** (useful for ephemeral test environments, though not recommended for production):

``` bash
rsync -avxP -e "ssh -p 13022 -o StrictHostKeyChecking=no" username@example.com:/remote/path/ /local/path/
```

**Increasing SSH verbosity for debugging:**

``` bash
rsync -avvP -e "ssh -p 13022 -vv" username@example.com:/remote/path/ /local/path/
```

### SSH config alternative

If you frequently connect to the same host, define it in `~/.ssh/config`:

    Host mycluster
        HostName example.com
        Port 13022
        User username
        IdentityFile ~/.ssh/custom_key

Then simplify your rsync command:

``` bash
rsync -avxP --delete mycluster:/remote/path/ /local/path/
```

### Performance considerations

For large transfers over high-latency networks, consider adding compression and tuning parameters:

``` bash
rsync -avxP --delete -e "ssh -p 13022 -C" --bwlimit=5000 username@example.com:/remote/path/ /local/path/
```

- `-C` — enable SSH compression
- `--bwlimit=5000` — limit bandwidth to 5000 KB/s (adjust as needed)

For very large files, you might also want `--partial-dir` to handle incomplete transfers more gracefully:

``` bash
rsync -avxP --delete --partial-dir=.rsync-partial -e "ssh -p 13022" username@example.com:/remote/path/ /local/path/
```

### Troubleshooting

If the connection fails, verify SSH works directly first:

``` bash
ssh -p 13022 username@example.com "ls /remote/path/"
```

Common issues:

- **Permission denied** — check your SSH key permissions (`chmod 600 ~/.ssh/key`) and that the remote user has access
- **Connection refused** — verify the port and that the SSH service is listening on that port (`netstat -tuln | grep 13022` on the remote host)
- **Timeout** — check firewall rules between your client and the port-forwarded gateway

### Summary

The `-e` flag is the standard way to customize rsync’s SSH transport. For cluster environments with non-standard ports, define your hosts in SSH config once, then use clean, repeatable rsync commands without embedding port numbers in every command.

## 2026 Best Practices and Advanced Techniques

For Using Rsync with Non-Standard SSH Ports, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
