---
title: "pnmtorast(1)"
name: "pnmtorast"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtorast/"
description: "pnmtorast – convert a portable pixmap into a Sun rasterfile"
---

<h2 class="name">NAME</h2>
<p> pnmtorast &#8211; convert a portable pixmap into a Sun rasterfile </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtorast</code> [<code>-standard</code>|<code>-rle</code>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces a Sun rasterfile as output. </p>
<p> Color values in Sun rasterfiles are eight bits wide, so <i>pnmtorast</i> will automatically scale colors to have a maxval of 255. An extra <i>pnmdepth</i> step is not necessary.</p>
<h2>OPTIONS</h2>
<p> The <code>-standard</code> flag forces the result to be in RT_STANDARD form; the <code>-rle</code> flag, RT_BYTE_ENCODED, which is smaller but, well, less standard. The default is <code>-rle</code>. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rasttopnm/">rasttopnm</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
