---
title: "gnutls_handshake_set_random(3)"
name: "gnutls_handshake_set_random"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_set_random/"
description: "gnutls_handshake_set_random – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_set_random &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_handshake_set_random(gnutls_session_t </code><i>session</i><code>, const gnutls_datum_t * </code><i>random</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const gnutls_datum_t * random</p>
<dd> a random value of 32-bytes</dl>
<h2>DESCRIPTION</h2>
<p> This function will explicitly set the server or client hello random value in the subsequent TLS handshake. The random value should be a 32-byte value. </p>
<p> Note that this function should not normally be used as gnutls will select automatically a random value for the handshake. </p>
<p> This function should not be used when resuming a session.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code. </p>
<p> Since 3.1.9</p>
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
