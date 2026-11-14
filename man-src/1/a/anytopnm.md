---
title: "anytopnm(1)"
name: "anytopnm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anytopnm/"
description: "anytopnm – attempt to convert an unknown type of image file to a portable anymap"
---

<h2 class="name">NAME</h2>
<p> anytopnm &#8211; attempt to convert an unknown type of image file to a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>anytopnm</code> [<i>file</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>anytopnm</code> converts the input image, which may be in any of dozens of graphics formats, to PBM, PGM, or PPM format, depending on that nature of the input image, and outputs it to Standard Output. </p>
<p> To determine the format of the input, <code>anytopnm</code> uses the <code>file</code> program (possibly assisted by the magic numbers file fragment included with Netpbm). If that fails (very few image formats have magic numbers), <code>anytopnm</code> looks at the filename extension. If that fails, <code>anytopnm</code> punts. </p>
<p> The type of the output file depends on the input image. </p>
<p> If <code>file</code> indicates that the input file is compressed (either via Unix compress, gzip, or bzip compression), <code>anytopnm</code> uncompresses it and proceeds as above with the uncompressed result. </p>
<p> If <code>file</code> indicates that the input file is encoded by uuencode or btoa, <code>anytopnm</code> decodes it and proceeds as above with the decoded result. </p>
<p> If <i>file</i> is <code>&#8211;</code> or not given, <code>anytopnm</code> takes its input from Standard Input. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmfile/">pnmfile</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-file/">file</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
