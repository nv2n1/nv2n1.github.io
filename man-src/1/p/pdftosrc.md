---
title: "pdftosrc(1)"
name: "pdftosrc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftosrc/"
description: "pdftosrc – extract source file or stream from PDF file"
---

<h2 class="name">NAME</h2>
<p> pdftosrc &#8211; extract source file or stream from PDF file </p>
<h2>SYNOPSIS</h2>
<p> <code>pdftosrc</code> <i>PDF-file</i> [<i>stream-object-number</i>]</p>
<h2>DESCRIPTION</h2>
<p> If only <i>PDF-file</i> is given as argument, <code>pdftosrc</code> extracts the embedded source file from the first found stream object with /Type /SourceFile within the <i>PDF-file</i> and writes it to a file with the name /SourceName as defined in that PDF stream object (see application example below). </p>
<p> If both <i>PDF-file</i> and <i>stream-object-number</i> are given as arguments, and <i>stream-object-number</i> is positive, <code>pdftosrc</code> extracts and uncompresses the PDF stream of the object given by its <i>stream-object-number</i> from the <i>PDF-file</i> and writes it to a file named <i>PDF-file</i>.<i>stream-object-number</i> with the ending <code>.pdf</code> or <code>.PDF</code> stripped from the original <i>PDF-file</i> name. </p>
<p> A special case is related to XRef object streams that are part of the PDF standard from PDF-1.5 onward: If <i>stream-object-number</i> equals -1, then <code>pdftosrc</code> decompresses the XRef stream from the PDF file and writes it in human-readable PDF cross-reference table format to a file named <i>PDF-file</i><code>.xref</code> (these XRef streams can not be extracted just by giving their object number). </p>
<p> In any case an existing file with the output file name will be overwritten.</p>
<h2>OPTIONS</h2>
<p> None.</p>
<h2>FILES</h2>
<p> Just the executable <code>pdftosrc</code>.</p>
<h2>ENVIRONMENT</h2>
<p> None.</p>
<h2>DIAGNOSTICS</h2>
<p> At success the exit code of <code>pdftosrc</code> is 0, else 1. </p>
<p> All messages go to stderr. At program invocation, <code>pdftosrc</code> issues the current version number of the program <code>xpdf</code>, on which <code>pdftosrc</code> is based: </p>
<dl>
<dt>
<dd> pdftosrc version 3.01 </p>
</dl>
<p> When <code>pdftosrc</code> was successful with the output file writing, one of the following messages will be issued: </p>
<dl>
<dt>
<dd> Source file extracted to <i>source-file-name</i> </p>
</dl>
<p> or </p>
<dl>
<dt>
<dd> Stream object extracted to <i>PDF-file</i>.<i>stream-object-number</i> </p>
</dl>
<p> or </p>
<dl>
<dt>
<dd> Cross-reference table extracted to <i>PDF-file</i>.xref </p>
</dl>
<p> When the object given by the <i>stream-object-number</i> does not contain a stream, <code>pdftosrc</code> issues the following error message: </p>
<dl>
<dt>
<dd> Not a Stream object </p>
</dl>
<p> When the <i>PDF-file</i> can&#8217;t be opened, the error message is: </p>
<dl>
<dt>
<dd> Error: Couldn&#8217;t open file &#8216;<i>PDF-file</i>&#8216;. </p>
</dl>
<p> When <code>pdftosrc</code> encounters an invalid PDF file, the error message (several lines) is: </p>
<dl>
<dt>
<dd> Error: May not be a PDF file (continuing anyway)</dl>
<dl>
<dt>
<dd> (more lines)</dl>
<dl>
<dt>
<dd> Invalid PDF file </p>
</dl>
<p> There are also more error messages from <code>pdftosrc</code> for various kinds of broken PDF files.</p>
<h2>NOTES</h2>
<p> An embedded source file will be written out unchanged, i. e. it will not be uncompressed in this process. </p>
<p> Only the stream of the object will be written, i. e. not the dictionary of that object. </p>
<p> Knowing which <i>stream-object-number</i> to query requires information about the PDF file that has to be gained elsewhere, e. g. by looking into the PDF file with an editor. </p>
<p> The stream extraction capabilities of <code>pdftosrc</code> (e. g. regarding understood PDF versions and filter types) follow the capabilities of the underlying <code>xpdf</code> program version. </p>
<p> Currently the generation number of the stream object is not supported. The default value 0 (zero) is taken. </p>
<p> The wording <i>stream-object-number</i> has nothing to do with the `object streams&#8217; introduced by the Adobe PDF Reference, 5th edition, version 1.6.</p>
<h2>EXAMPLES</h2>
<p> When using pdftex, a source file can be embedded into some <i>PDF-file</i> by using pdftex primitives, as illustrated by the following example: </p>
<p> \immediate\pdfobj<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream attr&nbsp;{/Type&nbsp;/SourceFile&nbsp;/SourceName&nbsp;(myfile.zip)}</p>
<dl>
<dt>
<dd></dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;file{myfile.zip}</p>
<dl>
<dt>
<dd></dl>
<p> \pdfcatalog{/SourceObject 	he\pdflastobj\space 0 R} </p>
<p> Then this zip file can be extracted from the <i>PDF-file</i> by calling <code>pdftosrc</code> <i>PDF-file</i>.</p>
<h2>BUGS</h2>
<p> Not all embedded source files will be extracted, only the first found one. </p>
<p> Email bug reports to <code>pdftex [at] tug.org.</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdftex/">pdftex</a></code>(1),</p>
<h2>AUTHORS</h2>
<p> <code>pdftosrc</code> written by Han The Thanh, using <code>xpdf</code> functionality from Derek Noonburg. </p>
<p> Man page written by Hartmut Henkel.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1996-2006 Han The Thanh, &lt;thanh [at] pdftex.org&gt; </p>
<p> This file is part of pdfTeX. </p>
<p> pdfTeX is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> pdfTeX is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with pdfTeX; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>Index</h2>
