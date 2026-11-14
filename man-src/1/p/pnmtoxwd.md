---
title: "pnmtoxwd(1)"
name: "pnmtoxwd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtoxwd/"
description: "pnmtoxwd – convert a portable anymap into an X11 window dump"
---

<h2 class="name">NAME</h2>
<p> pnmtoxwd &#8211; convert a portable anymap into an X11 window dump </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtoxwd</code> [<code>-pseudodepth</code> <i>n</i>] [<code>-directcolor</code>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Produces an X11 window dump as output. This window dump can be displayed using the xwud tool. </p>
<p> Normally, pnmtoxwd produces a StaticGray dump file for <i>pbm</i> and <i>pgm</i> files. For <i>ppm</i>, it writes a PseudoColor dump file if there are up to 256 colors in the input, and a DirectColor dump file otherwise. The <code>-directcolor</code> flag can be used to force a DirectColor dump. And the <code>-pseudodepth</code> flag can be used to change the depth of PseudoColor dumps from the default of 8 bits / 256 colors.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xwdtopnm/">xwdtopnm</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-xwud/">xwud</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
