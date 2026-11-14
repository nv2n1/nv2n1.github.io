---
title: "tpm_resetdalock(8)"
name: "tpm_resetdalock"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tpm_resetdalock/"
description: "tpm_resetdalock – reset the dictionary attack lock for the user (require owner authentication)"
---

<p>TPM Management &#8211; tpm_resetdalock<br />
 </center></p>
<h2>Name</h2>
<p>tpm_resetdalock &#8211; reset the dictionary attack lock for the user (require owner authentication)</p>
<h2>Synopsis</h2>
<p><code>tpm_resetdalock</code> </p>
<h2>Description</h2>
<p><code>tpm_resetdalock</code> resets the dictionary attack lock. It prompts for owner authentication and, if password is correct, calls &#8216;tpmSetStatus&#8217; which does necessary action to reset dictionary attack lock.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd>Set logging level.</p>
<dt><code>-z</code>, <code>&#8211;well-known</code></p>
<dd>Authenticate using 20 bytes of zeros as owner password (the default TSS Well Known Secret), instead of prompting for an owner password. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tpm_reset/">tpm_reset</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
