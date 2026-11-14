---
title: "gnutls_pkcs11_privkey_get_pk_algorithm(3)"
name: "gnutls_pkcs11_privkey_get_pk_algorithm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs11_privkey_get_pk_algorithm/"
description: "gnutls_pkcs11_privkey_get_pk_algorithm – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs11_privkey_get_pk_algorithm &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs11.h&gt;</code> </p>
<p> <code>int gnutls_pkcs11_privkey_get_pk_algorithm(gnutls_pkcs11_privkey_t </code><i>key</i><code>, unsigned int * </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs11_privkey_t key</p>
<dd> should contain a <code>gnutls_pkcs11_privkey_t</code> structure</p>
<dt>unsigned int * bits</p>
<dd> if bits is non null it will hold the size of the parameters&#8217; in bits</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the public key algorithm of a private key.</p>
<h2>RETURNS</h2>
<p> a member of the <code>gnutls_pk_algorithm_t</code> enumeration on success, or a negative error code on error.</p>
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
