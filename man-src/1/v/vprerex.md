---
title: "vprerex(1)"
name: "vprerex"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vprerex/"
description: "vprerex – graphical front-end and viewer for the"
---

<h2 class="name">NAME</h2>
<p> <code>vprerex</code> &#8211; graphical front-end and viewer for the <code></p>
<p> <a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) prerequisite-chart editor</p>
<h2>SYNOPSIS</h2>
<p> <code>vprerex</code> <i>basefile</i>[<i>.tex</i>] [ <i>chartfile</i>[<i>.tex</i>] ] </p>
<p> <code>vprerex</code> <i>file.pdf</i> </p>
<p> <code>vprerex</code></p>
<h2>DESCRIPTION</h2>
<p> <code>vprerex </code> (visual prerex) is a GUI front-end and viewer for the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) interactive editor of prerequisite-chart descriptions in the <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5) format. The viewer may be used just as a minimalistic viewer of arbitrary PDF files but supports editing of charts generated using <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7) by allowing coordinates of course boxes, arrows, and background points to be conveyed back to the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) command-line using the clipboard.</p>
<h2>USAGE</h2>
<p> If <code>vprerex</code> is invoked on a PDF file, it simply displays that file. </p>
<p> If the (first) argument does <i>not </i> have the .pdf suffix, it is assumed to be the base file for a LaTeX document containing a prerequisite-chart description in <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5) format, to be edited using <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1). If a <i>second</i> argument is supplied, it is regarded as an included file containing the specific chart environment to be edited. </p>
<p> If <i>no</i> arguments are supplied, a file-opening dialog allows the user the specify the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) base file to be edited (or the PDF file to be viewed); if a separate chartfile is needed, <code><a href="/docs/linux/man/1-vprerex/">vprerex</a></code>(1) must be invoked wth two arguments on the command line. </p>
<p> If the mouse hovers over a hyperlink in the PDF viewing window, the cursor shape will change to a pointing finger and a tooltip will display the URI. If the PDF file displayed contains a chart generated using <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7) and the background coordinate grid has been enabled, left-clicking the mouse on a course box, arrow mid-point, or background point will load the relevant coordinates into the X clipboard. The cursor shape changes to a plus-sign to indicate successful capture of the coordinates. Middle-clicking the mouse at the <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) command-line will then paste those coordinates into a command being composed. If the chart file is regenerated, the updated document will be re-loaded.</p>
<h2>DEPENDENCIES</h2>
<p> <code>vprerex</code> is based on the Qt-4 library. It calls <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) and <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1) for the editing window and uses <code>poppler-qt4</code> for rendering PDF files.</p>
<h2>AUTHOR</h2>
<p> R. D. Tennent (rdt [at] cs.queensu.ca), adapted from David Boddie&#8217;s PDFviewer, described in the QT Quarterly: <code><a rel="nofollow" href="http://doc.trolltech.com/qq/QtQuarterly27.pdf.">http://doc.trolltech.com/qq/QtQuarterly27.pdf.</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-prerex/">prerex</a></code>(1), <code><a href="/docs/linux/man/5-prerex/">prerex</a></code>(5), <code><a href="/docs/linux/man/7-prerex-sty/">prerex.sty</a></code>(7), and <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1). </p>
<h2>Index</h2>
