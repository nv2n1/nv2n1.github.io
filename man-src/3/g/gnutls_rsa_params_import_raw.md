---
title: "gnutls_rsa_params_import_raw(3)"
name: "gnutls_rsa_params_import_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_params_import_raw/"
description: "gnutls_rsa_params_import_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_rsa_params_import_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_params_import_raw(gnutls_rsa_params_t </code><i>rsa_params</i><code>, const gnutls_datum_t * </code><i>m</i><code>, const gnutls_datum_t * </code><i>e</i><code>, const gnutls_datum_t * </code><i>d</i><code>, const gnutls_datum_t * </code><i>p</i><code>, const gnutls_datum_t * </code><i>q</i><code>, const gnutls_datum_t * </code><i>u</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rsa_params_t rsa_params</p>
<dd> Is a structure will hold the parameters</p>
<dt>const gnutls_datum_t * m</p>
<dd> holds the modulus</p>
<dt>const gnutls_datum_t * e</p>
<dd> holds the public exponent</p>
<dt>const gnutls_datum_t * d</p>
<dd> holds the private exponent</p>
<dt>const gnutls_datum_t * p</p>
<dd> holds the first prime (p)</p>
<dt>const gnutls_datum_t * q</p>
<dd> holds the second prime (q)</p>
<dt>const gnutls_datum_t * u</p>
<dd> holds the coefficient</dl>
<h2>DESCRIPTION</h2>
<p> This function will replace the parameters in the given structure. The new parameters should be stored in the appropriate gnutls_datum.</p>
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
