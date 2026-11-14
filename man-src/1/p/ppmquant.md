---
title: "ppmquant(1)"
name: "ppmquant"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmquant/"
description: "ppmquant – quantize the colors in a portable pixmap down to a specified number"
---

<h2 class="name">NAME</h2>
<p> ppmquant &#8211; quantize the colors in a portable pixmap down to a specified number </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmquant</code> [<code>-floyd</code>|<code>-fs</code>] <i>ncolors</i> [<i>ppmfile</i>]<br />
 <code>ppmquant</code> [<code>-floyd</code>|<code>-fs</code>] [<code>-nofloyd</code>|<code>-nofs</code>] <code>-mapfile</code> <i>mapfile</i> [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmquant </code> is a newer, more general program that is backward compatible with <code>ppmquant</code>. <code>ppmquant</code> may be faster, though. </p>
<p> Reads a PPM image as input. Chooses <i>ncolors</i> colors to best represent the image, maps the existing colors to the new ones, and writes a PPM image as output. </p>
<p> The quantization method is Heckbert&#8217;s &quot;median cut&quot;. </p>
<p> Alternately, you can skip the color-choosing step by specifying your own set of colors with the <code>-mapfile</code> option. The <i>mapfile</i> is just a <i>ppm</i> file; it can be any shape, all that matters is the colors in it. For instance, to quantize down to the 8-color IBM TTL color set, you might use: </p>
<pre>
    P3
    8 1
    255
      0   0   0
    255   0   0
      0 255   0
      0   0 255
    255 255   0
    255   0 255
      0 255 255
    255 255 255
</pre>
<p> If you want to quantize one image to use the colors in another one, just use the second one as the mapfile. You don&#8217;t have to reduce it down to only one pixel of each color, just use it as is. </p>
<p> If you use a mapfile, the output image has the same maxval as the mapfile. Otherwise, the output maxval is the same as the input maxval, or less in some cases where the quantization process reduces the necessary resolution. </p>
<p> The <code>-floyd</code>/<code>-fs</code> option enables a Floyd-Steinberg error diffusion step. Floyd-Steinberg gives vastly better results on images where the unmodified quantization has banding or other artifacts, especially when going to a small number of colors such as the above IBM set. However, it does take substantially more CPU time, so the default is off. </p>
<p> <code>-nofloyd</code>/<code>-nofs</code> means not to use the Floyd-Steinberg error diffusion. This is the default. </p>
<h2>REFERENCES</h2>
<p> &quot;Color Image Quantization for Frame Buffer Display&quot; by Paul Heckbert, SIGGRAPH &#8217;82 Proceedings, page 297. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmquant/">pnmquant</a></code>(1), <code><a href="/docs/linux/man/1-ppmquantall/">ppmquantall</a></code>(1), <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-ppmdither/">ppmdither</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
