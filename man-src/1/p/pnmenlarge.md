---
title: "pnmenlarge(1)"
name: "pnmenlarge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmenlarge/"
description: "pnmenlarge – read a portable anymap and enlarge it N times"
---

<h2 class="name">NAME</h2>
<p> pnmenlarge &#8211; read a portable anymap and enlarge it N times </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmenlarge</code> <i>N</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Replicates its pixels <i>N</i> times, and produces a portable anymap as output. </p>
<p> <i>pnmenlarge</i> can only enlarge by integer factors. The slower but more general <i>pnmscale</i> can enlarge or reduce by arbitrary factors, and <i>pbmreduce</i> can reduce by integer factors, but only for bitmaps. </p>
<p> If you enlarge by a factor of 3 or more, you should probably add a <i>pnmsmooth</i> step; otherwise, you can see the original pixels in the resulting image.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmreduce/">pbmreduce</a>(1), <a href="/docs/linux/man/1-pnmscale/">pnmscale</a>(1), <a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
