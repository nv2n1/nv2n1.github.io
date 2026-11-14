---
title: "gnutls_handshake_set_max_packet_length(3)"
name: "gnutls_handshake_set_max_packet_length"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_set_max_packet_length/"
description: "gnutls_handshake_set_max_packet_length – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_set_max_packet_length &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_handshake_set_max_packet_length(gnutls_session_t </code><i>session</i><code>, size_t </code><i>max</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>size_t max</p>
<dd> is the maximum number.</dl>
<h2>DESCRIPTION</h2>
<p> This function will set the maximum size of all handshake messages. Handshakes over this size are rejected with <code>GNUTLS_E_HANDSHAKE_TOO_LARGE</code> error code. The default value is 128kb which is typically large enough. Set this to 0 if you do not want to set an upper limit. </p>
<p> The reason for restricting the handshake message sizes are to limit Denial of Service attacks. </p>
<p> Note that the maximum handshake size was increased to 128kb from 48kb in GnuTLS 3.3.25.</p>
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
