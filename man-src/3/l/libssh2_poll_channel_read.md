---
title: "libssh2_poll_channel_read(3)"
name: "libssh2_poll_channel_read"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_poll_channel_read/"
description: "libssh2_poll_channel_read – check if data is available"
---

<h2>NAME</h2>
<p> libssh2_poll_channel_read &#8211; check if data is available</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_poll_channel_read(LIBSSH2_CHANNEL *channel, int extended);</p>
<h2>DESCRIPTION</h2>
<p> This function is deprecated. Do note use. </p>
<p> <i><a href="/docs/linux/man/3-libssh2_poll_channel_read/">libssh2_poll_channel_read</a>(3)</i> checks to see if data is available in the <i>channel</i>&#8216;s read buffer. No attempt is made with this method to see if packets are available to be processed. For full polling support, use <i><a href="/docs/linux/man/3-libssh2_poll/">libssh2_poll</a>(3)</i>.</p>
<h2>RETURN VALUE</h2>
<p> Returns 1 when data is available and 0 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_poll/">libssh2_poll</a>(3)</code> </p>
<h2>Index</h2>
