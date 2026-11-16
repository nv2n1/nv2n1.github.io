---
title: "tpm_getpubek(8)"
name: "tpm_getpubek"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_getpubek/"
description: "tpm_getpubek – display the public portion of the TPM’s Endorsement Key"
---

<p>TPM Management &#8211; tpm_getpubek<br />
 </center></p>
<h2>Name</h2>
<p>tpm_getpubek &#8211; display the public portion of the TPM&#8217;s Endorsement Key</p>
<h2>Synopsis</h2>
<p><code>tpm_getpubek</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_getpubek</code> requests the TPM&#8217;s public portion of the Endorsement Key (via the TPM_ReadPubek API). This operation can be restricted to require owner authorization, in that case the command will prompt for the owner password and request the data. The key information is output on a successful call.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd>Set logging level.</dd>
<dt><code>-u</code>, <code>&#8211;unicode</code></dt>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</dd>
<dt><code>-z</code>, <code>&#8211;well-known</code></dt>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_restrictpubek/">tpm_restrictpubek</a></code>(8), <code><a href="/docs/linux/man/8-tpm_createek/">tpm_createek</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
</dl>