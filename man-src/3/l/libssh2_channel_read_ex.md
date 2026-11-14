---
title: "libssh2_channel_read_ex(3)"
name: "libssh2_channel_read_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_read_ex/"
description: "libssh2_channel_read_ex – read data from a channel stream"
---

<h2>NAME</h2>
<p> libssh2_channel_read_ex &#8211; read data from a channel stream</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> ssize_t libssh2_channel_read_ex(LIBSSH2_CHANNEL *channel, int stream_id, char *buf, size_t buflen); </p>
<p> ssize_t libssh2_channel_read(LIBSSH2_CHANNEL *channel, char *buf, size_t buflen); </p>
<p> ssize_t libssh2_channel_read_stderr(LIBSSH2_CHANNEL *channel, char *buf, size_t buflen); </p>
<h2>DESCRIPTION</h2>
<p> Attempt to read data from an active channel stream. All channel streams have one standard I/O substream (stream_id == 0), and may have up to 2^32 extended data streams as identified by the selected <i>stream_id</i>. The SSH2 protocol currently defines a stream ID of 1 to be the stderr substream. </p>
<p> <i>channel</i> &#8211; active channel stream to read from. </p>
<p> <i>stream_id</i> &#8211; substream ID number (e.g. 0 or SSH_EXTENDED_DATA_STDERR) </p>
<p> <i>buf</i> &#8211; pointer to storage buffer to read data into </p>
<p> <i>buflen</i> &#8211; size of the buf storage </p>
<p> <i><a href="/docs/linux/man/3-libssh2_channel_read/">libssh2_channel_read</a>(3)</i> and <i><a href="/docs/linux/man/3-libssh2_channel_read_stderr/">libssh2_channel_read_stderr</a>(3)</i> are macros.</p>
<h2>RETURN VALUE</h2>
<p> Actual number of bytes read or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<p> Note that a return value of zero (0) can in fact be a legitimate value and only signals that no payload data was read. It is not an error.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_CLOSED</i> &#8211; The channel has been closed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_poll_channel_read/">libssh2_poll_channel_read</a>(3)</code> </p>
<h2>Index</h2>
