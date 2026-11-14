---
title: "pnmalias(1)"
name: "pnmalias"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmalias/"
description: "pnmalias – antialias a portable anyumap."
---

<h2 class="name">NAME</h2>
<p> pnmalias &#8211; antialias a portable anyumap. </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmalias</code> [<code>-bgcolor</code> <i>color</i>] [<code>-fgcolor</code> <i>color</i>] [<code>-bonly</code>] [<code>-fonly</code>] [<code>-balias</code>] [<code>-falias</code>] [<code>-weight</code> <i>w</i>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input, and applies anti-aliasing to background and foreground pixels. If the input file is a portable bitmap, the output anti-aliased image is promoted to a graymap, and a message is printed informing the user of the change in format.</p>
<h2>OPTIONS</h2>
<p> <code>-bgcolor </code> <i>colorb,</i> <code>-fgcolor</code> <i>colorf</i></p>
<dl>
<dt>
<dd> set the background color to <i>colorb,</i> and the foreground to color to <i>colorf.</i> Pixels with these values will be anti-aliased. by default, the background color is taken to be black, and foreground color is assumed to be white. The colors can be specified in five ways:</p>
<dl>
<dt><code>o</code></p>
<dd> A name, assuming that a pointer to an X11-style color names file was compiled in.</p>
<dt><code>o</code></p>
<dd> An X11-style hexadecimal specifier: rgb:r/g/b, where r g and b are each 1- to 4-digit hexadecimal numbers.</p>
<dt><code>o</code></p>
<dd> An X11-style decimal specifier: rgbi:r/g/b, where r g and b are floating point numbers between 0 and 1.</p>
<dt><code>o</code></p>
<dd> For backwards compatibility, an old-X11-style hexadecimal number: #rgb, #rrggbb, #rrrgggbbb, or #rrrrggggbbbb.</p>
<dt><code>o</code></p>
<dd> For backwards compatibility, a triplet of numbers separated by commas: r,g,b, where r g and b are floating point numbers between 0 and 1. (This style was added before MIT came up with the similar rgbi style.)</dl>
<p> Note that even when dealing with graymaps, background and foreground colors need to be specified in the fashion described above. In this case, background and foreground pixel values are taken to be the value of the red component for the given color.</dl>
<p> <code>-bonly</code>, <code>-fonly</code></p>
<dl>
<dt>
<dd> Apply anti-aliasing only to background (<code>-bonly</code>), or foreground (<code>-fonly</code>) pixels.</dl>
<p> <code>-balias</code>, <code>-falias</code></p>
<dl>
<dt>
<dd> Apply anti-aliasing to all pixels surrounding background (<code>-balias</code>), or foreground (<code>-falias</code>) pixels. By default, anti-aliasing takes place only among neighboring background and foreground pixels.</dl>
<p> <code>-weight</code> <i>w</i></p>
<dl>
<dt>
<dd> Use <i>w</i> as the central weight for the aliasing filter. <i>W </i> must be a real number in the range 0 &lt; <i>w</i> &lt; 1. The lower the value of <i>w </i> is, the &quot;blurrier&quot; the output image is. The default is w = 1/3.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmtext/">pbmtext</a>(1), <a href="/docs/linux/man/1-pnmsmooth/">pnmsmooth</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1992 by Alberto Accomazzi, Smithsonian Astrophysical Observatory. </p>
<h2>Index</h2>
