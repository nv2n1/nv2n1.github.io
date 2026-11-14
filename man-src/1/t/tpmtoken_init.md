---
title: "tpmtoken_init(1)"
name: "tpmtoken_init"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpmtoken_init/"
description: "tpmtoken_init – initialize the user’s TPM PKCS#11 data store"
---

<p>TPM Management &#8211; tpmtoken_init<br />
 </center></p>
<h2 class="name">NAME</h2>
<p> tpmtoken_init &#8211; initialize the user&#8217;s TPM PKCS#11 data store </p>
<h2>SYNOPSIS</h2>
<p> <code>tpmtoken_init</code> [<code>OPTION</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>tpmtoken_init</code> initializes the user&#8217;s TPM PKCS#11 data store so that applications can exploit the TPM capabilities through the PKCS#11 interface. </p>
<p> PKCS#11 requires a password (or PIN) for the Security Officer (SO) and the User. The SO is responsible for initializing the token and setting the User password (or PIN). </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd> Set logging level.</p>
<dt><code>-k</code>, <code>&#8211;token</code> STRING</p>
<dd> Use STRING to identify the label of the PKCS#11 token to be used</p>
<dt><code>-y</code>, <code>&#8211;yes</code></p>
<dd> Assume an answer of yes for any confirmation prompts that would normally be asked </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tpmtoken_setpasswd/">tpmtoken_setpasswd</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_import/">tpmtoken_import</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_objects/">tpmtoken_objects</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_protect/">tpmtoken_protect</a></code>(1) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
<h2>Index</h2>
