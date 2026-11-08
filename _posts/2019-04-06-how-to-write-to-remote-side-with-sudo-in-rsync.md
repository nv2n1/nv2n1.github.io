---
title: "Rsync with Sudo on Remote Systems"
date: 2019-04-06 08:39:02 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-write-to-remote-side-with-sudo-in-rsync/
---

By default, rsync connects as your standard user. When you need to write to protected directories like `/etc`, `/var/www`, or other root-owned locations, use the `--rsync-path` option to invoke rsync with sudo privileges on the remote side.

## Basic syntax

``` bash
rsync -avz --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

This tells the remote server to execute rsync under sudo. If your user has passwordless sudo configured, the transfer proceeds without prompts. Otherwise, you’ll be prompted for the sudo password.

## Practical examples

Sync a local directory to a remote web root:

``` bash
rsync -avz --rsync-path="sudo rsync" /var/www/app/ deploy@server:/var/www/html/app/
```

Pull configuration files from remote with preserved permissions:

``` bash
rsync -avzp --rsync-path="sudo rsync" user@remote:/etc/app/ ./etc-backup/
```

Exclude specific files during transfer:

``` bash
rsync -avz --exclude='*.log' --exclude='.git' --rsync-path="sudo rsync" /app/ user@remote:/opt/app/
```

Bidirectional sync with deletion (use with caution):

``` bash
rsync -avz --delete --rsync-path="sudo rsync" local-dir/ user@remote:/opt/protected/
```

## Configuring passwordless sudo

For unattended transfers, set up passwordless sudo on the remote system. Use `visudo` to edit `/etc/sudoers`:

``` bash
deploy ALL=(ALL) NOPASSWD: /usr/bin/rsync
```

Always use the full path to the rsync binary. Find it with:

``` bash
which rsync
```

For tighter security, restrict the rsync command options:

``` bash
deploy ALL=(ALL) NOPASSWD: /usr/bin/rsync --server --daemon
```

This prevents the deploy user from running arbitrary rsync operations while still allowing legitimate transfers.

## SSH key authentication

Always use SSH key-based authentication instead of passwords. For new deployments, use Ed25519 keys:

``` bash
rsync -avz -e "ssh -i ~/.ssh/id_ed25519" --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

For non-standard SSH ports or additional options:

``` bash
rsync -avz -e "ssh -i ~/.ssh/id_ed25519 -p 2222 -o StrictHostKeyChecking=accept-new" \
  --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

Ensure proper permissions on the remote user’s SSH keys:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

## Setting ownership and permissions

By default, rsync respects the remote umask. Use `--chown` to set specific ownership:

``` bash
rsync -avz --rsync-path="sudo rsync" --chown=www-data:www-data local-file user@remote:/var/www/
```

The remote rsync process must have sudo privileges to change ownership. For numeric UIDs/GIDs (useful across systems with different user databases):

``` bash
rsync -avz --rsync-path="sudo rsync" --chown=33:33 local-file user@remote:/var/www/
```

## Preserving extended attributes and ACLs

To preserve SELinux contexts, extended attributes, and ACLs:

``` bash
rsync -avzXA --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

The `-X` flag preserves extended attributes; `-A` preserves ACLs.

## Testing before running

Always use `--dry-run` to preview changes before executing a large sync with sudo:

``` bash
rsync -avz --dry-run --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

This shows exactly what rsync would transfer, delete, or change without making any actual modifications.

## Troubleshooting

**Version mismatches:** Significant differences between local and remote rsync versions can cause protocol errors. Check both:

``` bash
rsync --version
ssh user@remote rsync --version
```

Update both systems to compatible versions if needed.

**Permission denied errors:** Verify the user has proper sudo access:

``` bash
ssh user@remote sudo -l
```

This lists what the user can run with sudo. Ensure `/usr/bin/rsync` appears in the output.

**Sudo environment issues:** By default, sudo strips most environment variables. If rsync fails mysteriously, verify the sudoers configuration preserves necessary paths:

``` bash
Defaults:deploy secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

**Hangs during transfer:** Some SSH configurations or firewall rules cause hangs with sudo. Try disabling pseudo-terminal allocation:

``` bash
rsync -avz -e "ssh -T -o ConnectTimeout=10" --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

The `-T` flag prevents pseudo-terminal allocation, which can cause deadlocks.

**Checksum failures:** Unexpected checksum mismatches may indicate issues with remote filtering. Force checksum verification:

``` bash
rsync -avz --checksum --rsync-path="sudo rsync" local-file user@remote:/protected/path
```

## When to use alternatives

For complex multi-server deployments with templating and orchestration needs, consider:

- **Ansible:** Native privilege escalation via `become`, built-in templating, idempotent operations, and scales across infrastructure.
- **Configuration management:** Chef, Puppet, or SaltStack provide full lifecycle management with sudo integration and change tracking.
- **SCP/SFTP:** Suitable for simple one-off transfers to unprivileged directories, but less efficient for large directory trees.

For ad-hoc synchronization, backups, or deployments where you control both systems with secure SSH configured, rsync with sudo remains the most practical choice.
