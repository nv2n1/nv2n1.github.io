---
title: "gnutls_transport_set_vec_push_function(3)"
name: "gnutls_transport_set_vec_push_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_set_vec_push_function/"
description: "gnutls_transport_set_vec_push_function – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_set_vec_push_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_set_vec_push_function(gnutls_session_t </code><i>session</i><code>, gnutls_vec_push_func </code><i>vec_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_vec_push_func vec_func</p>
<dd> a callback function similar to <code>writev()</code></dl>
<h2>DESCRIPTION</h2>
<p> Using this function you can override the default <a href="/docs/linux/man/2-writev/">writev</a>(2) function for gnutls to send data. Setting this callback instead of <code>gnutls_transport_set_push_function()</code> is recommended since it introduces less overhead in the TLS handshake process. </p>
<p>&nbsp;<wbr><i>vec_func</i>&nbsp;<wbr>is of the form, ssize_t (*gnutls_vec_push_func) (gnutls_transport_ptr_t, const giovec_t * iov, int iovcnt);</p>
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
