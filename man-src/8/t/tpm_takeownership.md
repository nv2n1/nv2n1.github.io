---
title: "tpm_takeownership(8)"
name: "tpm_takeownership"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_takeownership/"
description: "tpm_takeownership – setup an owner on the TPM"
---

<p>TPM Management &#8211; tpm_takeownership<br />
 </center></p>
<h2>Name</h2>
<p>tpm_takeownership &#8211; setup an owner on the TPM</p>
<h2>Synopsis</h2>
<p><code>tpm_takeownership</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_takeownership</code> setup an owner on the system&#8217;s TPM (via the TPM_TakeOwnership API). This operation requires the TPM to be enabled and can be restricted by tpm_setownable. The command will prompt for owner and SRK passwords and confirmations of these if executed without either of the <code>-well-known</code> options, otherwise, a secret of all zeros is set for the requested password. After the second confirmation, be patient as the command may take awhile.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</p>
<dt><code>-y</code>, <code>&#8211;owner-well-known</code></p>
<dd>Set a secret of all zeros (20 bytes of zeros) as the owner&#8217;s secret.</p>
<dt><code>-z</code>, <code>&#8211;srk-well-known</code></p>
<dd>Set a secret of all zeros (20 bytes of zeros) as the SRK secret. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_setownable/">tpm_setownable</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
