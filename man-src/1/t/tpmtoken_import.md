---
title: "tpmtoken_import(1)"
name: "tpmtoken_import"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tpmtoken_import/"
description: "tpmtoken_import – import an X.509 certficate and/or an RSA key pair into the user’s TPM PKCS#11 data store"
---

<p>TPM Management &#8211; tpmtoken_import<br />
 </center></p>
<h2 class="name">NAME</h2>
<p> tpmtoken_import &#8211; import an X.509 certficate and/or an RSA key pair into the user&#8217;s TPM PKCS#11 data store </p>
<h2>SYNOPSIS</h2>
<p> <code>tpmtoken_import</code> [ OPTION ] FILE </p>
<h2>DESCRIPTION</h2>
<p> <code>tpmtoken_import</code> imports a PEM formatted representation of an X.509 certificate and/or an RSA key contained in FILE. </p>
<p> Importing an X.509 certificate creates an X.509 Public Key Certificate PKCS#11 object and also an RSA Public Key PKCS#11 object using the RSA public key contained in the certificate. The certificate&#8217;s key must be an RSA key in order for the certificate to be successfully processed by this command. </p>
<p> Importing an RSA key creates an RSA Public Key and an RSA Private Key PKCS#11 object. In order to associate the RSA PKCS#11 objects with an X.509 Public Key Certificate PKCS#11 object, the RSA PKCS#11 objects must have a subject name and key identifier associated with them. This can be accomplished by supplying the corresponding X.509 certificate as an optional command parameter. </p>
<p> The input can contain PEM formatted representations of both an X.509 certificate and an RSA key. If both representations are present then an X.509 Public Key Certificate PKCS#11 object, an RSA Public Key PKCS#11 object and an RSA Private Key PKCS#11 object are created. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display command usage info.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display command version info.</dd>
<dt><code>-l</code>, <code>&#8211;log</code> [none|error|info|debug]</dt>
<dd> Set logging level.</dd>
<dt><code>-i</code>, <code>&#8211;idfile</code> FILE</dt>
<dd> Use FILE as the PEM formatted X.509 certificate input used to obtain the subject and id attributes</dd>
<dt><code>-k</code>, <code>&#8211;token</code> STRING</dt>
<dd> Use STRING to identify the label of the PKCS#11 token to be used</dd>
<dt><code>-n</code>, <code>&#8211;name</code> STRING</dt>
<dd> Use STRING as the label for the imported object(s)</dd>
<dt><code>-p</code>, <code>&#8211;public</code></dt>
<dd> Import the object(s) as a public object</dd>
<dt><code>-t</code>, <code>&#8211;type</code> key|cert</dt>
<dd> Import only the specified object type</dd>
<dt><code>-y</code>, <code>&#8211;yes</code></dt>
<dd> Assume an answer of yes for any confirmation prompts that would normally be asked </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tpmtoken_init/">tpmtoken_init</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_setpasswd/">tpmtoken_setpasswd</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_objects/">tpmtoken_objects</a></code>(1), <code><a href="/docs/linux/man/1-tpmtoken_protect/">tpmtoken_protect</a></code>(1) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt; </p>
