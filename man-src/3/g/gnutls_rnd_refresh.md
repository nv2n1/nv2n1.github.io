---
title: "gnutls_rnd_refresh(3)"
name: "gnutls_rnd_refresh"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rnd_refresh/"
description: "gnutls_rnd_refresh – API function"
---

<h2>NAME</h2>
<p> gnutls_rnd_refresh &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>void gnutls_rnd_refresh();</code></p>
<h2>ARGUMENTS</h2>
<h2>DESCRIPTION</h2>
<p> This function refreshes the random generator state. That is the current precise time, CPU usage, and other values are input into its state. </p>
<p> On a slower rate input from /dev/urandom is mixed too.</p>
<h2>SINCE</h2>
<p> 3.1.7</p>
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
