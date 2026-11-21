---

title: "gnutls_privkey_export_rsa_raw(3)"
name: "gnutls_privkey_export_rsa_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_export_rsa_raw/"
description: "gnutls_privkey_export_rsa_raw – API function"
---

<p> gnutls_privkey_export_rsa_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_export_rsa_raw(gnutls_privkey_t </code><i>key</i><code>, gnutls_datum_t * </code><i>m</i><code>, gnutls_datum_t * </code><i>e</i><code>, gnutls_datum_t * </code><i>d</i><code>, gnutls_datum_t * </code><i>p</i><code>, gnutls_datum_t * </code><i>q</i><code>, gnutls_datum_t * </code><i>u</i><code>, gnutls_datum_t * </code><i>e1</i><code>, gnutls_datum_t * </code><i>e2</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t key</dt>
<dd> Holds the certificate</dd>
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
<dt>gnutls_datum_t * e1</dt>
<dd> will hold e1 = d mod (p-1)</dd>
<dt>gnutls_datum_t * e2</dt>
<dd> will hold e2 = d mod (q-1)</dd></dl>
<h2>DESCRIPTION</h2>
<p> This function will export the RSA private key&#8217;s parameters found in the given structure. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 3.3.0</p>
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
