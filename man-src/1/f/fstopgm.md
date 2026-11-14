---
title: "fstopgm(1)"
name: "fstopgm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fstopgm/"
description: "fstopgm – convert a Usenix FaceSaver(tm) file into a portable graymap"
---

<h2 class="name">NAME</h2>
<p> fstopgm &#8211; convert a Usenix FaceSaver(tm) file into a portable graymap </p>
<h2>SYNOPSIS</h2>
<p> <code>fstopgm</code> [<i>fsfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a Usenix FaceSaver(tm) file as input. Produces a portable graymap as output. </p>
<p> FaceSaver(tm) files sometimes have rectangular pixels. While <i>fstopgm</i> won&#8217;t re-scale them into square pixels for you, it will give you the precise <i>pnmscale</i> command that will do the job. Because of this, reading a FaceSaver(tm) image is a two-step process. First you do: </p>
<pre>
  fstopgm &gt; /dev/null
</pre>
<p> This will tell you whether you need to use <i>pnmscale.</i> Then use one of the following pipelines: </p>
<pre>
  fstopgm | pgmnorm
  fstopgm | pnmscale -whatever | pgmnorm
</pre>
<p> To go to PBM, you want something more like one of these: </p>
<pre>
  fstopgm | pnmenlarge 3 | pgmnorm | pgmtopbm
  fstopgm | pnmenlarge 3 | pnmscale &lt;whatever&gt; | pgmnorm | pgmtopbm
</pre>
<p> You want to enlarge when going to a bitmap because otherwise you lose information; but enlarging by more than 3 does not look good. </p>
<p> FaceSaver is a registered trademark of Metron Computerware Ltd. of Oakland, CA.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pgmtofs/">pgmtofs</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5), <a href="/docs/linux/man/1-pgmnorm/">pgmnorm</a>(1), <a href="/docs/linux/man/1-pnmenlarge/">pnmenlarge</a>(1), <a href="/docs/linux/man/1-pnmscale/">pnmscale</a>(1), <a href="/docs/linux/man/1-pgmtopbm/">pgmtopbm</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
