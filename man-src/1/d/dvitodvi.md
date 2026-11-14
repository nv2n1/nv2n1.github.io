---
title: "dvitodvi(1)"
name: "dvitodvi"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvitodvi/"
description: "dvitodvi – rearrange pages in a DVI file"
---

<h2 class="name">NAME</h2>
<p> dvitodvi &#8211; rearrange pages in a DVI file </p>
<h2>SYNOPSIS</h2>
<p> <code>dvitodvi</code> [ <code>-q</code> ] [ <code>-i</code> <i>infile</i> ] [ <code>-o</code> <i>outfile</i> ] [ <code>-w</code><i>width</i> ] [ <code>-h</code><i>height</i> ] <i>pagespecs</i> [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Dvitodvi</i> rearranges pages from a DVI file, creating a new DVI file. <i>Dvitodvi</i> can be used to perform a large number of arbitrary re-arrangements of Documents, including arranging for printing 2-up, 4-up, booklets, reversing, selecting front or back sides of documents, scaling, etc. </p>
<p> <i>pagespecs</i> follow the syntax:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pagespecs</i></p>
<dd> <i>= [modulo:][mag@]specs</i></p>
<dt><i>specs</i></p>
<dd> <i>= spec[+specs][,specs]</i></p>
<dt><i>spec</i></p>
<dd> <i>= [-]pageno[(xoff,yoff)]</i></dl>
</dl>
<p> <i>modulo</i> is the number of pages in each block. The value of <i>modulo</i> should be greater than 0; the default value is 1. The optional <i>mag</i> parameter adjusts the file&#8217;s magnification by the magnification specified. The magnification and modulo can be specified in reverse order if desired. <i>specs</i> are the page specifications for the pages in each block. The value of the <i>pageno</i> in each <i>spec</i> should be between 0 (for the first page in the block) and <i>modulo</i>-1 (for the last page in each block) inclusive. The optional dimensions <i>xoff</i> and <i>yoff</i> shift the page by the specified (positive) amount. <i>xoff</i> and <i>yoff</i> are in PostScript&#8217;s points, but may be followed by the units <code>cm</code> or <code>in</code> to convert to centimetres or inches, or the flag <code>w</code> or <code>h</code> to specify as a multiple of the width or height. If the optional minus sign is specified, the page is relative to the end of the document, instead of the start. </p>
<p> If page <i>spec</i>s are separated by <code>+</code> the pages will be merged into one page; if they are separated by <code>,</code> they will be on separate pages. If there is only one page specification, with <i>pageno</i> zero, the <i>pageno</i> may be omitted. </p>
<p> The <i>-w</i> option gives the width which is used by the <code>w</code> dimension specifier, and the <i>-h</i> option gives the height which is used by the <code>h</code> dimension specifier. These dimensions are also used (after scaling) to set the clipping path for each page. </p>
<p> Dvitodvi normally prints the page numbers of the pages re-arranged; the <i>-q</i> option suppresses this.</p>
<h2>EXAMPLES</h2>
<p> This section contains some sample re-arrangements. To put two pages on one sheet (of landscaped A3 paper), the pagespec to use is: </p>
<dl>
<dt>
<dd> 2:0+1(21cm,0)</dl>
<p> To reduce an A3 page to A4 size, the pagespec to use is: </p>
<dl>
<dt>
<dd> 700@(-.3in,-.3in)</dl>
<p> To select all of the odd pages in reverse order, use: </p>
<dl>
<dt>
<dd> 2:-0</dl>
<h2>AUTHOR</h2>
<p> Angus Duggan, from <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), by Chris Torek, University of Maryland. Currently maintained as part of TeX Live (<a rel="nofollow" href="https://tug.org/texlive">https://tug.org/texlive</a>).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dvibook/">dvibook</a>(1), <a href="/docs/linux/man/1-dviconcat/">dviconcat</a>(1), <a href="/docs/linux/man/1-dviselect/">dviselect</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1), <a href="/docs/linux/man/1-tex/">tex</a>(1)<br />
 <i>MC-TeX User&#8217;s Guide</i></p>
<h2>BUGS</h2>
<p> <i>Dvitodvi</i> does not adjust some of the parameters in the postamble. This may be a problem if these values are used to size certain structures in the output conversion programs. </p>
<h2>Index</h2>
