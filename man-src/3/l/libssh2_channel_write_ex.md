---
title: "libssh2_channel_write_ex(3)"
name: "libssh2_channel_write_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_write_ex/"
description: "libssh2_channel_write_ex – write data to a channel stream blocking"
---

<h2>NAME</h2>
<p> libssh2_channel_write_ex &#8211; write data to a channel stream blocking</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
ssize_t libssh2_channel_write_ex(LIBSSH2_CHANNEL *channel,
                                 int stream_id, char *buf,
                                 size_t buflen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Write data to a channel stream. All channel streams have one standard I/O substream (stream_id == 0), and may have up to 2^32 extended data streams as identified by the selected <i>stream_id</i>. The SSH2 protocol currently defines a stream ID of 1 to be the stderr substream. </p>
<p> <i>channel</i> &#8211; active channel stream to write to. </p>
<p> <i>stream_id</i> &#8211; substream ID number (e.g. 0 or SSH_EXTENDED_DATA_STDERR) </p>
<p> <i>buf</i> &#8211; pointer to buffer to write </p>
<p> <i>buflen</i> &#8211; size of the data to write </p>
<p> <i><a href="/docs/linux/man/3-libssh2_channel_write/">libssh2_channel_write</a>(3)</i> and <i><a href="/docs/linux/man/3-libssh2_channel_write_stderr/">libssh2_channel_write_stderr</a>(3)</i> are convenience macros for this function. </p>
<p> <i><a href="/docs/linux/man/3-libssh2_channel_write_ex/">libssh2_channel_write_ex</a>(3)</i> will use as much as possible of the buffer and put it into a single SSH protocol packet. This means that to get maximum performance when sending larger files, you should try to always pass in at least 32K of data to this function.</p>
<h2>RETURN VALUE</h2>
<p> Actual number of bytes written or negative on failure. LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_CLOSED</i> &#8211; The channel has been closed. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_EOF_SENT</i> &#8211; The channel has been requested to be closed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</code> </p>
<h2>Index</h2>
