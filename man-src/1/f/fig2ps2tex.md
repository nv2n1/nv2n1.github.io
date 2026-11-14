---
title: "fig2ps2tex(1)"
name: "fig2ps2tex"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2ps2tex/"
description: "fig2ps2tex – generate a TeX file for including a PostScript file"
---

<h2 class="name">NAME</h2>
<p> fig2ps2tex &#8211; generate a TeX file for including a PostScript file</p>
<h2>SYNOPSIS</h2>
<p> <code>fig2ps2tex</code> <i>file</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>Fig2ps2tex</i> generates a TeX file for including a PostScript file in a TeX document. This involves calculating the bounding box from the Postscript document. The TeX inclusion file is written to stdout. </p>
<p> There is also <i>Fig2ps2tex.csh</i> for those systems with csh and dc. </p>
<p> Note that the <i>psfig</i> macro package provides a more sophisticated approach to including Postscript files in LaTeX documents. <i>Fig2ps2tex</i> works with plain TeX however. </p>
<h2>USAGE</h2>
<p> Assume the Postscript file is called <i>foo.ps .</i> The command </p>
<dl>
<dt>
<dd> % fig2ps2tex foo.ps &gt;foo.tex</dl>
<p> will create the inclusion file with bounding information. Then include this file in your TeX document with the command </p>
<dl>
<dt>
<dd> \input{foo}</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psfig/">psfig</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-fig2dev/">fig2dev</a>(1), <a href="/docs/linux/man/1-transfig/">transfig</a>(1). </p>
<h2>AUTHOR</h2>
<p> Micah Beck<br />
 Cornell University </p>
<p> Man page by George Ferguson, ferguson [at] cs.rochester.edu. </p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 Micah Beck </p>
<p> The X Consortium, and any party obtaining a copy of these files from the X Consortium, directly or indirectly, is granted, free of charge, a full and unrestricted irrevocable, world-wide, paid up, royalty-free, nonexclusive right and license to deal in this software and documentation files (the &quot;Software&quot;), including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons who receive copies from any such party to do so, with the only requirement being that this copyright notice remain intact. This license includes without limitation a license to do the foregoing actions under any patents of the party supplying this software to the X Consortium. </p>
<h2>Index</h2>
