---
title: "lav2yuv(1)"
name: "lav2yuv"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lav2yuv/"
description: "lav2yuv – Convert a MJPEG file to raw yuv"
---

<h2>NAME</h2>
<p> lav2yuv &#8211; Convert a MJPEG file to raw yuv </p>
<h2>SYNOPSIS</h2>
<p> <code>lav2yuv</code> [<i>options</i>] <i>lavfile1 </i>[<i>lavfile2 </i>&#8230;<i> lavfileN</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>lav2yuv</code> converts an MJPEG video sequence described by a sequence of MJPEG video files and/or edit lists pointing to such files into the simple uncompressed planar 4:2:0 Y&#8217;CbCr format, as used by <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1) MPEG encoder and image processing filters like <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) or <code><a href="/docs/linux/man/1-yuv2dfilter/">yuv2dfilter</a></code>(1) or <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1). </p>
<p> Output is to stdout so that by piping the output of lav2yuv into a suitable pipeline it is possible to process and then encode or play back video recorded in any of the mjpegtools MJPEG container formats: AVI, quicktime or edit lists describing editted versions of video held in such files. </p>
<p> Mixing different files with different video formats is currently not possible. </p>
<p> The <code>-S -T -D</code> options are used for scene detection which is used by linux video studio. </p>
<h2>OPTIONS</h2>
<p> <code>lav2yuv</code> accepts the following options: </p>
<dl>
<dt><code>-m</code></p>
<dd> Force mono-chrome</p>
<dt><code>-c</code></p>
<dd> Conceal frames containing corrupt MJPEG data by repeating the preceeding good frame.</p>
<dt><code>-S</code><i> list.el</i></p>
<dd> Output a scene list with scene detection</p>
<dt><code>-T</code><i> num</i></p>
<dd> Set scene detection threshold to num (default: 4)</p>
<dt><code>-D</code><i> num</i></p>
<dd> Width decimation to use for scene detection (default: 2)</p>
<dt><code>-o</code><i> num</i></p>
<dd> Frame offset &#8211; skip <i>num</i> frames at the beginning. if <i>num</i> is negative all but the last <i>num</i> frames are skipped</p>
<dt><code>-f</code><i> num</i></p>
<dd> Only <i>num</i> frames are written to stdout. 0 means that all frames are processed.</p>
<dt><code>-A</code><i>&nbsp;<wbr>width:height</i></p>
<dd> Set/override the sample aspect ratio (SAR) emitted in the output stream header. Currently, the SAR is only auto-detected for DV files, and guessed otherwise.</p>
<dt><code>-P</code><i>&nbsp;<wbr>width:height</i></p>
<dd> Set the intended/approximate display aspect ratio (DAR) for the stream. This value is only used to guess the SAR when it cannot be detected from the input stream. The default DAR is &#8216;4:3&#8242; (corresponding to a standard TV screen); another useful value is &#8217;16:9&#8217; (corresponding to widescreen TV).</p>
<dt><code>-C</code><i>&nbsp;<wbr>chroma</i></p>
<dd> Set output chroma (default: &#8216;420jpeg&#8217;). Currently, &#8216;420jpeg&#8217;, &#8216;420mpeg2&#8217;, &#8216;420paldv&#8217;, &#8216;422&#8217; are available.</p>
<dt><code>-x</code></p>
<dd> Exchange fields. Useful if the field order was reversed during editing.</dl>
<h2>AUTHOR</h2>
<p> This man page was originally written by Bernhard Praschinger.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvplay/">yuvplay</a></code>(1) </p>
<h2>Index</h2>
