---
title: "pgmenhance(1)"
name: "pgmenhance"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmenhance/"
description: "pgmenhance – edge-enhance a portable graymap"
---

<h2 class="name">NAME</h2>
<p> pgmenhance &#8211; edge-enhance a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmenhance</code> [<i>-N</i>] [<i>pgmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable graymap as input. Enhances the edges, and writes a portable graymap as output. </p>
<p> The edge enhancing technique is taken from Philip R. Thompson&#8217;s &quot;xim&quot; program, which in turn took it from section 6 of &quot;Digital Halftones by Dot Diffusion&quot;, D. E. Knuth, ACM Transaction on Graphics Vol. 6, No. 4, October 1987, which in turn got it from two 1976 papers by J. F. Jarvis et. al.</p>
<h2>OPTIONS</h2>
<p> The optional <i>-N</i> flag should be a digit from 1 to 9. 1 is the lowest level of enhancement, 9 is the highest, The default is 9.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pgmedge/">pgmedge</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
