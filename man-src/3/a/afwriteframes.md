---
title: "afwriteframes(3)"
name: "afwriteframes"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afwriteframes/"
description: "afWriteFrames – write sample frames to a track in an audio file"
---

<p>afWriteFrames &#8211; write sample frames to a track in an audio file </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>AFframecount afWriteFrames(AFfilehandle file, int track, const void *data,
 AFframecount count);</pre>
<h2>Description</h2>
<p>afWriteFrames attempts to write up to <i>count</i> frames of audio data from the buffer <i>data</i> to the audio file handle <i>file</i>.</p>
<h2>Parameters</h2>
<p><i>file</i> is a valid file handle returned by <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3). </p>
<p> <i>track</i> is always AF_DEFAULT_TRACK for all currently supported file formats. </p>
<p> <i>data</i> is a buffer of sample frames to be written to the file. </p>
<p> <i>count</i> is the number of sample frames to be written.</p>
<h2>Return Value</h2>
<p>afWriteFrames returns the number of sample frames successfully written to <i>file</i>.</p>
<h2>Errors</h2>
<p>afWriteFrames can produce these errors: </p>
<p> AF_BAD_FILEHANDLE</p>
<dl COMPACT>
<dd>the file handle was invalid</dl>
<p> AF_BAD_TRACKID</p>
<dl COMPACT>
<dd>the track is not AF_DEFAULT_TRACK</dl>
<p> AF_BAD_WRITE</p>
<dl COMPACT>
<dd>writing audio data to the file failed</dl>
<p> AF_BAD_LSEEK</p>
<dl COMPACT>
<dd>seeking within the file failed</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afreadframes/">afReadFrames</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
