---
title: "Mounting Remote Folders via SSH with SSHFS"
date: 2013-07-12 16:32:02 +0000
modified: 2026-04-12 16:40:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /mounting-remote-folder-through-ssh/
---

`sshfs` is the standard tool for mounting remote filesystems over SSH. It’s available in most distribution repositories.

**Debian/Ubuntu:**

``` bash
sudo apt install sshfs
```

**RHEL/CentOS/Fedora:**

``` bash
sudo dnf install sshfs
```

**Alpine:**

``` bash
apk add sshfs
```

On some systems you may need to ensure the `fuse` kernel module is loaded:

``` bash
sudo modprobe fuse
```

## Basic Mount

Mount a remote directory to a local mount point:

``` bash
sshfs username@server:/path/to/folder /path/to/mount/point
```

The mount point must exist. Create it if needed:

``` bash
mkdir -p /path/to/mount/point
```

Verify the mount:

``` bash
mount | grep sshfs
df -h /path/to/mount/point
```

## Common Options

Pass additional flags to customize the mount behavior:

``` bash
sshfs -o allow_other,default_permissions username@server:/path/to/folder /path/to/mount/point
```

Useful options:

- `allow_other` — allows other users to access the mount
- `default_permissions` — enforces standard Unix permissions
- `IdentityFile=/path/to/key` — use a specific SSH key
- `port=2222` — connect to non-standard SSH port
- `compression=yes` — enable SSH compression (useful for slow links)
- `reconnect` — automatically reconnect on connection loss
- `ServerAliveInterval=15` — send keepalive packets every 15 seconds
- `uid=1000,gid=1000` — set ownership of mounted files

Example with multiple options:

``` bash
sshfs -o IdentityFile=~/.ssh/id_ed25519,port=2222,compression=yes,reconnect \
  username@server:/path/to/folder /path/to/mount/point
```

## Using SSH Config

If you have SSH hosts defined in `~/.ssh/config`, you can reference them directly:

``` bash
sshfs myserver:/path/to/folder /path/to/mount/point
```

This is cleaner than repeating connection details each time.

## Unmounting

Unmount using `fusermount`:

``` bash
fusermount -u /path/to/mount/point
```

Force unmount if the mount is busy:

``` bash
fusermount -uz /path/to/mount/point
```

Or use standard `umount` on most modern systems:

``` bash
sudo umount /path/to/mount/point
```

## Persistent Mounts

To mount at boot, add an entry to `/etc/fstab`:

```fstab
username@server:/path/to/folder /path/to/mount/point fuse.sshfs defaults,IdentityFile=/home/user/.ssh/id_ed25519,allow_other,reconnect,ServerAliveInterval=15 0 0
```

Then mount all entries:

``` bash
sudo mount -a
```

Or mount just that entry:

``` bash
sudo mount /path/to/mount/point
```

Ensure the SSH key has no passphrase for unattended mounting, or use `ssh-agent` with the system’s init/systemd.

## Performance and Limitations

`sshfs` works well for occasional file access, but keep these in mind:

- **Latency-sensitive**: Each filesystem operation crosses the network. Random I/O will be slow.
- **Not suitable for databases**: Tools like MySQL, PostgreSQL, or SQLite perform poorly over `sshfs`.
- **Caching**: `sshfs` implements caching, but it won’t match local filesystem performance.
- **Connection drops**: Use `reconnect` option to handle temporary network issues.

For high-performance remote storage, consider NFS, SMB/CIFS, or dedicated block storage solutions instead.

## Troubleshooting

**Permission denied errors:**\
Check that your SSH user has read permissions on the remote path and that `allow_other` is set if needed.

**Host key verification fails:**\
Add the server to your `known_hosts`:

``` bash
ssh-keyscan server >> ~/.ssh/known_hosts
```

**Mount appears empty:**\
Verify the remote path exists and contains files:

``` bash
ssh username@server ls -la /path/to/folder
```

**Resource busy on unmount:**\
Close any open files or shells using the mount:

``` bash
lsof /path/to/mount/point
```

## 2026 Best Practices and Advanced Techniques

For Mounting Remote Folders via SSH with SSHFS, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
