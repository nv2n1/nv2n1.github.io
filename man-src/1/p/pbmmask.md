---
title: "pbmmask(1)"
name: "pbmmask"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmmask/"
description: "pbmmask – create a mask bitmap from a regular bitmap"
---

<h2 class="name">NAME</h2>
<p> pbmmask &#8211; create a mask bitmap from a regular bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmmask</code> [<code>-expand</code>] [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Creates a corresponding mask bitmap and writes it out. </p>
<p> The color to be interpreted as &quot;background&quot; is determined automatically. Regardless of which color is background, the mask will be white where the background is and black where the figure is. </p>
<p> This lets you do a masked paste like this, for objects with a black background: </p>
<pre>
    pbmmask obj &gt; objmask
    pnmpaste &lt; dest -and objmask &lt;x&gt; &lt;y&gt; | pnmpaste -or obj &lt;x&gt; &lt;y&gt;
</pre>
<p> For objects with a white background, you can either invert them or add a step: </p>
<pre>
    pbmmask obj &gt; objmask
    pnminvert objmask | pnmpaste -and obj 0 0 &gt; blackback
    pnmpaste &lt; dest -and objmask &lt;x&gt; &lt;y&gt; | pnmpaste -or blackback &lt;x&gt; &lt;y&gt;
</pre>
<p> Note that this three-step version works for objects with black backgrounds too, if you don&#8217;t care about the wasted time. </p>
<p> You can also use masks with graymaps and pixmaps, using the <i>pnmarith</i> tool. For instance: </p>
<pre>
    ppmtopgm obj.ppm | pgmtopbm -threshold | pbmmask &gt; objmask.pbm
    pnmarith -multiply dest.ppm objmask.pbm &gt; t1.ppm
    pnminvert objmask.pbm | pnmarith -multiply obj.ppm - &gt; t2.ppm
    pnmarith -add t1.ppm t2.ppm
</pre>
<p> An interesting variation on this is to pipe the mask through the <i>pnmsmooth</i> script before using it. This makes the boundary between the two images less sharp. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-expand</code></p>
<dd> Expands the mask by one pixel out from the image. This is useful if you want a little white border around your image. (A better solution might be to turn the <i>pbmlife</i> tool into a general cellular automaton tool&#8230;) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmcolormask/">ppmcolormask</a></code>(1), <code><a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a></code>(1), <code><a href="/docs/linux/man/1-pnminvert/">pnminvert</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/1-pnmarith/">pnmarith</a></code>(1), <code><a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1988 by Jef Poskanzer. </p>
<h2>Index</h2>
