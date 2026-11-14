---
title: "epsffit(1)"
name: "epsffit"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epsffit/"
description: "epsffit – fit encapsulated PostScript file (EPSF) into constrained size"
---

<h2 class="name">NAME</h2>
<p> epsffit &#8211; fit encapsulated PostScript file (EPSF) into constrained size </p>
<h2>SYNOPSIS</h2>
<p> <code>epsffit</code> [ <code>-c</code> ] [ <code>-r</code> ] [ <code>-a</code> ] [ <code>-m</code> ] [ <code>-s</code> ] <i>llx lly urx ury</i> [ <code>infile</code> [ <code>outfile</code> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Epsffit</i> fits an EPSF file (encapsulated PostScript) to a given bounding box. The coordinates of the box are given by <code>(llx,lly)</code> for the lower left, and <code>(urx,ury)</code> for the upper right, in PostScript units (points). </p>
<p> If no input or output files are specified, <i>epsffit</i> read from the standard input and writes to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Center the image in the given bounding box.</p>
<dt><code>-r</code></p>
<dd> Rotate the image by 90 degrees counter-clockwise.</p>
<dt><code>-a</code></p>
<dd> Adjust the aspect ratio to fit the bounding box. The default is to preserve the aspect ratio.</p>
<dt><code>-m</code></p>
<dd> Rotates the image to maximise the size if it would fit the specified bounding box better.</p>
<dt><code>-s</code></p>
<dd> Add a <i>showpage</i> at the end of the file to force the image to print.</dl>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated. </p>
<h2>Index</h2>
