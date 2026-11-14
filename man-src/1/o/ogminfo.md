---
title: "ogminfo(1)"
name: "ogminfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogminfo/"
description: "ogminfo – Print information about streams in OGG/OGM files"
---

<h2>NAME</h2>
<p> ogminfo &#8211; Print information about streams in OGG/OGM files</p>
<h2>SYNOPSIS</h2>
<p> <code>ogminfo</code> [<i>options</i>] <i>inname</i></p>
<h2>DESCRIPTION</h2>
<p> This program lists all streams contained in an OGM including information about the codecs used.</p>
<dl>
<dt>inname</p>
<dd> Use &#8216;<i>inname</i>&#8216; as the source.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose and show each OGG packet. See the section &#8216;<code>VERBOSITY LEVELS</code>&#8216; for details.</p>
<dt><code>-s</code>, <code>&#8211;summary</code></p>
<dd> Will print a short summary for each stream including the total size in bytes, the bitrate, the number of packets/frames and the length in seconds. This requires the parsing of the complete file.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show usage information.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>VERBOSITY LEVELS</h2>
<p> The <code>-v</code> option can be used to increase <code>ogminfo</code>&#8216;s verbosity level and print more information about the current file.</p>
<dl>
<dt>level 0</p>
<dd> will print only the streams it finds and their types.</p>
<dt>level 1</p>
<dd> will also print each stream&#8217;s header and comment packets&#8217; contents. These two modes will not process the whole file (as opposed to all other modes) if the comment packets are placed correctly.</p>
<dt>level 2</p>
<dd> will print a line for each OGG packet it encounters containing the stream the packet belongs to, the payload size, the packet&#8217;s granulepos, the packet&#8217;s number, its start time, its end time and several flags. The flags may include &#8216;sync_ok&#8217; or &#8216;OUT_OF_SYNC&#8217; which indicates whether the packet&#8217;s placement in the file is correct according to its granulepos. Other flags are &#8216;IS_SYNCPOINT&#8217; or &#8216;EOS&#8217;.<br />
 level 2 and above automatically imply <code>&#8211;summary</code>.</p>
<dt>level 3</p>
<dd> also prints a line whenever a new OGG page was read completely along with the page&#8217;s exact position in the file it was read from.</p>
<dt>level 4</p>
<dd> will dump the complete stream_header structure found in the header packet for any non-Vorbis stream.</dl>
<p> The levels 3 and 4 are intended for debugging purposes only. </p>
<h2>NOTES</h2>
<p> What works:</p>
<dl>
<dt>*</p>
<dd> OGM with Vorbis audio, &#8216;normal&#8217; video (like DivX etc.), audio streams (PCM, MP3 etc.), text streams (subtitles).</dl>
<p> What not works:</p>
<dl>
<dt>*</p>
<dd> Headers created by older OggDS (DirectShow) filter versions are not supported (and probably never will be).</dl>
<h2>AUTHOR</h2>
<p> <i>ogminfo</i> was written by Moritz Bunkus &lt;moritz [at] bunkus.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogmmerge/">ogmmerge</a></code>(1), <code><a href="/docs/linux/man/1-ogmsplit/">ogmsplit</a></code>(1), <code><a href="/docs/linux/man/1-ogmdemux/">ogmdemux</a></code>(1), <code><a href="/docs/linux/man/1-ogmcat/">ogmcat</a></code>(1), <code><a href="/docs/linux/man/1-dvdxchap/">dvdxchap</a></code>(1)</p>
<h2>WWW</h2>
<p> The newest version can always be found at &lt;<a rel="nofollow" href="http://www.bunkus.org/videotools/ogmtools/">http://www.bunkus.org/videotools/ogmtools/</a>&gt; </p>
<h2>Index</h2>
