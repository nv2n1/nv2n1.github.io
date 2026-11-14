---
title: "psselect(1)"
name: "psselect"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psselect/"
description: "psselect – select pages from a PostScript file"
---

<h2 class="name">NAME</h2>
<p> psselect &#8211; select pages from a PostScript file </p>
<h2>SYNOPSIS</h2>
<p> <code>psselect</code> [ <code>-q</code> ] [ <code>-e</code> ] [ <code>-o</code> ] [ <code>-r</code> ] [ <code>-p</code><i>pages</i> ] [ <i>pages</i> ] [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Psselect</i> selects pages from a PostScript document, creating a new PostScript file. The input PostScript file should follow the Adobe Document Structuring Conventions. </p>
<p> The <i>-e</i> option selects all of the even pages; it may be used in conjunction with the other page selection options to select the even pages from a range of pages. </p>
<p> The <i>-o</i> option selects all of the odd pages; it may be used in conjunction with the other page selection options. </p>
<p> The <i>-ppages</i> option specifies the pages which are to be selected. <i>Pages</i> is a comma separated list of page ranges, each of which may be a page number, or a page range of the form <i>first</i>&#8211;<i>last</i>. If <i>first</i> is omitted, the first page is assumed, and if <i>last</i> is omitted, the last page is assumed. </p>
<p> The prefix character `_&#8217; indicates that the page number is relative to the end of the document, counting backwards. If just this character with no page number is used, a blank page will be inserted. </p>
<p> The <i>-r</i> option causes <i>psselect</i> to output the selected pages in reverse order. </p>
<p> Psselect normally prints the page numbers of the pages rearranged; the <i>-q</i> option suppresses this. </p>
<p> If any of the <i>-r, -e,</i> or <i>-o</i> options are specified, the page range must be given with the <i>-p</i> option. This is for backwards compatibility with previous versions. </p>
<h2>NOTES</h2>
<p> The page number given to <i>psselect</i> is the number of the page counting from the start or end of the file, starting at one. The actual page number in the document may be different.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>Psselect</i> does not accept all DSC comments. </p>
<h2>Index</h2>
