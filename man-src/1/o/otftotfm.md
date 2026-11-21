---

title: "otftotfm(1)"
name: "otftotfm"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otftotfm/"
description: "otftotfm – create TeX font metrics from OpenType fonts"
---

<p> <code>otftotfm</code> [<code>-a</code>] [<code>options</code>] <i>fontfile</i> [<i>texname</i>]</p>
<p> <code>Otftotfm</code> creates the font metric and encoding files required to use an OpenType font with TeX. You supply an OpenType &quot;.otf&quot; or &quot;.ttf&quot; font file, a base &quot;.enc&quot; encoding, and a TeX name &quot;<i>texname</i>&quot; for the resulting font, and say which OpenType features should be turned on. Then <code>otftotfm</code> generates and installs the corresponding TeX-related metric files (&quot;.tfm&quot; TeX font metrics, &quot;.vf&quot; virtual fonts, and &quot;.enc&quot; encoding files). It works on both PostScript-flavored and TrueType-flavored OpenType fonts, although TrueType-flavor support will only work easily with pdftex. </p>
<p> The easiest way to use <code>otftotfm</code> is with the <code>-a</code> option; see Automatic Mode below. Without <code>-a</code>, <code>otftotfm</code> writes all its output files to the current directory. </p>
<p> After running &quot;<code>otftotfm</code> <i>fontfile</i> <i>texname</i>&quot; and installing the results (manually or with <code>-a</code>), you can use the OpenType font in plain TeX with a command like this: </p>
<pre>
    ont\myfont=<i>texname</i> at 10pt
    {\myfont This text uses the OpenType font.}
</pre>
<p> LaTeX users will generally make a &quot;.fd&quot; input file so that commands like &quot;
enewcommand{
mdefault}{TeXName}&quot; work correctly. See the EXAMPLE section for more; check the DIAGNOSTICS and FREQUENTLY ASKED QUESTIONS sections if you have trouble.</p>
<h3>OpenType Features</h3>
<p> OpenType fonts support optional <i>features</i> that change their appearance. Use the <code>-f</code> option to turn on selected features. For example, &quot;<code>-f</code>smcp&quot; replaces lower-case letters with the corresponding small capitals, in fonts that support this. </p>
<p> You&#8217;ll generally provide at least the &quot;<code>-f</code>kern&quot; and &quot;<code>-f</code>liga&quot; options, which activate pair kerns and f-ligatures. Other interesting features include &quot;<code>-f</code>cpsp&quot;, for capital spacing; &quot;<code>-f</code>dlig&quot;, for optional ligatures; &quot;<code>-f</code>lnum&quot;, &quot;<code>-f</code>onum&quot;, &quot;<code>-f</code>pnum&quot;, and &quot;<code>-f</code>tnum&quot;, to control digit glyphs; &quot;<code>-f</code>smcp&quot;, for small capitals; &quot;<code>-f</code>swsh&quot;, for swash variants; and &quot;<code>-f</code>cswh&quot;, for contextual swash. See the FEATURE DIRECTORY section below for more. The program will report which features a font supports; run &quot;<code>otfinfo</code> <code>-f</code> <i>fontfile</i>&quot;. </p>
<p> Feature options can also apply a feature to a subset of characters in the font. For example, &quot;<code>&#8211;lf</code> smcp&quot; <i>only</i> replaces letters with small capitals, whereas &quot;<code>-f</code>smcp&quot; might additionally replace digits and punctuation marks with small-capital versions.</p>
<h3>Automatic Mode</h3>
<p> Automatic mode, triggered by the <code>-a</code>/<code>&#8211;automatic</code> option, installs font metrics and encoding files where TeX can find them, and additionally installs a Type 1 font and mapping for This requires a TeX installation that follows the TeX Directory Structure standard (<a rel="nofollow" href="http://www.tug.org/tds/">http://www.tug.org/tds/</a>), such as most Unix TeX installations. </p>
<p> Automatic mode should run seamlessly out of the box. <code>Otftotfm</code> will install metrics files, encodings, map files, and Type~1 fonts into <i>$HOME/.texmf-var</i> or any other writable TEXMF directory, and run to update the global lists of installed fonts. (On older teTeX installations, you may first need to copy the system&#8217;s <i>updmap.cfg</i> file to <i>$HOME/texmf/web2c</i> and run On newer TeXLive installations, you may need to set the TEXMFVAR environment variable.) You can then run &quot;<code>otftotfm</code> <code>-a</code> <i>fontfile</i> <i>texname</i> and immediately refer to the font in TeX using the <i>texname</i> you supplied. Again, you will have to write &quot;.fd&quot; files and/or typescripts to make the font conveniently accessible from LaTeX or ConTeXt. See the DIAGNOSTICS section if you have problems with these instructions. </p>
<p> In automatic mode, <code>otftotfm</code> searches your $TEXMFVAR or $TEXMF path for a writable directory, then installs files under that directory tree as follows: </p>
<table>
<tr VALIGN=top>
<td><code>File type</code></td>
<td><code>Directory</code></td>
<td><code>Filename</code>
</td>
</tr>
<tr VALIGN=top>
<td>TFM</td>
<td>TEXMF/fonts/tfm/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>texname</i>[&#8211;base].tfm
</td>
</tr>
<tr VALIGN=top>
<td>VF</td>
<td>TEXMF/fonts/vf/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>texname</i>.vf
</td>
</tr>
<tr VALIGN=top>
<td>PL</td>
<td>TEXMF/fonts/pl/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>texname</i>[&#8211;base].pl
</td>
</tr>
<tr VALIGN=top>
<td>VPL</td>
<td>TEXMF/fonts/vpl/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>texname</i>.vpl
</td>
</tr>
<tr VALIGN=top>
<td>encoding</td>
<td>TEXMF/fonts/enc/dvips/<i>vendor</i>/</td>
<td>a_<i>signature</i>.enc
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>or TEXMF/dvips/<i>vendor</i>/</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>font map</td>
<td>TEXMF/fonts/map/dvips/<i>vendor</i>/</td>
<td><i>vendor</i>.map
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>or TEXMF/dvips/<i>vendor</i>/</td>
<td>
</td>
</tr>
</table>
<p> &quot;TEXMF&quot; stands for the writable TEXMF directory. <i>Texname</i> is the font name supplied as <code>otftotfm</code>&#8216;s second argument. The <i>vendor</i> and <i>typeface</i> strings are required by TDS; they default to &quot;lcdftools&quot; and the font&#8217;s family name, respectively, but see the <code>&#8211;vendor</code> and <code>&#8211;typeface</code> options. <i>Signature</i> is an opaque 6-character encoding signature. </p>
<p> <code>Otftotfm</code> also installs a font file suitable for printing. PostScript-flavored OpenType fonts are translated to Type 1 format and installed as PFB fonts. TrueType-flavored fonts are normally installed as is, since pdftex and pdflatex can read TrueType directly; but if you provide the <code>&#8211;type42</code> option, <code>otftotfm</code> will translate TrueType fonts to Type 42 format, which dvips understands. <code>Otftotfm</code> does not overwrite existing font files. </p>
<p> The installation paths are as follows, where <i>PSname</i> is the font&#8217;s PostScript name. </p>
<table>
<tr VALIGN=top>
<td>PFB</td>
<td>TEXMF/fonts/type1/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>PSname</i>.pfb
</td>
</tr>
<tr VALIGN=top>
<td>TrueType</td>
<td>TEXMF/fonts/truetype/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>fontfile</i>
</td>
</tr>
<tr VALIGN=top>
<td>Type 42</td>
<td>TEXMF/fonts/type42/<i>vendor</i>/<i>typeface</i>/</td>
<td><i>PSname</i>.t42
</td>
</tr>
</table>
<p> You can override these directories with environment variables and options as follows. Options take precedence over environment variables. </p>
<table>
<tr VALIGN=top>
<td><code>File type</code></td>
<td><code>Environment variable</code></td>
<td><code>Option</code>
</td>
</tr>
<tr VALIGN=top>
<td>TFM</td>
<td>TFMDESTDIR</td>
<td>&#8211;tfm-directory
</td>
</tr>
<tr VALIGN=top>
<td>VF</td>
<td>VFDESTDIR</td>
<td>&#8211;vf-directory
</td>
</tr>
<tr VALIGN=top>
<td>PL</td>
<td>PLDESTDIR</td>
<td>&#8211;pl-directory
</td>
</tr>
<tr VALIGN=top>
<td>VPL</td>
<td>VPLDESTDIR</td>
<td>&#8211;vpl-directory
</td>
</tr>
<tr VALIGN=top>
<td>encoding</td>
<td>ENCODINGDESTDIR</td>
<td>&#8211;encoding-directory
</td>
</tr>
<tr VALIGN=top>
<td>PFB</td>
<td>T1DESTDIR</td>
<td>&#8211;type1-directory
</td>
</tr>
<tr VALIGN=top>
<td>TrueType</td>
<td>TRUETYPEDESTDIR</td>
<td>&#8211;truetype-directory
</td>
</tr>
<tr VALIGN=top>
<td>Type 42</td>
<td>T42DESTDIR</td>
<td>&#8211;type42-directory
</td>
</tr>
<tr VALIGN=top>
<td>font map</td>
<td>&#8211;</td>
<td>&#8211;map-file
</td>
</tr>
</table>
<p> <code>Otftotfm</code> will update the <i>TEXMF/ls-R</i> file when installing files under TEXMF. It will also run the program after changing a map file, unless the <code>&#8211;no-updmap</code> option was supplied. However, if an executable file called <i>TEXMF/dvips/updmap</i> exists, this file is executed (from the <i>TEXMF/dvips</i> directory) rather than the global <code>updmap</code>. This is so you can write a fast, customized version of <code>updmap</code> if desired.</p>
<h2>EXAMPLE</h2>
<p> This section uses MinionPro to show one way to install OpenType fonts for LaTeX. We begin with six fonts: &quot;MinionPro-Regular.otf&quot;, &quot;MinionPro-It.otf&quot;, &quot;MinionPro-Semibold.otf&quot;, &quot;MinionPro-SemiboldIt.otf&quot;, &quot;MinionPro-Bold.otf&quot;, and &quot;MinionPro-BoldIt.otf&quot;. </p>
<p> Our first task is to decide how to encode the fonts. The &quot;encoding scheme&quot; is used by TeX to decide how to typeset accents and symbols like &quot;$&quot;. The &quot;LY1&quot; encoding scheme has reasonable accent support and is a good choice for many OpenType fonts. LY1 corresponds to the &quot;texnansx.enc&quot; encoding file, so we will supply <code>otftotfm</code> with the &quot;<code>-e</code> texnansx&quot; option.</p>
<dl>
<dt>
</dt><dd>
<p> Expert note: Strictly speaking, LY1 corresponds to the &quot;texnansi.enc&quot; encoding file. Since the &quot;texnansx.enc&quot; version omits duplicate characters, it has more room for font-specific glyphs and is generally a better choice; but if you plan to type characters like &quot;ae&quot; directly into your editor, rather than using TeX commands like e, you should use &quot;texnansi.enc&quot;.</dd></dl>
<p> Next, we decide on a naming scheme for the font metric files. Let&#8217;s use the OpenType font names as a base. (There&#8217;s generally no need to follow the six-character &quot;Karl Berry&quot; naming scheme.) Just in case we come back later and add a different encoding scheme, we&#8217;ll prepend &quot;LY1&#8211;&quot; to each name. </p>
<p> We&#8217;re now ready to run <code>otftotfm</code> for the first set of fonts. Note the &quot;<code>-f</code>kern <code>-f</code>liga&quot; options, which access pair kerns and the default &quot;f&quot; ligatures. </p>
<pre><code>
otftotfm - a - e texnansx MinionPro - Regular.otf - fkern - fliga LY1-- MinionPro - Regular otftotfm - a - e texnansx MinionPro - It.otf - fkern - fliga LY1-- MinionPro - It otftotfm - a - e texnansx MinionPro - Semibold.otf - fkern - fliga LY1-- MinionPro - Semibold otftotfm - a - e texnansx MinionPro - SemiboldIt.otf - fkern - fliga LY1-- MinionPro - SemiboldIt otftotfm - a - e texnansx MinionPro - Bold.otf - fkern - fliga LY1-- MinionPro - Bold otftotfm - a - e texnansx MinionPro - BoldIt.otf - fkern - fliga LY1-- MinionPro - BoldIt
</code></pre>
<p> The small-caps fonts are generated with an additional &quot;<code>-f</code>smcp&quot; option. We append &quot;&#8211;fsmcp&quot; to the font metric names as well, differentiating them from the regular fonts. Although MinionPro&#8217;s italic fonts support small-caps, the LaTeX font selection scheme can&#8217;t access them easily, so we&#8217;ve left them off. </p>
<p>otftotfm &#8211; a &#8211; e texnansx MinionPro &#8211; Regular.otf &#8211; fkern &#8211; fliga &#8211; fsmcp LY1&#8211; MinionPro &#8211; Regular&#8211; fsmcp otftotfm &#8211; a &#8211; e texnansx MinionPro &#8211; Semibold.otf &#8211; fkern &#8211; fliga &#8211; fsmcp LY1&#8211; MinionPro &#8211; Semibold&#8211; fsmcp otftotfm &#8211; a &#8211; e texnansx MinionPro &#8211; Bold.otf &#8211; fkern &#8211; fliga &#8211; fsmcp LY1&#8211; MinionPro &#8211; Bold&#8211; fsmcp</p>
<p> To get old-style numerals, just add the &quot;<code>-f</code>onum&quot; option to each invocation &#8212; and, to reduce confusion, append &quot;&#8211;fonum&quot; to the font metric names. </p>
<p> At this point, all our font metric files are installed, and it&#8217;s finally time to create the &quot;.fd&quot; file. (The &quot;.fd&quot; format is documented in <i>The LaTeX Companion</i>.) Let&#8217;s call the LaTeX font family &quot;MinionPro&quot;. Then the &quot;.fd&quot; file is &quot;LY1MinionPro.fd&quot;, and it contains: </p>
<p>\DeclareFontFamily{LY1} {MinionPro}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {m} {n} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; Regular}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {m} {it} { &lt;-&gt;LY1&#8211; MinionPro &#8211; It}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {m} {sc} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; Regular&#8211; fsmcp}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {sb} {n} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; Semibold}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {sb} {it} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; SemiboldIt}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {sb} {sc} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; Semibold&#8211; fsmcp}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {b} {n} { &lt;-&gt;LY1&#8211; MinionPro &#8211; Bold}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {b} {it} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; BoldIt}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {b} {sc} %<br />
    { &lt;-&gt;LY1&#8211; MinionPro &#8211; Bold&#8211; fsmcp}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {bx} {n} %<br />
    { &lt;-&gt;ssub * MinionPro / b / n}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {bx} {it} %<br />
    { &lt;-&gt;ssub * MinionPro / b / it}<br />
{<br />
}<br />
\DeclareFontShape{LY1} {MinionPro} {bx} {sc} %<br />
    { &lt;-&gt;ssub * MinionPro / b / sc}<br />
{<br />
}</p>
<p> We&#8217;re now ready to use MinionPro in LaTeX, with lines like this in the document preamble: </p>
<p> </p>
<pre><code>    \usepackage[LY1]{fontenc}
    \renewcommand{\rmdefault}{MinionPro}
    \renewcommand{\bfdefault}{b}
</code></pre>
<p> Of course, we&#8217;re free at any time to add more MinionPro variants with <code>otftotfm</code>; they&#8217;ll become accessible to LaTeX as soon as we edit the &quot;MinionPro.fd&quot; file.  </p>
<h2>OPTIONS</h2>
<p> With long options, you need type only as many characters as will make the option unique.  </p>
<h3>Font Feature and Transformation Options</h3>
<dl>
<dt><code>-s</code><i> script</i>[.<i>lang</i>], <code>--script=</code><i>script</i>[.<i>lang</i>] </dt>
<dd> <p> Apply features suitable to the script system <i>script</i> and language system <i>lang</i>. Scripts and language systems are two-to-four-letter names assigned by Microsoft and Adobe. Examples include &quot;latn&quot; (Latin script), &quot;grek&quot; (Greek script), and &quot;yi.YIC&quot; (Yi script with classic characters). If <i>lang</i> is not specified, <code>otftotfm</code> will use the default language system for that script. You can give this option multiple times. Run &quot;<code>otfinfo</code> -s <i>font</i>&quot; to see the list of scripts and languages a font supports. Defaults to &quot;latn&quot;. </p>
 </dd>
<dt><code>-f</code><i> feature</i>, <code>--feature=</code><i>feature</i></dt>
<dd> <p> Activate the feature named <i>feature</i>. Features are four-letter names assigned by Microsoft and Adobe; they are meant to correspond to font behaviors, such as kerning or small-capitals. Examples include &quot;liga&quot; (default ligatures), &quot;dlig&quot; (discretionary ligatures), &quot;kern&quot; (kerning), and &quot;c2sc&quot; (replacing capitals with small capitals). Give this option multiple times to apply multiple features. Run &quot;<code>otfinfo</code> -f [--script option] <i>font</i>&quot; to see the list of features a font supports for a specified script. Defaults to any features required by the selected scripts. </p>
 </dd>
<dt><code>--lf</code><i> feature</i>, <code>--letter-feature=</code><i>feature</i></dt>
<dd> <p> Activate the feature named <i>feature</i>, but only for letters. For instance, the &quot;-f smcp&quot; option will apply the small-caps feature to all characters in the encoding; this may result in changes to punctuation and numbers as well as letters. The &quot;--lf smcp&quot; option will apply the small-caps feature only to letters, meaning characters with the &quot;Letter&quot; Unicode property. </p>
 </dd>
<dt><code>--subs-filter</code><i> pattern</i></dt>
<dd>  </dd>
<dt><code>--include-subs</code><i> pattern</i></dt>
<dd>  </dd>
<dt><code>--exclude-subs</code><i> pattern</i></dt>
<dd>  </dd>
<dt><code>--clear-subs</code></dt>
<dd> <p> Limit the characters that <code>otftotfm</code> will substitute. Substitution is allowed on an input character if it matches at least one of the <code>--include</code> patterns, and none of the <code>--exclude</code> patterns. Each pattern applies to all following features, except that the <code>--clear</code> option clears any accumulated patterns. The <code>--subs-filter</code><i> pattern</i> option acts like <code>--clear-subs</code> followed by <code>--include-subs</code><i> pattern</i>. For pattern syntax, see GLYPH PATTERNS, below. </p>
<p> In the command line below, the &#8216;&lt;Number&gt;&#8216; pattern will force the &quot;onum&quot; feature to substitute only numbers (and not, for example, punctuation). The &quot;salt&quot; feature can still substitute any character. </p>
<pre><code> otftotfm  -f salt --include-subs =&quot;&lt;Number&gt;&quot; -f onum ...
</code></pre>
 </dd>
<dt><code>-E</code><i> fac</i>, <code>--extend=</code><i>fac</i></dt>
<dd> <p> Widen, or extend, the font by a factor of <i>fac</i>. Like <code>-e</code> option. </p>
 </dd>
<dt><code>-S</code><i> amt</i>, <code>--slant=</code><i>amt</i></dt>
<dd> <p> Oblique, or slant, the font by <i>amt</i>. Like <code>-s</code> option. </p>
 </dd>
<dt><code>-L</code><i> amt</i>, <code>--letterspacing=</code><i>amt</i></dt>
<dd> <p> Letterspace each character by <i>amt</i> units, where 1000 units equals one em. The width of each character increases by <i>amt</i>, with half the space distributed to each sidebearing. Boundary-character kerns are added to maintain alignment at the ends of lines. </p>
 </dd>
<dt><code>--math-spacing</code>[=<i>skewchar</i>] </dt>
<dd> <p> Ignore the font&#8217;s claimed character widths, deriving horizontal metrics from bounding boxes instead. This results in similar spacing as the Computer Modern Math Italic font, with increased sidebearings for letters like f and j. </p>
<p> If you provide <i>skewchar</i>, a number between 0 and 255 or a single character, then <code>otftotfm</code> adds heuristically-derived kerns to the font that may improve accent positions in math mode. To get the benefits, you must tell TeX about the <i>skewchar</i> with a command like &quot;\skewchar\font=<i>skewchar</i>&quot;. </p>
 </dd>
<dt><code>-k </code><i>N</i>, <code>--min-kern=</code><i>N</i></dt>
<dd> <p> Only output kerning pairs whose absolute value is <i>N</i> or larger. Larger minimum kerns make kerning less precise, but shrink the output TFM file. The default minimum kern is 2.0, or 0.002 em. </p>
 </dd>
<dt><code>--space-factor=</code><i>fac</i></dt>
<dd> <p> Scale the width of the inter-word space by a factor of <i>fac</i>. </p>
 </dd>
<dt><code>--design-size=</code><i>size</i></dt>
<dd> <p> Set the output font&#8217;s design size to <i>size</i>, a value in TeX points. This value is mostly just documentation, since LaTeX essentially ignores fonts&#8217; design sizes, but plain TeX may occasionally use the design size to decide how large a font should be. (Loading a font in TeX &quot;at&quot; a particular size effectively ignores the design size; loading a font plain or &quot;scaled&quot; by a given factor uses the design size.) The default is taken from the input font&#8217;s optical size feature, or 10pt if it has no such feature. </p>
 </dd>
<dt><code>--fixed-width</code></dt>
<dd> <p> Set the font to fixed-width (its space character will have no stretch or shrink). Normally you won&#8217;t need this option; the font will tell <code>otftotfm</code> whether it is fixed width. The opposite of <code>--fixed-width</code> is <code>--proportional-width</code>. </p>
 </dd>
<dt><code>--italic-angle=</code><i>angle</i></dt>
<dd> <p> Set the output font&#8217;s default italic angle to <i>angle</i>, a number of degrees. This value is used by TeX to position accents. Normally you won&#8217;t need this option; the font will tell <code>otftotfm</code> its italic angle. </p>
 </dd>
<dt><code>--x-height=</code><i>val</i></dt>
<dd> <p> Set the output font&#8217;s x-height to <i>val</i>. This value is used by TeX to position accents. Normally you won&#8217;t need this option. <i>Val</i> may be a number expressed in font units; &#8216;x&#8217;, which uses the height of the font&#8217;s lowercase x; or &#8216;font&#8217;, which uses the font&#8217;s declared x-height metric. </p>
 </dd></dl>
<h3>Encoding Options</h3>
<dl>
<dt><code>-e</code><i> encoding</i>, <code>--encoding=</code><i>encoding</i></dt>
<dd> <p> Select the output metrics&#8217;s base encoding. <code>Otftotfm</code> will search for <i>encoding</i>[.enc] the same way that <code>dvips</code> would, so you may not need to give a full pathname. Say <code>-e -</code> to start with the font&#8217;s default encoding. See ENCODINGS, below, for more information. </p>
 </dd>
<dt><code>--boundary-char=</code><i>char</i></dt>
<dd> <p> Set the font&#8217;s boundary character to <i>char</i>, which should either be a single non-digit character, or a number between -1 and 255. The default is taken from the encoding. </p>
 </dd>
<dt><code>--altselector-char=</code><i>char</i></dt>
<dd> <p> Set the font&#8217;s alternate selector character to <i>char</i>, which should either be a single non-digit character, or a number between -1 and 255. Alternate selectors let TeX authors explicitly choose between versions of a character. For instance, the &#8216;--altselector-char=&quot;*&quot;&#8216; option turns the &quot;*&quot; character into a special switch that cycles between alternates. For instance, the TeX input &quot;A&quot; would produce the normal version of the &quot;A&quot; Unicode character, &quot;A*&quot; would produce the first alternate, &quot;A**&quot; would produce the second alternate, and so forth. Furthermore, &quot;s*t&quot; will activate any discretionary &quot;s_t&quot; ligature in the font. </p>
<p> The <code>--altselector-char</code> mechanism uses the features specified by <code>--altselector-feature</code> options. </p>
<p> The alternate-selector character may also be specified in the encoding; see ENCODINGS, below. See Sivan Toledo&#8217;s article cited in the SEE ALSO section for more information. </p>
 </dd>
<dt><code>--altselector-feature=</code><i>feature</i></dt>
<dd> <p> Activate the feature named <i>feature</i> for the <code>--altselector-char</code> mechanism. Give this option multiple times to activate multiple features. This option activates features only for use with <code>--altselector-char</code>; use the <code>--feature</code> option to activate features globally. Defaults to the <i>salt</i> and <i>dlig</i> features. </p>
 </dd>
<dt><code>--alternates-filter=</code><i>pattern</i></dt>
<dd>  </dd>
<dt><code>--include-alternates=</code><i>pattern</i></dt>
<dd>  </dd>
<dt><code>--exclude-alternates=</code><i>pattern</i></dt>
<dd>  </dd>
<dt><code>--clear-alternates</code></dt>
<dd> <p> Limit the alternate characters that <code>otftotfm</code> will select. An alternate is used if it matches at least one of the <code>--include</code> patterns, and none of the <code>--exclude</code> patterns. Each pattern applies to all following features, except that the <code>--clear</code> option clears any accumulated patterns. The <code>--alternates-filter</code><i> pattern</i> option acts like <code>--clear-alternates</code> followed by <code>--include-alternates</code><i> pattern</i>. For pattern syntax, see GLYPH PATTERNS, below. </p>
<p> OpenType fonts can have many alternates per character, most of which aren&#8217;t interesting. For example, the character &quot;a&quot; in WarnockPro-Regular has five alternates, &quot;ordfeminine&quot;, &quot;Asmall&quot;, &quot;asuperior&quot;, &quot;a.end&quot;, and &quot;orn.013&quot;. The <code>--altselector-char</code> option lets you cycle through these alternates, but it&#8217;s better to leave out the ones you don&#8217;t want, to avoid overfull encodings. Thus, if you were only interested in &quot;.end&quot; variants, you might supply an &#8216;--include-alternates=&quot;*.end&quot;&#8216; option. </p>
<p> In the command line below, the &#8216;*.end&#8217; pattern will apply to &quot;aalt&quot; alternates, but not to &quot;salt&quot; alternates. </p>
<pre><code> otftotfm  -f salt --include-alternates =&quot;*.end&quot; -f aalt ...
</code></pre>
 </dd>
<dt><code>--ligkern=</code><i>command</i></dt>
<dd> <p> Add a LIGKERN <i>command</i> to the encoding. For example, &#8216;<code>--ligkern</code> &quot;T {L} h&quot;&#8216; suppresses any T_h ligature in the font. You can supply multiple <code>--ligkern</code> options. See ENCODINGS, below. </p>
 </dd>
<dt><code>--position=</code><i>command</i></dt>
<dd> <p> Add a POSITION <i>command</i> to the encoding. For example, &#8216;<code>--position</code> &quot;T 10 0 20&quot;&#8216; adds ten units of space to either side of the &quot;T&quot; character. You can supply multiple <code>--position</code> options. See ENCODINGS, below. </p>
 </dd>
<dt><code>--unicoding=</code><i>command</i></dt>
<dd> <p> Add a UNICODING <i>command</i> to the encoding. For example, &#8216;<code>--unicoding</code> &quot;pi1 =: uni03D6&quot;&#8216; tells <code>otftotfm </code> to encode &quot;/pi1&quot; as U+03D6 GREEK PI SYMBOL. You can supply multiple <code>--unicoding</code> options. See ENCODINGS, below. </p>
 </dd>
<dt><code>--no-encoding-commands</code></dt>
<dd> <p> Ignore any LIGKERN and/or UNICODING commands in the encoding file. </p>
 </dd>
<dt><code>--no-default-ligkern</code></dt>
<dd> <p> Don&#8217;t include <code>otftotfm</code>&#8216;s default LIGKERN commands. </p>
 </dd>
<dt><code>--coding-scheme=</code><i>scheme</i></dt>
<dd> <p> Add a CODINGSCHEME to the encoding. See ENCODINGS, below. </p>
 </dd>
<dt><code>--warn-missing</code></dt>
<dd> <p> Warn about encoded characters not supported by the font. See the WARNMISSING command in ENCODINGS, below. </p>
 </dd>
<dt><code>--literal-encoding=</code><i>encoding</i></dt>
<dd> <p> Select the encoding used for the font. No glyph substitutions will be permitted, so the output encoding will equal the input encoding (and <code>otftotfm</code> will not generate an output encoding). </p>
 </dd>
<dt><code>--base-encodings=</code><i>file</i></dt>
<dd> <p> <code>Experts only.</code> Allow the output font to refer to existing &quot;base&quot; fonts. This can greatly reduce the number of base fonts generated by <code>otftotfm</code>. Each line in the <i>file</i> argument contains a TeX font name (as for <code>--name</code>) and a corresponding literal encoding file (as for <code>--literal-encoding</code>); for example: </p>
<pre><code>    WarnoProReg--eka eka
    WarnoProReg--exp1 exp1
</code></pre>
<p> The named fonts must have been created by prior runs of <code>otftotfm</code> on the same input OpenType font, with the same <code>--extend</code> and <code>--slant</code> options as the current run. The current output font will refer to glyphs from the named base fonts when possible. If the base fonts cover all glyphs required by the output font, <code>otftotfm</code> won&#8217;t generate any new base fonts at all. The <i>file</i> can also refer to dotless-J fonts using the following syntax: </p>
<pre><code>    WarnoProReg--lcdfj - dotlessj
</code></pre>
 </dd></dl>
<h3>Automatic Mode Options</h3>
<dl>
<dt><code>-a</code><i></i>, <code>--automatic</code></dt>
<dd> <p> Select automatic mode. </p>
 </dd>
<dt><code>-v</code><i> vendor</i>, <code>--vendor=</code><i>vendor</i></dt>
<dd> <p> Set the font vendor name, which is used to locate files within the TDS. Defaults to &quot;lcdftools&quot;. </p>
<p> In automatic mode, TeX and friends will generally find required font files independently of the vendor you select. </p>
 </dd>
<dt><code>--typeface=</code><i>typeface</i></dt>
<dd> <p> Set the font typeface name, which is used to locate files within the TDS. Defaults to the current font&#8217;s family name with unsuiable characters removed. </p>
 </dd>
<dt><code>--no-type1</code></dt>
<dd> <p> Do not use to create Type 1 fonts corresponding to the OpenType input fonts. </p>
 </dd>
<dt><code>--no-dotlessj</code></dt>
<dd> <p> Do not use to create a special dotless-j font when the input font doesn&#8217;t have dotless-j. </p>
 </dd>
<dt><code>--no-truetype</code></dt>
<dd> <p> Do not install TrueType-flavored fonts. </p>
 </dd>
<dt><code>--type42</code></dt>
<dd> <p> Install TrueType-flavored fonts in translated Type 42 format. </p>
 </dd>
<dt><code>--no-updmap</code></dt>
<dd> <p> Do not run an program. This can be useful if you&#8217;re installing a bunch of fonts; it is much faster to run <code>updmap</code> once, at the end, than to run it once per font. </p>
 </dd></dl>
<h3>Output Options</h3>
<dl>
<dt><code>-n</code><i> texname</i>, <code>--name=</code><i>texname</i></dt>
<dd> <p> Set the TeX name of the output font, which is used in font map files and, in automatic mode, to generate the output filename. The default is derived from the OpenType font&#8217;s name and the features you selected. </p>
 </dd>
<dt><code>-p</code><i></i>, <code>--pl</code></dt>
<dd> <p> Output human-readable PL and VPL metrics, not binary TFM and VF metrics. Note: <code>Otftotfm</code>&#8216;s PL and VPL output files are legal, but the <code>fontinst</code> program may not accept them (it has a picky parser). Make sure to supply a <code>--coding-scheme</code>; if that doesn&#8217;t help, run the TFM output through </p>
 </dd>
<dt><code>--no-virtual</code></dt>
<dd> <p> Do not generate virtual fonts (VFs and VPLs). <code>Otftotfm</code> will warn if the selected font features cannot be implemented without virtual fonts. </p>
 </dd>
<dt><code>--no-encoding</code></dt>
<dd> <p> Do not generate an encoding file. </p>
 </dd>
<dt><code>--output-encoding</code>[=<i>file</i>] </dt>
<dd> <p> Only generate an encoding file; do not generate any other output. The encoding file is written to <i>file</i>, or to standard output if no <i>file</i> argument is supplied. </p>
 </dd>
<dt><code>--no-map</code></dt>
<dd> <p> Do not generate a font map line for the font. </p>
 </dd></dl>
<h3>File Location Options</h3>
<dl>
<dt><code>--tfm-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--pl-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--vf-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--vpl-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--encoding-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--type1-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--truetype-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--type42-directory=</code><i>dir</i></dt>
<dd>  </dd>
<dt><code>--directory=</code><i>dir</i></dt>
<dd> <p> Set the directory used for various output types. Each directory may be set by an environment variable, and defaults to a TDS directory in automatic mode, or to &quot;.&quot; otherwise. Environment variable names and default TDS locations are described in the Automatic Mode section above. The <code>--directory</code> option sets the default directory for all output types. </p>
 </dd>
<dt><code>--map-file=</code><i>filename</i></dt>
<dd> <p> Set file in which <code>otftotfm</code> will write a font map line for the font. The default is the standard output in manual mode, and &quot;TEXMF/fonts/map/dvips/<i>vendor</i>/<i>vendor</i>.map&quot; (or &quot;TEXMF/dvips/<i>vendor</i>/<i>vendor</i>.map&quot; on older installations) in automatic mode. </p>
 </dd></dl>
<h3>Miscellaneous Options</h3>
<dl>
<dt><code>--glyphlist=</code><i>file</i></dt>
<dd> <p> Use <i>file</i> as a Adobe glyph list, which helps translate glyph names to Unicode code points. Give multiple options to include multiple files. See ENCODINGS, below, for more information. </p>
 </dd>
<dt><code>-V</code>, <code>--verbose</code></dt>
<dd> <p> Write progress messages to standard error. </p>
 </dd>
<dt><code>--no-create</code></dt>
<dd> <p> Do not create or modify any files. Instead, write messages about the program&#8217;s hypothetical progress to standard error. </p>
 </dd>
<dt><code>--force</code></dt>
<dd> <p> Generate all files, even if it looks like versions are already installed. </p>
 </dd>
<dt><code>-q</code>, <code>--quiet</code></dt>
<dd> <p> Do not generate any error messages. </p>
 </dd>
<dt><code>--kpathsea-debug=</code><i>flags</i></dt>
<dd> <p> Set path searching debugging flags. See the <i>Kpathsea</i> manual for details. </p>
 </dd>
<dt><code>-h</code>, <code>--help</code></dt>
<dd> <p> Print usage information and exit. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print the version number and some short non-warranty information and exit. </p>
 </dd></dl>
<h2>ENCODINGS</h2>
<p> <code>Otftotfm</code> interprets encoding files as Unicode. For example, say an input encoding has &quot;/dotlessi&quot; at position 10. <code>Otftotfm</code> detects that position 10 should contain Unicode character U+0131 LATIN SMALL LETTER DOTLESS I, and uses the font&#8217;s glyph for that character (possibly modified by any active features). The selected glyph might not be named &quot;dotlessi&quot;; only the Unicode value matters. </p>
<p> <code>Otftotfm</code> assigns Unicode values to glyph names using a table published by Adobe (SEE ALSO has a reference), with extensions for TeX. For more fine-grained control, add UNICODING commands to the input encoding file. These commands have the following format: </p>
<pre><code>    % UNICODING glyph  =: choice1  [ choice2  ...] ;
</code></pre>
<p> This tells <code>otftotfm</code> that the glyph named <i>glyph</i> translates into the first Unicode value in the <i>choice</i> list that has a character in the font. <i>Glyph</i> and the <i>choice</i>s are PostScript glyph names; the initial &quot;%&quot; sign is required; and each UNICODING line can contain multiple commands, separated by spaced semicolons. For example, </p>
<pre><code>    % UNICODING pi1 =: uni03D6 ;
</code></pre>
<p> encodes the character &quot;/pi1&quot; as U+03D6 GREEK PI SYMBOL, and </p>
<pre><code>    % UNICODING Delta =: uni0394 uni2206 ;
</code></pre>
<p> makes U+0394 GREEK CAPITAL LETTER DELTA preferred to U+2206 INCREMENT as an encoding for &quot;/Delta&quot;. You can also supply glyph names: </p>
<pre><code>    % UNICODING Delta =: Deltagreek Delta ;
</code></pre>
<p> A mapping with no Unicode values removes that glyph from the input encoding. For instance, this erases any f-ligature characters from the encoding: </p>
<pre><code>    % UNICODING ff =: ; fi =: ; fl =: ; ffi =: ; ffl =: ;
</code></pre>
<p> The slots are available for <code>otftfm</code>&#8216;s own use, for example for other characters required by the font. (If the f-ligatures themselves are required by the font, for instance by a &#8216;liga&#8217; feature, then they will be stored into their old slots when possible.) Map a glyph to &#8216;emptyslot&#8217; if you don&#8217;t want <code>otftotfm</code> to use the slot. For example, this will leave the &#8216;ff&#8217; slot unused if the font has no &#8216;ff&#8217; glyph: </p>
<pre><code>    % UNICODING ff =: ff emptyslot ;
</code></pre>
<p> (Note that most OpenType fonts provide a visible representation for unused encoding slots, namely a box with an X inside.) </p>
<p> LIGKERN comments in the encoding can add ligatures and inhibit kerns, as in To add a ligature, say: </p>
<pre><code>    % LIGKERN glyph1  glyph2  =: result  ;
</code></pre>
<p> The &quot;=:&quot; operator indicates a normal ligature, where both the input glyphs are removed and replaced by <i>result</i>. To preserve the left-hand glyph, for an effect like &quot;<i>glyph1</i> <i>glyph2</i> =: <i>glyph1</i> <i>result</i>&quot;, use &quot;|=:&quot; instead; to preserve the right-hand glyph, use &quot;=:|&quot;. To remove all kerns between two characters, say: </p>
<pre><code>    % LIGKERN glyph1  {} glyph2  ;
</code></pre>
<p> A &quot;*&quot; matches any character, so </p>
<pre><code>    % LIGKERN a {} * ;
</code></pre>
<p> removes all kerns with &quot;a&quot; as the left-hand character, and </p>
<pre><code>    % LIGKERN * {} * ;
</code></pre>
<p> removes all kerns. </p>
<p> <code>Otftotfm</code> also supports extended syntax for setting kern values and inhibiting ligatures. To add an <i>n</i>-unit kern between two glyphs, say: </p>
<pre><code>    % LIGKERNX glyph1  { n } glyph2  ;
</code></pre>
<p> where <i>n</i> is an integer. This: </p>
<pre><code>    % LIGKERNX glyph1  {L} glyph2  ;
</code></pre>
<p> inhibits any ligature between <i>glyph1</i> and <i>glyph2</i>. &quot;{LK}&quot; and &quot;{KL}&quot; inhibit both ligatures and kerns. </p>
<p> You can set the <code>--boundary-char</code> and <code>--altselector-char</code> from an encoding file with commands like this: </p>
<pre><code>    % LIGKERN || = boundarychar  ;
    % LIGKERNX ^^ = altselectorchar  ;
</code></pre>
<p> As with UNICODING, each LIGKERN or LIGKERNX line can contain multiple commands, separated by spaced semicolons. </p>
<p> <code>Otftotfm</code> has a default set of eight ligatures, namely: </p>
<pre><code>    space l =: lslash ; space L =: Lslash ;
    question quoteleft =: questiondown ; exclam quoteleft =: exclamdown ;
    hyphen hyphen =: endash ; endash hyphen =: emdash ;
    quoteleft quoteleft =: quotedblleft ;
    quoteright quoteright =: quotedblright
</code></pre>
<p> LIGKERN commands in the encoding file and <code>--ligkern</code> options can override these defaults, or supply the <code>--no-default-ligkern</code> option to turn them off. </p>
<p> The POSITION command shifts a glyph within its bounding box. The syntax is </p>
<pre><code>    % POSITION glyph  pdx  pdy  adx  ;
</code></pre>
<p> This will add <i>pdx</i> units of space to <i>glyph</i>&#8216;s left edge; raise it up by <i>pdy</i> units; and add <i>adx</i> units to its width. For example, to add 10 units of space to either side of the &quot;T&quot; glyph, supply </p>
<pre><code>    % POSITION T 10 0 20
</code></pre>
<p> To move the &quot;degree&quot; symbol up by 20 units, supply </p>
<pre><code>    % POSITION degree 0 20 0
</code></pre>
<p> The CODINGSCHEME command specifies the coding scheme for fonts using this encoding. This is a string, less than 40 characters long and containing no parentheses, that classifies the encoding for TeX&#8217;s purposes. Sample coding schemes include &quot;TEX TEXT&quot;, &quot;TEX MATH ITALIC&quot;, and &quot;EXTENDED TEX FONT ENCODING &#8211; LATIN&quot;. For example: </p>
<pre><code>    % CODINGSCHEME EXTENDED TEX FONT ENCODING - LATIN
</code></pre>
<p> Most tools ignore the coding scheme; fontinst is an exception. <code>Otftotfm</code> uses the encoding&#8217;s PostScript name for the default coding scheme. </p>
<p> Finally, the WARNMISSING command makes any glyphs not supported by the input font appear as black boxes. The processor will also print a warning when encountering these glyphs. For example: </p>
<pre><code>    % WARNMISSING yes
</code></pre>
<p> The <code>--unicoding</code>, <code>--ligkern</code>, <code>--position</code>, <code>--coding-scheme</code>, and <code>--warn-missing</code> options add UNICODING, LIGKERN/LIGKERNX, POSITION, CODINGSCHEME, and WARNMISSING commands to an encoding, and can override commands in the encoding itself. Some common encoding files have commands that are inappropriate for OpenType fonts; for example, &quot;t1.enc&quot; hard-codes f-ligatures, which can cause problems with small-cap fonts. Supply the <code>--no-encoding-commands</code> option to ignore all commands from the encoding file. Commands from options like <code>--ligkern</code> are processed in any case.  </p>
<h3>New Glyphs</h3>
<p> New glyphs, such as ligatures and contextual substitutions, are added to the encoding in any empty spaces, using their original locations when possible. If the encoding doesn&#8217;t have enough space for all new glyphs, shorter ligatures composed of unaccented letters get precedence.  </p>
<h3>Synthetic Glyphs</h3>
<p> <code>Otftotfm</code> can synthesize some glyphs using virtual font manipulations, if a required glyph is not available in the input font. Specifically, it will synthesize: </p>
<dl>
<dt>cwm</dt>
<dd> <p> TeX&#8217;s compound word mark (a zero-width &quot;strut&quot; rule with height equal to the font&#8217;s x-height) </p>
 </dd>
<dt>ascendercompwordmark</dt>
<dd> <p> &quot;cwm&quot; with height equal to the font&#8217;s ascenders </p>
 </dd>
<dt>capitalcompwordmark</dt>
<dd> <p> &quot;cwm&quot; with height equal to the font&#8217;s capitals </p>
 </dd>
<dt>visualspace</dt>
<dd> <p> A square cup used to represent spaces </p>
 </dd>
<dt>dotlessj</dt>
<dd> <p> A dotless &quot;j&quot;, synthesized with </p>
 </dd>
<dt>dblbracketleft</dt>
<dd> <p> Kerned version of &quot;[[&quot; </p>
 </dd>
<dt>dblbracketright</dt>
<dd> <p> Kerned version of &quot;]]&quot; </p>
 </dd>
<dt>bardbl</dt>
<dd> <p> The parallel symbol &quot;||&quot; </p>
 </dd>
<dt>asteriskmath</dt>
<dd> <p> Vertically-centered &quot;*&quot; </p>
 </dd>
<dt>ringfitted</dt>
<dd> <p> Ring accent centered on the width of &quot;A&quot; </p>
 </dd>
<dt>twelveudash</dt>
<dd> <p> 2/3-em-wide dash </p>
 </dd>
<dt>threequartersemdash</dt>
<dd> <p> 3/4-em-wide dash </p>
 </dd>
<dt>centigrade</dt>
<dd> <p> &quot;(degrees)C&quot; </p>
 </dd>
<dt>interrobang</dt>
<dd> <p> Combined &quot;?!&quot; symbol </p>
 </dd>
<dt>interrobangdown</dt>
<dd> <p> Inverted interrobang </p>
 </dd>
<dt>pertenthousand</dt>
<dd> <p> Per-ten-thousand sign (% with two extra 0s) </p>
 </dd>
<dt>IJ</dt>
<dd> <p> &quot;IJ&quot; ligature </p>
 </dd>
<dt>ij</dt>
<dd> <p> &quot;ij&quot; ligature </p>
 </dd>
<dt>Germandbls</dt>
<dd> <p> &quot;SS&quot; (a capital sharp-s) </p>
 </dd>
<dt>SSsmall</dt>
<dd> <p> Small-capital version of &quot;SS&quot; </p>
 </dd>
<dt>FFsmall</dt>
<dd> <p> Small-capital version of &quot;FF&quot; </p>
 </dd>
<dt>FIsmall</dt>
<dd> <p> Small-capital version of &quot;FI&quot; </p>
 </dd>
<dt>FLsmall</dt>
<dd> <p> Small-capital version of &quot;FL&quot; </p>
 </dd>
<dt>FFIsmall</dt>
<dd> <p> Small-capital version of &quot;FFI&quot; </p>
 </dd>
<dt>FFLsmall</dt>
<dd> <p> Small-capital version of &quot;FFL&quot; </p>
 </dd></dl>
<h2>GLYPH PATTERNS</h2>
<p> The <code>--include-subs</code> and <code>--include-alternates</code> options, and their <code>--exclude</code> and <code>--*-filter</code> variants, accept the following types of pattern. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Glyph names. Example: &quot;Aacute&quot;. For PostScript-flavored fonts, use <code>-g</code> option to see a font&#8217;s glyph names, and &quot;<code>cfftot1</code> <i>font</i>.otf | <code>t1testpage</code>&quot; to generate a PostScript file showing each glyph. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Glyph name patterns using the shell-style glob-matching rules: &quot;*&quot; matches any number of characters, &quot;?&quot; matches any single character, and &quot;[...]&quot; matches any character in a set. Example: &quot;*.end&quot;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode category properties in angle brackets. Examples: &quot;&lt;Letter&gt;&quot;, &quot;&lt;UppercaseLetter&gt;&quot;, &quot;&lt;Lu&gt;&quot;. The complete list of both short and long names: Letter/L, UppercaseLetter/Lu, LowercaseLetter/Ll, TitlecaseLetter/Lt, ModifierLetter/Lm, OtherLetter/Lo; Number/N, DecimalNumber/Nd, LetterNumber/Nl, OtherNumber/No; Punctuation/P, ConnectorPunctuation/Pc, DashPunctuation/Pd, OpenPunctuation/Ps, ClosePunctuation/Pe, InitialPunctuation/Pi, FinalPunctuation/Pf, OtherPunctuation/Po; Symbol/S, MathSymbol/Sm, CurrencySymbol/Sc, ModifierSymbol/Sk, OtherSymbol/So; Mark/M, SpacingMark/Mc, EnclosingMark/Me, NonspacingMark/Mn; Separator/Z, SpaceSeparator/Zs, LineSeparator/Zl, ParagraphSeparator/Zp; Other/C, Surrogate/Cs, Format/Cf, Control/Cc, PrivateUse/Co, Unassigned/Cn. Category values current as of Unicode 4.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode ranges. Example: &quot;U+007f-U+008C&quot;. </p>
 </dd></dl>
<p> The &quot;!&quot; prefix negates a pattern, and you can separate multiple patterns by spaces.  </p>
<h2>FEATURE DIRECTORY</h2>
<p> This section lists features common to Western OpenType fonts and describes how <code>otftotfm </code> handles them for common fonts. Please send the author mail if <code>otftotfm</code> does not handle a feature you need, or you believe it handles some feature incorrectly. </p>
<dl>
<dt><i>aalt</i>, Access All Alternates </dt>
<dd> <p> Lets the user choose between all available alternate forms for a character. This includes things like superscript and subscript variants, different styles (swash, for example), and even ornaments. The <code>--altselector-feature=</code>aalt option can help an <code>--altselector-char</code> provide useful access to alternates, but the <i>aalt</i> feature isn&#8217;t usually useful on its own. Try the <i>salt</i> and <i>calt</i> features instead. </p>
 </dd>
<dt><i>c2sc</i>, Small Capitals From Capitals </dt>
<dd> <p> Replaces capital letters with small capitals: a sort of converse of the more conventional <i>smcp</i> feature, which replaces lower-case letters with small capitals. Supported. </p>
 </dd>
<dt><i>calt</i>, Contextual Alternates </dt>
<dd> <p> Lets the user choose between context-appropriate swash forms for each character. For example, given the word &quot;DREW&quot; in a cursive typeface, the &quot;R E W&quot; might be translated to calmer forms than the initial &quot;D&quot;. There may be more than one choice for a given letter, in which case the user should be able to select among them. TeX can&#8217;t support complex contextual alternates, or alternate selection, but <code>otftotfm </code> supports some fonts quite well. The input encoding should have lots of empty space for variants, and it should specify a boundary character. See also <i>cswh</i>. </p>
 </dd>
<dt><i>case</i>, Case-Sensitive Forms </dt>
<dd> <p> Shifts punctuation marks up to a position that works well with all-capital-letter sequences. For example, the hyphen character, which generally centers vertically on the x-height, is raised up to center vertically on a capital letter. Also replaces text figures with lining figures, and accent marks with forms more appropriate for capitals. Supported. </p>
 </dd>
<dt><i>cpsp</i>, Capital Spacing </dt>
<dd> <p> Adds a bit of space on either side of each capital letter. Supported. (However, the OpenType tag registry suggests that <i>cpsp</i> be on by default, but applying to all-caps text only; TeX cannot easily implement that contextual intelligence.) </p>
 </dd>
<dt><i>cswh</i>, Contextual Swash </dt>
<dd> <p> Lets the user choose between context-appropriate swash forms for each character. For example, in the words &quot;Ab AC&quot;, the first &quot;A&quot; might be translated to a swash form, while the second might not. There may be more than one choice for a given letter, in which case the user should be able to select among them. <code>Otftotfm</code> supports some fonts quite well. The input encoding should have lots of empty space for swash variants, and it should specify a boundary character. See also <i>calt</i> and <i>swsh</i>. </p>
 </dd>
<dt><i>dlig</i>, Discretionary Ligatures </dt>
<dd> <p> Activates uncommon ligatures, such as &quot;c_t&quot;, &quot;s_p&quot;, and &quot;s_t&quot;. Supported. </p>
 </dd>
<dt><i>dnom</i>, Denominators </dt>
<dd> <p> Replaces digits and some punctuation marks with smaller forms sitting on the baseline, intended for fraction denominators. Supported. </p>
 </dd>
<dt><i>fina</i>, Terminal Forms </dt>
<dd> <p> Substitutes appropriate forms for letters occurring at the ends of words. This feature doesn&#8217;t select swash variants; it&#8217;s intended for normal use, and the specification recommends that it be on by default. Partially supported: TeX will only treat spaces as the ends of words, where a correct implementation would probably include punctuation too. See <i>cswh</i> for selecting swash variants active at the ends of words. </p>
 </dd>
<dt><i>frac</i>, Fractions </dt>
<dd> <p> Replaces simple sequences like &quot;1/2&quot; with nice-looking fractions. Supported, but beware: many fonts will translate &quot;11/32&quot; into &quot;1&quot; + &quot;1/3&quot; + &quot;2&quot;. </p>
 </dd>
<dt><i>hist</i>, Historical Forms </dt>
<dd> <p> Replaces characters with historical variants. Usually, this means at least translating regular &quot;s&quot; to long &quot;s&quot;. Supported. </p>
 </dd>
<dt><i>kern</i>, Kerning </dt>
<dd> <p> Adjusts the space between characters (pair kerning). Generally supported, and you should probably turn it on. As a special case, &quot;<code>-f</code>kern&quot; can also read kerning information from the &quot;kern&quot; table in conventional TrueType fonts. </p>
 </dd>
<dt><i>liga</i>, Standard Ligatures </dt>
<dd> <p> Activates common ligatures, such as &quot;f_f&quot;, &quot;f_i&quot;, &quot;f_f_j&quot;, and (in some Adobe fonts) &quot;T_h&quot;. Generally supported, and you should probably turn it on. </p>
 </dd>
<dt><i>lnum</i>, Lining Figures </dt>
<dd> <p> Uses lining figures, the set of digits that are all about as high as capital letters. Supported. Compare <i>onum</i>; see also <i>pnum</i> and <i>tnum.</i> </p>
 </dd>
<dt><i>numr</i>, Numerators </dt>
<dd> <p> Replaces digits and some punctuation marks with smaller, raised forms intended for fraction numerators. Supported, but not usually useful. </p>
 </dd>
<dt><i>onum</i>, Oldstyle Figures </dt>
<dd> <p> Uses old-style figures, also known as text figures. This is the set of digits that have ascenders and descenders like lower-case letters. Supported. Compare <i>lnum</i>; see also <i>pnum</i> and <i>tnum</i>. </p>
 </dd>
<dt><i>ordn</i>, Ordinals </dt>
<dd> <p> Designed for Spanish and French. Replaces ordinal numbers, such as &quot;2.o&quot;, with forms where the &quot;o&quot; is raised, and replaces the sequence &quot;No&quot; with an integrated glyph. Supported. </p>
 </dd>
<dt><i>ornm</i>, Ornaments </dt>
<dd> <p> Replaces some alphabetic characters in the font with ornaments, and links the bullet character to a set of all bullet-like ornaments, from which the user can choose. Partially supported: TeX can handle alphabetic substitutions, but not bullet choice. </p>
 </dd>
<dt><i>pnum</i>, Proportional Figures </dt>
<dd> <p> Digits will have different widths. Supported. Compare <i>tnum</i>; see also <i>lnum</i> and <i>onum.</i> </p>
 </dd>
<dt><i>salt</i>, Stylistic Alternates </dt>
<dd> <p> Lets the user choose between stylistic alternate forms for a character. The <code>--altselector-char</code> mechanism provides useful access to this feature. If you turn on <i>salt</i> globally, <code>otftotfm</code> takes the first alternate form whenever there&#8217;s more than one choice. See also <i>aalt</i> and <i>ss01</i>; <i>salt</i> is generally more useful than <i>aalt</i> for TeX, since it refers exclusively to stylistic alternates. </p>
 </dd>
<dt><i>sinf</i>, Scientific Inferiors </dt>
<dd> <p> Replaces digits and some punctuation marks with smaller, lowered forms intended for subscripts. Supported. Compare <i>subs</i>. </p>
 </dd>
<dt><i>size</i>, Optical Size </dt>
<dd> <p> This feature stores information about the range of optical sizes for which the font was intended. There is no point in selecting it with <code>otftotfm</code>, since it should not change the font&#8217;s appearance in any way. </p>
 </dd>
<dt><i>smcp</i>, Small Capitals </dt>
<dd> <p> Replaces lower-case letters with small capitals. Supported. Compare <i>c2sc</i>. </p>
 </dd>
<dt><i>ss01</i>-<i>ss20</i>, Stylistic Sets 1-20 </dt>
<dd> <p> Replaces characters with a uniform set of stylistic alternates. Differs from features like <i>salt</i> in that a Stylistic Set is uniform: an <i>ssXX</i> feature should never involve selection from a set of possible alternate characters. Supported. </p>
 </dd>
<dt><i>subs</i>, Subscript </dt>
<dd> <p> Replaces characters with smaller, lowered forms intended for subscripts. Supported. Compare <i>sinf</i>; some fonts support <i>sinf</i> but not <i>subs</i>. </p>
 </dd>
<dt><i>sups</i>, Superscript </dt>
<dd> <p> Replaces digits, some punctuation marks, and some lower-case letters with smaller, raised forms intended for superscripts. Supported. </p>
 </dd>
<dt><i>swsh</i>, Swash </dt>
<dd> <p> Activates all swash forms for each character. There may be more than one swash form, in which case <code>otftotfm</code> will pick the first one listed. Supported, except that swash variants other than the first are inaccessible. Note that some fonts with swash variants support the <i>cswh</i> feature exclusively. </p>
 </dd>
<dt><i>tnum</i>, Tabular Figures </dt>
<dd> <p> All digits will have the same width, so that tables and the like will align visually. Supported. Compare <i>pnum</i>; see also <i>lnum</i> and <i>onum.</i> </p>
 </dd>
<dt><i>zero</i>, Slashed Zero </dt>
<dd> <p> Replaces the zero character with a slashed zero. Supported. </p>
 </dd></dl>
<h2>DIAGNOSTICS AND TROUBLESHOOTING</h2>
<dl>
<dt>no writable directory found in $TEXMF</dt>
<dd> <p> <code>Otftotfm</code> could not find a writable directory in your $TEXMFVAR or $TEXMF path. Did you create a <i>$HOME/.texmf-var</i> or <i>$HOME/texmf</i> directory? If so, run the command &quot;kpsewhich --expand-path=&#8216;$TEXMF&#8217;&quot; to verify that directory is not being found. You may need to set your TEXMF environment variable, to &#8216;{!!&#8216;&quot;$HOME&quot;&#8216;/texmf,!!$TEXMFMAIN}&#8216;, for instance (note the different kinds of quotes; on my machine, this expands to &#8216;{!!/home/kohler/texmf,!!$TEXMFMAIN}&#8216;). </p>
 </dd>
<dt>&#8216;<i>char</i>&#8216; has no encoding, ignoring kern removal</dt>
<dd>  </dd>
<dt>(or ligature removal, lig/kern removal, or ligature)</dt>
<dd> <p> These messages indicate a slight problem with your encoding file: one of the LIGKERN commands referred to a character not present in the encoding. This might be due to a misspelling in the LIGKERN command or the encoding file, or it might be an oversight. Either fix the encoding file or ignore the warning. </p>
 </dd>
<dt>can&#8217;t map &#8216;<i>char</i>&#8216; to Unicode</dt>
<dd> <p> Another encoding file problem: One of the glyph names in an UNICODING block could not be converted to Unicode. This is problematic since UNICODING exists wholly to translate glyph names into Unicode. Fix the encoding file or ignore the warning. </p>
 </dd>
<dt>not enough room in encoding, ignoring <i>N</i> glyph(s) ...</dt>
<dd> <p> There wasn&#8217;t space in the encoding for all the glyphs referred to by the features you selected. For example, maybe the font had more ligatures than there were empty slots in the encoding. Fix this warning by selecting fewer features, or by using an encoding with more empty slots, such as the 7t.enc encoding distributed with <code>otftotfm</code>. </p>
 </dd>
<dt>The &#8216;<code>-a</code>&#8216; option did not install my font correctly.</dt>
<dd> <p> Try again with the &#8216;<code>--verbose</code>&#8216; option, which causes <code>otftotfm</code> to explain its behavior. Note that by default, <code>otftotfm</code> will not re-install files already present in your system&#8217;s TeX search paths (in the current directory, for instance). Use &#8216;<code>--force</code>&#8216; to override this behavior. </p>
 </dd></dl>
<h2>FREQUENTLY ASKED QUESTIONS</h2>
<dl>
<dt>How can I get a small-caps &quot;SS&quot; in place of the German sharp-S?</dt>
<dd> <p> Supply the option &#8216;<code>--unicoding</code> &quot;germandbls =: SSsmall&quot;&#8216;. </p>
 </dd>
<dt>How can I prevent f-ligatures from forming in a small-caps font? </dt>
<dd> <p> This should happen automatically, but some overzealous encoding files add f-ligatures even when the font doesn&#8217;t request them. Try the &quot;<code>--no-encoding-commands</code>&quot; option if this is a problem for you. </p>
 </dd>
<dt><code>Otftotfm</code> seems to take a long time.</dt>
<dd> <p> Use the <code>-V</code> option to see what it&#8217;s doing. Often the culprit is the program; if you&#8217;re planning to run <code>otftotfm</code> multiple times, give it the <code>--no-updmap</code> option and run <code>updmap</code> manually when you&#8217;re done. </p>
 </dd>
<dt>How can I refer to the different forms of phi?</dt>
<dd> <p> <code>Otftotfm</code> follows TeX practice and widely-distributed TeX encoding vectors, so &quot;/phi&quot; in an input encoding vector should map to a &quot;straight&quot; phi and &quot;/phi1&quot; should map to a &quot;loopy&quot; phi. Note that TeX practice differs from the PostScript standard naming conventions, in which &quot;/phi&quot; is &quot;loopy&quot; and &quot;/phi1&quot; is &quot;straight&quot;; this means that <code>otftotfm</code> may map &quot;/phi&quot; in an input encoding vector to a font&#8217;s &quot;/phi1&quot; glyph, and vice versa. Perhaps most unambiguously, you can use &quot;/uni03D5&quot; for the &quot;straight&quot; form and &quot;/uni03C6&quot; for the &quot;loopy&quot; form. </p>
 </dd>
<dt>How can I get lining figures (that is, normal line-height digits) with small caps (&#8216;<code>-f</code>smcp&#8217;)?</dt>
<dd> <p> Many fonts use old-style figures by default with small caps. Since the default is not specified, it&#8217;s wise to explicitly supply &#8216;<code>-f</code>lnum&#8217; or &#8216;<code>-f</code>onum&#8217;. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> See the documentation for <code>--pl</code> above if you have problems running <code>otftotfm</code>&#8216;s output through <code>fontinst</code>.  </p>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i> </p>
<p> Adobe Technical Notes #5176, <i>The Compact Font Format Specification</i>, and #5177, <i>The Type 2 Charstring Format</i> </p>
<p> <i>OpenType Specification</i>, Version 1.4 </p>
<p> <i>A Directory Structure for TeX Files</i>, <a rel="nofollow" href="http://www.tug.org/tds/">http://www.tug.org/tds/</a> </p>
<p> <i>Kpathsea: A library for path searching</i>, <a rel="nofollow" href="http://www.tug.org/kpathsea/">http://www.tug.org/kpathsea/</a> </p>
<p> Sivan Toledo, <i>Exploiting Rich Fonts</i>, TUGboat <a href="/docs/linux/man/2-21/">21</a>(2), 2000, <a rel="nofollow" href="http://www.tug.org/TUGboat/Articles/tb21-2/tb67tole.pdf">http://www.tug.org/TUGboat/Articles/tb21-2/tb67tole.pdf</a> </p>
<p> Michel Goossens, Frank Mittelbach, and Alexander Samarin, <i>The LaTeX Companion</i> (for information on the .fd file format) </p>
<p> Adobe Systems, &quot;Unicode and Glyph Names&quot;. Refers to the glyphlist.txt file used to translate glyph names to Unicode code points. <a rel="nofollow" href="http://partners.adobe.com/public/developer/opentype/index_glyph.html">http://partners.adobe.com/public/developer/opentype/index_glyph.html</a>  </p>
<h2>AUTHOR</h2>
<p> Eddie Kohler (ekohler [at] gmail.com) </p>
<p> Thanks to Karl Berry, Marco Kuhlmann, Adam Lindsay, Bruce D&#8217;Arcus, Thomas Esser, Claire Connelly, Nelson H.F. Beebe, and Ryuji Suzuki for suggestions, bug reports, and help. Particular thanks to Achim Blumensath and Michael Zedler for suggestions and patches, some of them extensive. </p>
