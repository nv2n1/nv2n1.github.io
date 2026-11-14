---
title: "pamditherbw(1)"
name: "pamditherbw"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamditherbw/"
description: "pamditherbw – dither grayscale image to black and white"
---

<h2 class="name">NAME</h2>
<p> pamditherbw &#8211; dither grayscale image to black and white</p>
<h2>SYNOPSIS</h2>
<p> <code>pamditherbw</code> </p>
<p> [<code>-floyd</code> | <code>-fs</code> | <code>-atkinson</code> | <code>-threshold</code> | <code>-hilbert</code> | <code>-dither8</code> | <code>-d8</code> | <code>-cluster3</code> | <code>-c3</code> | <code>-cluster4</code> | <code>-c4</code> | <code>-cluster8</code> | <code>-c8</code>] </p>
<p> [<code>-value</code> <i>val</i>] </p>
<p> [<code>-clump</code> <i>size</i>] </p>
<p> [<code>-randomseed=</code><i>integer</i>] </p>
<p> [<i>pamfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamditherbw</code> dithers a grayscale image. Dithering means turning each shade of gray into a pattern of black and white pixels that, from a distance, look the same as the gray. </p>
<p> The input should be a PGM image or a PAM image of tuple type GRAYSCALE. However, <code>pamditherbw</code> doesn&#8217;t check, so if you feed it e.g. a PPM image, it will produce arbitrary results (actually, it just takes the first channel of whatever you give it and treats it as if it represented gray levels). </p>
<p> The output is a PAM with tuple type BLACKANDWHITE. You can turn this into a PBM (if you need to use it with an older program doesn&#8217;t understand PAM) with <code>pamtopnm</code>. </p>
<p> To do the opposite of dithering, you can usually just scale the image down and then back up again with <code>pamscale</code>, possibly smoothing or blurring the result with <code>pnmsmooth</code> or <code>pnmconvol</code>. Or use the special case program <code>pbmtopgm</code>. </p>
<p> To dither a color image (to reduce the number of pixel colors), use <code>ppmdither</code>. </p>
<p> Another way to convert a grayscale image to a black and white image is thresholding. Thresholding is simply replacing each grayscale pixel with a black or white pixel depending on whether its brightness is above or below a threshold. That threshold might vary. Simple thresholding is a degenerate case of dithering, so <code>pamditherbw</code> does very simple thresholding with its <code>-threshold</code> option. But <code>pamthreshold</code> does more sophisticated thresholding. </p>
<p> If all you want is to change a PGM image with maxval 1 to a PBM image, <code>pamtopnm</code> will do that. </p>
<h2>OPTIONS</h2>
<p> The default quantization method is boustrophedonic Floyd-Steinberg error diffusion (<code>-floyd</code> or <code>-fs</code>). </p>
<p> Also available are simple thresholding (<code>-threshold</code>); Bayer&#8217;s ordered dither (<code>-dither8</code>) with a 16&#215;16 matrix;<br />
&nbsp;<wbr>Atkinson ; and three different sizes of 45-degree clustered-dot dither (<code>-cluster3</code>, <code>-cluster4</code>, <code>-cluster8</code>). </p>
<p> A space filling curve halftoning method using the Hilbert curve is also available (<code>-hilbert</code>). </p>
<p> Floyd-Steinberg or Atkinson will almost always give the best looking results; however, looking good is not always what you want. For instance, you can use thresholding in a pipeline with the <code>pnmconvol</code>, for tasks such as edge and peak detection. And clustered-dot dithering gives a newspaper-ish look, a useful special effect. </p>
<p> Floyd-Steinberg is by far the more traditional, but<br />
&nbsp;<wbr>some claim Atkinson works better. </p>
<p> The Hilbert curve method is useful for processing images before display on devices that do not render individual pixels distinctly (like laser printers). This dithering method can give better results than the dithering usually done by the laser printers themselves. The <code>-clump</code> option alters the number of pixels in a clump. Typically a PGM image will have to be scaled to fit on a laser printer page (2400 x 3000 pixels for an A4 300 dpi page), and then dithered to a PBM image before being converted to a postscript file. A printing pipeline might look something like: </p>
<pre>
    pamscale -xysize 2400 3000 image.pgm | pamditherbw -hilbert |  \
      pamtopnm | pnmtops -scale 0.25 &gt; image.ps 
</pre>
<dl>
<dt><code>-value</code></p>
<dd> This option alters the thresholding value for Floyd-Steinberg, Atkinson, and simple thresholding. It should be a real number between 0 and 1. Above 0.5 means darker images; below 0.5 means lighter. </p>
<dt><code>-clump</code></p>
<dd> This option alters the number of pixels in a clump. This is usually an integer between 2 and 100 (default 5). Smaller clump sizes smear the image less and are less grainy, but seem to lose some grey scale linearity. </p>
<dt><code>-randomseed=</code><i>integer</i></p>
<dd> This is the seed for the random number generator that generates the pixels. </p>
<p> Use this to ensure you get the same image on separate invocations. </p>
<p> By default, <code>pgmnoise</code> uses a seed derived from the time of day and process ID, which gives you fairly uncorrelated results in multiple invocations. </p>
<p> This option was new in Netpbm 10.45 (December 2008). </p>
</dl>
<h2>REFERENCES</h2>
<p> The only reference you need for this stuff is &#8216;Digital Halftoning&#8217; by Robert Ulichney, MIT Press, ISBN 0-262-21009-6. </p>
<p> The Hilbert curve space filling method is taken from &#8216;Digital Halftoning with Space Filling Curves&#8217; by Luiz Velho, Computer Graphics Volume 25, Number 4, proceedings of SIGRAPH &#8217;91, page 81. ISBN 0-89791-436-8 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pgmtopgm/">pgmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtopgm/">pbmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pamthreshold/">pamthreshold</a></code>(1) , <code><a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a></code>(1) , <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) , <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamditherbw</code> was new in Netpbm 10.23 (July 2004), but is essentially the same program as <code>pgmtopbm</code> that has existed practically since the beginning. <code>pamditherbw</code> differs from its predecessor in that it properly adds brightnesses (using gamma transformations; <code>pgmtopbm</code> just adds them linearly) and that it accepts PAM input in addition to PGM and PBM and produces PAM output. </p>
<p> <code>pamditherbw</code> obsoletes <code>pgmtopbm</code>. </p>
<p> <code>-atkinson</code> was new in Netpbm 10.38 (March 2007). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
