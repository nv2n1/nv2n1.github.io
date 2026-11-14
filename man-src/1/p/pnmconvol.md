---
title: "pnmconvol(1)"
name: "pnmconvol"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmconvol/"
description: "pnmconvol – general MxN convolution on a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmconvol &#8211; general MxN convolution on a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmconvol</code> <i>convolutionfile</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads two portable anymaps as input. Convolves the second using the first, and writes a portable anymap as output. </p>
<p> Convolution means replacing each pixel with a weighted average of the nearby pixels. The weights and the area to average are determined by the convolution matrix. The unsigned numbers in the convolution file are offset by -maxval/2 to make signed numbers, and then normalized, so the actual values in the convolution file are only relative. </p>
<p> Here is a sample convolution file; it does a simple average of the nine immediate neighbors, resulting in a smoothed image: </p>
<pre>
    P2
    3 3
    18
    10 10 10
    10 10 10
    10 10 10
</pre>
<p> To see how this works, do the above-mentioned offset: 10 &#8211; 18/2 gives 1. The possible range of values is from 0 to 18, and after the offset that&#8217;s -9 to 9. The normalization step makes the range -1 to 1, and the values get scaled correspondingly so they become 1/9 &#8211; exactly what you want. The equivalent matrix for 5&#215;5 smoothing would have maxval 50 and be filled with 26. </p>
<p> The convolution file will usually be a graymap, so that the same convolution gets applied to each color component. However, if you want to use a pixmap and do a different convolution to different colors, you can certainly do that. </p>
<p> At the edges of the convolved image, where the convolution matrix would extend over the edge of the image, <code>pnmconvol</code> just copies the input pixels directly to the output. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer.<br />
 Modified 26 November 1994 by Mike Burns, burns [at] chem.psu.edu </p>
<h2>Index</h2>
