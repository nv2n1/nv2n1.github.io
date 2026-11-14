---
title: "avimerge(1)"
name: "avimerge"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avimerge/"
description: "avimerge – merge several AVI-files into one"
---

<h2>NAME</h2>
<p> avimerge &#8211; merge several AVI-files into one</p>
<h2>SYNOPSIS</h2>
<p> <code>avimerge</code> <code>-o</code> <i>name</i> <code>-i</code> <i>file1</i><code> [ </code><i>file2</i><code> [ </code><i>&#8230;</i><code> ] ] </code> [ <code>-p</code> <i>file</i> ] [ <code>-a</code> <i>num</i> ] [ <code>-A</code> <i>num</i> ] [ <code>-b</code> <i>num</i> ] [ <code>-c</code> ] [ <code>-f</code> <i>commentfile</i> ] [ <code>-x</code> <i>indexfile</i> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>avimerge</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>avimerge</code> is a versatile tool. It can contatenate several AVI files into one. It can also be used to fix an index of a broken file and can also replace audio tracks or muxes new ones. It can read raw AC3 and MP3 files for multplexing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o </code><i>name</i></p>
<dd> Specify the name of the output file.</p>
<dt><code>-i </code><i>file</i></p>
<dd> Specify the name(s) of the input file(s) to merge into the output file.</p>
<dt><code>-p </code><i>file</i></p>
<dd> Specify the name of the audio file to multiplex into the output file. The type of file can be either another AVI file or an MP3 or AC3 file.</p>
<dt><code>-b </code><i>num</i></p>
<dd> Specify if avimerge should write an VBR mp3 header into the AVI file. Default is dependent on the input file (and usually correct). <i>num</i> is either 1 or 0.</p>
<dt><code>-c</code></p>
<dd> Drop video frames in case audio is missing [off]<br />
 Only when merging multiple AVI files. Some AVI files run a little bit (usually for one or two video frames) short on audio. This means avimerge cannot keep up sync when concatinating them. The files play fine when played individually but not when merged because audio from the new file gets played back with video from the old file. <code>avimerge</code> will print a message like </p>
<pre>
  No audiodata left for track 0-&gt;0 (59950.25=59950.25) continuing ..
</pre>
<p> When you turn on the -c option, the video which is too much will be dropped.</p>
<dt><code>-f </code><i>commentfile</i></p>
<dd> Read AVI tombstone data for header comments from <i>commentfile</i>. See /docs/avi_comments.txt for a sample.</p>
<dt><code>-x </code><i>indexfile</i></p>
<dd> Read the AVI index from <i>indexfile.</i> See <a href="/docs/linux/man/1-aviindex/">aviindex</a>(1) for information on how to create such a file.</p>
<dt><code>-a </code><i>num</i></p>
<dd> Specify the number of the audio track you want to use from the <i>input</i> file.</p>
<dt><code>-A </code><i>num</i></p>
<dd> Specify the number of the audio track you want to use in the <i>output</i> file. If you specify an existing track number, the track will be replaced. If omitted, the next free slot will be used.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<pre>
<code>avimerge -o big.avi -i my_file1.avi my_file2.avi my_file3.avi</code>
</pre>
<p> merges the three input files <i>my_file[123].avi</i> into one big AVI-file <i>big.avi</i>. </p>
<pre>
<code>avimerge -o out.avi -i in.avi -p audio2.avi -a 1</code>
</pre>
<p> merges track number 1 form in.avi to the next free track number in out.avi. You can create audio-only AVI-files using </p>
<pre>
<code>transcode -i song.mp3 -x null,mp3 -g 0x0 -y raw -a 1 -o audio2.avi -u 50</code>
</pre>
<p> The command </p>
<pre>
<code>avimerge -o out.avi -i in.avi -p sound.mp3</code>
</pre>
<p> merges the file sound.mp3 as an additional audio track into out.avi. </p>
<h2>AUTHORS</h2>
<p> <code>avimerge</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aviindex/">aviindex</a></code>(1), <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
