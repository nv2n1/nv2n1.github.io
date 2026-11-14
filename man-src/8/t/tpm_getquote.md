---
title: "tpm_getquote(8)"
name: "tpm_getquote"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_getquote/"
description: "tpm_getquote"
---

<p>tpm_getquote</p>
<h2>Synopsis</h2>
<p><code>tpm_getquote</code> [<code>-r HOST</code>] [<code>-p PCR-VALUES-FILE</code>] [<code>-hv</code>] UUID-FILE NONCE-FILE QUOTE-FILE PCRS</p>
<h2>Description</h2>
<p>The program returns the signature produced by a TPM quote in the file QUOTE-FILE. PCRS is a sequence of integers that specify the Platform Configuration Registers used to produce the signature. The key used for the operation is the one registered under the UUID in UUID-FILE. The nonce used is taken from the file NONCE-FILE.</p>
<dl>
<dt>-r HOST</p>
<dd>Perform operation on remote HOST.</p>
<dt>-p PCR-VALUE-FILE</p>
<dd>Store the current list of PCR values in PCR-VALUE-FILE.</p>
<dt>-h</p>
<dd>Display command usage info.</p>
<dt>-v</p>
<dd>Display command version info.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_quote_tools/">tpm_quote_tools</a></code>(8), <code><a href="/docs/linux/man/8-tpm_loadkey/">tpm_loadkey</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getpcrhash/">tpm_getpcrhash</a></code>(8), <code><a href="/docs/linux/man/8-tpm_verifyquote/">tpm_verifyquote</a></code>(8) </p>
