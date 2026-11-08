---
title: "Deleting GNOME Keyrings: A Step-by-Step Guide"
date: 2018-03-24 08:04:32 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/gnome-disabling-deleting-keyrings/
---

GNOME Keyring stores encrypted credentials, SSH keys, and secrets for applications. If you need to disable it or start fresh after forgetting the password, you can remove the keyring database.

### Keyring Storage Locations

The location of keyrings depends on your GNOME version and configuration:

- **GNOME 3.0+**: `~/.local/share/gnome-keyring/` or `~/.local/share/evolution/calendar/`
- **Older GNOME**: `~/.gnome2/keyrings/`
- **XDG Base Directory compliant**: Check `$XDG_DATA_HOME/gnome-keyring/`

Check which applies to your system:

``` bash
ls -la ~/.local/share/gnome-keyring/
ls -la ~/.gnome2/keyrings/
```

### Backing Up Before Deletion

Always backup keyrings before deletion — they contain encrypted passwords and SSH keys you may need:

``` bash
cp -r ~/.local/share/gnome-keyring/ ~/.local/share/gnome-keyring.backup
```

### Deleting Keyrings

To completely remove keyrings and reset GNOME Keyring:

``` bash
rm -rf ~/.local/share/gnome-keyring/
```

If using older GNOME:

``` bash
rm -rf ~/.gnome2/keyrings/
```

After deletion, restart the keyring daemon or log out and back in:

``` bash
pkill -9 gnome-keyring-daemon
```

The daemon will respawn and create a new, empty keyring on next login.

### Disabling Keyring Without Deletion

If you want to disable GNOME Keyring without removing files, you can:

1.  **Disable the systemd service** (if available):

    ``` bash
    systemctl --user mask gnome-keyring-daemon.service
    systemctl --user stop gnome-keyring-daemon.service
    ```

2.  **Unset the SSH_AUTH_SOCK variable** to prevent applications from using it:

    ``` bash
    unset SSH_AUTH_SOCK
    ```

3.  **Use dconf to disable autostart**:

    ``` bash
    dconf write /org/gnome/keyring/daemon-components "[]"
    ```

### Listing Current Keyrings

Before deletion, see what’s stored:

``` bash
secret-tool search --all
```

Or use the GNOME Secrets GUI application to review contents.

### Removing Individual Passwords

If you only want to delete specific credentials rather than the entire keyring:

``` bash
secret-tool clear attribute value
```

For example, to remove a stored password for a service:

``` bash
secret-tool clear service example-service username myuser
```

### Resetting Password for Locked Keyring

If your keyring is locked and you forgot the password, deletion is often the only option. However, you can attempt to change it through the Passwords and Keys GUI application — search for “Passwords” in your applications menu.

### After Deletion

- New keyrings will be created automatically when needed
- SSH keys won’t be automatically cached — you’ll need to re-add them to ssh-agent or configure them again
- Saved browser passwords, email credentials, and VPN configs will be lost
- You’ll be prompted to re-enter passwords for services on next login

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Deleting GNOME Keyrings: A Step-by-Step Guide, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
