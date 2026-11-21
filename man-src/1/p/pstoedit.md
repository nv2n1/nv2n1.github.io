---
title: "pstoedit(1)"
name: "pstoedit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstoedit/"
description: "pstoedit – a tool converting PostScript and PDF files into various vector graphic formats"
---
<h2 class="name">NAME</h2>
<p> pstoedit - a tool converting PostScript and PDF files into various vector graphic formats  </p>
<h2>SYNOPSIS</h2>
<h3>FROM THE COMMAND SHELL</h3>
<p> pstoedit [<code>-v -help</code>] <br />
 </p>
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
<p> to get a list of supported output formats. Pstoedit comes with a large set of format drivers integrated in the binary. Additional drivers can be installed as plugins and are available via <code><a rel="nofollow" href="http://www.pstoedit.net/plugins/">http://www.pstoedit.net/plugins/</a></code>. Just copy the plugins to the same directory where the pstoedit binary is installed or - under Unix like systems only - alternatively into the lib directory parallel to the bin directory where pstoedit is installed. </p>
<p> However, unless you also get a license key for the plugins, the additional drivers will slightly distort the resulting graphics. See the documentation provided with the plugins for further details. </p>
<h3>PRINCIPLE OF CONVERSION</h3>
<p> pstoedit works by redefining some basic painting operators of PostScript, e.g. <code>stroke</code> or <code>show</code> (bitmaps drawn by the image operator are not supported by all output formats.) After redefining these operators, the PostScript or PDF file that needs to be converted is processed by a PostScript interpreter, e.g., Ghostscript (<i><a href="/docs/linux/man/1-gs/">gs</a></i>(1)). You normally need to have a PostScript interpreter installed in order to use this program. However, you can perform some &quot;back end only&quot; processing of files following the conventions of the pstoedit intermediate format by specifying the <code>-bo</code> option. See &quot;Available formats and their specific options&quot; below. </p>
<p> The output that is written by the interpreter due to the redefinition of the drawing operators is a sort of &#8216;flat&#8217; PostScript file that contains only simple operations like moveto, lineto, show, etc. You can look at this file using the <code>-f debug</code> option. </p>
<p> This output is read by end-processing functions of pstoedit and triggers the drawing functions in the selected output format driver sometime called also &quot;backend&quot;. </p>
<h3>NOTES</h3>
<p> If you want to process PDF files directly, your PostScript interpreter must provide this feature, as does Ghostscript. Aladdin Ghostscript is recommended for processing PDF and PostScript files. </p>
<h2>OPTIONS</h2>
<h3>GENERAL OPTIONS</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-include</code><i> name of a PostScript file to be included</i>]</dt>
<dd> <p> <br />
&nbsp;This option allows specifying an additional PostScript file that will be executed just before the normal input is read. This is helpful for including specific page settings or for disabling potentially unsafe PostScript operators, e.g., file, renamefile, or deletefile.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-xscale</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-yscale</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-xshift</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-yshift</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-centered</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-minlinewidth</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-pagenumberformat</code><i> page number format specification</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-split</code>]</dt>
<dd> <p> <br />
&nbsp;Create a new file for each page of the input. For this the output filename must contain a&nbsp;%d which is replaced with the current page number. This option is automatically switched on for output formats that do not support multiple pages within one file, e.g. fig or gnuplot.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-usebbfrominput</code>]</dt>
<dd> <p> <br />
&nbsp;If specified, pstoedit uses the BoundingBox as is&nbsp;(hopefully)&nbsp;found in the input file instead of one that is calculated by its own.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-page</code><i> page number</i>]</dt>
<dd> <p> <br />
&nbsp;Select a single page from a multi-page PostScript or PDF file.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-rgb</code>]</dt>
<dd> <p> <br />
&nbsp;Since version 3.30 pstoedit uses the CMYK colors internally. The -rgb option turns on the old behavior to use RGB values.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-useagl</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-noclip</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-rotate</code><i> angle (0-360)</i>]</dt>
<dd> <p> <br />
&nbsp;Rotate image by angle.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-pagesize</code><i> page format</i>]</dt>
<dd> <p> <br />
&nbsp;set page size for output medium.&nbsp; This option sets the page size for the output medium. Currently this is just used by the libplot output format driver, but might be used by other output format drivers in future. The page size is specified in terms of the usual page size names, e.g. letter or a4. </p>
 </dd></dl>
<dl>
<dt>[<code>-help</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-gs</code><i> path to the Ghostscript executable/DLL</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-bo</code>]</dt>
<dd> <p> <br />
&nbsp;You can run backend processing only&nbsp;(without the PostScript interpreter frontend)&nbsp;by first running&nbsp;<code>pstoedit</code> <code>-f dump</code> <i>infile</i> <i>dumpfile</i> and then running <code>pstoedit</code> <code>-f</code><i> format</i> <code>-bo</code> <i>dumpfile</i> <i>outfile</i>. </p>
 </dd></dl>
<dl>
<dt>[<code>-psarg</code><i> argument string</i>]</dt>
<dd> <p> <br />
&nbsp;The string given with this option is passed directly to Ghostscript when Ghostscript is called to process the PostScript file for pstoedit. For example: <code>-psarg</code><code> &quot;</code><code>-r300x300</code><code>&quot;</code>. This causes the resolution to be changed to 300x300 dpi. (With older versions of Ghostscript, changing the resolution this way has an effect only if the <code>-dis</code> option is given.) If you want to pass multiple options to Ghostscript you can use multiple -psarg options <code>-psarg opt1</code> <code>-psarg opt2</code> <code>-psarg opt2</code>. See the Ghostscript manual for other possible options. </p>
 </dd></dl>
<dl>
<dt>[<code>-pslanguagelevel</code><i> PostScript Language Level 1, 2, or 3 to be used.</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt><code>-f</code><i> &quot;format[:options]&quot;</i></dt>
<dd> <p> <br />
&nbsp;target output format recognized by pstoedit. Since other format drivers can be loaded dynamically, type pstoedit -help to get a full list of formats. See &quot;Available formats and their specific options&quot; below for an explanation of the [<i>:options</i>] to <code>-f</code> format. If the format option is not given, pstoedit tries to guess the target format from the suffix of the output filename. However, in a lot of cases, this is not a unique mapping and hence pstoedit demands the <code>-f</code> option. </p>
 </dd></dl>
<dl>
<dt>[<code>-gsregbase</code><i> Ghostscript base registry path</i>]</dt>
<dd> <p> <br />
&nbsp;registry path to use as a base path when searching Ghostscript interpreter.&nbsp; This option provides means to specify a registry key under HKLM/Software where to search for GS interpreter key, version and GS_DLL / GS_LIB values. Example: &quot;-gsregbase MyCompany&quot; means that HKLM/Software/MyCompany/GPL Ghostscript would be searched instead of HKLM/Software/GPL Ghostscript. </p>
 </dd></dl>
<h3>TEXT AND FONT HANDLING RELATED OPTIONS</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-df</code><i> font name</i>]</dt>
<dd> <p> <br />
&nbsp;Sometimes fonts embedded in a PostScript program do not have a fontname. For example, this happens in PostScript files generated by&nbsp;<i><a href="/docs/linux/man/1-dvips/">dvips</a></i>(1). In such a case pstoedit uses a replacement font. The default for this is Courier. Another font can be specified using the <code>-df</code> option. <code>-df Helvetica</code> causes all unnamed fonts to be replaced by Helvetica. </p>
 </dd></dl>
<dl>
<dt>[<code>-nomaptoisolatin1</code>]</dt>
<dd> <p> <br />
&nbsp;Normally pstoedit maps all character codes to the ones defined by the ISO Latin1 encoding. If you specify <code>-nomaptoisolatin1</code> then the encoding from the input PostScript is passed unchanged to the output. This may result in strange text output but on the other hand may be the only way to get some fonts converted appropriately. Try what fits best to your concrete case. </p>
 </dd></dl>
<dl>
<dt>[<code>-pngimage</code><i> filename</i>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-dt</code>]</dt>
<dd> <p> <br />
&nbsp;draw text. Text is drawn as polygons. This might produce a large output file. This option is automatically switched on if the selected output format does not support text, e.g.&nbsp;<i><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></i>(1). </p>
 </dd></dl>
<dl>
<dt>[<code>-adt</code>]</dt>
<dd> <p> <br />
&nbsp;automatic draw text. This option turns on the&nbsp;<code>-dt</code> option selectively for fonts that seem to be no normal text fonts, e.g. Symbol. </p>
 </dd></dl>
<dl>
<dt>[<code>-ndt</code>]</dt>
<dd> <p> <br />
&nbsp;never draw text. Fully disable the heuristics used by pstoedit to decide when to&nbsp;&quot;draw&quot;&nbsp;text instead of showing it as text. This may produce incorrect results, but in some cases it might nevertheless be useful.&nbsp;&quot;Use at own risk&quot;.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-dgbm</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-correctdefinefont</code>]</dt>
<dd> <p> <br />
&nbsp;Some PostScript files, e.g. such as generated by ChemDraw, use the PostScript definefont operator in a way that is incompatible with pstoedit&#8217;s assumptions. The new font is defined by copying an old font without changing the FontName of the new font. When this option is applied, some&nbsp;&quot;patches&quot;&nbsp;are done after a definefont in order to make it again compatible with pstoedit&#8217;s assumptions. This option is not enabled by default, since it may break other PostScript files. It is tested only with ChemDraw generated files.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-pti</code>]</dt>
<dd> <p> <br />
&nbsp;precision text. Normally a text string is drawn as it occurs in the input file. However, in some situations, this might produce wrongly positioned characters. This is due to limitations in most output formats of pstoedit. They cannot represent text with arbitrary inter-letter spacing which is easily possible in PDF and PostScript. With&nbsp;<code>-pta</code>, each character of a text string is placed separately. With <code>-pti</code>, this is done only in cases when there is a non zero inter-letter spacing. The downside of &quot;precision text&quot; is a bigger file size and hard to edit text. </p>
 </dd></dl>
<dl>
<dt>[<code>-pta</code>]</dt>
<dd> <p> <br />
&nbsp;see -pti&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-uchar</code><i> character</i>]</dt>
<dd> <p> <br />
&nbsp;Sometimes pstoedit cannot map a character from the encoding used by the PostScript file to the font encoding of the target format. In this case pstoedit replaces the input character by a special character in order to show all the places that could not be mapped correctly. The default for this is a&nbsp;&quot;#&quot;. Using the&nbsp;<code>-uchar</code> option it is possible to specify another character to be used instead. If you want to use a space, use -uchar &quot; &quot;. </p>
 </dd></dl>
<dl>
<dt>[<code>-t2fontsast1</code>]</dt>
<dd> <p> <br />
&nbsp;Handle Type 2 fonts same as Type 1. Type 2 fonts sometimes occur as embedded fonts within PDF files. In the default mode, text using such fonts is drawn as polygons since pstoedit assumes that such a font is not available on the user&#8217;s machine. If this option is set, pstoedit assumes that the internal encoding follows the same as for a standard font and generates normal text output. This assumption may not be true in all cases. But it is nearly impossible for pstoedit to verify this assumption - it would have to do a sort of OCR.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-nfr</code>]</dt>
<dd> <p> <br />
&nbsp;In normal mode pstoedit replaces bitmap fonts with a font as defined by the&nbsp;<code>-df</code> option. This is done, because most output formats cannot handle such fonts. This behavior can be switched off using the <code>-nfr</code> option but then it strongly depends on the application reading the generated file whether the file is usable and correctly interpreted or not. Any problems are then out of control of pstoedit. </p>
 </dd></dl>
<dl>
<dt>[<code>-glyphs</code>]</dt>
<dd> <p> <br />
&nbsp;pass glyph names to the output format driver. So far no output format driver really uses the glyph names, so this does not have any effect at the moment. It is a preparation for future work.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-useoldnormalization</code>]</dt>
<dd> <p> <br />
&nbsp;Just use this option in case the new heuristic introduced in 3.5 does not produce correct results - however, this normalization of font encoding will always be a best-effort approach since there is no real general solution to it with reasonable effort&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-fontmap</code><i> name of font map file for pstoedit</i>]</dt>
<dd> <p> <br />
&nbsp;The font map is a simple text file containing lines in the following format: <br />
 </p>
 </dd></dl>
<p> document_font_name target_font_name <br />
 Lines beginning with % are considerd comments. <br />
 For font names with spaces use the &quot;font name with spaces&quot; notation. </p>
<p> If a target_font_name starts with /, it is regarded as alias to a former entry. </p>
<p> Each font name found in the document is checked against this mapping and if there is a corresponding entry, the new name is used for the output. </p>
<p> If the <code>-fontmap</code> option is not specified, pstoedit automatically looks for the file <i>drivername</i>.fmp in the installation directory and uses that file as a default fontmap file if available. The installation directory is: </p>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> MS Windows: The same directory where the pstoedit executable is located </p>
 </dd>
<dl>
<dd>  </dd></dl>
<dt><code>*</code></dt>
<dd> <p> Unix: <br />
 The default installation directory. If it fails, then &lt;<i>The directory where the pstoedit executable is located</i>&gt; /../lib/ </p>
 </dd>
<dl>
<dd>  </dd></dl>
</dl>
</dl>
<dl>
<dd> <p> The mpost.fmp in the misc directory of the pstoedit distribution is a sample map file with mappings from over 5000 PostScript font names to their TeX equivalents. This is useful because MetaPost is frequently used with TeX/LaTeX and those programs do not use standard font names. This file and the MetaPost output format driver are provided by Scott Pakin (<code>scott+ps2ed_AT_pakin.org</code>). Another example is wemf.fmp to be used under Windows. See the misc directory of the pstoedit source distribution. After loading the implicit (based on driver name) or explicit (based on the -fontmap option) font map file, a system specific map file is searched and loaded from the installation directory (unix.fmp or windows.fmp). This file can be used to redirect certain fonts to system specific names using the /AliasName notation described above. </p>
 </dd></dl>
<h3>DRAWING RELATED OPTIONS</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-nc</code>]</dt>
<dd> <p> <br />
&nbsp;no curves.&nbsp; Normally pstoedit tries to keep curves from the input and transfers them to the output if the output format supports curves. If the output format does not support curves, then pstoedit replaces curves by a series of lines (see also <code>-flat</code> option). However, in some cases the user might wish to have this behavior also for output formats that originally support curves. This can be forced via the <code>-nc</code> option. </p>
 </dd></dl>
<dl>
<dt>[<code>-mergelines</code>]</dt>
<dd> <p> <br />
&nbsp;Some output formats permit the representation of filled polygons with edges that are in a different color than the fill color. Since PostScript does not support this by the standard drawing primitives directly, drawing programs typically generate two objects&nbsp;(the outline and the filled polygon)&nbsp;into the PostScript output. pstoedit is able to recombine these, if they follow each other directly and you specify <code>-mergelines</code>. However, this merging is not supported by all output formats due to restrictions in the target format. </p>
 </dd></dl>
<dl>
<dt>[<code>-filledrecttostroke</code>]</dt>
<dd> <p> <br />
&nbsp;Rectangles filled with a solid color can be converted to a stroked line with a width that corresponds to the width of the rectangle. This is of primary interest for output formats which do not support filled polygons at all. But it is restricted to rectangles only, i.e. it is not supported for general polygons&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-mergetext</code>]</dt>
<dd> <p> <br />
&nbsp;In order to produce nice looking text output, programs producing PostScript files often split words into smaller pieces which are then placed individually on adjacent positions. However, such split text is hard to edit later on and hence it is sometime better to recombine these pieces again to form a word&nbsp;(or even sequence of words). For this pstoedit implements some heuristics about what text pieces are to be considered parts of a split word. This is based on the geometrical proximity of the different parts and seems to work quite well so far. But there are certainly cases where this simple heuristic fails. So please check the results carefully.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-ssp</code>]</dt>
<dd> <p> <br />
&nbsp;simulate subpaths.&nbsp; Several output formats do not support PostScript paths containing subpaths, i.e. paths with intermediate movetos. In the normal case, each subpath is treated as an independent path for such output formats. This can lead to bad looking results. The most common case where this happens is if you use the <code>-dt</code> option and show some text with letters like e, o, or b, i.e. letters that have a &quot;hole&quot;. When the <code>-ssp</code> option is set, pstoedit tries to eliminate these problems. However, this option is CPU time intensive! </p>
 </dd></dl>
<dl>
<dt>[<code>-sfill</code>]</dt>
<dd> <p> <br />
&nbsp;simulate filling by individual strokes.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-flat</code><i> flatness factor</i>]</dt>
<dd> <p> <br />
&nbsp;If the output format does not support curves in the way PostScript does or if the&nbsp;<code>-nc</code> option is specified, all curves are approximated by lines. Using the <code>-flat</code> option one can control this approximation. This parameter is directly converted to a PostScript <code>setflat</code> command. Higher numbers, e.g. 10 give rougher, lower numbers, e.g. 0.1, give finer approximations. </p>
 </dd></dl>
<dl>
<dt>[<code>-sclip</code>]</dt>
<dd> <p> <br />
&nbsp;simulate clipping.&nbsp; Most output formats of pstoedit do not have native support for clipping. For that pstoedit offers an option to perform the clipping of the graphics directly without passing the clippath to the output driver. However, this results in curves being replaced by a lot of line segments and thus larger output files. So use this option only if your output looks different from the input due to clipping. In addition, this &quot;simulated clipping&quot; is not exactly the same as defined in PostScript. There might be lines drawn at double size. Also clipping of text is not supported unless you also use the <code>-dt</code> option. </p>
 </dd></dl>
<h3>DEBUG OPTIONS</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-dis</code>]</dt>
<dd> <p> <br />
&nbsp;Open a display during processing by Ghostscript. Some files only work correctly this way.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-q</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-nq</code>]</dt>
<dd> <p> <br />
&nbsp;no exit from the PostScript interpreter. Normally Ghostscript exits after processing the pstoedit input-file. For debugging it can be useful to avoid this. If you do, you will have to type quit at the GS&gt;&nbsp;prompt to exit from Ghostscript.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-v</code>]</dt>
<dd> <p> <br />
&nbsp;Switch on verbose mode. Some additional information is shown during processing.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-vl</code><i></i>]</dt>
<dd> <p> <br />
&nbsp;Switch on verbose mode with a given level. Some additional information is shown during processing.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-nb</code>]</dt>
<dd> <p> <br />
&nbsp;Since version 3.10 pstoedit uses the -dDELAYBIND option when calling Ghostscript. Previously the -dNOBIND option was used instead but that sometimes caused problems if a user&#8217;s PostScript file overloaded standard PostScript operator with totally new semantic, e.g. lt for lineto instead of the standard meaning of &quot;less than&quot;. Using <code>-nb</code> the old style can be activated again in case the -dDELAYBIND gives different results as before. In such a case please also contact the author. </p>
 </dd></dl>
<dl>
<dt>[<code>-rdb</code>]</dt>
<dd> <p> <br />
&nbsp;Since version 3.10 pstoedit uses the -dDELAYBIND option when calling Ghostscript. But in version 9.22 of GhostScript, that option is not supported anymore because of security reasons. As a fallback, that version provides the REALLYDELAYBIND option and pstoedit can use this if you supply the <code>-rdb</code> option. Use this with caution as it might open security risks, e.g. a PostScript file injecting some malicious code into PostScript standard operators. However, not using this option can cause some of the PostScript drawings operations to be not seen by pstoedit, hence causing missing artefacts in the output. Later versions of Ghostscript will probably support -dDELAYBIND again. But also in that case the security risk remains. So be careful with what files you process with pstoedit and Ghostscript. </p>
 </dd></dl>
<dl>
<dt>[<code>-ups</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-keep</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-debugfonthandling</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-gstest</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd>
<dt>[<code>-fakedateandversion</code>]</dt>
<dd> <p> <br />
&nbsp;.PP </p>
 </dd></dl>
<h3>INPUT AND OUTFILE FILE ARGUMENTS</h3>
<p> [ inputfile [outputfile] ] </p>
<p> If neither an input nor an output file is given as argument, pstoedit works as filter reading from standard input and writing to standard output. The special filename &quot;-&quot; can also be used. It represents standard input if it is the first on the command line and standard output if it is the second. So &quot;pstoedit - output.xxx&quot; reads from standard input and writes to output.xxx </p>
<h2>AVAILABLE FORMATS AND THEIR SPECIFIC OPTIONS</h2>
<p> pstoedit allows passing individual options to an output format driver. This is done by appending all options to the format specified after the <code>-f</code> option. The format specifier and its options must be separated by a colon (:). If more than one option needs to be passed to the output format driver, the whole argument to <code>-f</code> must be enclosed within double-quote characters, thus: </p>
<p> <code>-f</code><i> &quot;format[:option option ...]&quot;</i> </p>
<p> To see which options are supported by a specific format, type: <code>pstoedit -f format:-help</code> <br />
 </p>
<p> The following description of the different formats supported by pstoedit is extracted from the source code of the individual drivers. </p>
<h3>Format group: psf ps debug dump gs ps2ai</h3>
<p> This group consists of the following variants: </p>
<dl>
<dt>psf: </dt>
<dd> <p> Flattened PostScript (no curves). </p>
 </dd>
<dt>ps: </dt>
<dd> <p> Simplified PostScript with curves. </p>
 </dd>
<dt>debug: </dt>
<dd> <p> for test purposes. </p>
 </dd>
<dt>dump: </dt>
<dd> <p> for test purposes (same as debug). </p>
 </dd>
<dt>gs: </dt>
<dd> <p> any device that Ghostscript provides - use gs:format, e.g. gs:pdfwrite. </p>
 </dd>
<dt>ps2ai: </dt>
<dd> <p> Adobe Illustrator via ps2ai.ps of Ghostscript. </p>
 </dd></dl>
<p> No format specific options  </p>
<h3>sample - sample driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</h3>
<p> This is a long description for the sample driver </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-sampleoption</code><i> integer</i>]</dt>
<dd> <p> <br />
&nbsp;just an example&nbsp; </p>
 </dd></dl>
<h3>idraw - Interviews draw format (EPS)</h3>
<p> No format specific options  </p>
<h3>Format group: fig xfig tfig</h3>
<p> This group consists of the following variants: </p>
<dl>
<dt>fig: </dt>
<dd> <p> .fig format for xfig. </p>
 </dd>
<dt>xfig: </dt>
<dd> <p> .fig format for xfig. </p>
 </dd>
<dt>tfig: </dt>
<dd> <p> .fig format for xfig - test only version. </p>
 </dd></dl>
<p> The xfig format driver supports special fontnames, which may be produced by using a fontmap file. The following types of names are supported: <br />
 </p>
<pre><code>General notation:
&quot;PostScript Font Name&quot; ((LaTeX|PostScript|empty)(::special)::)XFigFontName
Examples:
Helvetica LaTeX::SansSerif
Courier LaTeX::special::Typewriter
GillSans &quot;AvantGarde Demi&quot;
Albertus PostScript::special::&quot;New Century Schoolbook Italic&quot;
Symbol ::special::Symbol (same as PostScript::special::Symbol)
</code></pre>
<p> See also the file examplefigmap.fmp in the misc directory of the pstoedit source distribution for an example font map file for xfig. Please note that the fontname has to be among those supported by xfig. See - <code><a rel="nofollow" href="http://www.xfig.org/userman/fig-format.html">http://www.xfig.org/userman/fig-format.html</a></code> for a list of legal font names </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-startdepth</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;set the initial depth&nbsp;(default 999)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-metric</code>]</dt>
<dd> <p> <br />
&nbsp;switch to centimeter display&nbsp;(default inches)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-usecorrectfontsize</code>]</dt>
<dd> <p> <br />
&nbsp;do not scale fonts for xfig. Use this if you also use this option with xfig&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-depth</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;set the page depth in inches&nbsp;(default 11)&nbsp; </p>
 </dd></dl>
<h3>tgif - Tgif .obj format</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-ta</code>]</dt>
<dd> <p> <br />
&nbsp;text as attribute&nbsp; </p>
 </dd></dl>
<h3>gnuplot - gnuplot format</h3>
<p> No format specific options  </p>
<h3>svm - StarView/OpenOffice.org metafile</h3>
<p> StarView/OpenOffice.org metafile, readable from OpenOffice.org 1.0/StarOffice 6.0 and above. </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-m</code>]</dt>
<dd> <p> <br />
&nbsp;map to Arial&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-nf</code>]</dt>
<dd> <p> <br />
&nbsp;emulate narrow fonts&nbsp; </p>
 </dd></dl>
<h3>vtk - VTK driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</h3>
<p> this is a long description for the VTKe driver </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-VTKeoption</code><i> integer</i>]</dt>
<dd> <p> <br />
&nbsp;just an example&nbsp; </p>
 </dd></dl>
<h3>tk - tk and/or tk applet source code</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-R</code>]</dt>
<dd> <p> <br />
&nbsp;swap HW&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-I</code>]</dt>
<dd> <p> <br />
&nbsp;no impress&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-n</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;tagnames&nbsp; </p>
 </dd></dl>
<h3>cfdg - Context Free Design Grammar</h3>
<p> Context Free Design Grammar, usable by Context Free Art (<a rel="nofollow" href="http://www.contextfreeart.org/)">http://www.contextfreeart.org/)</a> </p>
<p> No format specific options  </p>
<h3>gschem - gschem format</h3>
<p> See also: <code><a rel="nofollow" href="http://www.geda.seul.org/tools/gschem/">http://www.geda.seul.org/tools/gschem/</a></code> </p>
<p> No format specific options  </p>
<h3>pcb-rnd - pcb-rnd format</h3>
<p> See also: <code><a rel="nofollow" href="http://repo.hu/pcb-rnd">http://repo.hu/pcb-rnd</a></code> and <code><a rel="nofollow" href="http://www.penguin.cz/~utx/pstoedit-pcb/">http://www.penguin.cz/~utx/pstoedit-pcb/</a></code> </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-snapdist</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;grid snap distance ratio&nbsp;(0&nbsp;&lt;&nbsp;snapdist&nbsp;&lt;=&nbsp;0.5, default 0.1)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-tshiftx</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;additional x shift measured in target units&nbsp;(mils)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-tshifty</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;additional y shift measured in target units&nbsp;(mils)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-mm</code>]</dt>
<dd> <p> <br />
&nbsp;switch to metric units&nbsp;(mm)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-forcepoly</code>]</dt>
<dd> <p> <br />
&nbsp;force all objects to be interpreted as polygons&nbsp; </p>
 </dd></dl>
<h3>pcbfill - pcb format with fills</h3>
<p> See also: <code><a rel="nofollow" href="http://pcb.sourceforge.net">http://pcb.sourceforge.net</a></code> </p>
<p> No format specific options  </p>
<h3>pcb - pcb format</h3>
<p> See also: <code><a rel="nofollow" href="http://pcb.sourceforge.net">http://pcb.sourceforge.net</a></code> and <code><a rel="nofollow" href="http://www.penguin.cz/~utx/pstoedit-pcb/">http://www.penguin.cz/~utx/pstoedit-pcb/</a></code> </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-snapdist</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;grid snap distance ratio&nbsp;(0&nbsp;&lt;&nbsp;snapdist&nbsp;&lt;=&nbsp;0.5, default 0.1)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-tshiftx</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;additional x shift measured in target units&nbsp;(mils)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-tshifty</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;additional y shift measured in target units&nbsp;(mils)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-grid</code><i> missing arg name</i>]</dt>
<dd> <p> <br />
&nbsp;attempt to snap relevant output to grid&nbsp;(mils)&nbsp;and put failed objects to a different layer&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-mm</code>]</dt>
<dd> <p> <br />
&nbsp;switch to metric units&nbsp;(mm)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-stdnames</code>]</dt>
<dd> <p> <br />
&nbsp;use standard layer names instead of descriptive names&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-forcepoly</code>]</dt>
<dd> <p> <br />
&nbsp;force all objects to be interpreted as polygons&nbsp; </p>
 </dd></dl>
<h3>pcbi - engrave data - insulate/PCB format</h3>
<p> See <code><a rel="nofollow" href="http://home.vr-web.de/~hans-juergen-jahn/software/devpcb.html">http://home.vr-web.de/~hans-juergen-jahn/software/devpcb.html</a></code> for more details. </p>
<p> No format specific options  </p>
<h3>Format group: hpgl pcl</h3>
<p> This group consists of the following variants: </p>
<dl>
<dt>hpgl: </dt>
<dd> <p> HPGL code. </p>
 </dd>
<dt>pcl: </dt>
<dd> <p> PCL code. </p>
 </dd></dl>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-penplotter</code>]</dt>
<dd> <p> <br />
&nbsp;plotter is pen plotter&nbsp;(i.e. no support for specific line widths)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-pencolorsfromfile</code>]</dt>
<dd> <p> <br />
&nbsp;read pen colors from file drvhpgl.pencolors in pstoedit&#8217;s data directory&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-pencolors</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;maximum number of pen colors to be used by pstoedit&nbsp;(default 0)&nbsp;-&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-filltype</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;select fill type e.g. FT 1&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-hpgl2</code>]</dt>
<dd> <p> <br />
&nbsp;Use HPGL/2 instead of HPGL/1&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-rot90</code>]</dt>
<dd> <p> <br />
&nbsp;rotate hpgl by 90 degrees&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-rot180</code>]</dt>
<dd> <p> <br />
&nbsp;rotate hpgl by 180 degrees&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-rot270</code>]</dt>
<dd> <p> <br />
&nbsp;rotate hpgl by 270 degrees&nbsp; </p>
 </dd></dl>
<h3>pic - PIC format for troff et.al.</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-troff</code>]</dt>
<dd> <p> <br />
&nbsp;troff mode&nbsp;(default is groff)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-landscape</code>]</dt>
<dd> <p> <br />
&nbsp;landscape output&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-portrait</code>]</dt>
<dd> <p> <br />
&nbsp;portrait output&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-keepfont</code>]</dt>
<dd> <p> <br />
&nbsp;print unrecognized literally&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-text</code>]</dt>
<dd> <p> <br />
&nbsp;try not to make pictures from running text&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-debug</code>]</dt>
<dd> <p> <br />
&nbsp;enable debug output&nbsp; </p>
 </dd></dl>
<h3>noixml - Nemetschek NOI XML format</h3>
<p> Nemetschek Object Interface XML format </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-r</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;Allplan resource file&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-bsl</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;Bezier Split Level&nbsp;(default 3)&nbsp; </p>
 </dd></dl>
<h3>latex2e - LaTeX2e picture format</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-integers</code>]</dt>
<dd> <p> <br />
&nbsp;round all coordinates to the nearest integer&nbsp; </p>
 </dd></dl>
<h3>mma - Mathematica graphics</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-eofillfills</code>]</dt>
<dd> <p> <br />
&nbsp;Filling is used for eofill&nbsp;(default is not to fill)&nbsp; </p>
 </dd></dl>
<h3>asy - Asymptote Format</h3>
<p> No format specific options  </p>
<h3>mpost - MetaPost format</h3>
<p> No format specific options  </p>
<h3>sk - Sketch format</h3>
<p> No format specific options  </p>
<h3>text - text in different forms</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-height</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;page height in terms of characters&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-width</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;page width in terms of characters&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-dump</code>]</dt>
<dd> <p> <br />
&nbsp;dump text pieces&nbsp; </p>
 </dd></dl>
<h3>kil - .kil format for Kontour</h3>
<p> No format specific options  </p>
<h3>pdf - Adobe's Portable Document Format</h3>
<p> No format specific options  </p>
<h3>java2 - java 2 source code</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>java class name</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;name of java class to generate&nbsp; </p>
 </dd></dl>
<h3>java1 - java 1 applet source code</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>java class name</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;name of java class to generate&nbsp; </p>
 </dd></dl>
<h3>Format group: dxf dxf_14 dxf_s</h3>
<p> This group consists of the following variants: </p>
<dl>
<dt>dxf: </dt>
<dd> <p> CAD exchange format version 9 - only limited features. Consider using dxf_14 instead.. </p>
 </dd>
<dt>dxf_14: </dt>
<dd> <p> CAD exchange format version 14 supporting splines and linetypes. </p>
 </dd>
<dt>dxf_s: </dt>
<dd> <p> CAD exchange format version 14 supporting splines and linetypes. </p>
 </dd></dl>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-polyaslines</code>]</dt>
<dd> <p> <br />
&nbsp;use LINE instead of POLYLINE in DXF&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-mm</code>]</dt>
<dd> <p> <br />
&nbsp;use mm coordinates instead of points in DXF&nbsp;(mm=pt/72*25.4)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-ctl</code>]</dt>
<dd> <p> <br />
&nbsp;map colors to layers&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-filltohatch</code>]</dt>
<dd> <p> <br />
&nbsp;generate hatch objects from fill operations&nbsp;(still experimental)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineaspolyline</code>]</dt>
<dd> <p> <br />
&nbsp;approximate splines with PolyLines&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineasnurb</code>]</dt>
<dd> <p> <br />
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineasbspline</code>]</dt>
<dd> <p> <br />
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineassinglespline</code>]</dt>
<dd> <p> <br />
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineasmultispline</code>]</dt>
<dd> <p> <br />
&nbsp;experimental&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineasbezier</code>]</dt>
<dd> <p> <br />
&nbsp;use Bezier splines in DXF format&nbsp;(only for -f dxf_s)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-splineprecision</code><i> number</i>]</dt>
<dd> <p> <br />
&nbsp;number of samples to take from spline curve when doing approximation with -splineaspolyline or -splineasmultispline - should be&nbsp;=2&nbsp;(default 5)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-dumplayernames</code>]</dt>
<dd> <p> <br />
&nbsp;dump all layer names found to standard output&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-layers</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;layers to be shown&nbsp;(comma separated list of layer names, no space)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-layerfilter</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;layers to be hidden&nbsp;(comma separated list of layer names, no space)&nbsp; </p>
 </dd></dl>
<h3>rpl - Real3D Programming Language format</h3>
<p> No format specific options  </p>
<h3>rib - RenderMan Interface Bytestream</h3>
<p> No format specific options  </p>
<h3>lwo - LightWave 3D object format</h3>
<p> No format specific options  </p>
<h3>cairo - cairo driver</h3>
<p> generates compilable c code for rendering with cairo </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-pango</code>]</dt>
<dd> <p> <br />
&nbsp;use pango for font rendering&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-funcname</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;sets the base name for the generated functions and variables. e.g. myfig&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-header</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;sets the output file name for the generated C header file. e.g. myfig.h&nbsp; </p>
 </dd></dl>
<h3>gcode - emc2 gcode format</h3>
<p> See also: <code><a rel="nofollow" href="http://linuxcnc.org/">http://linuxcnc.org/</a></code> </p>
<p> No format specific options  </p>
<h3>magick - MAGICK driver compatible with version 6.9.11 of ImageMagick.</h3>
<p> This driver uses the C++ API of ImageMagick or GraphicsMagick to finally produce different output formats. The output format is determined automatically by Image-/GraphicsMagick based on the suffix of the output filename. So an output file test.png will force the creation of an image in PNG format. This binary of pstoedit was compiled against version 6.9.11 of ImageMagick. </p>
<p> No format specific options  </p>
<h3>Format group: gmfa gmfb plot plot-pnm plot-cgm plot-ai plot-svg plot-ps plot-fig plot-pcl plot-hpgl plot-tek</h3>
<p> This group consists of the following variants: </p>
<dl>
<dt>gmfa: </dt>
<dd> <p> ASCII GNU metafile . </p>
 </dd>
<dt>gmfb: </dt>
<dd> <p> binary GNU metafile . </p>
 </dd>
<dt>plot: </dt>
<dd> <p> GNU libplot output types, e.g. plot:-plotformat X. </p>
 </dd>
<dt>plot-pnm: </dt>
<dd> <p> pnm via GNU libplot. </p>
 </dd>
<dt>plot-cgm: </dt>
<dd> <p> cgm via GNU libplot. </p>
 </dd>
<dt>plot-ai: </dt>
<dd> <p> ai via GNU libplot. </p>
 </dd>
<dt>plot-svg: </dt>
<dd> <p> svg via GNU libplot. </p>
 </dd>
<dt>plot-ps: </dt>
<dd> <p> ps via GNU libplot. </p>
 </dd>
<dt>plot-fig: </dt>
<dd> <p> fig via GNU libplot. </p>
 </dd>
<dt>plot-pcl: </dt>
<dd> <p> pcl via GNU libplot. </p>
 </dd>
<dt>plot-hpgl: </dt>
<dd> <p> hpgl via GNU libplot. </p>
 </dd>
<dt>plot-tek: </dt>
<dd> <p> tek via GNU libplot. </p>
 </dd></dl>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-plotformat</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;plotutil format to generate&nbsp; </p>
 </dd></dl>
<h3>pptx - PresentationML (PowerPoint) format</h3>
<p> This is the format used internally by Microsoft PowerPoint. LibreOffice can also read/write PowerPoint files albeit with some lack of functionality. </p>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-colors</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;&quot;original&quot;&nbsp;to retain original colors&nbsp;(default),&nbsp;&quot;theme&quot;&nbsp;to convert randomly to theme colors, or&nbsp;&quot;theme-lum&quot;&nbsp;also to vary luminance&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-fonts</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;use&nbsp;&quot;windows&quot;&nbsp;fonts&nbsp;(default),&nbsp;&quot;native&quot;&nbsp;fonts, or convert to the&nbsp;&quot;theme&quot;&nbsp;font&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-embed</code><i> string</i>]</dt>
<dd> <p> <br />
&nbsp;embed fonts, specified as a comma-separated list of EOT-format font files&nbsp; </p>
 </dd></dl>
<h3>emf - Enhanced MS Windows Metafile</h3>
<p> The following format specific options are available: </p>
<dl>
<dt>[<code>-m</code>]</dt>
<dd> <p> <br />
&nbsp;map to Arial&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-nf</code>]</dt>
<dd> <p> <br />
&nbsp;emulate narrow fonts&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-drawbb</code>]</dt>
<dd> <p> <br />
&nbsp;draw bounding box&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-p</code>]</dt>
<dd> <p> <br />
&nbsp;prune line ends&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-nfw</code>]</dt>
<dd> <p> <br />
&nbsp;Newer versions of MS Windows&nbsp;(2000, XP, Vista, 7, ...)&nbsp;will not accept WMF/EMF files generated when this option is set and the input contains text. But if this option is not set, then the WMF/EMF driver will estimate interletter spacing of text using a very coarse heuristic. This may result in ugly looking output. On the other hand, OpenOffice can still read EMF/WMF files where pstoedit delegates the calculation of the inter letter spacing to the program reading the WMF/EMF file. So if the generated WMF/EMF file shall never be processed under MS Windows, use this option. If WMF/EMF files with high precision text need to be generated under&nbsp;*nix the only option is to use the -pta option of pstoedit. However that causes every text to be split into single characters which makes the text hard to edit afterwards. Hence the -nfw option provides a sort of compromise between portability and nice to edit but still nice looking text. Again - this option has no meaning when pstoedit is executed under MS Windows anyway. In that case the output is portable but nevertheless not split and still looks fine.&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-winbb</code>]</dt>
<dd> <p> <br />
&nbsp;let the MS Windows API calculate the Bounding Box&nbsp;(MS Windows only)&nbsp; </p>
 </dd></dl>
<dl>
<dt>[<code>-OO</code>]</dt>
<dd> <p> <br />
&nbsp;generate OpenOffice compatible EMF file&nbsp; </p>
 </dd></dl>
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
<h3>CONTEXT FREE - CFDG</h3>
<p> The driver for the CFDG format (drvcfdg) defines one shape per page of PostScript, but only the first shape is actually rendered (unless the user edits the generated CFDG code, of course). CFDG does not support multi-page output, so this probably is a reasonable thing to do. </p>
<p> For more on Context Free see: <code><a rel="nofollow" href="http://www.contextfreeart.org/">http://www.contextfreeart.org/</a></code> </p>
<h3>LaTeX2E</h3>
<dl>
<dt><code>*</code></dt>
<dd> <p> LaTeX2e&#8217;s picture environment is not very powerful. As a result, many elementary PostScript constructs are ignored -- fills, line thicknesses (besides &quot;thick&quot; and &quot;thin&quot;), and dash patterns, to name a few. Furthermore, complex pictures may overrun TeX&#8217;s memory capacity. (The eepic package overcomes many such restrictions.) </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Some PostScript constructs are not supported directly by &quot;picture&quot;, but can be handled by external packages. If a figure uses color, the top-level document will need to do a &quot;\usepackage{color}&quot; or &quot;\usepackage{xcolor}&quot;. And if a figure contains rotated text, the top-level document will need to do a &quot;\usepackage{rotating}&quot;. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> All lengths, coordinates, and font sizes output by the output format driver are in terms of \unitlength, so scaling a figure is simply a matter of doing a &quot;\setlength{\unitlength}{...}&quot;. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> The output format driver currently supports one output format driver specific option, &quot;integers&quot;, which rounds all lengths, coordinates, and font sizes to the nearest integer. This makes hand-editing the picture a little nicer. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Why is this output format driver useful? One answer is portability; any LaTeX2e system can handle the picture environment, even if it cannot handle PostScript graphics. (pdfLaTeX comes to mind here.) A second answer is that pictures can be edited easily to contain any arbitrary LaTeX2e code. For instance, the text in a figure can be modified to contain complex mathematics, non-Latin alphabets, bibliographic citations, or -- the real reason Scott wrote the LaTeX2e output format driver -- hyperlinks to the surrounding document (with help from the hyperref package). </p>
 </dd></dl>
<h3>CREATING A NEW OUTPUT FORMAT DRIVER</h3>
<p> To implement a new output format driver you can start from drvsampl.cpp and drvsampl.h. See also comments in drvbase.h and drvfuncs.h for an explanation of methods that should be implemented for a new output format driver. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> A default PostScript interpreter to be called by pstoedit is specified at compile time. You can overwrite the default by setting the GS environment variable to the name of a suitable PostScript interpreter. </p>
<p> You can check which name of a PostScript interpreter was compiled into pstoedit using: <code>pstoedit</code> <code>-help -v</code>. </p>
<p> See the Ghostscript manual for descriptions of environment variables used by Ghostscript, most importantly GS_FONTPATH and GS_LIB; other environment variables also affect output to display, print, and additional filtering and processing. See the related documentation. </p>
<p> pstoedit allocates temporary files using the function <i><a href="/docs/linux/man/3-tempnam/">tempnam</a></i>(3). Thus the location for temporary files might be controllable by other environment variables used by this function. See the <i><a href="/docs/linux/man/3-tempnam/">tempnam</a></i>(3) manpage for descriptions of environment variables used. On UNIX like system this is probably the TMPDIR variable, on DOS/WINDOWS either TMP or TEMP. </p>
<h2>TROUBLE SHOOTING</h2>
<p> If you have problems with pstoedit first try whether Ghostscript successfully displays your file. If yes, then try <code>pstoedit</code> <code>-f ps</code> <i>infile.ps</i> <i>testfile.ps</i> and check whether <i>testfile.ps</i> still displays correctly using Ghostscript. If this file does not look correctly then there seems to be a problem with pstoedit&#8217;s PostScript frontend. If this file looks good but the output for a specific format is wrong, the problem is probably in the output format driver for the specific format. In either case send bug fixes and reports to the author. </p>
<p> A common problem with PostScript files is that the PostScript file redefines one of the standard PostScript operators inconsistently. There is no effect of this if you just print the file since the original PostScript &quot;program&quot; uses these new operators in the new meaning and does not use the original ones anymore. However, when run under the control of pstoedit, these operators are expected to work with the original semantics. </p>
<p> So far I&#8217;ve seen redefinitions for: </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> lt - &quot;less-then&quot; to mean &quot;draw a line to&quot; </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> string - &quot;create a string object&quot; to mean &quot;draw a string&quot; </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> length - &quot;get the length of e.g. a string&quot; to a &quot;float constant&quot; </p>
 </dd></dl>
<p> I&#8217;ve included work-arounds for the ones mentioned above, but some others could show up in addition to those. </p>
<h2>RESTRICTIONS</h2>
<dl>
<dt><code>*</code></dt>
<dd> <p> Non-standard fonts (e.g. TeX bitmap fonts) are mapped to a default font which can be changed using the <code>-df</code> option. pstoedit chooses the size of the replacement font such that the width of the string in the original font is the same as with the replacement font. This is done for each text fragment displayed. Special character encoding support is limited in this case. If a character cannot be mapped into the target format, pstoedit displays a &#8216;#&#8216; instead. See also the -uchar option. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> pstoedit supports bitmap graphics only for some output format drivers. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Some output format drivers, e.g. the Gnuplot output format driver or the 3D output format driver (rpl, lwo, rib) do not support text. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> For most output format drivers pstoedit does not support clipping (mainly due to limitations in the target format). You can try to use the <code>-sclip</code> option to simulate clipping. However, this does not work in all cases as expected. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Special note about the Java output format drivers (java1 and java2). The java output format drivers generate a java source file that needs other files in order to be compiled and usable. These other files are Java classes (one applet and support classes) that allow stepping through the individual pages of a converted PostScript document. This applet can easily be activated from a html-document. See the contrib/java/java1/readme_java1.txt or contrib/java/java2/readme_java2.htm files for more details. </p>
 </dd></dl>
<h2>FAQS</h2>
<dl>
<dt>1.</dt>
<dd> <p> Why do letters like O or B get strange if converted to tgif/xfig using the <code>-dt</code> option? </p>
 </dd></dl>
<p> Most output format drivers do not support composite paths with intermediate gaps (moveto&#8217;s) and second do not support very well the (eo)fill operators of PostScript (winding rule). For such objects pstoedit breaks them into smaller objects whenever such a gap is found. This results in the &quot;hole&quot; being filled with black color instead of being transparent. Since version 3.11 you can try the <code>-ssp</code> option in combination with the xfig output format driver. </p>
<dl>
<dt>2.</dt>
<dd> <p> Why does pstoedit produce ugly results from PostScript files generated by dvips? </p>
 </dd></dl>
<p> This is because TeX documents usually use bitmap fonts. Such fonts cannot be used as native font in other format. So pstoedit replaces the TeX font with another native font. Of course, the replacement font will in most cases produce another look, especially if mathematical symbols are used. Try to use PostScript fonts instead of the bitmap fonts when generating a PostScript file from TeX or LaTeX. </p>
<h2>AUTHOR</h2>
<p> Wolfgang Glunz, <code>wglunz35_AT_pstoedit.net</code>, <code><a rel="nofollow" href="http://de.linkedin.com/in/wolfgangglunz">http://de.linkedin.com/in/wolfgangglunz</a></code> </p>
<h2>CANONICAL ARCHIVE SITE</h2>
<p> <code><a rel="nofollow" href="http://www.pstoedit.net/pstoedit/">http://www.pstoedit.net/pstoedit/</a></code> </p>
<p> At this site you also find more information about pstoedit and related programs and hints how to subscribe to a mailing list in order to get informed about new releases and bug-fixes. </p>
<p> If you like pstoedit - please express so also at Facebook <code><a rel="nofollow" href="http://www.facebook.com/pstoedit">http://www.facebook.com/pstoedit</a></code>. </p>
<h2>ACKNOWLEDGMENTS</h2>
<dl>
<dt><code>*</code></dt>
<dd> <p> Klaus Steinberger <code>Klaus.Steinberger_AT_physik.uni-muenchen.de</code> wrote the initial version of this manpage. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Lar Kaufman revised the increasingly complex command syntax diagrams and updated the structure and content of this manpage following release 2.5. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> David B. Rosen <code>rosen_AT_unr.edu</code> provided ideas and some PostScript code from his ps2aplot program. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Ian MacPhedran <code>Ian_MacPhedran_AT_engr.USask.CA</code> provided the xfig output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Carsten Hammer <code>chammer_AT_hermes.hrz.uni-bielefeld.de</code> provided the gnuplot output format driver and the initial DXF output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Christoph Jaeschke provided the OS/2 metafile (MET) output format driver. Thomas Hoffmann <code>thoffman_AT_zappa.sax.de</code> did some further updates on the OS/2 part. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Jens Weber <code>rz47b7_AT_PostAG.DE</code> provided the MS Windows metafile (WMF) output format driver, and a graphical user interface (GUI). </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> G. Edward Johnson <code>lorax_AT_nist.gov</code> provided the CGM Draw library used in the CGM output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Gerhard Kircher <code>kircher_AT_edvz.tuwien.ac.at</code> provided some bug fixes. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Bill Cheng <code>bill.cheng_AT_acm.org</code> provided help with the tgif format and some changes to tgif to make the output format driver easier to implement. <code><a rel="nofollow" href="http://bourbon.usc.edu:8001/">http://bourbon.usc.edu:8001/</a></code> </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Reini Urban <code>rurban_AT_sbox.tu-graz.ac.at</code> provided input for the extended DXF output format driver.(<code><a rel="nofollow" href="http://autocad.xarch.at/">http://autocad.xarch.at/</a></code>) </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Glenn M. Lewis <code>glenn_AT_gmlewis.com</code> provided RenderMan (RIB), Real3D (RPL), and LightWave 3D (LWO) output format drivers. (<code><a rel="nofollow" href="http://www.gmlewis.com/">http://www.gmlewis.com/</a></code>) </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Piet van Oostrum <code>piet_AT_cs.ruu.nl</code> made several bug fixes. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Lutz Vieweg <code>lkv_AT_mania.robin.de</code> provided several bug fixes and suggestions for improvements. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Derek B. Noonburg <code>derekn_AT_vw.ece.cmu.edu</code> and Rainer Dorsch <code>rd_AT_berlepsch.wohnheim.uni-ulm.de</code> isolated and resolved a Linux-specific core dump problem. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Rob Warner <code>rcw2_AT_ukc.ac.uk</code> made pstoedit compile under RiscOS. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Patrick Gosling <code>jpmg_AT_eng.cam.ac.uk</code> made some suggestions regarding the usage of pstoedit in Ghostscript&#8217;s SAFER mode. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Scott Pakin <code>scott+ps2ed_AT_pakin.org</code> for the Idraw output format driver and the autoconf support. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Peter Katzmann <code>p.katzmann_AT_thiesen.com</code> for the HPGL output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Chris Cox <code>ccox_AT_airmail.net</code> contributed the Tcl/Tk output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Thorsten Behrens <code>Thorsten_Behrens_AT_public.uni-hamburg.de</code> and Bjoern Petersen for reworking the WMF output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Leszek Piotrowicz <code>leszek_AT_sopot.rodan.pl</code> implemented the image support for the xfig driver and a JAVA based GUI. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Egil Kvaleberg <code>egil_AT_kvaleberg.no</code> contributed the pic output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Kai-Uwe Sattler <code>kus_AT_iti.cs.uni-magdeburg.de</code> implemented the output format driver for Kontour. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Scott Pakin, <code>scott+ps2ed_AT_pakin.org</code> provided the MetaPost and LaTeX2e and MS PowerPoint output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> The MS PowerPoint driver uses the libzip library - <code><a rel="nofollow" href="http://www.nih.at/libzip">http://www.nih.at/libzip</a></code>. Under MS Windows, this library is linked into the provided binary statically. Thanks to the whole libzip team. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Burkhard Plaum <code>plaum_AT_IPF.Uni-Stuttgart.de</code> added support for complex filled paths for the xfig output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Bernhard Herzog <code>herzog_AT_online.de</code> contributed the output format driver for sketch ( <code><a rel="nofollow" href="http://www.skencil.org/">http://www.skencil.org/</a></code> ) </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Rolf Niepraschk (<code>niepraschk_AT_ptb.de</code>) converted the HTML man page to LaTeX format. This allows generating the UNIX style and the HTML manual from this base format. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Several others sent smaller bug fixed and bug reports. Sorry if I do not mention them all here. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Gisbert W. Selke (<code>gisbert_AT_tapirsoft.de</code>) for the Java 2 output format driver. </p>
 </dd></dl>
<dl>
<dt><code>*</code></dt>
<dd> <p> Robert S. Maier (<code>rsm_AT_math.arizona.edu</code>) for many improvements on the libplot output format driver and for libplot itself. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> The authors of pstotext (<code>mcjones_AT_pa.dec.com</code> and <code>birrell_AT_pa.dec.com</code>) for giving me the permission to use their simple PostScript code for performing rotation. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Daniel Gehriger <code>gehriger_AT_linkcad.com</code> for his help concerning the handling of Splines in the DXF format. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Allen Barnett <code>libemf_AT_lignumcomputing.com</code> for his work on the libEMF which allows creating WMF/EMF files under *nix systems. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Dave <code>dave_AT_opaque.net</code> for providing the libming which is a multiplatform library for generating SWF files. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Masatake Yamoto for the introduction of autoconf, automake and libtool into pstoedit </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Bob Friesenhahn for his help and the building of the Magick++ API to ImageMagick. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> But most important: Peter Deutsch <code>ghost_AT_aladdin.com</code> and Russell Lang <code>gsview_AT_ghostgum.com.au</code> for their help and answers regarding Ghostscript and gsview. </p>
 </dd></dl>
<h2>LEGAL NOTICES</h2>
<p> Trademarks mentioned are the property of their respective owners. </p>
<p> Some code incorporated in the pstoedit package is subject to copyright or other intellectual property rights or restrictions including attribution rights. See the notes in individual files. </p>
<p> pstoedit is controlled under the Free Software Foundation GNU Public License (GPL). However, this does not apply to importps and the additional plugins. </p>
<p> Aladdin Ghostscript is a redistributable software package with copyright restrictions controlled by Aladdin Software. </p>
<p> pstoedit has no other relation to Ghostscript besides calling it in a subprocess. </p>
<p> The authors, contributors, and distributors of pstoedit are not responsible for its use for any purpose, or for the results generated thereby. </p>
<p> Restrictions such as the foregoing may apply in other countries according to international conventions and agreements. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">FROM THE COMMAND SHELL</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">FROM GSVIEW</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">FROM PROGRAMS THAT SUPPORT THE ALDUS GRAPHIC IMPORT FILTER INTERFACE</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAG">DESCRIPTION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAH">RELEASE LEVEL</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">USE</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">PRINCIPLE OF CONVERSION</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">NOTES</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAL">OPTIONS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAM">GENERAL OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">TEXT AND FONT HANDLING RELATED OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">DRAWING RELATED OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">DEBUG OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">INPUT AND OUTFILE FILE ARGUMENTS</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAR">AVAILABLE FORMATS AND THEIR SPECIFIC OPTIONS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAS">Format group: psf ps debug dump gs ps2ai </a></dt>
<dd>  </dd>
<dt><a href="#lbAT">sample - sample driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">idraw - Interviews draw format (EPS)</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">Format group: fig xfig tfig </a></dt>
<dd>  </dd>
<dt><a href="#lbAW">tgif - Tgif .obj format</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">gnuplot - gnuplot format</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">svm - StarView/OpenOffice.org metafile</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">vtk - VTK driver: if you do not want to see this, uncomment the corresponding line in makefile and make again</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">tk - tk and/or tk applet source code</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">cfdg - Context Free Design Grammar</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">gschem - gschem format</a></dt>
<dd>  </dd>
<dt><a href="#lbBD">pcb-rnd - pcb-rnd format</a></dt>
<dd>  </dd>
<dt><a href="#lbBE">pcbfill - pcb format with fills</a></dt>
<dd>  </dd>
<dt><a href="#lbBF">pcb - pcb format</a></dt>
<dd>  </dd>
<dt><a href="#lbBG">pcbi - engrave data - insulate/PCB format</a></dt>
<dd>  </dd>
<dt><a href="#lbBH">Format group: hpgl pcl </a></dt>
<dd>  </dd>
<dt><a href="#lbBI">pic - PIC format for troff et.al.</a></dt>
<dd>  </dd>
<dt><a href="#lbBJ">noixml - Nemetschek NOI XML format</a></dt>
<dd>  </dd>
<dt><a href="#lbBK">latex2e - LaTeX2e picture format</a></dt>
<dd>  </dd>
<dt><a href="#lbBL">mma - Mathematica graphics</a></dt>
<dd>  </dd>
<dt><a href="#lbBM">asy - Asymptote Format</a></dt>
<dd>  </dd>
<dt><a href="#lbBN">mpost - MetaPost format</a></dt>
<dd>  </dd>
<dt><a href="#lbBO">sk - Sketch format</a></dt>
<dd>  </dd>
<dt><a href="#lbBP">text - text in different forms </a></dt>
<dd>  </dd>
<dt><a href="#lbBQ">kil - .kil format for Kontour</a></dt>
<dd>  </dd>
<dt><a href="#lbBR">pdf - Adobe&#8217;s Portable Document Format</a></dt>
<dd>  </dd>
<dt><a href="#lbBS">java2 - java 2 source code</a></dt>
<dd>  </dd>
<dt><a href="#lbBT">java1 - java 1 applet source code</a></dt>
<dd>  </dd>
<dt><a href="#lbBU">Format group: dxf dxf_14 dxf_s </a></dt>
<dd>  </dd>
<dt><a href="#lbBV">rpl - Real3D Programming Language format</a></dt>
<dd>  </dd>
<dt><a href="#lbBW">rib - RenderMan Interface Bytestream</a></dt>
<dd>  </dd>
<dt><a href="#lbBX">lwo - LightWave 3D object format</a></dt>
<dd>  </dd>
<dt><a href="#lbBY">cairo - cairo driver</a></dt>
<dd>  </dd>
<dt><a href="#lbBZ">gcode - emc2 gcode format</a></dt>
<dd>  </dd>
<dt><a href="#lbCA">magick - MAGICK driver compatible with version 6.9.11 of ImageMagick.</a></dt>
<dd>  </dd>
<dt><a href="#lbCB">Format group: gmfa gmfb plot plot-pnm plot-cgm plot-ai plot-svg plot-ps plot-fig plot-pcl plot-hpgl plot-tek </a></dt>
<dd>  </dd>
<dt><a href="#lbCC">pptx - PresentationML (PowerPoint) format</a></dt>
<dd>  </dd>
<dt><a href="#lbCD">emf - Enhanced MS Windows Metafile</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbCE">NOTES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbCF">AUTOTRACE</a></dt>
<dd>  </dd>
<dt><a href="#lbCG">PS2AI</a></dt>
<dd>  </dd>
<dt><a href="#lbCH">METAPOST</a></dt>
<dd>  </dd>
<dt><a href="#lbCI">CONTEXT FREE - CFDG</a></dt>
<dd>  </dd>
<dt><a href="#lbCJ">LaTeX2E</a></dt>
<dd>  </dd>
<dt><a href="#lbCK">CREATING A NEW OUTPUT FORMAT DRIVER</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbCL">ENVIRONMENT VARIABLES</a></dt>
<dd>  </dd>
<dt><a href="#lbCM">TROUBLE SHOOTING</a></dt>
<dd>  </dd>
<dt><a href="#lbCN">RESTRICTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbCO">FAQS</a></dt>
<dd>  </dd>
<dt><a href="#lbCP">AUTHOR</a></dt>
<dd>  </dd>
<dt><a href="#lbCQ">CANONICAL ARCHIVE SITE</a></dt>
<dd>  </dd>
<dt><a href="#lbCR">ACKNOWLEDGMENTS</a></dt>
<dd>  </dd>
<dt><a href="#lbCS">LEGAL NOTICES</a></dt>
<dd>  </dd></dl>
