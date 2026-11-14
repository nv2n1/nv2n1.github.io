---
title: "gnutls_sign_is_secure(3)"
name: "gnutls_sign_is_secure"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_sign_is_secure/"
description: "gnutls_sign_is_secure – API function"
---

<h2>NAME</h2>
<p> gnutls_sign_is_secure &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_sign_is_secure(gnutls_sign_algorithm_t </code><i>algorithm</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_sign_algorithm_t algorithm</p>
<dd> is a sign algorithm</dl>
<h2>RETURNS</h2>
<p> Non-zero if the provided signature algorithm is considered to be secure.</p>
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
