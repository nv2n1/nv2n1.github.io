---
title: "gnutls_cipher_init(3)"
name: "gnutls_cipher_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_cipher_init/"
description: "gnutls_cipher_init – API function"
---

<h2>NAME</h2>
<p> gnutls_cipher_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>int gnutls_cipher_init(gnutls_cipher_hd_t * </code><i>handle</i><code>, gnutls_cipher_algorithm_t </code><i>cipher</i><code>, const gnutls_datum_t * </code><i>key</i><code>, const gnutls_datum_t * </code><i>iv</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_cipher_hd_t * handle</p>
<dd> is a <code>gnutls_cipher_hd_t</code> structure.</p>
<dt>gnutls_cipher_algorithm_t cipher</p>
<dd> the encryption algorithm to use</p>
<dt>const gnutls_datum_t * key</p>
<dd> The key to be used for encryption</p>
<dt>const gnutls_datum_t * iv</p>
<dd> The IV to use (if not applicable set NULL)</dl>
<h2>DESCRIPTION</h2>
<p> This function will initialize an context that can be used for encryption/decryption of data. This will effectively use the current crypto backend in use by gnutls or the cryptographic accelerator in use.</p>
<h2>RETURNS</h2>
<p> Zero or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 2.10.0</p>
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
