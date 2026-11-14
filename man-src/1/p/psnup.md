---
title: "psnup(1)"
name: "psnup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psnup/"
description: "psnup – multiple pages per sheet"
---

<h2 class="name">NAME</h2>
<p> psnup &#8211; multiple pages per sheet </p>
<h2>SYNOPSIS</h2>
<p> <code>psnup</code> [ <code>-w</code><i>width</i> ] [ <code>-h</code><i>height</i> ] [ <code>-p</code><i>paper</i> ] [ <code>-W</code><i>width</i> ] [ <code>-H</code><i>height</i> ] [ <code>-P</code><i>paper</i> ] [ <code>-l</code> ] [ <code>-r</code> ] [ <code>-f</code> ] [ <code>-c</code> ] [ <code>-m</code><i>margin</i> ] [ <code>-b</code><i>border</i> ] [ <code>-d</code><i>lwidth</i> ] [ <code>-s</code><i>scale</i> ] [ <code>&#8211;</code><i>nup</i> ] [ <code>-q</code> ] [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Psnup</i> puts multiple logical pages onto each physical sheet of paper. The input PostScript file should follow the Adobe Document Structuring Conventions. </p>
<p> The <i>-w</i> option gives the paper width, and the <i>-h</i> option gives the paper height, normally specified in <code>cm</code> or <code>in</code>. The <i>-p</i> option can be used as an alternative, to set the paper size to <code>a0, a1, a2, a3, a4, a5, b5, letter, legal, tabloid, statement,</code> executive, folio, quarto or <code>10&#215;14.</code> The default paper size is normally <code>a4,</code> but on a Debian system, /etc/papersize is consulted. The <i>-W, -H,</i> and <i>-P</i> options set the input paper size, if it is different from the output size. This makes it easy to impose pages of one size on a different size of paper. </p>
<p> The <i>-l</i> option should be used for pages which are in landscape orientation (rotated 90 degrees anticlockwise). The <i>-r</i> option should be used for pages which are in seascape orientation (rotated 90 degrees clockwise), and the <i>-f</i> option should be used for pages which have the width and height interchanged, but are not rotated. </p>
<p> <i>Psnup</i> normally uses `row-major&#8217; layout, where adjacent pages are placed in rows across the paper. The <i>-c</i> option changes the order to `column-major&#8217;, where successive pages are placed in columns down the paper. </p>
<p> A margin to leave around the whole page can be specified with the <i>-m</i> option. This is useful for sheets of `thumbnail&#8217; pages, because the normal page margins are reduced by putting multiple pages on a single sheet. </p>
<p> The <i>-b</i> option is used to specify an additional margin around each page on a sheet. </p>
<p> The <i>-d</i> option draws a line around the border of each page, of the specified width. If the <i>lwidth</i> parameter is omitted, a default linewidth of 1 point is assumed. The linewidth is relative to the original page dimensions, <i>i.e.</i> it is scaled down with the rest of the page. </p>
<p> The scale chosen by <i>psnup</i> can be overridden with the <i>-s</i> option. This is useful to merge pages which are already reduced. </p>
<p> The <i>-nup</i> option selects the number of logical pages to put on each sheet of paper. This can be any whole number; <i>psnup</i> tries to optimise the layout so that the minimum amount of space is wasted. If <i>psnup</i> cannot find a layout within its tolerance limit, it will abort with an error message. The alternative form <i>-i nup</i> can also be used, for compatibility with other n-up programs. </p>
<p> <i>Psnup</i> normally prints the page numbers of the pages re-arranged; the <i>-q</i> option suppresses this.</p>
<h2>EXAMPLES</h2>
<p> The potential use of this utility is varied but one particular use is in conjunction with <i><a href="/docs/linux/man/1-psbook/">psbook</a>(1).</i> For example, using groff to create a PostScript document and lpr as the <font SIZE="-1">UNIX </font> print spooler a typical command line might look like this: </p>
<p> groff -Tps -ms <i>file</i> | psbook | psnup -2 | lpr </p>
<p> Where file is a 4 page document this command will result in a two page document printing two pages of <i>file</i> per page and rearranges the page order to match the input pages 4 and 1 on the first output page and pages 2 then 3 of the input document on the second output page.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>Psnup</i> does not accept all DSC comments. </p>
<h2>Index</h2>
