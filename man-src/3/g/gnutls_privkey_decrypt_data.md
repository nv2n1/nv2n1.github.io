---
title: "gnutls_privkey_decrypt_data(3)"
name: "gnutls_privkey_decrypt_data"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_privkey_decrypt_data/"
description: "gnutls_privkey_decrypt_data – API function"
---

<h2>NAME</h2>
<p> gnutls_privkey_decrypt_data &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/abstract.h&gt;</code> </p>
<p> <code>int gnutls_privkey_decrypt_data(gnutls_privkey_t </code><i>key</i><code>, unsigned int </code><i>flags</i><code>, const gnutls_datum_t * </code><i>ciphertext</i><code>, gnutls_datum_t * </code><i>plaintext</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_privkey_t key</p>
<dd> Holds the key</p>
<dt>unsigned int flags</p>
<dd> zero for now</p>
<dt>const gnutls_datum_t * ciphertext</p>
<dd> holds the data to be decrypted</p>
<dt>gnutls_datum_t * plaintext</p>
<dd> will contain the decrypted data, allocated with <code>gnutls_malloc()</code></dl>
<h2>DESCRIPTION</h2>
<p> This function will decrypt the given data using the algorithm supported by the private key.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error value.</p>
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
