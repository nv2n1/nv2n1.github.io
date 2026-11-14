---
title: "ppmspread(1)"
name: "ppmspread"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmspread/"
---

<h2 class="name">NAME</h2>
 

 ppmspread - displace a portable pixmap's pixels by a random amount 

<h2>SYNOPSIS</h2>

 ppmspread <i>amount</i> [<i>ppmfile</i>]

<h2>DESCRIPTION</h2>

 Reads a portable pixmap as input. Moves every pixel around a bit relative to its original position. amount determines by how many pixels a pixel is to be moved around at most. 

 Pictures processed with this filter will seem to be somewhat dissolved or unfocussed (although they appear more coarse than images processed by something like <i>pnmconvol</i> ).

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-ppm/">ppm</a>(5), <a HREF="/docs/linux/man/1-pnmconvol/">pnmconvol</a>(1)

<h2>AUTHOR</h2>

 Copyright (C) 1993 by Frank Neumann 

<h2>Index</h2>


