---
title: "tpmtoken_objects(1)"
name: "tpmtoken_objects"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpmtoken_objects/"
description: "tpmtoken_objects – display the objects in the user’s TPM PKCS#11 data store"
---

<p>TPM Management &#8211; tpmtoken_objects<br />
 </center></p>
<h2 class="name">NAME</h2>
<p> tpmtoken_objects &#8211; display the objects in the user&#8217;s TPM PKCS#11 data store </p>
<h2>SYNOPSIS</h2>
<p> <code>tpmtoken_objects</code> [ OPTION ] </p>
<h2>DESCRIPTION</h2>
<p> <code>tpmtoken_objects</code> displays information about the PKCS#11 objects that are in the user&#8217;s data store. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display command usage info.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display command version info.</p>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</p>
<dd> Set logging level.</p>
<dt><code>-k</code>, <code>&#8211;token</code> STRING</p>
<dd> Use STRING to identify the label of the PKCS#11 token to be used</p>
<dt><code>-p</code>, <code>&#8211;public</code></p>
<dd> Display only public objects</p>
<dt><code>-x</code>, <code>&#8211;extended</code></p>
<dd> Display additional information about an object not displayed by default </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tpmtoken_init/">tpmtoken_init</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_setpasswd/">tpmtoken_setpasswd</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_import/">tpmtoken_import</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_protect/">tpmtoken_protect</a></code>(1) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
<h2>Index</h2>
