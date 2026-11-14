---
title: "gnutls_ia_allocate_server_credentials(3)"
name: "gnutls_ia_allocate_server_credentials"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_allocate_server_credentials/"
description: "gnutls_ia_allocate_server_credentials – Used to allocate an gnutls_ia_server_credentials_t structure"
---

<h2>NAME</h2>
<p> gnutls_ia_allocate_server_credentials &#8211; Used to allocate an gnutls_ia_server_credentials_t structure</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>int gnutls_ia_allocate_server_credentials(gnutls_ia_server_credentials_t * </code><i>sc</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ia_server_credentials_t * sc</p>
<dd> is a pointer to a <code>gnutls_ia_server_credentials_t</code> structure.</dl>
<h2>DESCRIPTION</h2>
<p> This structure is complex enough to manipulate directly thus this helper function is provided in order to allocate it. </p>
<p> Adding this credential to a session will enable TLS/IA, and will require an Application Phase after the TLS handshake (if the client support TLS/IA). Use <code>gnutls_ia_require_inner_phase()</code> to toggle the TLS/IA mode.</p>
<h2>RETURNS</h2>
<p> On success, <code>GNUTLS_E_SUCCESS</code> (0) is returned, otherwise an error code is returned.</p>
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
