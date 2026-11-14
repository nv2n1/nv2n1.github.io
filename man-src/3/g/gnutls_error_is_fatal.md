---
title: "gnutls_error_is_fatal(3)"
name: "gnutls_error_is_fatal"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_error_is_fatal/"
description: "gnutls_error_is_fatal – API function"
---

<h2>NAME</h2>
<p> gnutls_error_is_fatal &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_error_is_fatal(int </code><i>error</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int error</p>
<dd> is a GnuTLS error code, a negative error code</dl>
<h2>DESCRIPTION</h2>
<p> If a GnuTLS function returns a negative error code you may feed that value to this function to see if the error condition is fatal to a TLS session (i.e., must be terminated). </p>
<p> Note that you may also want to check the error code manually, since some non-fatal errors to the protocol (such as a warning alert or a rehandshake request) may be fatal for your program. </p>
<p> This function is only useful if you are dealing with errors from functions that relate to a TLS session (e.g., record layer or handshake layer handling functions).</p>
<h2>RETURNS</h2>
<p> Non-zero value on fatal errors or zero on non-fatal.</p>
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
