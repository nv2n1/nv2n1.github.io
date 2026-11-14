---
title: "tcdecode(1)"
name: "tcdecode"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcdecode/"
description: "tcdecode – read multimedia streams from medium, decode to raw format and print to standard output"
---

<h2>NAME</h2>
<p> tcdecode &#8211; read multimedia streams from medium, decode to raw format and print to standard output</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcdecode</code></p>
<dd> <code>-i</code> <i>name</i> [ <code>-x</code> <i>codec</i> ] [ <code>-t</code> <i>package</i> ] [ <code>-g</code> <i>WxH</i> ] [ <code>-s</code> <i>c,f,r</i> ] [ <code>-C</code> <i>s-e</i> ] [ <code>-y</code> <i>codec</i> ] [ <code>-Y</code> ] [ <code>-Q</code> <i>mode</i> ] [ <code>-A</code> <i>flag</i> ] [ <code>-d</code> <i>verbosity</i> ] [ <code>-v</code> ]</dl>
<h2>COPYRIGHT</h2>
<p> <code>tcdecode</code> is Copyright (C) by Thomas Oestreich.</p>
<h2>DESCRIPTION</h2>
<p> <code>tcdecode</code> is part of and usually called by <code>transcode</code>.<br />
 However, it can also be used independently.<br />
 <code>tcdecode</code> reads source (from stdin if not explicitely defined) and prints on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i </code><i>name</i></p>
<dd> Specify input source. If ommited, <i>stdin</i> is assumed. <code>tcdecode</code> reads streams from file or from stdin. </p>
<dt><code>-g </code><i>WxH</i></p>
<dd> video frame width and height [720&#215;576] </p>
<dt><code>-C </code><i>s-e</i></p>
<dd> decode and print out only this frame interval (video) or bytes (audio) [all]. </p>
<dt><code>-x </code><i>codec</i></p>
<dd> source codec, if not detected of reading from stdin. This option also specifies video and audio context of the source for decoding. Currently, supported parameter for <i>codec</i> are </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>mp3</i></td>
<td ALIGN=center>MPEG audio</td>
<td>(lame)
</td>
</tr>
<tr VALIGN=top>
<td><i>ac3</i></td>
<td ALIGN=center>AC3 audio</td>
<td>(liba52)
</td>
</tr>
<tr VALIGN=top>
<td><i>dv</i></td>
<td ALIGN=center>Digital Video DV</td>
<td>(libdv)
</td>
</tr>
<tr VALIGN=top>
<td><i>mpeg2</i></td>
<td ALIGN=center>MPEG video</td>
<td>(libmpeg2)
</td>
</tr>
<tr VALIGN=top>
<td><i>yv12</i></td>
<td ALIGN=center>Y&#8217;CbCr YUV</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>mov</i></td>
<td ALIGN=center>Quicktime</td>
<td>(libquicktime)
</td>
</tr>
</table>
</dl>
<dt><code>-t </code><i>package</i></p>
<dd> Currently only argument supported is &quot;lavc&quot;. Use the codec by -x from this package. Available (-x) codecs for <i>lavc</i> are: mpeg2, divx3, divx, divx4, mp42, mjpg, rv10, svq1, svq3, vp3, 4xm, wmv1, wmv2, hfyu, indeo3, h263p, h263i </p>
<dt><code>-y </code><i>codec</i></p>
<dd> target codec. <code> tcdecode </code> only decodes to raw format suitable for transcode. Valid option parameter for <i>codec</i> are </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>rgb</i></td>
<td ALIGN=right>RGB 24bit
</td>
</tr>
<tr VALIGN=top>
<td><i>yv12</i></td>
<td ALIGN=right>Y&#8217;CbCr YUV
</td>
</tr>
<tr VALIGN=top>
<td><i>yuy2</i></td>
<td ALIGN=right>4:2:2 YUV
</td>
</tr>
<tr VALIGN=top>
<td><i>pcm</i></td>
<td ALIGN=right>SIGNED LE 16bit PCM
</td>
</tr>
</table>
</dl>
<dt><code>-s</code> <i>c,f,r</i></p>
<dd> audio gain for AC3 downmixing [1.0,1.0,1.0] </p>
<dt><code>-Y</code></p>
<dd> decoded Digital Video (raw) YUV frame is in YUY2 (packet) format using libdv. Downsample frame to YV12. PAL users should compile libdv with &#8211;with-pal-yuv=YV12 to avoid this option [off] </p>
<dt><code>-A</code> <i>flag</i></p>
<dd> audio flag for AC3/A52 decoder [none]. This flag determines the down-mixing configuration. Valid choices for <i>flag</i> are determined by the following bits set: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>drc off</td>
<td ALIGN=right>1
</td>
</tr>
<tr VALIGN=top>
<td>demux</td>
<td ALIGN=right>2
</td>
</tr>
<tr VALIGN=top>
<td>dolby off</td>
<td ALIGN=right>4
</td>
</tr>
</table>
</dl>
<p> Add those numbers to turn multiple options on. </p>
<dt><code>-Q</code> <i>mode</i></p>
<dd> decoding quality. Certain codecs, e.g., DV with libdv allow for changing this parameter if speed is prefered over quality. Valid parameter are 1=fastest-5=best [5]. </p>
<dt><code>-d</code> <i>level</i></p>
<dd> With this option you can specify a bitmask to enable different levels of verbosity (if supported). You can combine several levels by adding the corresponding values: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>QUIET</td>
<td ALIGN=right>0
</td>
</tr>
<tr VALIGN=top>
<td>INFO</td>
<td ALIGN=right>1
</td>
</tr>
<tr VALIGN=top>
<td>DEBUG</td>
<td ALIGN=right>2
</td>
</tr>
<tr VALIGN=top>
<td>STATS</td>
<td ALIGN=right>4
</td>
</tr>
<tr VALIGN=top>
<td>WATCH</td>
<td ALIGN=right>8
</td>
</tr>
<tr VALIGN=top>
<td>FLIST</td>
<td ALIGN=right>16
</td>
</tr>
<tr VALIGN=top>
<td>VIDCORE</td>
<td ALIGN=right>32
</td>
</tr>
<tr VALIGN=top>
<td>SYNC</td>
<td ALIGN=right>64
</td>
</tr>
<tr VALIGN=top>
<td>COUNTER</td>
<td ALIGN=right>128
</td>
</tr>
<tr VALIGN=top>
<td>PRIVATE</td>
<td ALIGN=right>256
</td>
</tr>
</table>
</dl>
<dt><code>-v</code></p>
<dd> Print version information and exit. </p>
</dl>
<h2>NOTES</h2>
<p> <code>tcdecode</code> is a front end for decoding various sources and is used in <code><a href="/docs/linux/man/1-transcode/">transcode</a>(1)</code>&#8216;s import modules.</p>
<h2>EXAMPLES</h2>
<p> The command </p>
<pre>
	tcdecode -i foo.mp3 -x mp3
</pre>
<p> decodes an MPEG audio stream and prints raw PCM data to stdout. </p>
<p> The command </p>
<pre>
	tcextract -i foo.avi -x mp3 | tcdecode -x mp3
</pre>
<p> extracts an MPEG audio track from the AVI-file foo.avi and pipes the frames into the decoder </p>
<h2>AUTHORS</h2>
<p> <code>tcdecode</code> was written by Thomas Oestreich<br />
 &lt;ostreich [at] theorie.physik.uni-goettingen.de&gt; with contributions from many others. See AUTHORS for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avifix/">avifix</a></code>(1), <code><a href="/docs/linux/man/1-avisync/">avisync</a></code>(1), <code><a href="/docs/linux/man/1-avimerge/">avimerge</a></code>(1), <code><a href="/docs/linux/man/1-avisplit/">avisplit</a></code>(1), <code><a href="/docs/linux/man/1-tcprobe/">tcprobe</a></code>(1), <code><a href="/docs/linux/man/1-tcscan/">tcscan</a></code>(1), <code><a href="/docs/linux/man/1-tccat/">tccat</a></code>(1), <code><a href="/docs/linux/man/1-tcdemux/">tcdemux</a></code>(1), <code><a href="/docs/linux/man/1-tcextract/">tcextract</a></code>(1), <code><a href="/docs/linux/man/1-tcdecode/">tcdecode</a></code>(1), <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1) </p>
<h2>Index</h2>
