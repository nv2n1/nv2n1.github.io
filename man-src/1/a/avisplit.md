---
title: "avisplit(1)"
name: "avisplit"
section: "1"
letter: "a"
url: "/docs/linux/man/1-avisplit/"
description: "avisplit – split AVI-files into chunks of a maximum size"
---

<h2>NAME</h2>
<p> avisplit &#8211; split AVI-files into chunks of a maximum size</p>
<h2>SYNOPSIS</h2>
<p> <code>avisplit</code> [ <code>-i</code> <i>file</i> <code>-o</code> <i>base</i> [ <code>-s</code> <i>size</i> ] [ <code>-H</code> <i>num</i> ] [ <code>-t</code> <i>s1-s2[,s3-s4,..]</i> <code>-c</code> <code>-m</code> <code>-b</code> <i>num</i> <code>-f</code> <i>commentfile</i> ] ] [ <code>-v</code> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>avisplit</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>avisplit</code> splits a single AVI-file into chunks of size <i>size</i>.<br />
 Each of the created chunks will be an independent file, i.e. it can be played without needing any other of the chunk.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> <i>file</i></p>
<dd> Specify the filename of the file to split into chunks.</p>
<dt><code>-o</code> <i>base</i></p>
<dd> Specify the base of the output filename(s) <code>avisplit</code> will then split to <code>base-%04d.avi</code></p>
<dt><code>-s</code> <i>size</i></p>
<dd> Use this option to specify the maximum size (in units of MB) of the chunks <code>avisplit</code> should create. <i>0</i> means dechunk, create as many files as possible.</p>
<dt><code>-H</code> <i>num</i></p>
<dd> Create only the first <i>num</i> chunks then exit.</p>
<dt><code>-t</code> <i>s1-s2[,s3-s4,..]</i></p>
<dd> Split the input file based on time/framecode (hh:mm:ss.ms)</p>
<dt><code>-c</code></p>
<dd> Together with <code>-t</code>. Merge all segments into one AVI-File again instead generating seperate files.</p>
<dt><code>-m</code></p>
<dd> Together with <code>-t</code>. Force split at upper bondary instead of lower border.</p>
<dt><code>-b</code> <i>num</i></p>
<dd> Specify if avisplit should write an VBR mp3 header into the AVI file. Default is 1 because it does not hurt. <i>num</i> is either 1 or 0.</p>
<dt><code>-f</code> <i>commentfile</i></p>
<dd> Read AVI tombstone data for header comments from <i>commentfile</i>. See /docs/avi_comments.txt for a sample.</p>
<dt><code>-v</code></p>
<dd> Print only version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>avisplit -s 700 -i my_file.avi</code> </p>
<p> will split the file <i>my_file.avi</i> into chunks which&#8217;s maximum size will not exceed 700 MB, i.e. they will fit onto a CD, each. The created chunks will be named my_file.avi-0000, my_file.avi-0001, etc. </p>
<p> <code>avisplit -i my_file.avi -c -o out.avi -t 00:10:00-00:11:00,00:13:00-00:14:00</code> </p>
<p> will grab Minutes 10 to 11 and 13 to 14 from my_file.avi and merge it into out.avi</p>
<h2>BAD SYNCH</h2>
<p> When you split a file with <code>avisplit</code> and the A/V sync for the first file is OK but the sync on all successive files is bad then have a look at the output of <a href="/docs/linux/man/1-tcprobe/">tcprobe</a>(1) (shortend). </p>
<p>&nbsp;<wbr>| V: 25.000 fps, codec=dvsd, frames=250, width=720, height=576 </p>
<p>&nbsp;<wbr>| A: 48000 Hz, format=0x01, bits=16, channels=2, bitrate=1536 kbps, </p>
<p>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>10</i>&nbsp;<wbr>chunks, 1920000 bytes </p>
<p> You&#8217;ll see the AVI file has only 10 Audio chunks but 250 video chunks. That means one audio chunk spans several video frames. avisplit can not cut a chunk in half, it only handles complete chunks. If you do, say, avisplit -s 20, it is possible that the first file will have 6 audio chunks and the second one only 4 meaning there is too much audio in the first AVI file. </p>
<p> The solution is to remux the AVI file with</p>
<dl>
<dt>
<dd> <code>transcode -i in.avi -P1 -N 0x1 -y raw -o out.avi</code></dl>
<p> (of course -N 0x1 is not correct for all AVI files). Now look at tcprobe again </p>
<p>&nbsp;<wbr>| V: 25.000 fps, codec=dvsd, frames=250, width=720, height=576 </p>
<p>&nbsp;<wbr>| A: 48000 Hz, format=0x01, bits=16, channels=2, bitrate=1536 kbps, </p>
<p>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>250</i>&nbsp;<wbr>chunks, 1920000 bytes </p>
<p> The data in this file is <i>exactly</i> the same (its bit-identical) as it was in in.avi; the AVI file was just written in a different way, we do now have 250 audio chunks which makes splitting much easier and more accurate for avisplit.</p>
<h2>AUTHORS</h2>
<p> <code>avisplit</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aviindex/">aviindex</a></code>(1), <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
