---
title: "libssh2_channel_open_ex(3)"
name: "libssh2_channel_open_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_open_ex/"
description: "libssh2_channel_open_ex – establish a generic session channel"
---

<h2>NAME</h2>
<p> libssh2_channel_open_ex &#8211; establish a generic session channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_CHANNEL * libssh2_channel_open_ex(LIBSSH2_SESSION *session, const char *channel_type, unsigned int channel_type_len, unsigned int window_size, unsigned int packet_size, const char *message, unsigned int message_len); </p>
<p> LIBSSH2_CHANNEL * libssh2_channel_open_session(session); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>channel_type</i> &#8211; Channel type to open. Typically one of session, direct-tcpip, or tcpip-forward. The SSH2 protocol allowed for additional types including local, custom channel types. </p>
<p> <i>channel_type_len</i> &#8211; Length of channel_type </p>
<p> <i>window_size</i> &#8211; Maximum amount of unacknowledged data remote host is allowed to send before receiving an SSH_MSG_CHANNEL_WINDOW_ADJUST packet. </p>
<p> <i>packet_size</i> &#8211; Maximum number of bytes remote host is allowed to send in a single SSH_MSG_CHANNEL_DATA or SSG_MSG_CHANNEL_EXTENDED_DATA packet. </p>
<p> <i>message</i> &#8211; Additional data as required by the selected channel_type. </p>
<p> <i>message_len</i> &#8211; Length of message parameter. </p>
<p> Allocate a new channel for exchanging data with the server. This method is typically called through its macroized form: <code><a href="/docs/linux/man/3-libssh2_channel_open_session/">libssh2_channel_open_session</a>(3)</code> or via <code><a href="/docs/linux/man/3-libssh2_channel_direct_tcpip/">libssh2_channel_direct_tcpip</a>(3)</code> or <code><a href="/docs/linux/man/3-libssh2_channel_forward_listen/">libssh2_channel_forward_listen</a>(3)</code> </p>
<h2>RETURN VALUE</h2>
<p> Pointer to a newly allocated LIBSSH2_CHANNEL instance, or NULL on errors. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_FAILURE</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block. </p>
<h2>SEE ALSO</h2>
<p> Add related functions </p>
<h2>Index</h2>
