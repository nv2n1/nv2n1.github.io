---
title: "pamtohdiff(1)"
name: "pamtohdiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtohdiff/"
description: "pamtohdiff – convert PAM image to horizontal difference image"
---

<h2 class="name">NAME</h2>
<p> pamtohdiff &#8211; convert PAM image to horizontal difference image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtohdiff</code> [<i>pamfile</i>] [<code>-verbose</code>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphens to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtohdiff</code> takes a PAM (or PNM) image as input and produced a horizontal difference image version of it as output. A horizontal difference image is one where the samples in each row indicate the difference between the sample value in the corresponding sample of the input image and the sample directly above it (in the previous row) in the input image. The horizontal difference image has the property that if a row of the original image is identical to the row above it over a long extent, the corresponding row in the horizontal difference image will contain all zeroes. That makes it compress better than the original image. </p>
<p> Because the horizontal difference samples can be positive or negative, but PAM samples are unsigned integers, the samples in the horizontal difference image PAM are defined to be the difference modulus the range of the input (maxval + 1). This doesn&#8217;t lose any information, as it might seem, because: of the two differences that could result in the same <code>pamtohdiff</code> output value (e.g. if maxval is 99, +20 and -80 would both result in &quot;20&quot; in the output), only one is possible in context and the other would result, when reconstructing the original image, in a value less than 0 or greater than maxval. </p>
<p> Before the modulus operation, the values <code>pamtohdiff</code> computes are also biased by half the maxval. This is to make the results easier to inspect visually. Because of the bias, you can display the <code>pamtohdiff</code> output as if it were a PNM image. As long as none of your differences are more than half the maxval, large negative differences show up as dark spots, smaller negative differences are lighter, zero differences are medium intensity, and positive differences are light. If you want this to work even for images that have differences that exceed half the maxval, just use <code>ppmdim 50</code> on the original image. To avoid losing information, though, do a <code>pamdepth</code> to double the maxval first. </p>
<p> Note that because of the transfer function just described, a difference of zero, which is most common, is represented by a PAM sample value in the output of one half the maxval. </p>
<p> The output PAM has a tuple type of &quot;hdiff&quot;. </p>
<p> You can use <code>hdifftopam</code> to recover the original image from a horizontal difference image PAM. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hdifftopam/">hdifftopam</a></code>(1) , <code><a href="/docs/linux/man/1-pamdepth/">pamdepth</a></code>(1) , </p>
<h2>AUTHOR</h2>
<p> Bryan Henderson </p>
<h2>Index</h2>
