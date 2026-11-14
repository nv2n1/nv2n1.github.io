---
title: "pnmmargin(1)"
name: "pnmmargin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmmargin/"
description: "pnmmargin – add a border to a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmmargin &#8211; add a border to a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmmargin</code> [<code>-white</code>|<code>-black</code>|<code>-color</code> <i>colorspec</i>] <i>size</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Adds a border of the specified number of pixels, and produces a portable anymap as output.</p>
<h2>OPTIONS</h2>
<p> You can specify the border color with the <code>-white</code>, <code>-black</code>, and <code>-color</code> flags. If no color is specified, the program makes a guess. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>BUGS</h2>
<p> It&#8217;s a script. Scripts are not portable to non-Unix environments.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
