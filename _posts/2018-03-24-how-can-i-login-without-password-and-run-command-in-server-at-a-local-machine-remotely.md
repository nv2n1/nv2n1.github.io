---
title: "SSH Key-Based Authentication for Passwordless Remote Command Execution"
date: 2018-03-24 11:54:37 +0000
author: "Weiwei Jia"
layout: post
canonical: https://www.systutorials.com/how-can-i-login-without-password-and-run-command-in-server-at-a-local-machine-remotely/
---

Password-less SSH login is faster, more secure, and essential for automation. Combining it with remote command execution lets you run tasks on servers from your local machine without interactive authentication.

## Setting Up SSH Key-Based Authentication

### Generate SSH Keys

First, generate an ED25519 key pair on your local machine (A):

``` bash
ssh-keygen -t ed25519 -C "user@hostname" -f ~/.ssh/id_ed25519
```

This creates `~/.ssh/id_ed25519` (private key) and `~/.ssh/id_ed25519.pub` (public key). Use ED25519 over RSA—it’s more secure and faster.

### Add Your Public Key to the Remote Server

The easiest method is `ssh-copy-id`, which handles file permissions correctly:

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@RemoteServer
```

You’ll be prompted for the password once. This appends your public key to `~/.ssh/authorized_keys` on the remote server and sets proper permissions (700 for `.ssh`, 600 for `authorized_keys`).

If `ssh-copy-id` isn’t available, you can manually add the key:

``` bash
cat ~/.ssh/id_ed25519.pub | ssh user@RemoteServer 'cat >> ~/.ssh/authorized_keys'
```

### Verify the Connection

Test password-less login:

``` bash
ssh user@RemoteServer
```

If successful, you’ll connect without entering a password.

## Running Remote Commands

Execute a single command on the remote server:

``` bash
ssh user@RemoteServer "ls -la /home"
```

Or run multiple commands:

``` bash
ssh user@RemoteServer "cd /var/log && tail -20 syslog"
```

For complex scripts, pipe a local script to the remote shell:

``` bash
ssh user@RemoteServer bash < local_script.sh
```

Or run a script directly from the remote server:

``` bash
ssh user@RemoteServer "/path/to/remote/script.sh"
```

## Important Considerations for Remote Execution

**Environment variables and shell state**: Remote commands run in a non-login, non-interactive shell, so your `.bashrc` or `.bash_profile` may not load. Specify full paths or source your environment:

``` bash
ssh user@RemoteServer "source ~/.bashrc && command_name"
```

**Return codes**: Capture the exit status of remote commands:

``` bash
ssh user@RemoteServer "some_command"
echo $?
```

**Standard input/output redirection**: Remote I/O works correctly with proper quoting:

``` bash
ssh user@RemoteServer "cat file.txt | grep pattern"
```

**Security**: Only distribute your public key (`id_ed25519.pub`), never your private key. Set restrictive permissions:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/authorized_keys
```

## Automation with SSH

For unattended operations (cron jobs, scripts), combine SSH with key-based auth. Consider using `ssh-agent` to cache your passphrase:

``` bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519
```

Now subsequent SSH commands won’t prompt for your passphrase within that shell session.

For production servers, further harden SSH by disabling password authentication entirely in `/etc/ssh/sshd_config`:

    PasswordAuthentication no
    PubkeyAuthentication yes

Then restart SSH:

``` bash
sudo systemctl restart sshd
```

This forces all connections to use keys, eliminating brute-force password attacks.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
