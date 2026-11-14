---
title: "fitstopnm(1)"
name: "fitstopnm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fitstopnm/"
description: "fitstopnm – convert a FITS file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> fitstopnm &#8211; convert a FITS file into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>fitstopnm</code> [<code>-image</code> <i>N</i>] [<code>-noraw</code>] [<code>-scanmax</code>] [<code>-printmax</code>] [<code>-min</code> <i>f</i>] [<code>-max</code> <i>f</i>] [<i>FITSfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a FITS file as input. Produces a portable pixmap if the FITS file consists of 3 image planes (NAXIS = 3 and NAXIS3 = 3), a portable graymap if the FITS file consists of 2 image planes (NAXIS = 2), or whenever the <code>-image </code> flag is specified. The results may need to be flipped top for bottom; if so, just pipe the output through <code>pnmflip -tb.</code></p>
<h2>OPTIONS</h2>
<p> The <code>-image</code> option is for FITS files with three axes. The assumption is that the third axis is for multiple images, and this option lets you select which one you want. </p>
<p> Flags <code>-min</code> and <code>-max </code> can be used to override the min and max values as read from the FITS header or the image data if no DATAMIN and DATAMAX keywords are found. Flag <code>-scanmax</code> can be used to force the program to scan the data even when DATAMIN and DATAMAX are found in the header. If <code>-printmax </code> is specified, the program will just print the min and max values and quit. Flag <code>-noraw</code> can be used to force the program to produce an ASCII portable anymap. </p>
<p> The program will tell what kind of anymap is writing. All flags can be abbreviated to their shortest unique prefix.</p>
<h2>REFERENCES</h2>
<p> FITS stands for Flexible Image Transport System. A full description can be found in Astronomy &amp; Astrophysics Supplement Series 44 (1981), page 363.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmtofits/">pnmtofits</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/1-pnmflip/">pnmflip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer, with modifications by Daniel Briggs (dbriggs [at] nrao.edu) and Alberto Accomazzi (alberto [at] cfa.harvard.edu). </p>
<h2>Index</h2>
