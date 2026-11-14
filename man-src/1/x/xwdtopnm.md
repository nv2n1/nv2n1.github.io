---
title: "xwdtopnm(1)"
name: "xwdtopnm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xwdtopnm/"
description: "xwdtopnm – convert a X11 or X10 window dump file into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> xwdtopnm &#8211; convert a X11 or X10 window dump file into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>xwdtopnm</code> [<i>xwdfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a X11 or X10 window dump file as input. Produces a portable anymap as output. The type of the output file depends on the input file &#8211; if it&#8217;s black &amp; white, a <i>pbm</i> file is written, else if it&#8217;s grayscale a <i>pgm</i> file, else a <i>ppm</i> file. The program tells you which type it is writing. </p>
<p> Using this program, you can convert anything on an X workstation&#8217;s screen into an anymap. Just display whatever you&#8217;re interested in, do an xwd, run it through xwdtopnm, and then use pnmcut to select the part you want.</p>
<h2>BUGS</h2>
<p> I haven&#8217;t tested this tool with very many configurations, so there are probably bugs. Please let me know if you find any.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmtoxwd/">pnmtoxwd</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-xwd/">xwd</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
