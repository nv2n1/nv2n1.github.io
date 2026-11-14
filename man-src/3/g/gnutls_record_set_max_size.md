---
title: "gnutls_record_set_max_size(3)"
name: "gnutls_record_set_max_size"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_set_max_size/"
description: "gnutls_record_set_max_size – API function"
---

<h2>NAME</h2>
<p> gnutls_record_set_max_size &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_set_max_size(gnutls_session_t </code><i>session</i><code>, size_t </code><i>size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>size_t size</p>
<dd> is the new size</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the maximum record packet size in this connection. This property can only be set to clients. The server may choose not to accept the requested size. </p>
<p> Acceptable values are 512(=2^9), 1024(=2^10), 2048(=2^11) and 4096(=2^12). The requested record size does get in effect immediately only while sending data. The receive part will take effect after a successful handshake. </p>
<p> This function uses a TLS extension called &#8216;max record size&#8217;. Not all TLS implementations use or even understand this extension.</p>
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
