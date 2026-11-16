---
title: "pamtilt(1)"
name: "pamtilt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtilt/"
description: "pamtilt – print the tilt angle of a PGM file"
---

<h2 class="name">NAME</h2>
<p> pamtilt &#8211; print the tilt angle of a PGM file</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtilt</code> [<code>-angle=</code><i>maxangle</i>] [<code>-fast</code>] [<code>-quality=</code><i>q</i>] [<code>-hstep=</code><i>n</i>] [<code>-vstep=</code><i>n</i>] [<code>-dstep=</code><i>n</i>] [<code>-astep=</code><i>n</i>] [<code>-verbose</code>] [<i>pgmfile</i>] </p>
<h2>EXAMPLES</h2>
<pre>
<tt>
    scanimage --mode Gray --resolution 300 &gt;crooked.pgm
    pnmrotate -b white `pamtilt crooked.pgm` crooked.pgm &gt;straight.pgm
</tt>
    (then crop, threshold, etc.)
</pre>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtilt</code> tries to find the correct angle for untilting (de-skewing) a scanned text document. The output is a single floating-point number (the angle in degrees) for use as the argument to pnmrotate. </p>
<p> &#8216;Document skew&#8217; is the name given to what happens when you feed a page into an image scanner at an angle: the resulting image is tilted. <code>pamtilt</code> aims to correct that. </p>
<p> <code>pamtilt</code> makes three iterations at successively finer increments, testing prospective rotation angles to find the best one. <code>pamtilt</code> works best for straightening images with strong horizontal lines and does poorly with arbitrary photos. If <code>pamtilt</code> has no confidence in its results, it prints the special value 00.00; you can check for this or just pass it as a legal argument to pnmrotate. </p>
<p> <code>pamtilt</code> operates on the first plane of the input image, which is either PNM or PAM, and ignores any other planes. Ordinarily, the input is PGM or GRAYSCALE PAM, so there is only one plane. </p>
<p> <code>pamtilt</code> works on bilevel (PBM, BLACKANDWHITE PAM) images as well as grayscale, but you will minimize artifacts if you scan and rotate in grayscale before you apply a threshold to make a bilevel image.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h2>OPTIONS</h2>
<p> A few options have general utility: </p>
<dl>
<dt><code>-angle=</code><i>maxangle</i></dt>
<dd> Assume a maximum tilt angle of <i>maxangle</i> (measured in degrees). The default value is sufficient for most images, even those scanned somewhat carelessly. </dd>
<p> The default is 10.0. </p>
<dt><code>-fast</code></dt>
<dd> Skip the third iteration for speed at the expense of accuracy. </dd>
<dt><code>-verbose</code></dt>
<dd> Show on Standard Error the measurements computed at each tested angle. </dd>
</dl>
<p> Here are some other options you can use to tune the operation of <code>pamtilt</code> but they&#8217;re seldom needed. The default values accommodate a wide variety of input documents. </p>
<dl>
<dt>
</dt><dd> <code>-quality=</code><i>q</i> Require a signal-to-noise ratio of a least <i>q</i> on the first iteration to report a valid result. Larger values reduce the chances of obtaining a bogus result at the risk of obtaining no result at all. </dd>
<p> The default is 1.0. </p>
<dt><code>-hstep=</code><i>n</i></dt>
<dd> Set the horizontal increment to check every <i>n</i>th column. This value affects both run time and memory requirements. </dd>
<p> The default is 11. </p>
<dt><code>-vstep=</code><i>n</i></dt>
<dd> Set the vertical increment to check every nth row. Larger values usually work, reducing run time, but they increase the risk of incorrect results. </dd>
<p> The default is 5. </p>
<dt><code>-dstep=</code><i>n</i></dt>
<dd> Set the vertical distance used when checking pixels in a column. The default is intended to minimize the effect of noise along a horizontal boundary. </dd>
<p> The default is 2. </p>
<dt><code>-astep=</code><i>n</i></dt>
<dd> Set the angle increment of the first iteration, in degrees. </dd>
<p> The default is 1.0. </p>
</dl>
<h2>REFERENCES</h2>
<p> <code>pamtilt</code> implements a somewhat simplified algorithm inspired by: &quot;Measuring Document Image Skew and Orientation&quot;, by Bloomberg, Kopec, and Dasari. In SPIE Volume 2422, Document Recognition II, pages 302-316, February 1995. </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd>
<p> <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1) </p>
</dd><dt>&bull;</dt>
<dd>
<p> <code>pgm</code>(1) </p>
</dd></dl>
<h2>HISTORY</h2>
<p> <code>pamtilt</code> was new in Netpbm 10.30 (October 2005). </p>
<p> Gregg Townsend wrote it and sent it to Bryan Henderson in August 2005. Bryan recoded it to fit Netpbm conventions. </p>
<h2>Index</h2>
