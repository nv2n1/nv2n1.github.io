---
title: "Managing Multiple Git Server Keys"
date: 2018-03-24 08:19:46 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-use-different-keys-for-different-git-servers/
---

When you work with multiple git servers or need different credentials for different hosts, SSH’s config file lets you specify which key to use for each server. This is cleaner than managing aliases or environment variables.

## Setting Up ~/.ssh/config

Create or edit `~/.ssh/config` and add entries for each server:

    Host git.example.org
      Port 22111
      IdentityFile ~/.ssh/id_rsa.git.example.org
      User git

    Host code.example.org
      Port 22
      IdentityFile ~/.ssh/id_rsa.code.example.org
      User git

    Host github.com
      HostName github.com
      IdentityFile ~/.ssh/id_rsa.github
      User git

Each `Host` block specifies:

- **Port**: SSH port if non-standard (default is 22)
- **IdentityFile**: Path to the private key for this server
- **User**: SSH username (usually `git` for git servers)
- **HostName**: The actual hostname if different from the `Host` alias

Set proper permissions:

``` bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_rsa.*
```

## Using the Configuration

Once configured, git automatically uses the right key based on the remote URL. Clone normally:

``` bash
git clone git@git.example.org:team/project.git
git clone git@code.example.org:org/repo.git
git clone git@github.com:user/repo.git
```

Git matches the hostname in your URL to the `Host` entry and applies the corresponding configuration.

## Common Patterns

**Multiple accounts on the same server** — use host aliases:

    Host github-work
      HostName github.com
      IdentityFile ~/.ssh/id_rsa.work
      User git

    Host github-personal
      HostName github.com
      IdentityFile ~/.ssh/id_rsa.personal
      User git

Then clone work repos with `git@github-work:company/repo.git` and personal repos with `git@github-personal:username/repo.git`.

**Self-hosted servers with custom ports**:

    Host gitlab.internal
      HostName gitlab.company.local
      Port 2222
      IdentityFile ~/.ssh/id_rsa.internal
      User git

## Debugging SSH Issues

Verify which key is being used for a specific host:

``` bash
ssh -v git@github.com
```

Look for lines like `Offering public key` or `Trying private key` to confirm the correct identity file is being attempted.

Test the configuration without cloning:

``` bash
ssh -T git@github.com
```

This connects and authenticates without performing git operations — useful for verifying setup.

## Ed25519 Keys (Modern Alternative)

Consider using Ed25519 keys instead of RSA for better security and smaller key size:

``` bash
ssh-keygen -t ed25519 -C "git@example.org" -f ~/.ssh/id_ed25519.example
```

Then reference in config:

    Host git.example.org
      IdentityFile ~/.ssh/id_ed25519.example

## Key Points

- SSH checks `~/.ssh/config` before attempting authentication, so the right key is always selected automatically
- The `Host` value in the config file must match the hostname in your git remote URL exactly (unless you use `HostName` to redirect)
- If a server rejects your key, verify the public key is added to that server’s authorized_keys and that file permissions are correct (700 for the directory, 600 for the file)
- You can test multiple identities with `IdentityFile` entries — SSH tries them in order until one works

## Git Workflow Tips

Effective Git usage goes beyond knowing individual commands. Consider adopting a branching strategy that suits your team size. Feature branching works well for small teams, while GitFlow or trunk-based development scales better for larger organizations.

Always write descriptive commit messages. A good commit message explains what changed and why, not just what. Use the imperative mood: “Add feature” not “Added feature”.

## Useful Git Shortcuts

Add these aliases to your Git configuration for faster daily workflows:

```wp-block-code
[alias]
    st = status -sb
    co = checkout
    br = branch -v
    lg = log --oneline --graph --decorate -20
    unstage = reset HEAD --
    amend = commit --amend --no-edit
    last = log -1 HEAD --stat
```

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
