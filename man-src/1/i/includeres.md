---
title: "includeres(1)"
name: "includeres"
section: "1"
letter: "i"
url: "/docs/linux/man/1-includeres/"
description: "includeres – filter to include resources in a PostScript document"
---

<h2 class="name">NAME</h2>
<p> includeres &#8211; filter to include resources in a PostScript document </p>
<h2>SYNOPSIS</h2>
<p> <code>includeres </code> &lt; <i>document.ps</i> &gt; <i>output.ps</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Includeres</i> includes resources (fonts, procsets, patterns, files, etc) in place of <i>%%IncludeResource</i> comments in a PostScript document. The resources are searched for in the current directory and the system default directory under the resource name, and with an appropriate extension. The pipeline </p>
<p> <center> extractres file.ps | includeres &gt;out.ps<br />
 </center> </p>
<p> will move all resources appearing in a document to the document prologue, removing redundant copies. The output file can then be put through page re-arrangement filters such as <i>psnup</i> or <i>pstops</i> safely.</p>
<h2>FILES</h2>
<p> /usr/lib/psutils &#8211; system resource directory.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) Angus J. C. Duggan 1991-1995</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-psbook/">psbook</a>(1), <a href="/docs/linux/man/1-psselect/">psselect</a>(1), <a href="/docs/linux/man/1-pstops/">pstops</a>(1), <a href="/docs/linux/man/1-epsffit/">epsffit</a>(1), <a href="/docs/linux/man/1-psnup/">psnup</a>(1), <a href="/docs/linux/man/1-psresize/">psresize</a>(1), <a href="/docs/linux/man/1-psmerge/">psmerge</a>(1), <a href="/docs/linux/man/1-fixscribeps/">fixscribeps</a>(1), <a href="/docs/linux/man/1-getafm/">getafm</a>(1), <a href="/docs/linux/man/1-fixdlsrps/">fixdlsrps</a>(1), <a href="/docs/linux/man/1-fixfmps/">fixfmps</a>(1), <a href="/docs/linux/man/1-fixpsditps/">fixpsditps</a>(1), <a href="/docs/linux/man/1-fixpspps/">fixpspps</a>(1), <a href="/docs/linux/man/1-fixtpps/">fixtpps</a>(1), <a href="/docs/linux/man/1-fixwfwps/">fixwfwps</a>(1), <a href="/docs/linux/man/1-fixwpps/">fixwpps</a>(1), <a href="/docs/linux/man/1-fixwwps/">fixwwps</a>(1), <a href="/docs/linux/man/1-extractres/">extractres</a>(1), <a href="/docs/linux/man/1-includeres/">includeres</a>(1), <a href="/docs/linux/man/1-showchar/">showchar</a>(1)</p>
<h2>TRADEMARKS</h2>
<p> <code>PostScript</code> is a trademark of Adobe Systems Incorporated.</p>
<h2>BUGS</h2>
<p> <i>includeres</i> does not alter the <i>%%DocumentNeededResources</i> comments. </p>
<h2>Index</h2>
