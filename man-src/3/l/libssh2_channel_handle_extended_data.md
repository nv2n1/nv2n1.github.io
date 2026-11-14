---
title: "libssh2_channel_handle_extended_data(3)"
name: "libssh2_channel_handle_extended_data"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_handle_extended_data/"
description: "libssh2_channel_handle_extended_data – set extended data handling mode"
---

<h2>NAME</h2>
<p> libssh2_channel_handle_extended_data &#8211; set extended data handling mode</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_channel_handle_extended_data(LIBSSH2_CHANNEL *channel, int ignore_mode); </p>
<h2>DESCRIPTION</h2>
<p> This function is deprecated. Use the <i><a href="/docs/linux/man/3-libssh2_channel_handle_extended_data2/">libssh2_channel_handle_extended_data2</a>(3)</i> function instead! </p>
<p> <i>channel</i> &#8211; Active channel stream to change extended data handling on. </p>
<p> <i>ignore_mode</i> &#8211; One of the three LIBSSH2_CHANNEL_EXTENDED_DATA_* Constants.<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_NORMAL</code>: Queue extended data for eventual reading<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_MERGE</code>: Treat extended data and ordinary data the same. Merge all substreams such that calls to <i><a href="/docs/linux/man/3-libssh2_channel_read/">libssh2_channel_read</a>(3)</i> will pull from all substreams on a first-in/first-out basis.<br />
 <code>LIBSSH2_CHANNEL_EXTENDED_DATA_IGNORE</code>: Discard all extended data as it arrives. </p>
<p> Change how a channel deals with extended data packets. By default all extended data is queued until read by <i><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</i></p>
<h2>RETURN VALUE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_handle_extended_data2/">libssh2_channel_handle_extended_data2</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</code> </p>
<h2>Index</h2>
