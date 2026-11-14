---
title: "hpftodit(1)"
name: "hpftodit"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpftodit/"
description: "hpftodit – create font description files for use with groff -Tlj4"
---

<h2 class="name">NAME</h2>
<p> hpftodit &#8211; create font description files for use with groff -Tlj4 </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-aqs</code> ] [ <code>-i </code><i>n</i> ] <i>tfm-file</i> <i>map-file</i> <i>output-font</i> <code>-d</code> <i>tfm-file</i> [<i>map-file</i>] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>hpftodit</code> creates a font file for use with a Hewlett-Packard LaserJet~4-series (or newer) printer with <code>groff -Tlj4</code>, using data from an HP tagged font metric (TFM) file. <i>tfm-file</i> is the name of the TFM file for the font; Intellifont and TrueType TFM files are supported, but symbol set TFM files are not. <i>map-file</i> is a file giving the <i>groff</i> names for characters in the font; this file should consist of a sequence of lines of the form:</p>
<dl>
<dt>
<dd> <i>m u c1 c2 </i>&#8230; [#<i> comment</i>]</dl>
<p> where <i>m</i> is a decimal integer giving the MSL (Master Symbol List) number of the character, <i>u</i> is a hexadecimal integer giving the Unicode value of the character, and <i>c1</i>, <i>c2</i>, &#8230; are the <i>groff</i> names of the character (see <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) for a list). The values can be separated by any whitespace; the Unicode value must use uppercase digits A-F, and must be without a leading &#8216;<code>0x</code>&#8216;, &#8216;<code>u</code>&#8216;, or &#8216;<code>U+</code>&#8216;. Unicode values corresponding to composite glyphs are decomposed; e.g., &#8216;<code>u00C0</code>&#8216; becomes &#8216;<code>u0041_0300</code>&#8216;. The name for a glyph without a <i>groff</i> name may be given as <code>u</code><i>XXXX</i> if the glyph corresponds to a Unicode value, or as an unnamed glyph &#8216;<code>&#8212;</code>&#8216;. If the given Unicode value is in the Private Use Area (0xE000-0xF8FF), the glyph is included as an unnamed glyph. Refer to <code><a href="/docs/linux/man/1-groff_diff/">groff_diff</a></code>(1) for additional information about unnamed glyphs and how to access them. </p>
<p> Blank lines and lines beginning with &#8216;<code>#</code>&#8216; are ignored. A &#8216;<code>#</code>&#8216; following one or more <i>groff</i> names begins a comment. Because &#8216;<code>#</code>&#8216; is a valid <i>groff</i> name, it must appear first in a list of <i>groff</i> names if a comment is included, e.g.,</p>
<dl>
<dt>
<dd> <code>3 0023 # # number sign</code></dl>
<p> or</p>
<dl>
<dt>
<dd> <code>3 0023 # sh # number sign</code></dl>
<p> rather than</p>
<dl>
<dt>
<dd> <code>3 0023 sh # # number sign</code></dl>
<p> which will treat the first &#8216;<code>#</code>&#8216; as the beginning of the comment. </p>
<p> The <i>groff</i> font file is written to the specified <i>output-font</i>; if this operand is &#8216;<code>&#8211;</code>&#8216;, the font file is written to the standard output. </p>
<p> The <code>-s</code> option should be given if the font is special (a font is &#8220;special&#8221; if <i>groff</i> should search it whenever a character is not found in the current font). If the font is special, it should be listed in the <code>fonts</code> command in the DESC file; if it is not special, there is no need to list it, since <i>groff</i> can automatically mount it when it&#8217;s first used. </p>
<p> If the <code>-i</code> option is used, <code>hpftodit</code> automatically will generate an italic correction, a left italic correction and a subscript correction for each character (the significance of these parameters is explained in <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5)).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Include characters in the TFM file that are not included in <i>map-file</i>. A glyph with corresponding Unicode value is given the name u<i>XXXX</i>; a glyph without a Unicode value is included as an unnamed glyph &#8216;&#8212;&#8216;. A glyph with a Unicode value in the Private Use Area (0xE000-0xF8FF) also is included as an unnamed glyph.</p>
<dt>
<dd> This option provides a simple means of adding Unicode-named and unnamed glyphs to a font without including them in the map file, but it affords little control over which glyphs are placed in a regular font and which are placed in a special font. The presence or absence of the <code>-s</code> option has some effect on which glyphs are included: without the <code>-s</code> option, only the &#8220;text&#8221; symbol sets are searched for matching glyphs; with the <code>-s</code> option, only the &#8220;mathematical&#8221; symbol sets are searched. Nonetheless, restricting the symbol sets searched isn&#8217;t very selective&#8212;many glyphs are placed in both regular and special fonts. Normally, the <code>-a</code> option should be used only as a last resort.</p>
<dt><code>-d</code></p>
<dd> Dump information about the TFM file to the standard output; this option can be useful for ensuring that a TFM file is a proper match for a font, and that the contents of the TFM file are suitable. The information includes the values of important TFM tags, and a listing (by MSL number for Intellifont TFM files or by Unicode value for TrueType TFM files) of the glyphs included in the TFM file. The unit of measure &#8216;DU&#8217; for some tags indicates design units; there are 8782~design units per em for Intellifont fonts, and 2048~design units per em for TrueType fonts. Note that the accessibility of a glyph depends on its inclusion in a symbol set; some TFM files list many glyphs but only a few symbol sets.</p>
<dt>
<dd> The glyph listing includes the glyph index within the TFM file, the MSL or Unicode value, and the symbol set and character code that will be used to print the glyph. If <i>map-file</i> is given, <i>groff</i> names are given for matching glyphs. If only the glyph index and MSL or Unicode value are given, the glyph does not appear in any supported symbol set and cannot be printed.</p>
<dt>
<dd> With the <code>-d</code> option, <i>map-file</i> is optional, and <i>output-font</i> is ignored if given.</p>
<dt><code>-q</code></p>
<dd> Suppress warnings about characters in the map file that were not found in the TFM file. Warnings never are given for unnamed glyphs or by glyphs named by their Unicode values. This option is useful when sending the output of <code>hpftodit</code> to the standard output.</p>
<dt><code>-v</code></p>
<dd> Print the <code>hpftodit</code> version number and exit.</p>
<dt><code>-s</code></p>
<dd> The font is special. This option adds the <code>special</code> command to the font file, and affects the order in which HP symbol sets are searched for each glyph. Without the <code>-s</code> option, the &#8220;text&#8221; sets are searched before the &#8220;mathematical&#8221; symbol sets. With the <code>-s</code> option, the search order is reversed.</p>
<dt><code>-i</code><i>n</i></p>
<dd> Generate an italic correction for each character so that the character&#8217;s width plus the character&#8217;s italic correction is equal to <i>n</i> thousandths of an em plus the amount by which the right edge of the character&#8217;s bounding is to the right of the character&#8217;s origin. If this would result in a negative italic correction, use a zero italic correction instead.</p>
<dt>
<dd> Also generate a subscript correction equal to the product of the tangent of the slant of the font and four fifths of the x-height of the font. If this would result in a subscript correction greater than the italic correction, use a subscript correction equal to the italic correction instead.</p>
<dt>
<dd> Also generate a left italic correction for each character equal to <i>n</i> thousandths of an em plus the amount by which the left edge of the character&#8217;s bounding box is to the left of the character&#8217;s origin. The left italic correction may be negative.</p>
<dt>
<dd> This option normally is needed only with italic or oblique fonts; a value of 50 (0.05~em) usually is a reasonable choice.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devlj4/:DESC</i></p>
<dd> device description file</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devlj4/:</i>F</p>
<dd> Font description file for font <i>F</i></p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/:devlj4/:generate/:</i>*<i>.map</i></p>
<dd> symbol mapping files</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-groff_diff/">groff_diff</a></code>(1), <code><a href="/docs/linux/man/1-grolj4/">grolj4</a></code>(1), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/5-lj4_font/">lj4_font</a></code>(5) </p>
<h2>Index</h2>
