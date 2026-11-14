---
title: "gnutls_strerror_name(3)"
name: "gnutls_strerror_name"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_strerror_name/"
description: "gnutls_strerror_name – API function"
---

<h2>NAME</h2>
<p> gnutls_strerror_name &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>const char * gnutls_strerror_name(int </code><i>error</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int error</p>
<dd> is an error returned by a gnutls function.</dl>
<h2>DESCRIPTION</h2>
<p> Return the GnuTLS error code define as a string. For example, gnutls_strerror_name (GNUTLS_E_DH_PRIME_UNACCEPTABLE) will return the string &quot;GNUTLS_E_DH_PRIME_UNACCEPTABLE&quot;.</p>
<h2>RETURNS</h2>
<p> A string corresponding to the symbol name of the error code.</p>
<h2>SINCE</h2>
<p> 2.6.0</p>
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
