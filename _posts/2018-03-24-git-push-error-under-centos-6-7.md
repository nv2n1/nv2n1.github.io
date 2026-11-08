---
title: "Git Push 403 Forbidden: Common Causes and Solutions"
date: 2018-03-24 11:48:57 +0000
modified: 2026-04-11 15:52:53 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /git-push-error-under-centos-6-7/
---

When pushing to GitHub over HTTPS, you’ll see:

    error: The requested URL returned error: 403 Forbidden while accessing https://github.com/username/repo.git
    fatal: HTTP request failed

This means Git connected to GitHub successfully, but your credentials were rejected. Common causes:

- Expired or revoked Personal Access Token (PAT)
- Using a password instead of a PAT (GitHub disabled password auth over HTTPS in 2021)
- Insufficient repository permissions
- Two-factor authentication enabled without proper token setup
- Stale credentials cached locally

## Solution 1: Personal Access Tokens with Credential Helper

GitHub now requires Personal Access Tokens instead of passwords. This is the quickest fix.

### Generate a PAT on GitHub

1.  Go to **Settings → Developer settings → Personal access tokens → Tokens (classic)**
2.  Click **Generate new token (classic)**
3.  Select scopes:
    - `repo` — full repository access
    - `workflow` — if you use GitHub Actions
4.  Copy the token immediately (you won’t see it again)

### Configure Git to Use the Token

Use Git’s credential helper instead of storing credentials in plaintext:

``` bash
git config --global credential.helper store
```

On next push, Git will prompt for credentials:

``` bash
git push origin main
```

When prompted:

- **Username:** your GitHub username
- **Password:** paste your PAT token

Git caches these in `~/.git-credentials`. To clear cached credentials:

``` bash
git credential reject https://github.com
```

For Debian/Ubuntu systems with `pass` installed:

``` bash
sudo apt-get install pass
git config --global credential.helper pass
```

For RHEL/CentOS/Fedora:

``` bash
sudo dnf install pass
git config --global credential.helper pass
```

The `pass` helper is more secure — it encrypts credentials.

## Solution 2: SSH Keys (Recommended)

SSH authentication avoids credential management entirely and is more secure:

``` bash
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
```

Add the public key to **GitHub → Settings → SSH and GPG keys → New SSH key**.

Update your repository remote:

``` bash
git remote set-url origin git@github.com:your-username/your-repo.git
```

Test the connection:

``` bash
ssh -T git@github.com
```

Expected output:

    Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.

Push now works with SSH:

``` bash
git push origin main
```

## Verify Your Setup

Check which authentication method Git is using:

``` bash
git config --list | grep -E '(user|credential|remote)'
git remote -v
```

Example output:

    user.name=your-username
    user.email=your-email@example.com
    credential.helper=store
    origin  git@github.com:your-username/your-repo.git (fetch)
    origin  git@github.com:your-username/your-repo.git (push)

## Troubleshooting Specific Cases

**PAT has correct permissions but still getting 403:**

Verify the token hasn’t expired. GitHub tokens can have expiration dates. Go back to Settings and check **Expiration** date. If expired, delete and regenerate.

**SSH authentication failing:**

Check your SSH key permissions:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

Verify the public key is actually added to GitHub (not the private key). Test with verbose output:

``` bash
ssh -vT git@github.com
```

**Getting “fatal: could not read Username”:**

You have a misconfigured remote URL. Check:

``` bash
git remote -v
cat .git/config
```

Remove any embedded credentials and use `git config credential.helper` instead.

**Using a monorepo or custom hostname:**

For self-hosted Git (Gitea, Gitbucket, GitLab), the same solutions apply. Update the remote hostname:

``` bash
git remote set-url origin git@your-gitlab.internal:username/repo.git
```

Or for HTTPS with PAT on GitLab:

``` bash
git remote set-url origin https://your-gitlab.internal/username/repo.git
git config credential.helper store
```

## One-Time Credential Override

If you need to authenticate for a single push without saving credentials:

``` bash
git push https://your-username:your-token@github.com/your-username/your-repo.git main
```

Don’t store this in your shell history. Use a credential helper instead for regular work.
