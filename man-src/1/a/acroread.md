---
title: "acroread(1)"
name: "acroread"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acroread/"
description: "acroread – Adobe PDF Viewer for viewing PDF files on X Window System."
---

<h2>NAME</h2>
<p> acroread &#8211; Adobe PDF Viewer for viewing PDF files on X Window System. </p>
<h2>SYNOPSIS</h2>
<p> <code>acroread</code> [<i>OPTIONS</i>] [<i>file</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Adobe Reader</code> is a free PDF reader, designed for standards compliance, performance and portability. It is a tool for opening and using Adobe PDFs that are created in Adobe Acrobat. Although you can&#8217;t create PDFs in Reader, you can use Reader to view, print, and manage PDFs. After opening a PDF in Reader, you have a variety of tools to help you find information quickly. If you receive a PDF form, you can complete it online and submit it electronically. If you receive an invitation to review a PDF, use the commenting and markup tools to annotate it. Use the Reader multimedia tools to play video and music in a PDF. And if a PDF contains sensitive information, you can sign or certify a document with a digital ID. </p>
<h2>OPTIONS</h2>
<p> A summary of the options supported by <code>acroread</code> is included below. </p>
<h3>acroread options</h3>
<dl>
<dt><code>&#8211;display=</code><i>DISPLAY</i></p>
<dd> X display to use</p>
<dt><code>&#8211;screen=</code><i>SCREEN</i></p>
<dd> X screen to use. Use this options to override the screen part of the DISPLAY environment variable.</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous</p>
<dt><code>-h, -help</code></p>
<dd> Prints the common command-line options.</p>
<dt><code>-geometry</code> <i>width</i>x<i>height</i></p>
<dd> Set height of startup window to <i>value</i>.</p>
<dt><code>-v, -version</code></p>
<dd> Print <code>acroread</code> version.</p>
<dt><code>-iconic</code></p>
<dd> Launches in an iconic state on the desktop.</p>
<dt><code>-setenv</code> <i>var</i>=<i>value</i></p>
<dd> Tells the main application to perform the equivalent of C-shell setenv <i>var</i> <i>value</i>.</p>
<dt><code>-tempFile</code></p>
<dd> Indicates files listed on the command line are temporary files and should not be put in the recent file list. The document title will be the title in the pdf document, instead of the filename.</p>
<dt><code>-tempFileTitle</code> <i>title</i></p>
<dd> Same as -tempFile, except the title is specified.</p>
<dt><code>-openInNewInstance</code></p>
<dd> It launches a new instance of acroread process. The application starts normally without checking if it is already running.</p>
<dt><code>-openInNewWindow</code></p>
<dd> Same as OpenInNewInstance. But it is recommended to use OpenInNewInstance. openInNewWindow will be deprecated.</p>
<dt><code>-installCertificate &lt;server-ip&gt; &lt;server-port&gt;</code></p>
<dd> Fetches and installs client-side certificates for authentication to access the server while creating secured connections.</p>
<dt><code>-installCertificate [-PEM|-DER] &lt;PathName&gt;</code></p>
<dd> Installs the certificate in the specified format from the given path to the Adobe Reader Certificate repository. </p>
<dt><code>/a</code></p>
<dd> Switch used to pass the file open parameters. To use more than one file open parameter, use &amp; as the separator and the options should be within quotes. See the example below:<br />
 acroread /a &quot;page=NUM &amp; zoom=NUM&quot; PDF_FILE.pdf</p>
<dl>
<dt>
<dd> <code>nameddest=name</code> &#8211; Specifies a named destination in the PDF.<br />
 <code>page=pagenum</code> &#8211; Specifies a numbered page in the document, using an integer value.<br />
 <code>zoom=scale</code> &#8211; Sets the zoom and scroll factors, using float or integer values.<br />
 <code>zoom=scale,left,top</code> &#8211; Scroll values left and top are in a coordinate system where 0,0 is the top left of the visible page, regardless of document rotation.<br />
 <code>view=&lt;option&gt;</code> &#8211; Set the view of the displayed page, using keyword values defined in the PDF Language Specification. Scroll values left and top are floats or integers in a coordinate system where 0,0 is the top left of the visible page, regardless of document rotation. Use the page command before this command.<br />
 <code>view=Fit</code><br />
 <code>view=FitH</code><br />
 <code>view=FitH,top</code><br />
 <code>view=FitV</code><br />
 <code>view=FitV,left</code><br />
 <code>view=FitB</code><br />
 <code>view=FitBH</code><br />
 <code>view=FitBH,top</code><br />
 <code>view=FitBV</code><br />
 <code>view=FitBV,left</code><br />
 <code>viewrect=left,top,wd,ht</code> &#8211; Sets the view rectangle using float or integer values in a coordinate system where 0,0 is the top left of the visible page, regardless of document rotation. Use the page command before this command.<br />
 <code>pagemode=&lt;option&gt;</code> &#8211; Displays bookmarks or thumbnails.<br />
 <code>pagemode=bookmarks</code><br />
 <code>pagemode=thumbs</code><br />
 <code>pagemode=none (default)</code><br />
 <code>scrollbar=1|0</code> &#8211; Turns scrollbars on or off.<br />
 <code>search=wordList</code> &#8211; Opens the Search UI and performs a search for the specified word list in the document. Found words are highlighted in the document. The words must be enclosed in quotes and separated by spaces; for example: #search=”word1 word2”<br />
 <code>toolbar=1|0</code> &#8211; Turns the toolbar on or off.<br />
 <code>highlight=lt,rt,top,btm</code> &#8211; Highlights a specified rectangle on the displayed page. (Use the page command before this command.) The rectangle values are integers in a coordinate system where 0,0 is the top left of the visible page, regardless of document rotation.<br />
 <code>help=indexcontentssearch</code> &#8211; Used only when opening a file from the command line or an Apple Event. Opens the document in the Help window, with the specified navigation panel selected.</dl>
<dt><code>-toPostScript</code> <i>options</i> <i>pdf-file</i> &#8230; <i>ps-dir</i></p>
<dd>
<dt><code>-toPostScript</code> <i>options</i> <i>-pairs</i> <i>pdf-file1</i> <i>ps-file1</i> &#8230;</p>
<dd>
<dt><code>-toPostScript </code><i>options</i></p>
<dd> Converts the given pdf_files to PostScript. </p>
<p> In the first form, if the last file specified is a directory, then all preceding files will be converted to PostScript and the generated PostScript files will be placed into ps-dir. If a directory is not specified, then the PostScript files will be placed in the same directory as the original file. </p>
<p> In the second form, the file list contains pairs, each consisting of a PDF filename and a corresponding PostScript filename. </p>
<p> The third form specifies a filter, reading a PDF file from standard input and writing the PostScript file to standardoutput. </p>
<p> Note: When using <code>-toPostScript</code> it must be the first argument passed in on the command line. </p>
<p> The following are valid options for the conversion of PDF to PostScript:</p>
<dl>
<dt>
<dd> <code>-printerName</code> &lt;name&gt; &#8211; this is to print device-dependent PS.<br />
 <code>-rotateAndCenter</code>&#8211; auto-rotate and center the pages.<br />
 <code>-choosePaperByPDFPageSize</code>&#8211; use the pdf page size to determine the output tray.<br />
 <code>-nUp</code>&#8211; &lt;hpage&gt; &lt;vpage&gt; &lt;pageorder&gt; border rotate &#8211; print multiple pages on the same sheet of paper.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hpage,vpage: can take numbers upto 99.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pageorder: how the pages are ordered on paper. Possible page orders are:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 (Horizontal)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 (HorizontalReversed)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 (Vertical)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>3 (VerticalReversed)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>border: draws the crop-box of PDF pages</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>rotate: automatically rotates each page</p>
<p> <code>-booklet</code> &lt;subset&gt; &lt;binding&gt; rotate &lt;from&gt; &lt;to&gt; &#8211; prints multiple pages on the same sheet of paper in the order required to read correctly when folded.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> subset: determines which side of the paper print. Possible options are :</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 (PrintBothSides)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 (PrintFrontSideOnly)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 (PrintBackSideOnly)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>from,to: specifies the first and last sheet to print.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>rotate: automatically rotates each page.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>binding: determines the orientation for the binding. Possible options are:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 (BookletBinding_Left)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 (BookletBinding_Right)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 (BookletBinding_LeftTall)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>3 (BookletBinding_RightTall)</p>
<p> <code>-binary</code> &#8211; emit binary PostScript where possible<br />
 <code>-start</code> <i>int</i> &#8211; identify the first page in the document to be converted (default is the first page of the document)<br />
 <code>-end</code> <i>int</i> &#8211; identify the last page in the document to be converted (default is the last page of the document)<br />
 <code>-optimizeForSpeed</code> &#8211; emit PostScript such that all fonts are emitted once at the beginning of the document. This results in faster transmission times and smaller PostScript documents but requires more PostScript printer virtual memory.<br />
 <code>-landscape</code> &#8211; rotate the pages to print landscape<br />
 <code>-reverse</code> &#8211; reverse the page order of the output<br />
 <code>-odd</code> &#8211; emit only odd-numbered pages<br />
 <code>-even</code> &#8211; emit only even-numbered pages<br />
 <code>-commentsOff</code> &#8211; don&#8217;t print comments<br />
 <code>-annotsOff</code> &#8211; don&#8217;t print annots<br />
 <code>-stampsOff</code> &#8211; don&#8217;t print stamps<br />
 <code>-markupsOn</code> &#8211; print document and markups<br />
 <code>-level2</code> &#8211; emit Level 2 PostScript (level1 is not supported)<br />
 <code>-level3</code> &#8211; emit Level 3 PostScript<br />
 <code>-printerhalftones</code> &#8211; use the printer default halftones.<br />
 <code>-saveVM</code> &#8211; download fonts as needed to preserve printer memory<br />
 <code>-scale</code> &lt;int&gt; &#8211; scale the pages according to the scale factor (default is 100 percent)<br />
 <code>-shrink</code> &#8211; shrink the pages to fit the page size<br />
 <code>-expand</code> &#8211; expand the pages to fit the page size<br />
 <code>-size</code> &lt;pagesize&gt; &#8211; set the page size. The following page sizes are recognized:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>letter &#8211; letter size paper</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tabloid &#8211; tabloid size paper</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ledger &#8211; ledger size paper</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>legal &#8211; legal size paper</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>executive &#8211; executive size paper</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a3 &#8211; ISO standard A3 size</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a4 &#8211; ISO standard A4 size</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a5 &#8211; ISO standard A5 size</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b4 &#8211; ISO standard B4 size</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b5 &#8211; ISO standard B5 size</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>wxh &#8211; custom size paper where w is the integer width in points and h is the integer height in points</p>
<p> <code>-transQuality</code> <i>level</i> &#8211; set the transparency flattening level Value from 1-5, where 1 means rasterize everything, 5 means rasterize as little as possible, default is 3.</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>Mutually exclusive options</code></p>
<dd> The following are the mutually exclusive print options, their usage together can lead to undesired results:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1. expand, shrink, nUp and booklet</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2. annotsOff, commentsOff, markupsOn and stampsOff</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>3. landscape and choosePaperByPDFPageSize</p>
</dl>
</dl>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> ACRO_DISABLE_FONT_CONFIG : Set this if you donot want Adobe Reader to cache Font-config fonts. </p>
<h2>VERSION</h2>
<p> 9.1.0 </p>
<h2>AUTHORS</h2>
<p> This program was written by <code>Adobe Systems Incorporated</code> <i><a rel="nofollow" href="http://www.adobe.com">http://www.adobe.com</a></i>. </p>
<h2>Index</h2>
