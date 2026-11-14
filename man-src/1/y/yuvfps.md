---
title: "yuvfps(1)"
name: "yuvfps"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvfps/"
description: "yuvfps – Converts to a different frame rate"
---

<h2 class="name">NAME</h2>
<p> yuvfps &#8211; Converts to a different frame rate</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvfps </code> [<code>-r</code> <i>Num:Den</i>] [<code>-s</code> <i>Num:Den</i>] [<code>-i</code> <i>Interlacing</i>] [<code>-I</code> <i>Interlacing</i>] [<code>-c</code>] [<code>-n</code>] [<code>-w</code>] [<code>-v 0</code>&#8211;<code>2</code>] [<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvfps</code> is a general (UP or DOWN) resampling utility that is provided to allow the generation of video streams with the frame rates required for each standard video format. <code>yuvfps</code> reads a YUV4MPEG stream from the standard input and outputs a YUV4MPEG stream to the standard output in which frames from the original ones are skipped (downsampling) or duplicated (upsampling). This allows for other mjpegtools that require a specific frame rate to process the stream. </p>
<p> <code>yuvfps</code> uses by default Bresenham&#8217;s algorithm to do the resampling so that the new video stream is similar to the original one. Note, however, that downscaling is a non-reversible operation because frames are dropped. Moreover, the resulting video stream may not have the exact same duration as the original one if the new frame rate is not a whole multiple of the original rate.<br />
&nbsp;<wbr>&nbsp;<wbr> As an alternative to simply dropping or duplicating frames each output frame/field can be produced as a weighted average of the two temporally closest input frames/fields. In this mode, <code>yuvfps</code> can also change the interlacing mode of the stream. </p>
<p> <code>yuvfps</code> also can &quot;fix&quot; the framerate specified in the YUV4MPEG header. This allows for the generation of effects (fast-forwarding, slow motion) and also when the source stream has some framerate that is very close, but not exactly, the rate required for some standard video (for example, 24.9 vs 25). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r Num:Den</code></p>
<dd>
<dt>
<dd> Specifies the resulting stream frame rate.</p>
<dt><code>-s Num:Den</code></p>
<dd>
<dt>
<dd> Ignores the frame rate in the input stream and assumes this frame rate for the input stream.</p>
<dt><code>-i Interlacing</code></p>
<dd>
<dt>
<dd> Specifies the interlacing mode of the resulting stream. The interlacing mode can be changed only when using the weighted average resampling mode (the -w option).</p>
<dt>
<dd> p &#8211; progressive (non-interlaced)<br />
 t &#8211; top-field first<br />
 b &#8211; bottom-field first</p>
<dt><code>-I Interlacing</code></p>
<dd>
<dt>
<dd> Ignores the interlacing mode information in the input stream and assumes this interlacing mode for the input stream. The possible values are the same as for the -i option.</p>
<dt><code>-c </code></p>
<dd>
<dt>
<dd> Changes the stream header frame rate and interlacing mode in the output stream but copies frames from the original stream without changes. The -r and -i options specify the frame rate and interlacing mode for the output stream header.</p>
<dt><code>-n </code></p>
<dd>
<dt>
<dd> By default yuvfps tries to find a normalized framerate. Some programs create framerates like: 29969909:1000000 which is actually th typical NTSC framerate of 30000:1001. yuvfps prints out the normalizes values and the original when it starts. If you think the normalized value is not correct and want yuvfps to use the original given number you have to add that option. So yuvfps does not try to normalize the values.</p>
<dt><code>-w</code></p>
<dd>
<dt>
<dd> Produce each output frame/field as a weighted average of the two temporally closest input frames/fields instead of simply dropping or duplicating frames. The blending of two adjacent frames/fields reduces visible stepping compared to the default drop/duplicate algorithm but as a drawback it makes fast moving objects appear blurred and is much slower.</p>
<dt><code>-v [0,1,2]</code></p>
<dd>
<dt>
<dd> Set verbosity level.<br />
&nbsp;<wbr>0&nbsp;<wbr>=&nbsp;<wbr>warnings and error messages only.&nbsp;<wbr><br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>add informative messages, like the framerate conversation information.<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>add chatty debugging message, too. </p>
</dl>
<h2>AUTHOR</h2>
<p> This man page was written by Alfonso García-Patiño Barbolani.<br />
 Johannes Lehtinen added information about the weighted average resampling mode and the related options.<br />
 If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net/">http://mjpeg.sourceforge.net/</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1), <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-lavpipe/">lavpipe</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1) <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1) </p>
<h2>Index</h2>
