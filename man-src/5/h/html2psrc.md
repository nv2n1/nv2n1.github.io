---
title: "html2psrc(5)"
name: "html2psrc"
section: "5"
letter: "h"
url: "/docs/linux/man/5-html2psrc/"
description: "html2psrc – configuration file format for html2ps(1)"
---

<p>html2psrc &#8211; configuration file format for <a href="/docs/linux/man/1-html2ps/">html2ps</a>(1)</p>
<h2>Description</h2>
<p>Configuration files are used for layout control, resource information etc. Normally, there should always exist a global configuration file. In this file one typically specify things like: what image conversion packages are available on the system, the default paper size, the default text fonts and sizes, etc. </p>
<p> For Unix and Windows systems, the installation script &#8216;install&#8217; can be used to automatically build a global configuration file with all necessary definitions, and install all files. The files replaced by the installation are saved. If you for some reason are not satisfied with the new version: execute the script &#8216;backout&#8217; to reinstall your earlier version. </p>
<p> On other systems, you will have to manually create a global configuration file, and insert the name of this file into the html2ps script (close to the beginning, the line starting with &quot;$globrc=&quot;). The configuration file should contain a package block, and perhaps paper and hyphenation blocks, described below. </p>
<p> Each user can then have a personal configuration file (by default $HOME/.html2psrc) that complements/overrides the definitions made in the global file. It is also possible to specify alternative files on the command line, using the -f option.</p>
<h2>File Format</h2>
<p>A configuration file can include other configuration files. This is done with:</p>
<dl>
<dd></dl>
<dl>
<dd>@import &quot;<i>filename</i>&quot;;</dl>
<p> The rest of the configuration file consists of zero or more blocks. A block is given by a block name, followed by the block definition, as in:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>BODY {</dl>
<dl>
<dd>font-size: 12pt; </p>
<p> font-family: Helvetica; </p>
<p> text-align: justify</dl>
<dl>
<dd>}</dl>
<p> The block definition, enclosed by curly braces: { }, consists of key-value pairs and/or other blocks. A key-value pair consists of the key name followed by a colon, followed by the value. Blocks and key-value pairs are separated by semicolons. The semicolon may be omitted after a block. </p>
<p> Several blocks can share the same definition. The block names are then separated be commas, as in:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>H2, H4, H6 { font-style: italic }</dl>
<p> A comment in a configuration file starts with the characters &quot;/*&quot; and ends with &quot;*/&quot;:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>@html2ps {</dl>
<dl>
<dd>seq-number: 1; /* Automatic numbering of headings */</dl>
<dl>
<dd>}</dl>
<p> Notations </p>
<p> Here are some definitions of terms used below: </p>
<dl>
<dd>
<dl>
<dt><code>Flag:</code></p>
<dd>A value of either 0 (absence, inactive etc) or 1 (presence, active etc).</p>
<dt><code>Absolute size:</code></p>
<dd>A real number optionally followed by one of the following two-letter unit identifiers: cm (centimeters), mm (millimeters), in (inches), pt (points, 1pt = 1/72 inch), pc (picas, 1pc = 12pt). The default unit is centimeters.</p>
<dt><code>Relative size:</code></p>
<dd>A size relative to current fontsize. The default and currently only recognized unit is em. One em equals the size of the current font. The value should be given as a real number, optionally followed by &#8217;em&#8217;, as in &#8216;0.25em&#8217;.</p>
<dt><code>Whitespace:</code></p>
<dd>Any one of the characters: space, tab, newline, or carriage return.</dl>
</dl>
<p> CSS2 blocks </p>
<p> All blocks, except one: the @html2ps block, coincides with a subset of the Cascading Style Sheets, level 2 CSS2 Specification (<a rel="nofollow" href="http://www.w3.org/TR/REC-CSS2/">http://www.w3.org/TR/REC-CSS2/</a>). The following default settings for html2ps illustrate just about everything that currently can be used from the CSS2 specification:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>BODY {</dl>
<dl>
<dd>font-family: Times; </p>
<p> font-size: 11pt; </p>
<p> text-align: left; </p>
<p> background: white;</dl>
<dl>
<dd>} </p>
<p> H1, H2, H3, H4, H5, H6 {</dl>
<dl>
<dd>font-weight: bold; </p>
<p> margin-top: 0.8em; </p>
<p> margin-bottom: 0.5em;</dl>
<dl>
<dd>} </p>
<p> H1 { font-size: 19pt } </p>
<p> H2 { font-size: 17pt } </p>
<p> H3 { font-size: 15pt } </p>
<p> H4 { font-size: 13pt } </p>
<p> H5 { font-size: 12pt } </p>
<p> H6 { font-size: 11pt } </p>
<p> P, OL, UL, DL, BLOCKQUOTE, PRE {</dl>
<dl>
<dd>margin-top: 1em; </p>
<p> margin-bottom: 1em;</dl>
<dl>
<dd>} </p>
<p> P {</dl>
<dl>
<dd>line-height: 1.2em; </p>
<p> text-indent: 0;</dl>
<dl>
<dd>} </p>
<p> OL, UL, DD { margin-left: 2em } </p>
<p> TT, KBD, PRE { font-family: Courier } </p>
<p> PRE { font-size: 9pt } </p>
<p> BLOCKQUOTE {</dl>
<dl>
<dd>margin-left: 1em; </p>
<p> margin-right: 1em;</dl>
<dl>
<dd>} </p>
<p> ADDRESS {</dl>
<dl>
<dd>margin-top: 0.5em; </p>
<p> margin-bottom: 0.5em;</dl>
<dl>
<dd>} </p>
<p> TABLE {</dl>
<dl>
<dd>margin-top: 1.3em; </p>
<p> margin-bottom: 1em;</dl>
<dl>
<dd>} </p>
<p> DIV.noprint { display: none } </p>
<p> DEL { text-decoration: line-through } </p>
<p> A:link, HR { color: black } </p>
<p> @page {</dl>
<dl>
<dd>margin-left: 2.5cm; </p>
<p> margin-right: 2.5cm; </p>
<p> margin-top: 3cm; </p>
<p> margin-bottom: 3cm;</dl>
<dl>
<dd>}</dl>
<p> The program specific block <i>@html2ps</i>: </p>
<p> This block is used to specify parameters that are specific to html2ps, and not covered by CSS2. The @html2ps block has several sub-blocks and key-value pairs, these are described in this section.</p>
<dl>
<dt>The <i>package</i> block</p>
<dd>
<dl>
<dd>This block is used to specify which program packages are installed on the system. Typically, this is done in the global configuration file.</p>
<dl>
<dt><code>PerlMagick</code></p>
<dd>A flag specifying whether the Perl module PerlMagick is installed or not. The default is 0.</p>
<dt><code>ImageMagick</code></p>
<dd>A flag specifying whether the ImageMagick package is installed or not. The default is 0.</p>
<dt><code>pbmplus</code></p>
<dd>A flag specifying whether the pbmplus package is installed or not. The default is 0.</p>
<dt><code>netpbm</code></p>
<dd>A flag specifying whether the netpbm package is installed or not. The default is 0.</p>
<dt><code>djpeg</code></p>
<dd>A flag specifying whether djpeg is installed or not. The default is 0.</p>
<dt><code>Ghostscript</code></p>
<dd>A flag specifying whether Ghostscript is installed or not. The default is 0.</p>
<dt><code>TeX</code></p>
<dd>A flag specifying whether the TeX package is installed or not. The default is 0.</p>
<dt><code>dvips</code></p>
<dd>A flag specifying whether dvips is installed or not. The default is 0.</p>
<dt><code>libwww-perl</code></p>
<dd>A flag specifying whether the Perl module library libwww-perl is installed or not. The default is 0.</p>
<dt><code>geturl</code></p>
<dd>When neither of the Perl packages for retrieving remote documents are available, it is possible to use some other program like wget or lynx. This value should be set to a command that retrieves a document with a complete MIME header, such as &quot;wget -s -q -O-&quot; or &quot;lynx -source -mime_header&quot;.</p>
<dt><code>check</code></p>
<dd>The name of a program used for syntax checking HTML documents. No default, a good choice is weblint.</p>
<dt><code>path</code></p>
<dd>A colon separated list of directories where the executables from the program packages are. It is only necessary to include directories that are not in the PATH for a typical user.</dl>
</dl>
<dt>The <i>paper</i> block</p>
<dd>
<dl>
<dd>The paper size is defined in this block. The size can either be given as one of the recognized paper types or by giving explicit values for the paper height and width. As of version 1.0 beta2, one can also use the @page block in CSS2 for the paper size. The paper block is kept for backwards compatibility. Also, one can only specify explicit dimensions in @page, not any paper types by name.</p>
<dl>
<dt><code>type</code></p>
<dd>Paper type, possible choices are: A0, A1, A2, A3, A4,&#8230;,A10, B0, B1,&#8230;,B10, letter, legal, arche, archd, archc, archb, archa, flsa, flse, halfletter, 11&#215;17, and ledger (this set of paper types is taken from Aladdin Ghostscript). The default is A4.</p>
<dt><code>height</code></p>
<dd>An absolute size specifying the paper height.</p>
<dt><code>width</code></p>
<dd>An absolute size specifying the paper width.</dl>
</dl>
<dt>The <i>option</i> block</p>
<dd>
<dl>
<dd>This block is used to set default values for the command line options. The key in the key-value pair is the option name, in either its long or short form.</p>
<dl>
<dt><code>twoup</code></p>
<dd>Two column (2-up) output. The default is one column per page.</p>
<dt><code>base</code></p>
<dd>Use <i>URL</i> as a base to expand relative references for in-line images. This is useful if you have downloaded a document to a local file. The <i>URL</i> should then be the <i>URL</i> of the original document.</p>
<dt><code>check</code></p>
<dd>Check the syntax of the HTML file (using an external syntax checker). The default is to not make a syntax check.</p>
<dt><code>toc</code></p>
<dd>Generate a table of contents (ToC). The value should be a string consisting of one of the letters &#8216;f&#8217;, &#8216;h&#8217;, or &#8216;t&#8217;, optionally combined with the letter &#8216;b&#8217;:</dl>
<dl>
<dd>
<dl>
<dt><code>b</code></p>
<dd>The ToC will be printed first. This requires that Ghostscript is installed.</p>
<dt><code>f</code></p>
<dd>The ToC will be generated from the links in the converted document.</p>
<dt><code>h</code></p>
<dd>The ToC will be generated from headings and titles in the converted documents. Note that if the document author for some strange reason has chosen to use some other means to represent the headings than the HTML elements H1,&#8230;,H6, you are out of luck!</p>
<dt><code>t</code></p>
<dd>The ToC will be generated from links having the attribute rev=TOC in the converted document.</dl>
</dl>
<dl>
<dt><code>debug</code></p>
<dd>Generate debugging information. You should always use this option when reporting problems with html2ps.</p>
<dt><code>DSC</code></p>
<dd>Generate DSC compliant PostScript. This requires Ghostscript and can take quite some time to do. Note that a PostScript file generated with this option cannot be used as input to html2ps for reformatting later.</p>
<dt><code>encoding</code></p>
<dd>The document encoding. Currently recognized values are ISO-8859-1, EUC-JP, SHIFT-JIS, and ISO-2022-JP (other EUC-xx encodings may also work). The default is ISO-8859-1.</p>
<dt><code>rcfile</code></p>
<dd>A colon separated list of configuration file names to use instead of the default personal configuration file $HOME/.html2psrc. Definitions made in one file override definitions in previous files (the last file in the list has highest precedence). An empty file name (as in &#8216;:file&#8217;, &#8216;file1::file3&#8217;, or &#8216;file:&#8217;) will expand to the default personal file. The environment variable HTML2PSPATH is used to specify the directories where to search for these files. (Note: this is only supposed to be used on the command line, not in a configuration file.)</p>
<dt><code>frame</code></p>
<dd>Draw a frame around the text on each page. The default is to not draw a frame.</p>
<dt><code>grayscale</code></p>
<dd>Convert colour images to grayscale images. Note that the PostScript file will be smaller when the images are converted to grayscale. The default is to generate colour images.</p>
<dt><code>help</code></p>
<dd>Show usage information.</p>
<dt><code>hyphenate</code></p>
<dd>Hyphenate the text. This requires TeX hyphenation pattern files.</p>
<dt><code>scaleimage</code></p>
<dd>Scale in-line images with a factor <i>num</i>. The default is 1.</p>
<dt><code>cookie</code></p>
<dd>Enable cookie support, using a netscape formatted cookie <i>file</i> (requires libwww-perl).</p>
<dt><code>language</code></p>
<dd>Specifies the language of the document (overrides an eventual LANG attribute of the BODY element). The language should be given according to RFC1766 (<a href="ftp://ftp.nordu.net/rfc/rfc1766.txt)">ftp://ftp.nordu.net/rfc/rfc1766.txt)</a> and ISO 639 (<a rel="nofollow" href="http://www.w3.org/WAI/ER/IG/ert/iso639.htm">http://www.w3.org/WAI/ER/IG/ert/iso639.htm</a>).</p>
<dt><code>landscape</code></p>
<dd>Generate code for printing in landscape mode. The default is portrait mode.</p>
<dt><code>scalemath</code></p>
<dd>Scale mathematical formulas with a factor <i>num</i>. The default is 1.</p>
<dt><code>mainchapter</code></p>
<dd>Specifies the start number for automatic numbering of headings (by setting the seq-number parameter), the default is 1.</p>
<dt><code>number</code></p>
<dd>Insert page numbers. The default is to not number the pages.</p>
<dt><code>startno</code></p>
<dd>Specifies the starting page number, the default is 1.</p>
<dt><code>output</code></p>
<dd>Write the PostScript code to <i>file.</i> The default is to write to standard output.</p>
<dt><code>original</code></p>
<dd>Use PostScript original images if they exist. For example, if a document contains an image figure.gif, and an encapsulated PostScript file named figure.ps exists in the same directory, that file will be use instead. This only work for documents read as local files. Note: if the PostScript file is large or contains bitmap images, this must be combined with the -D option. In HTML 4.0 this can be achieved in a much better way with:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>&lt;OBJECT data=&quot;figure.ps&quot; type=&quot;application/postscript&quot;&gt;</dl>
<dl>
<dd>&lt;OBJECT data=&quot;figure.gif&quot; type=&quot;image/gif&quot;&gt;</dl>
<dl>
<dd>&lt;PRE&gt;[Maybe some ASCII art for text browsers]&lt;/PRE&gt;</dl>
<dl>
<dd>&lt;/OBJECT&gt;</dl>
<dl>
<dd>&lt;/OBJECT&gt;</dl>
</dl>
<dl>
<dt><code>rootdir</code></p>
<dd>When a document is read from a local file, this value specifies a base directory for resolving relative links starting with &quot;/&quot;. Typically, this should be the directory where your web server&#8217;s home page resides.</p>
<dt><code>xref</code></p>
<dd>Insert cross references at every link to within the set of converted documents.</p>
<dt><code>scaledoc</code></p>
<dd>Scale the entire document with a factor <i>num</i>. The default is 1.</p>
<dt><code>style</code></p>
<dd>This option complements/overrides definitions made in the configuration files. The <i>string</i> must follow the configuration file syntax. (Note: this is only supposed to be used on the command line, not in a configuration file.)</p>
<dt><code>titlepage</code></p>
<dd>Generate a title page. The default is to not generate one.</p>
<dt><code>text</code></p>
<dd>Text mode, ignore images. The default is to include the images.</p>
<dt><code>underline</code></p>
<dd>Underline text that constitutes a hypertext link. The default is to not underline.</p>
<dt><code>colour</code></p>
<dd>Produce colour output for text and background, when specified. The default is black text on white background (mnemonic: coloUr ;-).</p>
<dt><code>version</code></p>
<dd>Print information about the current version of html2ps.</p>
<dt><code>web</code></p>
<dd>Process a web of documents by recursively retrieve and convert documents that are referenced with hyperlinks. When dealing with remote documents it will of course be necessary to impose restrictions, to avoid downloading the entire web&#8230; The value should be a string consisting of one of the letters &#8216;a&#8217;, &#8216;b&#8217;, &#8216;l&#8217;, &#8216;r&#8217;, or &#8216;s&#8217;, optionally combined with a combination of the letters &#8216;p&#8217;, &#8216;L&#8217;, and a positive integer:</dl>
<dl>
<dd>
<dl>
<dt><code>a</code></p>
<dd>Follow all links.</p>
<dt><code>b</code></p>
<dd>Follow only links to within the same directory, or below, as the start document.</p>
<dt><code>l</code></p>
<dd>Follow only links specified with &quot;&lt;LINK rel=NEXT&gt;&quot; in the document.</p>
<dt><code>p</code></p>
<dd>Prompt for each remote document. This mode will automatically be entered after the first 50 documents.</p>
<dt><code>r</code></p>
<dd>Follow only relative links.</p>
<dt><code>s</code></p>
<dd>Follow only links to within the same server as the start document.</p>
<dt><code>L</code></p>
<dd>With this option, the order in which the documents are processed will be: first all top level documents, then the documents linked to from these etc. For example, if the document A has links to B and C, and B has a link to D, the order will be A-B-C-D. By default, each document will be followed by the first document it links to etc; so the default order for the example is A-B-D-C.</p>
<dt><code>#</code></p>
<dd>A positive integer giving the number of recursive levels. The default is 4 (when the option is present).</dl>
</dl>
<dl>
<dt><code>duplex</code></p>
<dd>Generate postscript code for single or double sided printing. No default, valid values are:</dl>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Single sided.</p>
<dt><code>1</code></p>
<dd>Double sided.</p>
<dt><code>2</code></p>
<dd>Double sided, opposite page reversed (tumble mode).</dl>
</dl>
</dl>
<dt>The <i>margin</i> block</p>
<dd>
<dl>
<dd>This block is used to specify page margins. The left, right, top and bottom margins, previously defined with this block, should now be defined using the @page construction from CSS2.</p>
<dl>
<dt><code>middle</code></p>
<dd>An absolute size for the distance between the columns when printing two columns per page, default is 2cm.</dl>
</dl>
<dt>The <i>xref</i> block</p>
<dd>
<dl>
<dd>At every hyperlink (to within the set of converted documents) it is possible to have a cross reference inserted. The <i>xref</i> block is used to control this function.</p>
<dl>
<dt><code>text</code></p>
<dd>This defines the cross reference text to be inserted; the symbol $N will expand to the page number, default is &quot;[p $N]&quot;.</p>
<dt><code>passes</code></p>
<dd>The number of passes used to insert the cross references. Normally, only one pass is run. But since the insertion of the page numbers may effect the page breaks, it might for large documents with many links be necessary with more than one pass to get the cross references right. The default is 1.</dl>
</dl>
<dt>The <i>quote</i> block</p>
<dd>
<dl>
<dd>Language specific quotation marks are defined in this block. These quotation marks are used with the HTML 4.01 element Q for short quotations. Quotation marks are predefined for a few languages (English, Swedish, Danish, Norwegian (also Nynorsk and Bokm&aring;l), Finnish, Spanish, French, German and Italian). It is possible to define different quotation marks for quotes within quotes. </p>
<p> A quotation mark is defined as a string, using the same encoding as the converted document (normally ISO-8859-1), and/or with character entities. Note that quotation mark characters for several languages are not included in ISO-8859-1, and their corresponding character entities were not been defined prior to HTML 4.0. </p>
<p> Quotation marks for a language can be defined explicitly in a sub-block of the quote block. One can also identify the set of quotation marks with another previously defined language, using a key-value pair. The sub-block/key name should equal the language code as defined in ISO 639. The language sub-block can have the following key-values: </p>
<dl>
<dd>
<dl>
<dt><code>open</code></p>
<dd>The quote opening character(s).</p>
<dt><code>close</code></p>
<dd>The quote closing character(s). If undefined, it will equal open.</p>
<dt><code>open2</code></p>
<dd>The quote opening character(s) for quotes within quotes. If undefined, it will equal open.</p>
<dt><code>close2</code></p>
<dd>The quote closing character(s) for quotes within quotes. If undefined, it will equal close.</dl>
</dl>
<p> Example: English and Spanish use the same set of quotation marks &#8211; at least according to my book on typography. These (already known to html2ps) are defined with:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>quote {</dl>
<dl>
<dd>en {</dl>
<dl>
<dd>open: &quot;&amp;ldquo;&quot;; </p>
<p> close: &quot;&amp;rdquo;&quot;; </p>
<p> open2: &quot;`&quot;; </p>
<p> close2: &quot;&#8217;&quot;;</dl>
<dl>
<dd>} </p>
<p> es: en;</dl>
<dl>
<dd>}</dl>
</dl>
<dt>The <i>toc</i> block</p>
<dd>
<dl>
<dd>When a table of contents (ToC) is generated from document headings and titles, the appearance is controlled by this block.</p>
<dl>
<dt><code>heading</code></p>
<dd>A string with HTML code specifying a heading used on the first ToC page.</p>
<dt><code>level</code></p>
<dd>The maximum heading level used for building the ToC. The default is 6, which means that all headings will generate ToC entries.</p>
<dt><code>indent</code></p>
<dd>The ToC entries are indented proportional to the corresponding heading level. This value specifies the size of the indentation. The default is 1em.</dl>
</dl>
<dt>The <i>titlepage</i> block</p>
<dd>
<dl>
<dd>When a title page is generated, its appearance is controlled by this block.</p>
<dl>
<dt><code>content</code></p>
<dd>A string with HTML code specifying a heading used on the title page, The default is &quot;&lt;DIV align=center&gt; &lt;H1&gt;&lt;BIG&gt;$T&lt;/BIG&gt;&lt;/H1&gt; &lt;H2&gt;$[author]&lt;/H2&gt;&lt;/DIV&gt;&quot;.</p>
<dt><code>margin-top</code></p>
<dd>The size of the top margin on the title page, The default is 4cm.</dl>
</dl>
<dt>The <i>font</i> block</p>
<dd>
<dl>
<dd>Currently, html2ps recognizes the fonts: Times, New-Century-Schoolbook, Helvetica, Helvetica-Narrow, Palatino, Avantgarde, Bookman, and Courier. To add a new font (family), choose a name (consisting of letters, digits, hyphens, and underscores) for the font. Then define a sub-block to the font block, with the same name as the chosen font name. This block can contain two key-value pairs: </p>
<dl>
<dd>
<dl>
<dt><code>names</code></p>
<dd>A string containing four PostScript font names, separated by whitespace, corresponding to the font styles normal, italic, bold, and bold-italic. If less than four names are given, the first is used for the missing names. Note that PostScript font names are case sensitive.</p>
<dt><code>files</code></p>
<dd>A string of four file names, separated by whitespace, for files containing font definitions for the four font styles as specified above.</dl>
</dl>
<p> Example: A font &#8216;myfont&#8217; has its four font styles defined in local files. To use this font in all tables in the converted documents, one can use something like:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>TABLE { font-family: myfont } </p>
<p> @html2ps {</dl>
<dl>
<dd>font {</dl>
<dl>
<dd>myfont {</dl>
<dl>
<dd>names: &quot;MyFont-Roman MyFont-Italic MyFont-Bold MyFont-BoldItalic&quot;; </p>
<p> files: &quot;/x/y/myfr.pfa /x/y/myfi.pfa /x/y/myfb.pfa /x/y/myfbi.pfa&quot;;</dl>
<dl>
<dd>}</dl>
<dl>
<dd>}</dl>
<dl>
<dd>}</dl>
</dl>
<dt>The <i>hyphenation</i> block</p>
<dd>
<dl>
<dd>Hyphenation pattern files for different languages are specified in sub-blocks within this block. The blocks names should equal the language code as defined in ISO 639. These language blocks can contain the following two key-values: </p>
<dl>
<dd>
<dl>
<dt><code>file</code></p>
<dd>A hyphenation pattern file in TeX format for this language.</p>
<dt><code>extfile</code></p>
<dd>A file containing a list of hyphenation exceptions for this language. The exception file should contain words, separated by whitespaces, with hyphens inserted where hyphenation is allowed, as in: &quot;in-fra-struc-ture white-space&quot;.</dl>
</dl>
<p> For example, for English (with language code &#8216;en&#8217;) one can have a block like:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>en {</dl>
<dl>
<dd>file: &quot;/opt/tex/lib/macros/hyphen.tex&quot;; </p>
<p> extfile: &quot;/opt/tdb/lib/html2ps/enhyphext&quot;;</dl>
<dl>
<dd>}</dl>
<p> The hyphenation block itself can furthermore have these key-values:</p>
<dl>
<dt><code>min</code></p>
<dd>A positive integer defining the minimum number of letters a word must contain to make it a candidate for hyphenation. The default is 8.</p>
<dt><code>start</code></p>
<dd>A positive integer defining the minimum number of letters that must precede the hyphen when a word is hyphenated. The default is 4.</p>
<dt><code>end</code></p>
<dd>A positive integer defining the minimum number of letters that must follow the hyphen when a word is hyphenated. The default is 3.</dl>
</dl>
<dt>The <i>header</i> block</p>
<dd>
<dl>
<dd>This block is used to specify page headers. It is possible to define left, center, and right headers. Different headers for odd and even pages can be specified. Some symbols can be used that will expand to document title, author, date etc. See below.</p>
<dl>
<dt><code>left</code></p>
<dd>A left aligned header. If the alternate flag in this block is set to 1, this will be the right header on even pages.</p>
<dt><code>center</code></p>
<dd>A centered header.</p>
<dt><code>right</code></p>
<dd>A right aligned header. If the alternate flag in this block is set to 1, this will be the left header on even pages.</p>
<dt><code>odd-left</code></p>
<dd>A left aligned header on odd pages.</p>
<dt><code>odd-center</code></p>
<dd>A centered header on odd pages.</p>
<dt><code>odd-right</code></p>
<dd>A right aligned header on odd pages.</p>
<dt><code>even-left</code></p>
<dd>A left aligned header on even pages.</p>
<dt><code>even-center</code></p>
<dd>A centered header on even pages.</p>
<dt><code>even-right</code></p>
<dd>A right aligned header on even pages.</p>
<dt><code>font-family</code></p>
<dd>The font used for the header, default is Helvetica.</p>
<dt><code>font-size</code></p>
<dd>The font size for the header, default is 8pt.</p>
<dt><code>font-style</code></p>
<dd>The default is &quot;normal&quot;.</p>
<dt><code>font-weight</code></p>
<dd>The default is &quot;normal&quot;.</p>
<dt><code>color</code></p>
<dd>The header color, default is black.</p>
<dt><code>alternate</code></p>
<dd>A flag indicating whether the headers given by the left and right keys should change place on even pages. Typically used for double sided printing. The default is 1.</dl>
</dl>
<dt>The <i>footer</i> block</p>
<dd>
<dl>
<dd>This block is used to specify page footers. It is possible to define left, center, and right footers. Different footers for odd and even pages can be specified. Some symbols can be used that will expand to document title, author, date etc. See below.</p>
<dl>
<dt><code>left</code></p>
<dd>A left aligned footer. If the alternate flag in this block is set to 1, this will be the right footer on even pages.</p>
<dt><code>center</code></p>
<dd>A centered footer.</p>
<dt><code>right</code></p>
<dd>A right aligned footer. If the alternate flag in this block is set to 1, this will be the left footer on even pages.</p>
<dt><code>odd-left</code></p>
<dd>A left aligned footer on odd pages.</p>
<dt><code>odd-center</code></p>
<dd>A centered footer on odd pages.</p>
<dt><code>odd-right</code></p>
<dd>A right aligned footer on odd pages.</p>
<dt><code>even-left</code></p>
<dd>A left aligned footer on even pages.</p>
<dt><code>even-center</code></p>
<dd>A centered footer on even pages.</p>
<dt><code>even-right</code></p>
<dd>A right aligned footer on even pages.</p>
<dt><code>font-family</code></p>
<dd>The font used for the footer, default is Helvetica.</p>
<dt><code>font-size</code></p>
<dd>The font size for the footer, default is 8pt.</p>
<dt><code>font-style</code></p>
<dd>The default is &quot;normal&quot;.</p>
<dt><code>font-weight</code></p>
<dd>The default is &quot;normal&quot;.</p>
<dt><code>color</code></p>
<dd>The footer color, default is black.</p>
<dt><code>alternate</code></p>
<dd>A flag indicating whether the footers given by the left and right keys should change place on even pages. Typically used for double sided printing. The default is 1.</dl>
</dl>
<dt>The <i>frame</i> block</p>
<dd>
<dl>
<dd>The appearance of the optional frame (drawn on each page) is controlled by this block.</p>
<dl>
<dt><code>width</code></p>
<dd>The width of the frame, default is 0.6pt.</p>
<dt><code>margin</code></p>
<dd>The size of the frame margin, default is 0.5cm.</p>
<dt><code>color</code></p>
<dd>The colour of the frame, default is black.</dl>
</dl>
<dt>The <i>justify</i> block</p>
<dd>
<dl>
<dd>This block specifies the maximum amount of extra space inserted between words and letters when text justification is in effect.</p>
<dl>
<dt><code>word</code></p>
<dd>Maximum amount of extra space inserted between words. The default is 15pt.</p>
<dt><code>letter</code></p>
<dd>Maximum amount of extra space inserted between letters within words. The default is 0pt.</dl>
</dl>
<dt>The <i>draft</i> block</p>
<dd>
<dl>
<dd>It is possible to have some text written in a large font diagonally across each page. Typically this is a word, written in a very light colour, indicating that the document is a draft.</p>
<dl>
<dt><code>text</code></p>
<dd>The text to be printed, default is &quot;DRAFT&quot;.</p>
<dt><code>print</code></p>
<dd>A flag specifying whether the draft text should be printed or not. If unspecified, the draft text is printed when the document head contains &lt;META name=&quot;Status&quot; content=&quot;Draft&quot;&gt;.</p>
<dt><code>dir</code></p>
<dd>Specifies print direction, 0=downwards, 1=upwards.</p>
<dt><code>font-family</code></p>
<dd>The default is Helvetica.</p>
<dt><code>font-style</code></p>
<dd>The default is &quot;normal&quot;.</p>
<dt><code>font-weight</code></p>
<dd>The default is &quot;bold&quot;.</p>
<dt><code>color</code></p>
<dd>The default is &quot;F0F0F0&quot;.</dl>
</dl>
<dt>The <i>colour</i> block</p>
<dd>
<dl>
<dd>The 16 standard colour names from HTML 4.01 (although their use in HTML elements are now deprecated) are recognized by html2ps. Use this block to extend this list of colours. This is done with key-value pairs, where the key is the colour name, and the value is the colour given as a hexadecimal RGB value, for example: &quot;brown: A52A2A;&quot;.</dl>
<p> <code>Key-value pairs in the @html2ps block</code></p>
<dt><code>html2psrc</code></p>
<dd>The name of the default personal configuration file. The default is $HOME/.html2psrc.</p>
<dt><code>imgalt</code></p>
<dd>Specifies which text should be written as a replacement for in-line images when the IMG element has no ALT attribute. The default is &quot;[IMAGE]&quot;.</p>
<dt><code>datefmt</code></p>
<dd>The symbol $D can be used in page headers and footers to insert the current date/time; the value of the datefmt key specifies the format used. The syntax is the same as in the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) routine. The default is &quot;%e %b %Y %R&quot;, which gives a date string like &quot; 7 May 2010 13:22&quot;.</p>
<dt><code>locale</code></p>
<dd>The locale (language code) used for formating language dependent parts of the date/time in datefmt. If unspecified, the value is taken from environment variables, see <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3). No default.</p>
<dt><code>doc-sep</code></p>
<dd>A string of HTML code that will be inserted between the documents when more than one are converted. The default is &quot;&lt;!&#8211;NewPage&#8211;&gt;&quot;, which will cause a page break. You may use (almost) any HTML code, for example &quot;&lt;HR&gt;&lt;HR&gt;&quot; or &quot;&lt;IMG src=&#8230;&gt;&quot;.</p>
<dt><code>ball-radius</code></p>
<dd>The radius, given as a relative size, of the balls used in unordered lists. The default is 0.25em.</p>
<dt><code>numbstyle</code></p>
<dd>Page numbering style, 0=arabic, 1=roman. The default is 0.</p>
<dt><code>showurl</code></p>
<dd>When this flag is set to 1, the URL for external links are shown within parentheses after the link. The default is 0.</p>
<dt><code>seq-number</code></p>
<dd>When this flag is set, the headings in the document will be sequentially numbered: H1 headings will be numbered 1, 2,&#8230;, H2 headings 1.1, 1.2, etc. The starting number for H1 can be changed using the -M (&#8211;mainchapter) option. The default is 0.</p>
<dt><code>extrapage</code></p>
<dd>A flag specifying whether an extra (empty) page should be printed, when necessary, to ensure that the title page, the table of contents, and the document itself will start on odd pages. This is typically desirable for double sided printing. The default is 1.</p>
<dt><code>break-table</code></p>
<dd>A flag specifying if a table should be broken across two pages when it does not fit on the current page, but it does on a page of its own. The default is 0 (avoid breaking tables when possible).</p>
<dt><code>forms</code></p>
<dd>This flag is used to specify whether FORM elements in the document should be processed or ignored. Some forms may be suitable for printing out and be filled out (with a pen), others are not. The default is 1.</p>
<dt><code>textarea-data</code></p>
<dd>When a TEXTAREA element contains prefilled data, the text will be used as labels if this flag is set, otherwise ignored. The default is 0.</p>
<dt><code>page-break</code></p>
<dd>Set this flag to 0 to suppress the normal behavior of generating page breaks from the comment &lt;!&#8211;NewPage&#8211;&gt; etc, as specified below. The default is 1.</p>
<dt><code>expand-acronyms</code></p>
<dd>A flag specifying whether acronyms, given by the ACRONYM element, should be expanded or not. The default is 0.</p>
<dt><code>spoof</code></p>
<dd>Some web servers return different documents depending on which user agent is used to retrieve the document. You can fool the web server that a certain browser is used, by setting this value to the identification used by the browser, such as &quot;Mozilla/4.0&quot;. This only works if you are using one of the Perl packages to retrieve remote documents.</p>
<dt><code>ssi</code></p>
<dd>When this flag is set, some Server Side Includes will be processed when the document is read from a local file. Examples are &lt;!&#8211;#include file=&#8230;&gt;, &lt;!&#8211;#echo var=&quot;LAST_MODIFIED&quot;&gt;, &lt;!&#8211;#config timefmt=&#8230;&gt;. The default is 0.</p>
<dt><code>prefilled</code></p>
<dd>This flag controls whether the content of form elements should be rendered or not. That is, when this flag is set, the content of TEXTAREA elements, and the value of the value attribute of text INPUT elements will be shown. Also, checked radio buttons and checkboxes will be marked. The default is 0.</dl>
<h2>Symbols</h2>
<p>The following symbols can be used on the title page, the page headers/footers, and in the heading for the table of contents: </p>
<p> Symbols of the form &quot;$[<i>name</i>]&quot; will expand to the value of the content attribute of META elements, having either of the attributes &quot;name=<i>name</i>&quot; or &quot;http-equiv=<i>name</i>&quot; (case insensitive string matching). For example, when a document containing:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>&lt;META name=&quot;expires&quot; content=&quot;31 Dec 2011&quot;&gt;</dl>
<p> is converted, using a configuration file with:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>footer { left: &quot;Expires: $[expires]&quot; }</dl>
<p> this left footer will be inserted:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>Expires: 31 Dec 2011</dl>
<p> In addition, these symbols are defined: </p>
<dl>
<dd>
<dl>
<dt><code>$T</code></p>
<dd>Current document title.</p>
<dt><code>$A</code></p>
<dd>Author of current document, as specified with &lt;META name=&quot;Author&quot; content=&quot;&#8230;&quot;&gt; in the document head.</p>
<dt><code>$U</code></p>
<dd>The URL, or file name, of current document.</p>
<dt><code>$N</code></p>
<dd>Page number.</p>
<dt><code>$H</code></p>
<dd>Current document heading (level 1-3).</p>
<dt><code>$D</code></p>
<dd>Current date/time. The format is given by the datefmt key.</dl>
</dl>
<p> So $A is equivalent to $[author], but kept for backwards compatibility. </p>
<p> To avoid symbol expansion, precede the dollar sign with a backslash, as in &quot;\$T&quot;.</p>
<h2>Hints</h2>
<p>I imagine that a typical use of configuration files can be something along the following lines. </p>
<p> System specific definitions (e.g. specification of available program packages) and global defaults (paper type etc) are defined in the global configuration file. </p>
<p> If there is more than one user of the program on the system, each user can also have a personal configuration file with his/hers own personal preferences. (On a single user system one can use the global configuration file for this purpose as well.) </p>
<p> One may also develop a collection of configuration files for typical situations. These files are placed in a directory that is searched by html2ps (the search path is defined with the environment variable HTML2PSPATH). For example, to print a document as slides &#8211; in landscape mode, with large text in Helvetica, and a thick frame &#8211; one can create a configuration file, called &#8216;slides&#8217; say, containing:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>@html2ps {</dl>
<dl>
<dd>option {</dl>
<dl>
<dd>landscape: 1; </p>
<p> frame: 1;</dl>
<dl>
<dd>} </p>
<p> frame { width: 3pt }</dl>
<dl>
<dd>} </p>
<p> BODY {</dl>
<dl>
<dd>font-family: Helvetica; </p>
<p> font-size: 20pt;</dl>
<dl>
<dd>} </p>
<p> H1 { font-size: 35pt } </p>
<p> H2 { font-size: 32pt } </p>
<p> H3 { font-size: 29pt } </p>
<p> H4 { font-size: 26pt } </p>
<p> H5 { font-size: 23pt } </p>
<p> H6 { font-size: 20pt } </p>
<p> PRE { font-size: 18pt }</dl>
<p> Then use the command:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>html2ps -f slides &#8230;</dl>
<p> to convert the document. Note that with this command the file &#8216;slides&#8217; is used instead of the personal configuration file. If you want both to be used, giving precedence to definitions made in the file &#8216;slides&#8217;, use the command:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>html2ps -f :slides &#8230;</dl>
<p> (The page breaks between the slides can for example be generated by adding &#8216;&lt;HR class=PAGE-BREAK&gt;&#8217; to the HTML document.) </p>
<p> For features that are frequently turned on and off, and that cannot be controlled by command line options, it may be a good idea to create small configuration files as &quot;building blocks&quot;. For example a file &#8216;A4&#8217; for printing on A4 paper (if you have some other default paper type):</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>@html2ps { paper { type: A4 } }</dl>
<p> and a file &#8216;hnum&#8217; for automatic numbering of headings:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>@html2ps { seq-number: 1 }</dl>
<p> Combining this with the previous example: to convert a document for printing on A4 sized slides with all headings numbered, use the command:</p>
<dl>
<dd></dl>
<dl>
<dd></dl>
<dl>
<dd>html2ps -f :slides:A4:hnum &#8230;</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-html2ps/">html2ps</a>(1), <a href="/docs/linux/man/3-setlocale/">setlocale</a>(3), <a href="/docs/linux/man/3-strftime/">strftime</a>(3)</p>
<h2>Version</h2>
<p>This manpage describes html2ps version 1.0 beta7.</p>
<h2>Availability</h2>
<p><a rel="nofollow" href="http://user.it.uu.se/~jan/html2ps.html">http://user.it.uu.se/~jan/html2ps.html</a></p>
<h2>Author</h2>
<p>Jan Karrman (jan [at] it.uu.se)</p>
