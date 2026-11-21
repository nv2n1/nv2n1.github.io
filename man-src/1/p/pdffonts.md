---
title: "pdffonts(1)"
name: "pdffonts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdffonts/"
description: "pdffonts – Portable Document Format (PDF) font analyzer (version 3.03)"
---

<h2>SYNOPSIS</h2>
<p> <code>pdffonts</code> [options] [<i>PDF-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdffonts</code> lists the fonts used in a Portable Document Format (PDF) file along with various information for each font. </p>
<p> If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The following information is listed for each font:</p>
<dl>
<dt><code>name</code></dt>
<dd> the font name, exactly as given in the PDF file (potentially including a subset prefix)</dd>
<dt><code>type</code></dt>
<dd> the font type &#8211; see below for details</dd>
<dt><code>encoding</code></dt>
<dd> the font encoding</dd>
<dt><code>emb</code></dt>
<dd> &quot;yes&quot; if the font is embedded in the PDF file</dd>
<dt><code>sub</code></dt>
<dd> &quot;yes&quot; if the font is a subset</dd>
<dt><code>uni</code></dt>
<dd> &quot;yes&quot; if there is an explicit &quot;ToUnicode&quot; map in the PDF file (the absence of a ToUnicode map doesn&#8217;t necessarily mean that the text can&#8217;t be converted to Unicode)</dd>
<dt><code>object ID</code></dt>
<dd> the font dictionary object ID (number and generation)</dd></dl>
<p> PDF files can contain the following types of fonts: </p>
<dl>
<dt>
</dt><dd> Type 1</dd></dl>
<dl>
<dt>
</dt><dd> Type 1C &#8211; aka Compact Font Format (CFF)</dd></dl>
<dl>
<dt>
</dt><dd> Type 3</dd></dl>
<dl>
<dt>
</dt><dd> TrueType</dd></dl>
<dl>
<dt>
</dt><dd> CID Type 0 &#8211; 16-bit font with no specified type</dd></dl>
<dl>
<dt>
</dt><dd> CID Type 0C &#8211; 16-bit PostScript CFF font</dd></dl>
<dl>
<dt>
</dt><dd> CID TrueType &#8211; 16-bit TrueType font</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to analyze.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to analyze.</dd>
<dt><code>-subst</code></dt>
<dd> List the substitute fonts that poppler will use for non embedded fonts.</dd>
<dt><code>-opw</code><i> password</i></dt>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</dd>
<dt><code>-upw</code><i> password</i></dt>
<dd> Specify the user password for the PDF file.</dd>
<dt><code>-v</code></dt>
<dd> Print copyright and version information.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dd></dl>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</dt>
<dd> No error.</dd>
<dt>1</dt>
<dd> Error opening a PDF file.</dd>
<dt>2</dt>
<dd> Error opening an output file.</dd>
<dt>3</dt>
<dd> Error related to PDF permissions.</dd>
<dt>99</dt>
<dd> Other error.</dd></dl>
<h2>AUTHOR</h2>
<p> The pdffonts software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
