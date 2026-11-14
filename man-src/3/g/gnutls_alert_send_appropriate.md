---
title: "gnutls_alert_send_appropriate(3)"
name: "gnutls_alert_send_appropriate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_alert_send_appropriate/"
description: "gnutls_alert_send_appropriate – API function"
---

<h2>NAME</h2>
<p> gnutls_alert_send_appropriate &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_alert_send_appropriate(gnutls_session_t </code><i>session</i><code>, int </code><i>err</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>int err</p>
<dd> is an integer</dl>
<h2>DESCRIPTION</h2>
<p> Sends an alert to the peer depending on the error code returned by a gnutls function. This function will call <code>gnutls_error_to_alert()</code> to determine the appropriate alert to send. </p>
<p> This function may also return <code>GNUTLS_E_AGAIN</code>, or <code>GNUTLS_E_INTERRUPTED</code>. </p>
<p> If the return value is <code>GNUTLS_E_INVALID_REQUEST</code>, then no alert has been sent to the peer.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
