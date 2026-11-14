---
title: "pgmabel(1)"
name: "pgmabel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgmabel/"
description: "pgmabel – create cross section using Abel Integration for Deconvolution"
---

<h2 class="name">NAME</h2>
<p> pgmabel &#8211; create cross section using Abel Integration for Deconvolution</p>
<h2>SYNOPSIS</h2>
<p> <code>pgmabel</code> [<code>-help</code>] [<code>-axis</code> <i>axis</i>] [<code>-factor</code> <i>factor</i>] [<code>-pixsize</code> <i>pixsize</i>] [<code>-left</code> | <code>-right</code>] [<code>-verbose</code>] [<i>filespec</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pgmabel</code> reads as input a PGM image, which it assumes to be an image of a rotational symmetric transparent object. The image must have a vertical symmetry axis. <code>pgmabel</code> produces as output an image of a cross-section of the image. </p>
<p> <code>pgmabel</code> does the calculation by performing the Abel Integration for Deconvolution of an axial-symmetrical image by solving the system of linear equations. </p>
<p> After integration, <code>pgmabel</code> weights all gray-values of one side by the surface area of the calculated ring in square pixels divided by 4*<i>factor</i> multiplied by the size of one pixel (<i>pixsize</i>). With the <code>-verbose</code> option, <code>pgmabel</code> prints the weighting factors. </p>
<p> Where the calculation generates a negative result, the output is black. </p>
<p> The computation is unstable against periodic structures with size 2 in the vertical direction. </p>
<h2>OPTIONS</h2>
<p> You can abbreviate any option to its shortest unique prefix. </p>
<dl>
<dt><code>-help</code></p>
<dd> Prints a help message. </p>
<dt><code>-axis</code> <i>axis</i></p>
<dd> Position of the axis of symmetry in the image in pixels from the left edge of the image. Default is the center of the image. </p>
<dt><code>-factor</code> <i>factor</i></p>
<dd> User defined factor for enhancement of the output. Use a <i>factor</i> less than 1 for decreasing gary values. Default is 1.0. </p>
<dt><code>-pixsize</code> <i>pixsize</i></p>
<dd> The size of a pixel for getting scale invariant. Default is 0.1. </p>
<dt><code>-left</code></p>
<dd> Calculate only the left side of the image. You cannot specify both <code>left</code> and <code>right</code>. </p>
<dt><code>-right</code></p>
<dd> Analogous to <code>-left</code>. </p>
<dt><code>-verbose</code></p>
<dd> print information about the calculation. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Rotate a PGM image to get an image with a vertical axis of symmetry, then calculate the cross section: </p>
<pre>
    pnmrotate 90 file.pgm | pgmabel -axis 140 &gt;cross_section.pgm
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1) , <code><a href="/docs/linux/man/1-pgm/">pgm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.3 (June 2002). </p>
<h2>AUTHOR</h2>
<p> Volker Schmidt (lefti [at] voyager.boerde.de) </p>
<p> Copyright (C) 1997-2002 German Aerospace research establishment </p>
<h2>Index</h2>
