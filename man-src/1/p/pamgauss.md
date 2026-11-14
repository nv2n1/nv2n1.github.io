---
title: "pamgauss(1)"
name: "pamgauss"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamgauss/"
description: "pamgauss – create a two dimensional gaussian function as a PAM image"
---

<h2 class="name">NAME</h2>
<p> pamgauss &#8211; create a two dimensional gaussian function as a PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamgauss</code> <i>width</i> <i>height</i> <code>-sigma=</code><i>number</i> [<code>-maxval=</code><i>number</i>] [<code>-tupletype=</code><i>string</i>] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>EXAMPLES</h2>
<pre>
     pamgauss 3 3 -sigma=.5 -tupletype=GRAYSCALE | pamtopnm &gt;gauss.pgm
     pnmconvol -nooffset gauss.pgm myimage.ppm &gt;blurred.ppm
</pre>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamgauss</code> generates a one-plane PAM image whose samples are a gaussian function of their distance from the center of the image. I.e. the sample value is highest in the center and goes down, in a bell curve shape, as you move away from the center. </p>
<p> The values are scaled so that the volume under the surface of the two-dimensional Gaussian function is the maxval of the image. </p>
<p> You can use this image as a convolution kernel with <code>pnmconvol</code> to blur an image. (This technique is known as Gaussian blurring). </p>
<p> <i>width</i> and <i>height</i> are the dimensions of the image that <code>pamgauss</code> generates. Mathematically speaking, they are the domain of the two dimensional gaussian function. </p>
<p> The sum of all the samples is equal to the image&#8217;s maxval (within rounding error). This is true even if you clip the Gaussian function by making the image too small. If you want to be sure you get a whole Gaussian function, make sure that you choose a sigma and image dimensions so that if you made it any larger, the sample values at the edges would be zero. </p>
<p> The output image is PAM. To make it usable with <code>pnmconvol</code>, specify <code>-tupletype=GRAYSCALE</code> so <code>pnmconvol</code> can use it as if it were PGM. You must use the <code>-nooffset</code> option on <code>pnmconvol</code> because zero means zero in the PAM that <code>pamgauss</code> generates. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-sigma=</code><i>number</i></p>
<dd> This is the sigma parameter of the Gaussian function (if it were a Gaussian probability function, this would be its standard deviation). The higher the number, the more spread out the function is. Normally, you want to make this number low enough that the function reaches zero value before the edge of your image. </p>
<p> <i>number</i> is in units of pixels. </p>
<p> This option is required. There is no default. </p>
<dt><code>-maxval=</code><i>number</i></p>
<dd> This is the maxval for the output image. It defaults to 255. </p>
<dt><code>-tupletype=</code><i>string</i></p>
<dd> This is the value of the &quot;tuple_type&quot; attribute of the created PAM image. It can be any string up to 255 characters. If you don&#8217;t specify this, <code>pamgauss</code> generates a PAM with unspecified tuple type. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pgmkernel/">pgmkernel</a></code>(1) , <code><a href="/docs/linux/man/1-pamseq/">pamseq</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamgauss</code> was new in Netpbm 10.23 (July 2004). </p>
<h2>Index</h2>
