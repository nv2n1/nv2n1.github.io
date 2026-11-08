---
title: "Understanding PGP: A Technical Reference Guide"
date: 2024-09-08 08:27:52 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/a-comprehensive-guide-to-pgp-technical-deep-dive/
---

PGP combines symmetric and asymmetric encryption to achieve both speed and security:

**Symmetric Encryption**: The message itself is encrypted using a random session key with an algorithm like AES-256. This is computationally fast for large files.

**Asymmetric Encryption**: The session key is then encrypted with the recipient’s public key using RSA or ECC. Only the holder of the corresponding private key can decrypt it.

**Digital Signatures**: You sign a message with your private key, producing a signature that others verify using your public key. This proves authenticity and non-repudiation—the signer cannot later deny signing the message.

## The Web of Trust vs. Public Key Infrastructure

PGP’s “Web of Trust” model decentralizes identity verification. Instead of relying on a certificate authority (CA) to vouch for you, users directly sign each other’s keys at key signing parties or online. When you trust someone’s key and they’ve signed others’ keys, you transitively trust those keys too.

This differs from X.509 PKI (used in HTTPS), where a centralized CA issues and revokes certificates. The Web of Trust requires more effort to bootstrap but offers resilience against CA compromise. In practice, most PGP users now rely on key servers and fingerprint verification rather than building deep webs.

## Modern GnuPG Workflow

GnuPG (GPG) is the FOSS implementation of PGP and remains the standard tool. Here’s a practical setup:

**Generate a key pair**:

``` bash
gpg --full-generate-key
```

Choose RSA (option 1), 4096 bits, and set an expiration date (1-2 years is reasonable). Add a strong passphrase.

**List your keys**:

``` bash
gpg --list-keys
gpg --list-secret-keys
```

**Export your public key for distribution**:

``` bash
gpg --export --armor your-email@example.com > pubkey.asc
```

**Sign and encrypt a file for a recipient**:

``` bash
gpg --sign --encrypt --recipient recipient@example.com document.txt
```

This creates `document.txt.gpg`.

**Decrypt and verify a signed file**:

``` bash
gpg --decrypt document.txt.gpg
```

GPG automatically verifies the signature and displays the signer’s information.

**Sign code commits** (essential for developers):

``` bash
git config user.signingkey your-key-id
git commit -S -m "Your message"
```

Verify commits with:

``` bash
git log --show-signature
```

## Key Management and Best Practices

**Passphrase Protection**: Always protect your private key with a strong passphrase. Your passphrase is the only thing preventing someone with file system access from using your key.

**Key Expiration**: Set expiration dates on your keys (1–2 years). If a key is compromised, a reasonable expiration limits the window of vulnerability. You can extend the expiration without regenerating the key:

``` bash
gpg --edit-key your-email@example.com
> expire
> save
```

**Subkeys**: Consider using separate subkeys for signing and encryption. Your master key stays offline in cold storage, while subkeys handle daily operations. If a subkey is compromised, you revoke it without replacing your identity:

``` bash
gpg --edit-key your-email@example.com
> addkey
```

**Revocation Certificate**: Generate and store a revocation certificate immediately after key creation. If your key is compromised or lost, this allows you to invalidate it:

``` bash
gpg --gen-revoke your-email@example.com > revoke.asc
```

**Key Backup**: Export your private key securely and store it offline:

``` bash
gpg --export-secret-keys --armor your-email@example.com > private-key.asc
```

Keep this file encrypted in cold storage (encrypted USB, hardware wallet, etc.).

## PGP in 2026: Current Relevance

PGP remains indispensable for specific use cases:

**Developers**: GPG signing for git commits is standard practice. Most platforms (GitHub, GitLab, Gitea) support signature verification on commits and tags. This prevents impersonation and proves authorship.

**Sensitive Document Distribution**: Journalists, lawyers, and security researchers use PGP to send documents that may be intercepted or stored by intermediaries. Unlike Signal (which requires both parties online), PGP works asynchronously over email or file transfer.

**Cryptocurrency and Custody**: Hardware wallet seed phrases and Shamir Secret Sharing backups are routinely encrypted with PGP before being distributed to multiple custodians or stored in the cloud.

**Legacy System Integration**: Many enterprise systems, compliance frameworks, and government communications still mandate PGP for data classification and secure transfers.

## Modern Alternatives

**Age**: A modern file encryption tool (successor to implicit in many Go projects) that offers simplicity and strong cryptography. No key servers, no trust model—just encrypt for specific recipients or passphrases. Excellent for scripting and DevOps:

``` bash
age -R recipient-pubkey.txt -o document.enc document.txt
age -d -i recipient-privkey.txt -o document.txt document.enc
```

**Minisign**: A minimal tool for signing and verifying files without the complexity of key management. Useful for software distribution:

``` bash
minisign -Sm document.txt
minisign -Vm document.txt -P pubkey
```

**TweetNaCl.js and libsodium**: Cryptographic libraries for developers who want fine-grained control without PGP’s legacy overhead.

Age and Minisign are simpler and less error-prone for file encryption, but they lack PGP’s Web of Trust and are not suitable for email. Choose based on your threat model: if you need decentralized identity verification and asynchronous communication, PGP is still the right answer.
