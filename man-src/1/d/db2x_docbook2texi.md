---
title: "db2x_docbook2texi(1)"
name: "db2x_docbook2texi"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db2x_docbook2texi/"
description: "docbook2texi – Convert DocBook to Texinfo"
---

<h2>NAME</h2>
<p> docbook2texi &#8211; Convert DocBook to Texinfo</p>
<h2>SYNOPSIS</h2>
<p> <code>docbook2texi</code> [<i>options</i>] <i>xml-document</i></p>
<h2>DESCRIPTION</h2>
<p> <code>docbook2texi</code> converts the given DocBook XML document into one or more Texinfo documents. By default, these Texinfo documents will be output to the current directory. </p>
<p> The <code>docbook2texi</code> command is a wrapper script for a two-step conversion process. See the section &#8220;CONVERSION PROCESS&#8221; below for details.</p>
<h2>OPTIONS</h2>
<p> The available options are essentially the union of the options for <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1) and <code><a href="/docs/linux/man/1-db2x_texixml/">db2x_texixml</a></code>(1). </p>
<p> Some commonly-used options are listed below:</p>
<dl>
<dt><code>&#8211;encoding=</code><i>encoding</i></p>
<dd> Sets the character encoding of the output.</p>
<dt><code>&#8211;string-param </code><i>parameter</i><code>=</code><i>value</i></p>
<dd> Sets a stylesheet parameter (options that affect how the output looks). See &#8220;Stylesheet parameters&#8221; below for the parameters that can be set.</p>
<dt><code>&#8211;sgml</code></p>
<dd> Accept an SGML source document as input instead of XML.</dl>
<h3>STYLESHEET PARAMETERS</h3>
<dl>
<dt>captions-display-as-headings</p>
<dd> <code>Brief</code>. Use heading markup for minor captions? </p>
<p> <code>Default setting</code>. 0 (boolean false) </p>
<p> If true, title content in some (formal) objects are rendered with the Texinfo @<i>heading</i> commands. </p>
<p> If false, captions are rendered as an emphasized paragraph.</p>
<dt>links-use-pxref</p>
<dd> <code>Brief</code>. Translate link using @pxref </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, link is translated with the hypertext followed by the cross reference in parentheses. </p>
<p> Otherwise, the hypertext content serves as the cross-reference name marked up using @ref. Typically info displays this contruct badly.</p>
<dt>explicit-node-names</p>
<dd> <code>Brief</code>. Insist on manually constructed Texinfo node names </p>
<p> <code>Default setting</code>. 0 (boolean false) </p>
<p> Elements in the source document can influence the Texinfo node name generation specifying either a xreflabel, or for the sectioning elements, a title with role=&#8217;texinfo-node&#8217; in the <i>*</i>info container. </p>
<p> However, for the majority of source documents, explicit Texinfo node names are not available, and the stylesheet tries to generate a reasonable one instead, e.g. from the normal title of an element. The generated name may not be optimal. If this option is set and the stylesheet needs to generate a name, a warning is emitted and <code>generate-id</code> is always used for the name. </p>
<p> When the hashtable extension is not available, the stylesheet cannot check for node name collisions, and in this case, setting this option and using explicit node names are recommended. </p>
<p> This option is not set (i.e. false) by default.</p>
<dl>
<dt>
<dd> <code>Note</code> </p>
<p> The absolute fallback for generating node names is using the XSLT function <code>generate-id</code>, and the stylesheet always emits a warning in this case regardless of the setting of explicit-node-names.</dl>
<dt>show-comments</p>
<dd> <code>Brief</code>. Display comment elements? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, comments will be displayed, otherwise they are suppressed. Comments here refers to the comment element, which will be renamed remark in DocBook V4.0, not XML comments (&lt;&#8211; like this &#8211;&gt;) which are unavailable.</p>
<dt>funcsynopsis-decoration</p>
<dd> <code>Brief</code>. Decorate elements of a FuncSynopsis? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, elements of the FuncSynopsis will be decorated (e.g. bold or italic). The decoration is controlled by functions that can be redefined in a customization layer.</p>
<dt>function-parens</p>
<dd> <code>Brief</code>. Generate parentheses after a function? </p>
<p> <code>Default setting</code>. 0 (boolean false) </p>
<p> If true, the formatting of a &lt;function&gt; element will include generated parenthesis.</p>
<dt>refentry-display-name</p>
<dd> <code>Brief</code>. Output NAME header before &#8216;RefName'(s)? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, a &quot;NAME&quot; section title is output before the list of &#8216;RefName&#8217;s.</p>
<dt>manvolnum-in-xref</p>
<dd> <code>Brief</code>. Output manvolnum as part of refentry cross-reference? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> if true, the manvolnum is used when cross-referencing refentrys, either with xref or citerefentry.</p>
<dt>prefer-textobjects</p>
<dd> <code>Brief</code>. Prefer textobject over imageobject? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, the textobject in a mediaobject is preferred over any imageobject. </p>
<p> (Of course, for output formats other than Texinfo, you usually want to prefer the imageobject, but Info is a text-only format.) </p>
<p> In addition to the values true and false, this parameter may be set to 2 to indicate that both the text and the images should be output. You may want to do this because some Texinfo viewers can read images. Note that the Texinfo @image command has its own mechanism for switching between text and image output &#8212; but we do not use this here. </p>
<p> The default is true.</p>
<dt>semantic-decorations</p>
<dd> <code>Brief</code>. Use Texinfo semantic inline markup? </p>
<p> <code>Default setting</code>. 1 (boolean true) </p>
<p> If true, the semantic inline markup of DocBook is translated into (the closest) Texinfo equivalent. This is the default. </p>
<p> However, because the Info format is limited to plain text, the semantic inline markup is often distinguished by using explicit quotes, which may not look good. You can set this option to false to suppress these. (For finer control over the inline formatting, you can use your own stylesheet.)</p>
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
<p> If true, the othername of an author appears between the firstname and surname. Otherwise, othername is suppressed.</p>
<dt>output-file</p>
<dd> <code>Brief</code>. Name of the Info file </p>
<p> <code>Default setting</code>. (blank) </p>
<p> This parameter specifies the name of the final Info file, overriding the setting in the document itself and the automatic selection in the stylesheet. If the document is a set, this parameter has no effect.</p>
<dl>
<dt>
<dd> <code>Important</code> </p>
<p> Do <i>not</i> include the .info extension in the name.</dl>
<p> (Note that this parameter has nothing to do with the name of the <i>Texi-XML output</i> by the XSLT processor you are running this stylesheet from.)</p>
<dt>directory-category</p>
<dd> <code>Brief</code>. The categorization of the document in the Info directory </p>
<p> <code>Default setting</code>. (blank) </p>
<p> This is set to the category that the document should go under in the Info directory of installed Info files. For example, General Commands.</p>
<dl>
<dt>
<dd> <code>Note</code> </p>
<p> Categories may also be set directly in the source document. But if this parameter is not empty, then it always overrides the setting in the source document.</dl>
<dt>directory-description</p>
<dd> <code>Brief</code>. The description of the document in the Info directory </p>
<p> <code>Default setting</code>. (blank) </p>
<p> This is a short description of the document that appears in the Info directory of installed Info files. For example, An Interactive Plotting Program.</p>
<dl>
<dt>
<dd> <code>Note</code> </p>
<p> Menu descriptions may also be set directly in the source document. But if this parameter is not empty, then it always overrides the setting in the source document.</dl>
<dt>index-category</p>
<dd> <code>Brief</code>. The Texinfo index to use </p>
<p> <code>Default setting</code>. cp </p>
<p> The Texinfo index for indexterm and index is specified using the role attribute. If the above elements do not have a role, then the default specified by this parameter is used. </p>
<p> The predefined indices are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>c, cp</p>
<dd> Concept index</p>
<dt>f, fn</p>
<dd> Function index</p>
<dt>v, vr</p>
<dd> Variable index</p>
<dt>k, ky</p>
<dd> Keystroke index</p>
<dt>p, pg</p>
<dd> Program index</p>
<dt>d, tp</p>
<dd> Data type index</dl>
</dl>
<p> User-defined indices are not yet supported.</p>
<dt>qanda-defaultlabel</p>
<dd> <code>Brief</code>. Sets the default for defaultlabel on QandASet. </p>
<p> <code>Default setting</code>. </p>
<p> If no defaultlabel attribute is specified on a QandASet, this value is used. It must be one of the legal values for the defaultlabel attribute.</p>
<dt>qandaset-generate-toc</p>
<dd> <code>Brief</code>. Is a Table of Contents created for QandASets? </p>
<p> <code>Default setting</code>. </p>
<p> If true, a ToC is constructed for QandASets.</dl>
<h2>EXAMPLES</h2>
<pre>
<code>$ </code>docbook2texi tdg.xml
<code>$ </code>docbook2texi --encoding=utf-8//TRANSLIT tdg.xml
<code>$ </code>docbook2texi --string-param semantic-decorations=0 tdg.xml
.fi
</pre>
<h2>CONVERSION PROCESS</h2>
<h3>Converting to Texinfo</h3>
<p> DocBook documents are converted to Texinfo in two steps:</p>
<dl>
<dt>1.</p>
<dd> The DocBook source is converted by a XSLT stylesheet into an intermediate XML format, Texi-XML. </p>
<p> Texi-XML is simpler than DocBook and closer to the Texinfo format; it is intended to make the stylesheets&#8217; job easier. </p>
<p> The stylesheet for this purpose is in <i>xslt/texi/docbook.xsl</i>. For portability, it should always be referred to by the following URI: </p>
<pre>
<a rel="nofollow" href="http://docbook2x.sourceforge.net/latest/xslt/texi/docbook.xsl">http://docbook2x.sourceforge.net/latest/xslt/texi/docbook.xsl</a>
</pre>
<p> Run this stylesheet with <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1). </p>
<p> <code>Customizing</code>. You can also customize the output by creating your own XSLT stylesheet &#8212; changing parameters or adding new templates &#8212; and importing <i>xslt/texi/docbook.xsl</i>.</p>
<dt>2.</p>
<dd> Texi-XML is converted to the actual Texinfo files by <code><a href="/docs/linux/man/1-db2x_texixml/">db2x_texixml</a></code>(1).</dl>
<p> The <code>docbook2texi</code> command does both steps automatically, but if any problems occur, you can see the errors more clearly if you do each step separately: </p>
<pre>
<code>$ </code>db2x_xsltproc -s texi <i>mydoc</i>.xml -o <i>mydoc</i>.txml
<code>$ </code>db2x_texixml <i>mydoc</i>.txml
.fi
Options to the conversion stylesheet are described
in the Texinfo stylesheets
reference.
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
<p> <i>/usr/local/share/docbook2X/xslt/texi/docbook.xsl</i><br />
 <i>/usr/local/share/docbook2X/xslt/backend/db2x_texixml.xsl</i><br />
 <i>/usr/local/share/docbook2X/xslt/catalog.xml</i><br />
 <i>/usr/local/share/docbook2X/charmaps/texi.charmap.xml</i><br />
 <i>/usr/local/share/docbook2X/charmaps/texi.charmap.xml</i> </p>
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
<p> <code><a href="/docs/linux/man/1-db2x_xsltproc/">db2x_xsltproc</a></code>(1), <code><a href="/docs/linux/man/1-db2x_texixml/">db2x_texixml</a></code>(1), <code><a href="/docs/linux/man/1-utf8trans/">utf8trans</a></code>(1) </p>
<p> The docbook2X manual (in Texinfo or HTML format) fully describes how to convert DocBook to man pages and Texinfo. </p>
<p> Up-to-date information about this program can be found at the docbook2X Web site &lt;<a rel="nofollow" href="http://docbook2x.sourceforge.net/">http://docbook2x.sourceforge.net/</a>&gt; . </p>
<h2>Index</h2>
