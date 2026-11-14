---
title: "gnutls_x509_privkey_sign_hash(3)"
name: "gnutls_x509_privkey_sign_hash"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_x509_privkey_sign_hash/"
description: "gnutls_x509_privkey_sign_hash – API function"
---

<h2>NAME</h2>
<p> gnutls_x509_privkey_sign_hash &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>int gnutls_x509_privkey_sign_hash(gnutls_x509_privkey_t </code><i>key</i><code>, const gnutls_datum_t * </code><i>hash</i><code>, gnutls_datum_t * </code><i>signature</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_x509_privkey_t key</p>
<dd> Holds the key</p>
<dt>const gnutls_datum_t * hash</p>
<dd> holds the data to be signed</p>
<dt>gnutls_datum_t * signature</p>
<dd> will contain newly allocated signature</dl>
<h2>DESCRIPTION</h2>
<p> This function will sign the given hash using the private key. Do not use this function directly unless you know what it is. Typical signing requires the data to be hashed and stored in special formats (e.g. BER Digest-Info for RSA).</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value. </p>
<p> Deprecated in: 2.12.0</p>
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
