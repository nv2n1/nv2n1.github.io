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
<p> <code>tpmtoken_objects</code> [ OPTION ] </p>
<p> <code>tpmtoken_objects</code> displays information about the PKCS#11 objects that are in the user&#8217;s data store. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd> Set logging level.</dd>
<dt><code>-k</code>, <code>&#8211;token</code> STRING</dt>
<dd> Use STRING to identify the label of the PKCS#11 token to be used</dd>
<dt><code>-p</code>, <code>&#8211;public</code></dt>
<dd> Display only public objects</dd>
<dt><code>-x</code>, <code>&#8211;extended</code></dt>
<dd> Display additional information about an object not displayed by default </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tpmtoken_init/">tpmtoken_init</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_setpasswd/">tpmtoken_setpasswd</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_import/">tpmtoken_import</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_protect/">tpmtoken_protect</a></code>(1) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
