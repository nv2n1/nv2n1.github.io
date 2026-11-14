---
title: "ximtoppm(1)"
name: "ximtoppm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-ximtoppm/"
description: "ximtoppm – convert an Xim file into a portable pixmap"
---

<h2 class="name">NAME</h2>
<p> ximtoppm &#8211; convert an Xim file into a portable pixmap </p>
<h2>SYNOPSIS</h2>
<p> <code>ximtoppm</code> [<code>&#8211;alphaout=</code>{<i>alpha-filename</i>,<code>&#8211;</code>}] [<i>ximfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads an Xim file as input. Produces a portable pixmap as output. The Xim toolkit is included in the contrib tree of the X.V11R4 release.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;alphaout=</code><i>alpha-filename</i></p>
<dd> <code>ximtoppm </code> creates a PGM (portable graymap) file containing the alpha channel values in the input image. If the input image doesn&#8217;t contain an alpha channel, the <i>alpha-filename</i> file contains all zero (transparent) alpha values. If you don&#8217;t specify <code>&#8211;alphaout</code>, <code>ximtoppm</code> does not generate an alpha file, and if the input image has an alpha channel, <code>ximtoppm</code> simply discards it. </p>
<p> If you specify <code>&#8211;</code> as the filename, <code>ximtoppm</code> writes the alpha output to Standard Output and discards the image. </p>
<p> Actually, an Xim image can contain an arbitrary fourth channel &#8212; it need not be an Alpha channel. <code>ximtoppm</code> extracts any fourth channel it finds as described above; it doesn&#8217;t matter if it is an alpha channel or not. </p>
<p> See <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1) for one way to use the alpha output file. </p>
</dl>
<p> All options can be abbreviated to their shortest unique prefix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
