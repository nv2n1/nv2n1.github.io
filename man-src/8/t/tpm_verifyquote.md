---
title: "tpm_verifyquote(8)"
name: "tpm_verifyquote"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_verifyquote/"
description: "tpm_verifyquote"
---

<p>tpm_verifyquote</p>
<h2>Synopsis</h2>
<p><code>tpm_verifyquote</code> [<code>-hv</code>] PUBKEY-FILE HASH-FILE NONCE-FILE [QUOTE-FILE]</p>
<h2>Description</h2>
<p>The program verifies the signature produced by a TPM quote in the file QUOTE-FILE, or when absent, the quote read from standard input. The file PUBKEY-FILE contains the public key used to validate the signature. The file HASH-FILE contains the signed data generated using the same key and Platform Configuration Registers used to generate the quote. Critically, the signed data includes the PCR composite hash used to validate that the PCRs contain their expected values. The file NONCE-FILE contains the nonce used to generate the quote.</p>
<dl>
<dt>-h</p>
<dd>Display command usage info.</p>
<dt>-v</p>
<dd>Display command version info.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_quote_tools/">tpm_quote_tools</a></code>(8), <code><a href="/docs/linux/man/8-tpm_mkaik/">tpm_mkaik</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getpcrhash/">tpm_getpcrhash</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getquote/">tpm_getquote</a></code>(8) </p>
