---
title: "Speed Up SSH Login by Disabling Reverse DNS Lookups"
date: 2018-03-24 11:46:57 +0000
layout: post
canonical: https://www.systutorials.com/how-to-disable-ssh-reverse-dns-lookup-on-linux/
---

SSH performs reverse DNS lookups on connecting clients by default. If your DNS infrastructure is slow or misconfigured, this can add several seconds to every login attempt. Disabling this lookup is a straightforward performance optimization, especially in cloud environments where internal IPs often lack valid PTR records.

## Disable the UseDNS Setting

Edit `/etc/ssh/sshd_config`:

``` bash
sudo nano /etc/ssh/sshd_config
```

Find the line `#UseDNS yes` (or add one if it doesn’t exist) and change it to:

    UseDNS no

Restart the SSH daemon:

``` bash
sudo systemctl restart sshd
```

Verify the change took effect by checking the running configuration:

``` bash
sudo sshctl -T | grep usedns
```

Test a new connection to ensure everything works as expected. You should notice login times improve, especially if DNS resolution was the bottleneck.

## Why This Matters

Reverse DNS lookups (`in-addr.arpa` queries) happen for every client connection. When DNS is slow or the PTR records don’t exist, sshd waits for a timeout before proceeding. In environments with hundreds of failed login attempts, this adds up quickly.

Modern security practices don’t rely on DNS for authentication anyway. SSH key-based authentication and fail2ban work independently of reverse DNS, making this setting safe to disable.

## When to Keep UseDNS Enabled

There are rare cases where you might want reverse DNS:

- If you’re logging client hostnames (rather than IPs) and need human-readable records
- If you have security policies that explicitly require hostname verification
- If you’re using PAM modules that depend on hostname resolution

For most deployments, disabling it is the right call.

## Related Performance Optimizations

Once you’ve disabled DNS lookups, consider these additional SSH optimizations:

**Reduce connection delays with connection multiplexing** on the client side by adding to `~/.ssh/config`:

    ControlMaster auto
    ControlPath ~/.ssh/control-%h-%p-%r
    ControlPersist 600

**Disable GSSAPI authentication** if you’re not using Kerberos. Edit `/etc/ssh/sshd_config`:

    GSSAPIAuthentication no

**Restrict login attempts** with fail2ban:

``` bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
```

Create `/etc/fail2ban/jail.local` to customize SSH protection:

    [sshd]
    enabled = true
    maxretry = 3
    findtime = 600
    bantime = 3600

**Use SSH certificates** instead of password authentication for better security and faster validation. Generate a certificate authority, sign user keys, and configure sshd to trust them in `/etc/ssh/sshd_config`:

    TrustedUserCAKeys /etc/ssh/ca.pub

These changes work well together and significantly improve both security and login speed across your infrastructure.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
