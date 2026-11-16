---
title: "ogmdemux(1)"
name: "ogmdemux"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogmdemux/"
description: "ogmdemux – Extract streams from OGG/OGM files into separate files"
---

<h2>NAME</h2>
<p> ogmdemux &#8211; Extract streams from OGG/OGM files into separate files</p>
<h2>SYNOPSIS</h2>
<p> <code>ogmdemux</code> [<i>options</i>] <i>inname</i></p>
<h2>DESCRIPTION</h2>
<p> This program extracts all or only some streams from an OGM and writes them to separate files.</p>
<dl>
<dt><i>inname</i></dt>
<dd> Use &#8216;<i>inname</i>&#8216; as the source.</dd>
<dt><code>-o</code>, <code>&#8211;output</code> <i>out</i></dt>
<dd> Use &#8216;<i>out</i>&#8216; as the base for destination file names. &#8216;-v1&#8217;, &#8216;-v2&#8217;, &#8216;-a1&#8217;, &#8216;-t1&#8217;&#8230; will be appended to this name. Default: use &#8216;<i>inname</i>&#8216;.</dd>
<dt><code>-a</code>, <code>&#8211;astream</code> <i>n</i></dt>
<dd> Extract specified audio stream. Can be used more than once. Default: extract all streams.</dd>
<dt><code>-d</code>, <code>&#8211;vstream</code> <i>n</i></dt>
<dd> Extract specified video stream. Can be used more than once. Default: extract all streams.</dd>
<dt><code>-t</code>, <code>&#8211;tstream</code> <i>n</i></dt>
<dd> Extract specified text stream. Can be used more than once. Default: extract all streams.</dd>
<dt><code>-na</code>, <code>&#8211;noaudio</code></dt>
<dd> Don&#8217;t extract any audio streams.</dd>
<dt><code>-nv</code>, <code>&#8211;novideo</code></dt>
<dd> Don&#8217;t extract any video streams.</dd>
<dt><code>-nt</code>, <code>&#8211;notext</code></dt>
<dd> Don&#8217;t extract any text streams. Default: extract all streams.</dd>
<dt><code>-r</code>, <code>&#8211;raw</code></dt>
<dd> Extract the raw streams only. Default: extract to useful formats (AVI, WAV, OGG, SRT&#8230;).</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Increase verbosity.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show this help.</dd>
<dt><code>-V</code>,<code> &#8211;version</code></dt>
<dd> Show version number.</dd></dl>
<h2>NOTES</h2>
<p> What works:</p>
<dl>
<dt>*</dt>
<dd> Extraction of the following formats is fully supported including writing the stream contents to useful container formats: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>video&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>AVI </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Vorbis -&gt;&nbsp;<wbr>OGG/Vorbis </p>
<p>&nbsp;<wbr>&nbsp;<wbr>PCM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>WAV </p>
<p>&nbsp;<wbr>&nbsp;<wbr>text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>text files&nbsp;<wbr>(SRT subtitle format)</p>
<dt>*</dt>
<dd> All other audio streams (MP3, AC3) are just copied 1:1 into output files. MP3 and AC3 files should be usable. Others might not.</dd></dl>
<p> What not works:</p>
<dl>
<dt>*</dt>
<dd> Headers created by older OggDS (DirectShow) filter versions are not supported (and probably never will be).</dd></dl>
<h2>AUTHOR</h2>
<p> <i>ogmdemux</i> was written by Moritz Bunkus &lt;moritz [at] bunkus.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogmmerge/">ogmmerge</a></code>(1), <code><a href="/docs/linux/man/1-ogmsplit/">ogmsplit</a></code>(1), <code><a href="/docs/linux/man/1-ogminfo/">ogminfo</a></code>(1), <code><a href="/docs/linux/man/1-ogmcat/">ogmcat</a></code>(1), <code><a href="/docs/linux/man/1-dvdxchap/">dvdxchap</a></code>(1)</p>
<h2>WWW</h2>
<p> The newest version can always be found at &lt;<a rel="nofollow" href="http://www.bunkus.org/videotools/ogmtools/">http://www.bunkus.org/videotools/ogmtools/</a>&gt; </p>
<h2>Index</h2>
