---
title: "ps2pdf(1)"
name: "ps2pdf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2pdf/"
description: "ps2pdf – Convert PostScript to PDF using ghostscript ps2pdf12 – Convert PostScript to PDF 1.2 (Acrobat 3-and-later compatible) using ghostscript ps2pdf13 – Convert PostScript to PDF 1.3 (Acrobat 4-..."
---

<h2 class="name">NAME</h2>
<p> ps2pdf &#8211; Convert PostScript to PDF using ghostscript<br />
 ps2pdf12 &#8211; Convert PostScript to PDF 1.2 (Acrobat 3-and-later compatible) using ghostscript<br />
 ps2pdf13 &#8211; Convert PostScript to PDF 1.3 (Acrobat 4-and-later compatible) using ghostscript<br />
 ps2pdf14 &#8211; Convert PostScript to PDF 1.4 (Acrobat 5-and-later compatible) using ghostscript </p>
<h2>SYNOPSIS</h2>
<p> <code>ps2pdf</code> [options&#8230;] {input.[e]ps|-} [output.pdf|-]<br />
 <code>ps2pdf12</code> [options&#8230;] {input.[e]ps|-} [output.pdf|-]<br />
 <code>ps2pdf13</code> [options&#8230;] {input.[e]ps|-} [output.pdf|-]<br />
 <code>ps2pdf14</code> [options&#8230;] {input.[e]ps|-} [output.pdf|-]</p>
<h2>DESCRIPTION</h2>
<p> The <code>ps2pdf</code> scripts are work-alikes for nearly all the functionality (but not the user interface) of Adobe&#8217;s Acrobat(TM) Distiller(TM) product: they convert PostScript files to Portable Document Format (PDF) files. </p>
<p> If the output filename is not specified, the output is placed in a file of the same name with a &#8216;.pdf&#8217; extension in the current working directory. Either the input filename or the output filename can be &#8216;-&#8216; to request reading from stdin or writing to stdout, respectively, when used as a filter. </p>
<p> The three scripts differ as follows:</p>
<dl>
<dt>&#8211;</p>
<dd> <code>ps2pdf12</code> will always produce PDF 1.2 output (Acrobat 3-and-later compatible).</p>
<dt>&#8211;</p>
<dd> <code>ps2pdf13</code> will always produce PDF 1.3 output (Acrobat 4-and-later compatible).</p>
<dt>&#8211;</p>
<dd> <code>ps2pdf14</code> will always produce PDF 1.4 output (Acrobat 5-and-later compatible).</p>
<dt>&#8211;</p>
<dd> <code>ps2pdf</code> per se currently produces PDF 1.4 output. However, this may change in the future. If you care about the compatibility level of the output, use <code>ps2pdf12</code>, <code>ps2pdf13</code> or <code>ps2pdf14</code>, or use the <code>-dCompatibilityLevel=1.x</code> switch in the command line.</dl>
<p> There are some limitations in <code>ps2pdf</code>&#8216;s conversion. See the HTML documentation for more information. A large number of Adobe Distiller(TM) parameters which can be used to control the conversion are also documented there, including instructions for generating PDF/X and PDF/A documents.</p>
<h2>OPTIONS</h2>
<p> The <code>ps2pdf</code> scripts use the same options as <a href="/docs/linux/man/1-gs/">gs</a>(1).</p>
<h2>EXAMPLES</h2>
<p> Converting a figure.ps to figure.pdf:</p>
<dl>
<dt>
<dd> <code>ps2pdf</code> <i>figure.ps</i></dl>
<p> A conversion with more specifics:</p>
<dl>
<dt>
<dd> <code>ps2pdf</code> -dPDFSETTINGS=/prepress <i>figure.ps proof.pdf</i></dl>
<p> Converting as part of a pipe:</p>
<dl>
<dt>
<dd> <code>make_report.pl </code> -t ps | <code>ps2pdf</code> -dCompatibilityLevel=1.3 &#8211; &#8211; | <code>lpr</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-ps2pdfwr/">ps2pdfwr</a>(1),<br />
 VectorDevices.htm in the Ghostscript documentation</p>
<h2>BUGS</h2>
<p> See <a rel="nofollow" href="http://bugs.ghostscript.com/">http://bugs.ghostscript.com/</a> and the Usenet news group comp.lang.postscript.</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. This manpage by George Ferguson. </p>
<h2>Index</h2>
