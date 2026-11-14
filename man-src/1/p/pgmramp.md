---
title: "pgmramp(1)"
name: "pgmramp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmramp/"
description: "pgmramp – generate a grayscale ramp"
---

<h2 class="name">NAME</h2>
<p> pgmramp &#8211; generate a grayscale ramp </p>
<h2>SYNOPSIS</h2>
<p> <code>pgmramp</code> <code>-lr</code>|<code>-tb</code> | <code>-rectangle</code>|<code>-ellipse</code> <i>width height</i></p>
<h2>DESCRIPTION</h2>
<p> Generates a graymap of the specified size containing a black-to-white ramp. These ramps are useful for multiplying with other images, using the <i>pnmarith</i> tool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-lr</code></p>
<dd> A left to right ramp.</p>
<dt><code>-tb</code></p>
<dd> A top to bottom ramp.</p>
<dt><code>-rectangle</code></p>
<dd> A rectangular ramp.</p>
<dt><code>-ellipse</code></p>
<dd> An elliptical ramp.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmarith/">pnmarith</a>(1), <a href="/docs/linux/man/5-pgm/">pgm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
