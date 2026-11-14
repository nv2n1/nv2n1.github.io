---
title: "gnutls_ia_verify_endphase(3)"
name: "gnutls_ia_verify_endphase"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_verify_endphase/"
description: "gnutls_ia_verify_endphase – API function"
---

<h2>NAME</h2>
<p> gnutls_ia_verify_endphase &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>int gnutls_ia_verify_endphase(gnutls_session_t </code><i>session</i><code>, const char * </code><i>checksum</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>const char * checksum</p>
<dd> 12-byte checksum data, received from <code>gnutls_ia_recv()</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Verify TLS/IA end phase checksum data. If verification fails, the <code>GNUTLS_A_INNER_APPLICATION_VERIFICATION</code> alert is sent to the other sie. </p>
<p> This function is called when <code>gnutls_ia_recv()</code> return <code>GNUTLS_E_WARNING_IA_IPHF_RECEIVED</code> or <code>GNUTLS_E_WARNING_IA_FPHF_RECEIVED</code>.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on successful verification, or an error code. If the checksum verification of the end phase message fails, <code>GNUTLS_E_IA_VERIFY_FAILED</code> is returned.</p>
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
