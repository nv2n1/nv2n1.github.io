---
title: "libssh2_channel_request_pty_ex(3)"
name: "libssh2_channel_request_pty_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_request_pty_ex/"
description: "libssh2_channel_request_pty_ex – short function description"
---

<h2>NAME</h2>
<p> libssh2_channel_request_pty_ex &#8211; short function description</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_request_pty_ex(LIBSSH2_CHANNEL *channel, const char *term, unsigned int term_len, const char *modes, unsigned int modes_len, int width, int height, int width_px, int height_px); </p>
<p> int libssh2_channel_request_pty(LIBSSH2_CHANNEL *channel, char *term); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Previously opened channel instance such as returned by <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<p> <i>term</i> &#8211; Terminal emulation (e.g. vt102, ansi, etc&#8230;) </p>
<p> <i>term_len</i> &#8211; Length of term parameter </p>
<p> <i>modes</i> &#8211; Terminal mode modifier values </p>
<p> <i>modes_len</i> &#8211; Length of modes parameter. </p>
<p> <i>width</i> &#8211; Width of pty in characters </p>
<p> <i>height</i> &#8211; Height of pty in characters </p>
<p> <i>width_px</i> &#8211; Width of pty in pixels </p>
<p> <i>height_px</i> &#8211; Height of pty in pixels </p>
<p> Request a PTY on an established channel. Note that this does not make sense for all channel types and may be ignored by the server despite returning success.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_REQUEST_DENIED</i> &#8211;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
