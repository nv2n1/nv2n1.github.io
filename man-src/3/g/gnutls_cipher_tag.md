---
title: "gnutls_cipher_tag(3)"
name: "gnutls_cipher_tag"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_cipher_tag/"
description: "gnutls_cipher_tag – API function"
---

<h2>NAME</h2>
<p> gnutls_cipher_tag &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>int gnutls_cipher_tag(gnutls_cipher_hd_t </code><i>handle</i><code>, void * </code><i>tag</i><code>, size_t </code><i>tag_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_cipher_hd_t handle</p>
<dd> is a <code>gnutls_cipher_hd_t</code> structure.</p>
<dt>void * tag</p>
<dd> will hold the tag</p>
<dt>size_t tag_size</p>
<dd> The length of the tag to return</dl>
<h2>DESCRIPTION</h2>
<p> This function operates on authenticated encryption with associated data (AEAD) ciphers and will return the output tag.</p>
<h2>RETURNS</h2>
<p> Zero or a negative error code on error.</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
