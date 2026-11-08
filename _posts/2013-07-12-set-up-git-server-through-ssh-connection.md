---
title: "Setting Up a Git Server with SSH"
date: 2013-07-12 16:31:44 +0000
modified: 2026-04-12 04:41:33 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /set-up-git-server-through-ssh-connection/
---

Git and SSH integrate seamlessly for version control infrastructure. An SSH-based Git server works well for small teams where all members are trusted and have administrator-level access to all repositories. This approach is straightforward to deploy, but lacks fine-grained access control.

For teams that need role-based repository access or audit trails, consider dedicated tools like Gitolite, Forgejo, or hosted solutions like GitHub/GitLab instead.

### Server-Side Configuration

Log into your Git server with an account that has sudo/root privileges.

**Install Git:**

``` bash
sudo dnf install git
```

**Create a dedicated Git user:**

``` bash
sudo useradd -m -d /home/git -s /usr/sbin/nologin git
```

Restrict the git user to Git operations only by setting the shell to `nologin` or `git-shell`. If using `git-shell`, add it to `/etc/shells` first to avoid “invalid shell” errors:

``` bash
echo /usr/bin/git-shell | sudo tee -a /etc/shells
sudo usermod -s /usr/bin/git-shell git
```

**Create the git-shell commands directory** (required for git-shell to function):

``` bash
sudo mkdir -p /home/git/git-shell-commands
sudo chown git:git /home/git/git-shell-commands
sudo chmod 755 /home/git/git-shell-commands
```

**Set up SSH key access:**

On your local machine, generate an SSH key if you don’t have one:

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -C "your-email@example.com"
```

Copy your public key to the server:

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub git@example.org
```

If `ssh-copy-id` isn’t available, manually append your key:

``` bash
cat ~/.ssh/id_ed25519.pub | ssh username@example.org "sudo tee -a /home/git/.ssh/authorized_keys"
sudo chmod 600 /home/git/.ssh/authorized_keys
sudo chown git:git /home/git/.ssh/authorized_keys
```

### Creating Repositories

On the server, create a bare repository (contains only version control data, no working directory):

``` bash
sudo su - git -s /bin/bash
mkdir -p repos/myproject.git
cd repos/myproject.git
git init --bare
```

The `--bare` flag creates a repository suitable for receiving pushes from multiple users.

### Initial Setup on Client

On your local machine, initialize a new project:

``` bash
mkdir myproject
cd myproject
git init
touch README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ssh://git@example.org/home/git/repos/myproject.git
git push -u origin main
```

For subsequent work:

``` bash
git clone ssh://git@example.org/home/git/repos/myproject.git
cd myproject
git pull
# Make changes
git commit -am "Update feature X"
git push
```

## Git Server Behind a Gateway (Port-Forwarded)

When your Git server is inside a private network accessed through a gateway with port forwarding (e.g., port 22111 on `gate.example.org` forwards to `vm111:22`), the setup is nearly identical—only the SSH connection details change.

**Server-side setup is unchanged**, but configure using the gateway:

``` bash
ssh username@gate.example.org -p 22111
# Then follow the steps above identically
```

**On the client, use the gateway address and forwarded port in your remote URL:**

``` bash
git remote add origin ssh://git@gate.example.org:22111/home/git/repos/myproject.git
git push -u origin main
```

When cloning:

``` bash
git clone ssh://git@gate.example.org:22111/home/git/repos/myproject.git
```

### Important Considerations

**SSH Key Types:** Use Ed25519 keys (`ssh-keygen -t ed25519`) for better security and performance than older RSA keys. Ensure your SSH client supports them (all modern clients do).

**Repository Paths:** Use absolute paths in remote URLs (`/home/git/repos/myproject.git`) rather than tilde expansion (`~/repos/myproject.git`), which can cause confusion with different shell contexts.

**File Permissions:** Ensure the git user owns all repositories and the `.ssh` directory. Incorrect permissions will silently fail during push/pull operations.

**Backup Keys:** Keep your SSH private keys backed up securely. Loss of the key means loss of access.

**Multiple Users:** Each user adds their public key to `/home/git/.ssh/authorized_keys`. All users authenticate as the `git` system user but are differentiated by their SSH keys. For per-repository access control or user attribution, migrate to Gitolite or similar tools.

**Monitoring:** Enable SSH logging to audit repository access:

``` bash
sudo journalctl -u sshd -f
```

This basic SSH Git server works well for small teams or internal CI/CD systems but scales poorly beyond a handful of users. Plan migrations to more sophisticated tools as your infrastructure grows.
