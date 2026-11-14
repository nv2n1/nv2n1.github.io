---
title: "afreadframes(3)"
name: "afreadframes"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afreadframes/"
description: "afReadFrames – read sample frames from a track in an audio file"
---

<p>afReadFrames &#8211; read sample frames from a track in an audio file </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>AFframecount afReadFrames(AFfilehandle file, int track, void *data,
 int count);</pre>
<h2>Description</h2>
<p>afReadFrames attempts to read up to <i>count</i> frames of audio data from the audio file handle <i>file</i> into the buffer at <i>data</i>.</p>
<h2>Parameters</h2>
<p><i>file</i> is a valid file handle returned by <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3). </p>
<p> <i>track</i> is always AF_DEFAULT_TRACK for all currently supported file formats. </p>
<p> <i>data</i> is a buffer of storing <i>count</i> frames of audio sample data. </p>
<p> <i>count</i> is the number of sample frames to be read.</p>
<h2>Return Value</h2>
<p>afReadFrames returns the number of frames successfully read from <i>file</i>.</p>
<h2>Errors</h2>
<p>afReadFrames can produce these errors: </p>
<p> AF_BAD_FILEHANDLE</p>
<dl COMPACT>
<dd>the file handle was invalid</dl>
<p> AF_BAD_TRACKID</p>
<dl COMPACT>
<dd>the track parameter is not AF_DEFAULT_TRACK</dl>
<p> AF_BAD_READ</p>
<dl COMPACT>
<dd>reading audio data from the file failed</dl>
<p> AF_BAD_LSEEK</p>
<dl COMPACT>
<dd>seeking within the file failed</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afwriteframes/">afWriteFrames</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
