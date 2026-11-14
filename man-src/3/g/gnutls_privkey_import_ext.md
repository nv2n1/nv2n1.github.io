---
title: "gnutls_privkey_import_ext(3)"
name: "gnutls_privkey_import_ext"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_import_ext/"
description: "gnutls_privkey_import_ext – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_import_ext &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_import_ext(gnutls_privkey_t </code><i>pkey</i><code>, gnutls_pk_algorithm_t </code><i>pk</i><code>, void * </code><i>userdata</i><code>, gnutls_privkey_sign_func </code><i>sign_func</i><code>, gnutls_privkey_decrypt_func </code><i>decrypt_func</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t pkey</p>
<dd> The private key</p>
<dt>gnutls_pk_algorithm_t pk</p>
<dd> The public key algorithm</p>
<dt>void * userdata</p>
<dd> private data to be provided to the callbacks</p>
<dt>gnutls_privkey_sign_func sign_func</p>
<dd> callback for signature operations</p>
<dt>gnutls_privkey_decrypt_func decrypt_func</p>
<dd> callback for decryption operations</p>
<dt>unsigned int flags</p>
<dd> Flags for the import</dl>
<h2>DESCRIPTION</h2>
<p> This function will associate the given callbacks with the <code>gnutls_privkey_t</code> structure. At least one of the two callbacks must be non-null. </p>
<p> See also <code>gnutls_privkey_import_ext2()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 3.0</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
