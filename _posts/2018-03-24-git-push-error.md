---
title: "Resolving Git Push 403 Forbidden: Authentication and Permissions"
date: 2018-03-24 11:47:40 +0000
layout: post
canonical: https://www.systutorials.com/git-push-error/
---

A 403 Forbidden error when running `git push` means your credentials aren’t valid or you lack permission to access the repository. This is one of the most common Git frustrations, but it’s usually fixable once you understand what’s actually happening.

## Why 403 Errors Happen

- Your authentication method has expired or been revoked
- Your GitHub Personal Access Token (PAT) has insufficient permissions or is outdated
- You’re using HTTPS with stored credentials that no longer work
- You don’t have write access to the repository
- The repository is archived or your organization has restricted your access
- SSH key permissions are incorrect or the key isn’t in your agent

## Diagnose the Problem

Start by checking your current remote configuration:

``` bash
git remote -v
```

This shows which URL your local repository uses. HTTPS output looks like:

    origin  https://github.com/username/repo.git (fetch)
    origin  https://github.com/username/repo.git (push)

SSH output looks like:

    origin  git@github.com:username/repo.git (fetch)
    origin  git@github.com:username/repo.git (push)

Next, check which authentication method Git is actually using:

``` bash
# For SSH
ssh -T git@github.com

# For HTTPS, attempt a push and note the error
git push
```

For SSH, you should see: `Hi username! You've successfully authenticated...`

## Solution 1: Switch to SSH (Recommended for Long-Term Use)

SSH avoids token expiration headaches and is more secure than HTTPS with tokens.

First, verify your SSH setup works:

``` bash
ssh -T git@github.com
```

If you get `Permission denied (publickey)`, you need to generate or add an SSH key. Generate a new key if you don’t have one:

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept the default location (`~/.ssh/id_ed25519`), then add a passphrase if desired.

Add the public key to GitHub:

``` bash
cat ~/.ssh/id_ed25519.pub
```

Copy the output and paste it into GitHub Settings → SSH and GPG keys → New SSH key.

Ensure your SSH key is loaded in the agent:

``` bash
ssh-add ~/.ssh/id_ed25519
```

Now update your remote URL:

``` bash
git remote set-url origin git@github.com:username/repo.git
```

Verify the change:

``` bash
git remote -v
```

Try pushing:

``` bash
git push origin main
```

## Solution 2: Use HTTPS with a Personal Access Token

If you need to use HTTPS (common in CI/CD pipelines), use a Personal Access Token instead of your GitHub password.

Generate a token on GitHub:

1.  Go to Settings → Developer settings → Personal access tokens → Tokens (classic)
2.  Click “Generate new token”
3.  Give it a descriptive name
4.  Select the `repo` scope for full repository access (or `public_repo` if the repo is public)
5.  Set an expiration date (90 days or less is recommended)
6.  Click “Generate token” and copy it immediately — you won’t see it again

Update your remote if needed:

``` bash
git remote set-url origin https://github.com/username/repo.git
```

To avoid entering credentials every push, configure a credential helper:

**On Linux (using in-memory cache):**

``` bash
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
```

**On macOS (using Keychain):**

``` bash
git config --global credential.helper osxkeychain
```

**On Windows (using Credential Manager):**

``` bash
git config --global credential.helper manager
```

On your next push, you’ll be prompted for username and password. Use your GitHub username and paste the PAT as the password.

## Solution 3: Clear Cached Credentials

If you have old or invalid credentials cached, clear them:

**On Linux/macOS:**

``` bash
rm ~/.git-credentials
```

**Using Git’s credential helper:**

``` bash
git credential reject
# Then type:
# host=github.com
# Press Enter twice
```

**On Windows, use Credential Manager GUI:**

Go to Control Panel → Credential Manager → Windows Credentials and remove GitHub entries.

## Verify Permissions and Repository Status

If you own the repository but still get 403:

- Check that the repository isn’t archived (archived repos are read-only)
- Verify your GitHub organization hasn’t restricted your access
- Confirm you have at least “Write” or “Maintain” access in repository settings
- If using a deploy key, ensure it has “Allow write access” enabled

If you’re pushing to someone else’s repository, you need:

- Direct write access, OR
- A pull request (if you have read access only)

## Test Your Fix

After making changes, attempt to push:

``` bash
git push origin main
```

Replace `main` with your actual branch name if different. A successful push shows:

    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (3/3), 456 bytes | 456.00 KiB/s, done.
    Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), done.
    To github.com:username/repo.git
       abc1234..def5678  main -> main

## Troubleshooting Checklist

- Run `git remote -v` and confirm the URL is correct
- Test authentication independently (`ssh -T git@github.com` or `git credential fill`)
- Check that your SSH key has the right permissions (600 for private key, 700 for `~/.ssh`)
- Verify the token/key hasn’t expired
- Confirm you have write access to the repository
- Try a different branch or a fresh clone to rule out local config issues

SSH is the long-term solution if you’re working regularly with Git. It’s more secure, doesn’t require token management, and works the same way across all platforms once configured.
