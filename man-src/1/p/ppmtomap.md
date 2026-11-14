---
title: "ppmtomap(1)"
name: "ppmtomap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtomap/"
description: "ppmtomap – extract all colors from a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> ppmtomap &#8211; extract all colors from a portable pixmap</p>
<h2>DESCRIPTION</h2>
<p> This program exists only for backward compatibility. </p>
<p> Use <code>pnmcolormap</code>, which replaced it in January 2002. </p>
<p> One trivial difference between <code>ppmtomap</code> and <code>pnmcolormap all</code> is that if the input is PBM or PGM, <code>ppmtomap</code> would produce PPM output, whereas <code>pnmcolormap all</code> produces the same kind of output as the input. This should not be very noticeable, though, as PBM and PGM images are usually usable anywhere a PPM image is. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcolormap/">pnmcolormap</a></code>(1) </p>
<h2>Index</h2>
