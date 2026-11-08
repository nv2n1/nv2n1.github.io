---
title: "Generating RSA Key Pairs with OpenSSL"
date: 2019-11-17 05:04:25 +0000
layout: post
canonical: https://www.systutorials.com/how-to-generate-a-pair-of-rsa-private-and-public-key-in-linux/
---

RSA (Rivest–Shamir–Adleman) underpins SSH authentication, TLS certificates, code signing, and encryption across most Linux systems. OpenSSL is the standard tool for generating and managing these keys.

## Verify OpenSSL Installation

OpenSSL is bundled with virtually all distributions. Check your version:

``` bash
openssl version
```

If it’s missing:

``` bash
# Ubuntu/Debian
sudo apt-get install openssl

# RHEL/CentOS/Fedora
sudo dnf install openssl

# Alpine
apk add openssl
```

## Generate a Private Key

Use `openssl genpkey` to create RSA private keys. This is the modern standard; the older `genrsa` command is deprecated.

For most use cases (development, testing, internal services):

``` bash
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
```

For production systems, certificates, or anything handling sensitive data:

``` bash
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096
```

## Encrypt Your Private Key

Always protect your private key with a passphrase. Add the `-aes256` flag:

``` bash
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096 -aes256
```

You’ll be prompted twice:

    Enter PEM pass phrase:
    Verifying - Enter PEM pass phrase:

Without encryption, anyone with filesystem access can use your key. Store passphrases in a password manager or secure vault—you’ll need it every time you use the key.

## Extract the Public Key

Generate the corresponding public key from your encrypted (or unencrypted) private key:

``` bash
openssl pkey -in private_key.pem -pubout -out public_key.pem
```

If your private key is encrypted, you’ll be prompted for the passphrase. The `pkey` command transparently handles both PKCS#1 and PKCS#8 formats.

## Inspect Your Keys

View the private key structure:

``` bash
openssl pkey -in private_key.pem -text -noout
```

Output includes the RSA modulus, public exponent, private exponent, and prime factors:

    Private-Key: (4096 bit, 2 primes)
    modulus:
        00:c8:ef:d4:50:2f:8b:66:86:a5:fe:d4:ed:17:3a:
        ...
    publicExponent: 65537 (0x10001)
    privateExponent:
        ...

View the public key structure:

``` bash
openssl pkey -in public_key.pem -pubin -text -noout
```

This shows the modulus and public exponent (typically 65537).

Check the file format directly:

``` bash
cat private_key.pem
```

Encrypted keys display as:

    -----BEGIN ENCRYPTED PRIVATE KEY-----
    MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIa1lJ...
    -----END ENCRYPTED PRIVATE KEY-----

Public keys show as:

    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2v3lFA...
    -----END PUBLIC KEY-----

## Key Size Guidelines

- **2048 bits**: Acceptable for most applications and non-critical internal services. Equivalent to 112-bit symmetric security.
- **3072 bits**: Better long-term security margin. Good compromise for certificates and general production use.
- **4096 bits**: Recommended for sensitive applications, high-value targets, and new key material. Slightly slower but the performance cost is negligible.
- **8192+ bits or larger**: Rarely justified in practice. The additional security gain doesn’t offset the computational overhead.

## Generate SSH Keys

Create a passwordless or passphrase-protected SSH key:

``` bash
openssl genpkey -algorithm RSA -out ~/.ssh/id_rsa -pkeyopt rsa_keygen_bits:4096 -aes256
chmod 600 ~/.ssh/id_rsa
```

Extract the public key:

``` bash
openssl pkey -in ~/.ssh/id_rsa -pubout -out ~/.ssh/id_rsa.pub
chmod 644 ~/.ssh/id_rsa.pub
```

Add the public key to remote servers for passwordless authentication:

``` bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

On target servers, ensure `~/.ssh/authorized_keys` contains your public key and has correct permissions:

``` bash
chmod 600 ~/.ssh/authorized_keys
```

Note: If you prefer using `ssh-keygen` instead, it generates keys in OpenSSH format by default. Either tool works, but OpenSSL’s `pkey` command integrates better with certificate and CSR workflows.

## Create TLS Certificate Signing Requests

Generate a private key for a web server or CSR:

``` bash
openssl genpkey -algorithm RSA -out server.key -pkeyopt rsa_keygen_bits:2048
```

Create a certificate signing request (CSR) to submit to a certificate authority:

``` bash
openssl req -new -key server.key -out server.csr
```

You’ll be prompted for certificate details: country, organization, common name (domain), and other fields. Fill them accurately—the CA will verify them.

## Verify Key Pair Consistency

Confirm that a public and private key belong together by comparing their moduli:

``` bash
openssl pkey -in private_key.pem -noout -modulus | openssl md5
openssl pkey -in public_key.pem -pubin -noout -modulus | openssl md5
```

Both commands must produce identical MD5 hashes. If they differ, the keys don’t belong together and you’ve likely mixed up key files.

## Convert Between Key Formats

Older systems or legacy software may require PKCS#1 format instead of the modern PKCS#8 default. Convert when necessary:

``` bash
openssl pkey -in private_key.pem -traditional -out private_key_legacy.pem
```

The `-traditional` flag outputs the older, simpler format. This is rarely needed with modern tooling.

To convert a public key from PEM to OpenSSH format (for `authorized_keys`):

``` bash
ssh-keygen -f public_key.pem -i -mPKCS8 > id_rsa.pub
```

## Troubleshooting

**Permission denied errors**: Private keys must be readable only by the owner:

``` bash
chmod 600 private_key.pem
```

**Bad password read**: Passphrases are case-sensitive. Verify capitalization and special characters carefully.

**Key generation hangs or is very slow**: On systems with low entropy, key generation can stall. Check available entropy:

``` bash
cat /proc/sys/kernel/random/entropy_avail
```

If consistently below 1000, install an entropy provider:

``` bash
# Ubuntu/Debian
sudo apt-get install rng-tools
sudo systemctl start rng-tools

# RHEL/CentOS/Fedora
sudo dnf install rng-tools
sudo systemctl start rngd
```

**Incompatible format errors**: If legacy tools reject your key, try the PKCS#1 conversion above or verify the tool’s documentation for supported formats.

**Can’t read encrypted key**: Ensure the passphrase is entered correctly. If you’ve forgotten it, the key is effectively lost—generate a new one.
