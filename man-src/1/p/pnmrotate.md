---
title: "pnmrotate(1)"
name: "pnmrotate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmrotate/"
description: "pnmrotate – rotate a portable anymap by some angle"
---

<h2 class="name">NAME</h2>
<p> pnmrotate &#8211; rotate a portable anymap by some angle </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmrotate</code> [<code>-noantialias</code>] <i>angle</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Rotates it by the specified angle and produces a portable anymap as output. If the input file is in color, the output will be too, otherwise it will be grayscale. The angle is in degrees (floating point), measured counter-clockwise. It can be negative, but it should be between -90 and 90. Also, for rotations greater than 45 degrees you may get better results if you first use <i>pnmflip</i> to do a 90 degree rotation and then <i>pnmrotate</i> less than 45 degrees back the other direction </p>
<p> The rotation algorithm is Alan Paeth&#8217;s three-shear method. Each shear is implemented by looping over the source pixels and distributing fractions to each of the destination pixels. This has an &quot;anti-aliasing&quot; effect &#8211; it avoids jagged edges and similar artifacts. However, it also means that the original colors or gray levels in the image are modified. If you need to keep precisely the same set of colors, you can use the <code>-noantialias</code> flag. This does the shearing by moving pixels without changing their values. If you want anti-aliasing and don&#8217;t care about the precise colors, but still need a limited *number* of colors, you can run the result through <i>ppmquant</i>. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>REFERENCES</h2>
<p> &quot;A Fast Algorithm for General Raster Rotation&quot; by Alan Paeth, Graphics Interface &#8217;86, pp. 77-81.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmshear/">pnmshear</a>(1), <a href="/docs/linux/man/1-pnmflip/">pnmflip</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
