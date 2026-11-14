---
title: "pamtopdbimg(1)"
name: "pamtopdbimg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtopdbimg/"
description: "pamtodbimg – convert a Netpbm image to a Palm Pilot Image Viewer PDB Image"
---

<h2 class="name">NAME</h2>
<p> pamtodbimg &#8211; convert a Netpbm image to a Palm Pilot Image Viewer PDB Image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtopdbimg</code> </p>
<p> [<code>-notefile=</code><i>filename</i>] [<code>-title=</code><i>text</i>] [<code>-compressed</code>] [<code>-uncompressed</code>] [<code>-maybecompressed</code>] [<code>-4depth</code>] </p>
<p> [<i>netpbmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtopdbimg</code> reads a Netpbm image as input and produced a Palm Pilot Image Viewer image (and Image record in a PDB file) as output. </p>
<p> If the Neptbm image is black and white, the Pilot image is monochrome. Otherwise, the Pilot image is either 4-level or 16-level grayscale, depending on the <code>-4depth</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-title=</code><i>text</i></p>
<dd> The title of the image, to be included in the image. </p>
<dt><code>-compressed</code></p>
<dd>
<dt><code>-uncompressed</code></p>
<dd>
<dt><code>-maybecompressed</code></p>
<dd> You may specify only one of these. <code>-compressed</code> says to generate the image in compressed format. <code>-uncompressed</code> says to generate the image in uncompressed format. <code>-maybecompressed</code> says to generate whichever format is smaller (the compression algorithm sometimes actually makes the data larger). </p>
<dt><code>-4depth</code></p>
<dd> This option makes <code>pamtopdbimg</code> create the image in 16-level grayscale (4 bits per pixel) format. If you don&#8217;t specify this, <code>pamtopdbimg</code> uses 4-level (2 bits per pixel) format. </p>
<p> This option has no effect when the input is black and white (maxval 1). In that case, <code>pamtopdbimg</code> generates the monochrome (1 bit per pixel) format regardless. </p>
<dt><code>-notefile=</code><i>filename</i></p>
<dd> Attach the note in the specified file to the image. </p>
<p> If you don&#8217;t specify this, <code>pamtopdbimg</code> does not attach any note. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdbimgtopam/">pdbimgtopam</a></code>(1) , <code><a href="/docs/linux/man/1-palmtopnm/">palmtopnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> <code>pamtopdbimg</code> was new in Netpbm 10.52 (September 2010). It was modelled after Eric A. Howe&#8217;s <code>imgvtopbm</code> package, which dates back to September 1997. </p>
<h2>Index</h2>
