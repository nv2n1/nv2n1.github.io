---
title: "gnutls_transport_get_int2(3)"
name: "gnutls_transport_get_int2"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_transport_get_int2/"
description: "gnutls_transport_get_int2 – API function"
---

<h2>NAME</h2>
<p> gnutls_transport_get_int2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_transport_get_int2(gnutls_session_t </code><i>session</i><code>, int * </code><i>recv_int</i><code>, int * </code><i>send_int</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>int * recv_int</p>
<dd> will hold the value for the pull function</p>
<dt>int * send_int</p>
<dd> will hold the value for the push function</dl>
<h2>DESCRIPTION</h2>
<p> Used to get the arguments of the transport functions (like PUSH and PULL). These should have been set using <code>gnutls_transport_set_int2()</code>.</p>
<h2>SINCE</h2>
<p> 3.1.9</p>
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
