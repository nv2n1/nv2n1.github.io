---
title: "tpm_revokeek(8)"
name: "tpm_revokeek"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_revokeek/"
description: "tpm_revokeek – revokes the Endorsement Key Pair of the TPM"
---

<p>TPM Management &#8211; tpm_revokeek<br />
 </center></p>
<h2>Name</h2>
<p>tpm_revokeek &#8211; revokes the Endorsement Key Pair of the TPM</p>
<h2>Synopsis</h2>
<p><code>tpm_revokeek</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_revokeek</code> clears the TPM revocable Endorsement Key Pair (via the TPM_RevokeEndorsementKey API). This command erases all counters (except the base one), erases the Ek, the SRK, the owner auth and any NVRAM locked to the owner auth. It does not touch the delegation tables or other NVRAM.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level. .TP <code>-i</code>, <code>&#8211;infile</code> [input file] Specifies the file that contains the authorization information required to revoke the Ek (secret data generated during the revocable Ek creation process). Only the first 20 bytes of this file are used and the remaining ones are ignored. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_createek/">tpm_createek</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getpubek/">tpm_getpubek</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
