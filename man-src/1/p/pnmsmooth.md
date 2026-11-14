---
title: "pnmsmooth(1)"
name: "pnmsmooth"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmsmooth/"
description: "pnmsmooth – smooth out an image"
---

<h2 class="name">NAME</h2>
<p> pnmsmooth &#8211; smooth out an image </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmsmooth</code> [<code>-size</code> <i>width</i> <i>height</i>] [<code>-dump</code> <i>dumpfile</i>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Smooths out an image by replacing each pixel with the average of its width X height neighbors. It is implemented as a C progam that generates a PGM convolution matrix and then invokes <i>pnmconvol</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-size width height</code></p>
<dd> Specifies the size of the convolution matrix. Default size is a 3&#215;3 matrix. Width and height sizes must be odd. Maximum size of convolution matrix is limited by the maximum value for a pixel such that (width * height * 2) must not exceed the maximum pixel value.</p>
<dt><code>-dump dumpfile</code></p>
<dd> Generates and saves the convolution file only. Use of this option does not invoke pnmconvol.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer.<br />
 Converted from script to C program December 1994 by Mike Burns (burns [at] chem.psu.edu). </p>
<h2>Index</h2>
