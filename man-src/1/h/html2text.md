---
title: "html2text(1)"
name: "html2text"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html2text/"
description: "html2text – an advanced HTML-to-text converter"
---

<h2 class="name">NAME</h2>
<p> html2text &#8211; an advanced HTML-to-text converter </p>
<h2>SYNOPSIS</h2>
<p> <code>html2text -help</code><br />
 <code>html2text -version</code><br />
 <code>html2text</code> [ <code>-unparse</code> | <code>-check</code> ] [ <code>-debug-scanner</code> ] [ <code>-debug-parser</code> ] [ <code>-rcfile</code> <i>path</i> ] [ <code>-style</code> ( <code>compact</code> | <code>pretty</code> ) ] [ <code>-width</code> <i>width</i> ] [ <code>-o</code> <i>output-file</i> ] [ <code>-nobs</code> ] [ <code>-ascii</code> | <code>-utf8</code> ] [ <code>-nometa</code> ] [ <i>input-file</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>html2text</code> reads HTML documents from the <i>input-file</i>s, formats each of them into a stream of plain text characters, and writes the result to standard output (or into <i>output-file</i>, if the <code>-o</code> command line option is used). </p>
<p> If no <i>input-file</i>s are specified on the command line, <code>html2text</code> reads from standard input. A dash as the <i>input-file</i> is an alternate way to specify standard input. </p>
<p> <code>html2text</code> understands all HTML 3.2 constructs, but can render only part of them due to the limitations of the text output format. However, the program attempts to provide good substitutes for the elements it cannot render. <code>html2text</code> parses HTML 4 input, too, but not always as successful as other HTML processors. It also accepts syntactically incorrect input, and attempts to interpret it &quot;reasonably&quot;. </p>
<p> The way <code>html2text</code> formats the HTML documents is controlled by formatting properties read from an RC file. <code>html2text</code> attempts to read <i>$HOME/.html2textrc</i> (or the file specified by the <code>-rcfile</code> command line option); if that file cannot be read, <code>html2text</code> attempts to read <i>/etc/html2textrc</i>. If no RC file can be read (or if the RC file does not override all formatting properties), then &quot;reasonable&quot; defaults are assumed. The RC file format is described in the <code><a href="/docs/linux/man/5-html2textrc/">html2textrc</a></code>(5) manual page. </p>
<p> Debian version of <code>html2text</code> also can do input and output recoding (see /usr/share/doc/html2text/README.Debian for more info). <code>html2text</code> tries to fetch encoding from HTML document. If encoding is not specified, you can use <code>-ascii</code> and <code>-utf8</code> options. Output is converted to user&#8217;s locale charset (LC_CTYPE).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-nometa</code></p>
<dd> By default, Debian version of <code>html2text</code> use &#8216;meta http-equiv&#8217; tag for input recoding. This option cancels this behavior.</p>
<dt><code>-ascii</code></p>
<dd> By default, when <code>-nometa</code> is supplied, <code>html2text</code> uses <code>UTF-8</code> for the output. Specifying this option, plain <code>ASCII</code> is used instead. To find out how non-ASCII characters are rendered, refer to the file &quot;ascii.substitutes&quot;.</p>
<dt><code>-utf8</code></p>
<dd> By default, when <code>-nometa</code> is supplied, <code>html2text</code> uses <code>ISO 8859-1</code> for the input. Specifying this option, <code>UTF-8</code> is used instead (both for input and output). This option implies <code>-nobs</code>.</p>
<dt><code>-check</code></p>
<dd> This option is for diagnostic purposes: The HTML document is only parsed and not processed otherwise. In this mode of operation, <code>html2text</code> will report on parse errors and scan errors, which it does not in other modes of operation. Note that parse and scan errors are not fatal for <code>html2text</code>, but may cause mis-interpretation of the HTML code and/or portions of the document being swallowed.</p>
<dt><code>-debug-parser</code></p>
<dd> Let <code>html2text</code> report on the tokens being shifted, rules being applied, etc., while scanning the HTML document. This option is for diagnostic purposes.</p>
<dt><code>-debug-scanner</code></p>
<dd> Let <code>html2text</code> report on each lexical token scanned, while scanning the HTML document. This option is for diagnostic purposes.</p>
<dt><code>-help</code></p>
<dd> Print command line summary and exit.</p>
<dt><code>-nobs</code></p>
<dd> By default, original <code>html2text</code> renders underlined letters with sequences like &quot;underscore-backspace-character&quot; and boldface letters like &quot;character-backspace-character&quot;. Because of issues with UTF-8, Debian version of <code>html2text</code> doesn&#8217;t produce backspaces, so this option really does nothing.</p>
<dt><code>-o</code><i> output-file</i></p>
<dd> Write the output to <i>output-file</i> instead of standard output. A dash as the <i>output-file</i> is an alternate way to specify the standard output.</p>
<dt><code>-rcfile</code><i> path</i></p>
<dd> Attempt to read the file specified in <i>path</i> as RC file.</p>
<dt><code>-style</code> ( <code>compact</code> | <code>pretty</code> )</p>
<dd> Style <code>pretty</code> changes some of the default values of the formatting parameters documented in <code><a href="/docs/linux/man/5-html2textrc/">html2textrc</a></code>(5). To find out which and how the formatting parameter defaults are changed, check the file &quot;pretty.style&quot;. If this option is omitted, style <code>compact</code> is assumed as default.</p>
<dt><code>-unparse</code></p>
<dd> This option is for diagnostic purposes: Instead of formatting the parsed document, generate HTML code, that is guaranteed to be syntactically correct. If <code>html2text</code> has problems parsing a syntactically incorrect HTML document, this option may help you to understand what <code>html2text</code> thinks that the original HTML code means.</p>
<dt><code>-version</code></p>
<dd> Print program version and exit.</p>
<dt><code>-width</code><i> width</i></p>
<dd> By default, <code>html2text</code> formats the HTML documents for a screen width of 79 characters. If redirecting the output into a file, or if your terminal has a width other than 80 characters, or if you just want to get an idea how <code>html2text</code> deals with large tables and different terminal widths, you may want to specify a different <i>width</i>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/html2textrc</i></p>
<dd> System wide parser configuration file.</p>
<dt><i>$HOME/.html2textrc</i></p>
<dd> Personal parser configuration file, overrides the system wide values.</dl>
<h2>CONFORMING TO</h2>
<p> <code>HTML 3.2</code> (HTML 3.2 Reference Specification &#8211; <a rel="nofollow" href="http://www.w3.org/TR/REC-html32">http://www.w3.org/TR/REC-html32</a>),</p>
<h2>RESTRICTIONS</h2>
<p> Debian version of <code>html2text</code> have no http support. Use <code>html2text</code> through pipes with curl or wget instead. See README.Debian for more information. </p>
<p> <code>html2text</code> was written to convert HTML 3.2 documents. When using it with HTML 4 or even XHTML 1 documents, some constructs present only in these HTML versions might not be rendered.</p>
<h2>AUTHOR</h2>
<p> <code>html2text</code> was written up to version 1.2.2 by Arno Unkrig &lt;arno [at] unkrig.de&gt; for GMRS Software GmbH, Unterschleissheim. </p>
<p> Current maintainer and primary download location is:<br />
 Martin Bayer &lt;mail [at] mbayer.de&gt;<br />
 <a rel="nofollow" href="http://www.mbayer.de/html2text/files.shtml">http://www.mbayer.de/html2text/files.shtml</a> </p>
<p> This man page was modified for Debian by Eugene V. Lyubimkin &lt;jackyf.devel [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-html2textrc/">html2textrc</a></code>(5), <code><a href="/docs/linux/man/1-less/">less</a></code>(1), <code><a href="/docs/linux/man/1-more/">more</a></code>(1) </p>
<h2>Index</h2>
