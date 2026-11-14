---
title: "tpm_setclearable(8)"
name: "tpm_setclearable"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setclearable/"
description: "tpm_setclearable – disable TPM clear operations"
---

<p>TPM Management &#8211; tpm_setclearable<br />
 </center></p>
<h2>Name</h2>
<p>tpm_setclearable &#8211; disable TPM clear operations</p>
<h2>Synopsis</h2>
<p><code>tpm_setclearable</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setclearable</code> reports the status of the TPM&#8217;s flags regarding how the TPM can be cleared. This is the default behavior and also accessible via the <code>&#8211;status</code> option. Requesting a report of this status prompts for the owner password. The <code>&#8211;owner</code> option requests that the TPM disable clear operations (via the TPM_DisableOwnerClear API) disabling the owner from clearing out the ownership information. This operation prompts for the owner password. This operation is in effect until the current owner is cleared. The <code>&#8211;force</code> option (via the TPM_DisableForceClear API) disables using Phyiscal Presence to authorize a clear operation. This operation does not require authorization and will skip the owner password prompt. This operation is only in effect until a reboot.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</p>
<dt><code>-s</code>, <code>&#8211;status</code></p>
<dd>Report the status of flags regarding how the TPM can be cleared.</p>
<dt><code>-o</code>, <code>&#8211;owner</code></p>
<dd>Disable use of owner authorization for authorizating a clear operation until a new owner exists.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Disable use of Physical Presence for authorizating a clear operation until a reboot has occurred.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_clear/">tpm_clear</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
