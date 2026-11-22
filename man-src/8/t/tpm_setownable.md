---
title: "tpm_setownable(8)"
name: "tpm_setownable"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setownable/"
description: "tpm_setownable – change whether the TPM allows tpm_takeownership operations"
---

<p>TPM Management &#8211; tpm_setownable<br/>
 </center></p>
<h2>Name</h2>
<p>tpm_setownable &#8211; change whether the TPM allows tpm_takeownership operations</p>
<h2>Synopsis</h2>
<p><code>tpm_setownable</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setownable</code> reports the status of the TPM&#8217;s flags regarding if the TPM can be owned. This is the default behavior and also accessible via the <code>&#8211;status</code> option. Requesting a report of this status prompts for the owner password. The <code>&#8211;allow</code> option sets the system&#8217;s TPM to allow tpm_takeownership operations (via the TPM_SetOwnerInstall API). This operation requires physical presence. The <code>&#8211;prevent</code> option (via the TPM_SetOwnerInstall API) prevents the TPM from accepting tpm_takeownership operations. This operation requires physical presence. These operations are persistent. tpm_takeownership requires the tpm be enabled.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd>Set logging level.</dd>
<dt><code>-u</code>, <code>&#8211;unicode</code></dt>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</dd>
<dt><code>-s</code>, <code>&#8211;status</code></dt>
<dd>Report the status of flags regarding if the TPM can be owned.</dd>
<dt><code>-a</code>, <code>&#8211;allow</code></dt>
<dd>Allow tpm_takeownership operations.</dd>
<dt><code>-p</code>, <code>&#8211;prevent</code></dt>
<dd>Prevent tpm_takeownership operations.</dd>
<dt><code>-z</code>, <code>&#8211;well-known</code></dt>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setpresence/">tpm_setpresence</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
</dl>