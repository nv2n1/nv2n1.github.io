---
title: "ogmsplit(1)"
name: "ogmsplit"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ogmsplit/"
description: "ogmsplit – Split OGG/OGM files into sevaral smaller OGG/OGM files"
---

<h2>NAME</h2>
<p> ogmsplit &#8211; Split OGG/OGM files into sevaral smaller OGG/OGM files</p>
<h2>SYNOPSIS</h2>
<p> <code>ogmsplit</code> [<i>options</i>] <i>inname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ogmsplit</code> can be used to easily split an OGM file after a given size. Several OGM files will be created that each start with a keyframe.</p>
<dl>
<dt>inname</p>
<dd> Use &#8216;<i>inname</i>&#8216; as the source.</p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>out</i></p>
<dd> Use &#8216;<i>out</i>&#8216; as the base name. Ascending part numbers will be appended to it. Default is &#8216;<i>inname</i>&#8216;. Examples:<br />
 1) If <code>-o</code> <i>output.ogg</i> is given on the command line then <code>ogmsplit</code> will create <i>output-000001.ogg</i>, <i>output-000002.ogg</i> and so on.<br />
 2) If no <code>-o</code> option is given and the input&#8217;s name is <i>movie.ogm</i> then <code>ogmsplit</code> will create <i>movie-000001.ogm</i> and so on.</dl>
<p> The operation mode can be set with exactly one of <code>-s</code>, <code>-t,</code> <code>-c</code> or <code>-p</code>. The default mode is to split by size (<code>-s</code>).</p>
<dl>
<dt><code>-s</code>, <code>&#8211;size</code> <i>size</i></p>
<dd> Size in MiB ( = 1024 * 1024 bytes) after which a new file will be opened (approximately). Default is 700MiB. Size can end in &#8216;B&#8217; to indicate &#8216;bytes&#8217; instead of &#8216;MiB&#8217;.</p>
<dt><code>-t</code>, <code>&#8211;time</code> <i>time</i></p>
<dd> Split after the given elapsed time (approximately). &#8216;<i>time</i>&#8216; takes the form <i>HH:MM:SS.sss</i> or simply <i>SS</i>(.<i>sss</i>), e.g. 00:05:00.000 or 300.000 or simply 300.</p>
<dt><code>-c</code>, <code>&#8211;cuts</code> <i>cuts</i></p>
<dd> Produce output files as specified by <i>cuts</i>, a list of slices of the form &quot;<i>start</i>&#8211;<i>end</i>&quot; or &quot;<i>start</i>+<i>length</i>&quot;, separated by commas. If <i>start</i> is omitted, it defaults to the end of the previous cut. <i>start</i> and <i>end</i> take the same format as the arguments to <code>-t</code>.</p>
<dt><code>-n</code>, <code>&#8211;num</code> <i>num</i></p>
<dd> Don&#8217;t create more than <i>num</i> separate files. The last one may be bigger than the desired size. Default is an unlimited number of files. Can only be used with <code>-s</code> or <code>-t</code>.</p>
<dt><code>&#8211;frontend</code></p>
<dd> Frontend mode. Progress output will be terminated by 
 instead of .</p>
<dt><code>-p</code>, <code>&#8211;print-splitpoints</code></p>
<dd> Only print the key frames and the number of bytes encountered before each. Useful to find the exact splitting point.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose and show each OGG packet. Can be used twice to increase verbosity.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>CHAPTER INFORMATION</h2>
<p> <code>ogmsplit</code> correctly handles chapter information. During the first pass the chapter information, if any is present, will be adjusted to match the output files generated. Chapters that are not contained in the current output file are removed entirely. The other chapters are renumbered to start at 1, and their timestamps will be recalculated.<br />
 Example: If your source file contains these four chapters: </p>
<p> CHAPTER01=00:00:00.000<br />
 CHAPTER01NAME=Chapter 01<br />
 CHAPTER02=00:10:00.000<br />
 CHAPTER02NAME=Chapter 02<br />
 CHAPTER03=00:20:00.000<br />
 CHAPTER03NAME=Chapter 03<br />
 CHAPTER04=00:25:00.000<br />
 CHAPTER04NAME=Chapter 04 </p>
<p> and you split after 15 minutes, then the first output file will only contain the first two chapters as shown above, and the second output file will contain the following two chapters and the remaining part of the first: </p>
<p> CHAPTER01=00:00:00.000<br />
 CHAPTER01NAME=Chapter 02 (continued)<br />
 CHAPTER02=00:05:00.000<br />
 CHAPTER02NAME=Chapter 03<br />
 CHAPTER03=00:10:00.000<br />
 CHAPTER03NAME=Chapter 04 </p>
<p> Note that only variable names are changed, not the chapter names themselves. The exception is the first chapter of the second and following files where &quot;(continued)&quot; is appended in order to indicate that this is not the start of this chapter. If you want to change them as well you&#8217;ll have to remerge the resulting file with a new chapter file.</p>
<h2>AUTHOR</h2>
<p> <i>ogmsplit</i> was written by Moritz Bunkus &lt;moritz [at] bunkus.org&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogmmerge/">ogmmerge</a></code>(1), <code><a href="/docs/linux/man/1-ogminfo/">ogminfo</a></code>(1), <code><a href="/docs/linux/man/1-ogmdemux/">ogmdemux</a></code>(1), <code><a href="/docs/linux/man/1-ogmcat/">ogmcat</a></code>(1), <code><a href="/docs/linux/man/1-dvdxchap/">dvdxchap</a></code>(1)</p>
<h2>WWW</h2>
<p> The newest version can always be found at &lt;<a rel="nofollow" href="http://www.bunkus.org/videotools/ogmtools/">http://www.bunkus.org/videotools/ogmtools/</a>&gt; </p>
<h2>Index</h2>
