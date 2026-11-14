---
title: "libssh2_channel_receive_window_adjust2(3)"
name: "libssh2_channel_receive_window_adjust2"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_receive_window_adjust2/"
description: "libssh2_channel_receive_window_adjust2 – adjust the channel window"
---

<h2>NAME</h2>
<p> libssh2_channel_receive_window_adjust2 &#8211; adjust the channel window</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_receive_window_adjust2(LIBSSH2_CHANNEL * channel,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long adjustment,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char force,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned int&nbsp;<wbr>*window); </p>
<h2>DESCRIPTION</h2>
<p> Adjust the receive window for a channel by adjustment bytes. If the amount to be adjusted is less than LIBSSH2_CHANNEL_MINADJUST and force is 0 the adjustment amount will be queued for a later packet. </p>
<p> This function stores the new size of the receive window (as understood by remote end) in the variable &#8216;window&#8217; points to.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success and a negative value on error. If used in non-blocking mode it will return LIBSSH2_ERROR_EAGAIN when it would otherwise block.</p>
<h2>ERRORS</h2>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.1 since the previous API has deficiencies.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_window_read_ex/">libssh2_channel_window_read_ex</a>(3)</code> </p>
<h2>Index</h2>
