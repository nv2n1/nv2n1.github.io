---
title: "ppmtoppm(1)"
name: "ppmtoppm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoppm/"
description: "ppmtoppm – copy PPM image"
---

<h2 class="name">NAME</h2>
<p> ppmtoppm &#8211; copy PPM image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoppm</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>ppmtoppm</code> simply copies a PPM image from Standard Input to Standard Output. This may seem an unnecessary duplication of <code>cat</code>, but remember that a PPM program can read a PBM or PGM image, and the right kind of PAM, as if it were PPM. So <code>ppmtoppm</code> can read either a PBM, PGM, or PPM image and produce a PPM image as output. </p>
<p> Even that is of limited usefulness because of the fact that almost any program to which you would feed the resulting PPM image could also just take the original image directly. However, sometimes you really need a true PPM image. </p>
<p> When you know you have a PGM image and want a PPM image, <code>pgmtoppm</code> is a more general way to do that conversion. When you know you have a PBM image, use that and <code>pbmtopgm</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmtopgm/">pgmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopam/">pamtopam</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtopgm/">pbmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.9 (September 2002). </p>
<h2>Index</h2>
