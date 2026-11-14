---
title: "pdffonts(1)"
name: "pdffonts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdffonts/"
description: "pdffonts – Portable Document Format (PDF) font analyzer (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdffonts &#8211; Portable Document Format (PDF) font analyzer (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdffonts</code> [options] [<i>PDF-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdffonts</code> lists the fonts used in a Portable Document Format (PDF) file along with various information for each font. </p>
<p> If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The following information is listed for each font:</p>
<dl>
<dt><code>name</code></p>
<dd> the font name, exactly as given in the PDF file (potentially including a subset prefix)</p>
<dt><code>type</code></p>
<dd> the font type &#8211; see below for details</p>
<dt><code>encoding</code></p>
<dd> the font encoding</p>
<dt><code>emb</code></p>
<dd> &quot;yes&quot; if the font is embedded in the PDF file</p>
<dt><code>sub</code></p>
<dd> &quot;yes&quot; if the font is a subset</p>
<dt><code>uni</code></p>
<dd> &quot;yes&quot; if there is an explicit &quot;ToUnicode&quot; map in the PDF file (the absence of a ToUnicode map doesn&#8217;t necessarily mean that the text can&#8217;t be converted to Unicode)</p>
<dt><code>object ID</code></p>
<dd> the font dictionary object ID (number and generation)</dl>
<p> PDF files can contain the following types of fonts: </p>
<dl>
<dt>
<dd> Type 1</dl>
<dl>
<dt>
<dd> Type 1C &#8211; aka Compact Font Format (CFF)</dl>
<dl>
<dt>
<dd> Type 3</dl>
<dl>
<dt>
<dd> TrueType</dl>
<dl>
<dt>
<dd> CID Type 0 &#8211; 16-bit font with no specified type</dl>
<dl>
<dt>
<dd> CID Type 0C &#8211; 16-bit PostScript CFF font</dl>
<dl>
<dt>
<dd> CID TrueType &#8211; 16-bit TrueType font</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to analyze.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to analyze.</p>
<dt><code>-subst</code></p>
<dd> List the substitute fonts that poppler will use for non embedded fonts.</p>
<dt><code>-opw</code><i> password</i></p>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</p>
<dt><code>-upw</code><i> password</i></p>
<dd> Specify the user password for the PDF file.</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</p>
<dd> No error.</p>
<dt>1</p>
<dd> Error opening a PDF file.</p>
<dt>2</p>
<dd> Error opening an output file.</p>
<dt>3</p>
<dd> Error related to PDF permissions.</p>
<dt>99</p>
<dd> Other error.</dl>
<h2>AUTHOR</h2>
<p> The pdffonts software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
