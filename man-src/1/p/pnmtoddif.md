---
title: "pnmtoddif(1)"
name: "pnmtoddif"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtoddif/"
description: "pnmtoddif – Convert a portable anymap to DDIF format"
---

<h2>Name</h2>
<p> pnmtoddif &#8211; Convert a portable anymap to DDIF format</p>
<h2>Syntax</h2>
<p> <code>pnmtoddif </code> pnmtoddif [-resolution x y] [pnmfile [ddiffile]]</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>resolution x y</i></p>
<dd> The horizontal and vertical resolution of the output image in dots per inch. Defaults to 78 dpi.</p>
<dt><i>pnmfile</i></p>
<dd> The filename for the image file in pnm format. If this argument is omitted, input is read from stdin.</p>
<dt><i>ddiffile</i></p>
<dd> The filename for the image file to be created in DDIF format. If this argument is omitted, the ddiffile is written to standard output. It can only specified if a pnmfile is also specified.</dl>
<h2>DESCRIPTION</h2>
<p> <tt>pnmtoddif</tt> takes a portable anymap from standard input and converts it into a DDIF image file on standard output or the specified DDIF file. </p>
<p> pbm format (bitmap) data is written as 1 bit DDIF, pgm format data (greyscale) as 8 bit greyscale DDIF, and ppm format data is written as 8,8,8 bit color DDIF. All DDIF image files are written as uncompressed. The data plane organization is interleaved by pixel. </p>
<p> In addition to the number of pixels in the width and height dimension, DDIF images also carry information about the size that the image should have, that is, the physical space that a pixel occupies. PBMPLUS images do not carry this information, hence it has to be externally supplied. The default of 78 dpi has the beneficial property of not causing a resize on most Digital Equipment Corporation color monitors.</p>
<h2>AUTHOR</h2>
<p> Burkhard Neidecker-Lutz<br />
 Digital Equipment Corporation, CEC Karlsruhe<br />
 neideck [at] nestvx.enet.dec.com </p>
<h2>Index</h2>
