---
title: "ppmtosixel(1)"
name: "ppmtosixel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtosixel/"
description: "ppmtosixel – convert a portable pixmap into DEC sixel format"
---

<h2 class="name">NAME</h2>
<p> ppmtosixel &#8211; convert a portable pixmap into DEC sixel format </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtosixel</code> [<code>-raw</code>] [<code>-margin</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces sixel commands (SIX) as output. The output is formatted for color printing, e.g. for a DEC LJ250 color inkjet printer. </p>
<p> If RGB values from the PPM file do not have maxval=100, the RGB values are rescaled. A printer control header and a color assignment table begin the SIX file. Image data is written in a compressed format by default. A printer control footer ends the image file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-raw</code></p>
<dd> If specified, each pixel will be explicitly described in the image file. If <code>-raw</code> is not specified, output will default to compressed format in which identical adjacent pixels are replaced by &quot;repeat pixel&quot; commands. A raw file is often an order of magnitude larger than a compressed file and prints much slower.</p>
<dt><code>-margin</code></p>
<dd> If <code>-margin</code> is not specified, the image will be start at the left margin (of the window, paper, or whatever). If <code>-margin</code> is specified, a 1.5 inch left margin will offset the image.</dl>
<h2>PRINTING</h2>
<p> Generally, sixel files must reach the printer unfiltered. Use the lpr -x option or cat filename &gt; /dev/tty0?.</p>
<h2>BUGS</h2>
<p> Upon rescaling, truncation of the least significant bits of RGB values may result in poor color conversion. If the original PPM maxval was greater than 100, rescaling also reduces the image depth. While the actual RGB values from the ppm file are more or less retained, the color palette of the LJ250 may not match the colors on your screen. This seems to be a printer limitation.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Rick Vinci. </p>
<h2>Index</h2>
