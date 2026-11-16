---
title: "tpm_restrictpubek(8)"
name: "tpm_restrictpubek"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_restrictpubek/"
description: "tpm_restrictpubek – restrict the ability to display the public portion of the Endorsement Key to the owner"
---

<p>TPM Management &#8211; tpm_restrictpubek<br />
 </center></p>
<h2>Name</h2>
<p>tpm_restrictpubek &#8211; restrict the ability to display the public portion of the Endorsement Key to the owner</p>
<h2>Synopsis</h2>
<p><code>tpm_restrictpubek</code> [<code>OPTION</code>] </p>
<h2>Description</h2>
<p><code>tpm_restrictpubek</code> reports the status of who can display the public portion of the Endorsement Key. This is the default behavior and also available with the <code>&#8211;status</code> option. This operation will be in effect until the owner is cleared and prompts for the owner passord. With the <code>&#8211;restrict</code> option, the ability to display the public portion of the Endorsement Key is resticted to the owner (via the TPM_DisablePubekRead API). The command prompts for the owner password to complete the operation. The <code>&#8211;status</code> and <code>&#8211;restrict</code> options are mutually exclusive and the last one on the command line will be carried out.</p>
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
<dd>Display the status of who can see the public portion of the Endorsement Key</dd>
<dt><code>-r</code>, <code>&#8211;restrict</code></dt>
<dd>Restrict seeing the public portion of the Endorsement Key to the owner</dd>
<dt><code>-z</code>, <code>&#8211;well-known</code></dt>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_version/">tpm_version</a></code>(1), <code><a href="/docs/linux/man/8-tpm_takeownership/">tpm_takeownership</a></code>(8), <code><a href="/docs/linux/man/8-tpm_getpubek/">tpm_getpubek</a></code>(8), <code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
</dl>