---
title: "libssh2_session_methods(3)"
name: "libssh2_session_methods"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_methods/"
description: "libssh2_session_methods – return the currently active algorithms"
---

<h2>NAME</h2>
<p> libssh2_session_methods &#8211; return the currently active algorithms</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> const char * libssh2_session_methods(LIBSSH2_SESSION *session, int method_type); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>method_type</i> &#8211; one of the method type constants: LIBSSH2_METHOD_KEX, LIBSSH2_METHOD_HOSTKEY, LIBSSH2_METHOD_CRYPT_CS, LIBSSH2_METHOD_CRYPT_SC, LIBSSH2_METHOD_MAC_CS, LIBSSH2_METHOD_MAC_SC, LIBSSH2_METHOD_COMP_CS, LIBSSH2_METHOD_COMP_SC, LIBSSH2_METHOD_LANG_CS, LIBSSH2_METHOD_LANG_SC. </p>
<p> Returns the actual method negotiated for a particular transport parameter.</p>
<h2>RETURN VALUE</h2>
<p> Negotiated method or NULL if the session has not yet been started.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_INVAL</i> &#8211; The requested method type was invalid. </p>
<p> <i>LIBSSH2_ERROR_METHOD_NONE</i> &#8211; no method has been set</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
