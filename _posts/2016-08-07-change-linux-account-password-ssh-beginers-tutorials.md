---
title: "Changing Your Linux Password Over SSH"
date: 2016-08-07 02:00:53 +0000
modified: 2026-04-12 16:55:14 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /change-linux-account-password-ssh-beginers-tutorials/
---

Open a terminal and connect to the server:

``` bash
ssh USER@HOST
```

Replace `USER` with your username and `HOST` with the server’s hostname or IP address.

On first connection, SSH will display the host key fingerprint:

    The authenticity of host 'HOST (IP_ADDRESS)' can't be established.
    ECDSA key fingerprint is SHA256:xxxxxxxxxxxx.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

Type `yes` and press Enter. SSH will then prompt for your password:

    USER@HOST's password:

Enter your current password. Characters won’t display as you type — this is normal for security.

## Change Your Password with passwd

Once logged in, run:

``` bash
passwd
```

The system will prompt for your current password:

    (current) UNIX password:

Enter it (characters won’t display), then you’ll see:

    New password:

Type your new password, then confirm it:

    Retype new password:

If successful, you’ll see:

    passwd: all authentication tokens updated successfully.

## Strong Password Requirements

Most modern systems enforce password complexity. Aim for at least 12 characters mixing uppercase, lowercase, numbers, and symbols. If your password is too weak, `passwd` will reject it:

    BAD PASSWORD: The password fails the dictionary check - too simplistic/systematic

Test your new password immediately by opening a new SSH session in another terminal before closing your original connection. This catches typos early — you can’t see what you’re typing, so mistakes are easy.

## Check Password Expiration

Some systems require periodic password changes. View your current settings:

``` bash
chage -l
```

This shows when your password will expire, when it was last changed, and the minimum days before it can be changed again.

If you’re an administrator, check another user’s expiration:

``` bash
sudo chage -l USERNAME
```

Set maximum password age (example: 90 days):

``` bash
sudo chage -M 90 USERNAME
```

Force a user to change their password on next login:

``` bash
sudo chage -d 0 USERNAME
```

## Prefer SSH Key Authentication

Password authentication is less secure and requires regular changes. SSH key-based authentication is better — use Ed25519 keys (the modern standard):

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Copy your public key to the server:

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub USER@HOST
```

You’ll now connect without password prompts. Once you’ve verified key access works, disable password authentication on servers you manage by editing `/etc/ssh/sshd_config`:

    PasswordAuthentication no

Reload SSH:

``` bash
sudo systemctl reload ssh
```

## Troubleshooting

**Password rejected as too similar to old one**

PAM’s `pwhistory` module prevents reusing recent passwords. Choose a sufficiently different password.

**Password change fails silently**

Check `/var/log/auth.log` for details:

``` bash
sudo tail -20 /var/log/auth.log
```

Issues often relate to home directory permissions or authentication backend problems (LDAP, Active Directory, etc.).

**Authentication token manipulation error**

Your password has expired and you’re locked out. Contact your system administrator — they may need to temporarily reset your account or enable emergency access.

**Reset another user’s password (admin only)**

``` bash
sudo passwd USERNAME
```

You won’t need the old password. Force them to change it on next login:

``` bash
sudo chage -d 0 USERNAME
```

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Changing Your Linux Password Over SSH with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Changing Your Linux Password Over SSH. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
