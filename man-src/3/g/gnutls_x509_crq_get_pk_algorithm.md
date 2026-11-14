---
title: "gnutls_x509_crq_get_pk_algorithm(3)"
name: "gnutls_x509_crq_get_pk_algorithm"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_pk_algorithm/"
description: "gnutls_x509_crq_get_pk_algorithm – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_pk_algorithm &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_pk_algorithm(gnutls_x509_crq_t </code><i>crq</i><code>, unsigned int * </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> should contain a <code>gnutls_x509_crq_t</code> structure</p>
<dt>unsigned int * bits</p>
<dd> if bits is non-<code>NULL</code> it will hold the size of the parameters&#8217; in bits</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the public key algorithm of a PKCS<code>10</code> certificate request. </p>
<p> If bits is non-<code>NULL</code>, it should have enough size to hold the parameters size in bits. For RSA the bits returned is the modulus. For DSA the bits returned are of the public exponent.</p>
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
