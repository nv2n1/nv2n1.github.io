---
title: "gnutls_rehandshake(3)"
name: "gnutls_rehandshake"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_rehandshake/"
description: "gnutls_rehandshake – API function"
---

<h2>NAME</h2>
<p> gnutls_rehandshake &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_rehandshake(gnutls_session_t </code><i>session</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This function will renegotiate security parameters with the client. This should only be called in case of a server. </p>
<p> This message informs the peer that we want to renegotiate parameters (perform a handshake). </p>
<p> If this function succeeds (returns 0), you must call the <code>gnutls_handshake()</code> function in order to negotiate the new parameters. </p>
<p> Since TLS is full duplex some application data might have been sent during peer&#8217;s processing of this message. In that case one should call <code>gnutls_record_recv()</code> until GNUTLS_E_REHANDSHAKE is returned to clear any pending data. Care must be taken if rehandshake is mandatory to terminate if it does not start after some threshold. </p>
<p> If the client does not wish to renegotiate parameters he should reply with an alert message, thus the return code will be <code>GNUTLS_E_WARNING_ALERT_RECEIVED</code> and the alert will be <code>GNUTLS_A_NO_RENEGOTIATION</code>. A client may also choose to ignore this message.</p>
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
