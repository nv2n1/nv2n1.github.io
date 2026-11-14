---
title: "yuvmedianfilter(1)"
name: "yuvmedianfilter"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yuvmedianfilter/"
description: "yuvmedianfilter – A filter for yuv images produced by the mjpeg tools"
---

<h2 class="name">NAME</h2>
<p> yuvmedianfilter &#8211; A filter for yuv images produced by the mjpeg tools</p>
<h2>SYNOPSIS</h2>
<p> <code>yuvmedianfilter</code> [<code>-r</code> <i>num</i>] [<code>-R</code> <i>num</i>] [<code>-t</code> <i>num</i>] [<code>-T</code> <i>num</i>] [<code>-I</code> <i>num</i>] [<code>-f</code>] [<code>-w</code> <i>num</i>] [<code>-s</code> <i>num</i>] [<code>-v</code> <i>num</i>] [<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>yuvmedianfilter</code> is designed to enhance/filter images. It takes the input from STDIN and writes output to STDOUT.<br />
 This filter looks around the current point for a radius and averages the values that fall inside a threshold. So the image is softened and the edges become more sharp. If the input material is noisy (it is always noisy but you do not always see it) the output images are improved and the encoder spends less bandwidth encoding noise. The more sophisticated version of image filtering is yuvdenoise. But you can use both programs in the encoding procces. It cannot process a recorded file and write the improved version to another file. </p>
<h2>OPTIONS</h2>
<p> <code>yuvmedianfilter</code> accepts the following options: </p>
<dl>
<dt><code>-r</code><i> num</i></p>
<dd> Radius for luma median (default: 2 pixels)</p>
<dt><code>-R</code><i> num</i></p>
<dd> Radius for chroma median (default: 2 pixels)</p>
<dt><code>-t</code><i> num</i></p>
<dd> Trigger threshold for luma (default: 2 [0=disable])</p>
<dt><code>-T</code><i> num</i></p>
<dd> Trigger threshold for chroma (default: 2 [0=disable])</p>
<dt><code>-I</code><i> num</i></p>
<dd> Interlacing type (0=no, 1=yes, default: taken from yuv stream)</p>
<dt><code>-f</code></p>
<dd> Fast mode, i.e. the threshold is ignored, and a simple mean of the surrounding values is calculated.</p>
<dt><code>-w</code><i> num</i></p>
<dd> In fast mode, the weight given to the current value versus the surrounding values. Default is 8.<br />
 Note that certain combinations of radii and weights have been optimized to be even faster &#8212; radius 1 and weight 2.667, radius 1 and weight 8, and radius 2 and weight 8.</p>
<dt><code>-c</code><i> num</i></p>
<dd> In slow mode, more than this fraction of the pixels must be within the threshold; otherwise the pixel is simply the weighted mean of pixels within a radius of 1. Default is 0.33333.</p>
<dt><code>-s</code><i> num</i></p>
<dd> Number of beginning frames to skip. The first num frames are written to stdout unfiltered. This is useful for resuming an interrupted job without having to duplicate work.</p>
<dt><code>-v</code><i> num</i></p>
<dd> Verbosity level (0, 1 or 2)</p>
<dt><code>-h</code></p>
<dd> Print out a help message </p>
</dl>
<h2>BUGS</h2>
<p> It is slow. Using a radius greater than the default of 2 is painfully slow. </p>
<h2>AUTHOR</h2>
<p> This man page was written by Bernhard Praschinger.<br />
 The yuvmedianfilter program was written by Mike Bernson, and adapted to the yuv4mpeg2 stream header format by Steven M. Schultz. </p>
<p> If you have questions, remarks, problems or you just want to contact the developers, the main mailing list for the MJPEG-tools is:<br />
&nbsp;<wbr>&nbsp;<wbr><i>mjpeg-users [at] lists.sourceforge.net</i> </p>
<dl>
<dt>For more info, see our website at</p>
<dd> <i><a rel="nofollow" href="http://mjpeg.sourceforge.net">http://mjpeg.sourceforge.net</a></i> </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mjpegtools/">mjpegtools</a></code>(1), <code><a href="/docs/linux/man/1-jpeg2yuv/">jpeg2yuv</a></code>(1), <code><a href="/docs/linux/man/1-lav2yuv/">lav2yuv</a></code>(1), <code><a href="/docs/linux/man/1-mpeg2enc/">mpeg2enc</a></code>(1), <code><a href="/docs/linux/man/1-ppmtoy4m/">ppmtoy4m</a></code>(1), <code><a href="/docs/linux/man/1-yuv2lav/">yuv2lav</a></code>(1), <code><a href="/docs/linux/man/1-yuvdenoise/">yuvdenoise</a></code>(1), <code><a href="/docs/linux/man/1-yuvscaler/">yuvscaler</a></code>(1) </p>
<h2>Index</h2>
