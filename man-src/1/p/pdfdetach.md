---
title: "pdfdetach(1)"
name: "pdfdetach"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfdetach/"
description: "pdfdetach – Portable Document Format (PDF) document embedded file extractor (version 3.03)"
---

<h2>SYNOPSIS</h2>
<p> <code>pdfdetach</code> [options] [<i>PDF-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdfdetach</code> lists or extracts embedded files (attachments) from a Portable Document Format (PDF) file.</p>
<h2>OPTIONS</h2>
<p> Some of the following options can be set with configuration file commands. These are listed in square brackets with the description of the corresponding command line option.</p>
<dl>
<dt><code>-list</code></dt>
<dd> List all of the embedded files in the PDF file. File names are converted to the text encoding specified by the &quot;-enc&quot; switch.</dd>
<dt><code>-save</code><i> number</i></dt>
<dd> Save the specified embedded file. By default, this uses the file name associated with the embedded file (as printed by the &quot;-list&quot; switch); the file name can be changed with the &quot;-o&quot; switch.</dd>
<dt><code>-savefile</code><i> filename</i></dt>
<dd> Save the specified embedded file. By default, this uses the file name associated with the embedded file (as printed by the &quot;-list&quot; switch); the file name can be changed with the &quot;-o&quot; switch.</dd>
<dt><code>-saveall</code></dt>
<dd> Save all of the embedded files. This uses the file names associated with the embedded files (as printed by the &quot;-list&quot; switch). By default, the files are saved in the current directory; this can be changed with the &quot;-o&quot; switch.</dd>
<dt><code>-o</code><i> path</i></dt>
<dd> Set the file name used when saving an embedded file with the &quot;-save&quot; switch, or the directory used by &quot;-saveall&quot;.</dd>
<dt><code>-enc</code><i> encoding-name</i></dt>
<dd> Sets the encoding to use for text output (embedded file names). This defaults to &quot;UTF-8&quot;.</dd>
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
<p> The pdfinfo software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
