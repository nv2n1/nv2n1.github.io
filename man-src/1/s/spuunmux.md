---
title: "spuunmux(1)"
name: "spuunmux"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spuunmux/"
description: "spuunmux – demultiplexes subtitles from an existing mpeg2 program stream"
---

<h2 class="name">NAME</h2>
<p> spuunmux &#8211; demultiplexes subtitles from an existing mpeg2 program stream </p>
<h2>SYNOPSIS</h2>
<p> <code>spuunmux</code> [ <i>input file</i> ] [ <i>input file</i><i> &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>spuunmux</code> demultiplexes subtitles from an existing mpeg2 program stream</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o </code><i>name</i></p>
<dd> base name for script and images. Defaults to <i>sub</i>.</p>
<dt><code>-v </code><i>level</i></p>
<dd> verbosity level. <i>sub</i>. Defaults to <i>0</i>.</p>
<dt><code>-f</code></p>
<dd> resize images to full size, which is 720&#215;480 for NTSC, 720&#215;576 for PAL.</p>
<dt><code>-F PAL|NTSC</code></p>
<dd> specifies the video format, which is used to compute the dimensions of full size for -f.</p>
<dt><code>-s </code><i>stream</i></p>
<dd> number of the substream to extract. Defaults to <i>0</i>.</p>
<dt><code>-p </code><i>file</i></p>
<dd> name of file with dvd palette. If palette file ends with .rgb, treated as a RGB else as a YCbCr color</p>
<dt><code>-h</code></p>
<dd> print this help</p>
<dt><code>-V</code></p>
<dd> print version number</dl>
<h2>USAGE</h2>
<p> <code>spuunmux</code> inputfile1 inputfile2 </p>
<p> demultiplexes subtitles from an existing mpeg2 program stream. To use stdin for demultiplexing, use &#8211; for the inputfile: </p>
<p> play_cell GoldFinger.iso 1 1 6 | <code>spuunmux</code> &#8211;</p>
<h2>CAVEATS</h2>
<p> None.</p>
<h2>BUGS</h2>
<p> None.</p>
<h2>AUTHOR</h2>
<p> MarcLeemanThis manual page was written by Marc Leeman &lt;marc.leeman [at] gmail.com&gt;, for the Debian GNU/Linux system (but may be used by others). &lt;marc.leeman [at] gmail.com&gt; MarcLeeman2016Marc Leeman </p>
<h2>Index</h2>
