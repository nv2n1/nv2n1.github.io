---
title: "gnutls_handshake_get_last_out(3)"
name: "gnutls_handshake_get_last_out"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_get_last_out/"
description: "gnutls_handshake_get_last_out – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_get_last_out &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>gnutls_handshake_description_t gnutls_handshake_get_last_out(gnutls_session_t </code><i>session</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This function is only useful to check where the last performed handshake failed. If the previous handshake succeed or was not performed at all then no meaningful value will be returned. </p>
<p> Check <code>gnutls_handshake_description_t</code> in gnutls.h for the available handshake descriptions.</p>
<h2>RETURNS</h2>
<p> the last handshake message type sent, a <code>gnutls_handshake_description_t</code>.</p>
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
