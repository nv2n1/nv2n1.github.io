---

title: "autoinst(1)"
name: "autoinst"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoinst/"
description: "autoinst – wrapper around the LCDF TypeTools, for installing and using OpenType fonts in LaTeX."
---

<p> autoinst &#8211; wrapper around the LCDF TypeTools, for installing and using OpenType fonts in LaTeX. </p>
<h2>SYNOPSIS</h2>
<p> <code>autoinst</code> <i>-help</i> </p>
<p> <code>autoinst</code> [<i>options</i>] <code>font(s)</code></p>
<h2>DESCRIPTION</h2>
<p> Eddie Kohler&#8217;s <i></i><i>LCDF</i><i> TypeTools</i> are superb tools for installing OpenType fonts in LaTeX, but they can be hard to use: they need many, often long, command lines and don&#8217;t generate the <i>fd</i> and <i>sty</i> files LaTeX needs. <code>autoinst</code> simplifies the use of the <i>TypeTools</i> for font installation by generating and executing all commands for <i>otftotfm</i>, and by creating and installing all necessary <i>fd</i> and <i>sty</i> files. </p>
<p> Given a family of font files (in <i>otf</i> or <i>ttf</i> format), <code>autoinst</code> will create several LaTeX font families:</p>
<dl>
<dl>
<dt>&#8211;</dt>
<dd> Four text families (with lining and oldstyle digits, each in both tabular and proportional variants), all with the following shapes:</dd>
<dl>
<dl>
<dl>
<dt><i>n</i></dt>
<dd> Roman (i.e., upright) text</dd>
<dt><i>it</i>, <i>sl</i></dt>
<dd> Italic and slanted (sometimes called oblique) text</dd>
<dt><i>sc</i></dt>
<dd> Small caps</dd>
<dt><i>scit</i>, <i>scsl</i></dt>
<dd> Italic and slanted small caps</dd>
<dt><i>sw</i></dt>
<dd> Swash</dd>
<dt><i>nw</i></dt>
<dd> &#8220;Upright swash&#8221;</dd></dl>
</dl>
<dl>
</dl>
</dl>
<dl>
</dl>
<dt>&#8211;</dt>
<dd> For each T1-encoded text family: a family of TS1-encoded symbol fonts, in roman, italic and slanted shapes.</dd>
<dt>&#8211;</dt>
<dd> Families with superiors, inferiors, numerators and denominators, in roman, italic and slanted shapes.</dd>
<dt>&#8211;</dt>
<dd> Families with &#8220;Titling&#8221; characters; these &#8220;&#8230; replace the default glyphs with corresponding forms designed specifically for titling. These may be all-capital and/or larger on the body, and adjusted for viewing at larger sizes&#8221; (according to the OpenType Specification).</dd>
<dt>&#8211;</dt>
<dd> An ornament family; also in roman, italic and slanted shapes.</dd></dl>
</dl>
<dl>
</dl>
<p> Of course, if your fonts don&#8217;t contain italics, oldstyle digits, small caps etc., the corresponding shapes and families are not created. In addition, the creation of most families and shapes can be controlled by the user (see &#8220;COMMAND-LINE OPTIONS&#8221; below). </p>
<p> These families use the <i>FontPro</i> project&#8217;s naming scheme: <i>&lt;FontFamily&gt;-&lt;Suffix&gt;</i>, where <i>&lt;Suffix&gt;</i> is:</p>
<dl>
<dt><i></i><i>LF</i><i></i></dt>
<dd> proportional (i.e., figures have varying widths) lining figures</dd>
<dt><i></i><i>TLF</i><i></i></dt>
<dd> tabular (i.e., all figures have the same width) lining figures</dd>
<dt><i>OsF</i></dt>
<dd> proportional oldstyle figures</dd>
<dt><i>TOsF</i></dt>
<dd> tabular oldstyle figures</dd>
<dt><i>Sup</i></dt>
<dd> superior characters (note that most fonts have only an incomplete set of superior characters: digits, some punctuation and the letters <i>abdeilmnorst</i>; normal forms are used for other characters)</dd>
<dt><i>Inf</i></dt>
<dd> inferior characters; usually only digits and some punctuation, normal forms for other characters</dd>
<dt><i>Titl</i></dt>
<dd> Titling characters; see above</dd>
<dt><i>Orn</i></dt>
<dd> ornaments</dd>
<dt><i>Numr</i>, <i>Dnom</i></dt>
<dd> numerators and denominators</dd></dl>
<p> The individual fonts are named <i>&lt;FontName&gt;-&lt;suffix&gt;-&lt;shape&gt;-&lt;enc&gt;</i>, where <i>&lt;suffix&gt;</i> is the same as above (but in lowercase), <i>&lt;shape&gt;</i> is either empty, &#8220;sc&#8221; or &#8220;swash&#8221;, and <i>&lt;enc&gt;</i> is the encoding (also in lowercase). A typical name in this scheme would be <i>FiraSans-Light-osf-sc-ly1</i>.</p>
<h3>Using the fonts in your LaTeX documents</h3>
<p> <code>autoinst</code> generates a style file for using the fonts in LaTeX documents, named <i>&lt;FontFamily&gt;.sty</i>. This style file also loads the <i>fontenc</i> and <i>textcomp</i> packages, if necessary. To use the fonts, add the command <tt>&quot;</tt>\usepackage{</code>&lt;FontFamily&gt;<code>}&quot;</code> to the preamble of your document. </p>
<p> This style file has a few options: </p>
<dl>
<dt>&quot;mainfont&quot;</dt>
<dd> <p> Redefine <code>&quot;\familydefault&quot;</code> to make this font the main font for the document. This is a no-op if the font is installed as a serif font; but if the font is installed as a sanserif or typewriter font, this option saves you from having to redefine <code>&quot;\familydefault&quot;</code> yourself. </p>
 </dd>
<dt>&quot;lining&quot;, &quot;oldstyle&quot;, &quot;tabular&quot;, &quot;proportional&quot;</dt>
<dd> <p> Choose which figure style to use. The defaults are ``oldstyle&#8217;&#8216; and ``proportional&#8217;&#8216; (if available). </p>
 </dd>
<dt>&quot;scale=<i>&lt;number&gt;</i>&quot;, &quot;scale=MatchLowercase&quot;</dt>
<dd> <p> Scale the font by a factor of <i>&lt;number&gt;</i>. E.g., to increase the size of the font by 5%, use <code>&quot;\usepackage[scale=1.05]{</code>&lt;FontFamily&gt;<code>}&quot;</code>. The special value <code>&quot;MatchLowercase&quot;</code> may be used to scale the font so that its x-height matches that of the current main font (which is usually Computer Modern Roman, unless you have loaded another font package before this one). The name <code>&quot;scaled&quot;</code> may be used as a synonym for <code>&quot;scale&quot;</code>. </p>
 </dd>
<dt>&quot;medium&quot;, &quot;book&quot;, &quot;text&quot;, &quot;normal&quot;, &quot;regular&quot;</dt>
<dd> <p> Select the weight that LaTeX will use as the ``regular&#8217;&#8216; weight. </p>
 </dd>
<dt>&quot;heavy&quot;, &quot;black&quot;, &quot;extrabold&quot;, &quot;demibold&quot;, &quot;semibold&quot;, &quot;bold&quot;</dt>
<dd> <p> Select the weight that LaTeX will use as the ``bold&#8217;&#8216; weight. </p>
 </dd></dl>
<p> The last two groups of options will only work if you have the <i>mweights</i> package installed. The default here is not to change LaTeX&#8217;s default, i.e. use the ``m&#8217;&#8216; and ``b&#8217;&#8216; weights. </p>
<p> The style file will also try to load the <i>fontaxes</i> package (on CTAN), which gives easy access to various font shapes and styles. Using the machinery set up by <i>fontaxes</i>, the generated style file defines a number of commands (which take the text to be typeset as argument) and declarations (which don&#8217;t take arguments, but affect all text up to the end of the current group) to access titling, superior and inferior characters: </p>
<pre><code>    DECLARATION COMMAND SHORT FORM OF COMMAND
    \tlshape \texttitling \texttl
    \supfigures \textsuperior \textsup, \textsu
    \inffigures \textinferior \textinf, \textin
</code></pre>
<p> In addition, the existing <code>&quot;\swshape&quot;</code> and <code>&quot;\textsw&quot;</code> commands are redefined to place swash on <i>fontaxes</i>&#8216; secondary shape axis (<i>fontaxes</i> places it on the primary shape axis) to make them behave properly when nested, so that <code>&quot;\swshape\upshape&quot;</code> will give upright swash. </p>
<p> There are no commands for accessing the numerator and denominator fonts; these can be selected using <i>fontaxes</i>&#8216; standard commands, e.g., <code>&quot;\fontfigurestyle{numerator}\selectfont&quot;</code>. </p>
<p> These commands are only generated for existing shapes and number styles; no commands are generated for shapes and styles that are missing from your fonts. Also these commands are built on top of <i>fontaxes</i>, so if that package cannot be found, you&#8217;re limited to using the lower-level commands from standard NFSS (<code>&quot;\fontfamily&quot;</code>, <code>&quot;\fontseries&quot;</code>, <code>&quot;\fontshape&quot;</code> etc.). </p>
<p> By default, <code>autoinst</code> generates text fonts with OT1, LY1 and T1 encodings, and the generated style files use T1 as the default text encoding. Other encodings can be chosen using the <i>-encoding</i> option (see ``COMMAND-LINE OPTIONS&#8217;&#8216; below).  </p>
<h3>Maths</h3>
<p> This is an experimental feature; <code>USE AT YOUR OWN RISK</code><code>!</code> Test the results thoroughly before using them in real documents, and be warned that future versions of <code>autoinst</code> may introduce incompatible changes. </p>
<p> The <i>-math</i> option tells <code>autoinst</code> to generate basic math fonts. When enabled, the generated style file defines a few extra options to access these math fonts: </p>
<dl>
<dt>&quot;math&quot;</dt>
<dd> <p> Use these fonts for the maths in your document. </p>
 </dd>
<dt>&quot;mathlining&quot;, &quot;matholdstyle&quot;</dt>
<dd> <p> Choose which figure style to use in maths. The default is ``mathlining&#8217;&#8216;. </p>
 </dd>
<dt>&quot;mathcal&quot;</dt>
<dd> <p> Use the swash characters from your fonts as the <code>&quot;\mathcal&quot;</code> alphabet. (This option will only exist if your fonts actually contain swash characters, plus a <code>&quot;swsh&quot;</code> feature to access them). </p>
 </dd>
<dt>&quot;nomathgreek&quot;</dt>
<dd> <p> Don&#8217;t redeclare greek letters in math. </p>
 </dd>
<dt>&quot;math-style=<i>&lt;style&gt;</i>&quot;</dt>
<dd> <p> Choose the ``math style&#8217;&#8216; to use. With <code>&quot;math-style=ISO&quot;</code>, all latin and greek letters in math are italic; with <code>&quot;math-style=TeX&quot;</code> (the default), uppercase greek is upright; with <code>&quot;math-style=french&quot;</code>, all greek as well as uppercase latin is upright; and with <code>&quot;math-style=upright&quot;</code> all letters are upright. </p>
 </dd></dl>
<p> Note that this <code>&quot;math&quot;</code> option only affects digits, latin and greek letters, plus a few basic punctuation characters; all other mathematical symbols, operators, delimiters etc. are left as they were before. If you don&#8217;t want to use TeX&#8217;s default versions of those symbols, load another math package (such as <i>mathdesign</i> or <i>newtxmath</i>) before loading the <code>autoinst</code>-generated style file. </p>
<p> Finally, note that <code>autoinst</code> doesn&#8217;t check if your fonts actually contains all of the required characters; it just assumes that they do and sets up the style file accordingly. Even if your fonts contain greek, characters such as <code>&quot;\varepsilon&quot;</code> may be missing. You may also find that some glyphs <i>are</i> present in your fonts, but don&#8217;t work well in equations or don&#8217;t match with other symbols; edit the generated style file to remove the declarations of these offending characters. Once again: test the results before using them! If the characters themselves are fine but spaced too tightly, you may try increasing the side bearings in math fonts with the <i>-mathspacing</i> option (see below), e.g. <code>&quot;-mathspacing=50&quot;</code>.  </p>
<h3>NFSS codes</h3>
<p> LaTeX&#8217;s New Font Selection System (NFSS) identifies fonts by a combination of family, series (the concatenation of weight and width), shape and size. <code>autoinst</code> parses the font&#8217;s metadata to determine these parameters. When this fails (usually because the font family contains uncommon weights, widths or shapes), <code>autoinst</code> ends up with multiple fonts having the same values for these font parameters; such fonts cannot be used in NFSS, since there&#8217;s no way distinguish them. When <code>autoinst</code> detects such a situation, it will print an error message and abort. If that happens, either rerun <code>autoinst</code> on a smaller set of fonts, or add the missing widths, weights and shapes to the tables <code>@WIDTH</code>, <code>@WEIGHT</code> and <code>%SHAPE</code> in the source code. Please also send a bug report (see AUTHOR below). </p>
<p> The mapping of shapes to NFSS codes is done using the following table: </p>
<pre><code>    SHAPE CODE
    -------------------------------- ----
    Roman, Upright n
    Italic it
    Oblique, Slant(ed), Incline(d) sl
</code></pre>
<p> (<i>Exception:</i> Adobe Silentium Pro contains two Roman shapes; we map the first of these to <code>&quot;n&quot;</code>, for the second one we (ab)use the <code>&quot;it&quot;</code> code as this family doesn&#8217;t contain an Italic shape.) </p>
<p> For weights and widths, <code>autoinst</code> tries to the standard NFSS codes (ul, el, l, sl, m, sb, b, eb and ub for weights; uc, ec, c, sc, m, sx, x, ex and ux for widths) as much as possible. Of course, not all 81 combinations of these NFSS weights and widths will map to existing fonts; and conversely it may not be possible to assign every existing font a unique code in a sane way (especially for the weights, some font families offer more variants than NFSS&#8216;s codes can handle; e.g., Fira Sans contains fifteen different weights!). Therefore every font is also assigned a ``series&#8217;&#8216; name that is the concatenation of its weight and width, after expanding any abbreviations and converting to lowercase. A font of ``Cond&#8217;&#8216; width and ``Ultra&#8217;&#8216; weight will then be known as ``ultrablackcondensed&#8217;&#8216;. </p>
<p> The exact mapping between fonts and NFSS codes can be found in the generated <i>fd</i> files and in the log file (you may want to run <code>autoinst</code> with the <i>-dryrun</i> option to check the chosen mapping beforehand). The <i>-nfssweight</i> and <i>-nfsswidth</i> command-line options can be used to finetune the mapping between NFSS codes and fonts. </p>
<p> To access specific weights or widths, one can always use the <code>&quot;\fontseries&quot;</code> command with the full series name (i.e., <code>&quot;\fontseries{demibold}\selectfont&quot;</code>).  </p>
<h3>Ornaments</h3>
<p> Ornament fonts are regular LY1-encoded fonts, with a number of ``regular&#8217;&#8216; characters replaced by ornament glyphs. The OpenType specification says that fonts should only put their ornaments in place of the lowercase ASCII letters, but some fonts put them in other positions (such as those of the digits) as well. </p>
<p> Ornaments can be accessed like <code>&quot;{\ornaments a}&quot;</code> and <code>&quot;{\ornaments\char&quot;61}&quot;</code>, or equivalently <code>&quot;\textornaments{a}&quot;</code> and <code>&quot;\textornaments{\char&quot;61}&quot;</code>. To see which ornaments a font contains (and at which positions), run LaTeX on the file <i>nfssfont.tex</i> (which is included in any standard LaTeX installation), supply the name of the ornament font (i.e., <code>&quot;GaramondLibre-Regular-orn-u&quot;</code>) and give the command <code>&quot;\table\bye&quot;</code>; this will create a table of all glyphs in that font. </p>
<p> Note that versions of <code>autoinst</code> up to 20200428 handled ornaments differently, and fonts and style files generated by those versions are not compatible with files generated by newer versions.  </p>
<h2>WARNINGS AND CAVEATS</h2>
<h3>OpenType fonts and licensing issues</h3>
<p> Since <i>pdfTeX</i> cannot subset otf-flavoured OpenType fonts, <i>otftotfm</i> will convert such fonts to Type1 (pfb) format. However, many fonts (at least those licensed under the SIL Open Font License) do not allow distributing such converted versions under their original name. </p>
<p> To meet these licensing requirements, <code>autoinst</code> provides a <i>-t1suffix</i> command-line option that appends a user-defined suffix to the names (both the filename and the internal font name) of all generated Type1 fonts; see ``COMMAND-LINE OPTIONS&#8217;&#8216; below.  </p>
<h3>Sorry, LIGTABLE too long for me to handle</h3>
<p> The LIGTABLE in TeX&#8217;s <i>tfm</i> files, which contains a font&#8217;s ligatures and kerning pairs, is limited to about 32,500 entries (2^15 &#8211; 256). If the number of ligatures plus kerns in a font is higher than that limit, <i>pltotf</i> and <i>vptovf</i> will complain loudly and ignore the excess entries. This happens at least with Adobe&#8217;s Source Serif 4 and Minion 3. The best way to handle this situation is to use <code>autoinst</code>&#8216;s <code>&quot;-extra&quot;</code> option to raise <i>otftotfm</i>&#8216;s value for the <code>&quot;--min-kern&quot;</code> parameter, which causes it to ignore small kerning pairs: <code>&quot;-extra=&#8216;--min-kern=5.0&#8217;&quot;</code>.  </p>
<h3>A note for MiKTeX users</h3>
<p> Automatically installing the fonts into a suitable TEXMF tree (as <code>autoinst</code> tries to do by default) only works for TeX-installations that use the <i>kpathsea</i> library; with TeX distributions that implement their own directory searching, such as MiKTeX, <code>autoinst</code> will complain that it cannot find the <i>kpsewhich</i> program and move all generated files into a subdirectory <code>&quot;autoinst_output/&quot;</code> of the current directory. If you use such a TeX distribution, you should either move these files to their correct destinations by hand, or use the <i>-target</i> option (see ``COMMAND-LINE OPTIONS&#8217;&#8216; below) to manually specify a TEXMF tree. </p>
<p> Also, some OpenType fonts contain so many kerning pairs that the resulting <i>pl</i> and <i>vpl</i> files are too big for MiKTeX&#8217;s <i>pltotf</i> and <i>vptovf</i>; the versions that come with W32TeX (<i><a rel="nofollow" href="http://www.w32tex.org">http://www.w32tex.org</a></i>) and TeXLive (<i><a rel="nofollow" href="http://tug.org/texlive">http://tug.org/texlive</a></i>) don&#8217;t seem to have this problem.  </p>
<h3>A note for MacTeX users</h3>
<p> By default, <code>autoinst</code> will try to install all generated files into the <code>$TEXMFLOCAL</code> tree; when this directory isn&#8217;t user-writable, it will use the <code>$TEXMFHOME</code> tree instead. Unfortunately, MacTeX&#8217;s version of <code>&quot;updmap-sys&quot;</code> doesn&#8217;t search in <code>$TEXMFHOME</code>, and hence MacTeX will not find the new fonts. </p>
<p> To remedy this, either run <code>autoinst</code> as root (so that it can install everything into <code>$TEXMFLOCAL</code>) or manually run <code>&quot;updmap -user&quot;</code> to tell TeX about the files in <code>$TEXMFHOME</code>. This latter option does, however, come with some caveats; see <i><a rel="nofollow" href="https://tug.org/texlive/scripts-sys-user.html">https://tug.org/texlive/scripts-sys-user.html</a></i>.  </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> <code>autoinst</code> tries hard to do The Right Thing (TM) by default, so you usually won&#8217;t need these options; but most aspects of its operation can be fine-tuned if you want to. </p>
<p> You may use either one or two dashes before options, and option names may be shortened to a unique prefix (e.g., <code>-encoding</code> may be abbreviated to <code>-enc</code> or even <code>-en</code>, but <code>-e</code> is ambiguous (it may mean either <code>-encoding</code> or <code>-extra</code>)).  </p>
<h3>General options</h3>
<dl>
<dt><code>-help</code></dt>
<dd> <p> Print a (relatively) short help text and exit. </p>
 </dd>
<dt><code>-dryrun</code></dt>
<dd> <p> Don&#8217;t generate output; just parse input fonts and write the results to the log file. </p>
 </dd>
<dt><code>-verbose</code></dt>
<dd> <p> Add more details to the log file. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print <code>autoinst</code>&#8216;s version number and exit. </p>
 </dd></dl>
<h3>Font creation options</h3>
<dl>
<dt><code>-encoding</code>=<i>encoding[,encoding]</i></dt>
<dd> <p> Generate the specified encoding(s) for the text fonts. Multiple encodings may be specified as a comma-separated list (without spaces!); the default choice of encodings is <code>&quot;OT1,LY1,T1&quot;</code>. </p>
<p> For each encoding argument, <code>autoinst</code> will first check if it is the filename of an encoding file, and if found it will use that; otherwise the argument is assumed to be the name of one of the built-in encodings. Currently <code>autoinst</code> comes with built-in support for the OT1, T1/TS1, LY1, LGR, T2A/B/C and T3/TS3 encodings. (These files are called <i>fontools_ot1.enc</i> etc. to avoid name clashes with other packages; the <i>fontools_</i> prefix may be omitted.) </p>
 </dd>
<dt><code>-ts1</code>/<code>-nots1</code></dt>
<dd> <p> Control the creation of TS1-encoded fonts. The default is <code>-ts1</code> if the text encodings (see <i>-encoding</i> above) include T1, <code>-nots1</code> otherwise. </p>
 </dd>
<dt><code>-lining</code>/<code>-nolining</code></dt>
<dd> <p> Control the creation of fonts with lining figures. The default is <code>-lining</code>. </p>
 </dd>
<dt><code>-oldstyle</code>/<code>-nooldstyle</code></dt>
<dd> <p> Control the creation of fonts with oldstyle figures. The default is <code>-oldstyle</code>. </p>
 </dd>
<dt><code>-proportional</code>/<code>-noproportional</code></dt>
<dd> <p> Control the creation of fonts with proportional figures. The default is <code>-proportional</code>. </p>
 </dd>
<dt><code>-tabular</code>/<code>-notabular</code></dt>
<dd> <p> Control the creation of fonts with tabular figures. The default is <code>-tabular</code>. </p>
 </dd>
<dt><code>-smallcaps</code>/<code>-nosmallcaps</code></dt>
<dd> <p> Control the creation of small caps fonts. The default is <code>-smallcaps</code>. </p>
 </dd>
<dt><code>-swash</code>/<code>-noswash</code></dt>
<dd> <p> Control the creation of swash fonts. The default is <code>-swash</code>. </p>
 </dd>
<dt><code>-titling</code>/<code>-notitling</code></dt>
<dd> <p> Control the creation of titling families. The default is <code>-titling</code>. </p>
 </dd>
<dt><code>-superiors</code>/<code>-nosuperiors</code></dt>
<dd> <p> Control the creation of fonts with superior characters. The default is <code>-superiors</code>. </p>
 </dd>
<dt><code>-inferiors</code> [ = <code>none</code> | <code>auto</code> | <code>subs</code> | <code>sinf</code> | <code>dnom</code> ]</dt>
<dd>  </dd>
<dt><code>-noinferiors</code></dt>
<dd> <p> The OpenType standard defines several kinds of digits that might be used as inferiors or subscripts: ``Subscripts&#8217;&#8216; (OpenType feature <code>&quot;subs&quot;</code>), ``Scientific Inferiors&#8217;&#8216; (<code>&quot;sinf&quot;</code>), and ``Denominators&#8217;&#8216; (<code>&quot;dnom&quot;</code>). This option allows the user to determine which of these styles <code>autoinst</code> should use for the inferior characters. Alternatively, the value ``auto&#8217;&#8216; tells <code>autoinst</code> to use the first value in <code>&quot;sinf&quot;</code>, <code>&quot;subs&quot;</code> or <code>&quot;dnom&quot;</code> that is supported by the font. Saying just <code>-inferiors</code> is equivalent to <code>-inferiors=auto</code>; otherwise the default is <code>-noinferiors</code>. </p>
<p> <i>If you specify a style of inferiors that isn&#8217;t present in the font, </i>autoinst <i> will fall back to its default behaviour of not creating fonts with inferiors at all; it won&#8217;t try to substitute one of the other styles.</i> </p>
 </dd>
<dt><code>-fractions</code>/<code>-nofractions</code></dt>
<dd> <p> Control the creation of fonts with numerators and denominators. The default is <code>-nofractions</code>. </p>
 </dd>
<dt><code>-ligatures</code>/<code>-noligatures</code></dt>
<dd> <p> Some fonts contain glyphs for the standard f-ligatures (ff, fi, fl, ffi, ffl), but don&#8217;t provide a <code>&quot;liga&quot;</code> feature to access these. This option tells <code>autoinst</code> to add extra <code>&quot;LIGKERN&quot;</code> rules to the generated fonts to enable the use of these ligatures. The default is <code>-ligatures</code>, except for typewriter fonts. </p>
<p> Specify <code>-noligatures</code> to disable generation of ligatures even for fonts that do contain a <code>&quot;liga&quot;</code> feature. </p>
 </dd>
<dt><code>-ornaments</code>/<code>-noornaments</code></dt>
<dd> <p> Control the creation of ornament fonts. The default is <code>-ornaments</code>. </p>
 </dd>
<dt><code>-serif</code>/<code>-sanserif</code>/<code>-typewriter</code></dt>
<dd> <p> Install the font as a serif, sanserif or typewriter font, respectively. This changes how you access the font in LaTeX: with <code>&quot;\rmfamily&quot;</code>/<code>&quot;\textrm&quot;</code>, <code>&quot;\sffamily&quot;</code>/<code>&quot;\textsf&quot;</code> or <code>&quot;\ttfamily&quot;</code>/<code>&quot;\texttt&quot;</code>. </p>
<p> Installing the font as a typewriter font will cause two further changes: it will &#8211; by default &#8211; turn off the use of f-ligatures (though this can be overridden with the <i>-ligatures</i> option), and it will disable hyphenation for this font. This latter effect cannot be re-enabled in <code>autoinst</code>; if you want typewriter text to be hyphenated, use the <i>hyphenat</i> package. </p>
<p> If none of these options is specified, <code>autoinst</code> tries to guess: if the font&#8217;s filename contains the string ``mono&#8217;&#8216; or if the field <code>&quot;isFixedPitch&quot;</code> in the font&#8217;s <code>&quot;post&quot;</code> table is True, it will select <code>-typewriter</code>; else if the filename contains ``sans&#8217;&#8216; it will select <code>-sanserif</code>; otherwise it will opt for <code>-serif</code>. </p>
 </dd>
<dt><code>-math</code></dt>
<dd> <p> Tells <code>autoinst</code> to create basic math fonts (see above). </p>
 </dd>
<dt><code>-mathspacing</code>=<i>amount</i></dt>
<dd> <p> Letterspace each character in the math fonts by <i>amount</i> units, where 1000 units equal one em. In my opinion, many text fonts benefit from letterspacing by 50 to 100 units when used in maths; some fonts need even more. Use your own judgement! </p>
 </dd></dl>
<h3>Output options</h3>
<dl>
<dt><code>-t1suffix</code> [ = <i></i><i>SUFFIX</i><i></i> ]</dt>
<dd> <p> Tell <code>autoinst</code> to modify the font names of all generated Type1-fonts, by adding <i></i><i>SUFFIX</i><i></i> to the family name. If you use this option without specifying a <i></i><i>SUFFIX</i><i></i> value, <code>autoinst</code> will use the value ``PS&#8217;&#8216;. The default behaviour when this option is not given is to not modify font names at all. </p>
<p> See also ``OpenType fonts and licensing issues&#8217;&#8216; in ``WARNINGS AND CAVEATS&#8217;&#8216; above. </p>
 </dd>
<dt><code>-target</code>=<i></i><i>DIRECTORY</i><i></i></dt>
<dd> <p> Install all generated files into the TEXMF tree at <i></i><i>DIRECTORY</i><i></i>. </p>
<p> By default, <code>autoinst</code> searches the <code>$TEXMFLOCAL</code> and <code>$TEXMFHOME</code> trees and installs all files into the first user-writable TEXMF tree it finds. If <code>autoinst</code> cannot find such a user-writable directory (which shouldn&#8217;t happen, since <code>$TEXMFHOME</code> is supposed to be user-writable) it will print a warning message and put all files into the subdirectory <code>&quot;autoinst_output/&quot;</code> of the current directory. It&#8217;s then up to the user to move the generated files to a better location and update all relevant databases (usually by calling <i>texhash</i> and <i>updmap</i>). </p>
 </dd>
<dt><code>-vendor</code>=<i></i><i>VENDOR</i><i></i></dt>
<dd>  </dd>
<dt><code>-typeface</code>=<i></i><i>TYPEFACE</i><i></i></dt>
<dd> <p> These options are equivalent to <i>otftotfm</i>&#8216;s <i> --vendor</i> and <i> --typeface</i> options: they change the ``vendor&#8217;&#8216; and ``typeface&#8217;&#8216; parts of the names of the subdirectories in the TEXMF tree where generated files will be stored. The default values are ``lcdftools&#8217;&#8216; and the font&#8217;s FontFamily name. These options change <i>only</i> directory names, not the names of any generated files. </p>
 </dd>
<dt><code>-logfile</code>=<i>filename</i></dt>
<dd> <p> Write log data to <i>filename</i> instead of the default <i>&lt;fontfamily&gt;.log</i>. If the file already exists, <code>autoinst</code> appends to it; it doesn&#8217;t overwrite an existing file. </p>
 </dd></dl>
<h3>Specialist options</h3>
<dl>
<dt><code>-defaultlining</code>/<code>-defaultoldstyle</code></dt>
<dd>  </dd>
<dt><code>-defaulttabular</code>/<code>-defaultproportional</code></dt>
<dd> <p> Tell <code>autoinst</code> which figure style is the current font family&#8217;s default (i.e., which figures you get when you don&#8217;t specify any OpenType features). </p>
<p> <i>Don&#8217;t use these options unless you are certain you need them!</i> They are only needed for fonts that don&#8217;t provide OpenType features for their default figure style; and even in that case, <code>autoinst</code>&#8216;s default values (<code>-defaultlining</code> and <code>-defaulttabular</code>) are usually correct. </p>
 </dd>
<dt><code>-nfssweight</code>=<i>code</i>=<i>weight</i></dt>
<dd>  </dd>
<dt><code>-nfsswidth</code>=<i>code</i>=<i>width</i></dt>
<dd> <p> Map the NFSS code <i>code</i> to the given weight or width, overriding the built-in tables. Each of these options may be given multiple times, to override more than one NFSS code. Example: to map the <code>&quot;ul&quot;</code> code to the ``Thin&#8217;&#8216; weight, use <code>&quot;-nfssweight=ul=thin&quot;</code>. To inhibit the use of the <code>&quot;ul&quot;</code> code completely, use <code>&quot;-nfssweight=ul=&quot;</code>. </p>
 </dd>
<dt><code>-extra</code>=<i>extra options</i></dt>
<dd> <p> Pass <i>extra options</i> to the commands for <i>otftotfm</i>. To prevent <i>extra options</i> from accidentily being interpreted as options to <code>autoinst</code>, they should be properly quoted. </p>
 </dd>
<dt><code>-nofigurekern</code></dt>
<dd> <p> Some fonts provide kerning pairs for tabular figures. This is very probably not what you want (e.g., numbers in tables won&#8217;t line up exactly). This option adds extra <i> --ligkern</i> options to the commands for <i>otftotfm</i> to suppress such kerns. Note that this option leads to very long commands (it adds one hundred <i> --ligkern</i> options), which may cause problems on some systems; hence it is not active by default. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> Eddie Kohler&#8217;s <code>TypeTools</code> and <code>T1Utils</code> (<i><a rel="nofollow" href="http://www.lcdf.org/type">http://www.lcdf.org/type</a></i>). </p>
<p> <code>Perl</code> can be obtained from <i><a rel="nofollow" href="http://www.perl.org">http://www.perl.org</a></i>; it is included in most Linux distributions. For Windows, try ActivePerl (<i><a rel="nofollow" href="http://www.activestate.com">http://www.activestate.com</a></i>) or Strawberry Perl (<i><a rel="nofollow" href="http://strawberryperl.com">http://strawberryperl.com</a></i>). </p>
<p> <code>LuaTeX</code> (<i><a rel="nofollow" href="http://www.luatex.org">http://www.luatex.org</a></i>) and <code>XeTeX</code> (<i><a rel="nofollow" href="http://www.tug.org/xetex">http://www.tug.org/xetex</a></i>) are Unicode-aware TeX engines that can use OpenType fonts directly, without any (La)TeX-specific support files. </p>
<p> The <code>FontPro</code> project (<i><a rel="nofollow" href="https://github.com/sebschub/FontPro">https://github.com/sebschub/FontPro</a></i>) offers very complete LaTeX support (even for typesetting maths) for Adobe&#8217;s Minion Pro, Myriad Pro and Cronos Pro font families.  </p>
<h2>AUTHOR</h2>
<p> Marc Penninga (<i>marcpenninga [at] gmail.com</i>) </p>
<p> When sending a bug report, please give as much relevant information as possible; this usually includes (but may not be limited to) the log file (please add the <i>-verbose</i> command-line option, for extra info). If you see any error messages, please include these <i>verbatim</i>; don&#8217;t paraphase.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2022 Marc Penninga.  </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. A copy of the text of the GNU General Public License is included in the <i>fontools</i> distribution; see the file <i>GPLv2.txt</i>.  </p>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  </p>
<h2>VERSION</h2>
<p> This document describes <code>autoinst</code> version 20220124.  </p>
<h2>RECENT CHANGES</h2>
<p> (See the source for the full story, all the way back to 2005.) </p>
<dl>
<dt><i>2021-11-15</i></dt>
<dd> <p> Bugfix: font info parsing now works for Adobe Source Serif 4. </p>
 </dd>
<dt><i>2021-07-21</i></dt>
<dd> <p> Bugfixes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>-</dt>
<dd> <p> Yet another problem with argument quoting on Windows. </p>
 </dd>
<dt>-</dt>
<dd> <p> Selecting numerator/denominator fonts didn&#8217;t work as documented. </p>
 </dd>
<dt>-</dt>
<dd> <p> Font info parsing failed for Microsoft Sitka and LucasFonts Thesis. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><i>2021-04-01</i></dt>
<dd> <p> The <i>-encoding</i> option now also accepts filenames of encoding files in directories other than the current directory. Directory names containing spaces do (or at least should) also work. </p>
 </dd>
<dt><i>2020-12-18</i></dt>
<dd> <p> Fixed a problem with files not being found on Windows. Added extra <code>&quot;--unicoding&quot;</code> options to prevent getting lowercase f-ligatures in smallcaps for some buggy fonts. Optimized font info parsing for DTL and TypeBy font families. Cleaned up the code for better maintainability. </p>
 </dd>
<dt><i>2020-07-29</i></dt>
<dd> <p> Some changes in the generated <i>sty</i> and <i>fd</i> files, to improve compatibility with the <i>microtype</i> package. Made sure that <i>pfb</i> fonts are always generated whenever the input fonts are in <i>otf</i> format. Added the <i>-t1suffix</i> command-line option, to modify the font and file names of those generated Type1 fonts. </p>
 </dd>
<dt><i>2020-06-19</i></dt>
<dd> <p> Added the <code>&quot;nomathgreek&quot;</code> option to generated style files. Reorganized the generated style files to make them more standards-conforming. </p>
 </dd>
<dt><i>2020-05-27</i></dt>
<dd> <p> Added basic (and still somewhat experimental) math support. Implemented the <code>&quot;scale=MatchLowercase&quot;</code> option value in the generated style files. ``Wide&#8217;&#8216; fonts are mapped to the <code>&quot;sx&quot;</code> NFSS code instead of <code>&quot;x&quot;</code>, to cater for League Mono Variable&#8217;s Wide and Extended widths. The generated style files now use <code>&quot;\textsup&quot;</code> and <code>&quot;\textinf&quot;</code> instead of the more cryptic <code>&quot;\textsu&quot;</code> and <code>&quot;\textin&quot;</code> to access superior and inferior characters (though the old forms are retained for backwards compatibility). </p>
 </dd>
<dt><i>2020-05-11</i></dt>
<dd> <p> When present, use encoding files in the current working directory in preference of the ones that come with <code>autoinst</code>. Changed the way ornament fonts are created; ornament glyphs are now always included in the position chosen by the font&#8217;s designer. </p>
 </dd>
<dt><i>2020-04-28</i></dt>
<dd> <p> Fix a bug where the first font argument would be mistaken for an argument to <i>-inferiors</i>. </p>
 </dd>
<dt><i>2020-01-29</i></dt>
<dd> <p> Don&#8217;t create empty subdirectories in the target TEXMF tree. </p>
 </dd></dl>
