---
title: "gnutls_record_recv_packet(3)"
name: "gnutls_record_recv_packet"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_recv_packet/"
description: "gnutls_record_recv_packet – API function"
---

<h2>NAME</h2>
<p> gnutls_record_recv_packet &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_recv_packet(gnutls_session_t </code><i>session</i><code>, gnutls_packet_t * </code><i>packet</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_packet_t * packet</p>
<dd> the structure that will hold the packet data</dl>
<h2>DESCRIPTION</h2>
<p> This is a lower-level function thatn <code>gnutls_record_recv()</code> and allows to directly receive the whole decrypted packet. That avoids a memory copy, and is mostly applicable to applications seeking high performance. </p>
<p> The received packet is accessed using <code>gnutls_packet_get()</code> and must be deinitialized using <code>gnutls_packet_deinit()</code>. The returned packet will be <code>NULL</code> if the return value is zero (EOF).</p>
<h2>RETURNS</h2>
<p> The number of bytes received and zero on EOF (for stream connections). A negative error code is returned in case of an error.</p>
<h2>SINCE</h2>
<p> 3.3.5</p>
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
