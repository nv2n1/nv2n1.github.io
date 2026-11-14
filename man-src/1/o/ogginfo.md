---
title: "ogginfo(1)"
name: "ogginfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogginfo/"
description: "ogginfo – gives information about Ogg files, and does extensive validity checking"
---

<h2 class="name">NAME</h2>
<p> ogginfo &#8211; gives information about Ogg files, and does extensive validity checking</p>
<h2>SYNOPSIS</h2>
<p> <code>ogginfo</code> [ <code>-q</code> ] [ <code>-v</code> ] [ <code>-h</code> ] <i>file1.ogg</i> <code>&#8230;</code> <i>fileN.ogg</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ogginfo</code> reads one or more Ogg files and prints information about stream contents (including chained and/or multiplexed streams) to standard output. It will detect (but not correct) a wide range of common defects, with many additional checks specifically for Ogg Vorbis streams. </p>
<p> For all stream types <code>ogginfo</code> will print the filename being processed, the stream serial numbers, and various common error conditions. </p>
<p> For <code>Vorbis</code> streams, information including the version used for encoding, the sample rate and number of channels, the bitrate and playback length, and the contents of the comment header are printed. </p>
<p> Similarly, for <code>Theora</code> streams, basic information about the video is provided, including frame rate, aspect ratio, bitrate, length, and the comment header. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> Show a help and usage message.</p>
<dt>-q</p>
<dd> Quiet mode. This may be specified multiple times. Doing so once will remove the detailed informative messages, twice will remove warnings as well.</p>
<dt>-v</p>
<dd> Verbose mode. At the current time, this does not do anything.</p>
<dt>-V</p>
<dd> Output version information and exit. </p>
</dl>
<h2>AUTHORS</h2>
<p> Michael Smith &lt;msmith [at] xiph.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vorbiscomment/">vorbiscomment</a></code>(1), <code><a href="/docs/linux/man/1-ogg123/">ogg123</a></code>(1), <code><a href="/docs/linux/man/1-oggdec/">oggdec</a></code>(1), <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1) </p>
<h2>Index</h2>
