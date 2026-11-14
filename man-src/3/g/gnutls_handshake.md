---
title: "gnutls_handshake(3)"
name: "gnutls_handshake"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake/"
description: "gnutls_handshake – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_handshake(gnutls_session_t </code><i>session</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This function does the handshake of the TLS/SSL protocol, and initializes the TLS connection. </p>
<p> This function will fail if any problem is encountered, and will return a negative error code. In case of a client, if the client has asked to resume a session, but the server couldn&#8217;t, then a full handshake will be performed. </p>
<p> The non-fatal errors expected by this function are: <code>GNUTLS_E_INTERRUPTED</code>, <code>GNUTLS_E_AGAIN</code>, <code>GNUTLS_E_WARNING_ALERT_RECEIVED</code>, and <code>GNUTLS_E_GOT_APPLICATION_DATA</code>, the latter only in a case of rehandshake. </p>
<p> The former two interrupt the handshake procedure due to the lower layer being interrupted, and the latter because of an alert that may be sent by a server (it is always a good idea to check any received alerts). On these errors call this function again, until it returns 0; cf. <code>gnutls_record_get_direction()</code> and <code>gnutls_error_is_fatal()</code>. In DTLS sessions the non-fatal error <code>GNUTLS_E_LARGE_PACKET</code> is also possible, and indicates that the MTU should be adjusted. </p>
<p> If this function is called by a server after a rehandshake request then <code>GNUTLS_E_GOT_APPLICATION_DATA</code> or <code>GNUTLS_E_WARNING_ALERT_RECEIVED</code> may be returned. Note that these are non fatal errors, only in the specific case of a rehandshake. Their meaning is that the client rejected the rehandshake request or in the case of <code>GNUTLS_E_GOT_APPLICATION_DATA</code> it could also mean that some data were pending.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
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
