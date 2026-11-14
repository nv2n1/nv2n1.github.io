---
title: "gnutls_openpgp_crt_get_subkey_pk_rsa_raw(3)"
name: "gnutls_openpgp_crt_get_subkey_pk_rsa_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_openpgp_crt_get_subkey_pk_rsa_raw/"
description: "gnutls_openpgp_crt_get_subkey_pk_rsa_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_openpgp_crt_get_subkey_pk_rsa_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/openpgp.h&gt;</code> </p>
<p> <code>int gnutls_openpgp_crt_get_subkey_pk_rsa_raw(gnutls_openpgp_crt_t </code><i>crt</i><code>, unsigned int </code><i>idx</i><code>, gnutls_datum_t * </code><i>m</i><code>, gnutls_datum_t * </code><i>e</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_openpgp_crt_t crt</p>
<dd> Holds the certificate</p>
<dt>unsigned int idx</p>
<dd> Is the subkey index</p>
<dt>gnutls_datum_t * m</p>
<dd> will hold the modulus</p>
<dt>gnutls_datum_t * e</p>
<dd> will hold the public exponent</dl>
<h2>DESCRIPTION</h2>
<p> This function will export the RSA public key&#8217;s parameters found in the given structure. The new parameters will be allocated using <code>gnutls_malloc()</code> and will be stored in the appropriate datum.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 2.4.0</p>
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
