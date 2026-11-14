---
title: "db2x_manxml(1)"
name: "db2x_manxml"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db2x_manxml/"
description: "db2x_manxml – Make man pages from Man-XML"
---

<h2>NAME</h2>
<p> db2x_manxml &#8211; Make man pages from Man-XML</p>
<h2>SYNOPSIS</h2>
<p> <code>db2x_manxml</code> [<i>options</i>] [<i>xml-document</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>db2x_manxml</code> converts a Man-XML document into one or more man pages. They are written in the current directory. </p>
<p> If <i>xml-document</i> is not given, then the document to convert is read from standard input.</p>
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
<dt><code>&#8211;help</code></p>
<dd> Show brief usage information and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version and exit.</dl>
<p> Some man pages may be referenced under two or more names, instead of just one. For example, <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3) and <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3) often point to the same man page which describes the two functions together. Choose one of the following options to select how such man pages are to be generated:</p>
<dl>
<dt><code>&#8211;symlinks</code></p>
<dd> For each of all the alternate names for a man page, erect symbolic links to the file that contains the real man page content.</p>
<dt><code>&#8211;solinks</code></p>
<dd> Generate stub pages (using .so roff requests) for the alternate names, pointing them to the real man page content.</p>
<dt><code>&#8211;no-links</code></p>
<dd> Do not make any alternative names available. The man page can only be referenced under its principal name.</dl>
<p> This program uses certain other programs for its operation. If they are not in their default installed locations, then use the following options to set their location:</p>
<dl>
<dt><code>&#8211;utf8trans-program=</code><i>path</i>, <code>&#8211;utf8trans-map=</code><i>charmap</i></p>
<dd> Use the character map <i>charmap</i> with the <code><a href="/docs/linux/man/1-utf8trans/">utf8trans</a></code>(1) program, included with docbook2X, found under <i>path</i>.</p>
<dt><code>&#8211;iconv-program=</code><i>path</i></p>
<dd> The location of the <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) program, used for encoding conversions.</dl>
<h2>NOTES</h2>
<p> The man pages produced should be compatible with most troff implementations and other tools that process man pages. Some backwards-compatible <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) extensions are used to make the output look nicer.</p>
<h2>AUTHOR</h2>
<p> Steve Cheng &lt;stevecheng [at] users.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> The docbook2X manual (in Texinfo or HTML format) fully describes how to convert DocBook to man pages and Texinfo. </p>
<p> Up-to-date information about this program can be found at the docbook2X Web site &lt;<a rel="nofollow" href="http://docbook2x.sourceforge.net/">http://docbook2x.sourceforge.net/</a>&gt; . </p>
<p> The input to <code>db2x_manxml</code> is defined by the XML DTD present at <i>dtd/Man-XML</i> in the docbook2X distribution. </p>
<h2>Index</h2>
