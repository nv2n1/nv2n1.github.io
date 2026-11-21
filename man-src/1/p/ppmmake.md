---
title: "ppmmake(1)"
name: "ppmmake"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmmake/"
description: "ppmmake – create a pixmap of a specified size and color"
---

<h2>SYNOPSIS</h2>
<p> <code>ppmmake</code> <i>color width height</i></p>
<h2>DESCRIPTION</h2>
<p> Produces a portable pixmap of the specified color, width, and height. </p>
<p> The color can be specified in five ways:</p>
<dl>
<dt>o</dt>
<dd> A name, assuming that a pointer to an X11-style color names file was compiled in.</dd>
<dt>o</dt>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</dd>
<dt>o</dt>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</dd>
<dt>o</dt>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</dd>
<dt>o</dt>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.)</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-ppm/">ppm</a>(5), <a href="/docs/linux/man/1-pbmmake/">pbmmake</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
