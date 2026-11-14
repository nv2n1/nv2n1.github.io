---
title: "zeisstopnm(1)"
name: "zeisstopnm"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zeisstopnm/"
description: "zeisstopnm – convert a Zeiss confocal file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> zeisstopnm &#8211; convert a Zeiss confocal file into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>zeisstopnm</code> [<i>-pgm</i> | <i>-ppm</i>] [<i>zeissfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Zeiss confocal file as input. Produces a portable anymap as output. The type of the output file depends on the input file &#8211; if it&#8217;s grayscale a <i>pgm</i> file, else a <i>ppm</i> file will be produced. The program tells you which type it is writing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-pgm</code></p>
<dd> Force the output to be a <i>pgm</i> file.</p>
<dt><code>-ppm</code></p>
<dd> Force the output to be a <i>ppm</i> file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1993 by Oliver Trepte </p>
<h2>Index</h2>
