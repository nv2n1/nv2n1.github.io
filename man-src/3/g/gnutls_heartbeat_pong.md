---
title: "gnutls_heartbeat_pong(3)"
name: "gnutls_heartbeat_pong"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_heartbeat_pong/"
description: "gnutls_heartbeat_pong – API function"
---

<h2>NAME</h2>
<p> gnutls_heartbeat_pong &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_heartbeat_pong(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int flags</p>
<dd> should be zero</dl>
<h2>DESCRIPTION</h2>
<p> This function replies to a ping by sending a pong to the peer.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, otherwise a negative error code.</p>
<h2>SINCE</h2>
<p> 3.1.2</p>
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
