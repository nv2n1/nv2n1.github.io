---
title: "Generating RSA Key Pairs in Go"
date: 2020-10-24 09:27:59 +0000
author: "David Yang"
layout: post
categories: [languages-frameworks]
canonical: /how-to-generate-rsa-private-and-public-key-pair-in-go-lang/
---

Go’s standard library provides everything needed to generate RSA key pairs and save them in PEM format. Here are the essential packages:

**crypto/rsa** — Implements RSA encryption per PKCS \#1 and RFC 8017. The `GenerateKey()` function creates a keypair of specified bit size.

**crypto/rand** — Provides `Reader`, a cryptographically secure random source. On Linux, it uses `getrandom(2)` when available, falling back to `/dev/urandom`.

**crypto/x509** — Handles key serialization. `MarshalPKCS1PrivateKey()` converts RSA private keys to PKCS \#1 ASN.1 DER format, and `MarshalPKIXPublicKey()` handles public keys in PKIX format.

**encoding/pem** — Encodes DER data into PEM blocks, the text format commonly used for key files.

## Basic Key Generation

Here’s a straightforward example that generates a 2048-bit RSA keypair and writes both keys to PEM files:

``` go
package main

import (
    "crypto/rand"
    "crypto/rsa"
    "crypto/x509"
    "encoding/pem"
    "fmt"
    "os"
)

func main() {
    // Generate RSA keypair
    privateKey, err := rsa.GenerateKey(rand.Reader, 2048)
    if err != nil {
        fmt.Printf("failed to generate private key: %v\n", err)
        os.Exit(1)
    }

    publicKey := &privateKey.PublicKey

    // Write private key to file
    if err := savePrivateKey(privateKey); err != nil {
        fmt.Printf("failed to save private key: %v\n", err)
        os.Exit(1)
    }

    // Write public key to file
    if err := savePublicKey(publicKey); err != nil {
        fmt.Printf("failed to save public key: %v\n", err)
        os.Exit(1)
    }

    fmt.Println("Keys generated successfully")
    fmt.Printf("Private key: private.pem\n")
    fmt.Printf("Public key: public.pem\n")
}

func savePrivateKey(key *rsa.PrivateKey) error {
    privateKeyBytes := x509.MarshalPKCS1PrivateKey(key)
    block := &pem.Block{
        Type:  "RSA PRIVATE KEY",
        Bytes: privateKeyBytes,
    }

    file, err := os.Create("private.pem")
    if err != nil {
        return fmt.Errorf("failed to create private.pem: %w", err)
    }
    defer file.Close()

    if err := pem.Encode(file, block); err != nil {
        return fmt.Errorf("failed to encode private key: %w", err)
    }

    return nil
}

func savePublicKey(key *rsa.PublicKey) error {
    publicKeyBytes, err := x509.MarshalPKIXPublicKey(key)
    if err != nil {
        return fmt.Errorf("failed to marshal public key: %w", err)
    }

    block := &pem.Block{
        Type:  "PUBLIC KEY",
        Bytes: publicKeyBytes,
    }

    file, err := os.Create("public.pem")
    if err != nil {
        return fmt.Errorf("failed to create public.pem: %w", err)
    }
    defer file.Close()

    if err := pem.Encode(file, block); err != nil {
        return fmt.Errorf("failed to encode public key: %w", err)
    }

    return nil
}
```

## Key Size Considerations

For new applications, use at least 2048 bits. If you need longer-term security (beyond 2030), consider 4096 bits:

``` go
privateKey, err := rsa.GenerateKey(rand.Reader, 4096)
```

Be aware that larger keys increase CPU usage during encryption and decryption operations.

## Reading Keys Back

To load and use the generated keys later:

``` go
package main

import (
    "crypto/rsa"
    "crypto/x509"
    "encoding/pem"
    "fmt"
    "os"
)

func loadPrivateKey(filename string) (*rsa.PrivateKey, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }

    block, _ := pem.Decode(data)
    if block == nil {
        return nil, fmt.Errorf("failed to parse PEM block")
    }

    privateKey, err := x509.ParsePKCS1PrivateKey(block.Bytes)
    if err != nil {
        return nil, err
    }

    return privateKey, nil
}

func loadPublicKey(filename string) (*rsa.PublicKey, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }

    block, _ := pem.Decode(data)
    if block == nil {
        return nil, fmt.Errorf("failed to parse PEM block")
    }

    pub, err := x509.ParsePKIXPublicKey(block.Bytes)
    if err != nil {
        return nil, err
    }

    publicKey, ok := pub.(*rsa.PublicKey)
    if !ok {
        return nil, fmt.Errorf("public key is not RSA")
    }

    return publicKey, nil
}
```

## Error Handling Best Practices

Always use wrapped errors (`fmt.Errorf` with `%w`) for better error chain tracking. Defer file closes to ensure resources are cleaned up properly. For production code, validate key sizes and consider using constants for bit lengths to avoid accidental weak key generation.

## File Permissions

When saving private keys, set restrictive file permissions:

``` go
if err := os.Chmod("private.pem", 0600); err != nil {
    fmt.Printf("failed to set permissions: %v\n", err)
}
```

This ensures only the file owner can read the private key, which is essential for security.
