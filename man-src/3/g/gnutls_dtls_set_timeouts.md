---
title: "gnutls_dtls_set_timeouts(3)"
name: "gnutls_dtls_set_timeouts"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dtls_set_timeouts/"
description: "gnutls_dtls_set_timeouts – API function"
---

<h2>NAME</h2>
<p> gnutls_dtls_set_timeouts &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/dtls.h&gt;</code> </p>
<p> <code>void gnutls_dtls_set_timeouts(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>retrans_timeout</i><code>, unsigned int </code><i>total_timeout</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int retrans_timeout</p>
<dd> The time at which a retransmission will occur in milliseconds</p>
<dt>unsigned int total_timeout</p>
<dd> The time at which the connection will be aborted, in milliseconds.</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the timeouts required for the DTLS handshake protocol. The retransmission timeout is the time after which a message from the peer is not received, the previous messages will be retransmitted. The total timeout is the time after which the handshake will be aborted with <code>GNUTLS_E_TIMEDOUT</code>. </p>
<p> The DTLS protocol recommends the values of 1 sec and 60 seconds respectively. </p>
<p> To disable retransmissions set a <i>retrans_timeout</i> larger than the <i>total_timeout</i> .</p>
<h2>SINCE</h2>
<p> 3.0</p>
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
