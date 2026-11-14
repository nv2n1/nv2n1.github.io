---
title: "psidtopgm(1)"
name: "psidtopgm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psidtopgm/"
description: "psidtopgm – convert PostScript \"image\" data into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> psidtopgm &#8211; convert PostScript &quot;image&quot; data into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>psidtopgm</code> <i>width height bits/sample</i> [<i>imagedata</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads the &quot;image&quot; data from a PostScript file as input. Produces a portable graymap as output. </p>
<p> This program is obsoleted by <code>pstopnm</code>. What follows was written before <code>pstopnm </code> existed. </p>
<p> This is a very simple and limited program, and is here only because so many people have asked for it. To use it you have to <code>manually</code> extract the readhexstring data portion from your PostScript file, and then give the width, height, and bits/sample on the command line. Before you attempt this, you should <code>at least</code> read the description of the &quot;image&quot; operator in the PostScript Language Reference Manual. </p>
<p> It would probably not be too hard to write a script that uses this filter to read a specific variety of PostScript image, but the variation is too great to make a general-purpose reader. Unless, of course, you want to write a full-fledged PostScript interpreter&#8230;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmtops/">pnmtops</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
