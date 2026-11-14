---
title: "grops(1)"
name: "grops"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grops/"
description: "grops – PostScript driver for groff"
---

<h2 class="name">NAME</h2>
<p> grops &#8211; PostScript driver for groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-glmv</code> ] [ <code>-b </code><i>n</i> ] [ <code>-c </code><i>n</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-p </code><i>papersize</i> ] [ <code>-P </code><i>prologue</i> ] [ <code>-w </code><i>n</i> ] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>grops</code> translates the output of GNU <code>troff</code> to PostScript. Normally <code>grops</code> should be invoked by using the groff command with a <code>-Tps</code> option. (Actually, this is the default for groff.) If no files are given, <code>grops</code> reads the standard input. A filename of <code>&#8211;</code> also causes <code>grops</code> to read the standard input. PostScript output is written to the standard output. When <code>grops</code> is run by <code>groff</code> options can be passed to <code>grops</code> using <code>groff</code>&#8216;s <code>-P</code> option. </p>
<p> Note that <code>grops</code> doesn&#8217;t produce a valid document structure (conforming to the Document Structuring Convention) if called with multiple file arguments. To print such concatenated output it is necessary to deactivate DSC handling in the printing program or previewer. See section &#8220;Font Installation&#8221; below for a guide how to install fonts for <code>grops</code>.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-b</code><i>n</i></p>
<dd> Provide workarounds for older printers, broken spoolers, and previewers. Normally <code>grops</code> produces output at PostScript LanguageLevel~2 that conforms to the Document Structuring Conventions version 3.0. Some older printers, spoolers, and previewers can&#8217;t handle such output. The value of~<i>n</i> controls what <code>grops</code> does to make its output acceptable to such programs. A value of~0 causes grops not to employ any workarounds.</p>
<dt>
<dd> Add~1 if no <code>%%BeginDocumentSetup</code> and <code>%%EndDocumentSetup</code> comments should be generated; this is needed for early versions of TranScript that get confused by anything between the <code>%%EndProlog</code> comment and the first <code>%%Page</code> comment.</p>
<dt>
<dd> Add~2 if lines in included files beginning with <code>%!</code> should be stripped out; this is needed for Sun&#8217;s pageview previewer.</p>
<dt>
<dd> Add~4 if <code>%%Page</code>, <code>%%Trailer</code> and <code>%%EndProlog</code> comments should be stripped out of included files; this is needed for spoolers that don&#8217;t understand the <code>%%BeginDocument</code> and <code>%%EndDocument</code> comments.</p>
<dt>
<dd> Add~8 if the first line of the PostScript output should be <code>%!PS-Adobe-2.0</code> rather than <code>%!PS-Adobe-3.0</code>; this is needed when using Sun&#8217;s Newsprint with a printer that requires page reversal.</p>
<dt>
<dd> Add~16 if no media size information should be included in the document (this is, neither use <code>%%DocumentMedia</code> nor the <code>setpagedevice</code> PostScript command). This was the behaviour of groff version 1.18.1 and earlier; it is needed for older printers which don&#8217;t understand PostScript LanguageLevel~2. It is also necessary if the output is further processed to get an encapsulated PS (EPS) file &#8211; see below.</p>
<dt>
<dd> The default value can be specified by a</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>broken&nbsp;</code><i>n</i></dl>
<p> command in the <i>DESC</i> file. Otherwise the default value is~0.</dl>
<dt><code>-c</code><i>n</i></p>
<dd> Print <i>n</i> copies of each page.</p>
<dt><code>-F</code><i>dir</i></p>
<dd> Prepend directory dir<i>/dev</i>name to the search path for prologue, font, and device description files; <i>name</i> is the name of the device, usually <code>ps</code>.</p>
<dt><code>-g</code></p>
<dd> Guess the page length. This generates PostScript code that guesses the page length. The guess is correct only if the imageable area is vertically centered on the page. This option allows you to generate documents that can be printed both on letter (8.5&#215;11) paper and on A4 paper without change.</p>
<dt><code>-I</code><i>dir</i></p>
<dd> This option may be used to add a directory to the search path for files on the command line and files named in <code>\X&#8217;ps: import&#8217;</code> and <code>\X&#8217;ps: file&#8217;</code> escapes. The search path is initialized with the current directory. This option may be specified more than once; the directories are then searched in the order specified (but before the current directory). If you want to make the current directory be read before other directories, add <code>-I.</code> at the appropriate place.</p>
<dt>
<dd> No directory search is performed for files with an absolute file name.</p>
<dt><code>-l</code></p>
<dd> Print the document in landscape format.</p>
<dt><code>-m</code></p>
<dd> Turn manual feed on for the document.</p>
<dt><code>-p</code><i>paper-size</i></p>
<dd> Set physical dimension of output medium. This overrides the <code>papersize</code>, <code>paperlength</code>, and <code>paperwidth</code> commands in the <i>DESC</i> file; it accepts the same arguments as the <code>papersize</code> command. See <code>groff_font (5)</code> for details.</p>
<dt><code>-P</code><i>prologue-file</i></p>
<dd> Use the file <i>prologue-file</i> (in the font path) as the prologue instead of the default prologue file <code>prologue</code>. This option overrides the environment variable <i>GROPS_PROLOGUE.</i></p>
<dt><code>-w</code><i>n</i></p>
<dd> Lines should be drawn using a thickness of <i>n</i>~thousandths of an em. If this option is not given, the line thickness defaults to 0.04~em.</p>
<dt><code>-v</code></p>
<dd> Print the version number.</dl>
<h2>USAGE</h2>
<p> The input to <code>grops</code> must be in the format output by <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). This is described in <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5). </p>
<p> In addition, the device and font description files for the device used must meet certain requirements: The resolution must be an integer multiple of~72 times the <code>sizescale</code>. The <code>ps</code> device uses a resolution of 72000 and a sizescale of 1000. </p>
<p> The device description file must contain a valid paper size; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more information. </p>
<p> Each font description file must contain a command</p>
<dl>
<dt>
<dd> <code>internalname&nbsp;</code><i>psname</i></dl>
<p> which says that the PostScript name of the font is <i>psname</i>. It may also contain a command</p>
<dl>
<dt>
<dd> <code>encoding&nbsp;</code><i>enc_file</i></dl>
<p> which says that the PostScript font should be reencoded using the encoding described in <i>enc_file</i>; this file should consist of a sequence of lines of the form:</p>
<dl>
<dt>
<dd> <i>pschar code</i></dl>
<p> where <i>pschar</i> is the PostScript name of the character, and <i>code</i> is its position in the encoding expressed as a decimal integer; valid values are in the range 0 to~255. Lines starting with <code>#</code> and blank lines are ignored. The code for each character given in the font file must correspond to the code for the character in encoding file, or to the code in the default encoding for the font if the PostScript font is not to be reencoded. This code can be used with the <code>\N</code> escape sequence in <code>troff</code> to select the character, even if the character does not have a groff name. Every character in the font file must exist in the PostScript font, and the widths given in the font file must match the widths used in the PostScript font. <code>grops</code> assumes that a character with a groff name of <code>space</code> is blank (makes no marks on the page); it can make use of such a character to generate more efficient and compact PostScript output. </p>
<p> Note that <code>grops</code> is able to display all glyphs in a PostScript font, not only 256. <i>enc_file</i> (or the default encoding if no encoding file specified) just defines the order of glyphs for the first 256 characters; all other glyphs are accessed with additional encoding vectors which <code>grops</code> produces on the fly. </p>
<p> <code>grops</code> can automatically include the downloadable fonts necessary to print the document. Such fonts must be in PFA format. Use <code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1) to convert a Type~1 font in PFB format. Any downloadable fonts which should, when required, be included by <code>grops</code> must be listed in the file <i>/usr/share/groff/1.22.4/font/devps/download</i>; this should consist of lines of the form</p>
<dl>
<dt>
<dd> <i>font filename</i></dl>
<p> where <i>font</i> is the PostScript name of the font, and <i>filename</i> is the name of the file containing the font; lines beginning with <code>#</code> and blank lines are ignored; fields may be separated by tabs or spaces; <i>filename</i> is searched for using the same mechanism that is used for groff font metric files. The <i>download</i> file itself is also searched for using this mechanism; currently, only the first found file in the font path is used. </p>
<p> If the file containing a downloadable font or imported document conforms to the Adobe Document Structuring Conventions, then <code>grops</code> interprets any comments in the files sufficiently to ensure that its own output is conforming. It also supplies any needed font resources that are listed in the <i>download</i> file as well as any needed file resources. It is also able to handle inter-resource dependencies. For example, suppose that you have a downloadable font called Garamond, and also a downloadable font called Garamond-Outline which depends on Garamond (typically it would be defined to copy Garamond&#8217;s font dictionary, and change the PaintType), then it is necessary for Garamond to appear before Garamond-Outline in the PostScript document. <code>grops</code> handles this automatically provided that the downloadable font file for Garamond-Outline indicates its dependence on Garamond by means of the Document Structuring Conventions, for example by beginning with the following lines</p>
<dl>
<dt>
<dd> <code>%!PS-Adobe-3.0 Resource-Font</code><br />
 <code>%%DocumentNeededResources: font Garamond</code><br />
 <code>%%EndComments</code><br />
 <code>%%IncludeResource: font Garamond</code></dl>
<p> In this case both Garamond and Garamond-Outline would need to be listed in the <i>download</i> file. A downloadable font should not include its own name in a <code>%%DocumentSuppliedResources</code> comment. </p>
<p> <code>grops</code> does not interpret <code>%%DocumentFonts</code> comments. The <code>%%DocumentNeededResources</code>, <code>%%DocumentSuppliedResources</code>, <code>%%IncludeResource</code>, <code>%%BeginResource</code>, and <code>%%EndResource</code> comments (or possibly the old <code>%%DocumentNeededFonts</code>, <code>%%DocumentSuppliedFonts</code>, <code>%%IncludeFont</code>, <code>%%BeginFont</code>, and <code>%%EndFont</code> comments) should be used. </p>
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
<p> There are also some special fonts called <code>S</code> for the PS Symbol font, and <code>SS</code>, containing slanted lowercase Greek letters taken from PS Symbol. Zapf Dingbats is available as <code>ZD</code>, and a reversed version of ZapfDingbats (with symbols pointing in the opposite direction) is available as <code>ZDR</code>; most characters in these fonts are unnamed and must be accessed using <code>\N</code>. </p>
<p> The default color for <code>\m</code> and <code>\M</code> is black; for colors defined in the &#8216;rgb&#8217; color space <code>setrgbcolor</code> is used, for &#8216;cmy&#8217; and &#8216;cmyk&#8217; <code>setcmykcolor</code>, and for &#8216;gray&#8217; <code>setgray</code>. Note that <code>setcmykcolor</code> is a PostScript LanguageLevel~2 command and thus not available on some older printers. </p>
<p> <code>grops</code> understands various X~commands produced using the <code>\X</code> escape sequence; <code>grops</code> only interprets commands that begin with a <code>ps:</code> tag.</p>
<dl>
<dt><code>\X&#8217;ps: exec&nbsp;</code><i>code</i><code>&#8216;</code></p>
<dd> This executes the arbitrary PostScript commands in <i>code</i>. The PostScript currentpoint is set to the position of the <code>\X</code> command before executing <i>code</i>. The origin is at the top left corner of the page, and y~coordinates increase down the page. A procedure~<code>u</code> is defined that converts groff units to the coordinate system in effect (provided the user doesn&#8217;t change the scale). For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.nr x 1i</code><br />
 <code>\X&#8217;ps: exec 
x u 0 rlineto stroke&#8217;</code>
</dl>
</dl>
<dt>
<dd> draws a horizontal line one inch long. <i>code</i> may make changes to the graphics state, but any changes persist only to the end of the page. A dictionary containing the definitions specified by the <code>def</code> and <code>mdef</code> is on top of the dictionary stack. If your code adds definitions to this dictionary, you should allocate space for them using <code>\X&#8217;ps mdef</code><i>&nbsp;n</i><code>&#8216;</code>. Any definitions persist only until the end of the page. If you use the <code>\Y</code> escape sequence with an argument that names a macro, <i>code</i> can extend over multiple lines. For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>.nr x 1i
.de y
ps: exec

x u 0 rlineto
stroke
..
\Yy
</code></pre>
</dl>
<p> is another way to draw a horizontal line one inch long. Note the single backslash before &#8216;nx&#8217; &#8211; the only reason to use a number register while defining the macro &#8216;y&#8217; is to convert a user-specified dimension &#8216;1i&#8217; to internal groff units which are in turn converted to PS units with the <code>u</code> procedure. </p>
<p> <code>grops</code> wraps user-specified PostScript code into a dictionary, nothing more. In particular, it doesn&#8217;t start and end the inserted code with <code>save</code> and <code>restore</code>, respectively. This must be supplied by the user, if necessary.</dl>
<dt><code>\X&#8217;ps: file&nbsp;</code><i>name</i><code>&#8216;</code></p>
<dd> This is the same as the <code>exec</code> command except that the PostScript code is read from file <i>name</i>.</p>
<dt><code>\X&#8217;ps: def&nbsp;</code><i>code</i><code>&#8216;</code></p>
<dd> Place a PostScript definition contained in <i>code</i> in the prologue. There should be at most one definition per <code>\X</code> command. Long definitions can be split over several <code>\X</code> commands; all the <i>code</i> arguments are simply joined together separated by newlines. The definitions are placed in a dictionary which is automatically pushed on the dictionary stack when an <code>exec</code> command is executed. If you use the <code>\Y</code> escape sequence with an argument that names a macro, <i>code</i> can extend over multiple lines.</p>
<dt><code>\X&#8217;ps: mdef&nbsp;</code><i>n code</i><code>&#8216;</code></p>
<dd> Like <code>def</code>, except that <i>code</i> may contain up to <i>n</i>~definitions. <code>grops</code> needs to know how many definitions <i>code</i> contains so that it can create an appropriately sized PostScript dictionary to contain them.</p>
<dt><code>\X&#8217;ps: import&nbsp;</code><i>file llx lly urx ury width&nbsp;</i>[&nbsp;height&nbsp;]<code>&#8216;</code></p>
<dd> Import a PostScript graphic from <i>file</i>. The arguments <i>llx</i>, <i>lly</i>, <i>urx</i>, and <i>ury</i> give the bounding box of the graphic in the default PostScript coordinate system; they should all be integers; <i>llx</i> and <i>lly</i> are the x and y~coordinates of the lower left corner of the graphic; <i>urx</i> and <i>ury</i> are the x and y~coordinates of the upper right corner of the graphic; <i>width</i> and <i>height</i> are integers that give the desired width and height in groff units of the graphic.</p>
<dt>
<dd> The graphic is scaled so that it has this width and height and translated so that the lower left corner of the graphic is located at the position associated with <code>\X</code> command. If the height argument is omitted it is scaled uniformly in the x and y~directions so that it has the specified width.</p>
<dt>
<dd> Note that the contents of the <code>\X</code> command are not interpreted by <code>troff</code>; so vertical space for the graphic is not automatically added, and the <i>width</i> and <i>height</i> arguments are not allowed to have attached scaling indicators.</p>
<dt>
<dd> If the PostScript file complies with the Adobe Document Structuring Conventions and contains a <code>%%BoundingBox</code> comment, then the bounding box can be automatically extracted from within groff by using the <code>psbb</code> request.</p>
<dt>
<dd> See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for a description of the <code>PSPIC</code> macro which provides a convenient high-level interface for inclusion of PostScript graphics.</p>
<dt><code>\X&#8217;ps: invis&#8217;</code></p>
<dd> <code>\X&#8217;ps: endinvis&#8217;</code> No output is generated for text and drawing commands that are bracketed with these <code>\X</code> commands. These commands are intended for use when output from <code>troff</code> is previewed before being processed with <code>grops</code>; if the previewer is unable to display certain characters or other constructs, then other substitute characters or constructs can be used for previewing by bracketing them with these <code>\X</code> commands.</p>
<dl>
<dt>
<dd>
<p> For example, <code>gxditview</code> is not able to display a proper <code>\(em</code> character because the standard X11 fonts do not provide it; this problem can be overcome by executing the following request</p>
<dl>
<dt>
<dd>
<pre>
.char \(em \X'ps: invis'\
\Z''-.25m'\h'.05m'\D'l .9m 0'\h'.05m''\
\X'ps: endinvis'\(em
</pre>
</dl>
<p> In this case, <code>gxditview</code> is unable to display the <code>\(em</code> character and draws the line, whereas <code>grops</code> prints the <code>\(em</code> character and ignores the line (this code is already in file <code>Xps.tmac</code> which is loaded if a document intended for <code>grops</code> is previewed with <code>gxditview</code>).</dl>
</dl>
<p> If a PostScript procedure <code>BPhook</code> has been defined via a &#8216;<code>ps: def</code>&#8216; or &#8216;<code>ps: mdef</code>&#8216; device command, it is executed at the beginning of every page (before anything is drawn or written by groff). For example, to underlay the page contents with the word &#8216;DRAFT&#8217; in light gray, you might use</p>
<dl>
<dt>
<dd>
<pre>
<code>.de XX
ps: def
/BPhook
{ gsave .9 setgray clippath pathbbox exch 2 copy
  .5 mul exch .5 mul translate atan rotate pop pop
  /NewCenturySchlbk-Roman findfont 200 scalefont setfont
  (DRAFT) dup stringwidth pop -.5 mul -70 moveto show
  grestore }
def
..
.devicem XX
</code></pre>
</dl>
<p> Or, to cause lines and polygons to be drawn with square linecaps and mitered linejoins instead of the round linecaps and linejoins normally used by <code>grops</code>, use</p>
<dl>
<dt>
<dd>
<pre>
<code>.de XX
ps: def
/BPhook { 2 setlinecap 0 setlinejoin } def
..
.devicem XX
</code></pre>
</dl>
<p> (square linecaps, as opposed to butt linecaps (0 setlinecap), give true corners in boxed tables even though the lines are drawn unconnected).</p>
<h3>Encapsulated PostScript</h3>
<p> <code>grops</code> itself doesn&#8217;t emit bounding box information. With the help of Ghostscript the following simple script, <code>groff2eps</code>, produces an encapsulated PS file.</p>
<dl>
<dt>
<dd>
<pre>
<code>#! /bin/sh
groff -P-b16 $1 &gt; $1.ps
gs -dNOPAUSE -sDEVICE=bbox -- $1.ps 2&gt; $1.bbox
sed -e &quot;/ha%%Orientation/r $1.bbox&quot; \
    -e &quot;/ha%!PS-Adobe-3.0/s/$/ EPSF-3.0/&quot; $1.ps &gt; $1.eps
rm $1.ps $1.bbox
</code></pre>
</dl>
<p> Just say</p>
<dl>
<dt>
<dd> <code>groff2eps foo</code></dl>
<p> to convert file <code>foo</code> to <code>foo.eps</code>.</p>
<h3>TrueType and other font formats</h3>
<p> TrueType fonts can be used with <code>grops</code> if converted first to <code>Type~42</code> format, a special PostScript wrapper equivalent to the PFA format mentioned in <code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1). There are several different methods to generate a type42 wrapper and most of them involve the use of a PostScript interpreter such as Ghostscript &#8211; see <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1). </p>
<p> Yet, the easiest method involves the use of the application <code><a href="/docs/linux/man/1-ttftot42/">ttftot42</a></code>(1). This program uses <code><a href="/docs/linux/man/3-freetype/">freetype</a></code>(3) (version 1.3.1) to generate type42 font wrappers and well-formed AFM files that can be fed to the <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1) script to create appropriate metric files. The resulting font wrappers should be added to the <i>download</i> file. <code>ttftot42</code> source code can be downloaded from <a href="ftp://www.giga.or.at/pub/nih/ttftot42/">ftp://www.giga.or.at/pub/nih/ttftot42/</a> </p>
<p> Another solution for creating type42 wrappers is to use FontForge, available from <a rel="nofollow" href="http://fontforge.sf.net">http://fontforge.sf.net</a> This font editor can convert most outline font formats.</p>
<h2>FONT INSTALLATION</h2>
<p> This section gives a summary of the above explanations; it can serve as a step-by-step font installation guide for <code>grops</code>.</p>
<dl>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Convert your font to something groff understands. This is either a PostScript Type~1 font in PFA format or a PostScript Type~42 font, together with an AFM file.</p>
<dt>
<dd> The very first characters in a PFA file look like this:</p>
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
<dd> The very first characters in a Type~42 font file look like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>%!PS-TrueTypeFont</code></dl>
</dl>
<dt>
<dd> This is a wrapper format for TrueType fonts. Old PS printers might not support it (this is, they don&#8217;t have a built-in TrueType font interpreter).</p>
<dt>
<dd> If your font is in PFB format (such fonts normally have <i>.pfb</i> as the file extension), you might use groff&#8217;s <code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1) program to convert it to PFA. For TrueType fonts, try <code>ttftot42</code> or <code>fontforge</code>. For all other font formats use <code>fontforge</code> which can convert most outline font formats.</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Convert the AFM file to a groff font description file with the <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1) program. An example call is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> afmtodit Foo-Bar-Bold.afm textmap FBB</dl>
</dl>
<dt>
<dd> which converts the metric file <i>Foo-Bar-Bold.afm</i> to the groff font <i>FBB</i>. If you have a font family which comes with normal, bold, italic, and bold italic faces, it is recommended to use the letters <code>R</code>, <code>B</code>, <code>I</code>, and <code>BI</code>, respectively, as postfixes in the groff font names to make groff&#8217;s &#8216;.fam&#8217; request work. An example is groff&#8217;s built-in Times-Roman font: The font family name is <code>T</code>, and the groff font names are <code>TR</code>, <code>TB</code>, <code>TI</code>, and <code>TBI</code>.</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Install both the groff font description files and the fonts in a <i>devps</i> subdirectory of the font path which groff finds. See section &#8220;Environment&#8221; in <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) for the actual value of the font path. Note that groff doesn&#8217;t use the AFM files (but it is a good idea to store them anyway).</p>
<dt>
<dd> &bull;&nbsp;<wbr>&nbsp; Register all fonts which must be downloaded to the printer in the <i>devps/download</i> file. Only the first occurrence of this file in the font path is read. This means that you should copy the default <i>download</i> file to the first directory in your font path and add your fonts there. To continue the above example we assume that the PS font name for <i>Foo-Bar-Bold.pfa</i> is &#8216;XY-Foo-Bar-Bold&#8217; (the PS font name is stored in the <code>internalname</code> field in the <i>FBB</i> file), thus the following line should be added to <i>download</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>XY-Foo-Bar-Bold Foo-Bar-Bold.pfa</code></dl>
</dl>
</dl>
<h2>OLD FONTS</h2>
<p> groff versions 1.19.2 and earlier contain a slightly different set of the 35 Adobe core fonts; the difference is mainly the lack of the &#8216;Euro&#8217; glyph and a reduced set of kerning pairs. For backwards compatibility, these old fonts are installed also in the</p>
<dl>
<dt>
<dd> <i>/usr/share/groff/1.22.4/oldfont/devps</i></dl>
<p> directory. </p>
<p> To use them, make sure that <code>grops</code> finds the fonts before the default system fonts (with the same names): Either add command-line option <code>-F</code> to <code>grops</code></p>
<dl>
<dt>
<dd> <code>groff -Tps -P-F -P/usr/share/groff/1.22.4/oldfont &#8230;</code></dl>
<p> or add the directory to groff&#8217;s font path environment variable</p>
<dl>
<dt>
<dd> <code>GROFF_FONT_PATH=/usr/share/groff/1.22.4/oldfont</code></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROPS_PROLOGUE</i></p>
<dd> If this is set to <i>foo</i>, then <code>grops</code> uses the file <i>foo</i> (in the font path) instead of the default prologue file <code>prologue</code>. The option <code>-P</code> overrides this environment variable.</p>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</p>
<dt><i>SOURCE_DATE_EPOCH</i></p>
<dd> A timestamp (expressed as seconds since the Unix epoch) to use as the creation timestamp in place of the current time.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/groff/1.22.4/font/devps/DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/share/groff/1.22.4/font/devps/</i>F</p>
<dd> Font description file for font <i>F</i>.</p>
<dt><i>/usr/share/groff/1.22.4/font/devps/download</i></p>
<dd> List of downloadable fonts.</p>
<dt><i>/usr/share/groff/1.22.4/font/devps/text.enc</i></p>
<dd> Encoding used for text fonts.</p>
<dt><i>/usr/share/groff/1.22.4/tmac/ps.tmac</i></p>
<dd> Macros for use with <code>grops</code>; automatically loaded by <code>troffrc</code></p>
<dt><i>/usr/share/groff/1.22.4/tmac/pspic.tmac</i></p>
<dd> Definition of <code>PSPIC</code> macro, automatically loaded by <i>ps.tmac</i>.</p>
<dt><i>/usr/share/groff/1.22.4/tmac/psold.tmac</i></p>
<dd> Macros to disable use of characters not present in older PostScript printers (e.g., &#8216;eth&#8217; or &#8216;thorn&#8217;).</p>
<dt><i>/tmp/grops</i>XXXXXX</p>
<dd> Temporary file. See <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for details on the location of temporary files.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1), <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7), <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) </p>
<p> PostScript Language Document Structuring Conventions Specification </p>
<h2>Index</h2>
