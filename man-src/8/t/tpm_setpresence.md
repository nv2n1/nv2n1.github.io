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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd>Set logging level.</dd>
<dt><code>-u</code>, <code>&#8211;unicode</code></dt>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</dd>
<dt><code>-a</code>, <code>&#8211;assert</code></dt>
<dd>Assert that an admin is physically present at the machine.</dd>
<dt><code>-c</code>, <code>&#8211;clear</code></dt>
<dd>Remove the assertion that an admin is physically present at the machine.</dd>
<dt><code>&#8211;lock</code></dt>
<dd>Lock the assertions of physical presence in there current states until a reboot.</dd>
<dt><code>&#8211;enable-cmd</code></dt>
<dd>Allow use of commands to signal an admin is physically present.</dd>
<dt><code>&#8211;disable-cmd</code></dt>
<dd>Disallow use of commands to signal an admin is physically present.</dd>
<dt><code>&#8211;enable-hw</code></dt>
<dd>Allow use of hardware signals to signal an admin is physically present.</dd>
<dt><code>&#8211;disable-hw</code></dt>
<dd>Disallow use of hardware signals to signal an admin is physically present.</dd>
<dt><code>&#8211;set-lifetime-lock</code></dt>
<dd>Allow no further changes to the flags controling how physical presence can be signaled. This is PERMANENT.</dd>
<dt><code>-y</code>, <code>&#8211;yes</code></dt>
<dd>Answer yes to all questions. Only applicable with <code>&#8211;set-lifetime-lock</code>.</dd>
<dt><code>-z</code>, <code>&#8211;well-known</code></dt>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_setenable/">tpm_setenable</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setactive/">tpm_setactive</a></code>(8), <code><a href="/docs/linux/man/8-tpm_setownable/">tpm_setownable</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
</dl>