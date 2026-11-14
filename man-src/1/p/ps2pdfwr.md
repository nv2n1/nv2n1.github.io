---
title: "ps2pdfwr(1)"
name: "ps2pdfwr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2pdfwr/"
description: "ps2pdfwr – Convert PostScript to PDF without specifying CompatibilityLevel, using ghostscript"
---

<h2 class="name">NAME</h2>
<p> ps2pdfwr &#8211; Convert PostScript to PDF without specifying CompatibilityLevel, using ghostscript </p>
<h2>SYNOPSIS</h2>
<p> <code>ps2pdfwr</code> [options&#8230;] {input.[e]ps|-} [output.pdf|-]</p>
<h2>DESCRIPTION</h2>
<p> This wrapper script invokes <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) with following arguments </p>
<p> <center> <code>-q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite</code><br />
 </center> </p>
<p> as well as the appropriate <code>-dOutputFile</code> argument, all preceded and followed by any command-line arguments. Finally, the security option <code>-dSAFER</code> is prepended before all the other options (This is now redundant as &quot;SAFER&quot; is now the default, but the option does no harm). </p>
<p> The version-specific <code>ps2pdf</code> scripts all invoke this one with the addition of the respective compatibility level option.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. This manpage by George Ferguson. </p>
<h2>Index</h2>
