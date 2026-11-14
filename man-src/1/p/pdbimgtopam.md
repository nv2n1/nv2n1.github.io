---
title: "pdbimgtopam(1)"
name: "pdbimgtopam"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdbimgtopam/"
description: "pdbimgtopam – convert a Palm Pilot Image Viewer PDB Image to a PAM image"
---

<h2 class="name">NAME</h2>
<p> pdbimgtopam &#8211; convert a Palm Pilot Image Viewer PDB Image to a PAM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pdbimgtopam</code> </p>
<p> [<code>-notefile=</code><i>filename</i>] [<code>-verbose</code>] </p>
<p> [<i>pdbimgfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pdbimgtopam</code> reads a Palm Pilot Image Viewer image (and Image record in a PDB file) as input, from Standard Input or <i>palmfile</i>, and produces a PAM image as output. </p>
<p> If the Pilot image is monochrome, the PAM output has maxval 1. Otherwise, it has maxval 255. Note that Pilot images are always monochrome. The PAM image has tuple type GRAYSCALE. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display various interesting information about the input file and process. </p>
<dt><code>-notefile=</code><i>filename</i></p>
<dd> Write the image note (if any) to the specified file. </p>
<p> If you don&#8217;t specify this, <code>pdbimgtopam</code> ignores any image note. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamtopdbimg/">pamtopdbimg</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtopalm/">pnmtopalm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pdbimgtopam</code> was new in Netpbm 10.52 (September 2010). It was modelled after Eric A. Howe&#8217;s <code>imgvtopbm</code> package, which dates back to September 1997. </p>
<h2>Index</h2>
