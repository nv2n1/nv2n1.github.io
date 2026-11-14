---
title: "moggsplit(1)"
name: "moggsplit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-moggsplit/"
description: "moggsplit – split Ogg logical streams"
---

<h2>NAME</h2>
<p> moggsplit &#8211; split Ogg logical streams</p>
<h2>SYNOPSIS</h2>
<p> <code>moggsplit</code> <i>filename</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>moggsplit</code> splits a multiplexed Ogg stream into separate files. For example, it can separate an OGM into separate Ogg DivX and Ogg Vorbis streams, or a chained Ogg Vorbis file into two separate files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;extension</code></p>
<dd> Use the supplied extension when generating new files; the default is <code>ogg</code>.</p>
<dt><code>&#8211;pattern</code></p>
<dd> Use the supplied pattern when generating new files. This is a Python keyword format string with three variables, <i>base</i> for the original file&#8217;s base name, <i>stream</i> for the stream&#8217;s serial number, and ext for the extension give by <code>&#8211;extension</code>. </p>
<p> The default is <code>%(base)s-%(stream)d.%(ext)s</code>.</p>
<dt><code>&#8211;m3u</code></p>
<dd> Generate an m3u playlist along with the newly generated files. Useful for large chained Oggs.</dl>
<h2>AUTHOR</h2>
<p> Joe Wreschnig </p>
<h2>Index</h2>
