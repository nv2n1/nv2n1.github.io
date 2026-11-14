---
title: "libssh2_channel_window_read_ex(3)"
name: "libssh2_channel_window_read_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_window_read_ex/"
description: "libssh2_channel_window_read_ex – Check the status of the read window"
---

<h2>NAME</h2>
<p> libssh2_channel_window_read_ex &#8211; Check the status of the read window</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> unsigned long libssh2_channel_window_read_ex(LIBSSH2_CHANNEL *channel,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long&nbsp;<wbr>*read_avail,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long&nbsp;<wbr>*window_size_initial)</p>
<h2>DESCRIPTION</h2>
<p> Check the status of the read window. Returns the number of bytes which the remote end may send without overflowing the window limit read_avail (if passed) will be populated with the number of bytes actually available to be read window_size_initial (if passed) will be populated with the window_size_initial as defined by the channel_open request</p>
<h2>RETURN VALUE</h2>
<p> The number of bytes which the remote end may send without overflowing the window limit</p>
<h2>ERRORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_receive_window_adjust/">libssh2_channel_receive_window_adjust</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_channel_window_write_ex/">libssh2_channel_window_write_ex</a>(3)</code> </p>
<h2>Index</h2>
