---
title: "gnutls_rnd(3)"
name: "gnutls_rnd"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rnd/"
description: "gnutls_rnd – API function"
---

<h2>NAME</h2>
<p> gnutls_rnd &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/crypto.h&gt;</code> </p>
<p> <code>int gnutls_rnd(gnutls_rnd_level_t </code><i>level</i><code>, void * </code><i>data</i><code>, size_t </code><i>len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_rnd_level_t level</p>
<dd> a security level</p>
<dt>void * data</p>
<dd> place to store random bytes</p>
<dt>size_t len</p>
<dd> The requested size</dl>
<h2>DESCRIPTION</h2>
<p> This function will generate random data and store it to output buffer. </p>
<p> This function is thread-safe and also fork-safe.</p>
<h2>RETURNS</h2>
<p> Zero on success, or a negative error code on error.</p>
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
