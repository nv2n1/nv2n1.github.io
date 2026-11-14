---
title: "gnutls_handshake_set_private_extensions(3)"
name: "gnutls_handshake_set_private_extensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_set_private_extensions/"
description: "gnutls_handshake_set_private_extensions – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_set_private_extensions &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_handshake_set_private_extensions(gnutls_session_t </code><i>session</i><code>, int </code><i>allow</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>int allow</p>
<dd> is an integer (0 or 1)</dl>
<h2>DESCRIPTION</h2>
<p> This function will enable or disable the use of private cipher suites (the ones that start with 0xFF). By default or if <i>allow</i> is 0 then these cipher suites will not be advertised nor used. </p>
<p> Currently GnuTLS does not include such cipher-suites or compression algorithms. </p>
<p> Enabling the private ciphersuites when talking to other than gnutls servers and clients may cause interoperability problems.</p>
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
