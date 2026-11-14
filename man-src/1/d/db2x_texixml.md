---
title: "db2x_texixml(1)"
name: "db2x_texixml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db2x_texixml/"
description: "db2x_texixml – Make Texinfo files from Texi-XML"
---

<h2>NAME</h2>
<p> db2x_texixml &#8211; Make Texinfo files from Texi-XML</p>
<h2>SYNOPSIS</h2>
<p> <code>db2x_texixml</code> [options]&#8230; [<i>xml-document</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>db2x_texixml</code> converts a Texi-XML document into one or more Texinfo documents. </p>
<p> If <i>xml-document</i> is not given, then the document to convert comes from standard input. </p>
<p> The filenames of the Texinfo documents are determined by markup in the Texi-XML source. (If the filenames are not specified in the markup, then <code>db2x_texixml</code> attempts to deduce them from the name of the input file. However, the Texi-XML source should specify the filename, because it does not work when there are multiple output files or when the Texi-XML source comes from standard input.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;encoding=</code><i>encoding</i></p>
<dd> Select the character encoding used for the output files. The available encodings are those of <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1). The default encoding is us-ascii. </p>
<p> The XML source may contain characters that are not representable in the encoding that you select; in this case the program will bomb out during processing, and you should choose another encoding. (This is guaranteed not to happen with any Unicode encoding such as UTF-8, but unfortunately not everyone is able to process Unicode texts.) </p>
<p> If you are using GNU&#8217;s version of <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), you can affix //TRANSLIT to the end of the encoding name to attempt transliterations of any unconvertible characters in the output. Beware, however, that the really inconvertible characters will be turned into another of those damned question marks. (Aren&#8217;t you sick of this?) </p>
<p> The suffix //TRANSLIT applied to a Unicode encoding &#8212; in particular, utf-8//TRANSLIT &#8212; means that the output files are to remain in Unicode, but markup-level character translations using <code>utf8trans</code> are still to be done. So in most cases, an English-language document, converted using <code>&#8211;encoding=</code><code>utf-8//TRANSLIT</code> will actually end up as a US-ASCII document, but any untranslatable characters will remain as UTF-8 without any warning whatsoever. (Note: strictly speaking this is not &#8220;transliteration&#8221;.) This method of conversion is a compromise over strict <code>&#8211;encoding=</code><code>us-ascii</code> processing, which aborts if any untranslatable characters are encountered. </p>
<p> Note that man pages and Texinfo documents in non-ASCII encodings (including UTF-8) may not be portable to older (non-internationalized) systems, which is why the default value for this option is us-ascii. </p>
<p> To suppress any automatic character mapping or encoding conversion whatsoever, pass the option <code>&#8211;encoding=</code><code>utf-8</code>.</p>
<dt><code>&#8211;list-files</code></p>
<dd> Write a list of all the output files to standard output, in addition to normal processing.</p>
<dt><code>&#8211;output-dir=</code><i>dir</i></p>
<dd> Specify the directory where the output files are placed. The default is the current working directory. </p>
<p> This option is ignored if the output is to be written to standard output (triggered by the option <code>&#8211;to-stdout</code>).</p>
<dt><code>&#8211;to-stdout</code></p>
<dd> Write the output to standard output instead of to individual files. </p>
<p> If this option is used even when there are supposed to be multiple output documents, then everything is concatenated to standard output. But beware that most other programs will not accept this concatenated output. </p>
<p> This option is incompatible with <code>&#8211;list-files</code>, obviously.</p>
<dt><code>&#8211;info</code></p>
<dd> Pipe the Texinfo output to <code><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></code>(1), creating Info files directly instead of Texinfo files.</p>
<dt><code>&#8211;plaintext</code></p>
<dd> Pipe the Texinfo output to <code>makeinfo &#8211;no-headers</code>, thereby creating plain text files.</p>
<dt><code>&#8211;help</code></p>
<dd> Show brief usage information and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version and exit.</dl>
<p> This program uses certain other programs for its operation. If they are not in their default installed locations, then use the following options to set their location:</p>
<dl>
<dt><code>&#8211;utf8trans-program=</code><i>path</i>, <code>&#8211;utf8trans-map=</code><i>charmap</i></p>
<dd> Use the character map <i>charmap</i> with the <code><a href="/docs/linux/man/1-utf8trans/">utf8trans</a></code>(1) program, included with docbook2X, found under <i>path</i>.</p>
<dt><code>&#8211;iconv-program=</code><i>path</i></p>
<dd> The location of the <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) program, used for encoding conversions.</dl>
<h2>NOTES</h2>
<p> <code>Texinfo language compatibility</code>. The Texinfo files generated by <code>db2x_texixml</code> sometimes require Texinfo version 4.7 (the latest version) to work properly. In particular:</p>
<dl>
<dt>&bull;</p>
<dd> <code>db2x_texixml</code> relies on <code>makeinfo</code> to automatically add punctuation after a @ref if it it not already there. Otherwise the hyperlink will not work in the Info reader (although <code>makeinfo</code> will not emit any error).</p>
<dt>&bull;</p>
<dd> The new @comma{} command is used for commas (,) occurring inside argument lists to Texinfo commands, to disambiguate it from the comma used to separate different arguments. The only alternative otherwise would be to translate , to . which is obviously undesirable (but earlier docbook2X versions did this). </p>
<p> If you cannot use version 4.7 of <code>makeinfo</code>, you can still use a <code>sed</code> script to perform manually the procedure just outlined.</dl>
<p> <code>Relation of Texi-XML with the XML output format of makeinfo</code>. The Texi-XML format used by docbook2X is <i>different</i> and incompatible with the XML format generated by <code><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></code>(1) with its <code>&#8211;xml</code> option. This situation arose partly because the Texi-XML format of docbook2X was designed and implemented independently before the appearance of <code>makeinfo</code>&#8216;s XML format. Also Texi-XML is very much geared towards being <i>machine-generated from other XML formats</i>, while there seems to be no non-trivial applications of <code>makeinfo</code>&#8216;s XML format. So there is no reason at this point for docbook2X to adopt <code>makeinfo</code>&#8216;s XML format in lieu of Texi-XML.</p>
<h2>BUGS</h2>
<dl>
<dt>&bull;</p>
<dd> Text wrapping in menus is utterly broken for non-ASCII text. It is probably also broken everywhere else in the output, but that would be <code>makeinfo</code>&#8216;s fault.</p>
<dt>&bull;</p>
<dd> <code>&#8211;list-files</code> might not work correctly with <code>&#8211;info</code>. Specifically, when the output Info file get too big, <code>makeinfo</code> will decide to split it into parts named <i>abc.info-1</i>, <i>abc.info-2</i>, <i>abc.info-3</i>, etc. <code>db2x_texixml</code> does not know exactly how many of these files there are, though you can just do an <code>ls</code> to find out.</dl>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> The docbook2X manual (in Texinfo or HTML format) fully describes how to convert DocBook to man pages and Texinfo. </p>
<p> Up-to-date information about this program can be found at the docbook2X Web site &lt;<a rel="nofollow" href="http://docbook2x.sourceforge.net/">http://docbook2x.sourceforge.net/</a>&gt; . </p>
<p> The input to <code>db2x_texixml</code> is defined by the XML DTD present at <i>dtd/Texi-XML</i> in the docbook2X distribution. </p>
<h2>Index</h2>
