---

title: "afm2pl(1)"
name: "afm2pl"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afm2pl/"
description: "afm2pl – convert AFM font metrics to TeX pl font metrics"
---

<p> afm2pl - convert AFM font metrics to TeX pl font metrics </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>afm2pl</code> [<code>-p</code>&nbsp;<i>encoding_file</i>] [<code>-o</code>] [<code>-e</code>&nbsp;<i>extension_factor</i>] [<code>-s</code>&nbsp;<i>slant_factor</i>] [<code>-f</code>&nbsp;<i>font_dimensions</i>] [<code>-k</code>] [<code>-m</code>&nbsp;<i>letter_spacing</i>] [<code>-l</code>&nbsp;<i>ligkern_spec</i>] [<code>-L</code>&nbsp;<i>ligkern_spec</i>] [<code>-n</code>] <i>input_file[.afm]</i> [<i>output_file[.pl]</i>] </dt>
<dt><code>afm2pl</code> [--help] | [--version] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> afm2pl converts an afm (Adobe Font Metric) file into a pl (Property List) file, which in its turn can be converted to a tfm (TeX Font Metric) file. It normally preserves kerns and ligatures, but also offers additional control over them. </p>
<p> afm2pl is meant to be a partial replacement for afm2tfm, on which it is based. With afm2tfm, preserving kerns and ligatures is possible only in a roundabout way, and handling of them is hard-wired. </p>
<p> For text fonts, Y&amp;Y&#8217;s texnansi is a good encoding to be used with afm2pl. Its character set includes all the accented characters likely to be needed for Western languages, plus many typographic symbols, without a need for either virtual fonts or a separate text companion font. </p>
<p> Full LaTeX support for this encoding is available in the form of the texnansi package, which is already part of TeX Live and teTeX. These distributions also contain the encoding file texnansi.enc. </p>
<p> The distribution contains uppercased and lowercased versions of texnansi, viz. texnanuc and texnanlc, to allow font-based rather than macro-based uppercasing and lowercasing, and the familiar old ot1 encoding plus some variations in PostScript .enc format (I included these because they seem to be absent from teTeX/TeX Live). However, check your mapfiles if you have old afm2pl-generated fonts using these. </p>
<p> Return value: 0 if no error; a negative number indicating the number of missing glyphs if conversion was otherwise successfull but glyphs are missing, and 1 in case of error.  </p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>encoding_file</i> </p>
 </dd>
<dl>
<dd> <p> The default is the encoding specified in the afm file, which had better match the encoding in the fontfile (pfa or pfb). If afm2pl-name.enc exists, afm2pl will use this file instead of name.enc, unless an option -n is given. The generated mapfile entry (see below) instructs pdftex or the dvi driver to reencode the font on the fly. On-the-fly reencoding does not require virtual fonts. </p>
 </dd></dl>
<p> <code>-o</code> </p>
<dl>
<dd> <p> Use octal for all character codes in the pl file. </p>
 </dd></dl>
<p> <code>-e</code> <i>extend_factor</i> </p>
<dl>
<dd> <p> Widen or narrow characters by <i>extend_factor</i>. Default is 1.0 (natural width). Not recommended[1]. </p>
 </dd></dl>
<p> <code>-s</code> <i>slant_factor</i> </p>
<dl>
<dd> <p> Oblique (slant) characters by <i>slant_factor</i>. Not recommended either. </p>
 </dd></dl>
<p> <code>-f</code> <i>font_dimensions</i> </p>
<dl>
<dd> <p> The value is either the keyword afm2tfm or a comma-separated list of up to five integers. The parameters are listed below, with their defaults and their value when the afm2tfm keyword is specified. &#8216;Space&#8217; means the width of a space in the target font, except of course in the last row. Keep in mind that the design size is 1000, and that all numbers must be nonnegative integers. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Font dimension </code></td>
<td><code> Default value </code></td>
<td><code> Afm2tfm value </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>stretch</i> </td>
<td> space div 2 </td>
<td> 300 &#215; <i>extend_factor</i> 
</td>
</tr>
<tr VALIGN=top>
<td> <i>shrink</i> </td>
<td> space div 3 </td>
<td> 100 &#215; <i>extend_factor</i> 
</td>
</tr>
<tr VALIGN=top>
<td> <i>extra space</i> </td>
<td> space div 3 </td>
<td> missing 
</td>
</tr>
<tr VALIGN=top>
<td> <i>quad</i> </td>
<td> 2 &#215; width of &#8216;0&#8217; </td>
<td> 1000 &#215; <i>extend_factor</i> 
</td>
</tr>
<tr VALIGN=top>
<td> <i>space</i> </td>
<td> (space source font) &#215; <i>extend_factor</i> </td>
<td> (space source font) &#215; <i>extend_factor</i> 
</td>
</tr>
</table>
<p> For fixed-pitch fonts, different values apply: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Font dimension </code></td>
<td><code> Default value </code></td>
<td><code> Afm2tfm value </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>stretch</i> </td>
<td> 0 </td>
<td> 0 
</td>
</tr>
<tr VALIGN=top>
<td> <i>shrink</i> </td>
<td> 0 </td>
<td> 0 
</td>
</tr>
<tr VALIGN=top>
<td> <i>extra space</i> </td>
<td> space </td>
<td> missing 
</td>
</tr>
<tr VALIGN=top>
<td> <i>quad</i> </td>
<td> 2 &#215; character width </td>
<td> 1000 &#215; <i>extend_factor</i> 
</td>
</tr>
<tr VALIGN=top>
<td> <i>space</i> </td>
<td> character width </td>
<td> character width 
</td>
</tr>
</table>
<p> Specify just a non-default stretch and shrink with e.g. 150,70 and just a non-default extra space with ,,10. </p>
 </dd></dl>
<p> <code>-k</code> </p>
<dl>
<dd> <p> Keep original ligatures. This option only has effect in combination with positive letterspacing; see the section on letterspacing and extra ligkern info. </p>
 </dd></dl>
<p> <code>-m</code> <i>letter_spacing</i> </p>
<dl>
<dd> <p> Letterspace by <i>letter_spacing</i>/1000 em (integer). This is useful for making all-caps typesetting look better. Try a value of e.g. 50 or 100. But see the section on letterspacing and extra ligkern info for details. A better alternative, though, is letting pdftex do the letterspacing. The microtype package gives LaTeX users access to this feature. </p>
 </dd></dl>
<p> <code>-l</code> <i>ligkern_spec</i>, <code>-L</code> <i>ligkern_spec</i> </p>
<dl>
<dd> <p> See the section on extra ligkern info for details. </p>
 </dd></dl>
<p> <code>-n</code> </p>
<dl>
<dd> <p> No prefix. For .enc- and .lig files, the program normally first prefixes the name with `afm2pl-&#8216;. Only if the prefixed filename is not found, will it search for the original filename. This option prevents searching for the prefixed filename. </p>
 </dd></dl>
<p> <code>-V</code> </p>
<dl>
<dd> <p> Verbose. If turned on, it reports the number of missing glyphs to stderr and their names to stdout. </p>
 </dd></dl>
<p> <code>--help</code> </p>
<dl>
<dd> <p> Display a short usage message. </p>
 </dd></dl>
<p> <code>--version</code> </p>
<dl>
<dd> <p> Display the version number of afm2pl. </p>
 </dd></dl>
<h2>MAPFILE ENTRIES</h2>
<p> afm2pl writes a mapfile entry to a file with the same basename as the pl output file, but with extension .map. It can be used for the dvips mapfile and for the pdftex mapfile. It is assumed that the pfb file has the same basename as the afm file and must be downloaded. <i>You may have to hand-edit this entry.</i> </p>
<p> You can configure dvips and pdftex to read this additional mapfile or otherwise add the entry to an existing mapfile. </p>
<p> <code>Check your mapfiles!</code> To reduce the likelihood of name conflicts, the .enc- files which are part of afm2pl (ot1, ot1csc, ot1ital, ot1tt, texnanlc and texnanuc) have now been prepended with afm2pl-. The .enc files are referenced in mapfiles. If you have old afm2pl-generated .tfm files using these, then you should update their mapfile fragments and rerun updmap or updmap-sys. Or you can copy the relevant enc files to your personal or local texmf tree under their previous non-prefixed names.  </p>
<h2>EXTRA LIGKERN INFO</h2>
<p> <i>Most users are well-advised to leave this mess alone and to accept the default behavior.</i> </p>
<p> The ligatures and kerns present in the afm file can be modified in various ways. Default, the encoding file is scanned for extra ligkern specifications, whose format will be described below. If there are no ligkern specifications in the encoding file, then extra ligkern specifications will be read from a file [afm2pl-]default.lig. A value of 0 for <i>ligkern_spec</i> means that the ligatures and kerns from the afm file won&#8217;t be tampered with and a value of 1 specifies default behavior. One can also specify a comma-separated list of files with extra ligkerns specs. </p>
<p> If afm2pl is compiled with the kpathsea library, then these files will be searched for under $TEXMF/fonts/lig. </p>
<p> <i>Note that ligatures and kerns are hints for the typesetting application; there is no need to download this information to the printer or to make it available to a dvi driver.</i> </p>
<p> The parser for ligkern info has been inherited from afm2tfm virtually without change. A ligkern specification can have one of the following forms: </p>
<dl>
<dd> <pre><code>
 glyph_name1  glyph_name2  lig_op  glyph_name3  ;
</code></pre>
 </dd></dl>
<p> This specifies a ligature. Possible values for <i>lig_op</i> are =:, |=:, |=:&gt;, =:|, =:|&gt;, |=:|, |=:|&gt; and |=:|&gt;&gt;. These correspond to LIG, /LIG, /LIG&gt;, LIG/, LIG/&gt;, /LIG/, /LIG/&gt;, /LIG/&gt;&gt; in .pl syntax; see the pltotf documentation and the .lig files in the distribution. </p>
<dl>
<dd> <pre><code>
 glyph_name1  &lt;&gt; glyph_name2  ;
</code></pre>
 </dd></dl>
<p> Kern <i>glyph_name1</i> as <i>glyph_name2</i>. </p>
<dl>
<dd> <pre><code>
 glyph_name1  {} glyph_name2  ;
</code></pre>
 </dd></dl>
<p> Remove the kern between <i>glyph_name1</i> and <i>glyph_name2</i>. A value of * for either glyph name is interpreted as a wildcard. </p>
<dl>
<dd> <pre><code>|| = glyph  ;
</code></pre>
 </dd></dl>
<p> Set the (right) boundary character to <i>glyph</i>. <i>glyph</i> may be either a glyphname or a slot in the encoding vector. Choosing a glyph which doesn&#8217;t occur in the output encoding is equivalent to not specifying a boundarychar at all. It is ok to pick an encoded glyphname which does not occur in the afm. In fact, this is what default.lig does: || = cwm ;. </p>
<p> You can copy the kerns of an unencoded character to the boundarychar. Below, space is the unencoded character: </p>
<dl>
<dd> <pre><code>|| &lt;&gt; space ;
</code></pre>
 </dd></dl>
<p> This ligkern specification should occur before the one that deletes space kerns. </p>
<p> A ligkern specification should be contained within one line. One line may contain several ligkern specifications, separated by spaces. Note that ; (space followed by semicolon) is considered part of the ligkern specification. See the lig files included in this distribution. Example: </p>
<dl>
<dd> <pre><code>one {} * ; * {} one ; two {} * ; * {} two ;
</code></pre>
 </dd></dl>
<p> Lines with ligkern specifications inside an encoding file should start with % LIGKERN. Ligkern specifications in a lig file may optionally start this way.  </p>
<h2>LETTERSPACING AND EXTRA LIGKERN INFO</h2>
<p> Letterspacing has various side-effects for ligkern info. Instead of simply applying the extra ligkern info (see previous section), the following is done: </p>
<dl>
<dt>1.</dt>
<dd> <p> In case of positive letterspacing, native ligatures are removed, unless the -k option is specified. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Extra ligkern info is applied as usual, except that in case of positive letterspacing different defaults apply: -l 0 is quietly ignored, ligkern comments in the encoding file are ignored, and defpre.lig is read instead of default.lig. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Letterspacing is applied. This adds a lot of kerns, and modifies existing kerns. </p>
 </dd>
<dt>4.</dt>
<dd> <p> The extra ligkern info specified with -L is applied. The only ligkern specs which are allowed here, are removals of kerning pairs (with the {} operator). Values 0 and 1 have a similar meaning as for the -l parameter. <i>The tfm format has room for only about 180x180 ligatures and kerning pairs.</i> This is enough for OT1 encoding, but for texnansi encoding quite a few ligkern specifications have to be removed. The pltotf program will remove <i>all</i> ligkern info if too many ligatures and kerns remain. The default lig file is defpost.lig. This file throws out kerning pairs which are unlikely to be involved in letterspacing, such as kerns involving accents or kerns with a punctuation character or right bracket at the left. It does not add letterspacing kerns involving boundarychars. Instead, fontspace is increased by twice the letterspacing. defpost.lig throws out enough kerns in case of texnansi encoding. With other encodings, you may have to throw out additional kerning pairs. </p>
 </dd></dl>
<h2>FONT-BASED UPPER- AND LOWERCASING</h2>
<p> The distribution includes encoding vectors texnanuc.enc and texnanlc.enc which produce all-uppercase and all-lowercase fonts </p>
<p> The principal uses for an all-uppercase font are page headers and section heads. If these contain math, then macro-based uppercasing would create unpleasant complications. Example: </p>
<dl>
<dd> <pre><code>afm2pl -p texnanuc ptmr8a ptmup8y
pltotf ptmup8y
</code></pre>
 </dd></dl>
<p> For best results, you should add some letterspacing. In LaTeX, this is best done with the microtype package; see the documentation of that package. But it can also be done with afm2pl: </p>
<dl>
<dd> <pre><code>afm2pl -p texnanuc -m 100 ptmr8a ptmup8y
</code></pre>
 </dd></dl>
<p> This requires caution; see above. </p>
<p> You can use this new font within the context of LaTeX font selection as follows: </p>
<dl>
<dd> <pre><code>&lt;preamble commands&gt;
\makeatletter
{\nfss [at] catcodes
\DeclareFontShape{LY1}{ptm}{m}{upp}{&lt;-&gt; ptmup8y}{}}
\makeatother
...
\begin{document}
...
{\fontshape{upp}\selectfont uppercase text}
</code></pre>
 </dd></dl>
<p> Note that upp is simply a newly made-up shape name.  </p>
<h3>The sz ligature ß</h3>
<p> Note that the texnanuc encoding provides no glyph for the sz ligature &szlig;; you&#8217;ll either have to substitute ss or provide a macro-based solution. The following code uses either the usual glyph or substitutes the letters ss, depending on whether the glyph exists in the current font: </p>
<dl>
<dd> <pre><code>\def\ss{%
  \setbox0\hbox{\char25}%
  \ifnum\wd0=0 ss\else\box0\fi
}
</code></pre>
 </dd></dl>
<p> In LaTeX, this code appears to work well enough, although on occasion you may need to insert \protect. A better solution might involve the sixth parameter of the \DeclareFontShape macro, but I failed to get that to work.  </p>
<h2>AFM2PL, FONTINST AND ARTIFICIAL SMALLCAPS</h2>
<p> Afm2pl doesn&#8217;t do virtual fonts. That means that for things such as artificial smallcaps you have to turn elsewhere, e.g. to the fontinst package, which is part of any mainstream TeX distribution. </p>
<p> Look under texmf/tex/fontinst for fontinst support files, which allow you to generate a smallcaps font (tfm and vf files) from an afm2pl-generated tfm file. This package only supports texnansi encoding. </p>
<p> There should be no real problem in doing the same for OT1 encoding. However, there are several variations of the OT1 encoding to take care of. Also, there are as far as I know no officially sanctioned PostScript names for all the variations of the OT1 encoding; the fontinst names contain spaces and are therefore not useable as PostScript names.  </p>
<h2>CHANGED IN VERSION 0.7.1</h2>
<p> In order to avoid name conflicts, the .enc- and .lig files distributed with afm2pl got afm2pl- prepended to their name. The program itself now first searches for the thus prepended name. If the .enc- or .lig file is not found it will look for the original filename. The renaming of the afm2pl .enc files may require modification of some mapfiles.  </p>
<h2>URLS</h2>
<p> The afm2pl homepage is <i><a rel="nofollow" href="http://tex.aanhet.net/afm2pl/">http://tex.aanhet.net/afm2pl/</a></i>. </p>
<p> The paper <i>Font installation the shallow way</i>[2] (EuroTeX 2006 Proceedings, published as <i>TUGboat</i>[3] issue 27.1) illustrates the use of afm2pl.  </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> Except that arguably a narrowed Courier is less jarring than a full-width Courier, when used in combination with a normal proportional font. For Courier, choose .833 to match the width of cmtt. Better yet, don&#8217;t use Courier at all; most TeX distributions offer various good replacements. </p>
 </dd>
<dt> 2.</dt>
<dd> <p> Font installation the shallow way </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.tug.org/TUGboat/Articles/tb27-1/tb86kroonenberg-fonts.pdf">http://www.tug.org/TUGboat/Articles/tb27-1/tb86kroonenberg-fonts.pdf</a> </p>
 </dd></dl>
<dt> 3.</dt>
<dd> <p> TUGboat </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.tug.org/TUGboat/">http://www.tug.org/TUGboat/</a> </p>
 </dd></dl>
