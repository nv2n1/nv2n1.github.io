---
title: "Setting Up Gitolite for SSH-Based Git Repositories"
date: 2014-03-07 00:13:51 +0000
modified: 2026-04-11 16:40:29 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-up-gitolite-git-server-a-ten-minute-tutorial/
---

Gitolite provides fine-grained access control over Git repositories without the overhead of a full-featured platform. It uses SSH keys for authentication and handles per-user, per-repository, and even per-branch permissions through a simple configuration file. This guide covers a working installation on modern Linux distributions.

## Prerequisites

**Server:**

- Linux (Ubuntu 20.04 LTS or later, Debian 11+, RHEL/Rocky 8+, Fedora 38+)
- Git installed
- SSH running (standard port 22)
- Unprivileged user with sudo access (or root, though running as unprivileged is safer)

**Workstation:**

- Linux, macOS, or WSL2
- SSH key pair (generate with `ssh-keygen -t ed25519` if needed)
- Git and SSH client

## Quick Start

Set these variables before running commands:

``` bash
GIT_SERVER=git.example.com
GIT_USER=git
ADMIN=$USER
ADMIN_KEY=$HOME/.ssh/id_ed25519.pub
```

Replace `git.example.com` with your actual server hostname or IP. Use Ed25519 keys if your workstation and server both support them (better than RSA for new setups).

## Copy Your Public Key to the Server

Transfer your public key to the server:

``` bash
scp $ADMIN_KEY $USER@$GIT_SERVER:/tmp/$ADMIN.pub
ssh $USER@$GIT_SERVER "chmod 644 /tmp/$ADMIN.pub"
```

## Install Gitolite

SSH to the server and run the installation as the unprivileged user (or adapt if using root):

``` bash
ssh $USER@$GIT_SERVER << 'EOFINSTALL'
sudo adduser --disabled-password --gecos '' $GIT_USER 2>/dev/null || true
sudo -u $GIT_USER bash << 'EOFGIT'
mkdir -p ~/bin
git clone https://github.com/sitaramc/gitolite /tmp/gitolite-src
/tmp/gitolite-src/install -to ~/bin
~/bin/gitolite setup -pk /tmp/$ADMIN.pub
EOFGIT
EOFINSTALL
```

This command:

- Creates the unprivileged `git` user
- Clones gitolite from GitHub
- Installs gitolite to the user’s `~/bin`
- Initializes gitolite with your public key

You should see output confirming the creation of the `gitolite-admin` and `testing` repositories.

## Verify the Installation

Clone the test repository:

``` bash
git clone $GIT_USER@$GIT_SERVER:testing
cd testing
echo "test" > testfile.txt
git add testfile.txt
git commit -m "test commit"
git push
```

If this succeeds without permission errors, your server is ready.

## Managing Repositories and Users

All administration happens through the `gitolite-admin` repository. Clone it on your workstation:

``` bash
git clone $GIT_USER@$GIT_SERVER:gitolite-admin
cd gitolite-admin
```

The directory structure:

- `conf/gitolite.conf` — All repository and permission rules
- `keydir/` — User SSH public keys (one file per user, named `username.pub`)

### Adding a User

Copy the user’s public key to `keydir/`:

``` bash
cp /path/to/alice.pub keydir/alice.pub
git add keydir/alice.pub
git commit -m "Add alice"
git push
```

### Creating a Repository with Permissions

Edit `conf/gitolite.conf` and add:

    repo my-project
        RW+     =   alice
        RW      =   bob
        R       =   charlie

Permission levels:

- `R` — read-only
- `RW` — read and write (no force push or delete)
- `RW+` — read, write, force push, delete
- `-` — deny access

Commit and push:

``` bash
git add conf/gitolite.conf
git commit -m "Add my-project repo with user permissions"
git push
```

The repository is created immediately on the server. Users can clone it:

``` bash
git clone git@$GIT_SERVER:my-project
```

## Branch-Level Access Control

Restrict write access to specific branches:

    repo feature-work
        RW+ refs/heads/feature/*    =   alice bob
        RW  refs/heads/main         =   alice
        R   refs/heads/main         =   bob charlie david

This grants:

- `alice` and `bob` full control over feature branches
- `alice` write access to main
- `bob`, `charlie`, and `david` read-only access to main

Use regex patterns for flexible branch matching:

    repo prod-code
        RW+ refs/heads/release-.*   =   release-manager
        RW  refs/heads/main         =   developers
        -   refs/heads/main         =   qa-users
        RW  refs/heads/main         =   qa-users

(The deny rule `-` is evaluated first, so this grants `qa-users` read-only access despite the later RW.)

## Managing User Access

### Revoking Access

Remove a user’s key and update configuration:

``` bash
rm keydir/alice.pub
# Update conf/gitolite.conf to remove alice from repos if needed
git add -A
git commit -m "Revoke alice"
git push
```

### Updating a Key

When a user regenerates their SSH key:

``` bash
cp /path/to/alice-new.pub keydir/alice.pub
git add keydir/alice.pub
git commit -m "Update alice SSH key"
git push
```

### Using Groups

Define groups in `conf/gitolite.conf` to manage permissions at scale:

    @developers = alice bob charlie
    @leads = alice bob
    @ops = david

    repo all-projects
        RW+     =   @leads
        RW      =   @developers
        R       =   @ops

Groups can include other groups:

    @backend = @developers david
    @frontend = @developers eve

    repo backend-code
        RW+     =   @backend

    repo frontend-code
        RW+     =   @frontend

## Checking Permissions

View all repositories and your access levels:

``` bash
ssh $GIT_USER@$GIT_SERVER gitolite info
```

Output shows each repository and your permissions on it.

Check what a specific user can access:

``` bash
ssh $GIT_USER@$GIT_SERVER gitolite access-info alice
```

## Troubleshooting

**“Permission denied (publickey)” when cloning:**

- Verify your key filename in `keydir/` matches your username (e.g., `alice.pub` for user `alice`)
- Confirm you’re using the correct private key: `ssh-add -l` to list loaded keys
- Test SSH directly: `ssh -v git@$GIT_SERVER` to see which key is being used

**Repository doesn’t exist after pushing to gitolite-admin:**

- Ensure `git push` completed without errors
- SSH to the server and verify: `sudo -u $GIT_USER ls ~/repositories/`
- Check for syntax errors in `conf/gitolite.conf`: `sudo -u $GIT_USER ~/bin/gitolite compile`

**Configuration changes not taking effect:**

- Gitolite only reads config when you push to `gitolite-admin`
- Avoid editing files directly on the server
- Always commit and push changes from your workstation

**SSH key not recognized after adding to keydir/:**

- SSH caches known keys; restart SSH or add to a new key slot
- Verify the key content: `cat keydir/alice.pub` (should start with `ssh-rsa`, `ssh-ed25519`, etc.)
- Check server-side logs: `sudo journalctl -u ssh` or equivalent

## Advanced Features

**Wild repositories** allow users to create repositories matching a pattern:

    repo my-project-[a-z0-9]*
        C       =   @developers
        RW+     =   CREATOR
        RW      =   @developers

Users can then push to any repository matching `my-project-*` on first push.

**Post-receive hooks** run after pushes. Create `.git/hooks/post-receive` in the server’s gitolite directory for notifications, CI/CD triggers, or backups.

**Deploy keys** allow CI/CD systems read-only access without a user account:

``` bash
cp /path/to/ci-system.pub keydir/ci-deploy.pub
```

Then grant minimal permissions:

    repo my-project
        R   =   ci-deploy

## Further Reading

- <a href="https://gitolite.com/" rel="nofollow noopener" target="_blank">Official gitolite documentation</a>
- <a href="https://gitolite.com/gitolite/conf" rel="nofollow noopener" target="_blank">gitolite access control rules</a>
- <a href="https://gitolite.com/gitolite/mirroring" rel="nofollow noopener" target="_blank">Migrating from GitHub to self-hosted gitolite</a>
