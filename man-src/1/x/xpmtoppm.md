---
title: "xpmtoppm(1)"
name: "xpmtoppm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpmtoppm/"
description: "xpmtoppm – convert an X11 pixmap into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> xpmtoppm &#8211; convert an X11 pixmap into a portable pixmap</p>
<h2>SYNOPSIS</h2>
<p> <code>xpmtoppm</code> [<code>&#8211;alphaout=</code>{<i>alpha-filename</i>,<code>&#8211;</code>}] [<code>-verbose</code>] [<i>xpmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads an X11 pixmap (XPM version 1 or 3) as input. Produces a PPM file as output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;alphaout=</code><i>alpha-filename</i></p>
<dd> <code>xpmtoppm </code> creates a PBM file containing the transparency mask for the image. If the input image doesn&#8217;t contain transparency information, the <i>alpha-filename</i> file contains all white (opaque) alpha values. If you don&#8217;t specify <code>&#8211;alphaout</code>, <code>xpmtoppm</code> does not generate an alpha file, and if the input image has transparency information, <code>xpmtoppm</code> simply discards it. </p>
<p> If you specify <code>&#8211;</code> as the filename, <code>xpmtoppm</code> writes the alpha output to Standard Output and discards the image. </p>
<p> See <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1) for one way to use the alpha output file.</p>
<dt><code>&#8211;verbose</code></p>
<dd> <code>xpmtoppm</code> prints information about its processing on Standard Error. </p>
</dl>
<h2>LIMITATIONS</h2>
<p> The support to XPM version 3 is limited. Comments can only be single lines and there must be for every pixel a default colorname for a color type visual. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtoxpm/">ppmtoxpm</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<p> Upgraded to support XPM version 3 by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Arnaud Le Hors&nbsp;(lehors [at] mirsa.inria.fr)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Tue Apr 9 1991 </p>
<h2>Index</h2>
