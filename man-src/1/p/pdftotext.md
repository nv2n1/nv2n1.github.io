---
title: "pdftotext(1)"
name: "pdftotext"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftotext/"
description: "pdftotext – Portable Document Format (PDF) to text converter (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdftotext &#8211; Portable Document Format (PDF) to text converter (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftotext</code> [options] [<i>PDF-file</i> [<i>text-file</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdftotext</code> converts Portable Document Format (PDF) files to plain text. </p>
<p> Pdftotext reads the PDF file, <i>PDF-file</i>, and writes a text file, <i>text-file</i>. If <i>text-file</i> is not specified, pdftotext converts <i>file.pdf</i> to <i>file.txt</i>. If <i>text-file</i> is &#8216;-&#8216;, the text is sent to stdout. If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to convert.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to convert.</dd>
<dt><code>-r</code><i> number</i></dt>
<dd> Specifies the resolution, in DPI. The default is 72 DPI.</dd>
<dt><code>-x</code><i> number</i></dt>
<dd> Specifies the x-coordinate of the crop area top left corner</dd>
<dt><code>-y</code><i> number</i></dt>
<dd> Specifies the y-coordinate of the crop area top left corner</dd>
<dt><code>-W</code><i> number</i></dt>
<dd> Specifies the width of crop area in pixels (default is 0)</dd>
<dt><code>-H</code><i> number</i></dt>
<dd> Specifies the height of crop area in pixels (default is 0)</dd>
<dt><code>-layout</code></dt>
<dd> Maintain (as best as possible) the original physical layout of the text. The default is to &#8216;undo&#8217; physical layout (columns, hyphenation, etc.) and output the text in reading order.</dd>
<dt><code>-fixed</code><i> number</i></dt>
<dd> Assume fixed-pitch (or tabular) text, with the specified character width (in points). This forces physical layout mode.</dd>
<dt><code>-raw</code></dt>
<dd> Keep the text in content stream order. This is a hack which often &quot;undoes&quot; column formatting, etc. Use of raw mode is no longer recommended.</dd>
<dt><code>-nodiag</code></dt>
<dd> Discard diagonal text (i.e., text that is not close to one of the 0, 90, 180, or 270 degree axes). This is useful for skipping watermarks drawn on body text.</dd>
<dt><code>-htmlmeta</code></dt>
<dd> Generate a simple HTML file, including the meta information. This simply wraps the text in &lt;pre&gt; and &lt;/pre&gt; and prepends the meta headers.</dd>
<dt><code>-bbox</code></dt>
<dd> Generate an XHTML file containing bounding box information for each word in the file.</dd>
<dt><code>-bbox-layout</code></dt>
<dd> Generate an XHTML file containing bounding box information for each block, line, and word in the file.</dd>
<dt><code>-cropbox</code></dt>
<dd> Use the crop box rather than the media box with -bbox and -bbox-layout.</dd>
<dt><code>-colspacing</code><i> number</i></dt>
<dd> Specifies how much spacing we allow after a word before considering adjacent text to be a new column, measured as a fraction of the font size. Current default is 0.7, old releases had a 0.3 default.</dd>
<dt><code>-enc</code><i> encoding-name</i></dt>
<dd> Sets the encoding to use for text output. This defaults to &quot;UTF-8&quot;.</dd>
<dt><code>-listenc</code></dt>
<dd> Lists the available encodings</dd>
<dt><code>-eol</code><i> unix | dos | mac</i></dt>
<dd> Sets the end-of-line convention to use for text output.</dd>
<dt><code>-nopgbrk</code></dt>
<dd> Don&#8217;t insert page breaks (form feed characters) between pages.</dd>
<dt><code>-opw</code><i> password</i></dt>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</dd>
<dt><code>-upw</code><i> password</i></dt>
<dd> Specify the user password for the PDF file.</dd>
<dt><code>-q</code></dt>
<dd> Don&#8217;t print any messages or errors.</dd>
<dt><code>-v</code></dt>
<dd> Print copyright and version information.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dd></dl>
<h2>BUGS</h2>
<p> Some PDF files contain fonts whose encodings have been mangled beyond recognition. There is no way (short of OCR) to extract text from these files.</p>
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
<p> The pdftotext software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
