---
title: "tcscan(1)"
name: "tcscan"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcscan/"
description: "tcscan – scan multimedia streams from medium and print information on the standard output"
---

<h2>NAME</h2>
<p> tcscan &#8211; scan multimedia streams from medium and print information on the standard output</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcscan</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-x</code> <i>codec</i> ] [ <code>-e</code> <i>r[,b[,c]]</i> ] [ <code>-b</code> <i>bitrate</i> ] [ <code>-w</code> <i>num</i> ] [ <code>-f</code> <i>rate</i> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tcscan</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tcscan</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tcscan</code> reads source (from stdin if not explicitely defined) and prints on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed.<br />
 You can specify a file, directory, device, mountpoint or host address as input source. <code>tcscan</code> usually handles the different types correctly.</p>
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
<dd> Print version information and exit.</dl>
<h2>NOTES</h2>
<p> <code>tcscan</code> is a front end for scaning various source types and is used in <code>transcode</code>&#8216;s import modules. <code>tcscan</code> does a complete scan of the source to gather information.</p>
<h2>EXAMPLES</h2>
<p> The command <code>tcscan -i foo.avi</code> prints header information about the AVI-file itself and lists details on the video and audio content, e.g., keyframes, chunk structure. </p>
<p> The command <code>cat audio.pcm | tcscan -x pcm -e 48000,16,2</code> simply determines the playtime lenghth of the raw audio stream. </p>
<p> The command <code>tcscan -x mp3 -i input.mp3</code> will print the number of chunks in the MP3 file and the average bitrate. </p>
<h2>AUTHORS</h2>
<p> <code>tcscan</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
