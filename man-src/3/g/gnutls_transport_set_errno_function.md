---
title: "gnutls_transport_set_errno_function(3)"
name: "gnutls_transport_set_errno_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_errno_function/"
description: "gnutls_transport_set_errno_function – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_errno_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_set_errno_function(gnutls_session_t </code><i>session</i><code>, gnutls_errno_func </code><i>errno_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_errno_func errno_func</p>
<dd> a callback function similar to <code>write()</code></dl>
<h2>DESCRIPTION</h2>
<p> This is the function where you set a function to retrieve errno after a failed push or pull operation. </p>
<p>&nbsp;<wbr><i>errno_func</i>&nbsp;<wbr>is of the form, int (*gnutls_errno_func)(gnutls_transport_ptr_t); and should return the errno.</p>
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
