---
title: "htmldoc(1)"
name: "htmldoc"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htmldoc/"
description: "htmldoc – convert html source files into html, postscript, or pdf."
---

<h2>NAME</h2>
<p> htmldoc &#8211; convert html source files into html, postscript, or pdf. </p>
<h2>SYNOPSIS</h2>
<p> htmldoc [options] filename1.html [ &#8230; filenameN.html ] </p>
<p> htmldoc [options] &#8211; </p>
<p> htmldoc [filename.book] </p>
<h2>DESCRIPTION</h2>
<p> <i>HTMLDOC</i> converts HTML source files into indexed HTML, PostScript, or Portable Document Format (PDF) files that can be viewed online or printed. With no options a HTML document is produced on stdout. </p>
<p> The second form of <i>HTMLDOC</i> reads HTML source from stdin, which allows you to use <i>HTMLDOC</i> as a filter. </p>
<p> The third form of <i>HTMLDOC</i> launches a graphical interface that allows you to change options and generate documents interactively.</p>
<h2>COMMON MISTAKES</h2>
<p> There are two types of HTML files &#8211; structured documents using headings (H1, H2, etc.) which <i>HTMLDOC</i> calls &quot;books&quot;, and unstructured documents that do not use headings which <i>HTMLDOC</i> calls &quot;web pages&quot;. </p>
<p> A very common mistake is to try converting a web page using:</p>
<dl>
<dt>htmldoc -f filename.pdf filename.html</dt>
<dd></dd></dl>
<p> which will likely produce a PDF file with no pages. To convert web page files you <code>must</code> use the <i>&#8211;webpage</i> or <i>&#8211;continuous</i> options at the command-line or choose <i>Web Page</i> or <i>Continuous</i> in the input tab of the GUI.</p>
<h2>OPTIONS</h2>
<p> The following command-line options are supported by <i>HTMLDOC</i>: </p>
<dl>
<dt>&#8211;batch <i>filename.book</i></dt>
<dd>
 Generates the specified book file without opening the GUI. </dd>
<dt>&#8211;bodycolor <i>color</i></dt>
<dd>
 Specifies the background color for all pages. </dd>
<dt>&#8211;bodyfont <i>{courier,helvetica,monospace,sans,serif,times}</i></dt>
<dd>
</dd><dt>&#8211;textfont <i>{courier,helvetica,monospace,sans,serif,times}</i></dt>
<dd>
 Specifies the default typeface for all normal text. </dd>
<dt>&#8211;bodyimage <i>filename</i></dt>
<dd>
 Specifies the background image that is tiled on all pages. </dd>
<dt>&#8211;book</dt>
<dd>
 Specifies that the HTML sources are structured (headings, chapters, etc.) </dd>
<dt>&#8211;bottom <i>margin</i></dt>
<dd>
 Specifies the bottom margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </dd>
<dt>&#8211;charset <i>{8859-1&#8230;8859-15}</i></dt>
<dd>
 Specifies the ISO character set to use for the output. </dd>
<dt>&#8211;color</dt>
<dd>
 Specifies that PostScript or PDF output should be in color. </dd>
<dt>&#8211;continuous</dt>
<dd>
 Specifies that the HTML sources are unstructured (plain web pages.) No page breaks are inserted between each file or URL in the output. </dd>
<dt>&#8211;datadir <i>directory</i></dt>
<dd>
 Specifies the location of the <i>HTMLDOC</i> data files, usually <i>/usr/share/htmldoc</i> or <i>C:\Program Files\HTMLDOC</i>. </dd>
<dt>&#8211;duplex</dt>
<dd>
 Specifies that the output should be formatted for double-sided printing. </dd>
<dt>&#8211;effectduration <i>{ 0.1..10.0 }</i></dt>
<dd>
 Specifies the duration in seconds of PDF page transition effects. </dd>
<dt>&#8211;embedfonts</dt>
<dd>
 Specifies that fonts should be embedded in PDF and PostScript output. </dd>
<dt>&#8211;encryption</dt>
<dd>
 Enables encryption of PDF files. </dd>
<dt>&#8211;fontsize <i>size</i></dt>
<dd>
 Specifies the default font size for body text. </dd>
<dt>&#8211;fontspacing <i>spacing</i></dt>
<dd>
 Specifies the default line spacing for body text. The line spacing is a multiplier for the font size, so a value of 1.2 will provide an additional 20% of space between the lines. </dd>
<dt>&#8211;footer <i>fff</i></dt>
<dd>
 Sets the page footer to use on body pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </dd>
<dt>&#8211;format <i>format</i></dt>
<dd>
</dd><dt>-t <i>format</i></dt>
<dd>
 Specifies the output format: html, htmlsep (separate HTML files for each heading in the table-of-contents), ps or ps2 (PostScript Level 2), ps1 (PostScript Level 1), ps3 (PostScript Level 3), pdf11 (PDF 1.1/Acrobat 2.0), pdf12 (PDF 1.2/Acrobat 3.0), pdf or pdf13 (PDF 1.3/Acrobat 4.0), or pdf14 (PDF 1.4/Acrobat 5.0). </dd>
<dt>&#8211;gray</dt>
<dd>
 Specifies that PostScript or PDF output should be grayscale. </dd>
<dt>&#8211;header <i>fff</i></dt>
<dd>
 Sets the page header to use on body pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </dd>
<dt>&#8211;headfootfont <i>font</i></dt>
<dd>
 Sets the font to use on headers and footers. </dd>
<dt>&#8211;headfootsize <i>size</i></dt>
<dd>
 Sets the size of the font to use on headers and footers. </dd>
<dt>&#8211;headingfont <i>typeface</i></dt>
<dd>
 Sets the typeface to use for headings. </dd>
<dt>&#8211;help</dt>
<dd>
 Displays a summary of command-line options. </dd>
<dt>&#8211;helpdir <i>directory</i></dt>
<dd>
 Specifies the location of the <i>HTMLDOC</i> on-line help files, usually <i>/usr/share/doc/htmldoc</i> or <i>C:\Program Files\HTMLDOC\DOC</i>. </dd>
<dt>&#8211;jpeg<i>[=quality]</i></dt>
<dd>
 Sets the JPEG compression level to use for large images. A value of 0 disables JPEG compression. </dd>
<dt>&#8211;left <i>margin</i></dt>
<dd>
 Specifies the left margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </dd>
<dt>&#8211;linkcolor <i>color</i></dt>
<dd>
 Sets the color of links. </dd>
<dt>&#8211;links</dt>
<dd>
 Enables generation of links in PDF files (default). </dd>
<dt>&#8211;linkstyle <i>{plain,underline}</i></dt>
<dd>
 Sets the style of links. </dd>
<dt>&#8211;logoimage <i>filename</i></dt>
<dd>
 Specifies an image to be used as a logo in the header or footer in a PostScript or PDF document, and in the navigation bar of a HTML document. </dd>
<p> Note that you need to use the <i>&#8211;header</i> and/or <i>&#8211;footer</i> options with the <i>l</i> parameter or use the corresponding HTML page comments to display the logo image in the header or footer. </p>
<dt>&#8211;no-compression</dt>
<dd>
 Disables compression of PostScript or PDF files. </dd>
<dt>&#8211;no-duplex</dt>
<dd>
 Disables double-sided printing. </dd>
<dt>&#8211;no-embedfonts</dt>
<dd>
 Specifies that fonts should not be embedded in PDF and PostScript output. </dd>
<dt>&#8211;no-encryption</dt>
<dd>
 Disables document encryption. </dd>
<dt>&#8211;no-jpeg</dt>
<dd>
 Disables JPEG compression of large images. </dd>
<dt>&#8211;no-links</dt>
<dd>
 Disables generation of links in a PDF document. </dd>
<dt>&#8211;no-numbered</dt>
<dd>
 Disables automatic heading numbering. </dd>
<dt>&#8211;no-pscommands</dt>
<dd>
 Disables generation of PostScript setpagedevice commands. </dd>
<dt>&#8211;no-strict</dt>
<dd>
 Disables strict HTML input checking. </dd>
<dt>&#8211;no-title</dt>
<dd>
 Disables generation of a title page. </dd>
<dt>&#8211;no-toc</dt>
<dd>
 Disables generation of a table of contents. </dd>
<dt>&#8211;numbered</dt>
<dd>
 Numbers all headings in a document. </dd>
<dt>&#8211;nup <i>pages</i></dt>
<dd>
 Sets the number of pages that are placed on each output page. Valid values are 1, 2, 4, 6, 9, and 16. </dd>
<dt>&#8211;outdir <i>directory</i></dt>
<dd>
</dd><dt>-d <i>directory</i></dt>
<dd>
 Specifies that output should be sent to a directory in multiple files. (Not compatible with PDF output) </dd>
<dt>&#8211;outfile <i>filename</i></dt>
<dd>
</dd><dt>-f <i>filename</i></dt>
<dd>
 Specifies that output should be sent to a single file. </dd>
<dt>&#8211;owner-password <i>password</i></dt>
<dd>
 Sets the owner password for encrypted PDF files. </dd>
<dt>&#8211;pageduration <i>{1.0..60.0}</i></dt>
<dd>
 Sets the view duration of a page in a PDF document. </dd>
<dt>&#8211;pageeffect <i>effect</i></dt>
<dd>
 Specifies the page transition effect for all pages; this attribute is ignored by all Adobe PDF viewers&#8230; </dd>
<dt>&#8211;pagelayout <i>{single,one,twoleft,tworight}</i></dt>
<dd>
 Specifies the initial layout of pages for a PDF file. </dd>
<dt>&#8211;pagemode <i>{document,outlines,fullscreen}</i></dt>
<dd>
 Specifies the initial viewing mode for a PDF file. </dd>
<dt>&#8211;path <i></dt>
<dd> Specifies a search path for files in a document. </dd>
<dt>&#8211;permissions permission[,permission,&#8230;]</i></dt>
<dd>
 Specifies document permissions for encrypted PDF files. The following permissions are understood: all, none, annotate, no-annotate, copy, no-copy, modify, no-modify, print, and no-print. Separate multiple permissions with commas. </dd>
<dt>&#8211;pscommands</dt>
<dd>
 Specifies that PostScript setpagedevice commands should be included in the output. </dd>
<dt>&#8211;quiet</dt>
<dd>
 Suppresses all messages, even error messages. </dd>
<dt>&#8211;referer <i>url</i></dt>
<dd>
 Specifies the URL that is passed in the Referer: field of HTTP requests. </dd>
<dt>&#8211;right <i>margin</i></dt>
<dd>
 Specifies the right margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </dd>
<dt>&#8211;size <i>pagesize</i></dt>
<dd>
 Specifies the page size using a standard name or in points (no suffix or ##x##pt), inches (##x##in), centimeters (##x##cm), or millimeters (##x##mm). The standard sizes that are currently recognized are &quot;letter&quot; (8.5x11in), &quot;legal&quot; (8.5x14in), &quot;a4&quot; (210x297mm), and &quot;universal&quot; (8.27x11in). </dd>
<dt>&#8211;strict</dt>
<dd>
 Enables strict HTML input checking. </dd>
<dt>&#8211;textcolor <i>color</i></dt>
<dd>
 Specifies the default color of all text. </dd>
<dt>&#8211;title</dt>
<dd>
 Enables the generation of a title page. </dd>
<dt>&#8211;titlefile <i>filename</i></dt>
<dd>
</dd><dt>&#8211;titleimage <i>filename</i></dt>
<dd>
 Specifies the file to use for the title page. If the file is an image then the title page is automatically generated using the document meta data and title image. </dd>
<dt>&#8211;tocfooter <i>fff</i></dt>
<dd>
 Sets the page footer to use on table-of-contents pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </dd>
<dt>&#8211;tocheader <i>fff</i></dt>
<dd>
 Sets the page header to use on table-of-contents pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </dd>
<dt>&#8211;toclevels <i>levels</i></dt>
<dd>
 Sets the number of levels in the table-of-contents. </dd>
<dt>&#8211;toctitle <i>string</i></dt>
<dd>
 Sets the title for the table-of-contents. </dd>
<dt>&#8211;top <i>margin</i></dt>
<dd>
 Specifies the top margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </dd>
<dt>&#8211;user-password <i>password</i></dt>
<dd>
 Specifies the user password for encryption of PDF files. </dd>
<dt>&#8211;verbose</dt>
<dd>
</dd><dt>-v</dt>
<dd>
 Provides verbose messages. </dd>
<dt>&#8211;version</dt>
<dd>
 Displays the current version number. </dd>
<dt>&#8211;webpage</dt>
<dd>
 Specifies that the HTML sources are unstructured (plain web pages.) A page break is inserted between each file or URL in the output. </dd>
</dl>
<h2>HEADER/FOOTER FORMATS</h2>
<p> The header and footer of each page can contain up to three preformatted values. These values are specified using a single character for the left, middle, and right of the page, resulting in the <i>fff</i> notation shown previously. </p>
<p> Each character can be one of the following: </p>
<dl>
<dt>.</dt>
<dd>
 blank </dd>
<dt>/</dt>
<dd>
 n/N arabic page numbers (1/3, 2/3, 3/3) </dd>
<dt>:</dt>
<dd>
 c/C arabic chapter page numbers (1/2, 2/2, 1/4, 2/4, &#8230;) </dd>
<dt>1</dt>
<dd>
 arabic numbers (1, 2, 3, &#8230;) </dd>
<dt>a</dt>
<dd>
 lowercase letters </dd>
<dt>A</dt>
<dd>
 uppercase letters </dd>
<dt>c</dt>
<dd>
 current chapter heading </dd>
<dt>C</dt>
<dd>
 current chapter page number (arabic) </dd>
<dt>d</dt>
<dd>
 current date </dd>
<dt>D</dt>
<dd>
 current date and time </dd>
<dt>h</dt>
<dd>
 current heading </dd>
<dt>i</dt>
<dd>
 lowercase roman numerals </dd>
<dt>I</dt>
<dd>
 uppercase roman numerals </dd>
<dt>l</dt>
<dd>
 logo image </dd>
<dt>t</dt>
<dd>
 title text </dd>
<dt>T</dt>
<dd>
 current time </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> HTMLDOC looks for several environment variables which can override the default directories, display additional debugging information, and disable CGI mode: </p>
<dl>
<dt>HTMLDOC_DATA</dt>
<dd>
 This environment variable specifies the location of HTMLDOC&#8217;s data and fonts directories, normally /usr/share/htmldoc or C:\Program Files\Easy Software Products\HTMLDOC. </dd>
<dt>HTMLDOC_DEBUG</dt>
<dd>
 This environment variable enables debugging information that is sent to stderr. The value is a list of any of the following keywords separated by spaces: &quot;all&quot;, &quot;links&quot;, &quot;memory&quot;, &quot;remotebytes&quot;, &quot;table&quot;, &quot;tempfiles&quot;, and/or &quot;timing&quot;. </dd>
<dt>HTMLDOC_HELP</dt>
<dd>
 This environment variable specifies the location of HTMLDOC&#8217;s documentation directory, normally /usr/share/doc/htmldoc or C:\Program Files\Easy Software Products\HTMLDOC\doc. </dd>
<dt>HTMLDOC_NOCGI</dt>
<dd>
 This environment variable, when set (the value doesn&#8217;t matter), disables CGI mode. It is most useful for using HTMLDOC on a web server from a scripting language or invocation from a program. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> HTMLDOC Software Users Manual </p>
<p> <a rel="nofollow" href="http://www.msweet.org/projects.php/HTMLDOC">http://www.msweet.org/projects.php/HTMLDOC</a></p>
<h2>AUTHOR</h2>
<p> Michael R Sweet</p>
<h2>COPYRIGHTS AND TRADEMARKS</h2>
<p> HTMLDOC is copyright 1997-2014 by Michael R Sweet. This program is free software. Distribution and use rights are outlined in the file &quot;COPYING.txt&quot;. </p>
<p> The Adobe Portable Document Format is Copyright 1985-2005 by Adobe Systems Incorporated. Adobe, FrameMaker, and PostScript are registered trademarks of Adobe Systems, Incorporated. </p>
<p> This software is based in part on the work of the Independent JPEG Group and FLTK project.</p>
<h2>NO WARRANTY</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
