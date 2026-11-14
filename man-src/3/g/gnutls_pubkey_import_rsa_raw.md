---
title: "gnutls_pubkey_import_rsa_raw(3)"
name: "gnutls_pubkey_import_rsa_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pubkey_import_rsa_raw/"
description: "gnutls_pubkey_import_rsa_raw – API function"
---

<h2>NAME</h2>
<p> gnutls_pubkey_import_rsa_raw &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_pubkey_import_rsa_raw(gnutls_pubkey_t </code><i>key</i><code>, const gnutls_datum_t * </code><i>m</i><code>, const gnutls_datum_t * </code><i>e</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pubkey_t key</p>
<dd> Is a structure will hold the parameters</p>
<dt>const gnutls_datum_t * m</p>
<dd> holds the modulus</p>
<dt>const gnutls_datum_t * e</p>
<dd> holds the public exponent</dl>
<h2>DESCRIPTION</h2>
<p> This function will replace the parameters in the given structure. The new parameters should be stored in the appropriate gnutls_datum.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an negative error code.</p>
<h2>SINCE</h2>
<p> 2.12.0</p>
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
