---
title: "gnutls_session_set_finished_function(3)"
name: "gnutls_session_set_finished_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_session_set_finished_function/"
description: "gnutls_session_set_finished_function – API function"
---

<h2>NAME</h2>
<p> gnutls_session_set_finished_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_session_set_finished_function(gnutls_session_t </code><i>session</i><code>, gnutls_finished_callback_func </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_finished_callback_func func</p>
<dd> a <code>gnutls_finished_callback_func</code> callback.</dl>
<h2>DESCRIPTION</h2>
<p> Register a callback function for the session that will be called when a TLS Finished message has been generated. The function is typically used to copy away the TLS finished message for later use as a channel binding or similar purpose.</p>
<h2>THE CALLBACK SHOULD FOLLOW THIS PROTOTYPE</h2>
<p> void callback (gnutls_session_t <i>session</i>, const void *<i>finished</i>, size_t <i>len</i>); </p>
<p> The <i>finished</i> parameter will contain the binary TLS finished message, and <i>len</i> will contains its length. For SSLv3 connections, the <i>len</i> parameter will be 36 and for TLS connections it will be 12. </p>
<p> It is recommended that the function returns quickly in order to not delay the handshake. Use the function to store a copy of the TLS finished message for later use.</p>
<h2>SINCE</h2>
<p> 2.6.0</p>
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
