---
title: "tpm_getpcrhash(8)"
name: "tpm_getpcrhash"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_getpcrhash/"
description: "tpm_getpcrhash"
---

<p>tpm_getpcrhash</p>
<h2>Synopsis</h2>
<p><code>tpm_getpcrhash</code> [<code>-r HOST</code>] [<code>-hv</code>] UUID-FILE HASH-FILE PCR-VALUE-FILE PCRS</p>
<h2>Description</h2>
<p>The program returns the signed data produced by a TPM quote in the file HASH-FILE and the list of Platform Configuration Register values in the file PCR-VALUE-FILE. PCRS is a sequence of integers that specify the Platform Configuration Registers used to produce the signed data. The key used for the operation is the one registered under the UUID in UUID-FILE. The nonce used while quoting is unpredictable. The nonce field in the signed data is ignored when using the signed data to verify a quote.</p>
<dl>
<dt>-r HOST</p>
<dd>Perform operation on remote HOST.</p>
<dt>-h</p>
<dd>Display command usage info.</p>
<dt>-v</p>
<dd>Display command version info.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_quote_tools/">tpm_quote_tools</a></code>(8), <code><a href="/docs/linux/man/8-tpm_loadkey/">tpm_loadkey</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getquote/">tpm_getquote</a></code>(8), <code><a href="/docs/linux/man/8-tpm_verifyquote/">tpm_verifyquote</a></code>(8), <code><a href="/docs/linux/man/8-tpm_updateprchash/">tpm_updateprchash</a></code>(8) </p>
