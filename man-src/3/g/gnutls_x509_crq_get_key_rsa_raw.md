---
title: "gnutls_x509_crq_get_key_rsa_raw(3)"
name: "gnutls_x509_crq_get_key_rsa_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_crq_get_key_rsa_raw/"
description: "gnutls_x509_crq_get_key_rsa_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_crq_get_key_rsa_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/x509.h&gt;</code> </p>
<p> <code>int gnutls_x509_crq_get_key_rsa_raw(gnutls_x509_crq_t </code><i>crq</i><code>, gnutls_datum_t * </code><i>m</i><code>, gnutls_datum_t * </code><i>e</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_crq_t crq</p>
<dd> Holds the certificate</p>
<dt>gnutls_datum_t * m</p>
<dd> will hold the modulus</p>
<dt>gnutls_datum_t * e</p>
<dd> will hold the public exponent</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the RSA public key&#8217;s parameters found in the given structure. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
<h2>SINCE</h2>
<p> 2.8.0</p>
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
