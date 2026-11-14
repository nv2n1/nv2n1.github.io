---
title: "flpsed(1)"
name: "flpsed"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flpsed/"
description: "flpsed – annotate PostScript and PDF files"
---

<h2>NAME</h2>
<p> <code>flpsed</code> &#8211; annotate PostScript and PDF files</p>
<h2>SYNOPSIS</h2>
<p> [-<code>bdh</code> ] [-<code>t </code><i>tag=value</i> ] [-<code>z </code><i>zoom</i> ] [<i>infile</i> ] [<i>outfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility allows to annotate Postscript files. PDF files can be imported using the pdftops and exported using the ps2pdf utility. If the document was saved in Postscript format, added text can be reedited later. is useful for filling in forms or adding short comments. Batch mode can be used to automate form filling. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b</code></p>
<dd> Batch mode (no GUI). In batch mode reads from stdin, if no <i>infile</i> is specified. Batch mode is useful in combination with the <i>&#8211;</i><code>t</code> option.</p>
<dt><code>-d</code></p>
<dd> Dump tags and values from a document to stdout (implies &#8211;<code>b</code> ).</p>
<dt><code>-h</code></p>
<dd> Show short help text.</p>
<dt><code>-t </code><i>tag=value</i></p>
<dd> Set text to <i>value</i> where tag is <i>tag</i> Multiple &#8211;<code>t</code> options are allowed.</p>
<dt><code>-z </code><i>zoom</i></p>
<dd> Set initial zoom value in percent.</p>
<dt><code>-geometry </code><i>WxH+X+Y</i></p>
<dd> Set initial geometry.</p>
<dt><code>-iconic</code></p>
<dd> Start iconified.</p>
<dt><code>-scheme </code><i>string</i></p>
<dd> Use fltk scheme <i>string</i> Currently fltk supports &quot;plastic&quot; and &quot;gtk+&quot;.</dl>
<h2>EXIT STATUS</h2>
<p> Ex -std</p>
<h2>EXAMPLES</h2>
<p> The command: </p>
<blockquote><p><tt>&quot;flpsed file1&quot;</tt></p></blockquote>
<p> will start flpsed and load file1 for interactive editing. </p>
<p> The command: </p>
<blockquote><p><tt>&quot;flpsed -b -t foo=bar file1 file2&quot;</tt></p></blockquote>
<p> will set the text of all text fields in file1 carrying the tag &quot;foo&quot; to &quot;bar&quot; and write the resulting Postscript document to file2</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pdftops/">pdftops</a>(1), <a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a>(1)</p>
<h2>AUTHOR</h2>
<p> Johannes Hofmann &lt;Johannes.Hofmann [at] gmx.de&gt; </p>
<h2>Index</h2>
