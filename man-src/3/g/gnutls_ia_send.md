---
title: "gnutls_ia_send(3)"
name: "gnutls_ia_send"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_send/"
description: "gnutls_ia_send – API function"
---

<h2>NAME</h2>
<p> gnutls_ia_send &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>ssize_t gnutls_ia_send(gnutls_session_t </code><i>session</i><code>, const char * </code><i>data</i><code>, size_t </code><i>sizeofdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const char * data</p>
<dd> contains the data to send</p>
<dt>size_t sizeofdata</p>
<dd> is the length of the data</dl>
<h2>DESCRIPTION</h2>
<p> Send TLS/IA application payload data. This function has the similar semantics with <code>send()</code>. The only difference is that it accepts a GnuTLS session, and uses different error codes. </p>
<p> The TLS/IA protocol is synchronous, so you cannot send more than one packet at a time. The client always send the first packet. </p>
<p> To finish an application phase in the server, use <code>gnutls_ia_endphase_send()</code>. The client cannot end an application phase unilaterally; rather, a client is required to respond with an endphase of its own if gnutls_ia_recv indicates that the server has sent one. </p>
<p> If the EINTR is returned by the internal push function (the default is <code>send()</code>} then <code>GNUTLS_E_INTERRUPTED</code> will be returned. If <code>GNUTLS_E_INTERRUPTED</code> or <code>GNUTLS_E_AGAIN</code> is returned, you must call this function again, with the same parameters; alternatively you could provide a <code>NULL</code> pointer for data, and 0 for size.</p>
<h2>RETURNS</h2>
<p> The number of bytes sent, or a negative error code.</p>
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
