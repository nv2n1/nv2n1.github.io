---
title: "macptopbm(1)"
name: "macptopbm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-macptopbm/"
description: "macptopbm – convert a MacPaint file into a portable bitmap"
---

<h2 class="name">NAME</h2>
<p> macptopbm &#8211; convert a MacPaint file into a portable bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>macptopbm</code> [<code>-extraskip</code> <i>N</i>] [<i>macpfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a MacPaint file as input. Produces a portable bitmap as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-extraskip</code></p>
<dd> This flag is to get around a problem with some methods of transferring files from the Mac world to the Unix world. Most of these methods leave the Mac files alone, but a few of them add the &quot;finderinfo&quot; data onto the front of the Unix file. This means an extra 128 bytes to skip over when reading the file. The symptom to watch for is that the resulting PBM file looks shifted to one side. If you get this, try <code>-extraskip</code> 128, and if that still doesn&#8217;t look right try another value.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-picttoppm/">picttoppm</a>(1), <a href="/docs/linux/man/1-pbmtomacp/">pbmtomacp</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 by Jef Poskanzer. The MacPaint-reading code is copyright (c) 1987 by Patrick J. Naughton (naughton [at] wind.sun.com). </p>
<h2>Index</h2>
