---
title: "libssh2_channel_flush_ex(3)"
name: "libssh2_channel_flush_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_flush_ex/"
description: "libssh2_channel_flush_ex – flush a channel"
---

<h2>NAME</h2>
<p> libssh2_channel_flush_ex &#8211; flush a channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_flush_ex(LIBSSH2_CHANNEL *channel, int streamid); </p>
<p> int libssh2_channel_flush(LIBSSH2_CHANNEL *channel); </p>
<p> int libssh2_channel_flush_stderr(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Active channel stream to flush. </p>
<p> <i>streamid</i> &#8211; Specific substream number to flush. Groups of substreams may be flushed by passing on of the following Constants.<br />
 <code>LIBSSH2_CHANNEL_FLUSH_EXTENDED_DATA</code>: Flush all extended data substreams<br />
 <code>LIBSSH2_CHANNEL_FLUSH_ALL</code>: Flush all substreams </p>
<p> Flush the read buffer for a given channel instance. Individual substreams may be flushed by number or using one of the provided macros. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>Index</h2>
