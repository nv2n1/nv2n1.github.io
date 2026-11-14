---
title: "gnutls_rsa_params_export_raw(3)"
name: "gnutls_rsa_params_export_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_params_export_raw/"
description: "gnutls_rsa_params_export_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_rsa_params_export_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_params_export_raw(gnutls_rsa_params_t </code><i>rsa</i><code>, gnutls_datum_t * </code><i>m</i><code>, gnutls_datum_t * </code><i>e</i><code>, gnutls_datum_t * </code><i>d</i><code>, gnutls_datum_t * </code><i>p</i><code>, gnutls_datum_t * </code><i>q</i><code>, gnutls_datum_t * </code><i>u</i><code>, unsigned int * </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rsa_params_t rsa</p>
<dd> a structure that holds the rsa parameters</p>
<dt>gnutls_datum_t * m</p>
<dd> will hold the modulus</p>
<dt>gnutls_datum_t * e</p>
<dd> will hold the public exponent</p>
<dt>gnutls_datum_t * d</p>
<dd> will hold the private exponent</p>
<dt>gnutls_datum_t * p</p>
<dd> will hold the first prime (p)</p>
<dt>gnutls_datum_t * q</p>
<dd> will hold the second prime (q)</p>
<dt>gnutls_datum_t * u</p>
<dd> will hold the coefficient</p>
<dt>unsigned int * bits</p>
<dd> if non null will hold the prime&#8217;s number of bits</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the RSA parameters found in the given structure. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an negative error code.</p>
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
