---
title: "pambayer(1)"
name: "pambayer"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pambayer/"
description: "pambayer – interpret Bayer patterns"
---

<h2 class="name">NAME</h2>
<p> pambayer &#8211; interpret Bayer patterns</p>
<h2>SYNOPSIS</h2>
<p> <code>pambayer</code> <code>-type=</code>{<code>1</code>|<code>2</code>|<code>3</code>|<code>4</code>} [<code>-nointerpolate</code>] [<i>pamfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pambayer</code> reads a Bayer pattern in a 1-deep Netpbm image and produces a color image in PAM RGB format as output. </p>
<p> A Bayer pattern is what you get from the optical sensor in some digital cameras. Such a camera doesn&#8217;t have a red, green, and blue sensor in the exact same place for an individual pixel. Instead, it has red, green, and blue sensors laid out in a two dimensional array. The pattern in which they are laid out is the Bayer pattern. The input to <code>pambayer</code> is one sample value for each of those sensors, so some samples are red, some are green, and some are blue. </p>
<p> <code>pambayer</code> turns that into a regular visual image with one pixel per sensor. For the two components of each pixel that are missing in the corresponding Bayer input, <code>pambayer</code> averages the sample values from the adjacent pixels that do have that component. </p>
<p> But you can have <code>pambayer</code> fill in black instead (see the <code>-noninterpolate</code> option), which gives you a simpler representation of what the camera saw, on which you might do further processing. Such an image still looks right, though considerably dimmer, if you stand far enough away and let your eyes do the interpolation. </p>
<p> The input image is a pseudo-PNM image (pseudo- because while the structure is the same, the sample values have different meanings) or PAM image of arbitrary tuple type. <code>pambayer</code> looks at only the first plane of the input. </p>
<p> The output image is a PAM image of tuple type &#8216;RGB&#8217;, i.e. a standard color image. You can convert this to PPM with <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) </p>
<p> If you&#8217;re interested in just one of the primary colors, use <code>pamchannel</code> on the output of <code>pambayer</code> to extract it. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-type=</code><i>n</i></p>
<dd> This tells which Bayer pattern the input is: </p>
<dt>1</p>
<dd> GBG/RGR/GBG matrix</p>
<dt>2</p>
<dd> RGR/GBG/RGR matrix</p>
<dt>3</p>
<dd> BGB/GRG/BGB matrix</p>
<dt>4</p>
<dd> GRG/BGB/GRG matrix </p>
<p> This option is mandatory. </p>
<dt><code>-nointerpolate</code></p>
<dd> Each output pixel position corresponds to one position in the input Bayer pattern, which means only one of the three color components is supplied by the input. For the other two, this option says to user zero. Without it, <code>pambayer</code> instead interpolates from the adjacent pixels that do have that color component. </p>
<p> This option was new in Netpbm 10.49 (December 2009). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cameratopam/">cameratopam</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pambayer</code> was new in Netpbm 10.30 (October 2005). </p>
<h2>Index</h2>
