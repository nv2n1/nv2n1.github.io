---
title: "gnutls_hmac_set_nonce(3)"
name: "gnutls_hmac_set_nonce"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_hmac_set_nonce/"
description: "gnutls_hmac_set_nonce – API function"
---

<h2>NAME</h2>
<p> gnutls_hmac_set_nonce &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>void gnutls_hmac_set_nonce(gnutls_hmac_hd_t </code><i>handle</i><code>, const void * </code><i>nonce</i><code>, size_t </code><i>nonce_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_hmac_hd_t handle</p>
<dd> is a <code>gnutls_cipher_hd_t</code> structure.</p>
<dt>const void * nonce</p>
<dd> the data to set as nonce</p>
<dt>size_t nonce_len</p>
<dd> The length of data</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the nonce in the MAC algorithm.</p>
<h2>SINCE</h2>
<p> 3.2.0</p>
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
