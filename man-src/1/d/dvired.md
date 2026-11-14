---
title: "dvired(1)"
name: "dvired"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvired/"
description: "dvired – print dvi-files"
---

<h2 class="name">NAME</h2>
<p> dvired &#8211; print dvi-files </p>
<h2>SYNOPSIS</h2>
<p> <code>dvired</code> [ <code>options</code> ] <code>file</code></p>
<h2>DESCRIPTION</h2>
<p> <i>dvired</i> behaves like <i>dvips</i>, except for the fact that two logical pages are put onto each physical sheet of paper. </p>
<p> For <i>options</i>, see <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1). This program only interprets the following options: </p>
<p> <i>-o file</i> &#8211; redirect output into <i>file.</i> </p>
<p> <i>-P printer</i> &#8211; direct output to <i>printer.</i> </p>
<p> <i>-f</i> &#8211; direct output to stdout. </p>
<p> Any other option is passed directly to <i>dvips</i>. </p>
<h2>EXAMPLES</h2>
<p> It is assumed that the PRINTER-variable is set. </p>
<p> <code>dvired -Plw foo</code> &#8211; send output to printer <i>lw</i>.<br />
 <code>dvired -o foo.ps foo</code> &#8211; send output to file <i>foo.ps</i>.<br />
 <code>dvired -pp4-7 foo</code> &#8211; send 4 pages (reduced onto 2 sheets) of <i>foo</i> to the printer.<br />
 <code>dvired foo -f | ghostview &#8211;</code> &#8211; preview output with ghostview. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1)</p>
<h2>BUGS</h2>
<p> <i>dvired</i> is fixed on A4 paper size. If you want to use it with other paper, you have to change the settings within the source.</p>
<h2>AUTHOR</h2>
<p> Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; </p>
<h2>Index</h2>
