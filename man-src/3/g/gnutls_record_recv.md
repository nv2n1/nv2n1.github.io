---
title: "gnutls_record_recv(3)"
name: "gnutls_record_recv"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_record_recv/"
description: "gnutls_record_recv – API function"
---

<h2>NAME</h2>
<p> gnutls_record_recv &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>ssize_t gnutls_record_recv(gnutls_session_t </code><i>session</i><code>, void * </code><i>data</i><code>, size_t </code><i>data_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>void * data</p>
<dd> the buffer that the data will be read into</p>
<dt>size_t data_size</p>
<dd> the number of requested bytes</dl>
<h2>DESCRIPTION</h2>
<p> This function has the similar semantics with <code>recv()</code>. The only difference is that it accepts a GnuTLS session, and uses different error codes. In the special case that a server requests a renegotiation, the client may receive an error code of <code>GNUTLS_E_REHANDSHAKE</code>. This message may be simply ignored, replied with an alert <code>GNUTLS_A_NO_RENEGOTIATION</code>, or replied with a new handshake, depending on the client&#8217;s will. If <code>EINTR</code> is returned by the internal push function (the default is <code>recv()</code>) then <code>GNUTLS_E_INTERRUPTED</code> will be returned. If <code>GNUTLS_E_INTERRUPTED</code> or <code>GNUTLS_E_AGAIN</code> is returned, you must call this function again to get the data. See also <code>gnutls_record_get_direction()</code>. A server may also receive <code>GNUTLS_E_REHANDSHAKE</code> when a client has initiated a handshake. In that case the server can only initiate a handshake or terminate the connection.</p>
<h2>RETURNS</h2>
<p> The number of bytes received and zero on EOF (for stream connections). A negative error code is returned in case of an error. The number of bytes received might be less than the requested <i>data_size</i> .</p>
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
