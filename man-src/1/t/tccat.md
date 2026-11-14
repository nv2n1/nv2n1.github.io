---
title: "tccat(1)"
name: "tccat"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tccat/"
description: "tccat – concatenate multimedia streams from medium and print on the standard output"
---

<h2>NAME</h2>
<p> tccat &#8211; concatenate multimedia streams from medium and print on the standard output</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tccat</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-t</code> <i>magic</i> ] [ <code>-T</code> <i>title[,chapter[,angle]]</i> ] [ <code>-L</code> ] [ <code>-S</code> <i>n</i> ] [ <code>-P</code> ] [ <code>-a</code> ] [ <code>-d</code> <i>mode</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tccat</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tccat</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tccat</code> reads source (from stdin if not explicitely defined) and prints on the standard output. Directory contents is concatenated, if source files have the same format. Multiple AVI-files are also supported.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed.<br />
 You can specify a file, directory, device, mountpoint or host address as input source. <code>tccat</code> usually handles the different types correctly.</p>
<dt><code>-t</code> <i>magic</i></p>
<dd> Tell <code>tccat</code> about the type of input. Currently only <code>dvd</code> is supported &#8211; any other parameter will be ignored.</p>
<dt><code>-T </code><i>title</i>[<code>,</code><i>chapter</i>[<code>,</code><i>angle</i>]]</p>
<dd> Select DVD <i>title</i> and extract only a single <i>chapter</i> with selected viewing <i>angle</i>. Setting the argument <i>chapter</i> to <code>-1</code> means to process all available chapters on the DVD.<br />
 If this option is given, the input type of <code>dvd</code> will also be assumed (see option <code>-t</code>).</p>
<dt><code>-L</code></p>
<dd> This option tells <code>tccat</code> to loop through all chapters starting at the one given with the option <code>-T</code>.</p>
<dt><code>-S</code> <i>n</i></p>
<dd> Seek to program stream (VOB) offset <i>n</i>x2kB before starting output.</p>
<dt><code>-P</code></p>
<dd> Stream full DVD title specified by -T.</p>
<dt><code>-a</code></p>
<dd> Use this option to dump an AVI-file/socket audio stream. The default is to extract and concatenate AVI-file video stream.</p>
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
<p> <code>tccat</code> is a front end for streaming various source types and is used in <code>transcode</code>&#8216;s import modules.</p>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>tccat -i /dev/dvd -T 1,-1 | mplayer &#8211;</code> </p>
<p> reads all chapters belonging to title <i>1</i> of a DVD (assuming that /dev/dvd/ is a symbolic link to a real DVD device) and pipes a MPEG program stream into player.</p>
<h2>AUTHORS</h2>
<p> <code>tccat</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
