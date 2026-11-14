---
title: "gnutls_heartbeat_enable(3)"
name: "gnutls_heartbeat_enable"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_heartbeat_enable/"
description: "gnutls_heartbeat_enable – API function"
---

<h2>NAME</h2>
<p> gnutls_heartbeat_enable &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_heartbeat_enable(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>type</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int type</p>
<dd> one of the GNUTLS_HB_* flags</dl>
<h2>DESCRIPTION</h2>
<p> If this function is called with the <code>GNUTLS_HB_PEER_ALLOWED_TO_SEND</code><br />
&nbsp;<wbr><i>type</i>&nbsp;<wbr>, GnuTLS will allow heartbeat messages to be received. Moreover it also request the peer to accept heartbeat messages. </p>
<p> If the <i>type</i> used is <code>GNUTLS_HB_LOCAL_ALLOWED_TO_SEND</code>, then the peer will be asked to accept heartbeat messages but not send ones. </p>
<p> The function <code>gnutls_heartbeat_allowed()</code> can be used to test Whether locally generated heartbeat messages can be accepted by the peer.</p>
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
