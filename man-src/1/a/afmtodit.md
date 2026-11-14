---
title: "afmtodit(1)"
name: "afmtodit"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afmtodit/"
description: "afmtodit – create font files for use with groff -Tps and -Tpdf"
---

<h2 class="name">NAME</h2>
<p> afmtodit &#8211; create font files for use with groff -Tps and -Tpdf </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-ckmnsx</code> ] [ <code>-a </code><i>n</i> ] [ <code>-d </code><i>desc-file</i> ] [ <code>-e </code><i>enc-file</i> ] [ <code>-f </code><i>internal-name</i> ] [ <code>-i </code><i>n</i> ] [ <code>-o </code><i>output-file</i> ] <i>afm-file</i> <i>map-file</i> <i>font</i> <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <i>afmtodit</i> creates a font file for use with <i>groff</i>, <i>grops</i>, and <i>gropdf</i>. <i>afmtodit</i> is written in Perl; you must have Perl version 5.004 or newer installed in order to run <i>afmtodit</i>. </p>
<p> <i>afm-file</i> is the AFM (Adobe Font Metric) file for the font. </p>
<p> <i>map-file</i> is a file that says which <i>groff</i> character names map onto each PostScript character name; this file should contain a sequence of lines of the form</p>
<dl>
<dt>
<dd> <i>ps-char groff-char</i></dl>
<p> where <i>ps-char</i> is the PostScript name of the character and <i>groff-char</i> is the groff name of the character (as used in the <i>groff</i> font file). The same <i>ps-char</i> can occur multiple times in the file; each <i>groff-char</i> must occur at most once. Lines starting with &#8216;#&#8217; and blank lines are ignored. If the file isn&#8217;t found in the current directory, it is searched for in the <i>devps/generate</i> subdirectory of the default font directory. </p>
<p> If a PostScript character is not mentioned in <i>map-file</i>, and a generic <i>groff</i> glyph name can&#8217;t be deduced using the Adobe Glyph List (AGL, built into <i>afmtodit</i>), then <i>afmtodit</i> puts the PostScript character into the <i>groff</i> font file as an unnamed character which can only be accessed by the &#8216;\N&#8217; escape sequence in a <i>roff</i> document. In particular, this is true for glyph variants named in the form &#8220;foo.bar&#8221;; all glyph names containing one or more periods are mapped to unnamed entities. If option <code>-e</code> is not specified, the encoding defined in the AFM file (i.e., entries with non-negative character codes) is used. Refer to section &#8220;Using Symbols&#8221; in <i>Groff: The GNU Implementation of troff</i>, the <i>groff</i> Texinfo manual, which describes how <i>groff</i> glyph names are constructed. </p>
<p> Characters not encoded in the AFM file (i.e., entries which have &#8216;-1&#8217; as the character code) are still available in <i>groff</i>; they get glyph index values greater than 255 (or greater than the biggest character code used in the AFM file in the unlikely case that it is greater than 255) in the <i>groff</i> font file. Glyph indices of unencoded characters don&#8217;t have a specific order; it is best to access them with glyph names only. </p>
<p> The <i>groff</i> font file will be output to a file called <i>font</i>, unless the <code>-o</code> option is used. </p>
<p> If there is a downloadable font file for the font, it may be listed in the file <i>/usr/:share/:groff/:1.22.4/:font/:devps/:download</i>; see <i><a href="/docs/linux/man/1-grops/">grops</a></i>(1). </p>
<p> If the <code>-i</code> option is used, <i>afmtodit</i> will automatically generate an italic correction, a left italic correction and a subscript correction for each character (the significance of these parameters is explained in <i><a href="/docs/linux/man/5-groff_font/">groff_font</a></i>(5)); these parameters may be specified for individual characters by adding to the <i>afm-file</i> lines of the form:</p>
<dl>
<dt>
<dd> <code>italicCorrection</code><i>~ps-char~n</i> <code>leftItalicCorrection</code><i>~ps-char~n</i> <code>subscriptCorrection</code><i>~ps-char~n</i></dl>
<p> where <i>ps-char</i> is the PostScript name of the character, and <i>n</i> is the desired value of the corresponding parameter in thousandths of an em. These parameters are normally needed only for italic (or oblique) fonts.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-a</code><i>n</i></p>
<dd> Use <i>n</i> as the slant parameter in the font file; this is used by <i>groff</i> in the positioning of accents. By default <i>afmtodit</i> uses the negative of the <code>ItalicAngle</code> specified in the AFM file; with true italic fonts it is sometimes desirable to use a slant that is less than this. If you find that characters from an italic font have accents placed too far to the right over them, then use the <code>-a</code> option to give the font a smaller slant.</p>
<dt><code>-c</code></p>
<dd> Include comments in the font file in order to identify the PostScript font.</p>
<dt><code>-d</code><i>desc-file</i></p>
<dd> The device description file is <i>desc-file</i> rather than the default <i>DESC</i>. If not found in the current directory, the <i>devps</i> subdirectory of the default font directory is searched (this is true for both the default device description file and a file given with option <code>-d</code>).</p>
<dt><code>-e</code><i>enc-file</i></p>
<dd> The PostScript font should be reencoded to use the encoding described in <i>enc-file</i>. The format of <i>enc-file</i> is described in <i><a href="/docs/linux/man/1-grops/">grops</a></i>(1). If not found in the current directory, the <i>devps</i> subdirectory of the default font directory is searched.</p>
<dt><code>-f</code><i>name</i></p>
<dd> The internal name of the <i>groff</i> font is set to <i>name</i>.</p>
<dt><code>-i</code><i>n</i></p>
<dd> Generate an italic correction for each character so that the character&#8217;s width plus the character&#8217;s italic correction is equal to <i>n</i> thousandths of an em plus the amount by which the right edge of the character&#8217;s bounding box is to the right of the character&#8217;s origin. If this would result in a negative italic correction, use a zero italic correction instead.</p>
<dt>
<dd> Also generate a subscript correction equal to the product of the tangent of the slant of the font and four fifths of the x-height of the font. If this would result in a subscript correction greater than the italic correction, use a subscript correction equal to the italic correction instead.</p>
<dt>
<dd> Also generate a left italic correction for each character equal to <i>n</i> thousandths of an em plus the amount by which the left edge of the character&#8217;s bounding box is to the left of the character&#8217;s origin. The left italic correction may be negative unless option <code>-m</code> is given.</p>
<dt>
<dd> This option is normally needed only with italic (or oblique) fonts. The font files distributed with <i>groff</i> were created using an option of <code>-i50</code> for italic fonts.</p>
<dt><code>-o</code><i>output-file</i></p>
<dd> The output file is <i>output-file</i> instead of <i>font</i>.</p>
<dt><code>-k</code></p>
<dd> Omit any kerning data from the <i>groff</i> font; use only for monospaced (constant-width) fonts.</p>
<dt><code>-m</code></p>
<dd> Prevent negative left italic correction values. Roman font files distributed with <i>groff</i> were created with <code>-i0 -m</code> to improve spacing with <i><a href="/docs/linux/man/1-eqn/">eqn</a></i>(1).</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t output a <code>ligatures</code> command for this font; use with monospaced (constant-width) fonts.</p>
<dt><code>-s</code></p>
<dd> The font is special. The effect of this option is to add the <code>special</code> command to the font file.</p>
<dt><code>-v</code></p>
<dd> Print version and exit.</p>
<dt><code>-x</code></p>
<dd> Don&#8217;t use the built-in Adobe Glyph List.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devps/:DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devps/:</i>F</p>
<dd> Font description file for font <i>F</i>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devps/:download</i></p>
<dd> List of downloadable fonts.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devps/:text.enc</i></p>
<dd> Encoding used for text fonts.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devps/:generate/:textmap</i></p>
<dd> Standard mapping.</dl>
<h2>SEE ALSO</h2>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. Section &#8220;Using Symbols&#8221; may be of particular note. You can browse it interactively with &#8220;info &#8216;(groff)Using Symbols'&#8221;. </p>
<p> <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-gropdf/">gropdf</a></i>(1), <i><a href="/docs/linux/man/1-grops/">grops</a></i>(1), <i><a href="/docs/linux/man/5-groff_font/">groff_font</a></i>(5), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1) </p>
<h2>Index</h2>
