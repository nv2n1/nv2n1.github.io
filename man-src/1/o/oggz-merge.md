---
title: "oggz-merge(1)"
name: "oggz-merge"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-merge/"
description: "oggz-merge — Merge Ogg files together, interleaving pages in order of presentation time."
---

<h2>NAME</h2>
<p> oggz-merge &#8212; Merge Ogg files together, interleaving pages in order of presentation time.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-merge</code> [-o <code>filename</code> | &#8211;output <code>filename</code> ] filename &#8230; </p>
<p> <code>oggz-merge</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-merge</code> merges Ogg files together, interleaving pages in order of presentation time. It correctly interprets the granulepos timestamps of Ogg CELT, CMML, Dirac, FLAC, Kate, PCM, Speex, Theora and Vorbis bitstreams. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr> </p>
<p> For example, if you have an Ogg Theora video file, and its soundtrack stored separately as an Ogg Speex audio file, and you can use <code>oggz-merge</code> to create a single Ogg file containing the video and audio, interleaved together in parallel.<br />
&nbsp;<wbr> </p>
<p> Similarly, using <code>oggz-merge</code> on a collection of Ogg Vorbis audio files will create a big Ogg file with all the songs in parallel, ie. interleaved for simultaneous playback. Such a file is proper Ogg, but not &quot;Ogg Vorbis I&quot; &#8212; the Ogg Vorbis I specification defines an Ogg Vorbis file as an Ogg file containing only one Vorbis track at a time (ie. no parallel multiplexing). Many music players (which use libvorbisfile) aren&#8217;t designed to play multitrack Ogg files. In general however, video players, and anything built on a multimedia framework (like GStreamer, DirectShow etc.) will probably be able to handle such files.<br />
&nbsp;<wbr> </p>
<p> If you want to create a file containing some Ogg files sequenced one after another, then you should simply concatenate them together using <code>cat</code>. In Ogg this is called &quot;chaining&quot;. If you cat Ogg Vorbis I audio files together, then the result will also be a compliant Ogg Vorbis file.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-merge</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Miscellaneous options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.<br />
&nbsp;<wbr></p>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Merge pages of audio.oga and video.ogv: </p>
<dl>
<dt>
<dd> <tt>oggz merge -o output.ogv audio.oga video.ogv</tt></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker September 21, 2004;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-rip/">oggz-rip</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-diff/">oggz-diff</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-hogg/">hogg</a></code><code>(1)</code> </p>
<h2>Index</h2>
