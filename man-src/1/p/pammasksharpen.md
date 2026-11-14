---
title: "pammasksharpen(1)"
name: "pammasksharpen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pammasksharpen/"
description: "pammasksharpen – Sharpen an image via an unsharp mask"
---

<h2 class="name">NAME</h2>
<p> pammasksharpen &#8211; Sharpen an image via an unsharp mask</p>
<h2>SYNOPSIS</h2>
<p> <code>pammasksharpen</code> [<code>-sharpness=</code><i>realnum</i>] [<code>-threshold=</code><i>realnum</i>] <i>maskfile</i> [<i>inputfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>EXAMPLES</h2>
<pre>
   pamgauss 5 5 -sigma=.7 -tupletype=GRAYSCALE | pamtopnm &gt;gauss.pgm
   pnmconvol -nooffset gauss.pgm myimage.ppm &gt;blurred.ppm
   pammasksharpen blurred.ppm myimage.ppm &gt;sharpened.ppm
</pre>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pammasksharpen</code> reads a Netpbm image as input and produces a sharpened version of it, in the same format, as output. It does this via an unsharp mask, which you supply as another Netpbm image. </p>
<p> An unsharp mask is generally a blurred version of the original image. The sharpening computation is this: Calculate the &#8216;edgeness&#8217; of a sample in the input image as the signed difference between the sample value and the corresponding sample in the unsharp mask. This tells how different the pixel is from its neighbors. Add a multiple of the edgeness to the original sample to get the corresponding output sample. Clip as necessary. This causes pixels that are brighter than their neighbors to get even brighter, while pixels that are dimmer than their neighbors get even dimmer. This makes edges &#8212; places where pixel values change quickly in space &#8212; stand out more. </p>
<p> The unsharp mask must be the same dimensions and have the same maxval as the input image. </p>
<h3>The Unsharp Mask</h3>
<p> You usually create the unsharp mask as a Gaussian blur of the original image, which you can do using <code>pamgauss</code> and <code>pnmconvol</code> as in the example above. The convolution kernel you use with <code>pnmconvol</code> is normally a square with side length an odd number of pixels. </p>
<p> When you create an unsharp mask like this, you will have to choose the side length of the convolution kernel. That length implements the parameter of unsharp mask sharpening usually known as &#8216;radius.&#8217; In particular, a radius of R pixels corresponds to a convolution kernel 2R+1 pixels on a side. </p>
<p> Radius is a very important parameter; you can ruin an image with a radius too large. You can safely use the highest radius with an inanimate object, while a human face demands the least. Landscapes fall in between. But it really depends on the size of the details. Fine detail needs a smaller radius, or else you may obliterate tiny detail of the same size as the Radius width. A large image often has larger detail (more pixels involved), so can use a larger radius. Radius and sharpness (see <code>-sharpness</code> option) interact: reducing one allows you to increase the other. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-sharpness=</code><i>realnum</i></p>
<dd> This specifies the magnitude of the sharpening. It is the multiple of edgeness that gets added to each sample as described above. </p>
<p> <i>realnum</i> is a nonnegative real decimal number. Zero means no sharpening at all. </p>
<p> This parameter is known as &#8216;amount&#8217; in ImageMagick. </p>
<p> The default is 1.0. </p>
<p> This option was new in Netpbm 10.30 (October 2005). Before that, the sharpness was always 1.0. </p>
<dt><code>-threshold=</code><i>realnum</i></p>
<dd> This minimum amount of edgeness that will be considered edgeness at all. i.e. if the magnitude of the edgeness is less than this, <code>pammasksharpen</code> will treat the edgeness as zero. </p>
<p> A nonzero value may be necessary here to avoid speckling in smooth areas. </p>
<p> This is a fraction of the maxval (so it is in the range [0, 1.0]). </p>
<p> The default is 0. </p>
<p> This option was new in Netpbm 10.34 (June 2006). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) , <code><a href="/docs/linux/man/1-pamedge/">pamedge</a></code>(1) , <code><a href="/docs/linux/man/1-pamsharpness/">pamsharpness</a></code>(1) , <code><a href="/docs/linux/man/1-pamsharpmap/">pamsharpmap</a></code>(1) , <code><a href="/docs/linux/man/1-pamarith/">pamarith</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pammasksharpen</code> was new in Netpbm 10.23 (July 2004). </p>
<h2>Index</h2>
