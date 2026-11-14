---
title: "pgmtopbm(1)"
name: "pgmtopbm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtopbm/"
description: "pgmtopbm – convert a portable graymap into a portable bitmap"
---

<h2 class="name">NAME</h2>
<p> pgmtopbm &#8211; convert a portable graymap into a portable bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtopbm</code> [<code>-floyd</code>|<code>-fs</code>|<code>-threshold</code> |<code>-hilbert</code> |<code>-dither8</code>|<code>-d8</code>|<code>-cluster3</code> |<code>-c3</code>|<code>-cluster4</code>|<code>-c4</code> |<code>-cluster8</code>|<code>-c8</code>] [<code>-value</code> <i>val</i>] [<code>-clump</code> <i>size</i>] [<i>pgmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable graymap as input. Produces a portable bitmap as output. </p>
<p> Note that there is no pbmtopgm converter. Any program that uses the Netpbm libraries to read PGM files, including virtually all programs in the Netpbm package, will read a PBM file automatically as if it were a PGM file. </p>
<p> If you are using a less intelligent program that expects PGM input, use <code>pnmdepth</code> to convert the PBM file to PGM. As long as the depth is greater than 1, <code>pnmdepth</code> will generate PGM. This less intelligent program quite probably is also not intelligent enough to deal with general maxvals, so you should specify a depth of 255. </p>
<h2>OPTIONS</h2>
<p> The default quantization method is boustrophedonic Floyd-Steinberg error diffusion (<code>-floyd</code> or <code>-fs</code>). Also available are simple thresholding (<code>-threshold</code>); Bayer&#8217;s ordered dither (<code>-dither8</code>) with a 16&#215;16 matrix; and three different sizes of 45-degree clustered-dot dither (<code>-cluster3</code>, <code>-cluster4</code>, <code>-cluster8</code>). A space filling curve halftoning method using the Hilbert curve is also available. (<code>-hilbert</code>); </p>
<p> Floyd-Steinberg will almost always give the best looking results; however, looking good is not always what you want. For instance, thresholding can be used in a pipeline with the <i>pnmconvol</i> tool, for tasks like edge and peak detection. And clustered-dot dithering gives a newspaper-ish look, a useful special effect. </p>
<p> The <code>-value</code> flag alters the thresholding value for Floyd-Steinberg and simple thresholding. It should be a real number between 0 and 1. Above 0.5 means darker images; below 0.5 means lighter. </p>
<p> The Hilbert curve method is useful for processing images before display on devices that do not render individual pixels distinctly (like laser printers). This dithering method can give better results than the dithering usually done by the laser printers themselves. The <code>-clump</code> flag alters the number of pixels in a clump. This is usually an integer between 2 and 100 (default 5). Smaller clump sizes smear the image less and are less grainy, but seem to loose some grey scale linearity. Typically a PGM image will have to be scaled to fit on a laser printer page (2400 x 3000 pixels for an A4 300 dpi page), and then dithered to a PBM image before being converted to a postscript file. A printing pipeline might look something like: pnmscale -xysize 2400 3000 image.pgm | pgmtopbm -hil | pnmtops -scale 0.25 &gt; image.ps </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>REFERENCES</h2>
<p> The only reference you need for this stuff is &quot;Digital Halftoning&quot; by Robert Ulichney, MIT Press, ISBN 0-262-21009-6. </p>
<p> The Hilbert curve space filling method is taken from &quot;Digital Halftoning with Space Filling Curves&quot; by Luiz Velho, Computer Graphics Volume 25, Number 4, proceedings of SIGRAPH &#8217;91, page 81. ISBN 0-89791-436-8</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/5-pbm/">pbm</a>(5), <a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a>(1), <a href="/docs/linux/man/1-pnmscale/">pnmscale</a>(1), <a href="/docs/linux/man/1-pnmtops/">pnmtops</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
