---
title: "tpm_mkaik(8)"
name: "tpm_mkaik"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_mkaik/"
description: "tpm_mkaik"
---

<p>tpm_mkaik</p>
<h2>Synopsis</h2>
<p><code>tpm_mkaik</code> [<code>-zuhv</code>] BLOB-FILE PUBKEY-FILE</p>
<h2>Description</h2>
<p>The program generates a TPM Attestation Identity Key and stores it in the file BLOB-FILE. The public key is stored in the file PUBKEY-FILE. The public key is DER encoded.</p>
<dl>
<dt>-z</p>
<dd>Use the well known secret used as the owner secret.</p>
<dt>-u</p>
<dd>Use TSS UNICODE encoding for passwords.</p>
<dt>-h</p>
<dd>Display command usage info.</p>
<dt>-v</p>
<dd>Display command version info.</dl>
<h2>Bugs</h2>
<p>Sometimes, when <code>tpm_mkaik</code> is invoked without the -z option, no password prompt appears. As a work around, use <code>tpm_changeownerauth</code> to set the secret to the well known one, generate the key, and then use <code>tpm_changeownerauth</code> to set the secret to its original value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_quote_tools/">tpm_quote_tools</a></code>(8), <code><a href="/docs/linux/man/8-tpm_changeownerauth/">tpm_changeownerauth</a></code>(8) </p>
