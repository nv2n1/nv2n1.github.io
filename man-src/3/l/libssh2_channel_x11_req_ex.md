---
title: "libssh2_channel_x11_req_ex(3)"
name: "libssh2_channel_x11_req_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_x11_req_ex/"
description: "libssh2_channel_x11_req_ex – request an X11 forwarding channel"
---

<h2>NAME</h2>
<p> libssh2_channel_x11_req_ex &#8211; request an X11 forwarding channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_x11_req_ex(LIBSSH2_CHANNEL *channel, int single_connection, const char *auth_proto, const char *auth_cookie, int screen_number); </p>
<p> int libssh2_channel_x11_req(LIBSSH2_CHANNEL *channel, int screen_number); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Previously opened channel instance such as returned by <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<p> <i>single_connection</i> &#8211; non-zero to only forward a single connection. </p>
<p> <i>auth_proto</i> &#8211; X11 authentication protocol to use </p>
<p> <i>auth_cookie</i> &#8211; the cookie (hexadecimal encoded). </p>
<p> <i>screen_number</i> &#8211; the XLL screen to forward </p>
<p> Request an X11 forwarding on <i>channel</i>. To use X11 forwarding, <code><a href="/docs/linux/man/3-libssh2_session_callback_set/">libssh2_session_callback_set</a>(3)</code> must first be called to set <code>LIBSSH2_CALLBACK_X11</code>. This callback will be invoked when the remote host accepts the X11 forwarding. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_REQUEST_DENIED</i> &#8211; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_session_callback_set/">libssh2_session_callback_set</a>(3)</code> </p>
<h2>Index</h2>
