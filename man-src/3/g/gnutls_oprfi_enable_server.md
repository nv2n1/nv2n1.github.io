---
title: "gnutls_oprfi_enable_server(3)"
name: "gnutls_oprfi_enable_server"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_oprfi_enable_server/"
description: "gnutls_oprfi_enable_server – API function"
---

<h2>NAME</h2>
<p> gnutls_oprfi_enable_server &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/gnutls.h">gnutls/gnutls.h</a>&gt;</code> </p>
<p> <code>void gnutls_oprfi_enable_server(gnutls_session_t </code><i>session</i><code>, gnutls_oprfi_callback_func </code><i>cb</i><code>, void * </code><i>userdata</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure.</p>
<dt>gnutls_oprfi_callback_func cb</p>
<dd> function pointer to Opaque PRF extension server callback.</p>
<dt>void * userdata</p>
<dd> hook passed to callback function for passing application state.</dl>
<h2>DESCRIPTION</h2>
<p> Request that the server should attempt to accept the Opaque PRF Input TLS extension. If the client requests the extension, the provided callback <i>cb</i> will be invoked. The callback must have the following prototype: </p>
<p> int callback (gnutls_session_t session, void *userdata, size_t oprfi_len, const unsigned char *in_oprfi, unsigned char *out_oprfi); </p>
<p> The callback can inspect the client-provided data in the input parameters, and specify its own opaque prf input data in the output variable. The function must return 0 on success, otherwise the handshake will be aborted.</p>
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
