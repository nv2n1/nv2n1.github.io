---
title: "aviindex(1)"
name: "aviindex"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aviindex/"
description: "aviindex – Write and read text files describing the index of an AVI file"
---

<h2>NAME</h2>
<p> aviindex &#8211; Write and read text files describing the index of an AVI file</p>
<h2>SYNOPSIS</h2>
<p> <code>aviindex</code> [ <code>-o</code> <i>ofile</i> <code>-i</code> <i>ifile</i> <code>-f</code> <code>-n</code> <code>-x</code> <code>-v</code> <code>-h</code> ]</p>
<h2>COPYRIGHT</h2>
<p> <code>aviindex</code> is Copyright (C) 2003,2004 by Tilmann Bitterberg</p>
<h2>DESCRIPTION</h2>
<p> <code>aviindex</code> writes a text file describing the index of an AVI file. It analyses the content or index if available of the AVI file and prints this information in a human readable form. </p>
<p> An AVI file can have an optional chunk called &quot;idx1&quot; which contains information about keyframes (syncpoints) and locations of video frames resp. audio chunks. Though larger AVI files (&gt;2-4GB), so-called OpenDML AVI or also AVI 2 files, have a more complicated indexing system, which consists of a superindex referring to (possibly) several &quot;standard&quot; indexes, the &quot;indexing principle&quot; is the same. Movie players use such indexes to seek in files. </p>
<p> <code>aviindex</code> reads the AVI file <i>ifile</i> and writes the index into <i>ofile</i>. This can either happen in &quot;dumb&quot; mode where <code>aviindex</code> looks for an existing index (and trusts this index!) in the file and dumps this index into a human readable form. The &quot;dumb&quot; mode is used, when <i>-n</i> is NOT specified or when the filesize of the input file is smaller than 2 GB. </p>
<p> In &quot;smart&quot; mode, <code>aviindex</code> scans through the complete AVI file and searches for chunks (may that video or audio) and reconstructs the index based on the information found. If an index chunk is found accidently, <code>aviindex</code> will use the information in this index to recover the keyframe information, which is important. <code>aviindex</code> will use smart mode, if given the <i>-n</i> option OR if the AVI file is larger than 2 GB. If the file is large, the index chunk cannot be found the usual way so one must use <i>-n</i> but it is possible that there is an index chunk in this file. Cross fingers. </p>
<p> Also in smart mode, <code>aviindex</code> analyzes the content of the video frame and tries to detect keyframes by looking at the data depending on the video codec. </p>
<p> The generated index file serves different purposes.</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The library which handles AVI files in <a href="/docs/linux/man/1-transcode/">transcode</a>(1) can read such index files and use this file to rebuild the index instead of scanning through the whole AVI file over and over again. Reading the index from the index file is <code>much</code> faster than scanning through the AVI.</p>
<dt>*</p>
<dd> It can be used as a seeking file. When given to transcode via the &#8211;nav_seek switch, transcode will use the file to seek directly to the position you specified via -c. This also works for multiple -c ranges.</p>
<dt>*</p>
<dd> Its nice to have for debugging.</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> <i>ofile</i></p>
<dd> Specify the name of the output file.</p>
<dt><code>-i</code> <i>ifile</i></p>
<dd> Specify the name of the input file.</p>
<dt><code>-f</code></p>
<dd> force the use of the existing index.</p>
<dt><code>-n</code></p>
<dd> force generating the index by scanning the file.</p>
<dt><code>-x</code></p>
<dd> (implies -n) don&#8217;t use any existing index to generate keyframes.</p>
<dt><code>-v</code></p>
<dd> show version.</p>
<dt><code>-h</code></p>
<dd> show help text.</dl>
<h2>MPLAYER</h2>
<p> <code>aviindex</code> can convert from and to mplayer-generated index files. Since mplayer-1.0pre3 mplayer has the ability to save the index via <i>-saveidx</i> FILE and load it again through <i>-loadidx</i> FILE. <code>aviindex</code> is able to convert an mplayer index file to a transcode index file and vice visa. It is not able to directly write an mplayer file, though. Example of a toolchain </p>
<pre>
  mplayer -frames 0 -saveidx mpidx broken.avi
  aviindex -i mpidx -o tcindex
  avimerge -x tcindex -i broken.avi -o fixed.avi
</pre>
<p> Or the other way round </p>
<pre>
  aviindex -i broken.avi -n -o broken.idx
  aviindex -i broken.idx -o mpidx
  mplayer -loadidx mpidx broken.avi
</pre>
<p> The major differences between the two index file formats is that the mplayer one is a binary format which is an exact copy of an index in the AVI file. <code>aviindex</code> &#8216;s format is text based. See <code>FORMAT</code> for details.</p>
<h2>EXAMPLES</h2>
<p> The command </p>
<pre>
  aviindex -i 3GBfile.avi -o 3GB.index
</pre>
<p> generates and index of the large file 3GBfile.avi. You can use the file 3GB.index to tell transcode to read the index from this file and not from the avi. This leads to much faster startup time. </p>
<p> Suppose 3GBfile.avi has DivX video and PCM sound and you want to encode several ranges. </p>
<pre>
transcode -V -i 3GBfile.avi --nav_seek 3GB.index \
	-x xvid,avi \
	-c 5000-6000,0:20:00-0:21:00,100000-100001 \
	-y xvid --lame_preset standard -o out.avi
</pre>
<h2>FORMAT</h2>
<p> The format of the index file. The first 7 bytes in this file are &quot;AVIIDX1&quot; for easy detection and a comment of who created the file. The second line is a comment and describes the fields. Do not delete it. Each line (except the first 2) consists of exactly 8 fields all seperated by one space and describing one particular chunk of the AVI file.<br />
 Here is an example of an AVI file with two audio tracks.</p>
<dl>
<dt>
<dd>
<pre>
AVIIDX1 # Generated by aviindex (transcode-0.6.8)
TAG TYPE CHUNK CHUNK/TYPE POS LEN KEY MS
00db 1 0 0 2048 8335 1 0.00
01wb 2 1 0 10392 847 1 0.00
01wb 2 2 1 11248 847 1 0.00
02wb 3 3 0 12104 847 1 0.00
02wb 3 4 1 12960 847 1 0.00
00db 1 5 1 13816 5263 0 0.00
00db 1 6 2 19088 3435 0 0.00
01wb 2 7 2 22532 834 1 0.00
</pre>
</dl>
<p> The field <i>TAG</i> is the chunk descriptor. Its &quot;00d*&quot; for the video, &quot;01wb&quot; for the first audio track, &quot;02wb&quot; for the second audio track and so on. </p>
<p> The field <i>TYPE</i> is the type of the chunk. This is redundant because the type is also embedded into the TAG field but its a convenient thing to have. Its 1 for video, 2 for first audio track and 3 for second audio track. </p>
<p> The field <i>CHUNK</i> is the absolute chunk number in the AVI file. If you read the CHUNK field in the last line of the index file, you know how many chunks this AVI file has. </p>
<p> The field <i>CHUNK/TYPE</i> holds information about how many chunks of this type were previously found in the AVI file. </p>
<p> The field <i>POS</i> is the absolute byte position in the AVI file where this chunk can be found. Note this field can hold really large numbers if you are dealing with large AVIs. </p>
<p> The field <i>LEN</i> is the length of this chunk. </p>
<p> The field <i>KEY</i> holds information if this chunk is a keyframe. In the example above, all audio chunks are key-chunks, but only the first video frame is a key frame. This field is either 0 or 1. </p>
<p> The field <i>MS</i> holds information about how many milliseconds have passed. This field may be 0.00 if unknown.</p>
<h2>AUTHORS</h2>
<p> <code>aviindex</code> was written by Tilmann Bitterberg &lt;transcode at tibit.org&gt;<br />
 and is part of transcode.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1), <code><a href="/docs/linux/man/1-mplayer/">mplayer</a></code>(1) </p>
<h2>Index</h2>
