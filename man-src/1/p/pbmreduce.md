---
title: "pbmreduce(1)"
name: "pbmreduce"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmreduce/"
description: "pbmreduce – read a portable bitmap and reduce it N times"
---

<h2 class="name">NAME</h2>
<p> pbmreduce &#8211; read a portable bitmap and reduce it N times </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmreduce</code> [<code>-floyd</code>|<code>-fs</code>|<code>-threshold</code> ] [<code>-value</code> <i>val</i>] <i>N</i> [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Reduces it by a factor of <i>N</i>, and produces a portable bitmap as output. </p>
<p> <i>pbmreduce</i> duplicates a lot of the functionality of <i>pgmtopbm;</i> you could do something like <code>pnmscale | pgmtopbm,</code> but <i>pbmreduce</i> is a lot faster. </p>
<p> <i>pbmreduce</i> can be used to &quot;re-halftone&quot; an image. Let&#8217;s say you have a scanner that only produces black&amp;white, not grayscale, and it does a terrible job of halftoning (most b&amp;w scanners fit this description). One way to fix the halftoning is to scan at the highest possible resolution, say 300 dpi, and then reduce by a factor of three or so using <i>pbmreduce</i>. You can even correct the brightness of an image, by using the <code>-value</code> flag.</p>
<h2>OPTIONS</h2>
<p> By default, the halftoning after the reduction is done via boustrophedonic Floyd-Steinberg error diffusion; however, the <code>-threshold</code> flag can be used to specify simple thresholding. This gives better results when reducing line drawings. </p>
<p> The <code>-value</code> flag alters the thresholding value for all quantizations. It should be a real number between 0 and 1. Above 0.5 means darker images; below 0.5 means lighter. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmenlarge/">pnmenlarge</a>(1), <a href="/docs/linux/man/1-pnmscale/">pnmscale</a>(1), <a href="/docs/linux/man/1-pgmtopbm/">pgmtopbm</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 by Jef Poskanzer. </p>
<h2>Index</h2>
