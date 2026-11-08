---
title: "Automating File Encryption with OpenSSL"
date: 2019-11-16 03:53:09 +0000
layout: post
canonical: https://www.systutorials.com/how-to-encrypt-a-file-using-openssl-on-linux-non-interactively/
---

OpenSSL’s `enc` command supports passing passphrases programmatically rather than prompting interactively. This is essential for automation—cron jobs, CI/CD pipelines, backup scripts, and batch processing.

## Basic encryption with environment variables

The safest approach is storing the passphrase in an environment variable, keeping it out of process listings and shell history:

``` bash
export PASS=examplepass
openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass env:PASS
```

The `-pass env:PASS` option tells OpenSSL to read the passphrase from the `PASS` environment variable rather than prompting. This prevents the passphrase from appearing in `ps` output or command history.

To decrypt:

``` bash
export PASS=examplepass
openssl enc -aes-256-cbc -d -in file.tgz.enc -out file.tgz -pass env:PASS
```

## Passphrase input methods

OpenSSL supports multiple input methods depending on your security constraints:

**Pass via stdin:**

``` bash
echo -n "examplepass" | openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass stdin
```

**Pass via file:**

``` bash
openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass file:/path/to/passfile
```

**Direct command-line argument (least secure, visible in process list):**

``` bash
openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass pass:examplepass
```

Avoid the `pass:` method in production—process arguments are visible to other users on the system via `ps` and `/proc/[pid]/cmdline`.

## Strengthening OpenSSL enc encryption

The `openssl enc` command derives keys from passphrases using EVP_BytesToKey. Modern OpenSSL versions default to SHA-256, but explicitly specify it for consistency across systems:

``` bash
export PASS=examplepass
openssl enc -aes-256-cbc -md sha256 -in file.tgz -out file.tgz.enc -pass env:PASS
```

The `-md sha256` flag ensures the key derivation function uses SHA-256 rather than weaker defaults on older systems.

For even stronger security with PBKDF2 key derivation, use the `-pbkdf2` flag (available in OpenSSL 1.1.1+):

``` bash
export PASS=examplepass
openssl enc -aes-256-cbc -pbkdf2 -in file.tgz -out file.tgz.enc -pass env:PASS
```

PBKDF2 applies many iterations of the hash function, making brute-force attacks significantly slower.

## When to use GPG instead

For new projects requiring higher assurance, use GPG instead of `openssl enc`. GPG uses PBKDF2 for key derivation and provides better integrity protection:

``` bash
export PASS=examplepass
gpg --batch --yes --symmetric --cipher-algo AES256 --passphrase "$PASS" file.tgz
```

This produces `file.tgz.gpg`. Decrypt with:

``` bash
gpg --batch --yes --passphrase "$PASS" --output file.tgz file.tgz.gpg
```

GPG is preferable for long-term data retention and compliance-sensitive environments. It also supports key-based encryption instead of passphrases, which is more appropriate for automated systems with key management.

## Practical backup script example

Here’s a complete automation example that encrypts and removes the original:

``` bash
#!/bin/bash
set -e

BACKUP_FILE="backup-$(date +%Y%m%d).tar.gz"
ENCRYPTED_FILE="${BACKUP_FILE}.enc"
PASS_FILE="/root/.backup_pass"  # Must have permissions 0600

if [ ! -r "$PASS_FILE" ]; then
    echo "Error: passphrase file not readable" >&2
    exit 1
fi

# Create backup
tar czf "$BACKUP_FILE" /data

# Encrypt with passphrase from file
PASS=$(cat "$PASS_FILE")
openssl enc -aes-256-cbc -pbkdf2 -in "$BACKUP_FILE" -out "$ENCRYPTED_FILE" -pass env:PASS

# Verify encryption succeeded before deleting original
if openssl enc -aes-256-cbc -pbkdf2 -d -in "$ENCRYPTED_FILE" -pass env:PASS | tar tzf - > /dev/null 2>&1; then
    rm "$BACKUP_FILE"
    unset PASS
else
    echo "Encryption verification failed" >&2
    unset PASS
    exit 1
fi
```

Create the passphrase file with restricted permissions:

``` bash
chmod 600 /root/.backup_pass
echo "your-secure-passphrase" > /root/.backup_pass
```

## Memory management for sensitive passphrases

Always unset environment variables after use:

``` bash
export PASS=examplepass
openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass env:PASS
unset PASS
```

For critical applications where shell history retention is a concern, use a temporary file that’s securely wiped:

``` bash
PASS_TEMP=$(mktemp)
chmod 600 "$PASS_TEMP"
echo -n "examplepass" > "$PASS_TEMP"
openssl enc -aes-256-cbc -in file.tgz -out file.tgz.enc -pass file:"$PASS_TEMP"
shred -ufz "$PASS_TEMP"
```

The `shred` command overwrites the file multiple times before deletion, preventing recovery via filesystem forensics. On systems with journaling filesystems (ext4, XFS, Btrfs), physical recovery may still be possible—for highly sensitive data, consider full-disk encryption instead.

## Verifying encrypted files

Ensure encryption succeeded and files aren’t corrupted by decrypting and checking integrity in one operation:

``` bash
openssl enc -aes-256-cbc -d -in file.tgz.enc -pass env:PASS | tar tzf - > /dev/null && echo "OK"
```

This decrypts to stdout, verifies the tar archive structure, and leaves no decrypted copy on disk. Exit code 0 means both encryption and archive integrity are valid.

For larger archives, save decrypted output to a temporary file and verify:

``` bash
TEMP_FILE=$(mktemp)
trap "shred -ufz '$TEMP_FILE'" EXIT
openssl enc -aes-256-cbc -d -in file.tgz.enc -pass env:PASS -out "$TEMP_FILE"
tar tzf "$TEMP_FILE" > /dev/null
```

The `trap` ensures the temporary file is securely wiped even if verification fails.

## Handling encryption in CI/CD pipelines

Store passphrases in CI/CD secrets management systems (GitHub Secrets, GitLab CI variables, Vault, etc.) rather than in scripts or configuration files:

``` bash
#!/bin/bash
# In CI/CD environment with BACKUP_PASSPHRASE set as a secret
openssl enc -aes-256-cbc -pbkdf2 -in backup.tgz -out backup.tgz.enc -pass env:BACKUP_PASSPHRASE
```

Never commit passphrases, keys, or `.env` files to version control. Use `.gitignore` to exclude sensitive files and validate in pre-commit hooks.
