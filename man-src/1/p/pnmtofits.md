---
title: "pnmtofits(1)"
name: "pnmtofits"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtofits/"
description: "pnmtofits – convert a portable anymap into FITS format"
---

<h2 class="name">NAME</h2>
<p> pnmtofits &#8211; convert a portable anymap into FITS format </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtofits</code> [<code>-max</code> <i>f</i>] [<code>-min</code> <i>f</i>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Produces a FITS (Flexible Image Transport System) file as output. The resolution of the output file is either 8 bits/pixel, or 16 bits/pixel, depending on the value of maxval in the input file. If the input file is a portable bitmap or a portable graymap, the output file consists of a single plane image (NAXIS = 2). If instead the input file is a portable pixmap, the output file will consist of a three-plane image (NAXIS = 3, NAXIS3 = 3). A full description of the FITS format can be found in Astronomy &amp; Astrophysics Supplement Series 44 (1981), page 363.</p>
<h2>OPTIONS</h2>
<p> Flags <code>-min</code> and <code>-max</code> can be used to set DATAMAX, DATAMIN, BSCALE and BZERO in the FITS header, but do not cause the data to be rescaled.</p>
<h2>BUGS</h2>
<p> FITS uses signed data, and this program outputs unsigned values. If you run into this problem, you might use &quot;-min 32768&quot;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fitstopnm/">fitstopnm</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Wilson H. Bent (whb [at] hoh-2.att.com), with modifications by Alberto Accomazzi (alberto [at] cfa.harvard.edu). </p>
<h2>Index</h2>
