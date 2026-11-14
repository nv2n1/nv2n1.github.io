---
title: "mpeg2desc(1)"
name: "mpeg2desc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpeg2desc/"
description: "mpeg2desc – multiplex audio/video streams"
---

<h2 class="name">NAME</h2>
<p> mpeg2desc &#8211; multiplex audio/video streams </p>
<h2>SYNOPSIS</h2>
<p> <code>mpeg2desc</code> [ <code>-a </code><i>stream</i> ] [ <code>-v </code><i>stream</i> ] [ <code>-o </code><i>FILE</i> ] [ <code>-s </code> ] [ <code>-m </code> ] [ <code>-h </code> ] [ <i>&lt; movie.mpg</i><i> &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>mpeg2desc</code> multiplexes audio and video streams</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>stream</i></p>
<dd> Output audio <i>stream</i> (0 .. 31) to stdout</p>
<dt><code>-v </code><i>stream</i></p>
<dd> Output video <i>stream</i> (0 .. 15) to stdout</p>
<dt><code>-o </code><i>FILE</i></p>
<dd> output the previous stream to <i>FILE</i> instead of stdout</p>
<dt><code>-s</code></p>
<dd> skip to first valid header &#8212; ensures mplex can handle output</p>
<dt><code>-m</code></p>
<dd> output mplex offset to stdout</p>
<dt><code>-u</code></p>
<dd> do not output messages about unrecognized headers</p>
<dt><code>-h</code></p>
<dd> show short help</dl>
<h2>USAGE</h2>
<p> <code>mpeg2desc</code> mpeg2desc [options] &lt; movie.mpg</p>
<h2>CAVEATS</h2>
<p> None.</p>
<h2>BUGS</h2>
<p> None.</p>
<h2>AUTHOR</h2>
<p> MarcLeemanThis manual page was written by Marc Leeman &lt;marc.leeman [at] gmail.com&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
