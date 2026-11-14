---
title: "tpm_changeownerauth(8)"
name: "tpm_changeownerauth"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_changeownerauth/"
description: "tpm_changeownerauth – change the authorization data associated with the owner or SRK"
---

<p>TPM Management &#8211; tpm_changeownerauth<br />
 </center></p>
<h2>Name</h2>
<p>tpm_changeownerauth &#8211; change the authorization data associated with the owner or SRK</p>
<h2>Synopsis</h2>
<p><code>tpm_changeownerauth</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_changeownerauth</code> allows for changing the authorization data for the TPM owner or the TPM&#8217;s Storage Root Key (via the TPM_ChangeAuthOwner API). This operation prompts for current password, followed by the new password and a confirmation of the new password. The <code>&#8211;owner</code> option changes the TPM owner password and <code>&#8211;srk</code> option changes the TPM&#8217;s SRK password. The <code>&#8211;well-known</code> option is used when SRK or owner passwords need to be changed and current owner password is a secret of zeros, <code>&#8211;set-well-known</code> option changes current password to a secret of zeros, both options do not work by themselves, they must be used with <code>&#8211;owner</code> and <code>&#8211;srk</code> options to indicate which of these passwords will be changed. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-u</code>, <code>&#8211;unicode</code></p>
<dd>Use TSS UNICODE encoding for passwords to comply with applications using TSS popup boxes</p>
<dt><code>-o</code>, <code>&#8211;owner</code></p>
<dd>Change the authorization data for the TPM owner.</p>
<dt><code>-s</code>, <code>&#8211;srk</code></p>
<dd>Change the authorization data for the TPM&#8217;s Storage Root Key.</p>
<dt><code>-g</code>, <code>&#8211;original_password_unicode</code></p>
<dd>Use TSS UNICODE encoding for original password to comply with applications using TSS popup boxes</p>
<dt><code>-n</code>, <code>&#8211;new_password_unicode</code></p>
<dd>Use TSS UNICODE encoding for new password to comply with applications using TSS popup boxes</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Change password to a new one when current owner password is a secret of all zeros (20 bytes of zeros). It must be specified which password (owner, SRK or both) to change</p>
<dt><code>-r</code>, <code>&#8211;set-well-known</code></p>
<dd>Change password to a secret of all zeros (20 bytes of zeros). It must be specified which password (owner, SRK or both) to change</p>
<dt></dl>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
