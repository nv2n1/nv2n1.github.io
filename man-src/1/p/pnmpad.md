---
title: "pnmpad(1)"
name: "pnmpad"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmpad/"
description: "pnmpad – add borders to portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmpad &#8211; add borders to portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmpad </code> [<code>-verbose</code>] [<code>-white</code>|<code>-black</code>]<br />
 [[[<code>-width=</code><i>width</i> [<code>-halign=</code><i>ratio</i>]] |<br />
 [<code>-left=</code><i>leftpad</i>] [<code>-right=</code><i>rightpad</i>]]]<br />
 [[[<code>-height=</code><i>height</i> [<code>-valign=</code><i>ratio</i>]] |<br />
 [<code>-top=</code><i>toppad</i>] [<code>-bottom=</code><i>botpad</i>]]]<br />
 [<i>pnmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> Reads a PNM image as input. Outputs a PNM image that is the input image plus black or white borders of the sizes specified. </p>
<p> If you just need to convert an image to a certain size regardless of the original dimensions, <code>pnmcut</code> with the <code>-pad</code> option may be a better choice. </p>
<h2>OPTIONS</h2>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Verbose output.</dl>
<p> <code>-white</code><br />
 <code>-black</code> (default)</p>
<dl>
<dt>
<dd> Set pad color.</dl>
<p> <code>-left </code><i>leftpad</i><br />
 <code>-right </code><i>rightpad</i><br />
 <code>-top </code><i>toppad</i><br />
 <code>-bottom </code><i>bottompad</i></p>
<dl>
<dt>
<dd> Specify amount of padding in pixels.</dl>
<p> <code>-width </code><i>width</i></p>
<dl>
<dt>
<dd> Set desired width of image. Overrides <code>-left</code> and <code>-right</code> if specified. If <i>width</i> is less than the actual image width, it is ignored. Use <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1) to cut off parts of images.</dl>
<p> <code>-height </code><i>height</i></p>
<dl>
<dt>
<dd> Set desired height of image. Overrides <code>-top</code> and <code>-bottom</code> if specified. If <i>height</i> is less than the actual image height, it is ignored. Use <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1) to cut off parts of images.</dl>
<p> <code>-halign </code><i>ratio</i></p>
<dl>
<dt>
<dd> A real number between 0 and 1. Used in conjunction with <code>-width</code>, sets the alignment ratio between left padding and right padding. </p>
<p> Useful values:</p>
<dl>
<dt><code>0.0</code></p>
<dd> &#8211; left aligned;</p>
<dt><code>0.5</code></p>
<dd> &#8211; center aligned (default);</p>
<dt><code>1.0</code></p>
<dd> &#8211; right aligned.</dl>
</dl>
<p> <code>-valign </code><i>ratio</i></p>
<dl>
<dt>
<dd> A real number between 0 and 1. Used in conjunction with <code>-height</code>, sets the alignment ratio between bottom padding and top padding. </p>
<p> Useful values:</p>
<dl>
<dt><code>0.0</code></p>
<dd> &#8211; bottom aligned;</p>
<dt><code>0.5</code></p>
<dd> &#8211; center aligned (default);</p>
<dt><code>1.0</code></p>
<dd> &#8211; top aligned.</dl>
</dl>
<h2>HISTORY</h2>
<dl>
<dt>Before February 2002,</p>
<dd> <code>pnmpad</code> had a different option syntax which was less expressive and not like conventional Netpbm programs. That syntax is still understood by <code>pnmpad</code> for backward compatibility, but not documented or supported for future use. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbmmake/">pbmmake</a></code>(1), <code><a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a></code>(1), <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/1-pnmcrop/">pnmcrop</a></code>(1), <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002 by Martin van Beilen<br />
 Copyright (C) 1990 by Angus Duggan<br />
 Copyright (C) 1989 by Jef Poskanzer. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty. </p>
<h2>Index</h2>
