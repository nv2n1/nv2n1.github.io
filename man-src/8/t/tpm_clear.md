---
title: "tpm_clear(8)"
name: "tpm_clear"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_clear/"
description: "tpm_clear – return the TPM to the default state (unowned, disabled, inactive)"
---

<p>TPM Management &#8211; tpm_clear<br />
 </center></p>
<h2>Name</h2>
<p>tpm_clear &#8211; return the TPM to the default state (unowned, disabled, inactive)</p>
<h2>Synopsis</h2>
<p><code>tpm_clear</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_clear</code> requests that the system&#8217;s TPM perform a clear (via the TPM_OwnerClear API) wiping out all ownership information, in effect invalidaing all keys and data tied to the TPM, as well as disabling and deactivating the TPM. This operation will prompt for the owner password. The <code>&#8211;force</code> option relies on Phyiscal Presence to authorize the command (via the TPM_ForceClear API) skipping the owner password prompt. The TPM OwnerClear API can be disabled until the current owner is cleared, requiring use of the <code>&#8211;force</code> with tpm_setclearable command. The TPM_ForceClear API can be disabled for the current boot cycle with the tpm_setclearable command. This command requires a reboot to complete the operation.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Rely on Physical Presence for authorization; therefore, do not prompt for owner password.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setclearable/">tpm_setclearable</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setactive/">tpm_setactive</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
