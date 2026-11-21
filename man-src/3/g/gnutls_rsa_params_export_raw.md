---

title: "gnutls_rsa_params_export_raw(3)"
name: "gnutls_rsa_params_export_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_params_export_raw/"
description: "gnutls_rsa_params_export_raw – API function"
---

<p> gnutls_rsa_params_export_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_params_export_raw(gnutls_rsa_params_t </code><i>rsa</i><code>, gnutls_datum_t * </code><i>m</i><code>, gnutls_datum_t * </code><i>e</i><code>, gnutls_datum_t * </code><i>d</i><code>, gnutls_datum_t * </code><i>p</i><code>, gnutls_datum_t * </code><i>q</i><code>, gnutls_datum_t * </code><i>u</i><code>, unsigned int * </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rsa_params_t rsa</dt>
<dd> a structure that holds the rsa parameters</dd>
<dt>gnutls_datum_t * m</dt>
<dd> will hold the modulus</dd>
<dt>gnutls_datum_t * e</dt>
<dd> will hold the public exponent</dd>
<dt>gnutls_datum_t * d</dt>
<dd> will hold the private exponent</dd>
<dt>gnutls_datum_t * p</dt>
<dd> will hold the first prime (p)</dd>
<dt>gnutls_datum_t * q</dt>
<dd> will hold the second prime (q)</dd>
<dt>gnutls_datum_t * u</dt>
<dd> will hold the coefficient</dd>
<dt>unsigned int * bits</dt>
<dd> if non null will hold the prime&#8217;s number of bits</dd></dl>
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
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></dt>
<dd> </code></dd></dl>
