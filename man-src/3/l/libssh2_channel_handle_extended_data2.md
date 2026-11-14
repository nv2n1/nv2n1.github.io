---
title: "libssh2_channel_handle_extended_data2(3)"
name: "libssh2_channel_handle_extended_data2"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_handle_extended_data2/"
description: "libssh2_channel_handle_extended_data2 – set extended data handling mode"
---

<h2>NAME</h2>
<p> libssh2_channel_handle_extended_data2 &#8211; set extended data handling mode</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_handle_extended_data2(LIBSSH2_CHANNEL *channel, int ignore_mode); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Active channel stream to change extended data handling on. </p>
<p> <i>ignore_mode</i> &#8211; One of the three LIBSSH2_CHANNEL_EXTENDED_DATA_* Constants.<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_NORMAL</code>: Queue extended data for eventual reading<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_MERGE</code>: Treat extended data and ordinary data the same. Merge all substreams such that calls to <code><a href="/docs/linux/man/3-libssh2_channel_read/">libssh2_channel_read</a>(3)</code> will pull from all substreams on a first-in/first-out basis.<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_IGNORE</code>: Discard all extended data as it arrives. </p>
<p> Change how a channel deals with extended data packets. By default all extended data is queued until read by <code><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</code> </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or LIBSSH2_ERROR_EAGAIN when it would otherwise block. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_handle_extended_data/">libssh2_channel_handle_extended_data</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</code> </p>
<h2>Index</h2>
