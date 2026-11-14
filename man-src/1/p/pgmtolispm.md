---
title: "pgmtolispm(1)"
name: "pgmtolispm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtolispm/"
description: "pgmtolispm – convert a portable graymap into Lisp Machine format"
---

<h2 class="name">NAME</h2>
<p> pgmtolispm &#8211; convert a portable graymap into Lisp Machine format </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtolispm</code> [<i>pgmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable graymap as input. Produces a Lisp Machine bitmap as output. </p>
<p> This is the file format read by the tv:read-bit-array-file function on TI Explorer and Symbolics lisp machines. </p>
<p> Given a pgm (instead of a pbm) a multi-plane image will be output. This is probably not useful unless you have a color lisp machine. </p>
<p> Multi-plane bitmaps on lisp machines are color; but the lispm image file format does not include a color map, so we must treat it as a graymap instead. This is unfortunate.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lispmtopgm/">lispmtopgm</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>BUGS</h2>
<p> Output width is always rounded up to the nearest multiple of 32; this might not always be what you want, but it probably is (arrays which are not modulo 32 cannot be passed to the Lispm BITBLT function, and thus cannot easily be displayed on the screen). </p>
<p> No color.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jamie Zawinski and Jef Poskanzer. </p>
<h2>Index</h2>
