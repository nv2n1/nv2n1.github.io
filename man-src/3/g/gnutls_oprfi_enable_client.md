---
title: "gnutls_oprfi_enable_client(3)"
name: "gnutls_oprfi_enable_client"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_oprfi_enable_client/"
description: "gnutls_oprfi_enable_client – API function"
---

<h2>NAME</h2>
<p> gnutls_oprfi_enable_client &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_oprfi_enable_client(gnutls_session_t </code><i>session</i><code>, size_t </code><i>len</i><code>, unsigned char * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>size_t len</p>
<dd> length of Opaque PRF data to use in client.</p>
<dt>unsigned char * data</p>
<dd> Opaque PRF data to use in client.</dl>
<h2>DESCRIPTION</h2>
<p> Request that the client should attempt to negotiate the Opaque PRF Input TLS extension, using the given data as the client&#8217;s Opaque PRF input. </p>
<p> The data is copied into the session context after this call, so you may de-allocate it immediately after calling this function.</p>
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
