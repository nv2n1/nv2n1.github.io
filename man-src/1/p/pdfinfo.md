---

title: "pdfinfo(1)"
name: "pdfinfo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfinfo/"
description: "pdfinfo – Portable Document Format (PDF) document information extractor (version 3.03)"
---

<p> <code>pdfinfo</code> [options] [<i>PDF-file</i>]</p>
<p> <code>Pdfinfo</code> prints the contents of the &#8216;Info&#8217; dictionary (plus some other useful information) from a Portable Document Format (PDF) file. </p>
<p> If <i>PDF-file</i> is &#8216;-&#8216;, it reads the PDF file from stdin. </p>
<p> The &#8216;Info&#8217; dictionary contains the following values: </p>
<dl>
<dt>
</dt><dd> title</dd></dl>
<dl>
<dt>
</dt><dd> subject</dd></dl>
<dl>
<dt>
</dt><dd> keywords</dd></dl>
<dl>
<dt>
</dt><dd> author</dd></dl>
<dl>
<dt>
</dt><dd> creator</dd></dl>
<dl>
<dt>
</dt><dd> producer</dd></dl>
<dl>
<dt>
</dt><dd> creation date</dd></dl>
<dl>
<dt>
</dt><dd> modification date</dd></dl>
<p> In addition, the following information is printed: </p>
<dl>
<dt>
</dt><dd> custom metadata (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> metadata stream (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> tagged (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> userproperties (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> suspects (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> form (AcroForm / XFA / none)</dd></dl>
<dl>
<dt>
</dt><dd> javascript (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> page count</dd></dl>
<dl>
<dt>
</dt><dd> encrypted flag (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> print and copy permissions (if encrypted)</dd></dl>
<dl>
<dt>
</dt><dd> page size</dd></dl>
<dl>
<dt>
</dt><dd> file size</dd></dl>
<dl>
<dt>
</dt><dd> linearized (yes/no)</dd></dl>
<dl>
<dt>
</dt><dd> PDF version</dd></dl>
<dl>
<dt>
</dt><dd> metadata (only if requested)</dd></dl>
<p> The options -listenc, -meta, -js, -struct, and -struct-text only print the requested information. The &#8216;Info&#8217; dictionary and related data listed above is not printed. At most one of these five options may be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to examine. If multiple pages are requested using the &quot;-f&quot; and &quot;-l&quot; options, the size of each requested page (and, optionally, the bounding boxes for each requested page) are printed. Otherwise, only page one is examined.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to examine.</dd>
<dt><code>-box</code></dt>
<dd> Prints the page box bounding boxes: MediaBox, CropBox, BleedBox, TrimBox, and ArtBox.</dd>
<dt><code>-meta</code></dt>
<dd> Prints document-level metadata. (This is the &quot;Metadata&quot; stream from the PDF file&#8217;s Catalog object.)</dd>
<dt><code>-custom</code></dt>
<dd> Prints custom and standard metadata.</dd>
<dt><code>-js</code></dt>
<dd> Prints all JavaScript in the PDF.</dd>
<dt><code>-struct</code></dt>
<dd> Prints the logical document structure of a Tagged-PDF file.</dd>
<dt><code>-struct-text</code></dt>
<dd> Print the textual content along with the document structure of a Tagged-PDF file. Note that extracting text this way might be slow for big PDF files. (Implies <code>-struct</code>.)</dd>
<dt><code>-url</code></dt>
<dd> Print all URLs in the PDF. Only the URL types supported by Poppler are listed. Currently, this is limited to Annotations. Note: only URLs referenced by the PDF objects such as Link Annotations are listed. pdfinfo does not attempt to extract strings matching <a rel="nofollow" href="http://...">http://&#8230;</a> from the text content.</dd>
<dt><code>-isodates</code></dt>
<dd> Prints dates in ISO-8601 format (including the time zone).</dd>
<dt><code>-rawdates</code></dt>
<dd> Prints the raw (undecoded) date strings, directly from the PDF file.</dd>
<dt><code>-dests</code></dt>
<dd> Print a list of all named destinations. If a page range is specified using &quot;-f&quot; and &quot;-l&quot;, only destinations in the page range are listed.</dd>
<dt><code>-enc</code><i> encoding-name</i></dt>
<dd> Sets the encoding to use for text output. This defaults to &quot;UTF-8&quot;.</dd>
<dt><code>-listenc</code></dt>
<dd> Lits the available encodings</dd>
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
<p> <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdftocairo/">pdftocairo</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1) <code><a href="/docs/linux/man/1-pdfseparate/">pdfseparate</a></code>(1), <code><a href="/docs/linux/man/1-pdfsig/">pdfsig</a></code>(1), <code><a href="/docs/linux/man/1-pdfunite/">pdfunite</a></code>(1) </p>
