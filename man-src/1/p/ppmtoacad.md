---
title: "ppmtoacad(1)"
name: "ppmtoacad"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtoacad/"
description: "ppmtoacad – convert portable pixmap to AutoCAD database or slide"
---

<h2 class="name">NAME</h2>
<p> ppmtoacad &#8211; convert portable pixmap to AutoCAD database or slide </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtoacad</code> [<code>-dxb</code>] [<code>-poly</code>] [<code>-background</code> <i>colour</i>] [<code>-white</code>] [<code>-aspect</code> <i>ratio</i>] [<code>-8</code>] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input. Produces an AutoCAD&#174; slide file or binary database import (.dxb) file as output. If no <i>ppmfile</i> is specified, input is read from standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dxb</code></p>
<dd> An AutoCAD binary database import (.dxb) file is written. This file is read with the DXBIN command and, once loaded, becomes part of the AutoCAD geometrical database and can be viewed and edited like any other object. Each sequence of identical pixels becomes a separate object in the database; this can result in very large AutoCAD drawing files. However, if you want to trace over a bitmap, it lets you zoom and pan around the bitmap as you wish.</p>
<dt><code>-poly</code></p>
<dd> If the <code>-dxb</code> option is not specified, the output of <code>ppmtoacad</code> is an AutoCAD slide file. Normally each row of pixels is represented by an AutoCAD line entity. If <code>-poly</code> is selected, the pixels are rendered as filled polygons. If the slide is viewed on a display with higher resolution than the source pixmap, this will cause the pixels to expand instead of appearing as discrete lines against the screen background colour. Regrettably, this representation yields slide files which occupy more disc space and take longer to display.</p>
<dt><code>-background</code><i> colour</i></p>
<dd> Most AutoCAD display drivers can be configured to use any available colour as the screen background. Some users perfer a black screen background, others white, while splinter groups advocate burnt ocher, tawny puce, and shocking grey. Discarding pixels whose closest AutoCAD colour representation is equal to the background colour can substantially reduce the size of the AutoCAD database or slide file needed to represent a bitmap. If no <code>-background</code> colour is specified, the screen background colour is assumed to be black. Any AutoCAD colour number may be specified as the screen background; colour numbers are assumed to specify the hues defined in the standard AutoCAD 256 colour palette.</p>
<dt><code>-white</code></p>
<dd> Since many AutoCAD users choose a white screen background, this option is provided as a short-cut. Specifying <code>-white</code> is identical in effect to <code>-background 7</code>.</p>
<dt><code>-aspect</code><i> ratio</i></p>
<dd> If the source pixmap had non-square pixels, the ratio of the pixel width to pixel height should be specified as <i>ratio</i>. The resulting slide or .dxb file will be corrected so that pixels on the AutoCAD screen will be square. For example, to correct an image made for a 320&#215;200 VGA/MCGA screen, specify <code>-aspect 0.8333</code>.</p>
<dt><code>-8</code></p>
<dd> Restricts the colours in the output file to the 8 RGB shades.</dl>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>BUGS</h2>
<p> AutoCAD has a fixed palette of 256 colours, distributed along the hue, lightness, and saturation axes. Pixmaps which contain many nearly-identical colours, or colours not closely approximated by AutoCAD&#8217;s palette, may be poorly rendered. </p>
<p> <code>ppmtoacad</code> works best if the system displaying its output supports the full 256 colour AutoCAD palette. Monochrome, 8 colour, and 16 colour configurations will produce less than optimal results. </p>
<p> When creating a .dxb file or a slide file with the <code>-poly</code> option, <code>ppmtoacad</code> finds both vertical and horizontal runs of identical pixels and consolidates them into rectangular regions to reduce the size of the output file. This is effective for images with large areas of constant colour but it&#8217;s no substitute for true raster to vector conversion. In particular, thin diagonal lines are not optimised at all by this process. </p>
<p> Output files can be huge.</p>
<h2>SEE ALSO</h2>
<p> AutoCAD Reference Manual: <i>Slide File Format</i> and <i>Binary Drawing Interchange (DXB) Files</i>, <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5)</p>
<h2>AUTHOR</h2>
<dl>
<dt>
<dd>
<pre>
John Walker
Autodesk SA
Avenue des Champs-Montants 14b
CH-2074 MARIN
Suisse/Schweiz/Svizzera/Svizra/Switzerland
<dl>
<dt>Usenet:<dd>kelvin [at] Autodesk.com
<dt>Fax:<dd>038/33 88 15
<dt>Voice:<dd>038/33 76 33
</pre>
</dl>
</dl>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, without any conditions or restrictions. This software is provided &#8220;as is&#8221; without express or implied warranty. </p>
<p> AutoCAD and Autodesk are registered trademarks of Autodesk, Inc. </p>
<h2>Index</h2>
