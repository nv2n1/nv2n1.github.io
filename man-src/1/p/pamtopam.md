---
title: "pamtopam(1)"
name: "pamtopam"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtopam/"
description: "pamtopam – copy PAM image"
---

<h2 class="name">NAME</h2>
<p> pamtopam &#8211; copy PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtopam</code> </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtopam</code> simply copies a PAM image from Standard Input to Standard Output. This may seem an unnecessary duplication of <code>cat</code>, but remember that a PAM program can read a PBM, PGM, or PPM image as if it were PAM. So <code>pamtopam</code> can read either a PBM, PGM, PPM, or PAM image and produce a PAM image as output. </p>
<p> Even that is of limited usefulness because of the fact that almost any program to which you would feed the resulting PAM image could also just take the original image directly. However, sometimes you really want a true PAM image. </p>
<p> You can do a more general job of translating PAM/PNM to PAM with <code>pamchannel</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtopnm/">pamtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtoppm/">ppmtoppm</a></code>(1) , <code><a href="/docs/linux/man/1-pgmtopgm/">pgmtopgm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.41 (December 2007). </p>
<h2>Index</h2>
