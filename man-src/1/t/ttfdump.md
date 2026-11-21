---

title: "ttfdump(1)"
name: "ttfdump"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttfdump/"
description: "ttfdump – Dumping the contents of a TrueType Font file"
---

<p> <code>ttfdump</code> [<code>-h</code>] [<code>-t</code> <i>tablename</i>] [<code>-g</code> <i>glyphnumber</i>] [<code>-c</code> <i>collection</i>] [<code>-o</code> <i>dumpfile</i>] [<code>-i</code>] <i>ttfile</i></p>
<p> <code>ttfdump</code> dumps the contents of a TrueType font file in ASCII form. A TrueType font file is consist of various tables. Those table are divided into two categories &#8211; <i>Required Tables</i> and <i>Optional Tables</i>. Mulitiple TrueType fonts can be merged to a TrueType Collection.</p>
<h3>Options</h3>
<dl>
<dt><code>-h</code></dt>
<dd> Print a help message on standard output and exit.</dd>
<dt><code>-t</code><i> tablename</i></dt>
<dd> If this option is specified then dump the table <i>&quot;tablename&quot;</i>, otherwise dump every tables in <i>ttfile</i>. <i>Tablename</i> can be one of the following:</dd>
<dl>
<dl>
<dt><code>Required Tables</code></dt>
<dd>
</dd><dt><i>cmap</i></dt>
<dd> character to glyph mapping table</dd>
<dt><i>glyf</i></dt>
<dd> glyph data</dd>
<dt><i>head</i></dt>
<dd> font header</dd>
<dt><i>hhea</i></dt>
<dd> horizontal header</dd>
<dt><i>hmtx</i></dt>
<dd> horizontal metrics</dd>
<dt><i>loca</i></dt>
<dd> index to location</dd>
<dt><i>maxp</i></dt>
<dd> maximum profile</dd>
<dt><i>name</i></dt>
<dd> naming table</dd>
<dt><i>post</i></dt>
<dd> PostScript information</dd>
<dt><i>OS/2</i></dt>
<dd> OS/2 and windows specific metrics</dd>
<dt><code>Optional Tables</code></dt>
<dd>
</dd><dt><i>cvt</i></dt>
<dd> control value table</dd>
<dt><i>fpgm</i></dt>
<dd> font program; <i>not implemented yet.</i></dd>
<dt><i>gasp</i></dt>
<dd> grid-fitting and scan conversion procedure (grayscale)</dd>
<dt><i>hdmx</i></dt>
<dd> horizontal device metrics</dd>
<dt><i>kern</i></dt>
<dd> kerning table</dd>
<dt><i>LTSH</i></dt>
<dd> Linear threshold table</dd>
<dt><i>prep</i></dt>
<dd> CVT program; <i>not implemented yet</i></dd>
<dt><i>PCLT</i></dt>
<dd> PCL5 table</dd>
<dt><i>VDMX</i></dt>
<dd> Vertical Device Metrics table</dd>
<dt><i>vhea</i></dt>
<dd> vertical metrics header</dd>
<dt><i>vmtx</i></dt>
<dd> vertical metrics</dd>
<dt><code>Additional OpenType Tables</code></dt>
<dd>
</dd><dt><i>GPOS</i></dt>
<dd> glyph positioning table</dd>
<dt><i>GSUB</i></dt>
<dd> glyph substitution table</dd></dl>
</dl>
<dt><code>-g</code><i> glyphnumber</i></dt>
<dd> If this option is specified then dump the glyph with index <i>glyphnumber</i>, otherwise dump all glyphs in <i>ttfile</i>.</dd>
<dt><code>-c</code><i> collection</i></dt>
<dd> Select a TrueType font in a TrueType Collection.</dd>
<dt><code>-o</code><i> dumpfile</i></dt>
<dd> Output of the dump. If this option is not specified, dump to stdout.</dd>
<dt><code>-i</code><i> ttfile</i></dt>
<dd> TrueType font file to be dumped.</dd></dl>
<h2>EXAMPLE</h2>
<p> To dump all information in the TrueType font file times.ttf:</p>
<dl>
<dt>
</dt><dd> ttfdump times.ttf</dd></dl>
<p> To dump the required table <i>cmap</i> in the file:</p>
<dl>
<dt>
</dt><dd> ttfdump -t cmap times.ttf</dd></dl>
<p> To dump a single glyph with index 50:</p>
<dl>
<dt>
</dt><dd> ttfdump -g 50 times.ttf</dd></dl>
<h2>SEE ALSO</h2>
<p> TrueType 1.0 Font Files, <i> Technical Specification Revision 1.66 November 1995</i></p>
<h2>NOTE</h2>
<p> Instruction disassembler in not implemented.</p>
<h2>AUTHOR</h2>
<p> Li-Da Lho, ollie [at] ms1.hinet.net </p>
