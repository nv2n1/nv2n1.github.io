---
title: "tpm_setenable(8)"
name: "tpm_setenable"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setenable/"
description: "tpm_setenable – change TPM enable states"
---

<p>TPM Management &#8211; tpm_setenable<br />
 </center></p>
<h2>Name</h2>
<p>tpm_setenable &#8211; change TPM enable states</p>
<h2>Synopsis</h2>
<p><code>tpm_setenable</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setenable</code> reports the status of the TPM&#8217;s flags regarding the enable state of the TPM. This is the default behavior and also accessible via the <code>&#8211;status</code> option. Requesting a report of this status prompts for the owner password. The <code>&#8211;enable</code> option changes the system&#8217;s TPM to the enabled state (via the TPM_OwnerSetDisable API). This operation prompts for the owner password and is persistent. The <code>&#8211;disable</code> option (via the TPM_OwnerSetDisable API) changes the system&#8217;s TPM to the disabled state. This operation prompts for the owner password and is persistent. A disabled TPM is essentially off and does not allow a tpm_takeownership to occur. The <code>&#8211;force</code> option overrides the owner password prompt and relies on physical presence for the operation authorization (via the TPM_PhysicalEnable and TPM_PhysicalDisable APIs). The <code>&#8211;enable</code>, <code>&#8211;disable</code>, and <code>&#8211;status</code> options are mutually exclusive and the last one on the command line will be carried out.</p>
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
<dd>Report the status of flags regarding the TPM enable states.</p>
<dt><code>-e</code>, <code>&#8211;enable</code></p>
<dd>Make the TPM enabled. Operation is persistent and prompts for owner authorization.</p>
<dt><code>-d</code>, <code>&#8211;disable</code></p>
<dd>Make the TPM disabled. Operation is persistent and prompts for owner authorization.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Overrides the prompt for owner authorization and uses physical presence to authorize the action.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_setpresence/">tpm_setpresence</a></code>(8), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setactive/">tpm_setactive</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
