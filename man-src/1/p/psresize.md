---
title: "psresize(1)"
name: "psresize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psresize/"
description: "psresize – rescales and centers a document for new output paper size"
---

<h2 class="name">NAME</h2>
<p> psresize &#8211; rescales and centers a document for new output paper size </p>
<h2>SYNOPSIS</h2>
<p> <code>psresize</code> [ <code>-w</code><i>width</i> ] [ <code>-h</code><i>height</i> ] [ <code>-p</code><i>paper</i> ] [ <code>-W</code><i>width</i> ] [ <code>-H</code><i>height</i> ] [ <code>-P</code><i>paper</i> ] [ <code>-q</code> ] [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Psresize</i> rescales and centres a document on a different size of paper. The input PostScript file should follow the Adobe Document Structuring Conventions. </p>
<p> The <i>-w</i> option gives the output paper width, and the <i>-h</i> option gives the output paper height, normally specified in <code>cm</code> or <code>in</code> to convert PostScript&#8217;s points (1/72 of an inch) to centimeters or inches. The <i>-p</i> option can be used as an alternative, to set the output paper size to <code>a0, a1, a2, a3, a4, a5, b5, letter, legal, tabloid, statement,</code> executive, folio, quarto or <code>10&#215;14.</code> The default output paper size is <code>a4.</code> </p>
<p> The <i>-W</i> option gives the input paper width, and the <i>-H</i> option gives the input paper height. The <i>-P</i> option can be used as an alternative, to set the input paper size. The default input paper size is <code>a4.</code> </p>
<p> <i>Psresize</i> normally prints the page numbers of the pages output; the <i>-q</i> option suppresses this.</p>
<h2>EXAMPLES</h2>
<p> The following command can be used to convert a document on A4 size paper to letter size paper: </p>
<p> psresize -PA4 -pletter in.ps out.ps </p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>Psresize</i> does not accept all DSC comments. </p>
<h2>Index</h2>
