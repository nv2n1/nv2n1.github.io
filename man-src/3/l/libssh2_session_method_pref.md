---
title: "libssh2_session_method_pref(3)"
name: "libssh2_session_method_pref"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_method_pref/"
description: "libssh2_session_method_pref – set preferred key exchange method"
---

<h2>NAME</h2>
<p> libssh2_session_method_pref &#8211; set preferred key exchange method</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_method_pref(LIBSSH2_SESSION *session, int method_type, const char *prefs); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>method_type</i> &#8211; One of the Method Type constants. </p>
<p> <i>prefs</i> &#8211; Coma delimited list of preferred methods to use with the most preferred listed first and the least preferred listed last. If a method is listed which is not supported by libssh2 it will be ignored and not sent to the remote host during protocol negotiation. </p>
<p> Set preferred methods to be negotiated. These preferrences must be set prior to calling <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</code> as they are used during the protocol initiation phase. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_INVAL</i> &#8211; The requested method type was invalid. </p>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_METHOD_NOT_SUPPORTED</i> &#8211; The requested method is not supported. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</code> </p>
<h2>Index</h2>
