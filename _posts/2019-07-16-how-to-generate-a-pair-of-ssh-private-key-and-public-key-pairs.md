---
title: "SSH Key Pair Generation: Ed25519 and FIDO2 Best Practices"
date: 2019-07-16 04:07:38 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-generate-a-pair-of-ssh-private-key-and-public-key-pairs/
---

SSH keys provide secure, password-less authentication to remote systems. Choosing the right algorithm matters for security, compatibility, and operational stability.

## Generate an Ed25519 Key Pair

Ed25519 is the modern standard for SSH key generation. It offers stronger security properties than RSA, faster operations, and smaller key sizes.

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

You’ll be prompted to choose a file location (default: `~/.ssh/id_ed25519`) and optionally set a passphrase. Using a passphrase protects your private key if your system is compromised, though it requires entering the passphrase each time you use the key (unless you use ssh-agent).

Verify the key was created:

``` bash
ls -la ~/.ssh/id_ed25519*
```

You should see both `id_ed25519` (private key) and `id_ed25519.pub` (public key).

## Why Ed25519 Over RSA

- **Smaller key size**: Ed25519 keys are 68 characters versus RSA-4096’s 3,389 characters, making them faster to transmit and easier to manage.
- **Better security margins**: Ed25519 provides 128-bit equivalent security with mathematically stronger constructions than RSA.
- **Faster operations**: Key generation, signing, and verification are significantly faster than comparable RSA operations.
- **Fewer implementation issues**: RSA implementations have historically suffered from padding oracle attacks and other implementation bugs. Ed25519’s simpler design reduces these risks.

## ECDSA Keys (Alternative)

If you need broader compatibility with older systems, ECDSA is acceptable but less preferred than Ed25519:

``` bash
ssh-keygen -t ecdsa -b 521 -C "your_email@example.com"
```

Use 521-bit ECDSA, not smaller variants. Still, Ed25519 should be your first choice.

## Avoid RSA

While RSA-4096 remains acceptable, it’s slower and uses larger keys than Ed25519 with no security advantage. Don’t generate RSA keys unless you have specific compatibility requirements with legacy systems.

## Deploy Your Public Key to Remote Systems

Copy your public key to the remote server’s `~/.ssh/authorized_keys` file using `ssh-copy-id`:

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote_host
```

Alternatively, copy manually:

``` bash
cat ~/.ssh/id_ed25519.pub | ssh user@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

Set proper permissions on the remote system:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

If you’re adding keys to multiple servers, consider using configuration management tools like Ansible or Terraform to standardize `authorized_keys` across your infrastructure.

## Using ssh-agent for Passphrase Management

If you’ve protected your key with a passphrase (recommended), load it into ssh-agent to avoid repeated prompts:

``` bash
ssh-add ~/.ssh/id_ed25519
```

The agent will prompt for your passphrase once per session. Verify it’s loaded:

``` bash
ssh-add -l
```

On systemd systems, ssh-agent typically runs as a socket under `XDG_RUNTIME_DIR`. Ensure your `SSH_AUTH_SOCK` environment variable points to it:

``` bash
echo $SSH_AUTH_SOCK
```

If using a graphical desktop environment, your session manager usually starts ssh-agent automatically. On headless servers, you may need to start it manually:

``` bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

## Hardware-Backed SSH Keys (FIDO2)

For high-security environments, FIDO2 hardware keys (YubiKey, Titan, etc.) provide stronger protection by keeping the private key on the hardware device itself. This approach is increasingly common in enterprise environments.

Generate an ed25519-sk (Ed25519 security key) backed key, the modern FIDO2 standard:

``` bash
ssh-keygen -t ed25519-sk -C "your_email@example.com"
```

For systems that don’t yet support ed25519-sk, fall back to ecdsa-sk:

``` bash
ssh-keygen -t ecdsa-sk -C "your_email@example.com"
```

You’ll be prompted to touch your hardware key during generation and each time you use it for authentication. This provides phishing resistance—attackers cannot use stolen credentials because they lack physical access to your key.

Check your OpenSSH version with `ssh -V`. OpenSSH 8.2 or newer is required for security key support. If you’re on an older system, upgrade OpenSSH or use standard Ed25519 keys with a strong passphrase instead.

## Managing Multiple Keys

For different servers or roles, generate separate keys:

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_github -C "github@example.com"
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_prod -C "prod@example.com"
```

Configure SSH to use specific keys for different hosts in `~/.ssh/config`:

    Host github.com
        User git
        IdentityFile ~/.ssh/id_ed25519_github

    Host prod.example.com
        User deploy
        IdentityFile ~/.ssh/id_ed25519_prod
        Port 2222

You can also specify multiple identity files per host, and SSH will try them in order:

    Host *.prod.example.com
        User deploy
        IdentityFile ~/.ssh/id_ed25519_prod
        IdentityFile ~/.ssh/id_ed25519_backup

This approach prevents accidentally exposing credentials meant for one system to another and makes key rotation easier.

## Key Security Practices

**Use passphrases**: Protect your private key with a strong passphrase, especially on shared systems or laptops. A passphrase is your last line of defense if the key file is compromised.

**Rotate keys periodically**: Generate new keys every 1-2 years and remove old public keys from servers. Track which keys are deployed where using comments or a key inventory.

**Restrict key permissions**: Keep private keys readable only by your user:

``` bash
chmod 600 ~/.ssh/id_ed25519
chmod 700 ~/.ssh
```

Overly permissive permissions will cause SSH to refuse to use the key.

**Audit authorized_keys**: Regularly review `~/.ssh/authorized_keys` on remote systems to remove stale keys. On production systems, implement automated key auditing:

``` bash
ssh user@remote_host "cat ~/.ssh/authorized_keys"
```

**Use SSH key comments**: The `-C` flag adds identifying metadata to your public key, useful when managing many keys. Comments appear when you list keys with `ssh-add -l`, making it easier to identify which key is which.

**Disable password authentication**: Once SSH keys are deployed, disable password-based authentication on remote systems by setting `PasswordAuthentication no` in `/etc/ssh/sshd_config`. Reload sshd with:

``` bash
sudo systemctl reload ssh
```

**Monitor for unauthorized key additions**: Use tools like `aide` or `tripwire` to detect modifications to `~/.ssh/authorized_keys`. On high-security systems, consider using centralized key management with LDAP or dedicated SSH certificate authorities.

**Generate keys on secure systems**: Generate SSH keys on machines you trust, not on shared systems or in cloud shells where the key file might be logged or exposed.
