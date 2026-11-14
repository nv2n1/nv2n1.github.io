---
title: "gnutls_ia_recv(3)"
name: "gnutls_ia_recv"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_recv/"
description: "gnutls_ia_recv – read data from the TLS/IA protocol"
---

<h2>NAME</h2>
<p> gnutls_ia_recv &#8211; read data from the TLS/IA protocol</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>ssize_t gnutls_ia_recv(gnutls_session_t </code><i>session</i><code>, char * </code><i>data</i><code>, size_t </code><i>sizeofdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>char * data</p>
<dd> the buffer that the data will be read into, must hold &gt;= 12 bytes.</p>
<dt>size_t sizeofdata</p>
<dd> the number of requested bytes, must be &gt;= 12.</dl>
<h2>DESCRIPTION</h2>
<p> Receive TLS/IA data. This function has the similar semantics with <code>recv()</code>. The only difference is that it accepts a GnuTLS session, and uses different error codes. </p>
<p> If the server attempt to finish an application phase, this function will return <code>GNUTLS_E_WARNING_IA_IPHF_RECEIVED</code> or <code>GNUTLS_E_WARNING_IA_FPHF_RECEIVED</code>. The caller should then invoke <code>gnutls_ia_verify_endphase()</code>, and if it runs the client side, also send an endphase message of its own using gnutls_ia_endphase_send. </p>
<p> If EINTR is returned by the internal push function (the default is <i>code</i>{<code>recv()</code>}) then GNUTLS_E_INTERRUPTED will be returned. If GNUTLS_E_INTERRUPTED or GNUTLS_E_AGAIN is returned, you must call this function again, with the same parameters; alternatively you could provide a NULL pointer for data, and 0 for size.</p>
<h2>RETURNS</h2>
<p> The number of bytes received. A negative error code is returned in case of an error. The <code>GNUTLS_E_WARNING_IA_IPHF_RECEIVED</code> and <code>GNUTLS_E_WARNING_IA_FPHF_RECEIVED</code> errors are returned when an application phase finished message has been sent by the server.</p>
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
