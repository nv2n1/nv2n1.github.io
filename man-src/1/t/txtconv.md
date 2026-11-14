---
title: "txtconv(1)"
name: "txtconv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-txtconv/"
description: "txtconv – A tool to apply TECkit mappings to convert the encoding of a plain text file"
---

<h2 class="name">NAME</h2>
<p> txtconv &#8211; A tool to apply TECkit mappings to convert the encoding of a plain text file </p>
<h2>SYNOPSIS</h2>
<p> <code>txtconv</code> <i>,-i inFile -o outFile /</i>[<i>,-t tecFile/</i>] [<i>,-r/</i>] [<i>,-if inForm/</i>] [<i>,-of outForm/</i>] [<i>,-nobom/</i>] [<i>,-nf/</i>[<i>,cd/</i>]] [<i>,-u n/</i>]</p>
<h2>OPTIONS</h2>
<p> <code>Required arguments:</code></p>
<dl>
<dt><code>-i</code> &lt;file&gt;</p>
<dd> input file</p>
<dt><code>-o</code> &lt;file&gt;</p>
<dd> output file</dl>
<p> <code>Optional arguments:</code></p>
<dl>
<dt><code>-t</code> &lt;file&gt;</p>
<dd> compiled TECkit mapping (.tec) file</p>
<dt><code>-r</code></p>
<dd> reverse (RHS-&gt;LHS, or Unicode-&gt;Byte) mapping</p>
<dt><code>-if</code> &lt;form&gt;</p>
<dd> input encoding form</p>
<dt><code>-of</code> &lt;form&gt;</p>
<dd> output encoding form</p>
<dt><code>-nobom</code></p>
<dd> don&#8217;t write a BOM to Unicode output</p>
<dt><code>-nf[cd]</code></p>
<dd> apply NFC or NFD normalization to Unicode output</p>
<dt><code>-u</code> &lt;n&gt;</p>
<dd> handling of unmappable input:</p>
<dt>
<dd> &bull; 0 = use replacement character .IP &bull; 1 = use replacement but generate warning .IP &bull; 2 = stop conversion</dl>
<p> <code>Encoding forms:</code></p>
<dl>
<dt>
<dd> bytes utf8 utf16be utf16le utf16 utf32be utf32le utf32</dl>
<h2>Further Information</h2>
<p> For further information see the document TECkit_Tools.pdf. On a Debian system, this can be found in /usr/share/doc/teckit. </p>
<h2>Index</h2>
