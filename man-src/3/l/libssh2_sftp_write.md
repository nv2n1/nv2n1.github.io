---
title: "libssh2_sftp_write(3)"
name: "libssh2_sftp_write"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_write/"
description: "libssh2_sftp_write – write SFTP data"
---

<h2>NAME</h2>
<p> libssh2_sftp_write &#8211; write SFTP data</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
ssize_t libssh2_sftp_write(LIBSSH2_SFTP_HANDLE *handle,
                           const char *buffer,
                           size_t count);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_write/">libssh2_sftp_write</a>(3)</code> writes a block of data to the SFTP server. This method is modeled after the POSIX write() function and uses the same calling semantics. </p>
<p> <i>handle</i> &#8211; SFTP file handle as returned by <i><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</i>. </p>
<p> <i>buffer</i> &#8211; points to the data to send off. </p>
<p> <i>count</i> &#8211; Number of bytes from &#8216;buffer&#8217; to write. Note that it may not be possible to write all bytes as requested. </p>
<p> <i><a href="/docs/linux/man/3-libssh2_sftp_handle/">libssh2_sftp_handle</a>(3)</i> will use as much as possible of the buffer and put it into a single SFTP protocol packet. This means that to get maximum performance when sending larger files, you should try to always pass in at least 32K of data to this function. </p>
<h2>WRITE AHEAD</h2>
<p> Starting in libssh2 version 1.2.8, the default behavior of libssh2 is to create several smaller outgoing packets for all data you pass to this function and it will return a positive number as soon as the first packet is acknowledged from the server. </p>
<p> This has the effect that sometimes more data has been sent off but isn&#8217;t acked yet when this function returns, and when this function is subsequently called again to write more data, libssh2 will immediately figure out that the data is already received remotely. </p>
<p> In most normal situation this should not cause any problems, but it should be noted that if you&#8217;ve once called libssh2_sftp_write() with data and it returns short, you MUST still assume that the rest of the data might&#8217;ve been cached so you need to make sure you don&#8217;t alter that data and think that the version you have in your next function invoke will be detected or used. </p>
<p> The reason for this funny behavior is that SFTP can only send 32K data in each packet and it gets all packets acked individually. This means we cannot use a simple serial approach if we want to reach high performance even on high latency connections. And we want that.</p>
<h2>RETURN VALUE</h2>
<p> Actual number of bytes written or negative on failure. </p>
<p> If used in non-blocking mode, it returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<p> If this function returns 0 (zero) it should not be considered an error, but simply that there was no error but yet no payload data got sent to the other end.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
