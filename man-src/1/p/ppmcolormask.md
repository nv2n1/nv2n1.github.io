---
title: "ppmcolormask(1)"
name: "ppmcolormask"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmcolormask/"
description: "ppmcolormask – produce mask of areas of a certain color in a PPM file"
---

<h2 class="name">NAME</h2>
<p> ppmcolormask &#8211; produce mask of areas of a certain color in a PPM file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmcolormask</code> <i>color</i> [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a PPM file as input. Produces a PBM (bitmap) file as output. The output file is the same dimensions as the input file and is black in all places where the input file is the color <i>color</i>, and white everywhere else. </p>
<p> The output of <code>ppmcolormask</code> is useful as an alpha mask input to <code>pnmcomp</code>. Note that you can generate such an alpha mask automatically as you convert to PNG format with <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1). Use its <code>-transparent</code> option. </p>
<p> <i>ppmfile</i> is the input file. If you don&#8217;t specify <i>ppmfile</i>, the input is from Standard Input. </p>
<p> The output goes to Standard Output. </p>
<p> You can specify <i>color</i> five ways:</p>
<dl>
<dt>o</p>
<dd> An X11-style color name (e.g. <code>black</code>).</p>
<dt>o</p>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</p>
<dt>o</p>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</p>
<dt>o</p>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</p>
<dt>o</p>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgmtoppm/">pgmtoppm</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-pbmmask/">pbmmask</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a>(5)</code> </p>
<h2>AUTHOR</h2>
<p> Bryan Henderson (bryanh [at] giraffe-data.com) </p>
<h2>Index</h2>
