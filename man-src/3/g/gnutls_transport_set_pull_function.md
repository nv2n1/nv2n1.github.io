---
title: "gnutls_transport_set_pull_function(3)"
name: "gnutls_transport_set_pull_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_pull_function/"
description: "gnutls_transport_set_pull_function – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_pull_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_set_pull_function(gnutls_session_t </code><i>session</i><code>, gnutls_pull_func </code><i>pull_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_pull_func pull_func</p>
<dd> a callback function similar to <code>read()</code></dl>
<h2>DESCRIPTION</h2>
<p> This is the function where you set a function for gnutls to receive data. Normally, if you use berkeley style sockets, do not need to use this function since the default <a href="/docs/linux/man/2-recv/">recv</a>(2) will probably be ok. The callback should return 0 on connection termination, a positive number indicating the number of bytes received, and -1 on error. </p>
<p>&nbsp;<wbr><i>gnutls_pull_func</i>&nbsp;<wbr>is of the form, ssize_t (*gnutls_pull_func)(gnutls_transport_ptr_t, void*, size_t);</p>
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
