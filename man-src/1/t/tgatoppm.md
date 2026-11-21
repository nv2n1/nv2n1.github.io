---
title: "tgatoppm(1)"
name: "tgatoppm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tgatoppm/"
---


  </p>
<h2 class="name">NAME</h2>
<p> tgatoppm &#8211; convert TrueVision Targa file into a portable pixmap  </p>
<h2>SYNOPSIS</h2>
<p> <code>tgatoppm</code> [<code>--alphaout=</code>{<i>alpha-filename</i>,<code>-</code>}] [<code>--headerdump</code>] <i>tga-filename</i> </p>
<h2>DESCRIPTION</h2>
<p> Reads a TrueVision Targa file as input.   Produces a portable pixmap as output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--alphaout=</code><i>alpha-filename</i></dt>
<dd> <p> <code>tgatoppm </code> creates a PGM (portable graymap) file containing the alpha channel values in the input image. If the input image doesn&#8217;t contain an alpha channel, the <i>alpha-filename</i> file contains all zero (transparent) alpha values. If you don&#8217;t specify <code>--alphaout</code>, <code>tgatoppm</code> does not generate an alpha file, and if the input image has an alpha channel, <code>tgatoppm</code> simply discards it. </p>
<p> If you specify <code>-</code> as the filename, <code>tgatoppm</code> writes the alpha output to Standard Output and discards the image. </p>
<p> See <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1) for one way to use the alpha output file. </p>
 </dd>
<dt><code>--headerdump</code></dt>
<dd> <p> Causes the header information to be dumped to stderr. </p>
 </dd></dl>
<p> All options can be abbreviated to their shortest unique prefix.  </p>
<h2>BUGS</h2>
<p> Should really be in PNM, not PPM. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtotga/">ppmtotga</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)  </p>
<h2>AUTHOR</h2>
<p> Partially based on tga2rast, version 1.0, by Ian J. MacPhedran. </p>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
