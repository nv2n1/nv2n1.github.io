---
title: "ppmtorgb3(1)"
name: "ppmtorgb3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtorgb3/"
description: "ppmtorgb3 – separate a portable pixmap into three portable graymaps"
---

<h2 class="name">NAME</h2>
<p> ppmtorgb3 &#8211; separate a portable pixmap into three portable graymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtorgb3</code> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Writes three portable graymaps as output, one each for red, green, and blue. </p>
<p> The output filenames are constructed by taking the input filename, stripping off any extension, and appending &quot;.red&quot;, &quot;.grn&quot;, and &quot;.blu&quot;. For example, separating lenna.ppm would result in lenna.red, lenna.grn, and lenna.blu. If the input comes from stdin, the names are noname.red, noname.grn, and noname.blu.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rgb3toppm/">rgb3toppm</a>(1), <a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a>(1), <a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a>(1), <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
