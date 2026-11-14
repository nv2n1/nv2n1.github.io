---
title: "pdftohtml(1)"
name: "pdftohtml"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftohtml/"
description: "pdftohtml – program to convert PDF files into HTML, XML and PNG images"
---

<h2 class="name">NAME</h2>
<p> pdftohtml &#8211; program to convert PDF files into HTML, XML and PNG images </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftohtml</code> <i>[options] &lt;PDF-file&gt; [&lt;HTML-file&gt; &lt;XML-file&gt;]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pdftohtml</code> command. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. </p>
<p> <code>pdftohtml</code> is a program that converts PDF documents into HTML. It generates its output in the current working directory. If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin.</p>
<h2>OPTIONS</h2>
<p> A summary of options are included below.</p>
<dl>
<dt><code>-h, -help</code></p>
<dd> Show summary of options.</p>
<dt><code>-f &lt;int&gt;</code></p>
<dd> first page to print</p>
<dt><code>-l &lt;int&gt;</code></p>
<dd> last page to print</p>
<dt><code>-q</code></p>
<dd> do not print any messages or errors</p>
<dt><code>-v</code></p>
<dd> print copyright and version info</p>
<dt><code>-p</code></p>
<dd> exchange .pdf links with .html</p>
<dt><code>-c</code></p>
<dd> generate complex output</p>
<dt><code>-s</code></p>
<dd> generate single HTML that includes all pages</p>
<dt><code>-dataurls</code></p>
<dd> use data URLs instead of external images in HTML. No available in all platforms</p>
<dt><code>-i</code></p>
<dd> ignore images</p>
<dt><code>-noframes</code></p>
<dd> generate no frames. Not supported in complex output mode.</p>
<dt><code>-stdout</code></p>
<dd> use standard output</p>
<dt><code>-zoom &lt;fp&gt;</code></p>
<dd> zoom the PDF document (default 1.5) (1 means 72 DPI)</p>
<dt><code>-xml</code></p>
<dd> output for XML post-processing</p>
<dt><code>-noroundcoord</code></p>
<dd> do not round coordinates (with XML output only)</p>
<dt><code>-enc &lt;string&gt;</code></p>
<dd> output text encoding name</p>
<dt><code>-opw &lt;string&gt;</code></p>
<dd> owner password (for encrypted files)</p>
<dt><code>-upw &lt;string&gt;</code></p>
<dd> user password (for encrypted files)</p>
<dt><code>-hidden</code></p>
<dd> force hidden text extraction</p>
<dt><code>-fmt</code></p>
<dd> image file format for Splash output (png or jpg). If complex is selected, but -fmt is not specified, -fmt png will be assumed</p>
<dt><code>-nomerge</code></p>
<dd> do not merge paragraphs</p>
<dt><code>-nodrm</code></p>
<dd> override document DRM settings</p>
<dt><code>-wbt &lt;fp&gt;</code></p>
<dd> adjust the word break threshold percent. Default is 10. Word break occurs when distance between two adjacent characters is greater than this percent of character height.</p>
<dt><code>-fontfullname</code></p>
<dd> outputs the font name without any substitutions. </p>
</dl>
<h2>AUTHOR</h2>
<p> Pdftohtml was developed by Gueorgui Ovtcharov and Rainer Dorsch. It is based and benefits a lot from Derek Noonburg&#8217;s xpdf package. </p>
<p> This manual page was written by Søren Boll Overgaard &lt;boll [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
