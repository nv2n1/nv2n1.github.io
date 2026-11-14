---
title: "y4munsharp(1)"
name: "y4munsharp"
section: "1"
letter: "y"
url: "/docs/linux/man/1-y4munsharp/"
description: "y4munsharp – Unsharp filter for YUV4MPEG2 streams"
---

<h2>NAME</h2>
<p> y4munsharp &#8211; Unsharp filter for YUV4MPEG2 streams</p>
<h2>SYNOPSIS</h2>
<p> <code>y4munsharp</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>y4munsharp</code> is an implementation of the GIMP unsharp filter for YUV4MPEG2 streams. The usual 3 parameters for unshap mask processing (radius, amount and threshold) are specified on the command line. By default only the Y&#8217; (luma) component is processed although processing of the CbCr (chroma) may be requested by a commandline option. Output must be either to a pipe or a file, leaving stdout as a terminal will elicit an error and the program will exit.</p>
<h2>OPTIONS</h2>
<p> <code>y4munsharp</code> accepts the following options:</p>
<dl>
<dt><code>-v</code><i> num</i></p>
<dd> Set verbosity level (0 = quiet, 1 = normal, 2 = debug) (default: 1)</p>
<dt><code>-h</code></p>
<dd> Print a suage summary and exit</p>
<dt><code>-L</code><i> radius,amount,threshold</i></p>
<dd> Y&#8217; (luma) unsharp parameters. The <i>radius</i> and <i>amount&quot; arguments are floating point numbers. The threshold</i> argument is an integer. (default: 3.0,0.3,4) <code>-C</code><i> radius,amount,threshold</i> CbCr (chroma) unsharp parameters. The chroma is not processed unless this option is given. Arguments are the same type as for the -L option above. (default: none)</p>
<dt><code>-N</code></p>
<dd> Filtering can produce output outside the 16 to 240 range for Y&#8217; and 16 to 235 for CbCr. By default values outside the legal range are clipped/cored (values over 240 for Y&#8217; are set to 240 for example). Using <code>-N</code> the limits 0 and 255 are used instead.</dl>
<h2>EXAMPLES</h2>
<p> A mild setting: </p>
<pre>
y4munsharp -L 2.0,0.3,0
An aggressive setting:
y4munsharp -L 5.0,0.5,0
</pre>
<h2>NOTES</h2>
<p> The radius, amount, threshold parameters have the same meaning as the GIMP&#8217;s unsharp plugin. This means you can use the GIMP on selected frame still images to determine suitable settings for <code>y4munsharp</code>. The key thing to remember is to be subtle &#8211; you just barely want to notice the sharpening effect. If the effect is obvious (&quot;jumps out at you&quot;) then the parameters are set too aggressively. </p>
<p> The chroma is not processed for a several reasons: 1) The eye is much more sensitive to changes in brightness, 2) the chroma is usually subsampled and doesn&#8217;t contribute much to the perceived sharpness of an image &#8211; so not processing the chroma provides a boost in speed of processing the image, and 3) possible artifacting &#8211; changes in Y&#8217; just make an image brighter/darker but changes in Cb or Cr can change colors and possibly lead to shifts in hue. Use the <code>-C</code> option to enable processing of the chroma planes.</p>
<h2>BUGS</h2>
<p> Only the 3 plane YUV4MPEG2 formats are supported. </p>
<p> Only progressive, top field first or bottom field first interlaced streams are handled. The mixed interlaced stream format is not supported. </p>
<h2>Index</h2>
