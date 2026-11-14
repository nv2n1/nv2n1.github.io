---
title: "pstoedit(1)"
name: "pstoedit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstoedit/"
description: "pstoedit – a tool converting PostScript and PDF files into various vector graphic formats"
---

<h2 class="name">NAME</h2>
<p> pstoedit &#8211; a tool converting PostScript and PDF files into various vector graphic formats</p>
<h2>SYNOPSIS</h2>
<h3>FROM THE COMMAND SHELL</h3>
<p> pstoedit [<code>-v -help</code>] </p>
<p> pstoedit [<code>-include</code><i> name of a PostScript file to be included</i>] [<code>-df</code><i> font name</i>] [<code>-nomaptoisolatin1</code>] [<code>-dis</code>] [<code>-pngimage</code><i> filename</i>] [<code>-q</code>] [<code>-nq</code>] [<code>-nc</code>] [<code>-mergelines</code>] [<code>-filledrecttostroke</code>] [<code>-mergetext</code>] [<code>-dt</code>] [<code>-adt</code>] [<code>-ndt</code>] [<code>-dgbm</code>] [<code>-correctdefinefont</code>] [<code>-pti</code>] [<code>-pta</code>] [<code>-xscale</code><i> number</i>] [<code>-yscale</code><i> number</i>] [<code>-xshift</code><i> number</i>] [<code>-yshift</code><i> number</i>] [<code>-centered</code>] [<code>-minlinewidth</code><i> number</i>] [<code>-pagenumberformat</code><i> page number format specification</i>] [<code>-split</code>] [<code>-v</code>] [<code>-vl</code><i> </i>] [<code>-usebbfrominput</code>] [<code>-ssp</code>] [<code>-sfill</code>] [<code>-uchar</code><i> character</i>] [<code>-nb</code>] [<code>-rdb</code>] [<code>-page</code><i> page number</i>] [<code>-flat</code><i> flatness factor</i>] [<code>-sclip</code>] [<code>-ups</code>] [<code>-rgb</code>] [<code>-useagl</code>] [<code>-noclip</code>] [<code>-t2fontsast1</code>] [<code>-keep</code>] [<code>-debugfonthandling</code>] [<code>-gstest</code>] [<code>-fakedateandversion</code>] [<code>-nfr</code>] [<code>-glyphs</code>] [<code>-useoldnormalization</code>] [<code>-rotate</code><i> angle (0-360)</i>] [<code>-fontmap</code><i> name of font map file for pstoedit</i>] [<code>-pagesize</code><i> page format</i>] [<code>-help</code>] [<code>-gs</code><i> path to the Ghostscript executable/DLL</i>] [<code>-bo</code>] [<code>-psarg</code><i> argument string</i>] [<code>-pslanguagelevel</code><i> PostScript Language Level 1, 2, or 3 to be used.</i>] <code>-f</code><i> &quot;format[:options]&quot;</i> [<code>-gsregbase</code><i> Ghostscript base registry path</i>] [ inputfile [outputfile] ] </p>
<h3>FROM GSVIEW</h3>
<p> Pstoedit can be called from within gsview via &quot;<code>Edit | Convert to vector format</code>&quot; </p>
<h3>FROM PROGRAMS THAT SUPPORT THE ALDUS GRAPHIC IMPORT FILTER INTERFACE</h3>
<p> pstoedit can also be used as PostScript and PDF graphic import filter for several programs including MS Office, PaintShop-Pro and PhotoLine. See <code><a rel="nofollow" href="http://www.pstoedit.net/importps/">http://www.pstoedit.net/importps/</a></code> for more details. </p>
<h2>DESCRIPTION</h2>
<h3>RELEASE LEVEL</h3>
<p> This manpage documents release 3.78 of pstoedit. </p>
<h3>USE</h3>
<p> pstoedit converts PostScript and PDF files to various vector graphic formats. The resulting files can be edited or imported into various drawing packages. Type </p>
<p> <code>pstoedit -help</code> </p>
<p> to get a list of supported output formats. Pstoedit comes with a large set of format drivers integrated in the binary. Additional drivers can be installed as plugins and are available via <code><a rel="nofollow" href="http://www.pstoedit.net/plugins/">http://www.pstoedit.net/plugins/</a></code>. Just copy the plugins to the same directory where the pstoedit binary is installed or &#8211; under Unix like systems only &#8211; alternatively into the lib directory parallel to the bin directory where pstoedit is installed. </p>
<p> However, unless you also get a license key for the plugins, the additional drivers will slightly distort the resulting graphics. See the documentation provided with the plugins for further details. </p>
<h3>PRINCIPLE OF CONVERSION</h3>
<p> pstoedit works by redefining some basic painting operators of PostScript, e.g. <code>stroke</code> or <code>show</code> (bitmaps drawn by the image operator are not supported by all output formats.) After redefining these operators, the PostScript or PDF file that needs to be converted is processed by a PostScript interpreter, e.g., Ghostscript (<i><a href="/docs/linux/man/1-gs/">gs</a></i>(1)). You normally need to have a PostScript interpreter installed in order to use this program. However, you can perform some &quot;back end only&quot; processing of files following the conventions of the pstoedit intermediate format by specifying the <code>-bo</code> option. See &quot;Available formats and their specific options&quot; below. </p>
<p> The output that is written by the interpreter due to the redefinition of the drawing operators is a sort of &#8216;flat&#8217; PostScript file that contains only simple operations like moveto, lineto, show, etc. You can look at this file using the <code>-f debug</code> option. </p>
<p> This output is read by end-processing functions of pstoedit and triggers the drawing functions in the selected output format driver sometime called also &quot;backend&quot;. </p>
<h3>NOTES</h3>
<p> If you want to process PDF files directly, your PostScript interpreter must provide this feature, as does Ghostscript. Aladdin Ghostscript is recommended for processing PDF and PostScript files. </p>
<h2>OPTIONS</h2>
<h3>GENERAL OPTIONS</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-include</code><i> name of a PostScript file to be included</i>]</p>
<dd>
&nbsp;This option allows specifying an additional PostScript file that will be executed just before the normal input is read. This is helpful for including specific page settings or for disabling potentially unsafe PostScript operators, e.g., file, renamefile, or deletefile.&nbsp;</dl>
<dl>
<dt>[<code>-xscale</code><i> number</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-yscale</code><i> number</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-xshift</code><i> number</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-yshift</code><i> number</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-centered</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-minlinewidth</code><i> number</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-pagenumberformat</code><i> page number format specification</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-split</code>]</p>
<dd>
&nbsp;Create a new file for each page of the input. For this the output filename must contain a&nbsp;%d which is replaced with the current page number. This option is automatically switched on for output formats that do not support multiple pages within one file, e.g. fig or gnuplot.&nbsp;</dl>
<dl>
<dt>[<code>-usebbfrominput</code>]</p>
<dd>
&nbsp;If specified, pstoedit uses the BoundingBox as is&nbsp;(hopefully)&nbsp;found in the input file instead of one that is calculated by its own.&nbsp;</dl>
<dl>
<dt>[<code>-page</code><i> page number</i>]</p>
<dd>
&nbsp;Select a single page from a multi-page PostScript or PDF file.&nbsp;</dl>
<dl>
<dt>[<code>-rgb</code>]</p>
<dd>
&nbsp;Since version 3.30 pstoedit uses the CMYK colors internally. The -rgb option turns on the old behavior to use RGB values.&nbsp;</dl>
<dl>
<dt>[<code>-useagl</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-noclip</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-rotate</code><i> angle (0-360)</i>]</p>
<dd>
&nbsp;Rotate image by angle.&nbsp;</dl>
<dl>
<dt>[<code>-pagesize</code><i> page format</i>]</p>
<dd>
&nbsp;set page size for output medium.&nbsp; This option sets the page size for the output medium. Currently this is just used by the libplot output format driver, but might be used by other output format drivers in future. The page size is specified in terms of the usual page size names, e.g. letter or a4.</dl>
<dl>
<dt>[<code>-help</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-gs</code><i> path to the Ghostscript executable/DLL</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-bo</code>]</p>
<dd>
&nbsp;You can run backend processing only&nbsp;(without the PostScript interpreter frontend)&nbsp;by first running&nbsp;<code>pstoedit</code> <code>-f dump</code> <i>infile</i> <i>dumpfile</i> and then running <code>pstoedit</code> <code>-f</code><i> format</i> <code>-bo</code> <i>dumpfile</i> <i>outfile</i>.</dl>
<dl>
<dt>[<code>-psarg</code><i> argument string</i>]</p>
<dd>
&nbsp;The string given with this option is passed directly to Ghostscript when Ghostscript is called to process the PostScript file for pstoedit. For example: <code>-psarg</code><code> &quot;</code><code>-r300x300</code><code>&quot;</code>. This causes the resolution to be changed to 300&#215;300 dpi. (With older versions of Ghostscript, changing the resolution this way has an effect only if the <code>-dis</code> option is given.) If you want to pass multiple options to Ghostscript you can use multiple -psarg options <code>-psarg opt1</code> <code>-psarg opt2</code> <code>-psarg opt2</code>. See the Ghostscript manual for other possible options.</dl>
<dl>
<dt>[<code>-pslanguagelevel</code><i> PostScript Language Level 1, 2, or 3 to be used.</i>]</p>
<dd>
&nbsp;.PP</p>
<dt><code>-f</code><i> &quot;format[:options]&quot;</i></p>
<dd>
&nbsp;target output format recognized by pstoedit. Since other format drivers can be loaded dynamically, type pstoedit -help to get a full list of formats. See &quot;Available formats and their specific options&quot; below for an explanation of the [<i>:options</i>] to <code>-f</code> format. If the format option is not given, pstoedit tries to guess the target format from the suffix of the output filename. However, in a lot of cases, this is not a unique mapping and hence pstoedit demands the <code>-f</code> option.</dl>
<dl>
<dt>[<code>-gsregbase</code><i> Ghostscript base registry path</i>]</p>
<dd>
&nbsp;registry path to use as a base path when searching Ghostscript interpreter.&nbsp; This option provides means to specify a registry key under HKLM/Software where to search for GS interpreter key, version and GS_DLL / GS_LIB values. Example: &quot;-gsregbase MyCompany&quot; means that HKLM/Software/MyCompany/GPL Ghostscript would be searched instead of HKLM/Software/GPL Ghostscript.</dl>
<h3>TEXT AND FONT HANDLING RELATED OPTIONS</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-df</code><i> font name</i>]</p>
<dd>
&nbsp;Sometimes fonts embedded in a PostScript program do not have a fontname. For example, this happens in PostScript files generated by&nbsp;<i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1). In such a case pstoedit uses a replacement font. The default for this is Courier. Another font can be specified using the <code>-df</code> option. <code>-df Helvetica</code> causes all unnamed fonts to be replaced by Helvetica.</dl>
<dl>
<dt>[<code>-nomaptoisolatin1</code>]</p>
<dd>
&nbsp;Normally pstoedit maps all character codes to the ones defined by the ISO Latin1 encoding. If you specify <code>-nomaptoisolatin1</code> then the encoding from the input PostScript is passed unchanged to the output. This may result in strange text output but on the other hand may be the only way to get some fonts converted appropriately. Try what fits best to your concrete case.</dl>
<dl>
<dt>[<code>-pngimage</code><i> filename</i>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-dt</code>]</p>
<dd>
&nbsp;draw text. Text is drawn as polygons. This might produce a large output file. This option is automatically switched on if the selected output format does not support text, e.g.&nbsp;<i><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></i>(1).</dl>
<dl>
<dt>[<code>-adt</code>]</p>
<dd>
&nbsp;automatic draw text. This option turns on the&nbsp;<code>-dt</code> option selectively for fonts that seem to be no normal text fonts, e.g. Symbol.</dl>
<dl>
<dt>[<code>-ndt</code>]</p>
<dd>
&nbsp;never draw text. Fully disable the heuristics used by pstoedit to decide when to&nbsp;&quot;draw&quot;&nbsp;text instead of showing it as text. This may produce incorrect results, but in some cases it might nevertheless be useful.&nbsp;&quot;Use at own risk&quot;.&nbsp;</dl>
<dl>
<dt>[<code>-dgbm</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-correctdefinefont</code>]</p>
<dd>
&nbsp;Some PostScript files, e.g. such as generated by ChemDraw, use the PostScript definefont operator in a way that is incompatible with pstoedit&#8217;s assumptions. The new font is defined by copying an old font without changing the FontName of the new font. When this option is applied, some&nbsp;&quot;patches&quot;&nbsp;are done after a definefont in order to make it again compatible with pstoedit&#8217;s assumptions. This option is not enabled by default, since it may break other PostScript files. It is tested only with ChemDraw generated files.&nbsp;</dl>
<dl>
<dt>[<code>-pti</code>]</p>
<dd>
&nbsp;precision text. Normally a text string is drawn as it occurs in the input file. However, in some situations, this might produce wrongly positioned characters. This is due to limitations in most output formats of pstoedit. They cannot represent text with arbitrary inter-letter spacing which is easily possible in PDF and PostScript. With&nbsp;<code>-pta</code>, each character of a text string is placed separately. With <code>-pti</code>, this is done only in cases when there is a non zero inter-letter spacing. The downside of &quot;precision text&quot; is a bigger file size and hard to edit text.</dl>
<dl>
<dt>[<code>-pta</code>]</p>
<dd>
&nbsp;see -pti&nbsp;</dl>
<dl>
<dt>[<code>-uchar</code><i> character</i>]</p>
<dd>
&nbsp;Sometimes pstoedit cannot map a character from the encoding used by the PostScript file to the font encoding of the target format. In this case pstoedit replaces the input character by a special character in order to show all the places that could not be mapped correctly. The default for this is a&nbsp;&quot;#&quot;. Using the&nbsp;<code>-uchar</code> option it is possible to specify another character to be used instead. If you want to use a space, use -uchar &quot; &quot;.</dl>
<dl>
<dt>[<code>-t2fontsast1</code>]</p>
<dd>
&nbsp;Handle Type 2 fonts same as Type 1. Type 2 fonts sometimes occur as embedded fonts within PDF files. In the default mode, text using such fonts is drawn as polygons since pstoedit assumes that such a font is not available on the user&#8217;s machine. If this option is set, pstoedit assumes that the internal encoding follows the same as for a standard font and generates normal text output. This assumption may not be true in all cases. But it is nearly impossible for pstoedit to verify this assumption &#8211; it would have to do a sort of OCR.&nbsp;</dl>
<dl>
<dt>[<code>-nfr</code>]</p>
<dd>
&nbsp;In normal mode pstoedit replaces bitmap fonts with a font as defined by the&nbsp;<code>-df</code> option. This is done, because most output formats cannot handle such fonts. This behavior can be switched off using the <code>-nfr</code> option but then it strongly depends on the application reading the generated file whether the file is usable and correctly interpreted or not. Any problems are then out of control of pstoedit.</dl>
<dl>
<dt>[<code>-glyphs</code>]</p>
<dd>
&nbsp;pass glyph names to the output format driver. So far no output format driver really uses the glyph names, so this does not have any effect at the moment. It is a preparation for future work.&nbsp;</dl>
<dl>
<dt>[<code>-useoldnormalization</code>]</p>
<dd>
&nbsp;Just use this option in case the new heuristic introduced in 3.5 does not produce correct results &#8211; however, this normalization of font encoding will always be a best-effort approach since there is no real general solution to it with reasonable effort&nbsp;</dl>
<dl>
<dt>[<code>-fontmap</code><i> name of font map file for pstoedit</i>]</p>
<dd>
&nbsp;The font map is a simple text file containing lines in the following format:
</dl>
<p> document_font_name target_font_name<br />
 Lines beginning with % are considerd comments.<br />
 For font names with spaces use the &quot;font name with spaces&quot; notation. </p>
<p> If a target_font_name starts with /, it is regarded as alias to a former entry. </p>
<p> Each font name found in the document is checked against this mapping and if there is a corresponding entry, the new name is used for the output. </p>
<p> If the <code>-fontmap</code> option is not specified, pstoedit automatically looks for the file <i>drivername</i>.fmp in the installation directory and uses that file as a default fontmap file if available. The installation directory is: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
</dl>
<dl>
<dt><code>*</code></p>
<dd> MS Windows: The same directory where the pstoedit executable is located</p>
<dl>
<dt>
<dd>
</dl>
<dt><code>*</code></p>
<dd> Unix:<br />
 The default installation directory. If it fails, then &lt;<i>The directory where the pstoedit executable is located</i>&gt; /../lib/</p>
<dl>
<dt>
<dd>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
<p> The mpost.fmp in the misc directory of the pstoedit distribution is a sample map file with mappings from over 5000 PostScript font names to their TeX equivalents. This is useful because MetaPost is frequently used with TeX/LaTeX and those programs do not use standard font names. This file and the MetaPost output format driver are provided by Scott Pakin (<code>scott+ps2ed_AT_pakin.org</code>). Another example is wemf.fmp to be used under Windows. See the misc directory of the pstoedit source distribution. After loading the implicit (based on driver name) or explicit (based on the -fontmap option) font map file, a system specific map file is searched and loaded from the installation directory (unix.fmp or windows.fmp). This file can be used to redirect certain fonts to system specific names using the /AliasName notation described above. </p>
</dl>
<h3>DRAWING RELATED OPTIONS</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-nc</code>]</p>
<dd>
&nbsp;no curves.&nbsp; Normally pstoedit tries to keep curves from the input and transfers them to the output if the output format supports curves. If the output format does not support curves, then pstoedit replaces curves by a series of lines (see also <code>-flat</code> option). However, in some cases the user might wish to have this behavior also for output formats that originally support curves. This can be forced via the <code>-nc</code> option.</dl>
<dl>
<dt>[<code>-mergelines</code>]</p>
<dd>
&nbsp;Some output formats permit the representation of filled polygons with edges that are in a different color than the fill color. Since PostScript does not support this by the standard drawing primitives directly, drawing programs typically generate two objects&nbsp;(the outline and the filled polygon)&nbsp;into the PostScript output. pstoedit is able to recombine these, if they follow each other directly and you specify <code>-mergelines</code>. However, this merging is not supported by all output formats due to restrictions in the target format.</dl>
<dl>
<dt>[<code>-filledrecttostroke</code>]</p>
<dd>
&nbsp;Rectangles filled with a solid color can be converted to a stroked line with a width that corresponds to the width of the rectangle. This is of primary interest for output formats which do not support filled polygons at all. But it is restricted to rectangles only, i.e. it is not supported for general polygons&nbsp;</dl>
<dl>
<dt>[<code>-mergetext</code>]</p>
<dd>
&nbsp;In order to produce nice looking text output, programs producing PostScript files often split words into smaller pieces which are then placed individually on adjacent positions. However, such split text is hard to edit later on and hence it is sometime better to recombine these pieces again to form a word&nbsp;(or even sequence of words). For this pstoedit implements some heuristics about what text pieces are to be considered parts of a split word. This is based on the geometrical proximity of the different parts and seems to work quite well so far. But there are certainly cases where this simple heuristic fails. So please check the results carefully.&nbsp;</dl>
<dl>
<dt>[<code>-ssp</code>]</p>
<dd>
&nbsp;simulate subpaths.&nbsp; Several output formats do not support PostScript paths containing subpaths, i.e. paths with intermediate movetos. In the normal case, each subpath is treated as an independent path for such output formats. This can lead to bad looking results. The most common case where this happens is if you use the <code>-dt</code> option and show some text with letters like e, o, or b, i.e. letters that have a &quot;hole&quot;. When the <code>-ssp</code> option is set, pstoedit tries to eliminate these problems. However, this option is CPU time intensive!</dl>
<dl>
<dt>[<code>-sfill</code>]</p>
<dd>
&nbsp;simulate filling by individual strokes.&nbsp;</dl>
<dl>
<dt>[<code>-flat</code><i> flatness factor</i>]</p>
<dd>
&nbsp;If the output format does not support curves in the way PostScript does or if the&nbsp;<code>-nc</code> option is specified, all curves are approximated by lines. Using the <code>-flat</code> option one can control this approximation. This parameter is directly converted to a PostScript <code>setflat</code> command. Higher numbers, e.g. 10 give rougher, lower numbers, e.g. 0.1, give finer approximations.</dl>
<dl>
<dt>[<code>-sclip</code>]</p>
<dd>
&nbsp;simulate clipping.&nbsp; Most output formats of pstoedit do not have native support for clipping. For that pstoedit offers an option to perform the clipping of the graphics directly without passing the clippath to the output driver. However, this results in curves being replaced by a lot of line segments and thus larger output files. So use this option only if your output looks different from the input due to clipping. In addition, this &quot;simulated clipping&quot; is not exactly the same as defined in PostScript. There might be lines drawn at double size. Also clipping of text is not supported unless you also use the <code>-dt</code> option.</dl>
<h3>DEBUG OPTIONS</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-dis</code>]</p>
<dd>
&nbsp;Open a display during processing by Ghostscript. Some files only work correctly this way.&nbsp;</dl>
<dl>
<dt>[<code>-q</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-nq</code>]</p>
<dd>
&nbsp;no exit from the PostScript interpreter. Normally Ghostscript exits after processing the pstoedit input-file. For debugging it can be useful to avoid this. If you do, you will have to type quit at the GS&gt;&nbsp;prompt to exit from Ghostscript.&nbsp;</dl>
<dl>
<dt>[<code>-v</code>]</p>
<dd>
&nbsp;Switch on verbose mode. Some additional information is shown during processing.&nbsp;</dl>
<dl>
<dt>[<code>-vl</code><i> </i>]</p>
<dd>
&nbsp;Switch on verbose mode with a given level. Some additional information is shown during processing.&nbsp;</dl>
<dl>
<dt>[<code>-nb</code>]</p>
<dd>
&nbsp;Since version 3.10 pstoedit uses the -dDELAYBIND option when calling Ghostscript. Previously the -dNOBIND option was used instead but that sometimes caused problems if a user&#8217;s PostScript file overloaded standard PostScript operator with totally new semantic, e.g. lt for lineto instead of the standard meaning of &quot;less than&quot;. Using <code>-nb</code> the old style can be activated again in case the -dDELAYBIND gives different results as before. In such a case please also contact the author.</dl>
<dl>
<dt>[<code>-rdb</code>]</p>
<dd>
&nbsp;Since version 3.10 pstoedit uses the -dDELAYBIND option when calling Ghostscript. But in version 9.22 of GhostScript, that option is not supported anymore because of security reasons. As a fallback, that version provides the REALLYDELAYBIND option and pstoedit can use this if you supply the <code>-rdb</code> option. Use this with caution as it might open security risks, e.g. a PostScript file injecting some malicious code into PostScript standard operators. However, not using this option can cause some of the PostScript drawings operations to be not seen by pstoedit, hence causing missing artefacts in the output. Later versions of Ghostscript will probably support -dDELAYBIND again. But also in that case the security risk remains. So be careful with what files you process with pstoedit and Ghostscript.</dl>
<dl>
<dt>[<code>-ups</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-keep</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-debugfonthandling</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-gstest</code>]</p>
<dd>
&nbsp;.PP</p>
<dt>[<code>-fakedateandversion</code>]</p>
<dd>
&nbsp;.PP</dl>
<h3>INPUT AND OUTFILE FILE ARGUMENTS</h3>
<p> [ inputfile [outputfile] ] </p>
<p> If neither an input nor an output file is given as argument, pstoedit works as filter reading from standard input and writing to standard output. The special filename &quot;-&quot; can also be used. It represents standard input if it is the first on the command line and standard output if it is the second. So &quot;pstoedit &#8211; output.xxx&quot; reads from standard input and writes to output.xxx </p>
<h2>AVAILABLE FORMATS AND THEIR SPECIFIC OPTIONS</h2>
<p> pstoedit allows passing individual options to an output format driver. This is done by appending all options to the format specified after the <code>-f</code> option. The format specifier and its options must be separated by a colon (:). If more than one option needs to be passed to the output format driver, the whole argument to <code>-f</code> must be enclosed within double-quote characters, thus: </p>
<p> <code>-f</code><i> &quot;format[:option option &#8230;]&quot;</i> </p>
<p> To see which options are supported by a specific format, type: <code>pstoedit -f format:-help</code> </p>
<p> The following description of the different formats supported by pstoedit is extracted from the source code of the individual drivers. </p>
<h3>Format group: psf ps debug dump gs ps2ai</h3>
<p> This group consists of the following variants:</p>
<dl>
<dt>psf:</p>
<dd> Flattened PostScript (no curves).</p>
<dt>ps:</p>
<dd> Simplified PostScript with curves.</p>
<dt>debug:</p>
<dd> for test purposes.</p>
<dt>dump:</p>
<dd> for test purposes (same as debug).</p>
<dt>gs:</p>
<dd> any device that Ghostscript provides &#8211; use gs:format, e.g. gs:pdfwrite.</p>
<dt>ps2ai:</p>
<dd> Adobe Illustrator via ps2ai.ps of Ghostscript.</dl>
<p> No format specific options</p>
<h3>sample &#8211; sample driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</h3>
<p> This is a long description for the sample driver </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-sampleoption</code><i> integer</i>]</p>
<dd>
&nbsp;just an example&nbsp;</dl>
<h3>idraw &#8211; Interviews draw format (EPS)</h3>
<p> No format specific options</p>
<h3>Format group: fig xfig tfig</h3>
<p> This group consists of the following variants:</p>
<dl>
<dt>fig:</p>
<dd> .fig format for xfig.</p>
<dt>xfig:</p>
<dd> .fig format for xfig.</p>
<dt>tfig:</p>
<dd> .fig format for xfig &#8211; test only version.</dl>
<p> The xfig format driver supports special fontnames, which may be produced by using a fontmap file. The following types of names are supported: </p>
<pre>
General notation:
&quot;PostScript Font Name&quot; ((LaTeX|PostScript|empty)(::special)::)XFigFontName
Examples:
Helvetica LaTeX::SansSerif
Courier LaTeX::special::Typewriter
GillSans &quot;AvantGarde Demi&quot;
Albertus PostScript::special::&quot;New Century Schoolbook Italic&quot;
Symbol ::special::Symbol (same as PostScript::special::Symbol)
</pre>
<p> See also the file examplefigmap.fmp in the misc directory of the pstoedit source distribution for an example font map file for xfig. Please note that the fontname has to be among those supported by xfig. See &#8211; <code><a rel="nofollow" href="http://www.xfig.org/userman/fig-format.html">http://www.xfig.org/userman/fig-format.html</a></code> for a list of legal font names </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-startdepth</code><i> number</i>]</p>
<dd>
&nbsp;set the initial depth&nbsp;(default 999)&nbsp;</dl>
<dl>
<dt>[<code>-metric</code>]</p>
<dd>
&nbsp;switch to centimeter display&nbsp;(default inches)&nbsp;</dl>
<dl>
<dt>[<code>-usecorrectfontsize</code>]</p>
<dd>
&nbsp;do not scale fonts for xfig. Use this if you also use this option with xfig&nbsp;</dl>
<dl>
<dt>[<code>-depth</code><i> number</i>]</p>
<dd>
&nbsp;set the page depth in inches&nbsp;(default 11)&nbsp;</dl>
<h3>tgif &#8211; Tgif .obj format</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-ta</code>]</p>
<dd>
&nbsp;text as attribute&nbsp;</dl>
<h3>gnuplot &#8211; gnuplot format</h3>
<p> No format specific options</p>
<h3>svm &#8211; StarView/OpenOffice.org metafile</h3>
<p> StarView/OpenOffice.org metafile, readable from OpenOffice.org 1.0/StarOffice 6.0 and above. </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-m</code>]</p>
<dd>
&nbsp;map to Arial&nbsp;</dl>
<dl>
<dt>[<code>-nf</code>]</p>
<dd>
&nbsp;emulate narrow fonts&nbsp;</dl>
<h3>vtk &#8211; VTK driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</h3>
<p> this is a long description for the VTKe driver </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-VTKeoption</code><i> integer</i>]</p>
<dd>
&nbsp;just an example&nbsp;</dl>
<h3>tk &#8211; tk and/or tk applet source code</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-R</code>]</p>
<dd>
&nbsp;swap HW&nbsp;</dl>
<dl>
<dt>[<code>-I</code>]</p>
<dd>
&nbsp;no impress&nbsp;</dl>
<dl>
<dt>[<code>-n</code><i> string</i>]</p>
<dd>
&nbsp;tagnames&nbsp;</dl>
<h3>cfdg &#8211; Context Free Design Grammar</h3>
<p> Context Free Design Grammar, usable by Context Free Art (<a rel="nofollow" href="http://www.contextfreeart.org/)">http://www.contextfreeart.org/)</a> </p>
<p> No format specific options</p>
<h3>gschem &#8211; gschem format</h3>
<p> See also: <code><a rel="nofollow" href="http://www.geda.seul.org/tools/gschem/">http://www.geda.seul.org/tools/gschem/</a></code> </p>
<p> No format specific options</p>
<h3>pcb-rnd &#8211; pcb-rnd format</h3>
<p> See also: <code><a rel="nofollow" href="http://repo.hu/pcb-rnd">http://repo.hu/pcb-rnd</a></code> and <code><a rel="nofollow" href="http://www.penguin.cz/~utx/pstoedit-pcb/">http://www.penguin.cz/~utx/pstoedit-pcb/</a></code> </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</p>
<dd>
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp;</dl>
<dl>
<dt>[<code>-snapdist</code><i> missing arg name</i>]</p>
<dd>
&nbsp;grid snap distance ratio&nbsp;(0&nbsp;&lt;&nbsp;snapdist&nbsp;&lt;=&nbsp;0.5, default 0.1)&nbsp;</dl>
<dl>
<dt>[<code>-tshiftx</code><i> missing arg name</i>]</p>
<dd>
&nbsp;additional x shift measured in target units&nbsp;(mils)&nbsp;</dl>
<dl>
<dt>[<code>-tshifty</code><i> missing arg name</i>]</p>
<dd>
&nbsp;additional y shift measured in target units&nbsp;(mils)&nbsp;</dl>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</p>
<dd>
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp;</dl>
<dl>
<dt>[<code>-mm</code>]</p>
<dd>
&nbsp;switch to metric units&nbsp;(mm)&nbsp;</dl>
<dl>
<dt>[<code>-forcepoly</code>]</p>
<dd>
&nbsp;force all objects to be interpreted as polygons&nbsp;</dl>
<h3>pcbfill &#8211; pcb format with fills</h3>
<p> See also: <code><a rel="nofollow" href="http://pcb.sourceforge.net">http://pcb.sourceforge.net</a></code> </p>
<p> No format specific options</p>
<h3>pcb &#8211; pcb format</h3>
<p> See also: <code><a rel="nofollow" href="http://pcb.sourceforge.net">http://pcb.sourceforge.net</a></code> and <code><a rel="nofollow" href="http://www.penguin.cz/~utx/pstoedit-pcb/">http://www.penguin.cz/~utx/pstoedit-pcb/</a></code> </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</p>
<dd>
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp;</dl>
<dl>
<dt>[<code>-snapdist</code><i> missing arg name</i>]</p>
<dd>
&nbsp;grid snap distance ratio&nbsp;(0&nbsp;&lt;&nbsp;snapdist&nbsp;&lt;=&nbsp;0.5, default 0.1)&nbsp;</dl>
<dl>
<dt>[<code>-tshiftx</code><i> missing arg name</i>]</p>
<dd>
&nbsp;additional x shift measured in target units&nbsp;(mils)&nbsp;</dl>
<dl>
<dt>[<code>-tshifty</code><i> missing arg name</i>]</p>
<dd>
&nbsp;additional y shift measured in target units&nbsp;(mils)&nbsp;</dl>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</p>
<dd>
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp;</dl>
<dl>
<dt>[<code>-mm</code>]</p>
<dd>
&nbsp;switch to metric units&nbsp;(mm)&nbsp;</dl>
<dl>
<dt>[<code>-stdnames</code>]</p>
<dd>
&nbsp;use standard layer names instead of descriptive names&nbsp;</dl>
<dl>
<dt>[<code>-forcepoly</code>]</p>
<dd>
&nbsp;force all objects to be interpreted as polygons&nbsp;</dl>
<h3>pcbi &#8211; engrave data &#8211; insulate/PCB format</h3>
<p> See <code><a rel="nofollow" href="http://home.vr-web.de/~hans-juergen-jahn/software/devpcb.html">http://home.vr-web.de/~hans-juergen-jahn/software/devpcb.html</a></code> for more details. </p>
<p> No format specific options</p>
<h3>Format group: hpgl pcl</h3>
<p> This group consists of the following variants:</p>
<dl>
<dt>hpgl:</p>
<dd> HPGL code.</p>
<dt>pcl:</p>
<dd> PCL code.</dl>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-penplotter</code>]</p>
<dd>
&nbsp;plotter is pen plotter&nbsp;(i.e. no support for specific line widths)&nbsp;</dl>
<dl>
<dt>[<code>-pencolorsfromfile</code>]</p>
<dd>
&nbsp;read pen colors from file drvhpgl.pencolors in pstoedit&#8217;s data directory&nbsp;</dl>
<dl>
<dt>[<code>-pencolors</code><i> number</i>]</p>
<dd>
&nbsp;maximum number of pen colors to be used by pstoedit&nbsp;(default 0)&nbsp;&#8211;&nbsp;</dl>
<dl>
<dt>[<code>-filltype</code><i> string</i>]</p>
<dd>
&nbsp;select fill type e.g. FT 1&nbsp;</dl>
<dl>
<dt>[<code>-hpgl2</code>]</p>
<dd>
&nbsp;Use HPGL/2 instead of HPGL/1&nbsp;</dl>
<dl>
<dt>[<code>-rot90</code>]</p>
<dd>
&nbsp;rotate hpgl by 90 degrees&nbsp;</dl>
<dl>
<dt>[<code>-rot180</code>]</p>
<dd>
&nbsp;rotate hpgl by 180 degrees&nbsp;</dl>
<dl>
<dt>[<code>-rot270</code>]</p>
<dd>
&nbsp;rotate hpgl by 270 degrees&nbsp;</dl>
<h3>pic &#8211; PIC format for troff et.al.</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-troff</code>]</p>
<dd>
&nbsp;troff mode&nbsp;(default is groff)&nbsp;</dl>
<dl>
<dt>[<code>-landscape</code>]</p>
<dd>
&nbsp;landscape output&nbsp;</dl>
<dl>
<dt>[<code>-portrait</code>]</p>
<dd>
&nbsp;portrait output&nbsp;</dl>
<dl>
<dt>[<code>-keepfont</code>]</p>
<dd>
&nbsp;print unrecognized literally&nbsp;</dl>
<dl>
<dt>[<code>-text</code>]</p>
<dd>
&nbsp;try not to make pictures from running text&nbsp;</dl>
<dl>
<dt>[<code>-debug</code>]</p>
<dd>
&nbsp;enable debug output&nbsp;</dl>
<h3>noixml &#8211; Nemetschek NOI XML format</h3>
<p> Nemetschek Object Interface XML format </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-r</code><i> string</i>]</p>
<dd>
&nbsp;Allplan resource file&nbsp;</dl>
<dl>
<dt>[<code>-bsl</code><i> number</i>]</p>
<dd>
&nbsp;Bezier Split Level&nbsp;(default 3)&nbsp;</dl>
<h3>latex2e &#8211; LaTeX2e picture format</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-integers</code>]</p>
<dd>
&nbsp;round all coordinates to the nearest integer&nbsp;</dl>
<h3>mma &#8211; Mathematica graphics</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-eofillfills</code>]</p>
<dd>
&nbsp;Filling is used for eofill&nbsp;(default is not to fill)&nbsp;</dl>
<h3>asy &#8211; Asymptote Format</h3>
<p> No format specific options</p>
<h3>mpost &#8211; MetaPost format</h3>
<p> No format specific options</p>
<h3>sk &#8211; Sketch format</h3>
<p> No format specific options</p>
<h3>text &#8211; text in different forms</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-height</code><i> number</i>]</p>
<dd>
&nbsp;page height in terms of characters&nbsp;</dl>
<dl>
<dt>[<code>-width</code><i> number</i>]</p>
<dd>
&nbsp;page width in terms of characters&nbsp;</dl>
<dl>
<dt>[<code>-dump</code>]</p>
<dd>
&nbsp;dump text pieces&nbsp;</dl>
<h3>kil &#8211; .kil format for Kontour</h3>
<p> No format specific options</p>
<h3>pdf &#8211; Adobe&#8217;s Portable Document Format</h3>
<p> No format specific options</p>
<h3>java2 &#8211; java 2 source code</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>java class name</code><i> string</i>]</p>
<dd>
&nbsp;name of java class to generate&nbsp;</dl>
<h3>java1 &#8211; java 1 applet source code</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>java class name</code><i> string</i>]</p>
<dd>
&nbsp;name of java class to generate&nbsp;</dl>
<h3>Format group: dxf dxf_14 dxf_s</h3>
<p> This group consists of the following variants:</p>
<dl>
<dt>dxf:</p>
<dd> CAD exchange format version 9 &#8211; only limited features. Consider using dxf_14 instead..</p>
<dt>dxf_14:</p>
<dd> CAD exchange format version 14 supporting splines and linetypes.</p>
<dt>dxf_s:</p>
<dd> CAD exchange format version 14 supporting splines and linetypes.</dl>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-polyaslines</code>]</p>
<dd>
&nbsp;use LINE instead of POLYLINE in DXF&nbsp;</dl>
<dl>
<dt>[<code>-mm</code>]</p>
<dd>
&nbsp;use mm coordinates instead of points in DXF&nbsp;(mm=pt/72*25.4)&nbsp;</dl>
<dl>
<dt>[<code>-ctl</code>]</p>
<dd>
&nbsp;map colors to layers&nbsp;</dl>
<dl>
<dt>[<code>-filltohatch</code>]</p>
<dd>
&nbsp;generate hatch objects from fill operations&nbsp;(still experimental)&nbsp;</dl>
<dl>
<dt>[<code>-splineaspolyline</code>]</p>
<dd>
&nbsp;approximate splines with PolyLines&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineasnurb</code>]</p>
<dd>
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineasbspline</code>]</p>
<dd>
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineassinglespline</code>]</p>
<dd>
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineasmultispline</code>]</p>
<dd>
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineasbezier</code>]</p>
<dd>
&nbsp;use Bezier splines in DXF format&nbsp;(only for -f dxf_s)&nbsp;</dl>
<dl>
<dt>[<code>-splineprecision</code><i> number</i>]</p>
<dd>
&nbsp;number of samples to take from spline curve when doing approximation with -splineaspolyline or -splineasmultispline &#8211; should be&nbsp;=2&nbsp;(default 5)&nbsp;</dl>
<dl>
<dt>[<code>-dumplayernames</code>]</p>
<dd>
&nbsp;dump all layer names found to standard output&nbsp;</dl>
<dl>
<dt>[<code>-layers</code><i> string</i>]</p>
<dd>
&nbsp;layers to be shown&nbsp;(comma separated list of layer names, no space)&nbsp;</dl>
<dl>
<dt>[<code>-layerfilter</code><i> string</i>]</p>
<dd>
&nbsp;layers to be hidden&nbsp;(comma separated list of layer names, no space)&nbsp;</dl>
<h3>rpl &#8211; Real3D Programming Language format</h3>
<p> No format specific options</p>
<h3>rib &#8211; RenderMan Interface Bytestream</h3>
<p> No format specific options</p>
<h3>lwo &#8211; LightWave 3D object format</h3>
<p> No format specific options</p>
<h3>cairo &#8211; cairo driver</h3>
<p> generates compilable c code for rendering with cairo </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-pango</code>]</p>
<dd>
&nbsp;use pango for font rendering&nbsp;</dl>
<dl>
<dt>[<code>-funcname</code><i> string</i>]</p>
<dd>
&nbsp;sets the base name for the generated functions and variables. e.g. myfig&nbsp;</dl>
<dl>
<dt>[<code>-header</code><i> string</i>]</p>
<dd>
&nbsp;sets the output file name for the generated C header file. e.g. myfig.h&nbsp;</dl>
<h3>gcode &#8211; emc2 gcode format</h3>
<p> See also: <code><a rel="nofollow" href="http://linuxcnc.org/">http://linuxcnc.org/</a></code> </p>
<p> No format specific options</p>
<h3>magick &#8211; MAGICK driver compatible with version 6.9.11 of ImageMagick.</h3>
<p> This driver uses the C++ API of ImageMagick or GraphicsMagick to finally produce different output formats. The output format is determined automatically by Image-/GraphicsMagick based on the suffix of the output filename. So an output file test.png will force the creation of an image in PNG format. This binary of pstoedit was compiled against version 6.9.11 of ImageMagick. </p>
<p> No format specific options</p>
<h3>Format group: gmfa gmfb plot plot-pnm plot-cgm plot-ai plot-svg plot-ps plot-fig plot-pcl plot-hpgl plot-tek</h3>
<p> This group consists of the following variants:</p>
<dl>
<dt>gmfa:</p>
<dd> ASCII GNU metafile .</p>
<dt>gmfb:</p>
<dd> binary GNU metafile .</p>
<dt>plot:</p>
<dd> GNU libplot output types, e.g. plot:-plotformat X.</p>
<dt>plot-pnm:</p>
<dd> pnm via GNU libplot.</p>
<dt>plot-cgm:</p>
<dd> cgm via GNU libplot.</p>
<dt>plot-ai:</p>
<dd> ai via GNU libplot.</p>
<dt>plot-svg:</p>
<dd> svg via GNU libplot.</p>
<dt>plot-ps:</p>
<dd> ps via GNU libplot.</p>
<dt>plot-fig:</p>
<dd> fig via GNU libplot.</p>
<dt>plot-pcl:</p>
<dd> pcl via GNU libplot.</p>
<dt>plot-hpgl:</p>
<dd> hpgl via GNU libplot.</p>
<dt>plot-tek:</p>
<dd> tek via GNU libplot.</dl>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-plotformat</code><i> string</i>]</p>
<dd>
&nbsp;plotutil format to generate&nbsp;</dl>
<h3>pptx &#8211; PresentationML (PowerPoint) format</h3>
<p> This is the format used internally by Microsoft PowerPoint. LibreOffice can also read/write PowerPoint files albeit with some lack of functionality. </p>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-colors</code><i> string</i>]</p>
<dd>
&nbsp;&quot;original&quot;&nbsp;to retain original colors&nbsp;(default),&nbsp;&quot;theme&quot;&nbsp;to convert randomly to theme colors, or&nbsp;&quot;theme-lum&quot;&nbsp;also to vary luminance&nbsp;</dl>
<dl>
<dt>[<code>-fonts</code><i> string</i>]</p>
<dd>
&nbsp;use&nbsp;&quot;windows&quot;&nbsp;fonts&nbsp;(default),&nbsp;&quot;native&quot;&nbsp;fonts, or convert to the&nbsp;&quot;theme&quot;&nbsp;font&nbsp;</dl>
<dl>
<dt>[<code>-embed</code><i> string</i>]</p>
<dd>
&nbsp;embed fonts, specified as a comma-separated list of EOT-format font files&nbsp;</dl>
<h3>emf &#8211; Enhanced MS Windows Metafile</h3>
<p> The following format specific options are available:</p>
<dl>
<dt>[<code>-m</code>]</p>
<dd>
&nbsp;map to Arial&nbsp;</dl>
<dl>
<dt>[<code>-nf</code>]</p>
<dd>
&nbsp;emulate narrow fonts&nbsp;</dl>
<dl>
<dt>[<code>-drawbb</code>]</p>
<dd>
&nbsp;draw bounding box&nbsp;</dl>
<dl>
<dt>[<code>-p</code>]</p>
<dd>
&nbsp;prune line ends&nbsp;</dl>
<dl>
<dt>[<code>-nfw</code>]</p>
<dd>
&nbsp;Newer versions of MS Windows&nbsp;(2000, XP, Vista, 7, &#8230;)&nbsp;will not accept WMF/EMF files generated when this option is set and the input contains text. But if this option is not set, then the WMF/EMF driver will estimate interletter spacing of text using a very coarse heuristic. This may result in ugly looking output. On the other hand, OpenOffice can still read EMF/WMF files where pstoedit delegates the calculation of the inter letter spacing to the program reading the WMF/EMF file. So if the generated WMF/EMF file shall never be processed under MS Windows, use this option. If WMF/EMF files with high precision text need to be generated under&nbsp;*nix the only option is to use the -pta option of pstoedit. However that causes every text to be split into single characters which makes the text hard to edit afterwards. Hence the -nfw option provides a sort of compromise between portability and nice to edit but still nice looking text. Again &#8211; this option has no meaning when pstoedit is executed under MS Windows anyway. In that case the output is portable but nevertheless not split and still looks fine.&nbsp;</dl>
<dl>
<dt>[<code>-winbb</code>]</p>
<dd>
&nbsp;let the MS Windows API calculate the Bounding Box&nbsp;(MS Windows only)&nbsp;</dl>
<dl>
<dt>[<code>-OO</code>]</p>
<dd>
&nbsp;generate OpenOffice compatible EMF file&nbsp;</dl>
<h2>NOTES</h2>
<h3>AUTOTRACE</h3>
<p> pstoedit cooperates with autotrace. Autotrace can now produce a dump file for further processing by pstoedit using the <code>-bo</code> (backend only) option. Autotrace is a program written by a group around Martin Weber and can be found at <code><a rel="nofollow" href="http://sourceforge.net/projects/autotrace/">http://sourceforge.net/projects/autotrace/</a></code>. </p>
<h3>PS2AI</h3>
<p> The ps2ai output format driver is not a native pstoedit output format driver. It does not use the pstoedit PostScript flattener, instead it uses the PostScript program ps2ai.ps which is installed in the Ghostscript distribution directory. It is included to provide the same &quot;look-and-feel&quot; for the conversion to AI. The additional benefit is that this conversion is now available also via the &quot;convert-to-vector&quot; menu of Gsview. However, lot&#8217;s of files do not convert nicely or at all using ps2ai.ps. So a native pstoedit driver would be much better. Anyone out there to take this? The AI format is usable for example by Mayura Draw (<code><a rel="nofollow" href="http://www.mayura.com">http://www.mayura.com</a></code>). Also a driver to the Mayura native format would be nice. </p>
<p> An alternative to the ps2ai based driver is available via the -f plot:ai format if the libplot(ter) is installed. </p>
<p> You should use a version of Ghostscript greater than or equal to 6.00 for using the ps2ai output format driver. </p>
<h3>METAPOST</h3>
<p> Note that, as far as Scott knows, MetaPost does not support PostScript&#8217;s eofill. The MetaPost output format driver just converts eofill to fill, and issues a warning if verbose is set. Fortunately, very few PostScript programs rely on the even-odd fill rule, even though many specify it. </p>
<p> For more on MetaPost see: </p>
<p> <code><a rel="nofollow" href="http://tug.org/metapost">http://tug.org/metapost</a></code> </p>
<h3>CONTEXT FREE &#8211; CFDG</h3>
<p> The driver for the CFDG format (drvcfdg) defines one shape per page of PostScript, but only the first shape is actually rendered (unless the user edits the generated CFDG code, of course). CFDG does not support multi-page output, so this probably is a reasonable thing to do. </p>
<p> For more on Context Free see: <code><a rel="nofollow" href="http://www.contextfreeart.org/">http://www.contextfreeart.org/</a></code> </p>
<h3>LaTeX2E</h3>
<dl>
<dt><code>*</code></p>
<dd> LaTeX2e&#8217;s picture environment is not very powerful. As a result, many elementary PostScript constructs are ignored &#8212; fills, line thicknesses (besides &quot;thick&quot; and &quot;thin&quot;), and dash patterns, to name a few. Furthermore, complex pictures may overrun TeX&#8217;s memory capacity. (The eepic package overcomes many such restrictions.)</dl>
<dl>
<dt><code>*</code></p>
<dd> Some PostScript constructs are not supported directly by &quot;picture&quot;, but can be handled by external packages. If a figure uses color, the top-level document will need to do a &quot;
