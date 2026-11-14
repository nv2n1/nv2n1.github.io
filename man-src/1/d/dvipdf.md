---
title: "dvipdf(1)"
name: "dvipdf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvipdf/"
description: "dvipdf – Convert TeX DVI file to PDF using ghostscript and dvips"
---

<h2 class="name">NAME</h2>
<p> dvipdf &#8211; Convert TeX DVI file to PDF using ghostscript and dvips </p>
<h2>SYNOPSIS</h2>
<p> <code>dvipdf</code> [ <i>options</i> ] <i>input.dvi</i> [ <i>output.pdf</i> ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> This script invokes <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1) with the <code>-q</code> option, and pipes its output into <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) with the following options: </p>
<p> <center> <code>-q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite</code><br />
 </center> </p>
<p> as well as <code>-sOutputFile</code> and any options from the command-line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-dvips/">dvips</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. This manpage by George Ferguson. </p>
<h2>Index</h2>
