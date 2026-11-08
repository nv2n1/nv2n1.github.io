---
title: "Extracting EC Public Keys from Certificates with OpenSSL"
date: 2024-08-23 14:20:18 +0000
layout: post
canonical: https://www.systutorials.com/extracting-ec-public-keys-with-openssl/
---

Verification: You need the public key to verify digital signatures (e.g., in Bitcoin or TLS).\
Sharing: Public keys are meant to be shared, while the private key must remain secret.\
Conversion: Sometimes you need to convert a private key file into a public-only certificate for a web server or blockchain application.\
System Integration: Many tools require public keys in specific formats for authentication, encryption, or policy enforcement.

## Generate and Extract Keys

### Generate an EC private key

``` bash
openssl ecparam -genkey -name secp256k1 -noout -out private.pem
```

This creates a secp256k1 key (Bitcoin/Ethereum standard). Substitute `prime256v1` for TLS/web applications or `P-384` for higher security margins.

### Extract the public key

``` bash
openssl ec -in private.pem -pubout -out public.pem
```

The `-pubout` flag is essential — it outputs the public key in PKCS#8 format, compatible with most modern tools and libraries.

### View key details

``` bash
openssl ec -in private.pem -text -noout
```

This displays the curve parameters, key coordinates, and bit length. Useful for debugging key generation or verifying curve selection.

### Extract public key in different formats

If you need the raw X and Y coordinates for blockchain addresses or custom implementations:

``` bash
openssl ec -in private.pem -text -noout | grep -A 5 "pub:"
```

For SEC1 format (without PKCS#8 wrapping):

``` bash
openssl ec -in private.pem -pubout -outform PEM | openssl pkey -pubin -inform PEM -text -noout
```

## Curve Selection in 2026

**secp256k1**: The Bitcoin/Ethereum standard. Smaller keyspace than NIST curves; widely supported in blockchain libraries but consider it legacy for new TLS deployments.

**P-256 (prime256v1)**: NIST standard for TLS and government applications. Recommended for web servers and federal systems. Balances security and performance.

**P-384 and P-521**: Higher security margins. Use for long-term key material or when storing encrypted data that must remain secure beyond 2035.

**Ed25519**: Modern default for SSH, certificate signing, and crypto wallets. Faster than P-256, resistant to side-channel attacks, and increasingly standard in production. Generate with:

``` bash
openssl genpkey -algorithm ed25519 -out ed25519_key.pem
openssl pkey -in ed25519_key.pem -pubout -out ed25519_pub.pem
```

## Practical Workflows

### Extract public key for TLS certificate signing request (CSR)

``` bash
openssl ecparam -genkey -name prime256v1 -noout -out server.key
openssl req -new -key server.key -out server.csr
openssl ec -in server.key -pubout -out server.pub
```

### Convert private key to different format

Extract as SEC1 (traditional EC format):

``` bash
openssl pkey -in private.pem -out private-sec1.pem
```

Export in DER format for binary applications:

``` bash
openssl ec -in private.pem -pubout -outform DER -out public.der
```

### Verify a signature using extracted public key

After extracting the public key, verify a signature:

``` bash
openssl dgst -sha256 -verify public.pem -signature signature.bin data.txt
```

## File Permissions and HSM Storage

Always secure private keys immediately after generation:

``` bash
chmod 600 private.pem
```

Only the owning user can read the file. No group or world permissions.

In production environments, never store private keys on disk. Use:

- **Hardware Security Modules (HSM)**: Thales Luna, Yubihsm, or cloud HSM services (AWS CloudHSM, Azure Key Vault)
- **Trusted Platform Module (TPM)**: For local machine security; integrates with systemd and many modern Linux applications
- **Key Management Services (KMS)**: AWS KMS, Google Cloud KMS, or HashiCorp Vault for distributed systems

## Verify Key Consistency

Confirm that the extracted public key matches your private key:

``` bash
# Extract public from private, then compare
openssl ec -in private.pem -pubout | openssl pkey -pubin -text -noout > pub_from_priv.txt
openssl ec -in private.pem -pubout -out extracted.pem
openssl pkey -pubin -in extracted.pem -text -noout > pub_extracted.txt
diff pub_from_priv.txt pub_extracted.txt
```

No output means they match.
