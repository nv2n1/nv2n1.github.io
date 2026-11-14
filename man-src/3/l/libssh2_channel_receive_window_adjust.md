---
title: "libssh2_channel_receive_window_adjust(3)"
name: "libssh2_channel_receive_window_adjust"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_receive_window_adjust/"
description: "libssh2_channel_receive_window_adjust – adjust the channel window"
---

<h2>NAME</h2>
<p> libssh2_channel_receive_window_adjust &#8211; adjust the channel window</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> unsigned long libssh2_channel_receive_window_adjust(LIBSSH2_CHANNEL * channel,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long adjustment,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char force); </p>
<h2>DESCRIPTION</h2>
<p> This function is deprecated in 1.1. Use <i><a href="/docs/linux/man/3-libssh2_channel_receive_window_adjust2/">libssh2_channel_receive_window_adjust2</a>(3)</i>! </p>
<p> Adjust the receive window for a channel by adjustment bytes. If the amount to be adjusted is less than LIBSSH2_CHANNEL_MINADJUST and force is 0 the adjustment amount will be queued for a later packet.</p>
<h2>RETURN VALUE</h2>
<p> Returns the new size of the receive window (as understood by remote end). Note that the window value sent over the wire is strictly 32bit, but this API is made to return a &#8216;long&#8217; which may not be 32 bit on all platforms.</p>
<h2>ERRORS</h2>
<p> In 1.0 and earlier, this function returns LIBSSH2_ERROR_EAGAIN for non-blocking channels where it would otherwise block. However, that is a negative number and this function only returns an unsigned value and this then leads to a very strange value being returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_window_read_ex/">libssh2_channel_window_read_ex</a>(3)</code> </p>
<h2>Index</h2>
