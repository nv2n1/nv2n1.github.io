---
title: "pbmtopgm(1)"
name: "pbmtopgm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtopgm/"
description: "pbmtopgm – convert portable bitmap to portable graymap by averaging areas"
---

<h2 class="name">NAME</h2>
<p> pbmtopgm &#8211; convert portable bitmap to portable graymap by averaging areas</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtopgm </code> <i>width</i> <i>height</i> [<i>pbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pbmtopgm</code> reads a portable bitmap as input. It outputs a portable graymap in which each pixel&#8217;s gray level is the average the surrounding black and white input pixels. The surrounding area is a rectangle of <i>width</i> by <i>height</i> pixels. </p>
<p> In other words, this is a convolution. <code>pbmtopgm </code> is similar to a special case of <code>pnmconvol</code>. </p>
<p> You may need a <code>ppmsmooth</code> step after <code>pbmtopgm</code>. </p>
<p> <code>pbmtopgm </code> has the effect of anti-aliasing bitmaps which contain distinct line features. </p>
<p> <code>pbmtopgm </code> works best with odd sample width and heights. </p>
<p> You don&#8217;t need <code>pbmtopgm</code> just to use a PGM program on a PBM image. Any PGM program (assuming it uses the Netpbm libraries to read the PGM input) takes PBM input as if it were PGM, with only the mininum and maximum gray levels. So unless your convolution rectangle is bigger than one pixel, you&#8217;re not gaining anything with a <code>pbmtopgm</code> step. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-netpbm/">netpbm</a></code>(1), <code><a href="/docs/linux/man/1-pgmtopbm/">pgmtopbm</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Angus Duggan Copyright (C) 1989 by Jef Poskanzer. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty. </p>
<h2>Index</h2>
