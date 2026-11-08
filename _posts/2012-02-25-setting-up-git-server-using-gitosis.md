---
title: "Git Server Setup with Gitosis"
date: 2012-02-25 13:17:48 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/setting-up-git-server-using-gitosis/
---

Gitosis is unmaintained and shouldn’t be used for new deployments. Use **Gitolite** or **Forgejo** instead. This guide covers Gitolite, which provides fine-grained access control, is actively maintained, and handles multiple repositories under a single system user.

## Prerequisites

- A server running Linux (Debian, Ubuntu, CentOS, or similar)
- SSH access to the server with sudo privileges
- A domain name or IP address for your git server
- Administrator’s SSH public key already generated (`ssh-keygen -t ed25519`)

## Install Git and Gitolite

SSH into your server and install dependencies:

``` bash
sudo apt update && sudo apt install -y git gitolite3
```

For CentOS/RHEL:

``` bash
sudo dnf install -y git gitolite3
```

Gitolite3 creates its own system user (`git`) automatically during installation on most distributions. Verify it exists:

``` bash
id git
```

## Initialize Gitolite

On your **local machine**, copy your public key to the server:

``` bash
scp ~/.ssh/id_ed25519.pub user@example.org:/tmp/admin.pub
```

Then on the **server**, switch to the git user and initialize Gitolite:

``` bash
sudo su - git
gitolite setup -pk /tmp/admin.pub
```

This creates the `gitolite-admin.git` repository and sets you as the administrator. Verify the setup:

``` bash
ls -la ~/.ssh/authorized_keys
ls -la ~/repositories/
```

You should see `gitolite-admin.git` and `testing.git` (the default test repo).

## Clone the Admin Repository

Back on your **local machine**, clone the admin repository:

``` bash
git clone git@example.org:gitolite-admin.git
cd gitolite-admin
```

The repository contains:

    conf/gitolite.conf    # Main configuration file
    keydir/               # Directory for user SSH public keys

## Basic Configuration

Edit `conf/gitolite.conf` to define repositories and permissions:

    repo gitolite-admin
        RW+  = admin

    repo testing
        RW+  = @developers
        R    = @viewers

    repo internal
        RW   = alice bob
        RW   = team-leads
        R    = @developers

Add user public keys to `keydir/` with names matching the config (e.g., `alice.pub`, `bob.pub`). Commit and push:

``` bash
git add conf/ keydir/
git commit -m "Add new repositories and users"
git push
```

Gitolite applies changes immediately on push.

## Access Control Examples

Define user groups in `conf/gitolite.conf`:

    @developers = alice bob charlie
    @leads = david eva

    repo project-x
        RW                 = @developers
        RW+ = @leads       # Can force-push and delete
        R                  = @viewers
        RW+ refs/tags/v*   = @leads   # Only leads can create version tags

Permissions:

- `R` – read
- `W` – write (non-forced)
- `+` – force-push and delete
- `-` – deny (useful to exclude users from groups)

Branch-level control:

    repo api
        RW                    = @developers
        RW+ refs/heads/dev    = @developers
        RW+ refs/heads/main   = @leads
        -  refs/heads/main    = @developers  # Developers cannot touch main

## Public Repository Access via Git Daemon

To offer read-only public access without SSH keys, use git-daemon.

Create a systemd service at `/etc/systemd/system/git-daemon.service`:

``` ini
[Unit]
Description=Git Daemon
After=network.target

[Service]
Type=simple
User=git
WorkingDirectory=/var/lib
ExecStart=/usr/bin/git daemon --reuseaddr --base-path=/home/git/repositories /home/git/repositories
StandardOutput=journal
StandardError=journal
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

``` bash
sudo systemctl enable git-daemon
sudo systemctl start git-daemon
```

For selective export, create `git-daemon-export-ok` in specific repository directories:

``` bash
sudo su - git
touch ~/repositories/public-repo.git/git-daemon-export-ok
```

Then users can clone via:

``` bash
git clone git://example.org/public-repo.git
```

## User Management

To add a new user:

1.  Have them generate an SSH key: `ssh-keygen -t ed25519`
2.  Get their public key
3.  Add it to `keydir/username.pub` in gitolite-admin
4.  Add their username to groups in `conf/gitolite.conf`
5.  Commit and push

To revoke access, remove their entry from the config and delete their public key file.

## Backup Repositories

Backup all repositories regularly:

``` bash
sudo su - git
tar -czf /backup/gitolite-$(date +%Y%m%d).tar.gz ~/repositories/
```

Or use a Git mirror approach:

``` bash
git clone --mirror git@example.org:repo-name.git repo-name.git
```

## Troubleshooting

Check Gitolite logs:

``` bash
sudo su - git
gitolite log
```

Test SSH access:

``` bash
ssh -v git@example.org
```

Verify permissions:

``` bash
ssh git@example.org info
```

This shows all repositories you have access to.
