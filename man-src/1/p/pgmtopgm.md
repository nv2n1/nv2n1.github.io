---
title: "pgmtopgm(1)"
name: "pgmtopgm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmtopgm/"
description: "pgmtopgm – copy PGM image"
---

<h2 class="name">NAME</h2>
<p> pgmtopgm &#8211; copy PGM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmtopgm</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmtopgm</code> simply copies a PGM image from Standard Input to Standard Output. This may seem an unnecessary duplication of <code>cat</code>, but remember that a PGM program can read a PBM image as if it were PGM. So <code>pgmtopgm</code> can read either a PBM or PGM image and produce a PGM image as output. </p>
<p> Even that is of limited usefulness because of the fact that almost any program to which you would feed the resulting PGM image could also just take the original image directly. However, sometimes you really need a true PGM image. </p>
<p> When you know you have a PBM image and want a PGM image, <code>pbmtopgm</code> is a more general way to do that conversion. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtoppm/">ppmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopam/">pamtopam</a></code>(1) , <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtopgm/">pbmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.9 (September 2002). </p>
<h2>Index</h2>
