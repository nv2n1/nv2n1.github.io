---
title: "pbmclean(1)"
name: "pbmclean"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmclean/"
description: "pbmclean – flip isolated pixels in portable bitmap"
---

<h2 class="name">NAME</h2>
<p> pbmclean &#8211; flip isolated pixels in portable bitmap</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmclean </code> [<code>-minneighbors=</code><i>N</i>] [<code>-black</code>|<code>-white</code>] [<i>pbmfile</i>] </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<p> Before December 2001, <code>pbmclean</code> accepted <code>&#8211;</code><i>N</i> instead of <code>-minneighbors</code>. </p>
<h2>DESCRIPTION</h2>
<p> <code>pbmclean</code> cleans up a PBM image of random specs. It reads a PBM image as input and outputs a PBM that is the same as the input except with every pixel which has less than <i>N</i> identical neighbours inverted. </p>
<p> The default for <i>N</i> is 1 &#8211; only completely isolated pixels are flipped. </p>
<p> (A value of <i>N</i> greater than 8 generates a completely inverted image (but use <code>pnminvert</code> to do that) &#8212; or a completely white or completely black image with the <code>-black</code> or <code>-white</code> option). </p>
<p> <code>pbmclean</code> considers the area beyond the edges of the image to be white. (This matters when you consider pixels right on the edge of the image). </p>
<p> You can use <code>pbmclean </code> to clean up &quot;snow&quot; on bitmap images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-black</code></p>
<dd>
<dt><code>-white</code></p>
<dd> Flip pixels of the specified color. By default, if you specify neither <code>-black</code> nor <code>-white</code>, <code>pbmclean</code> flips both black and white pixels which do not have sufficient identical neighbors. If you specify <code>-black</code>, <code>pbmclean</code> leaves the white pixels alone and just erases isolated black pixels. Vice versa for <code>-white</code>. You may specify both <code>-black</code> and <code>-white</code> to get the same as the default behavior. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1990 by Angus Duggan Copyright (C) 1989 by Jef Poskanzer. Copyright (C) 2001 by Michael Sternberg. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. This software is provided &quot;as is&quot; without express or implied warranty. </p>
<h2>Index</h2>
