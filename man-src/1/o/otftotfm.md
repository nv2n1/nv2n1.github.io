---
title: "otftotfm(1)"
name: "otftotfm"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otftotfm/"
description: "otftotfm – create TeX font metrics from OpenType fonts"
---

<h2 class="name">NAME</h2>
<p> otftotfm &#8211; create TeX font metrics from OpenType fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>otftotfm</code> [<code>-a</code>] [<code>options</code>] <i>fontfile</i> [<i>texname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Otftotfm</code> creates the font metric and encoding files required to use an OpenType font with TeX. You supply an OpenType &quot;.otf&quot; or &quot;.ttf&quot; font file, a base &quot;.enc&quot; encoding, and a TeX name &quot;<i>texname</i>&quot; for the resulting font, and say which OpenType features should be turned on. Then <code>otftotfm</code> generates and installs the corresponding TeX-related metric files (&quot;.tfm&quot; TeX font metrics, &quot;.vf&quot; virtual fonts, and &quot;.enc&quot; encoding files). It works on both PostScript-flavored and TrueType-flavored OpenType fonts, although TrueType-flavor support will only work easily with pdftex. </p>
<p> The easiest way to use <code>otftotfm</code> is with the <code>-a</code> option; see Automatic Mode below. Without <code>-a</code>, <code>otftotfm</code> writes all its output files to the current directory. </p>
<p> After running &quot;<code>otftotfm</code> <i>fontfile</i> <i>texname</i>&quot; and installing the results (manually or with <code>-a</code>), you can use the OpenType font in plain TeX with a command like this: </p>
<pre>
    ont\myfont=<i>texname</i> at 10pt
    {\myfont This text uses the OpenType font.}
</pre>
<p> LaTeX users will generally make a &quot;.fd&quot; input file so that commands like &quot;enewcommand{mdefault}{TeXName}&quot; work correctly. See the EXAMPLE section for more; check the DIAGNOSTICS and FREQUENTLY ASKED QUESTIONS sections if you have trouble.</p>
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
<dd>
<p> Expert note: Strictly speaking, LY1 corresponds to the &quot;texnansi.enc&quot; encoding file. Since the &quot;texnansx.enc&quot; version omits duplicate characters, it has more room for font-specific glyphs and is generally a better choice; but if you plan to type characters like &quot;ae&quot; directly into your editor, rather than using TeX commands like e, you should use &quot;texnansi.enc&quot;.</dl>
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
<p>
