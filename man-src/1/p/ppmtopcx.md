---
title: "ppmtopcx(1)"
name: "ppmtopcx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtopcx/"
description: "ppmtopcx – convert a portable pixmap into a PCX file"
---

<h2>SYNOPSIS</h2>
<p> <code>ppmtopcx</code> [<code>-24bit</code>] [<code>-packed</code>] [<code>-xpos=</code><i>cols</i>] [<code>-ypos=</code><i>rows</i>] [<i>ppmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a PPM image as input. Produces a PCX file as output. The type of the PCX file depends on the number of colors in the pixmap:</p>
<dl>
<dt>16 colors or less:</dt>
<dd> 1 bit/pixel, 1-4 planes.</dd>
<dt>256 colors or less:</dt>
<dd> 8 bits/pixel, 1 plane, colormap at the end of the file.</dd>
<dt>More than 256 colors:</dt>
<dd> 24bit truecolor file (8 bits/pixel, 3 planes).</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-24bit</code></dt>
<dd> Produce a 24bit truecolor file, even if the pixmap has 256 colors or less.</dd>
<dt><code>-packed</code></dt>
<dd> Use &quot;packed pixel&quot; format for files with 16 colors or less: 1, 2, or 4 bits/pixel, 1 plane.</dd>
<dt><code>-xpos=</code><i>cols</i></dt>
<dd>
</dd><dt><code>-ypos=</code><i>rows</i></dt>
<dd> These options set the position of the image in some field (e.g. on a screen) in columns to the right of the left edge and rows below the top edge. The PCX format contains image position information. Don&#8217;t confuse this with the position of an area of interest within the image. For example, using <code>pnmpad</code> to add a 10 pixel left border to an image and then converting that image to PCX with xpos = 0 is not the same as converting the original image to PCX and setting xpos = 10. </dd>
<p> The values may be from -32767 to 32768. </p>
<p> The default for each is zero. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcxtoppm/">pcxtoppm</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> Copyright (C) 1994 by Ingo Wilken (Ingo.Wilken [at] informatik.uni-oldenburg.de)<br />
 Based on previous work by Michael Davidson. </p>
