---
title: "Passwordless SSH Authentication on Linux"
date: 2013-07-12 16:32:02 +0000
modified: 2026-04-12 04:40:54 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /enabling-password-less-ssh-login/
---

If you don’t already have a key pair, use Ed25519 — it’s faster and more secure than RSA:

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

For older systems that don’t support Ed25519, RSA with 4096 bits still works:

``` bash
ssh-keygen -t rsa -b 4096
```

Keys are stored in `~/.ssh/` by default: `id_ed25519` (private) and `id_ed25519.pub` (public) for Ed25519, or `id_rsa` and `id_rsa.pub` for RSA.

If you’re accessing a server from multiple machines, use `ssh-agent` to avoid typing your passphrase repeatedly:

``` bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

For persistent agent setup across sessions, add the `ssh-agent` initialization to your shell’s rc file (`.bashrc`, `.zshrc`, etc.).

## Copy Public Key to Remote Machine

### Using ssh-copy-id (Recommended)

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@remotemachine
```

The `-i` flag explicitly selects which key to copy. If you have only one key and `ssh-copy-id` works without it, the flag is optional.

### Manual Method

When `ssh-copy-id` isn’t available, do it manually:

``` bash
scp ~/.ssh/id_ed25519.pub username@remotemachine:/tmp/
ssh username@remotemachine
```

On the remote machine:

``` bash
# Always back up before modifying authorized_keys
cp ~/.ssh/authorized_keys ~/.ssh/authorized_keys.bak

# Append the public key
cat /tmp/id_ed25519.pub >> ~/.ssh/authorized_keys

# Clean up and set correct permissions
rm /tmp/id_ed25519.pub
chmod 600 ~/.ssh/authorized_keys
```

## Set Correct File Permissions

Wrong permissions are the \#1 reason passwordless login fails. SSH enforces strict permission checks:

``` bash
# Home directory — no group/other write
chmod 700 ~

# .ssh directory
chmod 755 ~/.ssh

# authorized_keys (must be 600, not world-readable)
chmod 600 ~/.ssh/authorized_keys

# Private key (never readable by others)
chmod 600 ~/.ssh/id_ed25519

# Public key
chmod 644 ~/.ssh/id_ed25519.pub
```

The `authorized_keys` file mode **must** be 600. SSH will refuse to read it if it’s world-readable, resulting in “Permission denied (publickey)” with no clear explanation.

## Debugging SSH Key Authentication

Enable verbose mode to see what’s happening:

``` bash
ssh -v username@remotemachine
```

Look for these lines in the output:

- `Offering public key: ...` — your key was sent to the server
- `Server accepts key` — authentication succeeded
- `Authentication refused: bad ownership or modes` — permissions problem

For even more detail, use `-vv` or `-vvv`.

Check server-side logs:

``` bash
# Debian/Ubuntu
sudo tail -f /var/log/auth.log | grep sshd

# RHEL/Fedora
sudo tail -f /var/log/secure | grep sshd
```

Look for entries like:

    sshd[12345]: Accepted publickey for username from 192.168.1.50 port 54321 ssh2: ED25519 SHA256:xxxxx

Or if it failed:

    sshd[12345]: Invalid user username from 192.168.1.50
    sshd[12345]: Authentication refused: bad ownership or modes on authorized_keys

## Common Issues and Fixes

**SSH keeps asking for a password:**

- Verify the public key is in `.ssh/authorized_keys` on the server as a single unbroken line
- Check that `PubkeyAuthentication yes` is set in `/etc/ssh/sshd_config`
- Verify file permissions match the section above
- Restart SSH if you modified `sshd_config`: `sudo systemctl restart sshd`

**Connection refused:**

- SSH daemon isn’t running: `sudo systemctl status sshd`
- Firewall blocking port 22: `sudo iptables -L -n | grep 22` or check your firewall rules
- Non-standard port: use `ssh -p portnumber username@remotemachine`

**Authentication refused with no clear reason:**

- Run `ssh -v` and check the server logs (see debugging section above)
- Ensure the remote user actually owns `~/.ssh/` and `~/.ssh/authorized_keys`
- On some systems, SELinux policies block SSH access — check `sudo audit2allow` output

## Use SSH Config for Easier Access

Instead of typing hostnames and key paths repeatedly, create `~/.ssh/config`:

    Host myserver
        HostName 192.168.1.100
        User deploy
        Port 22
        IdentityFile ~/.ssh/id_ed25519

    Host github.com
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_ed25519

    Host *
        AddKeysToAgent yes
        IdentitiesOnly yes

Now just type `ssh myserver` without specifying the user or key path. The `Host *` section applies `AddKeysToAgent yes` globally, which automatically adds keys to `ssh-agent` on first use.

## SSH Certificates for Multi-Server Environments

For managing access across dozens or hundreds of servers, SSH certificates replace the need to copy public keys to every machine’s `authorized_keys`:

Generate a certificate from your public key:

``` bash
ssh-keygen -s /path/to/ca_key -I "username@hostname" -n username -V +52w ~/.ssh/id_ed25519.pub
```

This creates `id_ed25519-cert.pub`. Tell SSH to use it:

``` bash
cat >> ~/.ssh/config << EOF
Host *
    IdentityFile ~/.ssh/id_ed25519
    IdentityFile ~/.ssh/id_ed25519-cert.pub
EOF
```

On servers, configure SSH to trust the CA’s public key in `/etc/ssh/trusted-user-ca-keys.pem`:

``` bash
echo "ssh-ed25519 AAAAC3Nza..." | sudo tee /etc/ssh/trusted-user-ca-keys.pem
```

Then add to `/etc/ssh/sshd_config`:

    TrustedUserCAKeys /etc/ssh/trusted-user-ca-keys.pem

Restart SSH: `sudo systemctl restart sshd`

Now all users with certificates signed by your CA can log in without individual key deployment. This approach scales far better than managing `authorized_keys` files across hundreds of machines.

## Password-Based Automation with sshpass

For scripts and one-off automation where key-based auth isn’t practical, `sshpass` types passwords in for you:

``` bash
# Debian/Ubuntu
sudo apt install sshpass

# Fedora/RHEL
sudo dnf install sshpass
```

Provide the password directly:

``` bash
sshpass -p "your_password" ssh username@remotemachine
```

Or read from a file:

``` bash
sshpass -f /path/to/password_file ssh username@remotemachine
```

**Security note:** Passwords on the command line appear in `ps aux` output and shell history. For anything production-facing or long-term, key-based auth is strongly preferred. `sshpass` is acceptable for quick testing and non-critical automation, but don’t use it for production SSH access to important systems.
