---
title: "pstops(1)"
name: "pstops"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstops/"
description: "pstops – shuffle pages in a PostScript file"
---

<h2 class="name">NAME</h2>
<p> pstops &#8211; shuffle pages in a PostScript file </p>
<h2>SYNOPSIS</h2>
<p> <code>pstops</code> [ <code>-q</code> ] [ <code>-b</code> ] [ <code>-w</code><i>width</i> ] [ <code>-h</code><i>height</i> ] [ <code>-p</code><i>paper</i> ] [ <code>-d</code><i>lwidth</i> ] <i>pagespecs</i> [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Pstops</i> rearranges pages from a PostScript document, creating a new PostScript file. The input PostScript file should follow the Adobe Document Structuring Conventions. <i>Pstops</i> can be used to perform a large number of arbitrary re-arrangements of Documents, including arranging for printing 2-up, 4-up, booklets, reversing, selecting front or back sides of documents, scaling, etc. </p>
<p> <i>pagespecs</i> follow the syntax:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pagespecs</i></p>
<dd> <i>= [modulo:]specs</i></p>
<dt><i>specs</i></p>
<dd> <i>= spec[+specs][,specs]</i></p>
<dt><i>spec</i></p>
<dd> <i>= [-]pageno[L][R][U][H][V][@scale][(xoff,yoff)]</i></dl>
</dl>
<p> <i>modulo</i> is the number of pages in each block. The value of <i>modulo</i> should be greater than 0; the default value is 1. <i>specs</i> are the page specifications for the pages in each block. The value of the <i>pageno</i> in each <i>spec</i> should be between 0 (for the first page in the block) and <i>modulo</i>-1 (for the last page in each block) inclusive. The optional dimensions <i>xoff</i> and <i>yoff</i> shift the page by the specified amount. <i>xoff</i> and <i>yoff</i> are in PostScript&#8217;s points, but may be followed by the units <code>cm</code> or <code>in</code> to convert to centimetres or inches, or the flag <code>w</code> or <code>h</code> to specify as a multiple of the width or height. The optional parameters <i>L</i>, <i>R</i>, <i>U</i>, <i>H</i> and <i>V</i> rotate the page left, right, or upside-down, and flip (mirror) page horizontally or vertically. The optional <i>scale</i> parameter scales the page by the fraction specified. If the optional minus sign is specified, the page is relative to the end of the document, instead of the start. </p>
<p> If page <i>spec</i>s are separated by <code>+</code> the pages will be merged into one page; if they are separated by <code>,</code> they will be on separate pages. If there is only one page specification, with <i>pageno</i> zero, the <i>pageno</i> may be omitted. </p>
<p> The shift, rotation, and scaling are applied to the PostScript transformation matrix in that order regardless of which order they appear on the command line. The matrix accumulates the individual transformations. The effect on the image is to first scale with respect to an origin at the lower left corner, then rotate about the same origin, and finally shift. </p>
<p> The <i>-w</i> option gives the width which is used by the <code>w</code> dimension specifier, and the <i>-h</i> option gives the height which is used by the <code>h</code> dimension specifier. These dimensions are also used (after scaling) to set the clipping path for each page. The <i>-p</i> option can be used as an alternative, to set the paper size to <code>a0, a1, a2, a3, a4, a5, b5, letter, legal, tabloid, statement,</code> executive, folio, quarto or <code>10&#215;14.</code> The default paper size is <code>a4.</code> </p>
<p> The <i>-b</i> option prevents any <code>bind</code> operators in the PostScript prolog from binding. This may be needed in cases where complex multi-page re-arrangements are being done. </p>
<p> The <i>-d</i> option draws a line around the border of each page, of the specified width. If the <i>lwidth</i> parameter is omitted, a default linewidth of 1 point is assumed. The linewidth is relative to the original page dimensions, <i>i.e.</i> it is scaled up or down with the rest of the page. </p>
<p> Pstops normally prints the page numbers of the pages re-arranged; the <i>-q</i> option suppresses this.</p>
<h2>EXAMPLES</h2>
<p> This section contains some sample re-arrangements. To put two pages on one sheet (of A4 paper), the pagespec to use is: </p>
<p> <center> &quot;2:0L@.7(21cm,0)+1L@.7(21cm,14.85cm)&quot;<br />
 </center> </p>
<p> To select all of the odd pages in reverse order, use: </p>
<p> <center> 2:-0<br />
 </center> </p>
<p> To re-arrange pages for printing 2-up booklets, use </p>
<p> <center> &quot;4:-3L@.7(21cm,0)+0L@.7(21cm,14.85cm)&quot;<br />
 </center> </p>
<p> for the front sides, and </p>
<p> <center> &quot;4:1L@.7(21cm,0)+-2L@.7(21cm,14.85cm)&quot;<br />
 </center> </p>
<p> for the reverse sides (or join them with a comma for duplex printing).</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>Pstops</i> does not accept all DSC comments. </p>
<h2>Index</h2>
