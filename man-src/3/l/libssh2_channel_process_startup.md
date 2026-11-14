---
title: "libssh2_channel_process_startup(3)"
name: "libssh2_channel_process_startup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_process_startup/"
description: "libssh2_channel_process_startup – request a shell on a channel"
---

<h2>NAME</h2>
<p> libssh2_channel_process_startup &#8211; request a shell on a channel</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
int libssh2_channel_process_startup(LIBSSH2_CHANNEL *channel,
                                    const char *request,
                                    unsigned int request_len,
                                    const char *message,
                                    unsigned int message_len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Active session channel instance. </p>
<p> <i>request</i> &#8211; Type of process to startup. The SSH2 protocol currently defines shell, exec, and subsystem as standard process services. </p>
<p> <i>request_len</i> &#8211; Length of request parameter. </p>
<p> <i>message</i> &#8211; Request specific message data to include. </p>
<p> <i>message_len</i> &#8211; Length of message parameter. </p>
<p> Initiate a request on a session type channel such as returned by <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code></p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_REQUEST_DENIED</i> &#8211;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
