---
title: "tcprobe(1)"
name: "tcprobe"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcprobe/"
description: "tcprobe – probe multimedia streams from medium and print information on the standard output"
---

<h2>NAME</h2>
<p> tcprobe &#8211; probe multimedia streams from medium and print information on the standard output</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcprobe</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-B</code> ] [ <code>-M</code> ] [ <code>-T</code> <i>title</i> ] [ <code>-b</code> <i>bitrate</i> ] [ <code>-H</code> <i>n</i> ] [ <code>-f</code> <i>seekfile</i> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tcprobe</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tcprobe</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tcprobe</code> reads source (from stdin if not explicitely defined) and prints on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed.<br />
 You can specify a file, directory, device, mountpoint or host address as input source. <code>tcprobe</code> usually handles the different types correctly.</p>
<dt><code>-B</code></p>
<dd> Binary output to stdout for use in transcode.</p>
<dt><code>-M</code></p>
<dd> Use EXPERIMENTAL mplayer probe, useful for streams that tcprobe doesn&#8217;t recognize elsewhere. With this option enabled, tcprobe merely acts as a frontend for mplayer; of course mplayer binary needs to be installed and avalaible somewhere in PATH.</p>
<dt><code>-T </code><i>title</i></p>
<dd> Probe for DVD <i>title</i></p>
<dt><code>-H</code> <i>n</i></p>
<dd> This option tells <code>tcprobe</code> to scan <i>n</i> MB of input data. Default is to scan 1 MB. To detect all subtitles and audio tracks (if available) it is highly recommended that this <i>n</i> should be at least increased to 10 or even higher. Very often only some audio tracks start during the first MB of a VOB or DVD file so transcode cannot detect them if not called with a higher value. Please note that <a href="/docs/linux/man/1-transcode/">transcode</a>(1) has a similar -H option as well which has the same meaning.</p>
<dt><code>-s</code> <i>n</i></p>
<dd> Skip the first <i>n</i> bytes of the input stream. Default is to skip no bytes.</p>
<dt><code>-b</code> <i>bitrate</i></p>
<dd> Set audio encoder bitrate to <i>bitrate</i></p>
<dt><code>-f </code><i>seekfile</i></p>
<dd> Read index/seek information from <i>seekfile</i>. This is especially useful for AVI files when it takes a long time to probe when there is no index in the AVI available. Also see <a href="/docs/linux/man/1-aviindex/">aviindex</a>(1).</p>
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
<p> <code>tcprobe</code> is a front end for probing various source types and is used in <code>transcode</code>&#8216;s import modules.</p>
<h2>EXAMPLES</h2>
<p> The command <code>tcprobe -i foo.avi</code> will print interesting information about the AVI file itself and its video and audio content. </p>
<h2>AUTHORS</h2>
<p> <code>tcprobe</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aviindex/">aviindex</a></code>(1), <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
