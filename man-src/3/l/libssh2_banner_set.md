---
title: "libssh2_banner_set(3)"
name: "libssh2_banner_set"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_banner_set/"
description: "libssh2_banner_set – set the SSH prococol banner for the local client"
---

<h2>NAME</h2>
<p> libssh2_banner_set &#8211; set the SSH prococol banner for the local client</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_banner_set(LIBSSH2_SESSION *session, const char *banner); </p>
<h2>DESCRIPTION</h2>
<p> This function is <code>DEPRECATED</code>. Use <i><a href="/docs/linux/man/3-libssh2_session_banner_set/">libssh2_session_banner_set</a>(3)</i> instead! </p>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>banner</i> &#8211; A pointer to a user defined banner </p>
<p> Set the banner that will be sent to the remote host when the SSH session is started with <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</code><br />
&nbsp;<wbr>&nbsp;<wbr>This is optional;&nbsp;<wbr>a banner corresponding to the protocol and libssh2 version will be sent by default.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>AVAILABILITY</h2>
<p> Marked as deprecated since 1.4.0</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</code> </p>
<h2>Index</h2>
