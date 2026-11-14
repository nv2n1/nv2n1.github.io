---
title: "tcextract(1)"
name: "tcextract"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcextract/"
description: "tcextract – read multimedia file from medium, extract or demultiplex requested stream and print to standard output"
---

<h2>NAME</h2>
<p> tcextract &#8211; read multimedia file from medium, extract or demultiplex requested stream and print to standard output</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcextract</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-x</code> <i>codec</i> ] [ <code>-t</code> <i>magic</i> ] [ <code>-a</code> <i>track</i> ] [ <code>-C</code> <i>s-e</i> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tcextract</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tcextract</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tcextract</code> reads source (from stdin if not explicitely defined) and prints on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed. <code>tcextract</code> reads streams from file or from stdin. </p>
<dt><code>-C </code><i>s-e</i></p>
<dd> extract and print out only this frame interval (video) or bytes (audio) [all]. This option is only supported if the source contains proper information to perform a selective extraction. </p>
<dt><code>-t </code><i>magic</i></p>
<dd> source file magic. This option is used to identify the source file format if reading is performed from stdin or <i>tcextract</i> fails to identify the source file format. Supported formats are labeled with <i>magic</i>: </p>
<p> avi<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>RIFF AVI-file</p>
<p> vob<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG program streams</p>
<p> m2v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG elementary video stream</p>
<p> vdr<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG digital video recording</p>
<p> raw<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>raw bitstream</p>
<p> wav<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>RIFF WAVE audio</p>
<p> yuv4mpeg<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mjpeg-tools stream header format</p>
<dt><code>-x </code><i>codec</i></p>
<dd> source pdeudo-codec, if not detected when reading from stdin. Currently, supported parameter for <i>codec</i> are </p>
<p> mp3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG audio</p>
<p> ac3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>AC3 audio</p>
<p> a52<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>A52 audio</p>
<p> dv<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Digital Video DV</p>
<p> mpeg2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG video</p>
<p> yv12<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Y&#8217;CbCr YUV</p>
<p> rgb<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>RGB 24-bit</p>
<p> ps1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>MPEG private stream (subtitles)</p>
<p> pcm<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>raw audio stream</p>
<dt><code>-a </code><i>track</i></p>
<dd> extract selected audio or video track from source. </p>
<dt><code>-d</code> <i>level</i></p>
<dd> With this option you can specify a bitmask to enable different levels of verbosity (if supported). You can combine several levels by adding the corresponding values: </p>
<p> QUIET 0 </p>
<p> INFO 1 </p>
<p> DEBUG 2 </p>
<p> STATS 4 </p>
<p> WATCH 8 </p>
<p> FLIST 16 </p>
<p> VIDCORE 32 </p>
<p> SYNC 64 </p>
<p> COUNTER 128 </p>
<p> PRIVATE 256</p>
<dt><code>-v</code></p>
<dd> Print version information and exit. </p>
</dl>
<h2>NOTES</h2>
<p> <code>tcextract</code> is a front end for extracting various raw or encoded audio/video tracks from a source and is used in <code>transcode</code>&#8216;s import pipeline. </p>
<h2>EXAMPLES</h2>
<p> The command <code>tcextract -i foo.avi -x mp3 -a 3</code> extracts MPEG audio track 3 from the AVI-file foo.avi and prints the bitstream to stdout. </p>
<h2>AUTHORS</h2>
<p> <code>tcextract</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
