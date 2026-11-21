---
title: "tpmtoken_setpasswd(1)"
name: "tpmtoken_setpasswd"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpmtoken_setpasswd/"
description: "tpmtoken_setpasswd – change the password(s) associated with the user’s TPM PKCS#11 data store"
---

<p>TPM Management &#8211; tpmtoken_setpasswd<br />
 </center></p>
<h2 class="name">NAME</h2>
<p> tpmtoken_setpasswd &#8211; change the password(s) associated with the user&#8217;s TPM PKCS#11 data store </p>
<h2>SYNOPSIS</h2>
<p> <code>tpmtoken_setpasswd</code> [ OPTION ] </p>
<h2>DESCRIPTION</h2>
<p> <code>tpmtoken_setpasswd</code> is used to change the password(s) associated with the user&#8217;s data store. </p>
<p> PKCS#11 requires a password (or PIN) for the Security Officer (SO) and the User. The SO and User password are set when the data store is initialized. This command will allow the user change either password. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd> Set logging level.</dd>
<dt><code>-k</code>, <code>&#8211;token</code> STRING</dt>
<dd> Use STRING to identify the label of the PKCS#11 token to be used</dd>
<dt><code>-s</code>, <code>&#8211;security-officer</code></dt>
<dd> Set the Security Officer password instead of the User password </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tpmtoken_init/">tpmtoken_init</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_import/">tpmtoken_import</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_objects/">tpmtoken_objects</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_protect/">tpmtoken_protect</a></code>(1) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
