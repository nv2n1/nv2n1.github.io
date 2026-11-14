---
title: "pgmmake(1)"
name: "pgmmake"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmmake/"
description: "pgmmake – create a PGM image of a specified gray level and dimensions"
---

<h2 class="name">NAME</h2>
<p> pgmmake &#8211; create a PGM image of a specified gray level and dimensions</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmmake</code> [<code>-maxval=</code><i>maxval</i>] <i>graylevel</i> <i>width</i> <i>height</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmmake</code> produces a PGM image of the specified gray level, width, height, and maxval. </p>
<p> Specify the gray level (<i>graylevel</i>) as a decimal floating point number in the range [0, 1]. E.g. 1 is white, 0 is black, and 0.5 is half luminosity gray. </p>
<h2>EXAMPLES</h2>
<pre>
    pgmmake 1 50 50
</pre>
<pre>
    pgmmake .2 50 100 -maxval=5
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-maxval=</code><i>maxval</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>The maxval for the generated image.&nbsp;<wbr>&nbsp;<wbr>Default is 255. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmmake/">pbmmake</a></code>(1) , <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> This program was new in Netpbm 10.32 (February 2006). </p>
<p> With older Netpbm, use <code>ppmmake</code> and <code>ppmtopgm</code>. </p>
<h2>Index</h2>
