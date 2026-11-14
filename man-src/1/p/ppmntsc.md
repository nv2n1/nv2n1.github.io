---
title: "ppmntsc(1)"
name: "ppmntsc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmntsc/"
description: "ppmntsc – make a portable pixmap look like taken from an American TV"
---

<h2 class="name">NAME</h2>
<p> ppmntsc &#8211; make a portable pixmap look like taken from an American TV </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmntsc</code> [ <code>&#8211;pal</code> ] [ <code>&#8211;legalonly</code> ] [ <code>&#8211;illegalonly</code> ] [ <code>&#8211;correctedonly</code> ] [ <code>&#8211;verbose</code> ] [ <code>&#8211;debug</code> ] [ <i>infile</i> ] </p>
<p> Minimum unique abbreviations of options are acceptable. </p>
<h2>DESCRIPTION</h2>
<p> This program makes colors legal in the NTSC (or PAL) color systems. Often, images generated on the computer are made for use in movies which ultimately end up on video tape. However, the range of colors (as specified by their RGB values) on a computer does not match the range of colors that can be represented using the NTSC (or PAL) systems. If an image with &quot;illegal&quot; colors is sent directly to an NTSC (or PAL) video system for recording, the &quot;illegal&quot; colors will be clipped. This may result in an undesirable looking picture. </p>
<p> This utility tests each pixel in an image to see if it falls within the legal NTSC (or PAL) range. If not, it raises or lowers the pixel&#8217;s saturation in the output so that it does fall within legal limits. Pixels that are already OK just go unmodified into the output. </p>
<p> Input is from the file named <i>input</i>. If <i>input </i> is <code>&#8211;</code>, input is from Standard Input. If you don&#8217;t specify <i>input</i>, input is from Standard Input. </p>
<p> Output is always to Standard Output. </p>
<p> This program handles multi-image PPM input, producing multi-image PPM output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;pal</code></p>
<dd> Use the PAL transform instead of the default NTSC.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print a grand total of the number of illegal pixels.</p>
<dt><code>&#8211;debug</code></p>
<dd> Produce a humongous listing of illegal colors and their legal counterparts. NOTE: This option may produce a great deal of output.</p>
<dt><code>&#8211;legalonly</code></p>
<dd> Output only pixels that are already legal. Output black in place of pixels that are not.</p>
<dt><code>&#8211;illegalonly</code></p>
<dd> Output only pixels that are illegal (and output them uncorrected). Output black in place of pixels that are already legal.</p>
<dt><code>&#8211;correctedonly</code></p>
<dd> Output only pixels that are corrected versions of illegal pixels. Output black in place of pixels that are already legal. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-ppmdepth/">ppmdepth</a></code>(1), <code><a href="/docs/linux/man/1-ppmdim/">ppmdim</a></code>(1), <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Wes Barris, Minnesota Supercomputer Center, Inc., Bryan Henderson </p>
<h2>Index</h2>
