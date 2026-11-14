---
title: "gnutls_ia_extract_inner_secret(3)"
name: "gnutls_ia_extract_inner_secret"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_extract_inner_secret/"
description: "gnutls_ia_extract_inner_secret – API function"
---

<h2>NAME</h2>
<p> gnutls_ia_extract_inner_secret &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>void gnutls_ia_extract_inner_secret(gnutls_session_t </code><i>session</i><code>, char * </code><i>buffer</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>char * buffer</p>
<dd> pre-allocated buffer to hold 48 bytes of inner secret.</dl>
<h2>DESCRIPTION</h2>
<p> Copy the 48 bytes large inner secret into the specified buffer </p>
<p> This function is typically used after the TLS/IA handshake has concluded. The TLS/IA inner secret can be used as input to a PRF to derive session keys. Do not use the inner secret directly as a session key, because for a resumed session that does not include an application phase, the inner secret will be identical to the inner secret in the original session. It is important to include, for example, the client and server randomness when deriving a sesssion key from the inner secret.</p>
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
