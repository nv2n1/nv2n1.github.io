---
title: "gnutls_ia_set_client_avp_function(3)"
name: "gnutls_ia_set_client_avp_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_ia_set_client_avp_function/"
description: "gnutls_ia_set_client_avp_function – Used to set a AVP callback"
---

<h2>NAME</h2>
<p> gnutls_ia_set_client_avp_function &#8211; Used to set a AVP callback</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gnutls/extra.h">gnutls/extra.h</a>&gt;</code> </p>
<p> <code>void gnutls_ia_set_client_avp_function(gnutls_ia_client_credentials_t </code><i>cred</i><code>, gnutls_ia_avp_func </code><i>avp_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_ia_client_credentials_t cred</p>
<dd> is a <code>gnutls_ia_client_credentials_t</code> structure.</p>
<dt>gnutls_ia_avp_func avp_func</p>
<dd> is the callback function</dl>
<h2>DESCRIPTION</h2>
<p> Set the TLS/IA AVP callback handler used for the session. </p>
<p> The AVP callback is called to process AVPs received from the server, and to get a new AVP to send to the server. </p>
<p> The callback&#8217;s function form is: int (*avp_func) (gnutls_session_t session, void *ptr, const char *last, size_t lastlen, char **next, size_t *nextlen); </p>
<p> The <i>session</i> parameter is the <code>gnutls_session_t</code> structure corresponding to the current session. The <i>ptr</i> parameter is the application hook pointer, set through <code>gnutls_ia_set_client_avp_ptr()</code>. The AVP received from the server is present in <i>last</i> of <i>lastlen</i> size, which will be <code>NULL</code> on the first invocation. The newly allocated output AVP to send to the server should be placed in *<i>next</i> of *<i>nextlen</i> size. </p>
<p> The callback may invoke <code>gnutls_ia_permute_inner_secret()</code> to mix any generated session keys with the TLS/IA inner secret. </p>
<p> Return 0 (<code>GNUTLS_IA_APPLICATION_PAYLOAD</code>) on success, or a negative error code to abort the TLS/IA handshake. </p>
<p> Note that the callback must use allocate the <i>next</i> parameter using <code>gnutls_malloc()</code>, because it is released via <code>gnutls_free()</code> by the TLS/IA handshake function.</p>
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
