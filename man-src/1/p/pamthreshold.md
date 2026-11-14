---
title: "pamthreshold(1)"
name: "pamthreshold"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamthreshold/"
description: "pamthreshold – threshold grayscale image to black and white"
---

<h2 class="name">NAME</h2>
<p> pamthreshold &#8211; threshold grayscale image to black and white</p>
<h2>SYNOPSIS</h2>
<p> <code>pamthreshold</code> [<code>-simple</code>] [<code>-local=</code><i>width</i><code>x</code><i>height</i>] [<code>-dual=</code><i>width</i><code>x</code><i>height</i>] [<code>-threshold=</code><i>threshold</i>] [<code>-contrast=</code><i>threshold</i>] [<i>inputpamfile</i>] </p>
<p> Minimum unique abbreviations of options are acceptable. You may use double hyphens instead of a single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamthreshold</code> thresholds a grayscale image. Thresholding means dividing the image into background and foreground by comparing every pixel to a thresholding value. </p>
<p> The input should be a PGM image or a PAM image of tuple type GRAYSCALE or GRAYSCALE_ALPHA. However, pamthreshold doesn&#8217;t check; it just thresholds the first channel as if it were grayscale samples and if there is a second channel, processes it as if it is an alpha (transparency) channel. So if you feed it e.g. a PPM image, it will work but produce probably useless results. </p>
<p> The output is a PAM with tuple type BLACKANDWHITE or BLACKANDWHITE_ALPHA, depending on whether the input has an alpha channel. You can turn this into a PBM (if you need to use it with an older program that doesn&#8217;t understand PAM, or you can&#8217;t afford the 8X amount of space that PAM uses for the image) with <code>pamtopnm</code>. </p>
<p> The output is to Standard Output. </p>
<p> When the input has an alpha channel, <code>pamthreshold</code> includes an alpha channel in the output. Since the output has maxval 1, the alpha channel can indicate only fully transparent or fully opaque. <code>pamthreshold</code> make it fully transparent where the input is more than half transparent and fully opaque where it isn&#8217;t. </p>
<p> The alpha function was new in Netpbm 10.43 (June 2008). Before that, <code>pamthreshold</code> ignores any alpha channel in the input. </p>
<p> Another way to convert a grayscale image to black and white is to dither. Dithering is using clustered black and white pixels such that if you step back and look at the picture, you see varying levels of gray. <code>pamditherbw</code> does dithering. </p>
<h2>OPTIONS</h2>
<p> Without any options, <code>pamthreshold</code> uses a method based on the iterative algorithm found in the wikipedia article<br />
&nbsp;<wbr><i>Thresholding&nbsp;<wbr>(image processing)</i> to compute the thresholding value. ( this version of the Wikipedia article was current at the time of this writing). It uses this threshold to globally threshold the image. This should work well for most images. The program issues a message telling you what threshold it used. (Netpbm messages go to Standard Error, and you can turn them off with the Netpbm common option <code>-quiet</code>). </p>
<p> Options <code>-simple</code>, <code>-local</code>, and <code>-dual</code> select other methods. </p>
<dl>
<dt><code>-simple</code></p>
<dd> This selects simple or global thresholding, i.e. <code>pamthreshold</code> compares every pixel to the threshold you specify with <code>-threshold</code>. Those with a brightness greater than or equal to the threshold become white; others become black. This works well for black and white text pages scanned with a flatbed scanner and is faster than the default method that iteratively determines the thresholding value first. </p>
<dt><code>-local=</code><i>width</i><code>x</code><i>height</i></p>
<dd> This selects local adaptive thresholding (also known as dynamic thresholding) using the neighborhood which is the square <i>width</i> pixels wide and <i>height</i> pixels high centered on the pixel in question. <code>pamthreshold</code> computes the threshold individually for each pixel of the image. This can accommodate changing lighting conditions in the image. Depending on the size of the neighborhood this can be quite slow. </p>
<dt><code>-dual=</code><i>width</i><code>x</code><i>height</i></p>
<dd> This selects a dual thresholding algorithm using a global threshold for low contrast neighborhoods and local thresholding otherwise. This can preserve larger back- respectively foreground areas than local adaptive thresholding. This algorithm was proposed in the paper &quot;An Approach To Licence Plate Recognition&quot; by J.R. Parker and Pavol Federl. </p>
<dt><code>-threshold=</code><i>threshold</i></p>
<dd> This sets the thresholding value for simple or local thresholding. The value is a floating point number in the range [0, 1] directly proportional to the Netpbm sample values, where 0 corresponds to black and 1 to the maxval of the image. </p>
<p> If you don&#8217;t specify this option, <code>pamthreshold</code> uses a threshold of 0.5. </p>
<p> Without <code>-simple</code>, <code>-local</code>, or <code>-dual</code>, this option is meaningless. </p>
<p> The meaning of the threshold depends upon the kind of thresholding you do (as determined by other options). Roughly, pixels at least as bright as the threshold become white in the output while others become black. </p>
<dt><code>-contrast=</code><i>threshold</i></p>
<dd> This sets the threshold to determine if a neighborhood has low contrast or not for dual thresholding. The value is a floating point number in the range [0, 1]. </p>
<p> If you don&#8217;t specify this option, <code>pamthreshold</code> uses a contrast threshold of 0.05. Without <code>-dual</code> this option is meaningless. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamditherbw/">pamditherbw</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamthreshold</code> was new in Netpbm 10.34 (June 2006). </p>
<h2>AUTHOR</h2>
<p> <code>pamthreshold</code> is Copyright &#169; 2006 by Erik Auerswald and released under the <code><a href="/docs/linux/man/1-gpl/">GPL</a></code>(1) </p>
<h2>Index</h2>
