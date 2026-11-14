---
title: "pdf2dsc(1)"
name: "pdf2dsc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdf2dsc/"
description: "pdf2dsc – generate a PostScript page list of a PDF document"
---

<h2 class="name">NAME</h2>
<p> pdf2dsc &#8211; generate a PostScript page list of a PDF document </p>
<h2>SYNOPSIS</h2>
<p> <code>pdf2dsc</code> <i>input.pdf</i> [ <i>output.dsc</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pdf2dsc</code> uses <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to read an Adobe <code>Portable Document Format</code> (PDF) document &quot;input.pdf&quot; and create a <code>PostScript</code>(tm) document &quot;output.dsc&quot; that conforms to Adobe&#8217;s <code>Document Structuring Conventions</code> (DSC) requirements. </p>
<p> This new document simply tells Ghostscript to read the PDF file and to display pages one at a time. The generated document can then be viewed with any PostScript viewer based on Ghostscript, like <code><a href="/docs/linux/man/1-ghostview/">ghostview</a></code>(1) on Unix or <code>GSview</code> on Windows, with which the user can browse through the pages of the PDF document in any order. </p>
<p> If no output file is named on the command line, the name of the output file is that of the input file with any extension removed, followed by the extension &quot;.dsc&quot;.</p>
<h2>CAVEATS</h2>
<p> The DSC document uses Ghostscript-specific procedures. In addition, the original PDF document must be accessible when the DSC document is processed. </p>
<p> You need the file &quot;pdf2dsc.ps&quot; (originally by Russell Lang) supplied with Ghostscript since release 3.53.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-ghostview/">ghostview</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.55.0.</p>
<h2>AUTHOR</h2>
<p> Yves Arrouye &lt;yves.arrouye [at] usa.net&gt; and Russell Lang gsview at ghostgum.com.au </p>
<h2>Index</h2>
