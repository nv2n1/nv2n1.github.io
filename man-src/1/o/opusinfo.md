---
title: "opusinfo(1)"
name: "opusinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opusinfo/"
description: "opusinfo – gives information about Opus files and does extensive validity checking"
---

<h2 class="name">NAME</h2>
<p> opusinfo &#8211; gives information about Opus files and does extensive validity checking</p>
<h2>SYNOPSIS</h2>
<p> <code>opusinfo</code> [ <code>-q</code> | <code>-v</code> ] [ <code>-h</code> ] [ <code>-V</code> ] <i>file1.opus</i> <code>&#8230;</code> <i>fileN.opus</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>opusinfo</code> reads one or more Opus files and prints information about stream contents (including chained and/or multiplexed streams) to standard output. It will detect (but not correct) a wide range of common defects, with many additional checks specifically for Opus streams. </p>
<p> For all stream types <code>opusinfo</code> will print the filename being processed, the stream serial numbers, and various common error conditions. </p>
<p> For <code>Opus</code> streams, information including the version used for encoding, number of channels and other header information, the bitrate and playback length, the contents of the comment header, and general statistics about the stream are printed. </p>
<p> Opusinfo is a fork of <code><a href="/docs/linux/man/1-ogginfo/">ogginfo</a></code>(1) with the non-opus parts largely removed. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</dt>
<dd> Show a help and usage message.</dd>
<dt>-q</dt>
<dd> Quiet mode. This may be specified multiple times. Doing so once will remove the detailed informative messages; twice will remove warnings as well.</dd>
<dt>-v</dt>
<dd> Verbose mode. At the current time, this does not do anything.</dd>
<dt>-V</dt>
<dd> Show program version info and exit. </dd>
</dl>
<h2>NOTES</h2>
<p> There are many kinds of errored, invalid, non-normative, or otherwise unwise stream constructions which opusinfo will not produce warnings on. Passing opusinfo with flying colors is not certification of the correctness of a stream. Future versions may detect more error conditions. </p>
<h2>AUTHORS</h2>
<p> Michael Smith &lt;msmith [at] xiph.org&gt;<br />
 Gregory Maxwell &lt;greg [at] xiph.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-opusdec/">opusdec</a></code>(1), <code><a href="/docs/linux/man/1-opusenc/">opusenc</a></code>(1) </p>
<h2>Index</h2>
