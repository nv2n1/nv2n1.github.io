---
title: "diffimg(1)"
name: "diffimg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diffimg/"
description: "diffimg – Calculates intersection between two images"
---

<h2 class="name">NAME</h2>
<p> diffimg &#8211; Calculates intersection between two images </p>
<h2>SYNOPSIS</h2>
<p> <code>diffimg</code> image1 image2 [<i>outimage</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>diffimg</code> generates an image where each pixel is the difference between the corresponding pixel in each of the two source images. Thus, if the source images are the same the resulting image will be black, otherwise it will have regions of non-black where the images differ. </p>
<p> Currently supports: .png, .gif, .jpg, and .ps by using ghostscript</p>
<h2>AUTHOR</h2>
<p> diffimg was written by John Ellson &lt;ellson [at] research.att.com&gt; </p>
<p> This manual page was written by David Claughton &lt;dave [at] eclecticdave.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
