---
title: "ttf2tfm(1)"
name: "ttf2tfm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2tfm/"
description: "ttf2tfm – build TeX metric files from a TrueType font"
---

<h2 class="name">NAME</h2>
<p> ttf2tfm &#8211; build TeX metric files from a TrueType font </p>
<h2>SYNOPSIS</h2>
<p> <code>ttf2tfm</code> <i>ttffile</i>[<code>.ttf</code>|<code>.ttc</code>] [<code>-c</code><i>&nbsp;caps-height-factor</i>] [<code>-e</code><i>&nbsp;extension-factor</i>] [<code>-E</code><i>&nbsp;encoding-id</i>] [<code>-f</code><i>&nbsp;font-index</i>] [<code>-l</code>] [<code>-L&nbsp;</code><i>ligature-file</i>[<i>.sfd</i>]] [<code>-n</code>] [<code>-N</code>] [<code>-O</code>] [<code>-p&nbsp;</code><i>inencfile</i>[<i>.enc</i>]] [<code>-P</code><i>&nbsp;platform-id</i>] [<code>-q</code>] [<code>-r</code><i>&nbsp;old-glyphname new-glyphname</i>] [<code>-R&nbsp;</code><i>replacement-file</i>[<i>.rpl</i>]] [<code>-s</code><i>&nbsp;slant-factor</i>] [<code>-t&nbsp;</code><i>outencfile</i>[<i>.enc</i>]] [<code>-T&nbsp;</code><i>inoutencfile</i>[<i>.enc</i>]] [<code>-u</code>] [<code>-v&nbsp;</code><i>vplfile</i>[<i>.vpl</i>]] [<code>-V&nbsp;</code><i>scvplfile</i>[<i>.vpl</i>]] [<code>-w</code>] [<code>-x</code>] [<code>-y</code><i>&nbsp;vertical-shift-factor</i>] [<i>tfmfile</i>[<i>.tfm</i>]]<br />
 <code>ttf2tfm &#8211;version</code> | <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> This program extracts the metric and kerning information of a TrueType font and converts it into metric files usable by TeX (quite similar to <code>afm2tfm</code> which is part of the <code>dvips</code> package; please consult its info files for more details on the various parameters (especially encoding files). </p>
<p> Since a TrueType font often contains more than 256 glyphs, some means are necessary to map a subset of the TrueType glyphs onto a TeX font. To do this, two mapping tables are needed: the first (called `input&#8217; or `raw&#8217; encoding) maps the TrueType font to a raw TeX font (this mapping table is used by both <code>ttf2tfm</code> and <code>ttf2pk</code>), and the second (called `output&#8217; or `virtual&#8217; encoding) maps the raw TeX font to another (virtual) TeX font, providing all kerning and ligature information needed by TeX. </p>
<p> This two stage mapping has the advantage that one raw font can be accessed with various LaTeX encodings (e.g. T1 and OT1) via the virtual font mechanism, and just one file is necessary. </p>
<p> For CJKV (Chinese/Japanese/Korean/old Vietnamese) fonts, a different mechanism is provided (see <code>SUBFONT DEFINITION FILES</code> below).</p>
<h2>PARAMETERS</h2>
<p> Most of the command line switch names are the same as in <code>afm2tfm</code> for convenience. One or more space characters between an option and its value is mandatory; options can&#8217;t be concatenated. For historical reasons, the first parameter can <i>not</i> be a switch but must be the font name.</p>
<dl>
<dt><code>-c</code><i>&nbsp;caps-height-factor</i></p>
<dd> The height of small caps made with the <code>-V</code> switch. Default value of this real number is 0.8 times the height of uppercase glyphs.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-e</code><i>&nbsp;extension-factor</i></p>
<dd> The extension factor to stretch the characters horizontally. Default value of this real number is 1.0; if less than 1.0, you get a condensed font.</p>
<dt><code>-E</code><i>&nbsp;encoding-id</i></p>
<dd> The TrueType encoding ID. Default value of this non-negative integer is 1.</p>
<dt>
<dd> Will be ignored if <code>-N</code> is used.</p>
<dt><code>-f</code><i>&nbsp;font-index</i></p>
<dd> The font index in a TrueType Collection. Default is the first font (index 0). [TrueType collections are usually found in some CJK fonts; e.g. the first font index specifies glyphs and metrics for horizontal writing, and the second font index does the same for vertical writing. TrueType collections usually have the extension `</p>
<dt>
<dd> Will be ignored for ordinary TrueType fonts.</p>
<dt><code>-l</code></p>
<dd> Create ligatures in subfonts between first and second bytes of all the original character codes. Example: Character code 0xABCD maps to character position 123 in subfont 45. Then a ligature in subfont 45 between position 0xAB and 0xCD pointing to character 123 will be produced. The fonts of the Korean HLaTeX package use this feature. Note that this option generates correct ligatures only for TrueType fonts where the input cmap is identical to the output encoding. In case of HLaTeX, TTFs must have platform ID 3 and encoding ID 5.</p>
<dt>
<dd> Will be ignored if not in subfont mode.</p>
<dt><code>-L</code><i>&nbsp;ligature-file</i></p>
<dd> Same as <code>-l</code>, but character codes for ligatures are specified in <i>ligature-file</i>. For example, ` generates correct ligatures for the Korean HLaTeX package regardless of the platform and encoding ID of the used TrueType font (the file is part of the ttf2pk package).</p>
<dt>
<dd> Ligature files have the same format and extension as files. This option will be ignored if not in subfont mode.</p>
<dt><code>-n</code></p>
<dd> Use PS names (of glyphs) of the TrueType font. Only glyphs with a valid entry in the selected cmap are used.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-N</code></p>
<dd> Use only PS names of the TrueType font. No cmap is used, thus the switches <code>-E</code> and <code>-P</code> have no effect, causing a warning message.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-O</code></p>
<dd> Use octal values for all character codes in the file rather than names; this is useful for symbol or CJK fonts where character names such as `A&#8217; are meaningless.</p>
<dt><code>-p</code><i>&nbsp;inencfile</i></p>
<dd> The input encoding file name for the TTF&rarr;raw TeX mapping. This parameter has to be specified in a map file (default: recorded in for successive <code>ttf2pk</code> calls.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-P</code><i>&nbsp;platform-id</i></p>
<dd> The TrueType platform ID. Default value of this non-negative integer is 3.</p>
<dt>
<dd> Will be ignored if <code>-N</code> is used.</p>
<dt><code>-q</code></p>
<dd> Make <code>ttf2tfm</code> quiet. It suppresses any informational output except warning and error messages. For CJK fonts, the output can get quite large if you don&#8217;t specify this switch.</p>
<dt><code>-r</code><i>&nbsp;old-glyphname new-glyphname</i></p>
<dd> Replaces <i>old-glyphname</i> with <i>new-glyphname</i>. This switch is useful if you want to give an unnamed glyph (i.e., a glyph which can be represented with `.gXXX&#8217; or `.cXXX&#8217; only) a name or if you want to rename an already existing glyph name. You can&#8217;t use the `.gXXX&#8217; or `.cXXX&#8217; glyph name constructs for <i>new-glyphname</i>; multiple occurrences of <code>-r</code> are possible.</p>
<dt>
<dd> If in subfont mode or if no encoding file is specified, this switch is ignored.</p>
<dt><code>-R</code><i>&nbsp;replacement-file</i></p>
<dd> Use this switch if you have many replacement pairs; they can be collected in a file which should have ` as extension. The syntax used in such replacement files is simple: Each non-empty line must contain a pair `<i>old-glyphname new-glyphname</i>&#8216; separated by whitespace (without the quotation marks). A percent sign starts a line comment; you can continue a line on the next line with a backslash as the last character.</p>
<dt>
<dd> If in subfont mode or if no encoding file is specified, this switch is ignored.</p>
<dt><code>-s</code><i>&nbsp;slant-factor</i></p>
<dd> The obliqueness factor to slant the font, usually much smaller than 1. Default of this real number is 0.0; if the value is larger than zero, the characters slope to the right, otherwise to the left.</p>
<dt><code>-t</code><i>&nbsp;outencfile</i></p>
<dd> The output encoding file name for the virtual font(s). Only characters in the raw TeX font are used.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-T</code><i>&nbsp;inoutencfile</i></p>
<dd> This is equivalent to `<code>-p</code> <i>inoutencfile</i> <code>-t</code> <i>inoutencfile</i>&#8216;.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-u</code></p>
<dd> Use only those characters specified in the output encoding, and no others. By default, <code>ttf2tfm</code> tries to include all characters in the virtual font, even those not present in the encoding for the virtual font (it puts them into otherwise-unused positions, rather arbitrarily).</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-v</code><i>&nbsp;vplfile</i></p>
<dd> Output a file in addition to the file. If no output encoding file is specified, <code>ttf2tfm</code> uses a default font encoding (cmtt10). <code>Note:</code> Be careful to use different names for the virtual font and the raw font!</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-V</code><i>&nbsp;scvplfile</i></p>
<dd> Same as <code>-v</code>, but the virtual font generated is a pseudo small caps font obtained by scaling uppercase letters by 0.8 (resp. the value specified with <code>-c</code>) to typeset lowercase. This font handles accented letters and retains proper kerning.</p>
<dt>
<dd> Will be ignored in subfont mode.</p>
<dt><code>-w</code></p>
<dd> Generate PostScript encoding vectors containing glyph indices, primarily used to embed TrueType fonts in pdfTeX. <code>ttf2tfm</code> takes the names and replaces the suffix with that is, for files it creates at the same place.</p>
<dt>
<dd> Will be ignored if not in subfont mode.</p>
<dt><code>-x</code></p>
<dd> Rotate all glyphs by 90 degrees counter-clockwise. If no <code>-y</code> parameter is given, the rotated glyphs are shifted down vertically by 0.25em.</p>
<dt>
<dd> Will be ignored if not in subfont mode.</p>
<dt><code>-y</code><i>&nbsp;vertical-shift-factor</i></p>
<dd> Shift down rotated glyphs by the given amount (the unit is <i>em</i>).</p>
<dt>
<dd> Ignored if not in subfont mode or glyphs are not rotated.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the current version of <code>ttf2tfm</code> and the used file search library (e.g. <code>kpathsea</code>).</p>
<dt><code>&#8211;help</code></p>
<dd> Shows usage information.</dl>
<p> If no file name is given, the name of the file is used, including the full path and replacing the extension with `</p>
<h2>CMAPS</h2>
<p> Contrary to Type 1 PostScript fonts (but similar to the new CID PostScript font format), most TrueType fonts have more than one native mapping table, also called `cmap&#8217;, which maps the (internal) TTF glyph indices to the (external) TTF character codes. Common examples are a mapping table to Unicode encoded character positions, and the standard Macintosh mapping. </p>
<p> To specify a TrueType mapping table, use the options <code>-P</code> and <code>-E</code>. With <code>-P</code> you specify the platform ID; defined values are: </p>
<table>
<tr VALIGN=top>
<td><i>platform</i></td>
<td><i>platform ID (pid)</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Apple Unicode</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>Macintosh</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>ISO </td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>Microsoft</td>
<td>3
</td>
</tr>
</table>
<p> The encoding ID depends on the platform. For pid=0, we ignore the <code>-E</code> parameter (setting it to zero) since the mapping table is always Unicode version 2.0. For pid=1, the following table lists the defined values: </p>
<dl>
<dt>
<dd> platform ID = 1</dl>
<table>
<tr VALIGN=top>
<td><i>script</i></td>
<td><i>encoding ID (eid)</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Roman </td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>Japanese</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>Chinese </td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>Korean </td>
<td>3
</td>
</tr>
<tr VALIGN=top>
<td>Arabic </td>
<td>4
</td>
</tr>
<tr VALIGN=top>
<td>Hebrew </td>
<td>5
</td>
</tr>
<tr VALIGN=top>
<td>Greek </td>
<td>6
</td>
</tr>
<tr VALIGN=top>
<td>Russian </td>
<td>7
</td>
</tr>
<tr VALIGN=top>
<td>Roman Symbol</td>
<td>8
</td>
</tr>
<tr VALIGN=top>
<td>Devanagari</td>
<td>9
</td>
</tr>
<tr VALIGN=top>
<td>Gurmukhi</td>
<td>10
</td>
</tr>
<tr VALIGN=top>
<td>Gujarati</td>
<td>11
</td>
</tr>
<tr VALIGN=top>
<td>Oriya </td>
<td>12
</td>
</tr>
<tr VALIGN=top>
<td>Bengali </td>
<td>13
</td>
</tr>
<tr VALIGN=top>
<td>Tamil </td>
<td>14
</td>
</tr>
<tr VALIGN=top>
<td>Telugu </td>
<td>15
</td>
</tr>
<tr VALIGN=top>
<td>Kannada </td>
<td>16
</td>
</tr>
<tr VALIGN=top>
<td>Malayalam</td>
<td>17
</td>
</tr>
<tr VALIGN=top>
<td>Sinhalese</td>
<td>18
</td>
</tr>
<tr VALIGN=top>
<td>Burmese </td>
<td>19
</td>
</tr>
<tr VALIGN=top>
<td>Khmer </td>
<td>20
</td>
</tr>
<tr VALIGN=top>
<td>Thai </td>
<td>21
</td>
</tr>
<tr VALIGN=top>
<td>Laotian </td>
<td>22
</td>
</tr>
<tr VALIGN=top>
<td>Georgian</td>
<td>23
</td>
</tr>
<tr VALIGN=top>
<td>Armenian</td>
<td>24
</td>
</tr>
<tr VALIGN=top>
<td>Maldivian</td>
<td>25
</td>
</tr>
<tr VALIGN=top>
<td>Tibetan </td>
<td>26
</td>
</tr>
<tr VALIGN=top>
<td>Mongolian</td>
<td>27
</td>
</tr>
<tr VALIGN=top>
<td>Geez </td>
<td>28
</td>
</tr>
<tr VALIGN=top>
<td>Slavic </td>
<td>29
</td>
</tr>
<tr VALIGN=top>
<td>Vietnamese</td>
<td>30
</td>
</tr>
<tr VALIGN=top>
<td>Sindhi </td>
<td>31
</td>
</tr>
<tr VALIGN=top>
<td>Uninterpreted</td>
<td>32
</td>
</tr>
</table>
<p> Here are the ISO encoding IDs: </p>
<dl>
<dt>
<dd> platform ID = 2</dl>
<table>
<tr VALIGN=top>
<td><i>encoding</i></td>
<td><i>encoding ID (eid)</i>
</td>
</tr>
<tr VALIGN=top>
<td>ASCII </td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>ISO 10646</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>ISO 8859-1</td>
<td>2
</td>
</tr>
</table>
<p> And finally, the Microsoft encoding IDs: </p>
<dl>
<dt>
<dd> platform ID = 3</dl>
<table>
<tr VALIGN=top>
<td><i>encoding</i></td>
<td><i>encoding ID (eid)</i>
</td>
</tr>
<tr VALIGN=top>
<td>Symbol </td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>Unicode 2.0 </td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>Shift JIS </td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>GB 2312 (1980) </td>
<td>3
</td>
</tr>
<tr VALIGN=top>
<td>Big 5 </td>
<td>4
</td>
</tr>
<tr VALIGN=top>
<td>KS X 1001 (Wansung)</td>
<td>5
</td>
</tr>
<tr VALIGN=top>
<td>KS X 1001 (Johab)</td>
<td>6
</td>
</tr>
<tr VALIGN=top>
<td>UCS-4 </td>
<td>10
</td>
</tr>
</table>
<p> The program will abort if you specify an invalid platform/encoding ID pair. It will then show the possible pid/eid pairs. Please note that most fonts have at most two or three cmaps, usually corresponding to the pid/eid pairs (1,0), (3,0), or (3,1) in case of Latin based fonts. Valid Microsoft fonts should have a (3,1) mapping table, but some fonts exist (mostly Asian fonts) which have a (3,1) cmap not encoded in Unicode. The reason for this strange behavior is the fact that some old MS Windows versions will reject fonts having a non-(3,1) cmap (since all non-Unicode Microsoft encoding IDs are for Asian MS Windows versions). </p>
<p> The <code>-P</code> and <code>-E</code> options of <code>ttf2tfm</code> must be equally specified for <code>ttf2pk</code>; the corresponding parameters in a map file are `Pid&#8217; and `Eid&#8217;, respectively. </p>
<p> The default pid/eid pair is (3,1). </p>
<p> Similarly, an <code>-f</code> option must be specified as `Fontindex&#8217; parameter in a map file. </p>
<p> If you use the <code>-N</code> switch, all cmaps are ignored, using only the PostScript names in the TrueType font. The corresponding option in a map file is `PS=Only&#8217;. If you use the <code>-n</code> switch, the default glyph names built into <code>ttf2tfm</code> are replaced with the PS glyph names found in the font. In many cases this is not what you want because the glyph names in the font are often incorrect or non-standard. The corresponding option in a map file is `PS=Yes&#8217;. </p>
<p> Single replacement glyph names specified with <code>-r</code> must be given directly as `<i>old-glyphname new-glyphname</i>&#8216; in a map file; <code>-R</code> is equivalent to the `Replacement&#8217; option.</p>
<h2>INPUT AND OUTPUT ENCODINGS</h2>
<p> You must specify the encoding vectors from the TrueType font to the raw TeX font and from the raw TeX font to the virtual TeX font exactly as with <code>afm2tfm</code>, but you have more possibilities to address the character codes. [With `encoding vector&#8217; a mapping table with 256 entries in form of a PostScript vector is meant; see the file of this package for an example.] With <code>afm2tfm</code>, you must access each glyph with its Adobe glyph name, e.g.&nbsp;`/quotedsingle&#8217; or `/Acircumflex&#8217;. This has been extended with <code>ttf2tfm</code>; now you can (and sometimes must) access the code points and/or glyphs directly, using the following syntax for specifying the character position in decimal, octal, or hexadecimal notation: `/.c<i>&lt;decimal-number&gt;</i>&#8216;, `/.c0<i>&lt;octal-number&gt;</i>&#8216;, or `/.c0x<i>&lt;hexadecimal-number&gt;</i>&#8216;. Examples: `/.c72&#8242;, `/.c0646&#8242;, `/.c0x48&#8242;. To access a glyph index directly, use the character `g&#8217; instead of `c&#8217; in the just introduced notation. Example: `/.g0x32&#8242;. [Note: The `.cXXX&#8217; notation makes no sense if <code>-N</code> is used.] </p>
<p> For pid/eid pairs (1,0) and (3,1), both <code>ttf2tfm</code> and <code>ttf2pk</code> recognize built-in default Adobe glyph names; the former follows the names given in Appendix E of the book `Inside Macintosh&#8217;, volume 6, the latter uses the names given in the TrueType Specification (WGL4, a Unicode subset). Note that Adobe names for a given glyph are often not unique and do sometimes differ, e.g., many PS fonts have the glyph `mu&#8217;, whereas this glyph is called `mu1&#8242; in the WGL4 character set to distinguish it from the real Greek letter mu. Be also aware that OpenType (i.e. TrueType 2.0) fonts use an updated WGL4 table; we use the data from the latest published TrueType specification (1.66). You can find those mapping tables in the source code file </p>
<p> On the other hand, the switches <code>-n</code> and <code>-N</code> makes <code>ttf2tfm</code> read in and use the PostScript names in the TrueType font itself (stored in the `post&#8217; table) instead of the default Adobe glyph names. </p>
<p> Use the <code>-r</code> switch to remap single glyph names and <code>-R</code> to specify a file containing replacement glyph name pairs. </p>
<p> If you don&#8217;t select an input encoding, the first 256 glyphs of the TrueType font with a valid entry in the selected cmap will be mapped to the TeX raw font (without the <code>-q</code> option, <code>ttf2tfm</code> prints this mapping table to standard output), followed by all glyphs not yet addressed in the selected cmap. However, some code points for the (1,0) pid/eid pair are omitted since they do not represent glyphs useful for TeX: 0x00 (null), 0x08 (backspace), 0x09 (horizontal tabulation), 0x0d (carriage return), and 0x1d (group separator). The `invalid character&#8217; with glyph index 0 will be omitted too. </p>
<p> If you select the <code>-N</code> switch, the first 256 glyphs of the TrueType font with a valid PostScript name will be used in case no input encoding is specified. Again, some glyphs are omitted: `.notdef&#8217;, `.null&#8217;, and `nonmarkingreturn&#8217;. </p>
<p> If you don&#8217;t select an output encoding, <code>ttf2tfm</code> uses the same mapping table as <code>afm2tfm</code> would use (you can find it in the source code file it corresponds to TeX typewriter text. Unused positions (either caused by empty code points in the mapping table or missing glyphs in the TrueType font) will be filled (rather arbitrarily) with characters present in the input encoding but not specified in the output encoding (without the <code>-q</code> option <code>ttf2tfm</code> prints the final output encoding to standard output). Use the <code>-u</code> option if you want only glyphs in the virtual font which are defined in the output encoding file, and nothing more. </p>
<p> One feature missing in <code>afm2tfm</code> has been added which is needed by LaTeX&#8217;s T1 encoding: <code>ttf2tfm</code> will construct the glyph `Germandbls&#8217; (by simply concatenating two `S&#8217; glyphs) even for normal fonts if possible. It appears in the glyph list as the last item, marked with an asterisk. Since this isn&#8217;t a real glyph it will be available only in the virtual font. </p>
<p> For both input and output encoding, an empty code position is represented by the glyph name `/.notdef&#8217;. </p>
<p> In encoding files, you can use `\&#8217; as the final character of a line to indicate that the input is continued on the next line. The backslash and the following newline character will be removed. </p>
<h2>SUBFONT DEFINITION FILES</h2>
<p> CJKV (Chinese/Japanese/Korean/old Vietnamese) fonts usually contain several thousand glyphs; to use them with TeX it is necessary to split such large fonts into subfonts. Subfont definition files (usually having the extension ` are a simple means to do this smoothly. </p>
<p> A subfont file name usually consists of a prefix, a subfont infix, and a postfix (which is empty in most cases), e.g. </p>
<p> ntukai23 &rarr; prefix: ntukai, infix: 23, postfix: (empty) </p>
<p> Here the syntax of a line in an file, describing one subfont:</p>
<dl>
<dt><i>&lt;whitespace&gt; &lt;infix&gt; &lt;whitespace&gt; &lt;ranges&gt; &lt;whitespace&gt;</i></p>
<dd>
<dt><i>&lt;infix&gt;</i>&nbsp;:=</p>
<dd> anything except whitespace. It is best to use only alphanumerical characters.</p>
<dt><i>&lt;whitespace&gt;</i>&nbsp;:=</p>
<dd> space, formfeed, carriage return, horizontal and vertical tabs &#8212; no newline characters.</p>
<dt><i>&lt;ranges&gt;</i>&nbsp;:=</p>
<dd> <i>&lt;ranges&gt; &lt;whitespace&gt; &lt;codepoint&gt;</i>&nbsp;|<br />
 <i>&lt;ranges&gt; &lt;whitespace&gt; &lt;range&gt;</i>&nbsp;|<br />
 <i>&lt;ranges&gt; &lt;whitespace&gt; &lt;offset&gt; &lt;whitespace&gt; &lt;range&gt;</i></p>
<dt><i>&lt;codepoint&gt;</i>&nbsp;:=</p>
<dd> <i>&lt;number&gt;</i> </p>
<dt><i>&lt;range&gt;</i>&nbsp;:=</p>
<dd> <i>&lt;number&gt;</i>&nbsp;`_&#8217;<i>&nbsp;&lt;number&gt;</i> </p>
<dt><i>&lt;offset&gt;</i>&nbsp;:=</p>
<dd> <i>&lt;number&gt;</i>&nbsp;`:&#8217;</p>
<dt><i>&lt;number&gt;</i>&nbsp;:=</p>
<dd> hexadecimal (prefix `0x&#8217;), decimal, or octal (prefix `0&#8242;)</dl>
<p> A line can be continued on the next line with a backslash ending the line. The ranges must not overlap; offsets have to be in the range 0-255. </p>
<p> Example: </p>
<p> The line </p>
<p> assigns to the code positions 10, 11, 12, and 13 of the subfont having the infix `03&#8242; the character codes 0x2349, 0x2345, 0x2346, and 0x2347 respectively. </p>
<p> The files in the distribution are customized for the CJK package for LaTeX. </p>
<p> You have to embed the file name into the font name (at the place where the infix will appear) surrounded by two `@&#8217; signs, on the command line resp. a map file; both <code>ttf2tfm</code> and <code>ttf2pk</code> switch then to subfont mode. </p>
<p> It is possible to use more than a single file by separating them with commata and no whitespace; for a given subfont, the first file is scanned for an entry, then the next file, and so on. Later entries override entries found earlier (possibly only partially). For example, the first file sets up range 0x10-0xA0, and the next one modifies entries 0x12 and 0x25. As can be easily seen, this algorithm allows for adding and replacing, but not for removing entries. </p>
<p> Subfont mode disables the options <code>-n</code>, <code>-N</code>, <code>-p</code>, <code>-r</code>, <code>-R</code>, <code>-t</code>, <code>-T</code>, <code>-u</code>, <code>-v</code>, <code>-V</code> and <code>-w</code> for <code>ttf2tfm</code>; similarly, no `Encoding&#8217; or `Replacement&#8217; parameter is allowed in a map file. Single replacement glyph names are ignored too. </p>
<p> <code>ttf2tfm</code> will create all subfont files specified in the files (provided the subfont contains glyphs) in one run. </p>
<p> Example: </p>
<p> The call </p>
<p> will use and producing <i>all</i> subfont files etc.</p>
<h2>RETURN VALUE</h2>
<p> ttf2tfm returns 0 on success and 1 on error; warning and error messages are written to standard error.</p>
<h2>SOME NOTES ON FILE SEARCHING</h2>
<p> Both <code>ttf2pk</code> and <code>ttf2tfm</code> use either the <code>kpathsea</code>, <code>emtexdir</code>, or <code>MiKTeX</code> library for searching files (<code>emtexdir</code> will work only on operating systems which have an MS-DOSish background, i.e. MS-DOS, OS/2, Windows; <code>MikTeX</code> is specific to MS Windows). </p>
<p> As a last resort, both programs can be compiled without a search library; the searched files must be then in the current directory or specified with a path. Default extensions will be appended also (with the exception that only ` is appended and not `</p>
<h3>kpathsea</h3>
<p> The actual version of kpathsea is displayed on screen if you call either <code>ttf2pk</code> or <code>ttf2tfm</code> with the <code>&#8211;version</code> command line switch. </p>
<p> Here is a table of the file type and the corresponding <code>kpathsea</code> variables. and are program specific environment variables introduced in <code>kpathsea</code> version 3.2: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>.ttf and .ttc</td>
<td>TTFONTS
</td>
</tr>
<tr VALIGN=top>
<td>ttf2pk.cfg </td>
<td>TTF2PKINPUTS
</td>
</tr>
<tr VALIGN=top>
<td>.map </td>
<td>TTF2PKINPUTS
</td>
</tr>
<tr VALIGN=top>
<td>.enc </td>
<td>TTF2PKINPUTS, TTF2TFMINPUTS
</td>
</tr>
<tr VALIGN=top>
<td>.rpl </td>
<td>TTF2PKINPUTS, TTF2TFMINPUTS
</td>
</tr>
<tr VALIGN=top>
<td>.tfm </td>
<td>TFMFONTS
</td>
</tr>
<tr VALIGN=top>
<td>.sfd </td>
<td>TTF2PKINPUTS, TTF2TFMINPUTS
</td>
</tr>
</table>
</dl>
<p> Please consult the info files of <code>kpathsea</code> for details on these variables. </p>
<p> You should set the variable to the directory where your configuration file resides. </p>
<p> Here is the proper command to find out to which value a <code>kpathsea</code> variable is set (we use as an example). This is especially useful if a variable isn&#8217;t set in or in the environment, thus pointing to the default value which is hard-coded into the <code>kpathsea</code> library. </p>
<dl>
<dt>
<dd></dl>
<p> We select the program name also since it is possible to specify variables which are searched only for a certain program &#8212; in our example it would be </p>
<p> A similar but not identical method is to say </p>
<p> [A full list of format types can be obtained by saying ` on the command line prompt.] This is exactly how <code>ttf2tfm</code> (and <code>ttf2pk</code>) searches for files; the disadvantage is that all variables are expanded which can cause very long strings.</p>
<h3>emtexdir</h3>
<p> Here the list of suffixes and their related environment variables to be set in (resp. in for OS/2): </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>.ttf and .ttc</td>
<td>TTFONTS
</td>
</tr>
<tr VALIGN=top>
<td>ttf2pk.cfg</td>
<td>TTFCFG
</td>
</tr>
<tr VALIGN=top>
<td>.map </td>
<td>TTFCFG
</td>
</tr>
<tr VALIGN=top>
<td>.enc </td>
<td>TTFCFG
</td>
</tr>
<tr VALIGN=top>
<td>.rpl </td>
<td>TTFCFG
</td>
</tr>
<tr VALIGN=top>
<td>.tfm </td>
<td>TEXTFM
</td>
</tr>
<tr VALIGN=top>
<td>.sfd </td>
<td>TTFCFG
</td>
</tr>
</table>
</dl>
<p> If one of the variables isn&#8217;t set, a warning message is emitted. The current directory will always be searched. As usual, one exclamation mark appended to a directory path causes subdirectories one level deep to be searched, two exclamation marks cause all subdirectories to be searched. Example: </p>
<p> Constructions like ` aren&#8217;t possible.</p>
<h3>MiKTeX</h3>
<p> Both <code>ttf2tfm</code> and <code>ttf2pk</code> have been fully integrated into <code>MiKTeX</code>. Please refer to the documentation of <code>MiKTeX</code> for more details on file searching.</p>
<h2>PROBLEMS</h2>
<p> Many <code>vptovf</code> implementations allow only 100 bytes for the header (the limit is 1024 in the file format itself): 8 bytes for checksum and design size, 40 bytes for the family name, 20 bytes for the encoding, and 4 bytes for a face byte. There remain only 28 bytes for some additional information which is used by <code>ttf2tfm</code> for an identification string (which is essentially a copy of the command line), and this limit is always exceeded. </p>
<p> The optimal solution is to increase the value of <i>max_header_bytes</i> in the file (and probably too) to, say, 400 and recompile <code>vptovf</code> (and <code>pltotf</code>). Otherwise you&#8217;ll get some (harmless) error messages like </p>
<p> which can be safely ignored.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ttf2pk/">ttf2pk</a></code>(1), <code><a href="/docs/linux/man/1-afm2tfm/">afm2tfm</a></code>(1), <code><a href="/docs/linux/man/1-vptovf/">vptovf</a></code>(1),<br />
 the info pages for <code>dvips</code> and <code>kpathsea</code></p>
<h2>AVAILABILITY</h2>
<p> <code>ttf2tfm</code> is part of the FreeType 1 package, a high quality TrueType rendering library.</p>
<h2>AUTHORS</h2>
<p> Werner LEMBERG<br />
 Fr&eacute;d&eacute;ric LOYER </p>
<h2>Index</h2>
