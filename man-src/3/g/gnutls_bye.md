---
title: "gnutls_bye(3)"
name: "gnutls_bye"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_bye/"
description: "gnutls_bye – API function"
---

<h2>NAME</h2>
<p> gnutls_bye &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_bye(gnutls_session_t </code><i>session</i><code>, gnutls_close_request_t </code><i>how</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_close_request_t how</p>
<dd> is an integer</dl>
<h2>DESCRIPTION</h2>
<p> Terminates the current TLS/SSL connection. The connection should have been initiated using <code>gnutls_handshake()</code>. <i>how</i> should be one of <code>GNUTLS_SHUT_RDWR</code>, <code>GNUTLS_SHUT_WR</code>. </p>
<p> In case of <code>GNUTLS_SHUT_RDWR</code> the TLS session gets terminated and further receives and sends will be disallowed. If the return value is zero you may continue using the underlying transport layer. <code>GNUTLS_SHUT_RDWR</code> sends an alert containing a close request and waits for the peer to reply with the same message. </p>
<p> In case of <code>GNUTLS_SHUT_WR</code> the TLS session gets terminated and further sends will be disallowed. In order to reuse the connection you should wait for an EOF from the peer. <code>GNUTLS_SHUT_WR</code> sends an alert containing a close request. </p>
<p> Note that not all implementations will properly terminate a TLS connection. Some of them, usually for performance reasons, will terminate only the underlying transport layer, and thus not distinguishing between a malicious party prematurely terminating the connection and normal termination. </p>
<p> This function may also return <code>GNUTLS_E_AGAIN</code> or <code>GNUTLS_E_INTERRUPTED</code>; cf. <code>gnutls_record_get_direction()</code>.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code, see function documentation for entire semantics.</p>
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
