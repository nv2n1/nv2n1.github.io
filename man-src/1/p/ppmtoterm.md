---
title: "ppmtoterm(1)"
name: "ppmtoterm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoterm/"
description: "ppmtoterm – convert a PPM image to a ANSI ISO 6429 ascii image"
---

<h2 class="name">NAME</h2>
<p> ppmtoterm &#8211; convert a PPM image to a ANSI ISO 6429 ascii image</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoterm</code> </p>
<p> [<i>ppmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> This program tries to produce an accurate representation of a PPM image on an terminal that implements the ANSI ISO 6429 standard. It approximates colors, finding the minimum Cartesian distance between the input RGB vectors and the ones in the generated palette. As the available color palette is somewhat restricted, you get the best results when the colors in the original image are few and the RGB intensities are close to zero, half of maximum, and maximum. </p>
<p> You can usually get good results with cartoons or images with plain colors (no gradients). With photos, results can vary, but are usually not very accurate. </p>
<p> The output image has one line for each row and one character for each column of the input image. E.g. an 80 pixel by 25 pixel PPM image would fill up an 80&#215;25 terminal screen. Use <code>pamscale</code> or <code>pamcut</code> to make your image fit properly on your screen. </p>
<p> Furthermore, use <code>pamscale</code> to recover the proper aspect ratio, because a character on a terminal screen is rarely square. Typically, a character is twice has high as it is wide, so in order for a 20&#215;20 image to appear square on your terminal, as it should, you&#8217;ll want to squash it vertically or stretch it horizontally by a factor of two (resulting int 10&#215;20 characters are 20&#215;40 characters). </p>
<p> The image starts at the current cursor position on the terminal screen. Each successive row starts at Column 0 on the screen. If you want to shift the image up or down, for example to center it, use <code>pnmpad</code> on the input. </p>
<p> This program was born with the objective of displaying nice color images on the Linux console, e.g. a proper logo at Linux boot. </p>
<p> <code>pbmto4425</code> does a similar thing for black and white images, using line drawing characters, on some terminals. </p>
<h2>OPTIONS</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamscale/">pamscale</a></code>(1) , <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtoascii/">pbmtoascii</a></code>(1) , <code><a href="/docs/linux/man/1-pbmto4425/">pbmto4425</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002 by Ero Carrera. </p>
<h2>HISTORY</h2>
<p> This program was new in Netpbm 10.9 (August 2002). </p>
<h2>Index</h2>
