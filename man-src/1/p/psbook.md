---
title: "psbook(1)"
name: "psbook"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psbook/"
description: "psbook – rearrange pages in PostScript file into signatures"
---

<h2 class="name">NAME</h2>
<p> psbook &#8211; rearrange pages in PostScript file into signatures </p>
<h2>SYNOPSIS</h2>
<p> <code>psbook</code> [ <code>-q</code> ] [ <code>-s</code><i>signature</i> ] [ <i>infile</i> [ <i>outfile</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Psbook</i> rearranges pages from a PostScript document into &#8220;signatures&#8221; for printing books or booklets, creating a new PostScript file. The input PostScript file should follow the Adobe Document Structuring Conventions. </p>
<p> The <i>-s</i> option selects the size of signature which will be used. The signature size is the number of sides which will be folded and bound together; the number given should be a multiple of four. The default is to use one signature for the whole file. Extra blank sides will be added if the file does not contain a multiple of four pages. </p>
<p> Psbook normally prints the page numbers of the pages rearranged; the <i>-q</i> option suppresses this.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>Psbook</i> does not accept all DSC comments. </p>
<h2>Index</h2>
