---
title: "ppmtopjxl(1)"
name: "ppmtopjxl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtopjxl/"
description: "ppmtopjxl – convert a PPM image to an HP PaintJet XL PCL file"
---

<h2 class="name">NAME</h2>
<p> ppmtopjxl &#8211; convert a PPM image to an HP PaintJet XL PCL file</p>
<h2>SYNOPSIS</h2>
<p> ppmtopjxl [<code>-nopack</code>] [<code>-gamma</code> <i>n</i>] [<code>-presentation</code>] [<code>-dark</code>] [<code>-diffuse</code>] [<code>-cluster</code>] [<code>-dither</code>] [<code>-xshift</code> <i>s</i>] [<code>-yshift</code> <i>s</i>] [<code>-xshift</code> <i>s</i>] [<code>-yshift</code> <i>s</i>] [{<code>-xsize</code>|<code>-width</code>|<code>-xscale</code>} <i>s</i>] [{<code>-ysize</code>|<code>-height</code>|<code>-yscale</code>} <i>s</i>] [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmtopjxl</code> reads a PPM image as input and produces a PCL file suitable for printing on an HP PaintJet XL printer as output. </p>
<p> The generated file is not suitable for printing on a normal PrintJet printer. The <code>-nopack</code> option generates a file which does not use the normal TIFF 4.0 compression method. This file might be printable on a normal PaintJet printer (not an XL). </p>
<p> The <code>-gamma</code> option sets the gamma correction for the image. The useful range for the PaintJet XL is approximately 0.6 to 1.5. </p>
<p> You an alter the rendering algorithm used for images with the <code>-dither,</code> <code>-cluster,</code> and <code>-diffuse</code> options. These options select ordered dithering, clustered ordered dithering, or error diffusion respectively. You can use the <code>-dark</code> option to enhance images with a dark background when they are reduced in size. The <code>-presentation</code> option turns on presentation mode, in which two passes are made over the paper to increase ink density. You should use this only for images where quality is critical. </p>
<p> You can resize the image by setting the <code>-xsize</code> and <code>-ysize</code> options. The parameter to either of these options is interpreted as the number of dots to set the width or height to, but you may append an optional dimension of `<code>pt</code>&#8216; (points), `<code>dp</code>&#8216; (decipoints), `<code>in</code>&#8216; (inches), or `<code>cm</code>&#8216; (centimetres). If you specify only one dimension, <code>ppmtopjxl</code> will scale the other one appropriately. </p>
<p> The options <code>-width</code> and <code>-height</code> are synonyms of <code>-xsize</code> and <code>-ysize.</code> </p>
<p> You can alternatively use the <code>-xscale</code> and <code>-yscale</code> options to scale the image by a simple factor. </p>
<p> You can shift the image on the page with the <code>-xshift</code> and <code>-yshift</code> options. These move the image the specified dimensions right and down. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Angus Duggan </p>
<h2>Index</h2>
