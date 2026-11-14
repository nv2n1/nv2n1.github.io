---
title: "gropdf(1)"
name: "gropdf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gropdf/"
description: "gropdf – PDF driver for groff"
---

<h2 class="name">NAME</h2>
<p> gropdf &#8211; PDF driver for groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-dels</code> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-p </code><i>paper-size</i> ] #.OP -w n [<code>-u</code> [<i>cmapfile</i>]] [ <code>-y </code><i>foundry</i> ] [<i>file</i> &#8230;] <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gropdf</code> translates the output of GNU <code>troff</code> to PDF. Normally <code>gropdf</code> should be invoked by using the groff command with a <code>-Tpdf</code> option. If no files are given, <code>gropdf</code> reads the standard input. A filename of <code>&#8211;</code> also causes <code>gropdf</code> to read the standard input. PDF output is written to the standard output. When <code>gropdf</code> is run by <code>groff</code> options can be passed to <code>gropdf</code> using <code>groff</code>&#8216;s <code>-P</code> option. </p>
<p> See section &#8220;Font Installation&#8221; below for a guide how to install fonts for <code>gropdf</code>.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-d</code></p>
<dd> Include debug information as comments within the PDF. Also produces an uncompressed PDF.</p>
<dt><code>-e</code></p>
<dd> Forces <code>gropdf</code> to embed <i>all</i> fonts (even the 14 base PDF fonts).</p>
<dt><code>-F</code><i> dir</i></p>
<dd> Prepend directory <i>dir</i>/dev<i>name</i> to the search path for font, and device description files; <i>name</i> is the name of the device, usually <code>pdf</code>.</p>
<dt><code>-I</code><i> dir</i></p>
<dd> This option may be used to add a directory to the search path for files named in <code>\X&#8217;pdf: pdfpic&#8217;</code> escape. The current directory is always searched first. This option may be specified more than once; the directories are then searched in the order specified.</p>
<dt>
<dd> No directory search is performed for files with an absolute file name.</p>
<dt><code>-l</code></p>
<dd> Orient the document in landscape format.</p>
<dt><code>-p</code><i> paper-size</i></p>
<dd> Set physical dimension of output medium. This overrides the <code>papersize</code>, <code>paperlength</code>, and <code>paperwidth</code> commands in the <i>DESC</i> file; it accepts the same arguments as the <code>papersize</code> command. See <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for details.</p>
<dt><code>-s</code></p>
<dd> Append a comment line to end of PDF showing statistics, i.e. number of pages in document. Ghostscript&#8217;s <code>ps2pdf</code> complains about this line if it is included, but works anyway.</p>
<dt><code>-u</code></p>
<dd> [<i>cmapfile</i>] <code>Gropdf</code> normally includes a ToUnicode CMap with any font created using <i>text.enc</i> as the encoding file, this makes it easier to search for words which contain ligatures. You can include your own CMap by specifying a <i>cmapfile</i> or have no CMap at all by omitting the argument.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Print the version number and exit.</p>
<dt><code>-y</code><i> foundry</i></p>
<dd> Set the foundry to use for selecting fonts of the same name.</dl>
<h2>USAGE</h2>
<p> The input to <code>gropdf</code> must be in the format output by <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). This is described in <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5). </p>
<p> In addition, the device and font description files for the device used must meet certain requirements: The resolution must be an integer multiple of~72 times the <code>sizescale</code>. The <code>pdf</code> device uses a resolution of 72000 and a sizescale of 1000. </p>
<p> The device description file must contain a valid paper size; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more information. <code>gropdf</code> uses the same Type~1 Adobe PostScript fonts as the <code>grops</code> device driver. Although the PDF Standard allows the use of other font types (like TrueType) this implementation only accepts the Type~1 PostScript font. Fewer Type~1 fonts are supported natively in PDF documents than the standard 35 fonts supported by <code>grops</code> and all PostScript printers, but all the fonts are available since any which aren&#8217;t supported natively are automatically embedded in the PDF. </p>
<p> <code>gropdf</code> supports the concept of foundries, that is different versions of basically the same font. During install a <i>Foundry</i> file controls where fonts are found and builds <code>groff</code> fonts from the files it discovers on your system. </p>
<p> Each font description file must contain a command</p>
<dl>
<dt>
<dd> <code>internalname&nbsp;</code><i>psname</i></dl>
<p> which says that the PostScript name of the font is <i>psname</i>. Lines starting with <code>#</code> and blank lines are ignored. The code for each character given in the font file must correspond to the code in the default encoding for the font. This code can be used with the <code>\N</code> escape sequence in <code>troff</code> to select the character, even if the character does not have a groff name. Every character in the font file must exist in the PostScript font, and the widths given in the font file must match the widths used in the PostScript font. </p>
<p> Note that <code>gropdf</code> is currently only able to display the first 256 glyphs in any font. This restriction will be lifted in a later version. </p>
<p> <code>gropdf</code> can automatically include the downloadable fonts necessary to print the document. Fonts may be in PFA or PFB format. </p>
<p> Any downloadable fonts which should, when required, be included by <code>gropdf</code> must be listed in the file <i>/usr/:share/:groff/:1.22.4/:font/devpdf/download</i>; this should consist of lines of the form</p>
<dl>
<dt>
<dd> <i>foundry font filename</i></dl>
<p> where <i>foundry</i> is the foundry name or blank for the default foundry. <i>font</i> is the PostScript name of the font, and <i>filename</i> is the name of the file containing the font; lines beginning with <code>#</code> and blank lines are ignored; fields must be separated by tabs (spaces are <code>not</code> allowed); <i>filename</i> is searched for using the same mechanism that is used for groff font metric files. The <i>download</i> file itself is also searched for using this mechanism; currently, only the first found file in the font path is used. Foundry names are usually a single character (such as &#8216;U&#8217; for the URW Foundry) or blank for the default foundry. This default uses the same fonts as <code>ghostscript</code> uses when it embeds fonts in a PDF file. </p>
<p> In the default setup there are styles called <code>R</code>, <code>I</code>, <code>B</code>, and <code>BI</code> mounted at font positions 1 to~4. The fonts are grouped into families <code>A</code>, <code>BM</code>, <code>C</code>, <code>H</code>, <code>HN</code>, <code>N</code>, <code>P</code>, and~<code>T</code> having members in each of these styles:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>AR</code></p>
<dd> AvantGarde-Book <code>AI</code> AvantGarde-BookOblique <code>AB</code> AvantGarde-Demi <code>ABI</code> AvantGarde-DemiOblique <code>BMR</code> Bookman-Light <code>BMI</code> Bookman-LightItalic <code>BMB</code> Bookman-Demi <code>BMBI</code> Bookman-DemiItalic <code>CR</code> Courier <code>CI</code> Courier-Oblique <code>CB</code> Courier-Bold <code>CBI</code> Courier-BoldOblique <code>HR</code> Helvetica <code>HI</code> Helvetica-Oblique <code>HB</code> Helvetica-Bold <code>HBI</code> Helvetica-BoldOblique <code>HNR</code> Helvetica-Narrow <code>HNI</code> Helvetica-Narrow-Oblique <code>HNB</code> Helvetica-Narrow-Bold <code>HNBI</code> Helvetica-Narrow-BoldOblique <code>NR</code> NewCenturySchlbk-Roman <code>NI</code> NewCenturySchlbk-Italic <code>NB</code> NewCenturySchlbk-Bold <code>NBI</code> NewCenturySchlbk-BoldItalic <code>PR</code> Palatino-Roman <code>PI</code> Palatino-Italic <code>PB</code> Palatino-Bold <code>PBI</code> Palatino-BoldItalic <code>TR</code> Times-Roman <code>TI</code> Times-Italic <code>TB</code> Times-Bold <code>TBI</code> Times-BoldItalic</dl>
</dl>
<p> There is also the following font which is not a member of a family:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ZCMI</code></p>
<dd> ZapfChancery-MediumItalic</dl>
</dl>
<p> There are also some special fonts called <code>S</code> for the PS Symbol font. The lower case greek characters are automatically slanted (to match the SymbolSlanted font (SS) available to PostScript). Zapf Dingbats is available as <code>ZD</code>, the &quot;hand pointing left&quot; glyph (\[lh]) is available since it has been defined using the \X&#8217;pdf: xrev&#8217; extension which reverses the direction of letters within words. </p>
<p> The default color for <code>\m</code> and <code>\M</code> is black. </p>
<p> <code>gropdf</code> understands some of the X~commands produced using the <code>\X</code> escape sequences supported by <code>grops.</code> Specifically, the following is supported.</p>
<dl>
<dt><code>\X&#8217;ps: invis&#8217;</code></p>
<dd> Suppress output.</p>
<dt><code>\X&#8217;ps: endinvis&#8217;</code></p>
<dd> Stop suppressing output.</p>
<dt><code>\X&#8217;ps: exec gsave currentpoint 2 copy translate </code><i>n</i> rotate neg exch neg exch translate&#8217;</p>
<dd> where <i>n</i> is the angle of rotation. This is to support the <i>align</i> command in <code>gpic</code>.</p>
<dt><code>\X&#8217;ps: exec grestore&#8217;</code></p>
<dd> Again used by <code>gpic</code> to restore after rotation.</p>
<dt><code>\X&#8217;ps: exec </code><i>n </i><code>setlinejoin&#8217;</code></p>
<dd> where <i>n</i> can be one of the following values.</p>
<dt>
<dd> 0 = Miter join<br />
 1 = Round join<br />
 2 = Bevel join</p>
<dt><code>\X&#8217;ps: exec </code><i>n </i><code>setlinecap&#8217;</code></p>
<dd> where <i>n</i> can be one of the following values.</p>
<dt>
<dd> 0 = Butt cap<br />
 1 = Round cap, and<br />
 2 = Projecting square cap</dl>
<dl>
<dt><code>\X&#8217;ps: &#8230; pdfmark&#8217;</code></p>
<dd> All the <i>pdfmark</i> macros installed by using <i>-m pdfmark</i> or <i>-m mspdf</i> (see documentation in <i>pdfmark.pdf</i>). A subset of these macros are installed automatically when you use <code>-Tpdf</code> so you should not need to use &#8216;-m pdfmark&#8217; for using most of the PDF functionality.</dl>
<p> <code>gropdf</code> also supports a subset of the commands introduced in present.tmac. Specifically it supports:-</p>
<dl>
<dt>
<dd> PAUSE<br />
 BLOCKS<br />
 BLOCKE</dl>
<p> Which allows you to create presentation type PDFs. Many of the other commands are already available in other macro packages. </p>
<p> These commands are implemented with <code>groff</code> X commands:- </p>
<dl>
<dt><code>\X&#8217;ps: exec %%%%PAUSE</code></p>
<dd> The section before this is treated as a block and is introduced using the current BLOCK transition setting (see &#8216;pdf: transition&#8217; below). This command can be introduced using the macro <code>.pdfpause</code>.</p>
<dt><code>\X&#8217;ps: exec %%%%BEGINONCE</code></p>
<dd> Any text following this command (up to %%%%ENDONCE) is shown only once, the next %%%%PAUSE will remove it. If producing a non presentation pdf, i.e. ignoring the pauses, see <i>GROPDF_NOSLIDE</i> below, this text is ignored.</dl>
<dl>
<dt><code>\X&#8217;ps: exec %%%%ENDONCE</code></p>
<dd> This terminates the block defined by %%%%BEGINONCE. This pair of commands is what implements the .BLOCKS Once/.BLOCKE commands in present.tmac.</dl>
<p> The <code>mom</code> macro set already has integration with these extensions so you can build slides with <code>mom</code>. </p>
<p> If you use present.tmac with <code>gropdf</code> there is no need to run the program <code><a href="/docs/linux/man/1-presentps/">presentps</a></code>(1) since the output will already be a presentation pdf. </p>
<p> All other <code>ps:</code> tags are silently ignored. </p>
<p> One <code>\X</code> special used by the DVI driver is also recognised:</p>
<dl>
<dt><code>\X&#8217;papersize=</code><i>paper-size</i><code>&#8216;</code></p>
<dd> where the <i>paper-size</i> parameter is the same as the <code>papersize</code> command. See <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for details. This means that you can alter the page size at will within the PDF file being created by <code>gropdf</code>. If you do want to change the paper size, it must be done before you start creating the page.</dl>
<p> In addition, <code>gropdf</code> supports its own suite of <code>pdf:</code> tags. The following tags are supported:</p>
<dl>
<dt><code>\X&#8217;pdf: pdfpic </code><i>file alignment width height line-length</i><code>&#8216;</code></p>
<dd> Place an image of the specified <i>width</i> containing the PDF drawing from file <i>file</i> of desired <i>width</i> and <i>height</i> (if <i>height</i> is missing or zero then it is scaled proportionally). If <i>alignment</i> is <code>-L</code> the drawing is left aligned. If it is <code>-C</code> or <code>-R</code> a <i>linelength</i> greater than the width of the drawing is required as well. If <i>width</i> is specified as zero then the width is scaled in proportion to the height.</p>
<dt><code>\X&#8217;pdf: xrev&#8217;</code></p>
<dd> This toggles a flag which reverses the direction of printing <i>letter by letter</i>, i.e., each separate letter is reversed, not the entire word. This is useful for reversing the direction of glyphs in the Dingbats font. To return to normal printing repeat the command again.</p>
<dt><code>\X&#8217;pdf: markstart </code><i>/ANN definition</i><code>&#8216;</code></p>
<dd> The macros which support PDF Bookmarks use this call internally to start the definition of bookmark hotspot (user will have called &#8216;.pdfhref~L&#8217; with the text which will become the &#8216;hot spot&#8217; region). Normally this is never used except from within the pdfmark macros.</p>
<dt><code>\X&#8217;pdf: markend&#8217;</code></p>
<dd> The macros which support PDF Bookmarks use this call internally to stop the definition of bookmark hotspot (user will have called &#8216;.pdfhref~L&#8217; with the text which will become the &#8216;hot spot&#8217; region). Normally this is never used except from within the pdfmark macros.</p>
<dt><code>\X&#8217;pdf: marksuspend&#8217;</code></p>
<dd> <code>\X&#8217;pdf: markrestart&#8217;</code> If you are using page traps to produce headings, footings, etc., you need to use these in case a &#8216;hot spot&#8217; crosses a page boundary, otherwise any text output by the heading or footing macro will be marked as part of the &#8216;hot spot&#8217;. To stop this happening just place &#8216;.pdfmarksuspend&#8217; and &#8216;.pdfmarkrestart&#8217; at the start and end of the page trap macro, respectively. (These are just convenience macros which emit the \X code. These macros must only be used within page traps.)</p>
<dt><code>\X&#8217;pdf: transition&#8217;</code>feature mode duration dimension motion direction scale bool</p>
<dd> where</p>
<dt>
<dd> <i>feature</i> can be either SLIDE or BLOCK. When it is SLIDE the transition is used when a new slide is introduced to the screen, if BLOCK then this transition is used for the individual blocks which make up the slide.<br />
 <i>mode</i> is the transition type between slides:-</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>Split</code> &#8211; Two lines sweep across the screen, revealing the new page. The lines may be either horizontal or vertical and may move inward from the edges of the page or outward from the center, as specified by the <i>dimension</i> and <i>motion</i> entries, respectively.<br />
 <code>Blinds</code> &#8211; Multiple lines, evenly spaced across the screen, synchronously sweep in the same direction to reveal the new page. The lines may be either horizontal or vertical, as specified by the <i>dimension</i><br />
&nbsp;entry. Horizontal lines move downward; vertical lines move to the right.<br />
 <code>Box</code> &#8211; A rectangular box sweeps inward from the edges of the page or outward from the center, as specified by the <i>motion</i> entry, revealing the new page.<br />
 <code>Wipe</code> &#8211; A single line sweeps across the screen from one edge to the other in the direction specified by the <i>direction</i> entry, revealing the new page.<br />
 <code>Dissolve</code> &#8211; The old page dissolves gradually to reveal the new one.<br />
 <code>Glitter</code> &#8211; Similar to Dissolve, except that the effect sweeps across the page in a wide band moving from one side of the screen to the other in the direction specified by the <i>direction</i> entry.<br />
 <code>R</code> &#8211; The new page simply replaces the old one with no special transition effect; the <i>direction</i> entry shall be ignored.<br />
 <code>Fly</code> &#8211; (PDF 1.5) Changes are flown out or in (as specified by <i>motion</i>), in the direction specified by <i>direction</i>, to or from a location that is offscreen except when <i>direction</i> is <code>None</code>.<br />
 <code>Push</code> &#8211; (PDF 1.5) The old page slides off the screen while the new page slides in, pushing the old page out in the direction specified by <i>direction</i>.<br />
 <code>Cover</code> &#8211; (PDF 1.5) The new page slides on to the screen in the direction specified by <i>direction</i>, covering the old page.<br />
 <code>Uncover</code> &#8211; (PDF 1.5) The old page slides off the screen in the direction specified by <i>direction</i>, uncovering the new page in the direction specified by <i>direction</i>.<br />
 <code>Fade</code> &#8211; (PDF 1.5) The new page gradually becomes visible through the old one.</dl>
</dl>
<dt>
<dd> <i>duration</i> is the length of the transition in seconds (default 1).</dl>
<dl>
<dt>
<dd> <i>dimension</i> (Optional; <code>Split</code> and <code>Blinds</code> transition styles only) The dimension in which the specified transition effect shall occur: <code>H</code> Horizontal, or <code>V</code> Vertical.</dl>
<dl>
<dt>
<dd> <i>motion</i> (Optional; <code>Split</code>, <code>Box</code> and <code>Fly</code> transition styles only) The direction of motion for the specified transition effect: <code>I</code> Inward from the edges of the page, or <code>O</code> Outward from the center of the page.</dl>
<dl>
<dt>
<dd> <i>direction</i> (Optional; <code>Wipe</code>, <code>Glitter</code>, <code>Fly</code>, <code>Cover</code>, <code>Uncover</code> and <code>Push</code> transition styles only) The direction in which the specified transition effect shall moves, expressed in degrees counterclockwise starting from a left-to-right direction. If the value is a number, it shall be one of: <code>0</code> = Left to right, <code>90</code> = Bottom to top (Wipe only), <code>180</code> = Right to left (Wipe only), <code>270</code> = Top to bottom, <code>315</code> = Top-left to bottom-right (Glitter only) The value can be <code>None</code>, which is relevant only for the <code>Fly</code> transition when the value of <i>scale</i> is not 1.0.</dl>
<dl>
<dt>
<dd> <i>scale</i> (Optional; PDF 1.5; <code>Fly</code> transition style only) The starting or ending scale at which the changes shall be drawn. If <i>motion</i> specifies an inward transition, the scale of the changes drawn shall progress from <i>scale</i> to 1.0 over the course of the transition. If <i>motion</i> specifies an outward transition, the scale of the changes drawn shall progress from 1.0 to <i>scale</i> over the course of the transition</dl>
<dl>
<dt>
<dd> <i>bool</i> (Optional; PDF 1.5; <code>Fly</code> transition style only) If <code>true</code>, the area that shall be flown in is rectangular and opaque.</dl>
<dl>
<dt>
<dd> This command can be used by calling the macro <code>.pdftransition</code> using the parameters described above. Any of the parameters may be replaced with a &quot;.&quot; which signifies the parameter retains its previous value, also any trailing missing parameters are ignored.</dl>
<dl>
<dt>
<dd> <code>Note:</code> not all PDF Readers support any or all these transitions.</dl>
<h3>Importing graphics</h3>
<p> <code>gropdf</code> only supports importing other PDF files as graphics. But that PDF file may contain any of the graphic formats supported by the PDF standard (such as JPEG, PNG, GIF, etc.). So any application which outputs PDF can be used as an embedded file in <code>gropdf</code>. The PDF file you wish to insert must be a single page and the drawing must just fit inside the media size of the PDF file. So, in <code><a href="/docs/linux/man/1-inkscape/">inkscape</a></code>(1) or <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) (for example) make sure the canvas size just fits the image. </p>
<p> The PDF parser used in <code>gropdf</code> has not been rigorously tested with all possible applications which produce PDFs. If you find a single page PDF which fails to import properly, it is worth running it through the <code><a href="/docs/linux/man/1-pdftk/">pdftk</a></code>(1) program by issuing the command:</p>
<dl>
<dt>
<dd>
<p> <code>pdftk</code> <i>oldfile.pdf</i> <code>output</code> <i>newfile.pdf</i></dl>
<p> You may find that <i>newfile.pdf</i> will now load successfully.</p>
<h3>TrueType and other font formats</h3>
<p> <code>gropdf</code> does not support any other fonts except Adobe Type 1 (PFA or PFB).</p>
<h2>FONT INSTALLATION</h2>
<p> This section gives a summary of the above explanations; it can serve as a step-by-step font installation guide for <code>gropdf</code>.</p>
<dl>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Convert your font to something groff understands. This is either a PostScript Type~1 font in either PFA or PFB, together with an AFM file.</p>
<dt>
<dd> The very first line in a PFA/PFB file contains this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>%!PS-AdobeFont-1.0:</code></dl>
</dl>
<dt>
<dd> A PFB file has this also in the first line, but the string is preceded with some binary bytes.</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Convert the AFM file to a groff font description file with the <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1) program. An example call is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> afmtodit Foo-Bar-Bold.afm map/textmap FBB</dl>
</dl>
<dt>
<dd> which converts the metric file &#8216;Foo-Bar-Bold.afm&#8217; to the groff font &#8216;FBB&#8217;. If you have a font family which comes with normal, bold, italic, and bold italic faces, it is recommended to use the letters <code>R</code>, <code>B</code>, <code>I</code>, and <code>BI</code>, respectively, as postfixes in the groff font names to make groff&#8217;s &#8216;.fam&#8217; request work. An example is groff&#8217;s built-in Times-Roman font: The font family name is <code>T</code>, and the groff font names are <code>TR</code>, <code>TB</code>, <code>TI</code>, and <code>TBI</code>.</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Install both the groff font description files and the fonts in a &#8216;devpdf&#8217; subdirectory of the font path which groff finds. See section &#8220;Environment&#8221; in <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) for the actual value of the font path. Note that groff doesn&#8217;t use the AFM files (but it is a good idea to store them anyway).</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Register all fonts which must be downloaded to the printer in the <i>devpdf/download</i> file. Only the first occurrence of this file in the font path is read. This means that you should copy the default <i>download</i> file to the first directory in your font path and add your fonts there. To continue the above example we assume that the PS font name for Foo-Bar-Bold.pfa is &#8216;XY-Foo-Bar-Bold&#8217; (the PS font name is stored in the <code>internalname</code> field in the <i>FBB</i> file) and belongs to foundry &#8216;F&#8217; thus the following line should be added to <i>download</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>F XY-Foo-Bar-Bold Foo-Bar-Bold.pfa</code></dl>
<p> Use a tab character to separate the fields, and the &#8216;foundry&#8217; field should be null for the default foundry.</dl>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. If, in the <i>download</i> file, the font file has been specified with a full path, no directories are searched. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</p>
<dt><i>GROPDF_NOSLIDE</i></p>
<dd> If this is set true, <code>gropdf</code> will ignore all commands which produce a presentation pdf, and produce a normal pdf instead.</p>
<dt><i>SOURCE_DATE_EPOCH</i></p>
<dd> A timestamp (expressed as seconds since the Unix epoch) to use as the creation timestamp in place of the current time.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/</i>F</p>
<dd> Font description file for font~<i>F</i>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/</i>U-F</p>
<dd> Font description file for font~<i>F</i> (using foundry~<i>U</i> rather than the default foundry).</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/download</i></p>
<dd> List of downloadable fonts.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/Foundry</i></p>
<dd> A Perl script used during install to locate suitable fonts.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devpdf/enc/text.enc</i></p>
<dd> Encoding used for text fonts.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/pdf.tmac</i></p>
<dd> Macros for use with <code>gropdf</code>; automatically loaded by <code>troffrc</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5) </p>
<h2>Index</h2>
