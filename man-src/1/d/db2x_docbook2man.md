---
title: "db2x_docbook2man(1)"
name: "db2x_docbook2man"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db2x_docbook2man/"
description: "docbook2man – Convert DocBook to man pages"
---

<h2>NAME</h2>
<p> docbook2man &#8211; Convert DocBook to man pages</p>
<h2>SYNOPSIS</h2>
<p> <code>docbook2man</code> [<i>options</i>] <i>xml-document</i></p>
<h2>DESCRIPTION</h2>
<p> <code>docbook2man</code> converts the given DocBook XML document into man pages. By default, the man pages will be output to the current directory. </p>
<p> Only the refentry content in the DocBook document is converted. (To convert content outside of a refentry, stylesheet customization is required. See the docbook2X package for details.) </p>
<p> The <code>docbook2man</code> command is a wrapper script for a two-step conversion process. See the section &#8220;CONVERSION PROCESS&#8221; below for details.</p>
<h2>OPTIONS</h2>
<p> The available options are essentially the union of the options from <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1) and <code><a href="/docs/linux/man/1-db2x_manxml/">db2x_manxml</a></code>(1). </p>
<p> Some commonly-used options are listed below:</p>
<dl>
<dt><code>&#8211;encoding=</code><i>encoding</i></p>
<dd> Sets the character encoding of the output.</p>
<dt><code>&#8211;string-param </code><i>parameter</i><code>=</code><i>value</i></p>
<dd> Sets a stylesheet parameter (options that affect how the output looks). See &#8220;Stylesheet parameters&#8221; below for the parameters that can be set.</p>
<dt><code>&#8211;sgml</code></p>
<dd> Accept an SGML source document as input instead of XML.</p>
<dt><code>&#8211;solinks</code></p>
<dd> Make stub pages for alternate names for an output man page.</dl>
<h3>STYLESHEET PARAMETERS</h3>
<dl>
<dt>uppercase-headings</p>
<dd> <code>Brief</code>. Make headings uppercase? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> Headings in man page content should be or should not be uppercased.</p>
<dt>manvolnum-cite-numeral-only</p>
<dd> <code>Brief</code>. Man page section citation should use only the number </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> When citing other man pages, the man-page section is either given as is, or has the letters stripped from it, citing only the number of the section (e.g. section 3x becomes 3). This option specifies which style.</p>
<dt>quotes-on-literals</p>
<dd> <code>Brief</code>. Display quotes on literal elements? </p>
<p> <code>Default setting</code>. 0 (boolean false) </p>
<p> If true, render literal elements with quotes around them.</p>
<dt>show-comments</p>
<dd> <code>Brief</code>. Display comment elements? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, comments will be displayed, otherwise they are suppressed. Comments here refers to the comment element, which will be renamed remark in DocBook V4.0, not XML comments (&lt;&#8211; like this &#8211;&gt;) which are unavailable.</p>
<dt>function-parens</p>
<dd> <code>Brief</code>. Generate parentheses after a function? </p>
<p> <code>Default setting</code>. 0 (boolean false) </p>
<p> If true, the formatting of a &lt;function&gt; element will include generated parenthesis.</p>
<dt>xref-on-link</p>
<dd> <code>Brief</code>. Should link generate a cross-reference? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> Man pages cannot render the hypertext links created by link. If this option is set, then the stylesheet renders a cross reference to the target of the link. (This may reduce clutter). Otherwise, only the content of the link is rendered and the actual link itself is ignored.</p>
<dt>header-3</p>
<dd> <code>Brief</code>. Third header text </p>
<p> <code>Default setting</code>. (blank) </p>
<p> Specifies the text of the third header of a man page, typically the date for the man page. If empty, the date content for the refentry is used.</p>
<dt>header-4</p>
<dd> <code>Brief</code>. Fourth header text </p>
<p> <code>Default setting</code>. (blank) </p>
<p> Specifies the text of the fourth header of a man page. If empty, the refmiscinfo content for the refentry is used.</p>
<dt>header-5</p>
<dd> <code>Brief</code>. Fifth header text </p>
<p> <code>Default setting</code>. (blank) </p>
<p> Specifies the text of the fifth header of a man page. If empty, the &#8216;manual name&#8217;, that is, the title of the book or reference container is used.</p>
<dt>default-manpage-section</p>
<dd> <code>Brief</code>. Default man page section </p>
<p> <code>Default setting</code>. 1 </p>
<p> The source document usually indicates the sections that each man page should belong to (with manvolnum in refmeta). In case the source document does not indicate man-page sections, this option specifies the default.</p>
<dt>custom-localization-file</p>
<dd> <code>Brief</code>. URI of XML document containing custom localization data </p>
<p> <code>Default setting</code>. (blank) </p>
<p> This parameter specifies the URI of a XML document that describes text translations (and other locale-specific information) that is needed by the stylesheet to process the DocBook document. </p>
<p> The text translations pointed to by this parameter always override the default text translations (from the internal parameter localization-file). If a particular translation is not present here, the corresponding default translation is used as a fallback. </p>
<p> This parameter is primarily for changing certain punctuation characters used in formatting the source document. The settings for punctuation characters are often specific to the source document, but can also be dependent on the locale. </p>
<p> To not use custom text translations, leave this parameter as the empty string.</p>
<dt>custom-l10n-data</p>
<dd> <code>Brief</code>. XML document containing custom localization data </p>
<p> <code>Default setting</code>. document($custom-localization-file) </p>
<p> This parameter specifies the XML document that describes text translations (and other locale-specific information) that is needed by the stylesheet to process the DocBook document. </p>
<p> This parameter is internal to the stylesheet. To point to an external XML document with a URI or a file name, you should use the custom-localization-file parameter instead. </p>
<p> However, inside a custom stylesheet (<i>not on the command-line</i>) this paramter can be set to the XPath expression document(&#8221;), which will cause the custom translations directly embedded inside the custom stylesheet to be read.</p>
<dt>author-othername-in-middle</p>
<dd> <code>Brief</code>. Is othername in author a middle name? </p>
<p> <code>Default setting</code>. 1 </p>
<p> If true, the othername of an author appears between the firstname and surname. Otherwise, othername is suppressed.</dl>
<h2>EXAMPLES</h2>
<pre><code>
$ docbook2man-- solinks manpages.xml
    $ docbook2man-- solinks-- encoding = utf - 8 // TRANSLIT manpages.xml
                                         $ docbook2man-- string -
                                         param header - 4 = "Free Recode 3.6" document.xml
                                                                .fi
</code></pre>
<h2>CONVERSION PROCESS</h2>
<h3>Converting to man pages</h3>
<p> DocBook documents are converted to man pages in two steps:</p>
<dl>
<dt>1.</p>
<dd> The DocBook source is converted by a XSLT stylesheet into an intermediate XML format, Man-XML. </p>
<p> Man-XML is simpler than DocBook and closer to the man page format; it is intended to make the stylesheets&#8217; job easier. </p>
<p> The stylesheet for this purpose is in <i>xslt/man/docbook.xsl</i>. For portability, it should always be referred to by the following URI: </p>
<pre>
<a rel="nofollow" href="http://docbook2x.sourceforge.net/latest/xslt/man/docbook.xsl">http://docbook2x.sourceforge.net/latest/xslt/man/docbook.xsl</a>
</pre>
<p> Run this stylesheet with <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1). </p>
<p> <code>Customizing</code>. You can also customize the output by creating your own XSLT stylesheet &#8212; changing parameters or adding new templates &#8212; and importing <i>xslt/man/docbook.xsl</i>.</p>
<dt>2.</p>
<dd> Man-XML is converted to the actual man pages by <code><a href="/docs/linux/man/1-db2x_manxml/">db2x_manxml</a></code>(1).</dl>
<p> The <code>docbook2man</code> command does both steps automatically, but if any problems occur, you can see the errors more clearly if you do each step separately: </p>
<pre>
<code>$ </code>db2x_xsltproc -s man <i>mydoc</i>.xml -o <i>mydoc</i>.mxml
<code>$ </code>db2x_manxml <i>mydoc</i>.mxml
.fi
Options to the conversion stylesheet are described in
the man-pages stylesheets
reference.
<code>Pure XSLT conversion</code>. 
An alternative to the <code>db2x_manxml</code> Perl script is the XSLT
stylesheet in 
<i>xslt/backend/db2x_manxml.xsl</i>.
This stylesheet performs a similar function
of converting Man-XML to actual man pages.
It is useful if you desire a pure XSLT
solution to man-page conversion.
Of course, the quality of the conversion using this stylesheet
will never be as good as the Perl <code>db2x_manxml</code>,
and it runs slower. 
In particular, the pure XSLT version
currently does not support tables in man pages,
but its Perl counterpart does.
</pre>
<h3>Character set conversion</h3>
<p> When translating XML to legacy ASCII-based formats with poor support for Unicode, such as man pages and Texinfo, there is always the problem that Unicode characters in the source document also have to be translated somehow. </p>
<p> A straightforward character set conversion from Unicode does not suffice, because the target character set, usually US-ASCII or ISO Latin-1, do not contain common characters such as dashes and directional quotation marks that are widely used in XML documents. But document formatters (man and Texinfo) allow such characters to be entered by a markup escape: for example, \(lq for the left directional quote &#8220;. And if a markup-level escape is not available, an ASCII transliteration might be used: for example, using the ASCII less-than sign &lt; for the angle quotation mark &lt;. </p>
<p> So the Unicode character problem can be solved in two steps:</p>
<dl>
<dt>1.</p>
<dd> <code><a href="/docs/linux/man/1-utf8trans/">utf8trans</a></code>(1), a program included in docbook2X, maps Unicode characters to markup-level escapes or transliterations. </p>
<p> Since there is not necessarily a fixed, official mapping of Unicode characters, <code>utf8trans</code> can read in user-modifiable character mappings expressed in text files and apply them. (Unlike most character set converters.) </p>
<p> In <i>charmaps/man/roff.charmap</i> and <i>charmaps/man/texi.charmap</i> are character maps that may be used for man-page and Texinfo conversion. The programs <code><a href="/docs/linux/man/1-db2x_manxml/">db2x_manxml</a></code>(1) and <code><a href="/docs/linux/man/1-db2x_texixml/">db2x_texixml</a></code>(1) will apply these character maps, or another character map specified by the user, automatically.</p>
<dt>2.</p>
<dd> The rest of the Unicode text is converted to some other character set (encoding). For example, a French document with accented characters (such as &eacute;) might be converted to ISO Latin 1. </p>
<p> This step is applied after <code>utf8trans</code> character mapping, using the <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) encoding conversion tool. Both <code><a href="/docs/linux/man/1-db2x_manxml/">db2x_manxml</a></code>(1) and <code><a href="/docs/linux/man/1-db2x_texixml/">db2x_texixml</a></code>(1) can call <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) automatically when producing their output.</dl>
<h2>FILES</h2>
<p> <i>/usr/local/share/docbook2X/xslt/man/docbook.xsl</i><br />
 <i>/usr/local/share/docbook2X/xslt/backend/db2x_manxml.xsl</i><br />
 <i>/usr/local/share/docbook2X/xslt/catalog.xml</i><br />
 <i>/usr/local/share/docbook2X/charmaps/roff.charmap</i><br />
 <i>/usr/local/share/docbook2X/charmaps/roff.charmap.xml</i> </p>
<p> The above files are distributed and installed by the docbook2X package.</p>
<h2>NOTES</h2>
<p> The <code>docbook2man</code> or the <code>docbook2texi</code> command described in this manual page come from the docbook2X package. It should not be confused with the command of the same name from the obsoleted docbook-utils package.</p>
<h2>LIMITATIONS</h2>
<dl>
<dt>&bull;</p>
<dd> Internally there is one long pipeline of programs which your document goes through. If any segment of the pipeline fails (even trivially, like from mistyped program options), the resulting errors can be difficult to decipher &#8212; in this case, try running the components of docbook2X separately.</dl>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1), <code><a href="/docs/linux/man/1-db2x_manxml/">db2x_manxml</a></code>(1), <code><a href="/docs/linux/man/1-utf8trans/">utf8trans</a></code>(1) </p>
<p> The docbook2X manual (in Texinfo or HTML format) fully describes how to convert DocBook to man pages and Texinfo. </p>
<p> Up-to-date information about this program can be found at the docbook2X Web site &lt;<a rel="nofollow" href="http://docbook2x.sourceforge.net/">http://docbook2x.sourceforge.net/</a>&gt; . </p>
<h2>Index</h2>
