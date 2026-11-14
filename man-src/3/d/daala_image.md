---
title: "daala_image(3)"
name: "daala_image"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daala_image/"
description: "daala_image –"
---

<h2 class="name">NAME</h2>
<p> daala_image &#8211; </p>
<p> Representation of an image or video frame.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;codec.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>daala_image_plane</code> <code>planes</code> [<code>OD_NPLANES_MAX</code>]<br />
 <i>Typical 3 planes for Y, Cb, and Cr. </i><br />
 int <code>nplanes</code><br />
 <i>Number of planes (1 for greyscale, 3 for YCbCr, 4 for YCbCr+Alpha ) </i><br />
 int32_t <code>width</code><br />
 <i>Width and height in pixels. </i><br />
 int32_t <code>height</code> </p>
<h2>Detailed Description</h2>
<p> Representation of an image or video frame. </p>
<h2>Field Documentation</h2>
<h3><code>daala_image_plane</code> daala_image::planes[<code>OD_NPLANES_MAX</code>]</h3>
<p> Typical 3 planes for Y, Cb, and Cr. Can have a 4th plane for alpha </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
