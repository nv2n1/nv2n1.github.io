---
title: "gnutls_ia_enable(3)"
name: "gnutls_ia_enable"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_enable/"
description: "gnutls_ia_enable – Indicate willingness for TLS/IA application phases"
---

<h2>NAME</h2>
<p> gnutls_ia_enable &#8211; Indicate willingness for TLS/IA application phases</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>void gnutls_ia_enable(gnutls_session_t </code><i>session</i><code>, int </code><i>allow_skip_on_resume</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>int allow_skip_on_resume</p>
<dd> non-zero if local party allows to skip the TLS/IA application phases for a resumed session.</dl>
<h2>DESCRIPTION</h2>
<p> Specify whether we must advertise support for the TLS/IA extension during the handshake. </p>
<p> At the client side, we always advertise TLS/IA if gnutls_ia_enable was called before the handshake; at the server side, we also require that the client has advertised that it wants to run TLS/IA before including the advertisement, as required by the protocol. </p>
<p> Similarly, at the client side we always advertise that we allow TLS/IA to be skipped for resumed sessions if <i>allow_skip_on_resume</i> is non-zero; at the server side, we also require that the session is indeed resumable and that the client has also advertised that it allows TLS/IA to be skipped for resumed sessions. </p>
<p> After the TLS handshake, call <code>gnutls_ia_handshake_p()</code> to find out whether both parties agreed to do a TLS/IA handshake, before calling <code>gnutls_ia_handshake()</code> or one of the lower level gnutls_ia_* functions.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gnutls [at] gnu.org&gt;. GnuTLS home page: <a rel="nofollow" href="http://www.gnu.org/software/gnutls/">http://www.gnu.org/software/gnutls/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 Free Software Foundation.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gnutls</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gnutls</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
