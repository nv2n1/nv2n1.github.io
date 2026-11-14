---
title: "gnutls_init(3)"
name: "gnutls_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_init/"
description: "gnutls_init – API function"
---

<h2>NAME</h2>
<p> gnutls_init &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>int gnutls_init(gnutls_session_t * </code><i>session</i><code>, unsigned int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t * session</p>
<dd> is a pointer to a <code>gnutls_session_t</code> structure.</p>
<dt>unsigned int flags</p>
<dd> indicate if this session is to be used for server or client.</dl>
<h2>DESCRIPTION</h2>
<p> This function initializes the current session to null. Every session must be initialized before use, so internal structures can be allocated. This function allocates structures which can only be free&#8217;d by calling <code>gnutls_deinit()</code>. Returns <code>GNUTLS_E_SUCCESS</code> (0) on success. </p>
<p>&nbsp;<wbr><i>flags</i>&nbsp;<wbr>can be one of&nbsp;<wbr><code>GNUTLS_CLIENT</code>&nbsp;<wbr>and&nbsp;<wbr><code>GNUTLS_SERVER</code>. For a DTLS entity, the flags <code>GNUTLS_DATAGRAM</code> and <code>GNUTLS_NONBLOCK</code> are also available. The latter flag will enable a non-blocking operation of the DTLS timers. </p>
<p> The flag <code>GNUTLS_NO_REPLAY_PROTECTION</code> will disable any replay protection in DTLS mode. That must only used when replay protection is achieved using other means. </p>
<p> Note that since version 3.1.2 this function enables some common TLS extensions such as session tickets and OCSP certificate status request in client side by default. To prevent that use the <code>GNUTLS_NO_EXTENSIONS</code> flag.</p>
<h2>RETURNS</h2>
<p> <code>GNUTLS_E_SUCCESS</code> on success, or an error code.</p>
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
