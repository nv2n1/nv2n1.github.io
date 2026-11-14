---
title: "gnutls_pkcs12_bag_decrypt(3)"
name: "gnutls_pkcs12_bag_decrypt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_pkcs12_bag_decrypt/"
description: "gnutls_pkcs12_bag_decrypt – API function"
---

<h2>NAME</h2>
<p> gnutls_pkcs12_bag_decrypt &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/pkcs12.h&gt;</code> </p>
<p> <code>int gnutls_pkcs12_bag_decrypt(gnutls_pkcs12_bag_t </code><i>bag</i><code>, const char * </code><i>pass</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_pkcs12_bag_t bag</p>
<dd> The bag</p>
<dt>const char * pass</p>
<dd> The password used for encryption, must be ASCII.</dl>
<h2>DESCRIPTION</h2>
<p> This function will decrypt the given encrypted bag and return 0 on success.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise a negative error code is returned.</p>
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
