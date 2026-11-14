---
title: "ppmqvga(1)"
name: "ppmqvga"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmqvga/"
description: "ppmqvga – 8 plane quantization"
---

<h2 class="name">NAME</h2>
<p> ppmqvga &#8211; 8 plane quantization </p>
<h2>SYNOPSIS</h2>
<p> ppmqvga [ options ] [ input file ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ppmqvga</code> quantizes PPM files to 8 planes, with optional Floyd-Steinberg dithering. Input is a PPM file from the file named, or standard input of no file is provided.</p>
<h3>Options</h3>
<p> <code>-d</code> dither. Apply Floyd-Steinberg dithering to the data </p>
<p> <code>-q</code> quiet. Produces no progress reporting, and no terminal output unless and error occurs. </p>
<p> <code>-v</code> verbose. Produces additional output describing the number of colors found, and some information on the resulting mapping. May be repeated to generate loads of internal table output, but generally only useful once.</p>
<h2>EXAMPLES</h2>
<p> ppmqvga -d my_image.ppm | ppmtogif &gt;my_image.gif </p>
<p> tgatoppm zombie.tga | ppmqvga | ppmtotif &gt; zombie.tif</p>
<h2>SEE ALSO</h2>
<p> ppmquant</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages if problems, various levels of optional progress reporting.</p>
<h2>LIMITATIONS</h2>
<p> none known.</p>
<h2>AUTHOR</h2>
<p> Original by Lyle Rains (lrains [at] netcom.com) as ppmq256 and ppmq256fs combined, documented, and enhanced by Bill Davidsen (davidsen [at] crd.ge.com)</p>
<h2>Copyright</h2>
<p> Copyright 1991,1992 by Bill Davidsen, all rights reserved. The program and documentation may be freely distributed by anyone in source or binary format. Please clearly note any changes. </p>
<h2>Index</h2>
