---
title: "pdfmom(1)"
name: "pdfmom"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfmom/"
description: "pdfmom – produce PDF documents using the mom macro package for groff"
---

<h2 class="name">NAME</h2>
<p> pdfmom &#8211; produce PDF documents using the mom macro package for groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-Tpdf</code> ] [<i>groff-options</i>] <i>file</i> &#8230; <code>-Tps</code> [<i>pdfroff-options</i>] [<i>groff-options</i>] <i>file</i> &#8230; <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <i>pdfmom</i> is a wrapper around <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1) that facilitates the production of PDF documents from files formatted with the <i>mom</i> macros. </p>
<p> <i>pdfmom</i> prints to the standard output, so output must usually be redirected to a destination file. The size of the final PDF can be reduced by piping the output through <i><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></i>(1). </p>
<p> If called with the <code>-Tpdf</code> option (which is the default), <i>pdfmom</i> processes files using groff&#8217;s native PDF driver, <i><a href="/docs/linux/man/1-gropdf/">gropdf</a></i>(1). If <code>-Tps</code> is given, processing is passed over to <i>pdfroff</i>, which uses <i>groff</i>&#8216;s PostScript driver. In either case, multiple runs of the source file are performed in order to satisfy any forward references in the document. </p>
<p> <i>pdfmom</i> accepts all the same options as <i>groff</i>. If <code>-Tps</code> is given, the options associated with <i>pdfroff</i> are accepted as well. Please note that when <i>pdfmom</i> calls <i>pdfroff</i>, the</p>
<dl>
<dt>
<dd> <code>-mpdfmark -mom &#8211;no-toc</code></dl>
<p> options are implied and should not be given on the command line. Equally, it is not necessary to supply the <code>-mom</code> or <code>-m~mom</code> options when <code>-Tps</code> is absent. </p>
<p> PDF integration with the <i>mom</i> macros is discussed in full in the manual <i>Producing PDFs with groff and mom</i>, which was itself produced with <i>pdfmom</i>. </p>
<p> If called with the <code>-v</code> option, <i>pdfmom</i> simply displays its version information and exits.</p>
<h2>BUGS</h2>
<p> <i>pdfmom</i> sometimes issues warnings of the type</p>
<dl>
<dt>
<dd> &#8230;: can&#8217;t transparently output node at top level</dl>
<p> but this is more of an annoyance than a bug, and may safely be ignored.</p>
<h2>AUTHORS</h2>
<p> <i>pfdmom</i> was written by Deri James and Peter Schaffter</p>
<h2>SEE ALSO</h2>
<p> <i>Producing PDFs with groff and mom</i>, by Deri James and Peter Schaffter; a copy is installed at <i>/usr/:share/:doc/:groff-base/:pdf/:mom-pdf.pdf</i>. </p>
<p> <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-gropdf/">gropdf</a></i>(1), <i><a href="/docs/linux/man/1-pdfroff/">pdfroff</a></i>(1), <i><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></i>(1) </p>
<h2>Index</h2>
