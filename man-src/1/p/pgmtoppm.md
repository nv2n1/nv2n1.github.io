---
title: "pgmtoppm(1)"
name: "pgmtoppm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtoppm/"
description: "pgmtoppm – colorize a portable graymap into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> pgmtoppm &#8211; colorize a portable graymap into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtoppm</code> <i>colorspec</i> [<i>pgmfile</i>]<br />
 <code>pgmtoppm</code> <i>colorspec1</i><code>&#8211;</code><i>colorspec2</i> [<i>pgmfile</i>]<br />
 <code>pgmtoppm -map</code> <i>mapfile</i> [<i>pgmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PGM as input. Produces a PPM file as output with a specific color assigned to each gray value in the input. </p>
<p> If you specify one color argument, black in the pgm file stays black and white in the pgm file turns into the specified color in the ppm file. Gray values in between are linearly mapped to differing intensities of the specified color. </p>
<p> If you specify two color arguments (separated by a dash), then black gets mapped to the first color and white gets mapped to the second and gray values in between get mapped linearly (across a three dimensional space) to colors in between. </p>
<p> You can specify the color in one of five ways:</p>
<dl>
<dt>o</p>
<dd> A name, from an X11-style color names file.</p>
<dt>o</p>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</p>
<dt>o</p>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</p>
<dt>o</p>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</p>
<dt>o</p>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.)</dl>
<p> Also, you can specify an entire colormap with the <code>-map</code> option. The mapfile is just a <code>ppm</code> file; it can be any shape, all that matters is the colors in it and their order. In this case, black gets mapped into the first color in the map file, and white gets mapped to the last and gray values in between are mapped linearly onto the sequence of colors in between. </p>
<h2>NOTE &#8211; MAXVAL</h2>
<p> The &quot;maxval,&quot; or depth, of the output image is the same as that of the input image. The maxval affects the color resolution, which may cause quantization errors you don&#8217;t anticipate in your output. For example, you have a simple black and white image (in fact, let&#8217;s say it&#8217;s a PBM file, since <code>pgmtoppm</code>, like all Netpbm programs, can accept a PBM file as if it were PGM. The maxval of this image is 1, because only two gray values are needed: black and white. Run this image through <code>pgmtoppm 0f/00/00</code> to try to make the image black and faint red. Because the output image will also have maxval 1, there is no such thing as faint red. It has to be either full-on red or black. <code>pgmtoppm</code> rounds the color 0f/00/00 down to black, and you get an output image that is nothing but black. </p>
<p> The fix is easy: Pass the input through <code>pnmdepth</code> on the way into <code>pgmtoppm</code> to increase its depth to something that would give you the resolution you need to get your desired color. In this case, <code>pnmdepth 16</code> would do it. Or spare yourself the unnecessary thinking and just say <code>pnmdepth 255 .</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmdepth/">pnmdepth</a></code>(1), <code><a href="/docs/linux/man/1-rgb3toppm/">rgb3toppm</a></code>(1), <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1), <code><a href="/docs/linux/man/1-ppmtorgb3/">ppmtorgb3</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
