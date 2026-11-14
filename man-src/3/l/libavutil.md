---
title: "libavutil(3)"
name: "libavutil"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libavutil/"
description: "libavutil – multimedia-biased utility library"
---

<h2 class="name">NAME</h2>
<p> libavutil &#8211; multimedia-biased utility library </p>
<h2>DESCRIPTION</h2>
<p> The libavutil library is a utility library to aid portable multimedia programming. It contains safe portable string functions, random number generators, data structures, additional mathematics functions, cryptography and multimedia related functionality (like enumerations for pixel and sample formats). It is not a library for code needed by both libavcodec and libavformat. </p>
<p> The goals for this library is to be:</p>
<dl>
<dt><code>Modular</code></p>
<dd> It should have few interdependencies and the possibility of disabling individual parts during <code>./configure</code>.</p>
<dt><code>Small</code></p>
<dd> Both sources and objects should be small.</p>
<dt><code>Efficient</code></p>
<dd> It should have low <font SIZE="-1">CPU</font> and memory usage.</p>
<dt><code>Useful</code></p>
<dd> It should avoid useless features that almost no one needs.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></i>(1), <i><a href="/docs/linux/man/1-ffplay/">ffplay</a></i>(1), <i><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></i>(1), <i><a href="/docs/linux/man/1-ffserver/">ffserver</a></i>(1), <i><a href="/docs/linux/man/1-ffmpeg-utils/">ffmpeg-utils</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
