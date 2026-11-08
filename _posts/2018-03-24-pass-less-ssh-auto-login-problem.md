---
title: "SSH Auto-Login Without Passwords: Troubleshooting Guide"
date: 2018-03-24 08:04:15 +0000
modified: 2026-04-12 04:40:38 +0000
author: "Q A"
layout: post
categories: [scripting-utilities]
canonical: /pass-less-ssh-auto-login-problem/
---

When passwordless SSH authentication fails despite proper key setup, start by checking the SSH daemon logs to identify the actual problem.

## Checking SSH Logs

The SSH daemon logs are your primary diagnostic tool:

``` bash
sudo tail -f /var/log/auth.log          # Debian/Ubuntu
sudo tail -f /var/log/secure            # RHEL/CentOS/Fedora
sudo journalctl -u ssh -f               # systemd-based systems
```

Watch the log while attempting to connect to see detailed rejection reasons.

## Common Permission Issues

The most frequent cause is incorrect file or directory permissions. SSH is strict about this for security reasons.

### Home Directory Permissions

If you see `Authentication refused: bad ownership or modes for directory`, fix the home directory:

``` bash
chmod 700 /home/username
```

The home directory must be owned by the user and readable only by that user. If ownership is wrong:

``` bash
chown username:username /home/username
```

### SSH Directory and Key Permissions

Similarly, the `.ssh` directory and authorized_keys file have strict requirements:

``` bash
chmod 700 /home/username/.ssh
chmod 600 /home/username/.ssh/authorized_keys
chown -R username:username /home/username/.ssh
```

If these are wrong, you’ll see errors like `Authentication refused: bad ownership or modes for /home/username/.ssh` or similar.

### Private Key File Permissions (Local Machine)

On the machine where you’re initiating the connection, your private key must also have restricted permissions:

``` bash
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_ed25519
```

## Setting Up Passwordless Login

If you’re starting fresh, use `ssh-copy-id`:

``` bash
ssh-copy-id -i ~/.ssh/id_rsa username@remote_host
ssh-copy-id -i ~/.ssh/id_rsa -p 2222 username@remote_host  # non-standard port
```

This command automatically creates the `.ssh` directory with correct permissions and appends your public key to `authorized_keys`.

Manual setup if needed:

``` bash
# On the remote host
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "your_public_key_content" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

## SELinux Considerations

On SELinux-enforcing systems (RHEL, CentOS, Fedora), incorrect contexts can block SSH even with correct Unix permissions. Check the context:

``` bash
ls -Z ~/.ssh
```

If needed, restore the default SELinux context:

``` bash
restorecon -Rv ~/.ssh
```

Rather than disabling SELinux entirely, let it restore proper contexts for SSH to function.

## SSH Daemon Configuration

Verify that your SSH daemon configuration allows public key authentication:

``` bash
grep -E "PubkeyAuthentication|PasswordAuthentication" /etc/ssh/sshd_config
```

Ensure `PubkeyAuthentication yes` is set and not commented out. After making changes:

``` bash
sudo sshd -t                    # Test configuration syntax
sudo systemctl restart sshd     # Apply changes
```

## Debugging with SSH Client

Use verbose output from the client side to see the authentication flow:

``` bash
ssh -vvv username@remote_host
```

Look for messages about key offerings and responses from the server. If you see “Offering public key” but the server doesn’t accept it, that points to a server-side permission problem.

For a specific key file:

``` bash
ssh -i ~/.ssh/id_rsa -vvv username@remote_host
```

## Verify Key Generation

Ensure your keys were generated correctly:

``` bash
ssh-keygen -l -f ~/.ssh/id_rsa.pub
ssh-keygen -l -f ~/.ssh/id_rsa
```

Both should produce fingerprints. Modern best practice is to use Ed25519 keys:

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh-copy-id -i ~/.ssh/id_ed25519 username@remote_host
```

## Common Checklist

- Remote home directory: `700` ownership
- Remote `.ssh` directory: `700` ownership
- Remote `authorized_keys`: `600` ownership
- Local private key: `600` permissions
- Local public key: `644` permissions (or `600`)
- SSH daemon is running: `systemctl status ssh`
- SSH daemon config has `PubkeyAuthentication yes`
- No typos in usernames or hostnames
- Correct port if not using 22

Work through these systematically with verbose output and log checking, and you’ll identify the issue quickly.
