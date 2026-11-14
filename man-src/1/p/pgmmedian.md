---
title: "pgmmedian(1)"
name: "pgmmedian"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmmedian/"
description: "pgmmedian – apply a median filter to a PGM file"
---

<h2 class="name">NAME</h2>
<p> pgmmedian &#8211; apply a median filter to a PGM file</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmmedian</code> </p>
<p> [<code>-width=</code><i>n</i>] </p>
<p> [<code>-height=</code><i>n</i>] </p>
<p> [<code>-type=</code><i>median_type</i>] </p>
<p> [<code>-cutoff=</code><i>int</i>] </p>
<p> [<i>pnmfile</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmmedian</code> applies a median filter to a PGM image, using either the histogram sort or select kth value method to determine the median. </p>
<p> A median filter is a convolution filter in which the value of a pixel in the output is the median of a certain set of pixels in the neighborhood of the corresponding input pixel. The effect is to eliminate locally extreme values. Such pixels typically show up as speckles. </p>
<p> See the <code>-type</code> and <code>-cutoff</code> options for information on how <code>pgmmedian</code> chooses between the two methods. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-cutoff</code> <i>int</i></p>
<dd> This option provides the cutoff value that <code>pgmmedian</code> uses to decide between using the histogram sort or select kth value method to find the median. </p>
<p> If (<i>maxval</i> / ((<i>width</i> * <i>height</i>) &#8211; 1)), where <i>maxval</i> is the maxval of the image and <i>width</i> and <i>height</i> are the dimensions of the mask, is less than the cutoff value, <code>pgmmedian</code> uses histogram sort. Otherwise, it uses kth value. </p>
<p> This option has no effect if you specify <code>-type</code>. </p>
<p> The default is 250 </p>
<dt><code>-width=</code><i>n</i></p>
<dd> Width of the median mask to apply. </p>
<p> Default is 3. </p>
<dt><code>-height=</code><i>n</i></p>
<dd> Height of the median mask to apply. </p>
<p> Default is 3. </p>
<dt><code>-type</code> <i>median_type</i></p>
<dd> This option selects which method to use to find median regardless of cutoff value. Choices are <code>histogram_sort</code> and <code>select</code>. </p>
<p> By default, <code>pgmmedian</code> decides which method to use as described under the <code>-cutoff</code> option. </p>
</dl>
<h2>REFERENCES</h2>
<dl>
<dt>&bull;</p>
<dd> &#8216;Collected Algorithms from ACM&#8217; Volume II, Algorithm 489 by Robert W. Floyd </p>
<dt>&bull;</p>
<dd> &#8216;A Fast Two-Dimensional Median Filtering Algorithm&#8217; in &#8216;IEEE Transactions on Acoustics, Speech, and Signal Processing&#8217; Vol. ASSP-27, No. 1, February 1979 </p>
<dt>&bull;</p>
<dd> &#8216;Digital Image Processing Algorithms&#8217; by Ioannis Pitas, Prentice Hall, 1993 ISBN 0-13-145814-0 </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmnoise/">pgmnoise</a></code>(1) , <code><a href="/docs/linux/man/1-pamaddnoise/">pamaddnoise</a></code>(1) , <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) , <code><a href="/docs/linux/man/1-pgmmorphconv/">pgmmorphconv</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pgmmedian</code> was added to Netpbm in Version 10.29 (August 2005). It had been distributed by Mike Burns via his own web site before that (and continued to be so). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1996 by Mike Burns &lt;<i>burns [at] cac.psu.edu</i>&gt; </p>
<h2>Index</h2>
