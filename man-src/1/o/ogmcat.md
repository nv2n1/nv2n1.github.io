---
title: "ogmcat(1)"
name: "ogmcat"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogmcat/"
description: "ogmcat – Concatenate several OGG/OGM files into one big OGG/OGM file"
---

<h2>NAME</h2>
<p> ogmcat &#8211; Concatenate several OGG/OGM files into one big OGG/OGM file</p>
<h2>SYNOPSIS</h2>
<p> <code>ogmcat</code> [<i>options</i>] -o <i>outname</i> <i>inname1</i> [<i>inname2</i> [<i>inname3</i> &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>ogmcat does NOT work at the moment. It is work in progress. I included it just out of laziness (otherwise I&#8217;d have to remove it from the Makefile/configure stuff prior to releasing this version).</code> </p>
<p> <code>ogmcat</code> can be used to concatenate several OGG/OGM files into one big file if they are of the same type. For a more in-depth description refer to the <code>LIMITATIONS</code> section.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code> <i>outname</i></p>
<dd> Output to &#8216;<i>outname</i>&#8216;.</p>
<dt>inname1</p>
<dd> Use &#8216;<i>inname1</i>&#8216;, &#8216;<i>inname2</i>&#8216; etc as the sources.</p>
<dt><code>-m</code>, <code>&#8211;manualsync</code> <i>n</i></p>
<dd> Specifies a manual sync value in ms that will be added to each stream&#8217;s presentation timestamps along with the value calculated by the chosen sync algorithm (see the <code>-s</code> option). This option can be used for each input file although it has no effect if used for the first one as well.</p>
<dt><code>-s</code>, <code>&#8211;sync</code> <i>nr</i></p>
<dd> Uses sync mode <i>nr</i>. Valid values are 0 &#8211; 4. The default value is shown on <code>ogmcat</code>&#8216;s help screen.</p>
<dt><code>-n</code>, <code>&#8211;nosafetychecks</code></p>
<dd> Disable the safety checks made prior to the concatenating. The resulting file may be unplayable. See the <code>LIMITATIONS</code> section for further details.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose and show each OGG packet. Can be used twice to increase verbosity.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>LIMITATIONS</h2>
<p> Concatenating streams is difficult at the best and might even be impossible. Therefore <code>ogmcat</code> makes very strict comparisons between the streams contained in the input files. The checks done include:</p>
<dl>
<dt>*</p>
<dd> general: All streams with the same serial number must be of the same type (video, audio, Vorbis audio or text streams).</p>
<dt>*</p>
<dd> general: If a stream exists in one file it <code>must</code> in the other files as well.</p>
<dt>*</p>
<dd> video streams: The codec FourCC, width, height and FPS must match.</p>
<dt>*</p>
<dd> Vorbis streams: The sample rate and the number of channels must match.</p>
<dt>*</p>
<dd> other audio streams: The codec ID, sample rate, bits per sample and number of channels must match.</p>
<dt>*</p>
<dd> text/subtitle streams: The &#8216;time unit&#8217; must match.</dl>
<p> The user can forcefully override the last four checks with the <code>-n</code> parameter. The checks marked as &#8216;general&#8217; cannot be overridden this way. </p>
<p> Audio/video synchronization might not be ok in the resulting file even if the source files were perfectly in sync. The user can experiment with the <code>-s</code> parameter which causes <code>ogmcat</code> to use slightly different algorithms for calculating the granulepos values for the audio and text streams. The range of valid parameters will be printed on <code>ogmcat</code>&#8216;s help screen. </p>
<p> If none of the synchronization algorithms provided works correctly then the user can also manually add a synchronization offset using the <code>-m</code> option for each input file.</p>
<h2>AUTHOR</h2>
<p> <i>ogmcat</i> was written by Moritz Bunkus &lt;moritz [at] bunkus.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogmmerge/">ogmmerge</a></code>(1), <code><a href="/docs/linux/man/1-ogminfo/">ogminfo</a></code>(1), <code><a href="/docs/linux/man/1-ogmdemux/">ogmdemux</a></code>(1), <code><a href="/docs/linux/man/1-ogmsplit/">ogmsplit</a></code>(1), <code><a href="/docs/linux/man/1-dvdxchap/">dvdxchap</a></code>(1)</p>
<h2>WWW</h2>
<p> The newest version can always be found at &lt;<a rel="nofollow" href="http://www.bunkus.org/videotools/ogmtools/">http://www.bunkus.org/videotools/ogmtools/</a>&gt; </p>
<h2>Index</h2>
