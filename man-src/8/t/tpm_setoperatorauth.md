---
title: "tpm_setoperatorauth(8)"
name: "tpm_setoperatorauth"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setoperatorauth/"
description: "tpm_setoperatorauth – sets the operator authorization value in the TPM"
---

<p>TPM Management &#8211; tpm_setoperatorauth<br/>
 </center></p>
<h2>Name</h2>
<p>tpm_setoperatorauth &#8211; sets the operator authorization value in the TPM</p>
<h2>Synopsis</h2>
<p><code>tpm_setoperatorauth</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setoperatorauth</code> allows setting the operator authorization value in the TPM (via the TPM_SetOperatorAuth API). This operation prompts for the new password and a confirmation of it. The <code>&#8211;well-known</code> option tells the API to use the default TSS_WELL_KNOWN_SECRET (a 20-bytes array of zeros) as operator authorization information, instead of prompting for one.</p>
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
<dd>Use the default TSS_WELL_KNOWN_SECRET 20-bytes array of zeros as the operator password.</dd>
<dt><code>-p</code>, <code>&#8211;op_password_unicode</code></dt>
<dd>Use TSS UNICODE encoding for new operator password to comply with applications using TSS popup boxes </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
</dl>