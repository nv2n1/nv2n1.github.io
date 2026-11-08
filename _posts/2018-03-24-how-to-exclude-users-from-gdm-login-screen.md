---
title: "Hide User Accounts from the GDM Login Screen"
date: 2018-03-24 11:40:21 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /how-to-exclude-users-from-gdm-login-screen/
---

GDM (GNOME Display Manager) lets you control which users appear on the login screen. You have two main options: hide the entire user list or exclude specific users while keeping the list visible for others.

## Disable the user list entirely

The most straightforward approach is to disable user listing completely. This forces everyone to type their username instead of selecting from a dropdown:

``` bash
sudo tee /etc/dconf/db/gdm.d/01-mysettings > /dev/null <<EOF
[org/gnome/login-screen]
disable-user-list=true
EOF

sudo dconf update
```

This writes the setting to the GDM dconf database. Users will see a blank login screen requiring manual credential entry. Restart GDM to apply:

``` bash
sudo systemctl restart gdm
```

On Wayland sessions (default in GNOME 40+), you may need to log out and back in for changes to take full effect.

## Hide specific users

If you want to keep the user list visible but exclude certain accounts, use the `exclude-users` dconf setting:

``` bash
sudo tee /etc/dconf/db/gdm.d/01-mysettings > /dev/null <<EOF
[org/gnome/login-screen]
disable-user-list=false
exclude-users=['user1', 'user2', 'testuser']
EOF

sudo dconf update
sudo systemctl restart gdm
```

Replace `user1`, `user2`, and `testuser` with the actual usernames you want to hide. The `exclude-users` list accepts any number of accounts.

## Verify your changes

Check that the configuration was applied correctly:

``` bash
sudo dconf read -d /org/gnome/login-screen
```

You should see your settings in the output. If changes don’t take effect after restarting GDM, verify the file exists and is readable:

``` bash
ls -la /etc/dconf/db/gdm.d/01-mysettings
```

The file should be readable by all users. If permissions are wrong, fix them:

``` bash
sudo chmod 644 /etc/dconf/db/gdm.d/01-mysettings
```

## Revert to default behavior

Remove the configuration and recompile the dconf database:

``` bash
sudo rm /etc/dconf/db/gdm.d/01-mysettings
sudo dconf update
sudo systemctl restart gdm
```

## Important notes

- These settings apply only to the GDM login screen, not system user listings elsewhere
- Users with admin access can still view system user information through other means (e.g., `getent passwd`)
- The `disable-user-list` setting is more reliable than `exclude-users` across different GNOME versions
- Always run `sudo dconf update` after editing dconf files—this compiles the database and is required for changes to take effect
- Behavior varies slightly between distributions and GNOME versions; check your distro’s documentation if settings don’t apply

## Troubleshooting

**Settings aren’t taking effect:**

- Ensure you’re editing `/etc/dconf/db/gdm.d/` (system-wide GDM settings), not user-level dconf directories
- Run `sudo dconf update` after every change—this is required
- Restart GDM: `sudo systemctl restart gdm`
- Check file syntax—dconf is strict about formatting (proper quotes, commas between list items)
- Verify the file is readable: `sudo cat /etc/dconf/db/gdm.d/01-mysettings`

**Syntax errors:**

If dconf complains about syntax, check your list formatting. Lists must use single quotes and comma-separated values:

``` bash
# Correct
exclude-users=['user1', 'user2', 'user3']

# Wrong
exclude-users=['user1' 'user2' 'user3']
exclude-users=["user1", "user2", "user3"]
```

**Changes apply temporarily but revert:**

This usually means the dconf database wasn’t properly updated or recompiled. Run `sudo dconf update` again and restart GDM. If the issue persists, check that `/etc/dconf/db/gdm.d/` directory exists and is writable by root:

``` bash
sudo ls -ld /etc/dconf/db/gdm.d/
```

If the directory doesn’t exist, create it:

``` bash
sudo mkdir -p /etc/dconf/db/gdm.d/
```

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Hide User Accounts from the GDM Login Screen with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Hide User Accounts from the GDM Login Screen. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
