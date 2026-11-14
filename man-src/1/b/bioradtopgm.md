---
title: "bioradtopgm(1)"
name: "bioradtopgm"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bioradtopgm/"
description: "bioradtopgm – convert a Biorad confocal file into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> bioradtopgm &#8211; convert a Biorad confocal file into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>bioradtopgm</code> [<code>-image#</code>] [<i>imagedata</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Biorad confocal file as input. Produces a portable graymap as output. If the resulting image is upside down, run it through <code>pnmflip -tb .</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-image#</code></p>
<dd> A Biorad image file may contain more than one image. With this flag, you can specify which image to extract (only one at a time). The first image in the file has number zero. If no image number is supplied, only information about the image size and the number of images in the input is printed out. No output is produced.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/1-pnmflip/">pnmflip</a>(1)</p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1993 by Oliver Trepte </p>
<h2>Index</h2>
