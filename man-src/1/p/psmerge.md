---
title: "psmerge(1)"
name: "psmerge"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psmerge/"
description: "psmerge – filter to merge several PostScript files into one"
---

<h2 class="name">NAME</h2>
<p> psmerge &#8211; filter to merge several PostScript files into one </p>
<h2>SYNOPSIS</h2>
<p> <code>psmerge </code> [ <code>-o</code><i>out.ps</i> ] <i>file.ps &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Psmerge</i> merges PostScript documents into a single document. It only works in the specific case the the files were created using the same application, with the same device setup and resources (fonts, procsets, patterns, files, etc) loaded. </p>
<p> If the <code>-o</code> option is used, output will be sent to the file named, otherwise it will go to standard output. </p>
<p> <i>Psmerge</i> will merge multiple files concatenated into a single file as if they were in separate files.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>psmerge</i> is for a very specific case; it does not merge files in the general case. </p>
<h2>Index</h2>
