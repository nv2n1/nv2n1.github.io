---
title: "palmtopnm(1)"
name: "palmtopnm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-palmtopnm/"
description: "palmtopnm – convert a Palm pixmap into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> palmtopnm &#8211; convert a Palm pixmap into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>palmtopnm</code> [<code>-verbose</code>] [<code>-rendition</code> <i>N</i>] [<code>-showhist</code>]<br />
 [<code>-forceplain</code>] [<i>pnmfile</i>]<br />
 <code>palmtopnm</code> <code>-transparent </code> [<code>-verbose</code>] [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads a Palm pixmap as input, from stdin or <i>pnmfile</i>. Produces either a portable pixmap as output, or writes the value of the transparent color in the Palm pixmap to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-verbose</code></p>
<dd> Display various interesting information about the input file and process.</p>
<dt><code>-transparent</code></p>
<dd> If the Palm pixmap has a transparent color set, the RGB value for that color will be written to stdout as in the form #RRGGBB, where RR, GG, and BB are two-digit hexadecimal numbers indicating a value between 0 and 255. If no transparent color is set in the bitmap, nothing will be output. No additional output will be generated; no anymap will be output.</p>
<dt><code>-rendition N</code></p>
<dd> Palm pixmaps may contain several different renditions of the same pixmap, with different depths. By default, <code>palmtopnm </code> operates on the first rendition (rendition number 1) in the pixmap. This switch allows you to operate on a different rendition. The value must be between 1 and the number of renditions in the pixmap, inclusive.</p>
<dt><code>-showhist</code></p>
<dd> Writes a histogram of colors in the input file to stderr.</p>
<dt><code>-forceplain</code></p>
<dd> Force the output anymap to be in ASCII &#8216;plain&#8217; netpbm format. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmtopalm/">pnmtopalm</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a>(5)</code> </p>
<h2>BUGS</h2>
<p> An additional compression format, &quot;packbits,&quot; has been added with PalmOS 4.0. This package should be updated to handle it. </p>
<p> You currently cannot generate an alpha mask if the Palm pixmap has a transparent color. However, you can still do this with <code>ppmcolormask</code> with a Netpbm pipe similar to: </p>
<p> <code>palmtopnm pixmap.palm | ppmcolormask `palmtopnm -transparent pixmap.palm`</code> </p>
<h2>AUTHORS</h2>
<p> This program was originally written as Tbmptopnm.c, by Ian Goldberg. It was heavily modified by Bill Janssen to add color, compression, and transparency function.<br />
 Copyright 1995-2001 by Ian Goldberg and Bill Janssen. </p>
<h2>Index</h2>
