---
title: "html2ps(1)"
name: "html2ps"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html2ps/"
description: "html2ps – convert HTML to PostScript"
---

<h2 class="name">NAME</h2>
<p> html2ps &#8211; convert HTML to PostScript </p>
<h2>SYNOPSIS</h2>
<p> <code>html2ps</code> [ <code>-2cdDFghHLnORtTuUv</code> ] [ <code>-b</code><i> URL</i> ] [ <code>-C</code><i> string</i> ] [ <code>-e</code><i> encoding</i> ] [ <code>-f</code><i> file[:file[:&#8230;]]</i> ] [ <code>-i</code><i> num</i> ] [ <code>-k</code><i> file</i> ] [ <code>-l</code><i> lang</i> ] [ <code>-m</code><i> num</i> ] [ <code>-M</code><i> num</i> ] [ <code>-N</code><i> num</i> ] [ <code>-o</code><i> file</i> ] [ <code>-r</code><i> path</i> ] [ <code>-s</code><i> num</i> ] [ <code>-S</code><i> string</i> ] [ <code>-W</code><i> string</i> ] [ <code>-x</code><i> num</i> ] [ <i>URL|file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The program <code>html2ps</code> converts HTML to PostScript. The HTML code can be retrieved from one or more URL:s or local files, specified as parameters on the command line. If no parameter is given, html2ps reads from standard input. </p>
<p> Note: To avoid unnecessary network traffic, one can rebuild an already generated PostScript file with new options. This is done by running html2ps with the new options, and with the old PostScript file as input (not applicable for all options).</p>
<h2>OPTIONS</h2>
<p> All options have a short (case sensitive), and a long (case insensitive) form.</p>
<dl>
<dt><code>-2 &#8211;twoup </code></p>
<dd> Two column (2-up) output. The default is one column per page.</p>
<dt><code>-b </code><i>URL</i> &#8211;base <i>URL</i></p>
<dd> Use <i>URL</i> as a base to expand relative references for in-line images. This is useful if you have downloaded a document to a local file. The <i>URL</i> should then be the <i>URL</i> of the original document.</p>
<dt><code>-c &#8211;check </code></p>
<dd> Check the syntax of the HTML file (using an external syntax checker). The default is to not make a syntax check.</p>
<dt><code>-C </code><i>string</i> &#8211;toc <i>string</i></p>
<dd> Generate a table of contents (ToC). The value should be a string consisting of one of the letters &#8216;f&#8217;, &#8216;h&#8217;, or &#8216;t&#8217;, optionally combined with the letter &#8216;b&#8217;:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>b</code></p>
<dd> The ToC will be printed first. This requires that Ghostscript is installed.</p>
<dt><code>f</code></p>
<dd> The ToC will be generated from the links in the converted document.</p>
<dt><code>h</code></p>
<dd> The ToC will be generated from headings and titles in the converted documents. Note that if the document author for some strange reason has chosen to use some other means to represent the headings than the HTML elements H1,&#8230;,H6, you are out of luck!</p>
<dt><code>t</code></p>
<dd> The ToC will be generated from links having the attribute rev=TOC in the converted document.</dl>
</dl>
<dl>
<dt><code>-d &#8211;debug </code></p>
<dd> Generate debugging information. You should always use this option when reporting problems with html2ps.</p>
<dt><code>-D &#8211;dsc &#8211;DSC </code></p>
<dd> Generate DSC compliant PostScript. This requires Ghostscript and can take quite some time to do. Note that a PostScript file generated with this option cannot be used as input to html2ps for reformatting later.</p>
<dt><code>-e </code><i>encoding</i> &#8211;encoding <i>encoding</i></p>
<dd> The document encoding. Currently recognized values are ISO-8859-1, EUC-JP, SHIFT-JIS, and ISO-2022-JP (other EUC-xx encodings may also work). The default is ISO-8859-1.</p>
<dt><code>-f </code><i>file[:file[:&#8230;]]</i> &#8211;rcfile <i>file[:file[:&#8230;]]</i></p>
<dd> A colon separated list of configuration file names to use instead of the default personal configuration file $HOME/.html2psrc. Definitions made in one file override definitions in previous files (the last file in the list has highest precedence). An empty file name (as in &#8216;:file&#8217;, &#8216;file1::file3&#8217;, or &#8216;file:&#8217;) will expand to the default personal file. The environment variable HTML2PSPATH is used to specify the directories where to search for these files. (Note: this is only supposed to be used on the command line, not in a configuration file.)</p>
<dt><code>-F &#8211;frame </code></p>
<dd> Draw a frame around the text on each page. The default is to not draw a frame.</p>
<dt><code>-g &#8211;grayscale </code></p>
<dd> Convert colour images to grayscale images. Note that the PostScript file will be smaller when the images are converted to grayscale. The default is to generate colour images.</p>
<dt><code>-h &#8211;help </code></p>
<dd> Show usage information.</p>
<dt><code>-H &#8211;hyphenate </code></p>
<dd> Hyphenate the text. This requires TeX hyphenation pattern files.</p>
<dt><code>-i </code><i>num</i> &#8211;scaleimage <i>num</i></p>
<dd> Scale in-line images with a factor <i>num</i> The default is 1.</p>
<dt><code>-k </code><i>file</i> &#8211;cookie <i>file</i></p>
<dd> Enable cookie support, using a netscape formatted cookie <i>file</i> (requires libwww-perl).</p>
<dt><code>-l </code><i>lang</i> &#8211;language <i>lang</i></p>
<dd> Specifies the language of the document (overrides an eventual LANG attribute of the BODY element). The language should be given according to RFC1766 (<a href="ftp://ftp.nordu.net/rfc/rfc1766.txt)">ftp://ftp.nordu.net/rfc/rfc1766.txt)</a> and ISO 639 (<a rel="nofollow" href="http://www.w3.org/WAI/ER/IG/ert/iso639.htm">http://www.w3.org/WAI/ER/IG/ert/iso639.htm</a>).</p>
<dt><code>-L &#8211;landscape </code></p>
<dd> Generate code for printing in landscape mode. The default is portrait mode.</p>
<dt><code>-m </code><i>num</i> &#8211;scalemath <i>num</i></p>
<dd> Scale mathematical formulas with a factor <i>num</i> The default is 1.</p>
<dt><code>-M </code><i>num</i> &#8211;mainchapter <i>num</i></p>
<dd> Specifies the start number for automatic numbering of headings (by setting the seq-number parameter), the default is 1.</p>
<dt><code>-n &#8211;number </code></p>
<dd> Insert page numbers. The default is to not number the pages.</p>
<dt><code>-N </code><i>num</i> &#8211;startno <i>num</i></p>
<dd> Specifies the starting page number, the default is 1.</p>
<dt><code>-o </code><i>file</i> &#8211;output <i>file</i></p>
<dd> Write the PostScript code to <i>file.</i> The default is to write to standard output.</p>
<dt><code>-O &#8211;original </code></p>
<dd> Use PostScript original images if they exist. For example, if a document contains an image figure.gif, and an encapsulated PostScript file named figure.ps exists in the same directory, that file will be use instead. This only work for documents read as local files. Note: if the PostScript file is large or contains bitmap images, this must be combined with the -D option. In HTML 4.0 this can be achieved in a much better way with:</p>
<dl>
<dt>
<dd>
<p> &lt;OBJECT data=&quot;figure.ps&quot; type=&quot;application/postscript&quot;&gt; </p>
<p> &lt;OBJECT data=&quot;figure.gif&quot; type=&quot;image/gif&quot;&gt; </p>
<p> &lt;PRE&gt;[Maybe some ASCII art for text browsers]&lt;/PRE&gt; </p>
<p> &lt;/OBJECT&gt; </p>
<p> &lt;/OBJECT&gt;</dl>
</dl>
<dl>
<dt><code>-r </code><i>path</i> &#8211;rootdir <i>path</i></p>
<dd> When a document is read from a local file, this value specifies a base directory for resolving relative links starting with &quot;/&quot;. Typically, this should be the directory where your web server&#8217;s home page resides.</p>
<dt><code>-R &#8211;xref </code></p>
<dd> Insert cross references at every link to within the set of converted documents.</p>
<dt><code>-s </code><i>num</i> &#8211;scaledoc <i>num</i></p>
<dd> Scale the entire document with a factor <i>num</i> The default is 1.</p>
<dt><code>-S </code><i>string</i> &#8211;style <i>string</i></p>
<dd> This option complements/overrides definitions made in the configuration files. The <i>string</i> must follow the configuration file syntax. (Note: this is only supposed to be used on the command line, not in a configuration file.)</p>
<dt><code>-t &#8211;titlepage </code></p>
<dd> Generate a title page. The default is to not generate one.</p>
<dt><code>-T &#8211;text </code></p>
<dd> Text mode, ignore images. The default is to include the images.</p>
<dt><code>-u &#8211;underline </code></p>
<dd> Underline text that constitutes a hypertext link. The default is to not underline.</p>
<dt><code>-U &#8211;colour </code></p>
<dd> Produce colour output for text and background, when specified. The default is black text on white background (mnemonic: coloUr ;-).</p>
<dt><code>-v &#8211;version </code></p>
<dd> Print information about the current version of html2ps.</p>
<dt><code>-W </code><i>string</i> &#8211;web <i>string</i></p>
<dd> Process a web of documents by recursively retrieve and convert documents that are referenced with hyperlinks. When dealing with remote documents it will of course be necessary to impose restrictions, to avoid downloading the entire web&#8230; The value should be a string consisting of one of the letters &#8216;a&#8217;, &#8216;b&#8217;, &#8216;l&#8217;, &#8216;r&#8217;, or &#8216;s&#8217;, optionally combined with a combination of the letters &#8216;p&#8217;, &#8216;L&#8217;, and a positive integer:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>a</code></p>
<dd> Follow all links.</p>
<dt><code>b</code></p>
<dd> Follow only links to within the same directory, or below, as the start document.</p>
<dt><code>l</code></p>
<dd> Follow only links specified with &quot;&lt;LINK rel=NEXT&gt;&quot; in the document.</p>
<dt><code>p</code></p>
<dd> Prompt for each remote document. This mode will automatically be entered after the first 50 documents.</p>
<dt><code>r</code></p>
<dd> Follow only relative links.</p>
<dt><code>s</code></p>
<dd> Follow only links to within the same server as the start document.</p>
<dt><code>L</code></p>
<dd> With this option, the order in which the documents are processed will be: first all top level documents, then the documents linked to from these etc. For example, if the document A has links to B and C, and B has a link to D, the order will be A-B-C-D. By default, each document will be followed by the first document it links to etc; so the default order for the example is A-B-D-C.</p>
<dt><code>#</code></p>
<dd> A positive integer giving the number of recursive levels. The default is 4 (when the option is present).</dl>
</dl>
<dl>
<dt><code>-x </code><i>num</i> &#8211;duplex <i>num</i></p>
<dd> Generate postscript code for single or double sided printing. No default, valid values are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Single sided.</p>
<dt><code>1</code></p>
<dd> Double sided.</p>
<dt><code>2</code></p>
<dd> Double sided, opposite page reversed (tumble mode).</dl>
</dl>
<h2>BUGS</h2>
<p> (This is incomplete.) </p>
<p> The CELLSPACING attribute of the TABLE element is not implemented as described in the specification; instead the value of the CELLPADDING attribute is increased by half the value of CELLSPACING. </p>
<p> Rendering HTML tables well is a non-trivial task. For &quot;real&quot; tables, that is representation of tabular data, html2ps usually generates reasonably good output. When tables are used for layout purposes, the result varies from good to useless. This is because a table cell is never broken across pages. So if a table contains a cell with a lot of content, the entire table may have to be scaled down in size in order to make this cell fit on a single page. Sometimes this may even result in unreadable output. </p>
<p> Page breaks are occasionally done in bad places: for example directly after a (long) heading, and before the last line in a paragraph.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>HTML2PSPATH</p>
<dd> This variable specifies the directories to search for configuration files. It should be a colon separated list of directory names. Use a dot &#8216;.&#8217; to denote the current directory. An empty directory name (as in &#8216;:dir&#8217;, &#8216;dir1::dir3&#8217;, or &#8216;dir:&#8217;) will expand to the directory where the global configuration file is. The default value is &#8216;.:&#8217;, that is: search the current directory first, and then the global one. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.html2psrc</p>
<dd> User configuration file, see <a href="/docs/linux/man/5-html2psrc/">html2psrc</a>(5).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-html2psrc/">html2psrc</a>(5), <a href="/docs/linux/man/1-perl/">perl</a>(1), <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3), <a href="/docs/linux/man/3-strftime/">strftime</a>(3), <a href="/docs/linux/man/1-weblint/">weblint</a>(1)</p>
<h2>VERSION</h2>
<p> This manpage describes html2ps version 1.0 beta7.</p>
<h2>AVAILABILITY</h2>
<p> <a rel="nofollow" href="http://user.it.uu.se/~jan/html2ps.html">http://user.it.uu.se/~jan/html2ps.html</a></p>
<h2>AUTHOR</h2>
<p> Jan Karrman (jan [at] it.uu.se) </p>
<h2>Index</h2>
