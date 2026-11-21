---
title: "thumbnail(1)"
name: "thumbnail"
section: "1"
letter: "t"
url: "/docs/linux/man/1-thumbnail/"
---


 </p>
<h2>NAME</h2>
<p> thumbnail &#8211; create a <font SIZE="-1">TIFF</font> file with thumbnail images  </p>
<h2>SYNOPSIS</h2>
<p> <code>thumbnail</code> [ <i>options</i> ] <i>input.tif</i> <i>output.tif</i>  </p>
<h2>DESCRIPTION</h2>
<p> <i>thumbnail</i> is a program written to show how one might use the SubIFD tag (#330) to store thumbnail images. <i>thumbnail</i> copies a <font SIZE="-1">TIFF</font> Class F facsimile file to the output file and for each image an 8-bit greyscale <i>thumbnail sketch</i>. The output file contains the thumbnail image with the associated full-resolution page linked below with the SubIFD tag. </p>
<p> By default, thumbnail images are 216 pixels wide by 274 pixels high. Pixels are calculated by sampling and filtering the input image with each pixel value passed through a contrast curve.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code></dt>
<dd> <p> Specify the width of thumbnail images in pixels. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Specify the height of thumbnail images in pixels. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Specify a contrast curve to apply in generating the thumbnail images. By default pixels values are passed through a linear contrast curve that simply maps the pixel value ranges. Alternative curves are: <code>exp50</code> for a 50% exponential curve, <code>exp60</code> for a 60% exponential curve, <code>exp70</code> for a 70% exponential curve, <code>exp80</code> for a 80% exponential curve, <code>exp90</code> for a 90% exponential curve, <code>exp</code> for a pure exponential curve, <code>linear</code> for a linear curve. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> There are no options to control the format of the saved thumbnail images.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tiffdump/">tiffdump</a></code>(1), <code><a href="/docs/linux/man/1-tiffgt/">tiffgt</a></code>(1), <code><a href="/docs/linux/man/1-tiffinfo/">tiffinfo</a></code>(1), <code><a href="/docs/linux/man/3-libtiff/">libtiff</a></code>(3) </p>
<p> Libtiff library home page: <code><a rel="nofollow" href="http://www.remotesensing.org/libtiff/">http://www.remotesensing.org/libtiff/</a></code> </p>
