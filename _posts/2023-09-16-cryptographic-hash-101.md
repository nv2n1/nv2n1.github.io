---
title: "Understanding Cryptographic Hash Functions"
date: 2023-09-16 06:28:42 +0000
author: "Tony"
layout: post
canonical: https://www.systutorials.com/cryptographic-hash-101/
---

A cryptographic hash function is a mathematical algorithm that takes any input—a file, password, transaction, or string of any length—and produces a fixed-length output called a “hash” or “digest.” The output is always the same size regardless of input size. SHA-256, for example, always produces a 256-bit (64 hexadecimal character) output.

## Core Properties

**Deterministic**\
The same input always produces identical output. This is foundational: if hashing isn’t deterministic, it’s not cryptographically secure.

**One-Way (Preimage Resistance)**\
Given a hash, you cannot feasibly compute the original input. This is computationally irreversible—trying to reverse it requires brute force across an astronomically large keyspace.

**Avalanche Effect (Sensitivity)**\
A single bit change in input produces a completely different hash. Change one character in a file, and the hash becomes unrecognizable. This property catches tampering immediately.

**Collision Resistance**\
Two different inputs should never produce the same hash. A strong hash function makes finding collisions computationally infeasible. This is critical for security—if collisions exist, an attacker could forge transactions or files.

## Common Cryptographic Hash Functions

**SHA-2 Family (SHA-256, SHA-512)**\
Industry standard. SHA-256 produces 256-bit digests and is used in Bitcoin, TLS certificates, and most Unix password systems. Still considered secure as of 2026, though NIST recommends SHA-512 for new applications due to larger digest size.

**SHA-3 (Keccak)**\
NIST’s newer standard. Used in Ethereum and some modern protocols. More resistant to certain theoretical attacks than SHA-2, though SHA-2 remains secure.

**BLAKE2 / BLAKE3**\
Faster than MD5, SHA-2, and SHA-3 while being at least as secure. BLAKE3 offers parallelization and streaming hashing. Popular in modern systems like Kubernetes and distributed storage.

**MD5 and SHA-1**\
Cryptographically broken. Do not use for security-sensitive applications. MD5 collisions are trivial to generate; SHA-1 has practical collision attacks. Legacy systems still encounter them, but they’re deprecated.

## Practical Applications

**Data Integrity**\
Hash files to verify they haven’t been modified. A single bit flip in a file changes its hash completely. This catches network transmission errors or tampering:

``` bash
sha256sum file.tar.gz > file.sha256
sha256sum -c file.sha256
```

**Password Storage**\
Hash passwords with a salt (random data) so identical passwords produce different hashes. Never store plaintext passwords. Modern approach uses Argon2 or bcrypt with salt:

``` bash
# Don't use plain SHA-256 for passwords—use bcrypt or Argon2
python3 -c "import bcrypt; print(bcrypt.hashpw(b'password', bcrypt.gensalt()).decode())"
```

**Blockchain and Distributed Systems**\
Bitcoin uses SHA-256 to secure transactions and create the immutable ledger. Changing a single transaction requires recalculating every subsequent block’s hash—computationally prohibitive. Ethereum uses Keccak-256 similarly.

**Certificate Pinning and TLS**\
Hash values of public certificates are pinned in applications to prevent MITM attacks. If a certificate changes, the hash changes, triggering an alert.

**Git Commits**\
Git uses SHA-1 (being phased to SHA-256) to hash commits. Each commit’s hash is based on its contents, parent commit, timestamp, and author. Tamper with history, and hashes diverge from the network’s version.

## Hash Collisions and Vulnerabilities

Theoretical collision attacks exist for older algorithms:

- **MD5**: Practical collisions; broken.
- **SHA-1**: Practical attacks; deprecated in TLS and certificates.
- **SHA-256/SHA-3**: No known practical collisions; secure.

A “length extension attack” affects some hash functions (like SHA-1, SHA-256): given a hash and message length, an attacker can compute valid hashes for extended messages without knowing the original input. HMAC (Hash-based Message Authentication Code) mitigates this by using a secret key.

## Modern Hashing: Beyond Digests

**HMAC (Hash-based Message Authentication Code)**\
Combines hashing with a secret key. Verifies both authenticity and integrity:

``` bash
echo -n "message" | openssl dgst -sha256 -mac HMAC -macopt key:secret
```

**Zero-Knowledge Proofs (ZKPs)**\
Use hashing alongside other cryptographic primitives to prove statements without revealing underlying data. A blockchain can verify a transaction is valid (correct nonce, sufficient balance) without exposing user account details.

**Content-Addressable Storage**\
Systems like IPFS use content hashes as immutable identifiers. Files are stored and retrieved by their SHA-256 hash. Corruption is immediately detectable.

## Best Practices

- Use **SHA-256 or SHA-3** for new systems requiring cryptographic security.
- Use **BLAKE3** for performance-critical applications.
- Use **Argon2** or **bcrypt** for password hashing—never plain SHA.
- Always use **HMAC** for authenticated messages requiring both integrity and authenticity.
- Include **salt** when hashing passwords; regenerate per password.
- Verify hash values over **separate, secure channels** to avoid man-in-the-middle attacks.
- Keep hash functions updated; follow NIST recommendations as standards evolve.

Hash functions are foundational to modern security. Understanding their properties and limitations is essential for designing systems that resist tampering and maintain data integrity.
