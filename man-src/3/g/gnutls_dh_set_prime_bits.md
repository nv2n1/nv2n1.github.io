---
title: "gnutls_dh_set_prime_bits(3)"
name: "gnutls_dh_set_prime_bits"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_dh_set_prime_bits/"
description: "gnutls_dh_set_prime_bits – API function"
---

<h2>NAME</h2>
<p> gnutls_dh_set_prime_bits &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_dh_set_prime_bits(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>bits</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int bits</p>
<dd> is the number of bits</dl>
<h2>DESCRIPTION</h2>
<p> This function sets the number of bits, for use in a Diffie-Hellman key exchange. This is used both in DH ephemeral and DH anonymous cipher suites. This will set the minimum size of the prime that will be used for the handshake. </p>
<p> In the client side it sets the minimum accepted number of bits. If a server sends a prime with less bits than that <code>GNUTLS_E_DH_PRIME_UNACCEPTABLE</code> will be returned by the handshake. </p>
<p> Note that this function will warn via the audit log for value that are believed to be weak. </p>
<p> The function has no effect in server side. </p>
<p> Note that since 3.1.7 this function is deprecated. The minimum number of bits is set by the priority string level. Also this function must be called after <code>gnutls_priority_set_direct()</code> or the set value may be overridden by the selected priority options.</p>
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
