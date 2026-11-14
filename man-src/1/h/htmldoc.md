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
<dt>htmldoc -f filename.pdf filename.html</p>
<dd></dl>
<p> which will likely produce a PDF file with no pages. To convert web page files you <code>must</code> use the <i>&#8211;webpage</i> or <i>&#8211;continuous</i> options at the command-line or choose <i>Web Page</i> or <i>Continuous</i> in the input tab of the GUI.</p>
<h2>OPTIONS</h2>
<p> The following command-line options are supported by <i>HTMLDOC</i>: </p>
<dl>
<dt>&#8211;batch <i>filename.book</i></p>
<dd>
 Generates the specified book file without opening the GUI. </p>
<dt>&#8211;bodycolor <i>color</i></p>
<dd>
 Specifies the background color for all pages. </p>
<dt>&#8211;bodyfont <i>{courier,helvetica,monospace,sans,serif,times}</i></p>
<dd>
<dt>&#8211;textfont <i>{courier,helvetica,monospace,sans,serif,times}</i></p>
<dd>
 Specifies the default typeface for all normal text. </p>
<dt>&#8211;bodyimage <i>filename</i></p>
<dd>
 Specifies the background image that is tiled on all pages. </p>
<dt>&#8211;book</p>
<dd>
 Specifies that the HTML sources are structured (headings, chapters, etc.) </p>
<dt>&#8211;bottom <i>margin</i></p>
<dd>
 Specifies the bottom margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </p>
<dt>&#8211;charset <i>{8859-1&#8230;8859-15}</i></p>
<dd>
 Specifies the ISO character set to use for the output. </p>
<dt>&#8211;color</p>
<dd>
 Specifies that PostScript or PDF output should be in color. </p>
<dt>&#8211;continuous</p>
<dd>
 Specifies that the HTML sources are unstructured (plain web pages.) No page breaks are inserted between each file or URL in the output. </p>
<dt>&#8211;datadir <i>directory</i></p>
<dd>
 Specifies the location of the <i>HTMLDOC</i> data files, usually <i>/usr/share/htmldoc</i> or <i>C:\Program Files\HTMLDOC</i>. </p>
<dt>&#8211;duplex</p>
<dd>
 Specifies that the output should be formatted for double-sided printing. </p>
<dt>&#8211;effectduration <i>{ 0.1..10.0 }</i></p>
<dd>
 Specifies the duration in seconds of PDF page transition effects. </p>
<dt>&#8211;embedfonts</p>
<dd>
 Specifies that fonts should be embedded in PDF and PostScript output. </p>
<dt>&#8211;encryption</p>
<dd>
 Enables encryption of PDF files. </p>
<dt>&#8211;fontsize <i>size</i></p>
<dd>
 Specifies the default font size for body text. </p>
<dt>&#8211;fontspacing <i>spacing</i></p>
<dd>
 Specifies the default line spacing for body text. The line spacing is a multiplier for the font size, so a value of 1.2 will provide an additional 20% of space between the lines. </p>
<dt>&#8211;footer <i>fff</i></p>
<dd>
 Sets the page footer to use on body pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </p>
<dt>&#8211;format <i>format</i></p>
<dd>
<dt>-t <i>format</i></p>
<dd>
 Specifies the output format: html, htmlsep (separate HTML files for each heading in the table-of-contents), ps or ps2 (PostScript Level 2), ps1 (PostScript Level 1), ps3 (PostScript Level 3), pdf11 (PDF 1.1/Acrobat 2.0), pdf12 (PDF 1.2/Acrobat 3.0), pdf or pdf13 (PDF 1.3/Acrobat 4.0), or pdf14 (PDF 1.4/Acrobat 5.0). </p>
<dt>&#8211;gray</p>
<dd>
 Specifies that PostScript or PDF output should be grayscale. </p>
<dt>&#8211;header <i>fff</i></p>
<dd>
 Sets the page header to use on body pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </p>
<dt>&#8211;headfootfont <i>font</i></p>
<dd>
 Sets the font to use on headers and footers. </p>
<dt>&#8211;headfootsize <i>size</i></p>
<dd>
 Sets the size of the font to use on headers and footers. </p>
<dt>&#8211;headingfont <i>typeface</i></p>
<dd>
 Sets the typeface to use for headings. </p>
<dt>&#8211;help</p>
<dd>
 Displays a summary of command-line options. </p>
<dt>&#8211;helpdir <i>directory</i></p>
<dd>
 Specifies the location of the <i>HTMLDOC</i> on-line help files, usually <i>/usr/share/doc/htmldoc</i> or <i>C:\Program Files\HTMLDOC\DOC</i>. </p>
<dt>&#8211;jpeg<i>[=quality]</i></p>
<dd>
 Sets the JPEG compression level to use for large images. A value of 0 disables JPEG compression. </p>
<dt>&#8211;left <i>margin</i></p>
<dd>
 Specifies the left margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </p>
<dt>&#8211;linkcolor <i>color</i></p>
<dd>
 Sets the color of links. </p>
<dt>&#8211;links</p>
<dd>
 Enables generation of links in PDF files (default). </p>
<dt>&#8211;linkstyle <i>{plain,underline}</i></p>
<dd>
 Sets the style of links. </p>
<dt>&#8211;logoimage <i>filename</i></p>
<dd>
 Specifies an image to be used as a logo in the header or footer in a PostScript or PDF document, and in the navigation bar of a HTML document. </p>
<p> Note that you need to use the <i>&#8211;header</i> and/or <i>&#8211;footer</i> options with the <i>l</i> parameter or use the corresponding HTML page comments to display the logo image in the header or footer. </p>
<dt>&#8211;no-compression</p>
<dd>
 Disables compression of PostScript or PDF files. </p>
<dt>&#8211;no-duplex</p>
<dd>
 Disables double-sided printing. </p>
<dt>&#8211;no-embedfonts</p>
<dd>
 Specifies that fonts should not be embedded in PDF and PostScript output. </p>
<dt>&#8211;no-encryption</p>
<dd>
 Disables document encryption. </p>
<dt>&#8211;no-jpeg</p>
<dd>
 Disables JPEG compression of large images. </p>
<dt>&#8211;no-links</p>
<dd>
 Disables generation of links in a PDF document. </p>
<dt>&#8211;no-numbered</p>
<dd>
 Disables automatic heading numbering. </p>
<dt>&#8211;no-pscommands</p>
<dd>
 Disables generation of PostScript setpagedevice commands. </p>
<dt>&#8211;no-strict</p>
<dd>
 Disables strict HTML input checking. </p>
<dt>&#8211;no-title</p>
<dd>
 Disables generation of a title page. </p>
<dt>&#8211;no-toc</p>
<dd>
 Disables generation of a table of contents. </p>
<dt>&#8211;numbered</p>
<dd>
 Numbers all headings in a document. </p>
<dt>&#8211;nup <i>pages</i></p>
<dd>
 Sets the number of pages that are placed on each output page. Valid values are 1, 2, 4, 6, 9, and 16. </p>
<dt>&#8211;outdir <i>directory</i></p>
<dd>
<dt>-d <i>directory</i></p>
<dd>
 Specifies that output should be sent to a directory in multiple files. (Not compatible with PDF output) </p>
<dt>&#8211;outfile <i>filename</i></p>
<dd>
<dt>-f <i>filename</i></p>
<dd>
 Specifies that output should be sent to a single file. </p>
<dt>&#8211;owner-password <i>password</i></p>
<dd>
 Sets the owner password for encrypted PDF files. </p>
<dt>&#8211;pageduration <i>{1.0..60.0}</i></p>
<dd>
 Sets the view duration of a page in a PDF document. </p>
<dt>&#8211;pageeffect <i>effect</i></p>
<dd>
 Specifies the page transition effect for all pages; this attribute is ignored by all Adobe PDF viewers&#8230; </p>
<dt>&#8211;pagelayout <i>{single,one,twoleft,tworight}</i></p>
<dd>
 Specifies the initial layout of pages for a PDF file. </p>
<dt>&#8211;pagemode <i>{document,outlines,fullscreen}</i></p>
<dd>
 Specifies the initial viewing mode for a PDF file. </p>
<dt>&#8211;path <i></p>
<dd> Specifies a search path for files in a document. </p>
<dt>&#8211;permissions permission[,permission,&#8230;]</i></p>
<dd>
 Specifies document permissions for encrypted PDF files. The following permissions are understood: all, none, annotate, no-annotate, copy, no-copy, modify, no-modify, print, and no-print. Separate multiple permissions with commas. </p>
<dt>&#8211;pscommands</p>
<dd>
 Specifies that PostScript setpagedevice commands should be included in the output. </p>
<dt>&#8211;quiet</p>
<dd>
 Suppresses all messages, even error messages. </p>
<dt>&#8211;referer <i>url</i></p>
<dd>
 Specifies the URL that is passed in the Referer: field of HTTP requests. </p>
<dt>&#8211;right <i>margin</i></p>
<dd>
 Specifies the right margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </p>
<dt>&#8211;size <i>pagesize</i></p>
<dd>
 Specifies the page size using a standard name or in points (no suffix or ##x##pt), inches (##x##in), centimeters (##x##cm), or millimeters (##x##mm). The standard sizes that are currently recognized are &quot;letter&quot; (8.5x11in), &quot;legal&quot; (8.5x14in), &quot;a4&quot; (210x297mm), and &quot;universal&quot; (8.27x11in). </p>
<dt>&#8211;strict</p>
<dd>
 Enables strict HTML input checking. </p>
<dt>&#8211;textcolor <i>color</i></p>
<dd>
 Specifies the default color of all text. </p>
<dt>&#8211;title</p>
<dd>
 Enables the generation of a title page. </p>
<dt>&#8211;titlefile <i>filename</i></p>
<dd>
<dt>&#8211;titleimage <i>filename</i></p>
<dd>
 Specifies the file to use for the title page. If the file is an image then the title page is automatically generated using the document meta data and title image. </p>
<dt>&#8211;tocfooter <i>fff</i></p>
<dd>
 Sets the page footer to use on table-of-contents pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </p>
<dt>&#8211;tocheader <i>fff</i></p>
<dd>
 Sets the page header to use on table-of-contents pages. See the <i>HEADERS/FOOTERS FORMATS</i> section below. </p>
<dt>&#8211;toclevels <i>levels</i></p>
<dd>
 Sets the number of levels in the table-of-contents. </p>
<dt>&#8211;toctitle <i>string</i></p>
<dd>
 Sets the title for the table-of-contents. </p>
<dt>&#8211;top <i>margin</i></p>
<dd>
 Specifies the top margin in points (no suffix or ##pt), inches (##in), centimeters (##cm), or millimeters (##mm). </p>
<dt>&#8211;user-password <i>password</i></p>
<dd>
 Specifies the user password for encryption of PDF files. </p>
<dt>&#8211;verbose</p>
<dd>
<dt>-v</p>
<dd>
 Provides verbose messages. </p>
<dt>&#8211;version</p>
<dd>
 Displays the current version number. </p>
<dt>&#8211;webpage</p>
<dd>
 Specifies that the HTML sources are unstructured (plain web pages.) A page break is inserted between each file or URL in the output. </p>
</dl>
<h2>HEADER/FOOTER FORMATS</h2>
<p> The header and footer of each page can contain up to three preformatted values. These values are specified using a single character for the left, middle, and right of the page, resulting in the <i>fff</i> notation shown previously. </p>
<p> Each character can be one of the following: </p>
<dl>
<dt>.</p>
<dd>
 blank </p>
<dt>/</p>
<dd>
 n/N arabic page numbers (1/3, 2/3, 3/3) </p>
<dt>:</p>
<dd>
 c/C arabic chapter page numbers (1/2, 2/2, 1/4, 2/4, &#8230;) </p>
<dt>1</p>
<dd>
 arabic numbers (1, 2, 3, &#8230;) </p>
<dt>a</p>
<dd>
 lowercase letters </p>
<dt>A</p>
<dd>
 uppercase letters </p>
<dt>c</p>
<dd>
 current chapter heading </p>
<dt>C</p>
<dd>
 current chapter page number (arabic) </p>
<dt>d</p>
<dd>
 current date </p>
<dt>D</p>
<dd>
 current date and time </p>
<dt>h</p>
<dd>
 current heading </p>
<dt>i</p>
<dd>
 lowercase roman numerals </p>
<dt>I</p>
<dd>
 uppercase roman numerals </p>
<dt>l</p>
<dd>
 logo image </p>
<dt>t</p>
<dd>
 title text </p>
<dt>T</p>
<dd>
 current time </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> HTMLDOC looks for several environment variables which can override the default directories, display additional debugging information, and disable CGI mode: </p>
<dl>
<dt>HTMLDOC_DATA</p>
<dd>
 This environment variable specifies the location of HTMLDOC&#8217;s data and fonts directories, normally /usr/share/htmldoc or C:\Program Files\Easy Software Products\HTMLDOC. </p>
<dt>HTMLDOC_DEBUG</p>
<dd>
 This environment variable enables debugging information that is sent to stderr. The value is a list of any of the following keywords separated by spaces: &quot;all&quot;, &quot;links&quot;, &quot;memory&quot;, &quot;remotebytes&quot;, &quot;table&quot;, &quot;tempfiles&quot;, and/or &quot;timing&quot;. </p>
<dt>HTMLDOC_HELP</p>
<dd>
 This environment variable specifies the location of HTMLDOC&#8217;s documentation directory, normally /usr/share/doc/htmldoc or C:\Program Files\Easy Software Products\HTMLDOC\doc. </p>
<dt>HTMLDOC_NOCGI</p>
<dd>
 This environment variable, when set (the value doesn&#8217;t matter), disables CGI mode. It is most useful for using HTMLDOC on a web server from a scripting language or invocation from a program. </p>
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
