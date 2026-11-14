---
title: "ttfdump(1)"
name: "ttfdump"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttfdump/"
description: "ttfdump – Dumping the contents of a TrueType Font file"
---

<h2 class="name">NAME</h2>
<p> ttfdump &#8211; Dumping the contents of a TrueType Font file </p>
<h2>SYNOPSIS</h2>
<p> <code>ttfdump</code> [<code>-h</code>] [<code>-t</code> <i>tablename</i>] [<code>-g</code> <i>glyphnumber</i>] [<code>-c</code> <i>collection</i>] [<code>-o</code> <i>dumpfile</i>] [<code>-i</code>] <i>ttfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ttfdump</code> dumps the contents of a TrueType font file in ASCII form. A TrueType font file is consist of various tables. Those table are divided into two categories &#8211; <i>Required Tables</i> and <i>Optional Tables</i>. Mulitiple TrueType fonts can be merged to a TrueType Collection.</p>
<h3>Options</h3>
<dl>
<dt><code>-h</code></p>
<dd> Print a help message on standard output and exit.</p>
<dt><code>-t</code><i> tablename</i></p>
<dd> If this option is specified then dump the table <i>&quot;tablename&quot;</i>, otherwise dump every tables in <i>ttfile</i>. <i>Tablename</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Required Tables</code></p>
<dd>
<dt><i>cmap</i></p>
<dd> character to glyph mapping table</p>
<dt><i>glyf</i></p>
<dd> glyph data</p>
<dt><i>head</i></p>
<dd> font header</p>
<dt><i>hhea</i></p>
<dd> horizontal header</p>
<dt><i>hmtx</i></p>
<dd> horizontal metrics</p>
<dt><i>loca</i></p>
<dd> index to location</p>
<dt><i>maxp</i></p>
<dd> maximum profile</p>
<dt><i>name</i></p>
<dd> naming table</p>
<dt><i>post</i></p>
<dd> PostScript information</p>
<dt><i>OS/2</i></p>
<dd> OS/2 and windows specific metrics</p>
<dt><code>Optional Tables</code></p>
<dd>
<dt><i>cvt</i></p>
<dd> control value table</p>
<dt><i>fpgm</i></p>
<dd> font program; <i>not implemented yet.</i></p>
<dt><i>gasp</i></p>
<dd> grid-fitting and scan conversion procedure (grayscale)</p>
<dt><i>hdmx</i></p>
<dd> horizontal device metrics</p>
<dt><i>kern</i></p>
<dd> kerning table</p>
<dt><i>LTSH</i></p>
<dd> Linear threshold table</p>
<dt><i>prep</i></p>
<dd> CVT program; <i>not implemented yet</i></p>
<dt><i>PCLT</i></p>
<dd> PCL5 table</p>
<dt><i>VDMX</i></p>
<dd> Vertical Device Metrics table</p>
<dt><i>vhea</i></p>
<dd> vertical metrics header</p>
<dt><i>vmtx</i></p>
<dd> vertical metrics</p>
<dt><code>Additional OpenType Tables</code></p>
<dd>
<dt><i>GPOS</i></p>
<dd> glyph positioning table</p>
<dt><i>GSUB</i></p>
<dd> glyph substitution table</dl>
</dl>
<dt><code>-g</code><i> glyphnumber</i></p>
<dd> If this option is specified then dump the glyph with index <i>glyphnumber</i>, otherwise dump all glyphs in <i>ttfile</i>.</p>
<dt><code>-c</code><i> collection</i></p>
<dd> Select a TrueType font in a TrueType Collection.</p>
<dt><code>-o</code><i> dumpfile</i></p>
<dd> Output of the dump. If this option is not specified, dump to stdout.</p>
<dt><code>-i</code><i> ttfile</i></p>
<dd> TrueType font file to be dumped.</dl>
<h2>EXAMPLE</h2>
<p> To dump all information in the TrueType font file times.ttf:</p>
<dl>
<dt>
<dd> ttfdump times.ttf</dl>
<p> To dump the required table <i>cmap</i> in the file:</p>
<dl>
<dt>
<dd> ttfdump -t cmap times.ttf</dl>
<p> To dump a single glyph with index 50:</p>
<dl>
<dt>
<dd> ttfdump -g 50 times.ttf</dl>
<h2>SEE ALSO</h2>
<p> TrueType 1.0 Font Files, <i> Technical Specification Revision 1.66 November 1995</i></p>
<h2>NOTE</h2>
<p> Instruction disassembler in not implemented.</p>
<h2>AUTHOR</h2>
<p> Li-Da Lho, ollie [at] ms1.hinet.net </p>
<h2>Index</h2>
