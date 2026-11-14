---
title: "pbmtoascii(1)"
name: "pbmtoascii"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtoascii/"
description: "pbmtoascii – convert a portable bitmap into ASCII graphics"
---

<h2 class="name">NAME</h2>
<p> pbmtoascii &#8211; convert a portable bitmap into ASCII graphics </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtoascii</code> [<code>-1&#215;2</code>|<code>-2&#215;4</code>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Produces a somewhat crude ASCII graphic as output. </p>
<p> Note that there is no asciitopbm tool &#8211; this transformation is one-way.</p>
<h2>OPTIONS</h2>
<p> The <code>-1&#215;2</code> and <code>-2&#215;4</code> flags give you two alternate ways for the bits to get mapped to characters. With <code>1&#215;2</code>, the default, each character represents a group of 1 bit across by 2 bits down. With <code>-2&#215;4</code>, each character represents 2 bits across by 4 bits down. With the 1&#215;2 mode you can see the individual bits, so it&#8217;s useful for previewing small bitmaps on a non-graphics terminal. The 2&#215;4 mode lets you display larger bitmaps on a standard 80-column display, but it obscures bit-level details. 2&#215;4 mode is also good for displaying graymaps &#8211; &quot;pnmscale -width 158 | pgmnorm | pgmtopbm -thresh&quot; should give good results.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988, 1992 by Jef Poskanzer. </p>
<h2>Index</h2>
