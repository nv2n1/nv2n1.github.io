---
title: "tcdemux(1)"
name: "tcdemux"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcdemux/"
description: "tcdemux – demultiplex a program stream"
---

<h2>NAME</h2>
<p> tcdemux &#8211; demultiplex a program stream</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcdemux</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-t</code> <i>magic</i> ] [ <code>-x</code> <i>codec</i> ] [ <code>-S</code> <i>unit,[s1-s2]</i> ] [ <code>-a</code> <i>ach,[vch]</i> ] [ <code>-s</code> <i>0xnn</i> ] [ <code>-M</code> <i>mode</i> ] [ <code>-f</code> <i>fps</i> ] [ <code>-W</code> ] [ <code>-O</code> ] [ <code>-P</code> <i>name</i> ] [ <code>-A</code> <i>n[,m[,&#8230;]]</i> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tcdemux</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tcdemux</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tcdemux</code> reads source (from stdin if not explicitely defined) and prints on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed. </p>
<dt><code>-x </code><i>codec</i></p>
<dd> Process only packets containing given <i>codec</i> as payload. Examples are &quot;mpeg2&quot; for MPEG video or &quot;ac3&quot; for audio packets. </p>
<dt><code>-t </code><i>magic</i></p>
<dd> Specify the input file type <i>magic.</i> Useful for using <code>tcdemux</code> in pipelines. This is normally autodetected. </p>
<dt><code>-a </code><i>ach[,vch]</i></p>
<dd> Process only packets containing given audio track <i>ach</i> and video track <i>vch.</i> Most program stream feature multiple audio tracks but only a single video stream. Default is &quot;-a 0,0&quot;. </p>
<dt><code>-s </code><i>0xnn</i></p>
<dd> Select specific multimedia track using the standard identifier <i>0xnn.</i> This useful to extract subtitle packets. </p>
<dt><code>-f </code><i>fps</i></p>
<dd> Specify the frame rate <i>fps</i> for subtitle meta information used by external applications. </p>
<dt><code>-S </code><i>unit[,s1-s2]</i></p>
<dd> Select a program unit <i>unit</i> and a selected GOP range <i>s1-s2</i> for processing. A <i>unit</i> is usually a set of GOPs that need to be synchronized at the very beginning. This option can be used to eleminate junk units at the beginning of the main presentation or to select certain episodes of a TV series from a DVD. A GOP is a logical unit to be properly decoded, i.e., decoding can only start at the beginning of a GOP. </p>
<dt><code>-O</p>
<dd> Do not skip initial sequence. Used internally by transcode. </p>
<dt>-A </code><i>n[,m[,&#8230;]]</i></p>
<dd> Select packets using an identifier for extracting only selected streams without processing. This is useful for size reduction of your multimedia stream. Example: </p>
<p> <code>tcdemux -i big_dvd.vob -A 0xe0,0x81,0x20 &gt; small_dvd.vob</code> </p>
<p> extracts all packets for the video stream, AC3 audio track (1) and the first subtitle stream (0). </p>
<dt><code>-M </code><i>mode</i></p>
<dd> Select synchronization strategy <i>mode.</i> This is how transcode selects the beginning of a video and audio stream to assure both streams are sychronized for further processing: </p>
<p> 0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>no synchronization. Packets are printed directly to <i>stdout</i>.</p>
<p> 1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>synchronization based on PTS information found in the packet header. Audio packets are delayed until a suitable starting point is found. Default for PAL videos.</p>
<p> 2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NTSC adapted synchronization mode. Detailed information for each GOP contained in the video stream are piped to a <i>stdout</i> to be processed by<br />
 the certain import modules. This enables adjusting the frame rate or inverse telecine, if necessary. </p>
<p> 3 more advanced synchronization mode 1 with msec granular adjustment. Details delegated to transcode. </p>
<p> 4 more advanced synchronization mode 2 with msec granular adjustment for NTSC materail. Details delegated to transcode. </p>
<p> 5-7<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>undocumented debugging modes for internal use.</p>
<dt><code>-P </code><i>file</i></p>
<dd> Write GOP meta information to <i>file</i> instead of tdout. </p>
<dt><code>-W</p>
<dd> Print a navigation log file for a given video stream to </code><i>stdout</i>. This is used for transcode&#8217;s &quot;psu mode&quot; and &quot;cluster mode&quot;. </p>
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
<p> <code>tcdemux</code> is a front end for de-multiplexing program streams and is used in <code>transcode</code>&#8216;s import modules.</p>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>tcprobe -i movie.vob -x mpeg2</code> </p>
<p> extracts only MPEG video packets. Further processing, i.e., extracting the elementary video stream is done by <code>tcextract.</code> </p>
<h2>AUTHORS</h2>
<p> <code>tcdemux</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
