---
title: "libssh2_channel_eof(3)"
name: "libssh2_channel_eof"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_eof/"
description: "libssh2_channel_eof – check a channel’s EOF status"
---

<h2>NAME</h2>
<p> libssh2_channel_eof &#8211; check a channel&#8217;s EOF status</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_eof(LIBSSH2_CHANNEL *channel);</p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; active channel stream to set closed status on. </p>
<p> Check if the remote host has sent an EOF status for the selected stream.</p>
<h2>RETURN VALUE</h2>
<p> Returns 1 if the remote host has sent EOF, otherwise 0. Negative on failure.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_close/">libssh2_channel_close</a>(3)</code> </p>
<h2>Index</h2>
