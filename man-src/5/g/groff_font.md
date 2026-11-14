---
title: "groff_font(5)"
name: "groff_font"
section: "5"
letter: "g"
url: "/docs/linux/man/5-groff_font/"
description: "groff_font – format of groff device and font description files"
---

<p>groff_font &#8211; format of groff device and font description files</p>
<h2>Description</h2>
<p>The groff font format is roughly a superset of the ditroff font format. The font files for device <i>name</i> are stored in a directory <i>dev</i>name. There are two types of file: a device description file called <i>DESC</i> and for each font<i>~F</i>, a font file called~F. These are text files; unlike the ditroff font format, there is no associated binary format.</p>
<h3>DESC file format</h3>
<p>The <i>DESC</i> file can contain the following types of line as shown below. Later entries in the file override previous values. </p>
<p> Empty lines are ignored.</p>
<dl>
<dt><code>charset</code></p>
<dd>This line and everything following in the file are ignored. It is allowed for the sake of backwards compatibility.</p>
<dt><code>family </code><i>fam</i></p>
<dd>The default font family is <i>fam</i>.</p>
<dt><code>fonts </code><i>n F1 F2 F3 &#8230; Fn</i></p>
<dd>Fonts <i>F1</i>, &#8230;, <i>Fn</i> are mounted in the font positions <i>m</i>+1, &#8230;, <i>m</i>+<i>n</i> where <i>m</i> is the number of styles. This command may extend over more than one line. A font name of~<code>0</code> causes no font to be mounted on the corresponding font position.</p>
<dt><code>hor </code><i>n</i></p>
<dd>The horizontal resolution is <i>n</i>~machine units.</p>
<dt><code>image_generator </code><i>string</i></p>
<dd>Needed for <code>grohtml</code> only. It specifies the program to generate PNG images from PostScript input. Under GNU/Linux this is usually <i>gs</i> but under other systems (notably cygwin) it might be set to another name.</p>
<dt><code>paperlength </code><i>n</i></p>
<dd>The physical vertical dimension of the output medium in machine units. This isn&#8217;t used by <code>troff</code> itself but by output devices. Deprecated. Use <code>papersize</code> instead.</p>
<dt><code>papersize </code><i>string</i></p>
<dd>Select a paper size. Valid values for <i>string</i> are the ISO paper types A0-A7, B0-B7, C0-C7, D0-D7, DL, and the US paper types letter, legal, tabloid, ledger, statement, executive, com10, and monarch. Case is not significant for <i>string</i> if it holds predefined paper types. Alternatively, <i>string</i> can be a file name (e.g. <i>/etc/papersize</i>); if the file can be opened, <code>groff</code> reads the first line and tests for the above paper sizes. Finally, <i>string</i> can be a custom paper size in the format <i>length</i><code>,</code><i>width</i> (no spaces before and after the comma). Both <i>length</i> and <i>width</i> must have a unit appended; valid values are &#8216;i&#8217; for inches, &#8216;c&#8217; for centimeters, &#8216;p&#8217; for points, and &#8216;P&#8217; for picas. Example: <code>12c,235p</code>. An argument which starts with a digit is always treated as a custom paper format. <code>papersize</code> sets both the vertical and horizontal dimension of the output medium.</p>
<dd>More than one argument can be specified; <code>groff</code> scans from left to right and uses the first valid paper specification.</p>
<dt><code>paperwidth </code><i>n</i></p>
<dd>The physical horizontal dimension of the output medium in machine units. Deprecated. Use <code>papersize</code> instead. This isn&#8217;t used by <code>troff</code> itself but by output devices.</p>
<dt><code>pass_filenames</code></p>
<dd>Make troff tell the driver the source file name being processed. This is achieved by another tcommand: <code>F</code>~<i>filename</i>.</p>
<dt><code>postpro </code><i>program</i></p>
<dd>Use <i>program</i> as the postprocessor.</p>
<dt><code>prepro </code><i>program</i></p>
<dd>Call <i>program</i> as a preprocessor.</p>
<dt><code>print </code><i>program</i></p>
<dd>Use <i>program</i> as the spooler program for printing. If omitted, the <code>-l</code> and <code>-L</code> options of <code>groff</code> are ignored.</p>
<dt><code>res </code><i>n</i></p>
<dd>There are <i>n</i> machine units per inch.</p>
<dt><code>sizes </code><i>s1 s2 &#8230; sn </i><code>0</code></p>
<dd>This means that the device has fonts at <i>s1</i>, <i>s2</i>, &#8230;, <i>sn</i> scaled points. The list of sizes must be terminated by a <code>0</code>. Each <i>si</i> can also be a range of sizes <i>m</i>&#8211;<i>n</i>. The list can extend over more than one line.</p>
<dt><code>sizescale </code><i>n</i></p>
<dd>The scale factor for point sizes. By default this has a value of 1. One <i>scaled point</i> is equal to one point/<i>n</i>. The arguments to the <code>unitwidth</code> and <code>sizes</code> commands are given in scaled points.</p>
<dt><code>styles </code><i>S1 S2 &#8230; Sm</i></p>
<dd>The first <i>m</i> font positions are associated with styles <i>S1</i>, &#8230;, <i>Sm</i>.</p>
<dt><code>tcommand</code></p>
<dd>This means that the postprocessor can handle the <code>t</code> and~<code>u</code> output commands.</p>
<dt><code>unicode</code></p>
<dd>Indicate that the output device supports the complete Unicode repertoire. Useful only for devices which produce <i>character entities</i> instead of glyphs.</p>
<dd>If <code>unicode</code> is present, no <code>charset</code> section is required in the font description files since the Unicode handling built into <code>groff</code> is used. However, if there are entries in a <code>charset</code> section, they either override the default mappings for those particular characters or add new mappings (normally for composite characters).</p>
<dd>This is used for <code>-Tutf8</code>, <code>-Thtml</code>, and <code>-Txhtml</code>.</p>
<dt><code>unitwidth </code><i>n</i></p>
<dd>Quantities in the font files are given in machine units for fonts whose point size is <i>n</i>~scaled points.</p>
<dt><code>unscaled_charwidths</code></p>
<dd>Make the font handling module always return unscaled glyph widths. Needed for the <code>grohtml</code> device.</p>
<dt><code>use_charnames_in_special</code></p>
<dd>This command indicates that troff should encode named glyphs inside special commands.</p>
<dt><code>vert </code><i>n</i></p>
<dd>The vertical resolution is <i>n</i>~machine units.</dl>
<p> The <code>res</code>, <code>unitwidth</code>, <code>fonts</code>, and <code>sizes</code> lines are compulsory. Not all commands in the <i>DESC</i> file are used by <code>troff</code> itself; some of the keywords (or even additional ones) are used by postprocessors to store arbitrary information about the device. </p>
<p> Here a list of obsolete keywords which are recognized by <code>groff</code> but completely ignored: <code>spare1</code>, <code>spare2</code>, <code>biggestfont</code>.</p>
<h3>Font file format</h3>
<p>A font file has two sections; empty lines are ignored in both of them. </p>
<p> The first section is a sequence of lines each containing a sequence of blank delimited words; the first word in the line is a key, and subsequent words give a value for that key.</p>
<dl>
<dt><code>ligatures </code><i>lig1 lig2 &#8230; lign </i>[<code>0</code><i></i>]</p>
<dd>Glyphs <i>lig1</i>, <i>lig2</i>, &#8230;, <i>lign</i> are ligatures; possible ligatures are <code>ff</code>, <code>fi</code>, <code>fl</code>, <code>ffi</code>, and <code>ffl</code>. For backwards compatibility, the list of ligatures may be terminated with a~<code>0</code>. The list of ligatures may not extend over more than one line.</p>
<dt><code>name </code><i>F</i></p>
<dd>The name of the font is~<i>F</i>.</p>
<dt><code>slant </code><i>n</i></p>
<dd>The glyphs of the font have a slant of <i>n</i>~degrees. (Positive means forward.)</p>
<dt><code>spacewidth </code><i>n</i></p>
<dd>The normal width of a space is~<i>n</i>.</p>
<dt><code>special</code></p>
<dd>The font is <i>special</i>; this means that when a glyph is requested that is not present in the current font, it is searched for in any special fonts that are mounted.</dl>
<p> Other commands are ignored by <code>troff</code> but may be used by postprocessors to store arbitrary information about the font in the font file. </p>
<p> The first section can contain comments which start with the <code>#</code> character and extend to the end of a line. </p>
<p> The second section contains one or two subsections. It must contain a <i>charset</i> subsection and it may also contain a <i>kernpairs</i> subsection. These subsections can appear in any order. Each subsection starts with a word on a line by itself. </p>
<p> The word <code>charset</code> starts the charset subsection. The <code>charset</code> line is followed by a sequence of lines. Each line gives information for one glyph. A line comprises a number of fields separated by blanks or tabs. The format is</p>
<dl>
<dd><i>name metrics type code</i> [<i>entity_name</i>] [<code>&#8212;</code> <i>comment</i>]</dl>
<p> <i>name</i> identifies the glyph: if <i>name</i> is a single glyph <i>c</i> then it corresponds to the groff input character <i>c</i>; if it is of the form <code>\</code><i>c</i> where c is a single character, then it corresponds to the special character <code>\[</code><i>c</i><code>]</code>; otherwise it corresponds to the groff input character <code>\[</code><i>name</i><code>]</code>. If it is exactly two characters <i>xx</i> it can be entered as <code>\(</code><i>xx</i>. Note that single-letter special characters can&#8217;t be accessed as <code>\</code><i>c</i>; the only exception is &#8216;\-&#8216; which is identical to &#8216;\[-]&#8217;. The name <code>&#8212;</code> is special and indicates that the glyph is unnamed; such glyphs can only be used by means of the <code>\N</code> escape sequence in <code>troff</code>. </p>
<p> The <i>type</i> field gives the glyph type:</p>
<dl>
<dt>1</p>
<dd>means the glyph has a descender, for example, &#8216;p&#8217;;</p>
<dt>2</p>
<dd>means the glyph has an ascender, for example, &#8216;b&#8217;;</p>
<dt>3</p>
<dd>means the glyph has both an ascender and a descender, for example, &#8216;(&#8216;.</dl>
<p> The <i>code</i> field gives the code which the postprocessor uses to print the glyph. The glyph can also be input to groff using this code by means of the <code>\N</code> escape sequence. The code can be any integer. If it starts with a~<code>0</code> it is interpreted as octal; if it starts with <code>0x</code> or <code>0X</code> it is interpreted as hexadecimal. Note, however, that the <code>\N</code> escape sequence only accepts a decimal integer. </p>
<p> The <i>entity_name</i> field gives an ASCII string identifying the glyph which the postprocessor uses to print that glyph. This field is optional and is currently used by <code>grops</code> to build sub-encoding arrays for PS fonts containing more than 256 glyphs. (It has also been used for <code>grohtml</code>&#8216;s entity names but for efficiency reasons this data is now compiled directly into <code>grohtml</code>.) </p>
<p> Anything on the line after the encoding field or &#8216;&#8211;&#8216; are ignored. </p>
<p> The <i>metrics</i> field has the form (in one line; it is broken here for the sake of readability):</p>
<dl>
<dd><i>width/</i>[<code>,</code><i>height/</i>[<code>,</code><i>depth/</i>[<code>,</code><i>italic-correction</i><br />
 [<code>,</code><i>left-italic-correction/</i>[<code>,</code><i>subscript-correction</i>]]]]]</dl>
<p> There must not be any spaces between these subfields. Missing subfields are assumed to be~0. The subfields are all decimal integers. Since there is no associated binary format, these values are not required to fit into a variable of type <code>char</code> as they are in ditroff. The <i>width</i> subfields gives the width of the glyph. The <i>height</i> subfield gives the height of the glyph (upwards is positive); if a glyph does not extend above the baseline, it should be given a zero height, rather than a negative height. The <i>depth</i> subfield gives the depth of the glyph, that is, the distance below the baseline to which the glyph extends (downwards is positive); if a glyph does not extend below the baseline, it should be given a zero depth, rather than a negative depth. The <i>italic-correction</i> subfield gives the amount of space that should be added after the glyph when it is immediately to be followed by a glyph from a roman font. The <i>left-italic-correction</i> subfield gives the amount of space that should be added before the glyph when it is immediately to be preceded by a glyph from a roman font. The <i>subscript-correction</i> gives the amount of space that should be added after a glyph before adding a subscript. This should be less than the italic correction. </p>
<p> A line in the charset section can also have the format</p>
<dl>
<dd><i>name </i><code>&quot;</code></dl>
<p> This indicates that <i>name</i> is just another name for the glyph mentioned in the preceding line. </p>
<p> The word <code>kernpairs</code> starts the kernpairs section. This contains a sequence of lines of the form:</p>
<dl>
<dd><i>c1 c2 n</i></dl>
<p> This means that when glyph <i>c1</i> appears next to glyph <i>c2</i> the space between them should be increased by~<i>n</i>. Most entries in kernpairs section have a negative value for~<i>n</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/dev</i>name<i>/DESC</i></p>
<dd>Device description file for device <i>name</i>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/dev</i>name<i>/</i>F</p>
<dd>Font file for font~<i>F</i> of device <i>name</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-addftinfo/">addftinfo</a></code>(1), <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1) A man page <i>name</i>(<i>n</i>) of section <i>n</i> can be viewed either with</p>
<dl>
<dd>$ <code>man</code><i> n name</i></dl>
<p> for text mode or</p>
<dl>
<dd>$ <code>groffer</code><i> n name</i></dl>
<p> for graphical mode (default is PDF mode). </p>
