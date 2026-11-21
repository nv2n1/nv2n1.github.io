---
title: "txtconv(1)"
name: "txtconv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-txtconv/"
description: "txtconv – A tool to apply TECkit mappings to convert the encoding of a plain text file"
---

<h2>SYNOPSIS</h2>
<p> <code>txtconv</code> <i>,-i inFile -o outFile /</i>[<i>,-t tecFile/</i>] [<i>,-r/</i>] [<i>,-if inForm/</i>] [<i>,-of outForm/</i>] [<i>,-nobom/</i>] [<i>,-nf/</i>[<i>,cd/</i>]] [<i>,-u n/</i>]</p>
<h2>OPTIONS</h2>
<p> <code>Required arguments:</code></p>
<dl>
<dt><code>-i</code> &lt;file&gt;</dt>
<dd> input file</dd>
<dt><code>-o</code> &lt;file&gt;</dt>
<dd> output file</dd></dl>
<p> <code>Optional arguments:</code></p>
<dl>
<dt><code>-t</code> &lt;file&gt;</dt>
<dd> compiled TECkit mapping (.tec) file</dd>
<dt><code>-r</code></dt>
<dd> reverse (RHS-&gt;LHS, or Unicode-&gt;Byte) mapping</dd>
<dt><code>-if</code> &lt;form&gt;</dt>
<dd> input encoding form</dd>
<dt><code>-of</code> &lt;form&gt;</dt>
<dd> output encoding form</dd>
<dt><code>-nobom</code></dt>
<dd> don&#8217;t write a BOM to Unicode output</dd>
<dt><code>-nf[cd]</code></dt>
<dd> apply NFC or NFD normalization to Unicode output</dd>
<dt><code>-u</code> &lt;n&gt;</dt>
<dd> handling of unmappable input:</dd>
<dt>
</dt><dd> &bull; 0 = use replacement character .IP &bull; 1 = use replacement but generate warning .IP &bull; 2 = stop conversion</dd></dl>
<p> <code>Encoding forms:</code></p>
<dl>
<dt>
</dt><dd> bytes utf8 utf16be utf16le utf16 utf32be utf32le utf32</dd></dl>
<h2>Further Information</h2>
<p> For further information see the document TECkit_Tools.pdf. On a Debian system, this can be found in /usr/share/doc/teckit. </p>
