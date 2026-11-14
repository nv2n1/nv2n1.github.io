---
title: "tpm_setactive(8)"
name: "tpm_setactive"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setactive/"
description: "tpm_setactive – change TPM active states"
---

<p>TPM Management &#8211; tpm_setactive<br />
 </center></p>
<h2>Name</h2>
<p>tpm_setactive &#8211; change TPM active states</p>
<h2>Synopsis</h2>
<p><code>tpm_setactive</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setactive</code> reports the status of the TPM&#8217;s flags regarding the active state of the TPM. This is the default behavior and also accessible via the <code>&#8211;status</code> option. Requesting a report of this status prompts for the owner password. The <code>&#8211;active</code> option changes the TPM to the active state (via the TPM_PhysicalSetDeactivated API). This operation requires evidence of physical presence, is persistent and requires a reboot to take effect. The <code>&#8211;inactive</code> option (via the TPM_PhysicalSetDeactivated API) changes the TPM to the inactive state. This operation requires evidence of physical presence, is persistent and requires a reboot to take effect. An inactive TPM is essentially off but still allows for a tpm_takeownership to occur. The <code>&#8211;temp</code> option causes deactivation (via the TPM_SetTempDeactivated API) to happen immediately but only endure for the current boot cycle. The <code>&#8211;status</code>, <code>&#8211;active</code>, <code>&#8211;inactive</code>, and <code>&#8211;temp</code> options are mutually exclusive and the last one on the command line will be carried out.</p>
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
<dd>Report the status of flags regarding the TPM active states.</p>
<dt><code>-a</code>, <code>&#8211;active</code></p>
<dd>Make the TPM active. Operation is persistent, requires phyiscal presence to authorize, and a reboot to take effect.</p>
<dt><code>-i</code>, <code>&#8211;inactive</code></p>
<dd>Make the TPM inactive. Operation is persistent, requires phyiscal presence to authorize, and a reboot to take effect.</p>
<dt><code>-t</code>, <code>&#8211;temp</code></p>
<dd>Makes the TPM inactive for the current boot cycle only.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_setpresence/">tpm_setpresence</a></code>(8), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
