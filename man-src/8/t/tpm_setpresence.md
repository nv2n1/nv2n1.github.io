---
title: "tpm_setpresence(8)"
name: "tpm_setpresence"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_setpresence/"
description: "tpm_setpresence- change TPM physical presence states or settings"
---

<p>TPM Management &#8211; tpm_setpresence<br />
 </center></p>
<h2>Name</h2>
<p>tpm_setpresence- change TPM physical presence states or settings</p>
<h2>Synopsis</h2>
<p><code>tpm_setpresence</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_setpresence</code> reports the status of the TPM&#8217;s flags regarding physical presence. This is the default behavior and also accessible via the <code>&#8211;status</code> option. Requesting a report of this status prompts for the owner password. The <code>&#8211;assert</code> option changes the TPM to the physically present state. The <code>&#8211;clear</code> option changes the TPM to the not present state. The <code>&#8211;lock</code> option locks the TPM to the current physical presence state for the current boot cycle. The <code>&#8211;enable-cmd</code> option allows the TPM to accept local commands to toggle physical presence states. The <code>&#8211;disable-cmd</code> option prevents the TPM from accepting local commands to toggle physical presence states. The <code>&#8211;enable-hw</code> option allows the TPM to accept hardware signals to toggle physical presence states. The <code>&#8211;disable-hw</code> option prevents the TPM from accepting hardware signals to toggle physical presence states. The <code>&#8211;set-lifetime-lock</code> option locks the Command and Hardware enablement flags in their current state permenantly. This option can never be undone. The system will attempt to use the owner password to display the current states before preceding unless the <code>&#8211;yes</code> option is given to answer yes to all questions. All changes are made with the TSC_Physical Presence API.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</p>
<dt><code>-a</code>, <code>&#8211;assert</code></p>
<dd>Assert that an admin is physically present at the machine.</p>
<dt><code>-c</code>, <code>&#8211;clear</code></p>
<dd>Remove the assertion that an admin is physically present at the machine.</p>
<dt><code>&#8211;lock</code></p>
<dd>Lock the assertions of physical presence in there current states until a reboot.</p>
<dt><code>&#8211;enable-cmd</code></p>
<dd>Allow use of commands to signal an admin is physically present.</p>
<dt><code>&#8211;disable-cmd</code></p>
<dd>Disallow use of commands to signal an admin is physically present.</p>
<dt><code>&#8211;enable-hw</code></p>
<dd>Allow use of hardware signals to signal an admin is physically present.</p>
<dt><code>&#8211;disable-hw</code></p>
<dd>Disallow use of hardware signals to signal an admin is physically present.</p>
<dt><code>&#8211;set-lifetime-lock</code></p>
<dd>Allow no further changes to the flags controling how physical presence can be signaled. This is PERMANENT.</p>
<dt><code>-y</code>, <code>&#8211;yes</code></p>
<dd>Answer yes to all questions. Only applicable with <code>&#8211;set-lifetime-lock</code>.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setactive/">tpm_setactive</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setownable/">tpm_setownable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
