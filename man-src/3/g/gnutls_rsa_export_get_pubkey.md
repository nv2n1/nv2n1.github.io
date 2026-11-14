---
title: "gnutls_rsa_export_get_pubkey(3)"
name: "gnutls_rsa_export_get_pubkey"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rsa_export_get_pubkey/"
description: "gnutls_rsa_export_get_pubkey – API function"
---

<h2>NAME</h2>
<p> gnutls_rsa_export_get_pubkey &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_rsa_export_get_pubkey(gnutls_session_t </code><i>session</i><code>, gnutls_datum_t * </code><i>exponent</i><code>, gnutls_datum_t * </code><i>modulus</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a gnutls session</p>
<dt>gnutls_datum_t * exponent</p>
<dd> will hold the exponent.</p>
<dt>gnutls_datum_t * modulus</p>
<dd> will hold the modulus.</dl>
<h2>DESCRIPTION</h2>
<p> This function will return the peer&#8217;s public key exponent and modulus used in the last RSA-EXPORT authentication. The output parameters must be freed with <code>gnutls_free()</code>.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
