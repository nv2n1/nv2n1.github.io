---
title: "pdfinfo(1)"
name: "pdfinfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfinfo/"
description: "pdfinfo – Portable Document Format (PDF) document information extractor (version 3.03)"
---

<h2 class="name">NAME</h2>
<p> pdfinfo &#8211; Portable Document Format (PDF) document information extractor (version 3.03) </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfinfo</code> [options] [<i>PDF-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pdfinfo</code> prints the contents of the &#8216;Info&#8217; dictionary (plus some other useful information) from a Portable Document Format (PDF) file. </p>
<p> If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The &#8216;Info&#8217; dictionary contains the following values: </p>
<dl>
<dt>
<dd> title</dl>
<dl>
<dt>
<dd> subject</dl>
<dl>
<dt>
<dd> keywords</dl>
<dl>
<dt>
<dd> author</dl>
<dl>
<dt>
<dd> creator</dl>
<dl>
<dt>
<dd> producer</dl>
<dl>
<dt>
<dd> creation date</dl>
<dl>
<dt>
<dd> modification date</dl>
<p> In addition, the following information is printed: </p>
<dl>
<dt>
<dd> custom metadata (yes/no)</dl>
<dl>
<dt>
<dd> metadata stream (yes/no)</dl>
<dl>
<dt>
<dd> tagged (yes/no)</dl>
<dl>
<dt>
<dd> userproperties (yes/no)</dl>
<dl>
<dt>
<dd> suspects (yes/no)</dl>
<dl>
<dt>
<dd> form (AcroForm / XFA / none)</dl>
<dl>
<dt>
<dd> javascript (yes/no)</dl>
<dl>
<dt>
<dd> page count</dl>
<dl>
<dt>
<dd> encrypted flag (yes/no)</dl>
<dl>
<dt>
<dd> print and copy permissions (if encrypted)</dl>
<dl>
<dt>
<dd> page size</dl>
<dl>
<dt>
<dd> file size</dl>
<dl>
<dt>
<dd> linearized (yes/no)</dl>
<dl>
<dt>
<dd> PDF version</dl>
<dl>
<dt>
<dd> metadata (only if requested)</dl>
<p> The options -listenc, -meta, -js, -struct, and -struct-text only print the requested information. The &#8216;Info&#8217; dictionary and related data listed above is not printed. At most one of these five options may be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></p>
<dd> Specifies the first page to examine. If multiple pages are requested using the &quot;-f&quot; and &quot;-l&quot; options, the size of each requested page (and, optionally, the bounding boxes for each requested page) are printed. Otherwise, only page one is examined.</p>
<dt><code>-l</code><i> number</i></p>
<dd> Specifies the last page to examine.</p>
<dt><code>-box</code></p>
<dd> Prints the page box bounding boxes: MediaBox, CropBox, BleedBox, TrimBox, and ArtBox.</p>
<dt><code>-meta</code></p>
<dd> Prints document-level metadata. (This is the &quot;Metadata&quot; stream from the PDF file&#8217;s Catalog object.)</p>
<dt><code>-custom</code></p>
<dd> Prints custom and standard metadata.</p>
<dt><code>-js</code></p>
<dd> Prints all JavaScript in the PDF.</p>
<dt><code>-struct</code></p>
<dd> Prints the logical document structure of a Tagged-PDF file.</p>
<dt><code>-struct-text</code></p>
<dd> Print the textual content along with the document structure of a Tagged-PDF file. Note that extracting text this way might be slow for big PDF files. (Implies <code>-struct</code>.)</p>
<dt><code>-url</code></p>
<dd> Print all URLs in the PDF. Only the URL types supported by Poppler are listed. Currently, this is limited to Annotations. Note: only URLs referenced by the PDF objects such as Link Annotations are listed. pdfinfo does not attempt to extract strings matching <a rel="nofollow" href="http://...">http://&#8230;</a> from the text content.</p>
<dt><code>-isodates</code></p>
<dd> Prints dates in ISO-8601 format (including the time zone).</p>
<dt><code>-rawdates</code></p>
<dd> Prints the raw (undecoded) date strings, directly from the PDF file.</p>
<dt><code>-dests</code></p>
<dd> Print a list of all named destinations. If a page range is specified using &quot;-f&quot; and &quot;-l&quot;, only destinations in the page range are listed.</p>
<dt><code>-enc</code><i> encoding-name</i></p>
<dd> Sets the encoding to use for text output. This defaults to &quot;UTF-8&quot;.</p>
<dt><code>-listenc</code></p>
<dd> Lits the available encodings</p>
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
<p> The pdfinfo software and documentation are copyright 1996-2011 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
<h2>Index</h2>
