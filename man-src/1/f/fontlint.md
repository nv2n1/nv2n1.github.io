---
title: "fontlint(1)"
name: "fontlint"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontlint/"
description: "fontlint – check a font"
---

<h2>NAME</h2>
<p> <code>fontlint &#8211; check a font</code></p>
<h2>SYNOPSIS</h2>
<p> <code>fontlint</code> <i>fontfile &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The program <code>fontlint</code> loads a font (or more than one), which may be in any format <i><a href="/docs/linux/man/1-fontforge/">fontforge</a></i>(1) can read, and checks the font for certain common errors </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Intersecting contours </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Incorrectly oriented contours </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Extrema not marked by points<br />
 And for PostScript fonts: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Too many points in a glyph </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Too many hints in a glyph </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> * Bad glyph name </p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual at:<br />
 <a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2007 by George Williams (gww [at] silcom.com). </p>
<h2>Index</h2>
