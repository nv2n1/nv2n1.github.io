---

title: "fig2dev(1)"
name: "fig2dev"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2dev/"
description: "fig2dev – translates Fig code to various graphics languages"
---

<dl>
<dt><code>fig2dev</code> [<code>-L</code><i>language</i>] [<code>-m</code><i>mag</i>] [<code>-s</code><i>fsize</i>] [<code>-Z</code><i>maxdimension</i>] [<code>-D</code><i>+/-rangelist</i> [<code>-K</code>]] [<i>other options</i>] [<i>fig-file</i> [<i>out-file</i>]] </dt>
</dl>
<p> <code>fig2dev -h</code>|<code>-V</code> </p>
<p> <code>fig2dev</code> </p>
<dd> <p> translates fig code in the named <i>fig-file</i> into the specified graphics <i>language</i> and puts them in <i>out-file.</i> The graphics language is inferred from the suffix of <i>out-file,</i> or it must be given with the <code>-L</code> option. The default <i>fig-file</i> and <i>out-file</i> are standard input and standard output, respectively. A minus (-) in place of <i>fig-file</i> or <i>out-file</i> also denotes either standard input or standard output. </p>
<p> Xfig (Facility for Interactive Generation of figures) is a screen-oriented tool which runs under the X Window System, and allows the user to draw and manipulate objects interactively. This version of fig2dev is compatible with xfig versions 1.3, 1.4, 2.0, 2.1, 3.0, 3.1 and 3.2. </p>
<p> Xfig version 3.2.3 and later saves and allows the user to edit comments for each Fig object. These comments are output with several of the output languages, such as PostScript, CGM, EMF, LaTeX, MetaFont, PicTeX, (as % comments), tk (as # comments), and pic (as .\&quot; comments). </p>
<h2>GENERAL OPTIONS (all drivers)</h2>
 </dd>
<dl>
<dt><code>-L language</code></dt>
<dd> <p> Set the output graphics language. Valid languages are <code>box, cgm, dxf, epic, eepic, eepicemu, emf, eps, gbx (Gerber beta driver), gif, ibmgl, jpeg, latex, map (HTML image map), mf (MetaFont), mp (MetaPost), pcx, pdf, pdftex, pdftex_t, pic, pict2e, pictex, png, ppm, ps, pstex, pstex_t, pstricks, ptk (Perl/tk), shape (LaTeX shaped paragraphs), sld (AutoCad slide format), svg, textyl, tiff, tikz, tk (tcl/tk), tpic, xbm and xpm</code>. </p>
<p> Notes: <br />
 You must have ghostscript installed to get the pdf output, and ghostscript and one from the netpbm, the ImageMagick or the GraphicsMagick packages to get the bitmap formats (png, jpeg, etc.). </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Print help message with all options for all output languages then exit. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Print the program version number and exit. </p>
 </dd>
<dt><code>-D +/-rangelist</code></dt>
<dd> <p> With <i>+rangelist</i>, keep only those depths in the list. With <i>-rangelist</i>, keep all depths except those in the list. The rangelist may be a list of comma-separated numbers or ranges separated by colon (:). For example, <code>-D +10,40,55:70,80</code> means keep only layers 10, 40, 55 through 70, and 80. </p>
 </dd>
<dt><code>-K</code></dt>
<dd> <p> The selection of the depths with the <code>-D</code><i> +/-rangelist</i> option does normally not affect the calculation of the bounding box. Thus the generated document might have a much larger bounding box than necessary. If <code>-K</code> is given then the bounding box is adjusted to include only those objects in the selected depths. </p>
 </dd>
<dt><code>-G minor[:major][:unit]</code></dt>
<dd> <p> Draws a grid on the page. Specify thin, or thin and thick line spacing in one of several units. For example, <code>-G .25:1cm</code> draws a thin, gray line every .25 cm and a thicker gray line every 1 cm. Specifying <code>-G 1in</code> draws a thin line every 1 inch. Fractions may be used, e.g. <code>-G :1/2in</code> will draw a thick line every 1/2 inch. <br />
 Allowable units are: i, in, inch, f, ft, feet, c, cm, mm, and m. <br />
 <code>Only allowed for PostScript, EPS, PDF, pstricks, tikz and</code> <code>bitmap (GIF, JPEG, etc) drivers.</code> </p>
 </dd>
<dt><code>-j</code></dt>
<dd> <p> Enable the I18N internationalization facility. </p>
 </dd>
<dt><code>-m mag</code></dt>
<dd> <p> Set the magnification at which the figure is rendered to <i>mag.</i> The default is 1.0. This may not be used with the maxdimension option (<code>-Z</code>). </p>
 </dd>
<dt><code>-s fsize</code></dt>
<dd> <p> Set the default font size (in points, 1/72 inch) for text objects to <i>fsize.</i> The default is 11*mag, and thus is scaled by the <code>-m</code> option. If there is no scaling, the default font is eleven point Roman. </p>
 </dd>
<dt><code>-Z maxdimension</code></dt>
<dd> <p> Scale the figure so that the maximum dimension (width or height) is <i>maxdimension</i> inches or cm, depending on whether the figure was saved with imperial or metric units. This may not be used with the magnification option (<code>-m</code>). </p>
 </dd>
<dt><i>other options</i></dt>
<dd> <p> The other options are specific to the choice of graphics <i>language,</i> as described below. </p>
 </dd></dl>
<h2>OPTIONS COMMON TO ALL BITMAP FORMATS</h2>
<dl>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i> (1/72 inch). </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Use correct font sizes (points, 1/72 inch) instead of the traditional size that xfig/fig2dev uses, which is 1/80 inch. The corresponding xfig command-line option is -correct_font_size. </p>
 </dd>
<dt><code>-g color</code></dt>
<dd> <p> Use <i>color</i> for the background. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Convert all colors to grayscale. </p>
 </dd>
<dt><code>-S smoothfactor</code></dt>
<dd> <p> This will smooth the output by passing <i>smoothfactor</i> to ghostscript in the <i>-dTextAlphaBits</i> and <i>-dGraphicsAlphaBits</i> options to improve font rendering and graphic smoothing. A value of 2 for <i>smoothfactor</i> provides some smoothing and 4 provides more. </p>
 </dd></dl>
<h2>GIF OPTIONS</h2>
<dl>
<dt><code>-t color</code></dt>
<dd> <p> Use <i>color</i> for the transparent color in the GIF file. This must be specified in the same format that <a href="/docs/linux/man/1-ppmmake/">ppmmake</a>(1) allows. It may allow an X11 color name, but at least you may use a six-digit hexadecimal RGBvalue using the # sign, e.g. #ff0000 (Red). </p>
 </dd></dl>
<h2>JPEG OPTIONS</h2>
<dl>
<dt><code>-q image_quality</code></dt>
<dd> <p> use the integer value <i>image_quality</i> for the JPEG &quot;Quality&quot; factor. Valid values are 0 - 100, with the default being 75. </p>
 </dd></dl>
<h2>CGM OPTIONS</h2>
<p> CGM is Computer Graphics Metafile, developed by ISO and ANSI and is a vector-based plus bitmap language. Microsoft WORD, PowerPoint and probably other products can import this format <i>and display it on the screen,</i> something that they won&#8217;t do with EPS files that have an ASCII preview. </p>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Generate binary output. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Position arrowheads for CGM viewers that display rounded arrowheads. Normally, arrowheads are pointed, so fig2dev compensates for this by moving the endpoint of the line back so the tip of the arrowhead ends where the original endpoint of the line was. If the <code>-r</code> option is used, the position of arrows will <i>NOT</i> be corrected for compensating line width effects, because the rounded arrowhead doesn&#8217;t extend beyond the endpoint of the line. </p>
 </dd></dl>
<h2>DXF OPTIONS</h2>
<p> DXF is the Drawing Interchange File Format. The output to DXF is experimental. </p>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Select ANSI A paper size instead of the default ISO A4. </p>
 </dd>
<dt><code>-d xll,yll,xur,yur</code></dt>
<dd> <p> Restrict plotting to a rectangular area of the plotter paper which has a lower left hand corner at <i>(xll,yll)</i> and a upper right hand corner at <i>(xur,yur).</i> All four numbers are in inches and follow <code>-d</code> in a comma-separated list - <i>xll,yll,xur,yur</i> - with no spaces between them. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Rotate the figure to portrait mode. The default is landscape mode. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Plot the figure upside-down in portrait mode or backwards in landscape mode. </p>
 </dd></dl>
<h2>EMF OPTIONS</h2>
<p> EMF is Enhanced Metafile, developed by Microsoft and is a vector-based plus bitmap language. Microsoft WORD, PowerPoint and probably other products can import this format <i>and display it on the screen,</i> something that they won&#8217;t do with EPS files that have an ASCII preview. </p>
<dl>
<dt><code>-l lang</code></dt>
<dd> <p> Set the compatibility level to <i>lang</i>, where <i>lang</i> is one of <i>win95, win98</i> or <i>winnt.</i> The default is <i>winnt</i>. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Position arrowheads for EMF viewers that display rounded arrowheads. See the discussion of the <code>-r</code> option for the CGM output driver above. </p>
 </dd></dl>
<h2>EPIC OPTIONS</h2>
<p> EPIC is an enhancement to LaTeX picture drawing environment. </p>
<p> EEPIC is an extension to EPIC and LaTeX picture drawing environment which uses tpic specials as a graphics mechanism. It was written by Conrad Kwok of Division of Computer Science at University of California, Davis. Conrad Kwok has also written the EEPIC driver of fig2dev. </p>
<p> EEPIC-EMU is an EEPIC emulation package which does not use tpic specials. </p>
<dl>
<dt><code>-d factor</code></dt>
<dd> <p> Scale arrowheads by <i>factor.</i> The width and height of arrowheads is <i>divided</i> by this factor. This is because EPIC arrowheads are normally about double the size of TeX arrowheads. </p>
 </dd>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for text translation (0 = none, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Don&#8217;t set the font face, series, and style; only set it&#8217;s size and the baselineskip. By default, fig2dev sets all 5 font parameters when it puts some text. The disadvantage is that you can&#8217;t set the font from your LaTeX document. With this option on, you can set the font from your LaTeX document. </p>
 </dd>
<dd> <p> If any of the pictures included in your LaTeX document has been generated with <code>-F</code>, then all pictures must be generated with this option. </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
 </dd>
<dt><code>-l lwidth</code></dt>
<dd> <p> Use &quot;<code>\thicklines</code>&quot; when the width of the line is equal or wider than <i>lwidth.</i> The default is 2. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Generate a complete LaTeX file. In other words, the output file can be formatted without requiring any changes. </p>
 </dd>
<dt><code>-R dummyarg</code></dt>
<dd> <p> Allow rotated text. Rotated text will be set using the \rotatebox command. So, you will need to include &quot;<code>\usepackage{graphics}</code>&quot; in the preamble of your LaTeX document. A dummy argument is required after the <code>-R</code>. </p>
 </dd>
<dd> <p> If this option is not set, then rotated text will be set horizontally. </p>
 </dd>
<dt><code>-S scale</code></dt>
<dd> <p> Set the scale to which the figure is rendered. This option automatically sets the <i>magnification</i> and <i>fsize</i> to <i>scale</i>/12 and <i>scale</i> respectively. <i>Scale</i> must be between 8 and 12, inclusively. </p>
 </dd>
<dt><code>-t stretch</code></dt>
<dd> <p> Set the stretch factor of dashed lines to <i>stretch.</i> The default is 30. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Include comments in the output file. </p>
 </dd>
<dt><code>-W</code></dt>
<dd> <p> Enable variable line width. By default, only two line widths are available: The normal line width (&quot;<code>\thinlines</code>&quot;), and thick lines (&quot;<code>\thicklines</code>&quot;). See also the <code>-l</code> option above. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Disable variable line width. Only &quot;<code>\thicklines</code>&quot; and/or &quot;<code>\thinlines</code>&quot; commands will be generated in the output file. </p>
<p> When variable line width option is enabled, the &quot;<code>\thinlines</code>&quot; command is still used when the line width is less than <i>LineThick</i>. One potential problem is that the width of &quot;<code>\thinlines</code>&quot; is 0.4pt but the resolution of Fig is 1/80 inch (approx. 1pt). If <i>LineThick</i> is set to 2, normal lines will be drawn in 0.4pt wide lines but the next line width is already 2pt. One possible solution is to set <i>LineThick</i> to 1 and set the width of those lines you want to be drawn in &quot;<code>\thinlines</code>&quot; to 0. </p>
<p> Due to this problem, variable line width is disabled by default (<code>-w</code>). </p>
 </dd></dl>
<h2>IBM-GL (HP/GL) OPTIONS</h2>
<p> IBM-GL (IBM Graphics Language) is compatible with HP-GL (Hewlett-Packard Graphics Language). </p>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Select ANSI A paper size instead of the default ISO A4. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Generate instructions for an IBM 6180 Color Plotter without an IBM Graphics Enhancement Cartridge (IBM-GEC). </p>
 </dd>
<dt><code>-d xll,yll,xur,yur</code></dt>
<dd> <p> Restrict plotting to a rectangular area of the plotter paper which has a lower left hand corner at <i>(xll,yll)</i> and a upper right hand corner at <i>(xur,yur).</i> All four numbers are in inches and follow <code>-d</code> in a comma-separated list - <i>xll,yll,xur,yur</i> - with no spaces between them. </p>
 </dd>
<dt><code>-f fontfile</code></dt>
<dd> <p> Load text character specifications from the table in the file <i>fontfile</i>. The table must have 36 entries - one for each font plus a default. Each entry consists of 5 numbers which specify the <br />
 1.) standard character set (0 - 4, 6 - 9, 30 - 39), <br />
 2.) alternate character set (0 - 4, 6 - 9, 30 - 39), <br />
 3.) character slant angle (degrees), <br />
 4.) character width scale factor and <br />
 5.) character height scale factor. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> Precede output with PCL command to use HP/GL. </p>
 </dd>
<dt><code>-l pattfile</code></dt>
<dd> <p> Load area fill line patterns from the table in the <i>pattfile</i> file. The table must have 21 entries - one for each of the area fill patterns. Each entry consists of 5 numbers which specify the <br />
 1.) pattern number (-1 - 6), <br />
 2.) pattern length (inches), <br />
 3.) fill type (1 - 5), <br />
 4.) fill spacing (inches) and <br />
 5.) fill angle (degrees). </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Rotate the figure to portrait mode. The default is landscape mode. </p>
 </dd>
<dt><code>-p penfile</code></dt>
<dd> <p> Load plotter pen specifications from the table in the <i>penfile</i> file. The table must have 9 entries - one for each color plus a default. Each entry consists of 2 numbers which specify the <br />
 1.) pen number (1 - 8) and <br />
 2.) pen thickness (millimeters). </p>
 </dd>
<dt><code>-S speed</code></dt>
<dd> <p> Set the pen speed to <i>speed</i> (centimeters/second). </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Plot the figure upside-down in portrait mode or backwards in landscape mode. This allows you to write on the top surface of overhead transparencies without disturbing the plotter ink on the bottom surface. </p>
 </dd>
<dt><code>-x offset</code></dt>
<dd> <p> Shift figure left by <i>offset</i> inches. </p>
 </dd>
<dt><code>-y offset</code></dt>
<dd> <p> Shift figure up by <i>offset</i> inches. </p>
 </dd></dl>
<p> Fig2dev may be installed with either ANSI A or ISO A4 default paper size. The <code>-a</code> option selects the alternate paper size. Fig2dev does not fill closed splines. The IBM-GEC is required to fill other polygons. Fig2dev may be installed for plotters with or without the IBM-GEC. The <code>-c</code> option selects the alternate instruction set. </p>
<h2>LATEX OPTIONS</h2>
<dl>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i> (1/72 inch). </p>
 </dd>
<dt><code>-d dmag</code></dt>
<dd> <p> Set a separate magnification for the length of line dashes to <i>dmag</i>. </p>
 </dd>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for latex text translation (0 = no translation, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Don&#8217;t set the font face, series, and style; only set it&#8217;s size and the baselineskip. By default, fig2dev sets all 5 font parameters when it puts some text. The disadvantage is that you can&#8217;t set the font from your LaTeX document. With this option on, you can set the font from your LaTeX document. </p>
 </dd>
<dd> <p> If any of the pictures included in your LaTeX document has been generated with <code>-F</code>, then all pictures must be generated with this option. </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
 </dd>
<dt><code>-l lwidth</code></dt>
<dd> <p> Sets the threshold between LaTeX thin and thick lines to <i>lwidth</i> pixels. LaTeX supports only two different line widths: \thinlines and \thicklines. Lines of width greater than <i>lwidth</i> pixels are drawn as \thicklines. Also affects the size of dots in dotted line style. The default is 1. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Verbose mode. Include comments in the otput file. </p>
 </dd></dl>
<p> LaTeX cannot accurately represent all the graphics objects which can be described by Fig. For example, the possible slopes which lines may have are limited. Some objects, such as spline curves, cannot be drawn at all. Fig2latex chooses the closest possible line slope, and prints error messages when objects cannot be drawn accurately. </p>
<h2>MAP (HTML image map) OPTIONS</h2>
<p> Xfig version 3.2.3 and later saves and allows the user to edit comments for each Fig object. The fig2dev map output language will produce an HTML image map using Fig objects that have href=&quot;some_html_reference&quot; in their comments. Any Fig object except compound objects may be used for this. Usually, besides generating the map file, you would also generate a PNG file, which is the image to which the map refers. </p>
<p> For example, you may have an xfig drawing with an imported image that has the comment href=&quot;go_here.html&quot; and a box object with a comment href=&quot;go_away.html&quot;. This will produce an image map file such the user may click on the image and the browser will load the &quot;go_here.html&quot; page, or click on the box and the browser will load the &quot;go_away.html&quot; page. </p>
<p> After the map file is generated by <i>fig2dev</i> you will need to edit it to fill out any additional information it may need. </p>
<dl>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i> (1/72 inch). </p>
 </dd></dl>
<h2>METAFONT OPTIONS</h2>
<p> <i>Fig2dev</i> scales the figure by 1/8 before generating METAFONT code. The magnification can be further changed with the <code>-m</code> option or by giving magnification options to <code>mf</code>. </p>
<p> In order to process the generated METAFONT code, the mfpic macros must be installed where <code>mf</code> can find them. The mfpic macro package is available at any CTAN cite under the subdirectory: graphics/mfpic </p>
<dl>
<dt><code>-C code</code></dt>
<dd> <p> Specify the starting METAFONT font code. The default is 32. </p>
 </dd>
<dt><code>-n name</code></dt>
<dd> <p> Specify the name to use in the output file. </p>
 </dd>
<dt><code>-p pen_magnification</code></dt>
<dd> <p> Specify how much the line width should be magnified compared to the original figure. The default is 1. </p>
 </dd>
<dt><code>-t top</code></dt>
<dd> <p> Specify the top of the whole coordinate system. The default is <code>ypos</code>. </p>
 </dd>
<dt><code>-x xmin</code></dt>
<dd> <p> Specify the minimum x coordinate value of the figure (inches). The default is 0. </p>
 </dd>
<dt><code>-y ymin</code></dt>
<dd> <p> Specify the minimum y coordinate value of the figure (inches). The default is 0. </p>
 </dd>
<dt><code>-X xmax</code></dt>
<dd> <p> Specify the maximum x coordinate value of the figure (inches). The default is 8. </p>
 </dd>
<dt><code>-Y ymax</code></dt>
<dd> <p> Specify the maximum y coordinate value of the figure (inches). The default is 8. </p>
 </dd></dl>
<h2>METAPOST OPTIONS</h2>
<dl>
<dt><code>-d file</code></dt>
<dd> <p> Include file content as additional header. </p>
 </dd>
<dt><code>-i file</code></dt>
<dd> <p> Include file content via \input-command. </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> Multipage mode, generate one figure for each depth. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> Old mode (no latex). </p>
 </dd>
<dt><code>-p number</code></dt>
<dd> <p> Adds the line &quot;prologues:=number&quot; to the output. </p>
 </dd></dl>
<h2>PIC OPTIONS</h2>
<dl>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>R</i> (roman), <i>B</i> (bold), <i>I</i> (italic), <i>H</i> (sans serif) or <i>C</i> (typewriter). The default is <i>R</i>. </p>
 </dd>
<dt><code>-p ext</code></dt>
<dd> <p> Enables the use of certain PIC extensions which are known to work with the groff package; compatibility with DWB PIC is unknown. The extensions enabled by each option are: </p>
 </dd></dl>
<pre><code>
 arc      Allow ARC_BOX i.e. use rounded corners


 line     Use the 'line_thickness' value


 fill     Allow ellipses to be filled


 all      Use all of the above


 psfont   Don't convert PostScript fonts generic type
        (useful for files going to be Ditroff'ed for
        and printed on PS printer). DWB-compatible.


 allps    Use all of the above (i.e. &quot;all&quot; + &quot;psfont&quot;)
</code></pre>
<h2>PICT2E OPTIONS</h2>
<p> PICT2E is an enhancement to the LaTeX picture environment. It is enabled by inserting &quot;<code>\usepackage{pict2e}</code>&quot; in the document preamble. Depending on the content of the figure, it may be necessary to also include &quot;<code>\usepackage{color}</code>&quot; and &quot;<code>\usepackage{graphics}</code>&quot;. Figures produced with the PICT2E driver can be processed with any LaTeX engine, e.g., LaTeX + dvips, LaTeX + dvipdfm, pdflatex, xelatex, ConTeX, etc. Pattern fills are not supported by the PICT2E output language. The PICT2E driver renders patterns by filling the respective area with the pen-color at 25% intensity, i.e., a 75% tint of the pen-color. The PICT2E driver allows one to choose any font available to the LaTeX engine, including PostScript fonts. TeX an PostScript fonts may appear together in the same document. </p>
<dl>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i>*(1/72) inches. </p>
 </dd>
<dt><code>-C num</code></dt>
<dd> <p> Do not emit a \color-command for the color number <code>num</code>. (0 = black, 1 = blue, 2 = green - see the color chooser widget in Xfig). By default, <i>fig2dev</i> does not issue a \color-command for objects which have the color set to &quot;Default&quot; in xfig. With this option, the &quot;\color&quot;-command is also omitted for objects having the color <code>num</code>. The color of these objects, as well as of those having the color set to &quot;Default&quot;, is picked up from the including LaTeX-document. </p>
<p> The option <code>-C 0</code> is particularly useful. By default, xfig starts with the color set to black. Then, <i>fig2dev</i> emits &quot;\color{black}&quot; commands, and the color-package must be included in the document preamble. For black text and black-and-white drawings, this is superfluous. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Do not try to be compatible with epic/eepic. By default, you can include &quot;<code>\usepackage{pict2e, epic, eepic}</code>&quot; (in this order!) in the document preamble and mix LaTeX pictures using the epic/eepic command set and pictures produced with the PICT2E output language within one document. With this option on, epic or eepic pictures can not be mixed with PICT2E-pictures. </p>
<p> By default, <i>fig2dev</i> avoids the use of the &quot;\circle&quot; and &quot;\oval&quot;-commands, which are defined by epic, in lieu of the &quot;\circlearc&quot;-command exclusive to pict2e. In addition, line widths are not only set using &quot;\linethickness&quot;, but also with the eepic-command &quot;\allinethickness&quot; (if it is defined). </p>
 </dd>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for text translation (0 = no translation, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). For instance, to use utf8-encoded text, first <i>create</i> a text object, then <i>edit</i> the text using the edit-button in xfig. Convert the fig-file to pict2e with the option <code>-E 0</code> and include &quot;<code>\usepackage[utf8]{inputenc}</code>&quot; in the LaTeX file In xfig, the text typed in may not be displayed correctly, but the document produced from the LaTeX file will show the same text as was typed in. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Do not set the font family, series or shape. By default, <i>fig2dev</i> sets the font family, series, shape, font size and baselineskip. With this option on, the text font can be set from the including LaTeX-document, e.g., &quot;<code>\itshape \input{fig1.pict2e}</code>&quot;. See also <code>-o</code> (no font size). </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>. The string <i>font</i> may be one of <i>rm</i>, <i>bf, it</i>, <i>sf</i>, <i>tt</i>, <i>\rmfamily</i>, <i>\bfseries</i>, <i>\itshape</i>, <i>\sffamily</i>, <i>\ttfamily</i>, or one of the 35 standard PostScript font names. The default is <i>\rmfamily</i>. </p>
 </dd>
<dt><code>-i dir</code></dt>
<dd> <p> Prepend the string <i>dir</i> to graphics files included in the pict2e-picture. For instance, having imported &quot;image.jpg&quot; in xfig, with <code>-i &#8216;$HOME/Figures/&#8216;</code> the code &quot;\incudegraphics{$HOME/Figures/image.jpg}&quot; will be generated. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> Do not set the font size or baselineskip. Text will be rendered at the size that is in force where the pict2e-code is inserted into the LaTeX-document, e.g., &quot;<code>\small \input{fig1.pict2e}</code>&quot;. See also <code>-F</code> (no font properties). </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> Do not quote characters special to TeX/LaTeX. Useful to get, e.g., an italic <i>x</i>, not $x$, because it was forgotten to set the text-flag &quot;special-text&quot; in xfig. This option effectively sets the &quot;special-text&quot; flag for all text. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Pagemode, generate a stand-alone LaTeX-file as <i>out-file</i>. The document produced from the LaTeX-file will have the paper size equal to the figure&#8217;s bounding box (but see the <code>-b</code> option to add a margin). The generated LaTeX-file calls the package &quot;geometry.sty&quot; to set the paper size. </p>
 </dd>
<dt><code>-R num</code></dt>
<dd> <p> Replace arrowheads <i>num</i> by LaTeX-arrows (&quot;\vector&quot;). The number of an arrowhead (&quot;Arrow Type&quot; in xfig) can be found by opening the arrow chooser widget in xfig and counting the arrows, starting from 1. For instance, to replace filled triangle arrowheads with LaTeX \vector-commands, use <code>-R 3</code>. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Replace all arrows by LaTeX-arrows. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> Only use TeX fonts, even where PostScript-fonts are specified. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Verbose mode. Write comment lines into the output file, usually naming the type of the object that is drawn. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Remove the suffix from included graphics-files. With this option on, <i>fig2dev</i> generates code that contains, e.g., &quot;<code>\includegraphics{fig1}</code>&quot;, instead of &quot;<code>\includegraphics{fig1.eps}</code>&quot;. </p>
 </dd></dl>
<h2>PICTEX OPTIONS</h2>
<p> In order to include PiCTeX pictures into a document, it is necessary to load the PiCTeX macros. </p>
<p> PiCTeX uses TeX integer register arithmetic to generate curves, and so it is very slow. PiCTeX draws curves by <code>\put</code>-ing the <i>psymbol</i> repeatedly, and so requires a large amount of TeX&#8217;s internal memory, and generates large DVI files. The size of TeX&#8217;s memory limits the number of plot symbols in a picture. As a result, it is best to use PiCTeX to generate small pictures. </p>
<dl>
<dt><code>-a</code></dt>
<dd> <p> Anonymous mode. Do not write the user name into the output file. </p>
 </dd>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for latex text translation (0 = no translation, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
 </dd>
<dt><code>-l dimen</code></dt>
<dd> <p> Set line thickness to <i>dimen</i>. Default &quot;1pt&quot;. </p>
 </dd>
<dt><code>-p psymbol</code></dt>
<dd> <p> Set the <i>psymbol</i>. Default &quot;\makebox(0,0)[l]{\tencirc\symbol{&#8216;160}}&quot;. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Do not allow rotated text. Otherwise, files with PiCTeX macros and rotated text need to be processed with <i>dvips</i>. </p>
 </dd></dl>
<h2>GBX OPTIONS (Gerber, RS-247-X)</h2>
<p> Typically you will wish to set the y scale to -1. See <code>-g</code> for more information. </p>
<dl>
<dt><code>-d [mm|in]</code></dt>
<dd> <p> Output dimensions should be assumed to be millimeters (mm) or inches (in). The default is millimeters. </p>
 </dd>
<dt><code>-p [pos|neg]</code></dt>
<dd> <p> Select the image polarity. For positive images lines drawn in the fig file will generate lines of material. For negative images lines drawn in the fig file will result in removed material. Consider etching a chrome on glass transmission mask. Drawing lines in the fig file and choosing &#8216;neg&#8217; will result in these lines being etched through the chrome, leaving transparent lines. </p>
 </dd>
<dt><code>-g &lt;x scale&gt;x&lt;y scale&gt;+&lt;x offset&gt;+&lt;y offset&gt;</code></dt>
<dd> <p> This controls the geometry of the output, scaling the dimensions as shown and applying the given offset. Typically you will wish to set the y scale to -1, mirroring about the x axis. This is because Gerber assumes the origin to be bottom left, while xfig selects top left. </p>
 </dd>
<dt><code>-f &lt;n digits&gt;.&lt;n digits&gt;</code></dt>
<dd> <p> This controls the number of digits of precision before and after the implied decimal point. With <code>-f 5.3</code> the following number 12345678 corresponds to 12345.678. Whereas with <code>-f 3.5</code> it corresponds to 123.45678. The default is for 3 places before the decimal point and 5 after. This corresponds, to a range of 0 to 1m in 10 micron increments. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Output comments describing the type of objects being output. The text appears as comments starting with ## on each line in the output file. </p>
 </dd></dl>
<h2>POSTSCRIPT, ENCAPSULATED POSTSCRIPT (EPS), and PDF OPTIONS</h2>
<p> With PostScript, xfig can be used to create multiple page figures. Specify the <code>-M</code> option to produce a multi-page output. For posters, add <code>-O</code> to overlap the pages slightly to get around the problem of the unprintable area in most printers, then cut and paste the pages together. Great for text with very big letters. </p>
<p> The EPS driver has the following differences from PostScript: <br />
 o No showpage is generated because the output is meant to be imported into another program or document and not printed <br />
 o The landscape/portrait options are ignored <br />
 o The centering option is ignored <br />
 o The multiple-page option is ignored <br />
 o The paper size option is ignored <br />
 o The x/y offset options are ignored </p>
<p> The EPS driver has the following two special options: </p>
<dl>
<dt><code>-B &#8216;Wx [Wy X0 Y0]&#8216;</code></dt>
<dd> <p> This specifies that the bounding box of the EPS file should have the width <i>Wx</i> and the height <i>Wy</i>. Note that it doesn&#8217;t scale the figure to this size, it merely sets the bounding box. If a value less than or equal to 0 is specified for <i>Wx</i> or <i>Wy</i>, these are set to the width/height respectively of the figure. Origin is relative to screen (0,0) (upper-left). <i>Wx</i>, <i>Wy</i>, <i>X0</i> and <i>Y0</i> are interpreted in centimeters or inches depending on the measure given in the fig-file. Remember to put either quotes (&quot;) or apostrophes (&#8216;) to group the arguments to <code>-B</code>. </p>
 </dd>
<dt><code>-R &#8216;Wx [Wy X0 Y0]&#8216;</code></dt>
<dd> <p> Same as the <code>-B</code> option except that <i>X0</i> and <i>Y0</i> is relative to the lower left corner of the <code>figure.</code> Remember to put either quotes (&quot;) or apostrophes (&#8216;) to group the arguments to <code>-R</code>. </p>
 </dd></dl>
<p> The PDF driver accepts all of the PostScript options, if the <code>-P</code> (pagemode) option is given. In this case, the size of the PDF is the pagesize given in the file or set from the command line via the <code>-z</code> option. Otherwise, if <code>-P</code> is not given, the PDF is cropped to the bounding box of the figure (optionally with a blank border margin set by the <code>-b</code> option), and all of the EPS options are supported. </p>
<p> Text can now include various ISO-character codes above 0x7f, which is useful for language specific characters to be printed directly. Not all ISO-characters are implemented. </p>
<p> Color support: Colored objects created by Fig can be printed on a color postscript printer. There are 32 standard colors: black, yellow, white, gold, five shades of blue, four shades of green, four shades of cyan, four shades of red, five shades of magenta, four shades of brown, and four shades of pink. In addition there may be user-defined colors in the file. See the xfig FORMAT3.2 file for the definition of these colors. On a monochrome printer, colored objects will be mapped into different grayscales by the printer. Filled objects are printed using the given area fill and color. There are 21 &quot;shades&quot; going from black to full saturation of the fill color, and 21 more &quot;tints&quot; from full saturation + 1 to white. In addition, there are 16 patterns such as bricks, diagonal lines, crosshatch, etc. </p>
<dl>
<dt><code>-A</code></dt>
<dd> <p> Add an ASCII (EPSI) preview. Not for PDF. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Anonymous mode. Do not write the user&#8217;s login name into the output file. </p>
 </dd>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i> (1/72 inch). </p>
 </dd>
<dt><code>-C dummy_arg</code></dt>
<dd> <p> Add a color *binary* TIFF preview for Microsoft products that need a binary preview. See also -T (monochrome preview). A dummy argument must be supplied for historical reasons. Not for PDF output. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Center the figure on the page. The centering may not be accurate if there are texts in the <i>fig_file</i> that extends too far to the right of other objects. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Put the figure against the edge (not centered) of the page. Not available in EPS. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Use correct font sizes (points, 1/72 inch) instead of the traditional size that xfig/fig2dev uses, which is 1/80 inch. The corresponding xfig command-line option is -correct_font_size. </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of the 35 standard PostScript font names. The default is <i>Times-Roman</i>. </p>
 </dd>
<dt><code>-g color</code></dt>
<dd> <p> Use <i>color</i> for the background. </p>
 </dd>
<dt><code>-l dummy_arg</code></dt>
<dd> <p> Generate figure in landscape mode. The dummy argument is ignored, but must appear on the command line for reasons of compatibility. This option will override the orientation specification in the file (for file versions 3.0 and higher). Not available in EPS. </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> Generate multiple pages if figure exceeds paper size. Not available in EPS. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Convert all colors to grayscale. </p>
 </dd>
<dt><code>-n name</code></dt>
<dd> <p> Set the Title part of the PostScript output to <i>name.</i> This is useful when the input to <i>fig2dev</i> comes from standard input. </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> When used with <code>-M</code>, overlaps the pages slightly to get around the problem of the unprintable area in most printers. Not available in EPS. </p>
 </dd>
<dt><code>-p dummy_arg</code></dt>
<dd> <p> Generate figure in portrait mode. The dummy argument is ignored, but must appear on the command line for reasons of compatibility. This option will override the orientation specification in the file (for file versions 3.0 and higher). This is the default for Fig files of version 2.1 or lower. Not available in EPS. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> Add a monochrome *binary* TIFF preview for Microsoft products that need a binary preview. See also <code>-C</code> (color preview). Not available for PDF output. </p>
 </dd>
<dt><code>-x offset</code></dt>
<dd> <p> Shift the figure in the X direction by <i>offset</i> PostScript points (1/72 inch). A negative value shifts the figure to the left and a positive value to the right. Not available in EPS. </p>
 </dd>
<dt><code>-y offset</code></dt>
<dd> <p> Shift the figure in the Y direction by <i>offset</i> points (1/72 inch). A negative value shifts the figure up and a positive value down. Not available in EPS. </p>
 </dd>
<dt><code>-z papersize</code></dt>
<dd> <p> Set the papersize. Not available in EPS. <br />
 Available paper sizes are: <br />
 </p>
<table>
<tr VALIGN=top>
<td><i>Letter</i></td>
<td>(8.5&quot; x 11&quot; also <i>A</i>),
</td>
</tr>
<tr VALIGN=top>
<td><i>Legal</i></td>
<td>( 11&quot; x 14&quot;)
</td>
</tr>
<tr VALIGN=top>
<td><i>Ledger</i></td>
<td>( 11&quot; x 17&quot;),
</td>
</tr>
<tr VALIGN=top>
<td><i>Tabloid</i></td>
<td>( 17&quot; x 11&quot;, really <i>Ledger</i> in Landscape mode),
</td>
</tr>
<tr VALIGN=top>
<td><i>A</i></td>
<td>(8.5&quot; x 11&quot; also <i>Letter</i>),
</td>
</tr>
<tr VALIGN=top>
<td><i>B</i></td>
<td>( 11&quot; x 17&quot; also <i>Ledger</i>),
</td>
</tr>
<tr VALIGN=top>
<td><i>C</i></td>
<td>( 17&quot; x 22&quot;),
</td>
</tr>
<tr VALIGN=top>
<td><i>D</i></td>
<td>( 22&quot; x 34&quot;),
</td>
</tr>
<tr VALIGN=top>
<td><i>E</i></td>
<td>( 34&quot; x 44&quot;),
</td>
</tr>
<tr VALIGN=top>
<td><i>A9</i></td>
<td>( 37 mm x 52 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A8</i></td>
<td>( 52 mm x 74 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A7</i></td>
<td>( 74 mm x 105 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A6</i></td>
<td>(105 mm x 148 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A5</i></td>
<td>(148 mm x 210 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A4</i></td>
<td>(210 mm x 297 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A3</i></td>
<td>(297 mm x 420 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A2</i></td>
<td>(420 mm x 594 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A1</i></td>
<td>(594 mm x 841 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>A0</i></td>
<td>(841 mm x1189 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B10</i></td>
<td>( 32 mm x 45 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B9</i></td>
<td>( 45 mm x 64 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B8</i></td>
<td>( 64 mm x 91 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B7</i></td>
<td>( 91 mm x 128 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B6</i></td>
<td>(128 mm x 182 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B5</i></td>
<td>(182 mm x 257 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B4</i></td>
<td>(257 mm x 364 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B3</i></td>
<td>(364 mm x 515 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B2</i></td>
<td>(515 mm x 728 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B1</i></td>
<td>(728 mm x1030 mm),
</td>
</tr>
<tr VALIGN=top>
<td><i>B0</i></td>
<td>(1030mm x1456 mm).
</td>
</tr>
</table>
<p> <br />
 </p>
 </dd></dl>
<h2>PSTEX and PDFTEX OPTIONS</h2>
<p> The <code>pstex</code> and <code>pdftex</code> languages are a variant of <code>ps</code> which suppress text that has the text flag &quot;TeX Text&quot; set. The <code>pstex_t</code> and <code>pdftex_t</code> languages have the complementary behavior: they generate only the text that has the &quot;Tex Text&quot; flag set and the commands necessary to position this text. They also generate the commands necessary to overlay the PostScript or PDF file generated using <code>pstex</code>/<code>pdftex</code>. These two drivers can be used to generate a figure which combines the flexibility of PostScript graphics with LaTeX text formatting of text flagged as &quot;TeX Text&quot;. </p>
<p> The pstex and pdftex drivers accept the same options that the EPS driver accepts. </p>
<dl>
<dt><code>-n name</code></dt>
<dd> <p> Set the Title part of the PostScript output to <i>name.</i> This is useful when the input to <i>fig2dev</i> comes from standard input. </p>
 </dd></dl>
<h2>PSTEX_T and PDFTEX_T OPTIONS</h2>
<p> The <code>pstex_t</code> and <code>pdftex_t</code> languages produce only the text flagged with the &quot;TeX Text&quot; flag, the commands necessary to position this text, and the commands necessary to overlay the PostScript or PDF file generated using <code>pstex</code> or <code>pdftex</code> (see above). </p>
<dl>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for latex text translation (0 no translation, 1 ISO-8859-1, 2 ISO-8859-2; default 1) </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Don&#8217;t set the font face, series, and style; only set it&#8217;s size and the baselineskip. By default, fig2dev sets all 5 font parameters when it puts some text. The disadvantage is that you can&#8217;t set the font from your LaTeX document. With this option on, you can set the font from your LaTeX document (like &quot;<code>\sfshape \input picture.eepic</code>&quot;). </p>
 </dd>
<dt><code>-p file</code></dt>
<dd> <p> specifies the name of the PostScript file to be overlaid. If not set or its value is null then no PS file will be inserted. </p>
 </dd></dl>
<h2>PSTricks OPTIONS</h2>
<p> The <code>PSTricks</code> driver provides full <code>LaTeX</code> text and math formatting for XFig drawings without overlaying separate outputs as in the <code>PSTEX</code> methods. The output matches the quality of output of the PostScript driver except for text, where the <code>Latex</code> font selection mechanism is used as for other <i>fig2dev</i> LaTeX drivers. In addition, text is rendered black, although font color-changing <code>LaTex</code> code can be embedded in the drawing. The generated PSTricks code is meant to be readable. Each command stands alone, not relying on global option state variables. Thus the user can easily use XFig to rough out a PSTricks drawing, then finish by hand editing. </p>
<p> To use the driver&#8217;s output, give the command &quot;<code>\usepackage{pstricks}</code>&quot; in your document preamble. The <code>graphicx</code> and <code>pstricks-add</code> packages may also be required. The former is used for bitmap graphics and the second for complex line styles and/or hollow PSTricks arrows (with the -R 1 option). The driver will tell you which packages are needed. In the document body, include the figure with &quot;<code>\input{pstfile}</code>&quot; where <code>pstfile.tex</code> is the output file. Use the <code>XFig TeX text</code> flag to have text passed as-is to LaTeX. For non-TeX text, the same mechanism as the LaTeX and epic driver mechanism is used to match font specs, but this is imprecise. </p>
<dl>
<dt><code>Known bugs and limitations.</code></dt>
<dd> <p> PSTricks support for join styles is version dependent. Raw postscript is inserted with &quot;<code>\pstVerb</code>&quot; for old versions when other than angle joins are needed. The <code>-t</code> option controls this behavior. PSTricks does not support rotated ellipses directly, so a <code>rput</code> command is emitted that rotates and locates a horizontal ellipse. This makes a problem with hatch patterns, which are moved and rotated along with the ellipse. Hatch rotation is fixed by a counter-rotation, but the origin is not adjusted, so registration with adjacent hatch patterns will be incorrect. Flipped bitmap graphics use an undocumented feature of the <code>graphicx</code> package: a negative height flips the image vertically. This appears to work reliably. However, you may want to flip graphics with another program before including them in <code>Xfig</code> drawings just to be sure. With the <code>-p</code> option, the driver attempts to convert non-EPS pictures to EPS with the TeX distribution&#8217;s <code>bmeps</code> program, but <code>bmeps</code> does not know about very many file formats including <code>gif</code>. </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
 </dd>
<dt><code>-G dummy_arg</code></dt>
<dd> <p> Draws a standard PSTricks grid in light gray, ignoring the size parameters, numbered in PSTricks units. </p>
 </dd>
<dt><code>-l weight</code></dt>
<dd> <p> Sets a line weight factor that is multiplied by the actual Fig line width. The default value 0.5 roughly matches the output of the PS driver. </p>
 </dd>
<dt><code>-n 0|1|2|3</code></dt>
<dd> <p> Sets environment type. Default 0 creates a <code>\picture</code> environment with bounding box exactly enclosing the picture (but see <code>-x</code> and <code>-y</code> ). A 1 emits bare PSTricks commands with no environment at all, which can be used with <code>\input{commands}</code> inside an existing <code>\pspicture</code>. A 2 emits a complete LaTeX document. A 3 also emits a complete LaTeX document but attempts to set the PSTricks unit to fit a 7.5 by 10 inch (portrait aspect) box. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Shorthand for <code>-n 3</code>. </p>
 </dd>
<dt><code>-p dir</code></dt>
<dd> <p> Attempts to run the <code>bmeps</code> program to translate picture files to EPS, which is required by PSTricks. The translated files go in <i>dir</i> , which must already exist (the driver will not create it). Moreover, (BIG CAVEAT HERE) the driver overwrites files with impunity in this directory! Don&#8217;t put your stuff here. The <code>includegraphics</code> commands in the output file refer to this directory. Even if the -p option is not used, <code>includegraphics</code> commands follow this convention with the default directory <i>./eps.</i> In this case, the user must do the conversions independently. The <code>bmeps</code> program is part of the standard TeX distribution. It converts the following formats to EPS: <code>png jpg pnm tif.</code> You can see the bmeps command with the <code>-v</code> option. </p>
 </dd>
<dt><code>-R 0|1|2</code></dt>
<dd> <p> Sets arrow style. With the default style 0, Fig arrows are converted to lines and polygons. With style 1, the Fig arrowhead dimensions are converted to PSTricks arrowhead dimensions and PSTricks arrowhead options are emitted. Hollow arrows will require the additional package <code>pstricks-add</code>. With style 2, PSTricks arrowhead options are emitted with no dimensions at all, and arrowhead size may be controlled globally with <code>psset</code>. </p>
 </dd>
<dt><code>-S scale</code></dt>
<dd> <p> Scales the image according to the same convention as the EPIC driver, i.e., to size <i>scale</i>/12. </p>
 </dd>
<dt><code>-t version</code></dt>
<dd> <p> Provides the driver with PSTricks version number so output can match expected LaTeX input. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print verbose warnings and extra comments in the output file. Information provided includes font substitution details, the <code>bmeps</code> commands used for picture conversion, if any, and one comment per Fig object in the output. </p>
 </dd>
<dt><code>-x marginsize</code></dt>
<dd> <p> Adds <i>marginsize</i> on the left and right of the <code>PStricks</code> bounding box. By default, the box exactly encloses the image. </p>
 </dd>
<dt><code>-y marginsize</code></dt>
<dd> <p> Adds <i>marginsize</i> on the top and bottom of the <code>PStricks</code> bounding box. By default, the box exactly encloses the image. </p>
 </dd>
<dt><code>-z 0|1|2</code></dt>
<dd> <p> Sets font handling option. Default option 0 attempts to honor Fig font names and sizes, finding the best match with a standard LaTeX font. Option 1 sets LaTeX font size only. Option 2 issues no font commands at all. </p>
 </dd></dl>
<h2>TEXTYL OPTIONS</h2>
<dl>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
 </dd>
<dt><code>-l lwidth</code></dt>
<dd> <p> Set the line thickness. <i>lwidth</i> must be a value between 1 and 12. </p>
 </dd></dl>
<h2>TIKZ OPTIONS</h2>
<p> TIKZ is a powerful frontend to the Portable Graphics Format (PGF) for TeX/LaTeX. To use figures created by the TIKZ driver in a LaTeX document, use &quot;<code>\usepackage{tikz}</code>&quot; and, depending on the contents of your figure, &quot;<code>\usetikzlibrary{arrows.meta, bending}</code>&quot; and &quot;<code>\usetikzlibrary{patterns}</code>&quot; in the document preamble. Simply \input or copy the output file into the TeX-document. TIKZ files produced by <i>fig2dev</i> may be included into a plain TeX document. However, the stand-alone file produced with the <code>-P</code> option must be processed with a LaTeX-engine. In addition, font-commands may require a LaTeX engine. </p>
<dl>
<dt><code>-b borderwidth</code></dt>
<dd> <p> Make blank border around figure of width <i>borderwidth</i>*(1/72) inches. </p>
 </dd>
<dt><code>-C num</code></dt>
<dd> <p> Do not emit a \color-command for the color number <code>num</code>. (0 = black, 1 = blue, 2 = green - see the color chooser widget in Xfig). By default, <i>fig2dev</i> does not issue a \color-command for objects which have the color set to &quot;Default&quot; in xfig. With this option, the &quot;\color&quot;-command is also omitted for objects having the color <code>num</code>. The color of these objects, as well as of those having the color set to &quot;Default&quot;, is picked up from the including document. </p>
 </dd>
<dt><code>-E num</code></dt>
<dd> <p> Set encoding for text translation (0 = no translation, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). For instance, to use utf8-encoded text, first <i>create</i> a text object, then <i>edit</i> the text using the edit-button in xfig. Convert the fig-file to tikz with the option <code>-E 0</code> and include &quot;<code>\usepackage[utf8]{inputenc}</code>&quot; in the LaTeX file (not necessary when using xelatex). In xfig, the text typed in may not be displayed correctly, but the document produced from the LaTeX file will show the same text as was typed in. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Do not set the font family, series or shape. By default, <i>fig2dev</i> sets the font family, series, shape, font size and baselineskip. As a side effect, this requires the New Font Selection Scheme (NFSS) of LaTeX. With this option on, the text font can be set from the including document, which may be TeX or LaTeX. See also <code>-o</code> (no font size). </p>
 </dd>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>. The string <i>font</i> may be one of <i>rm</i>, <i>bf, it</i>, <i>sf</i>, <i>tt</i>, <i>\rmfamily</i>, <i>\bfseries</i>, <i>\itshape</i>, <i>\sffamily</i>, <i>\ttfamily</i>, or one of the 35 standard PostScript font names. The default is <i>\rmfamily</i>. </p>
 </dd>
<dt><code>-i dir</code></dt>
<dd> <p> Prepend the string <i>dir</i> to graphics files included in the tikz-picture. For instance, having imported &quot;image.jpg&quot; in xfig, with <code>- i &#8216;$HOME/Figures/&#8216;</code> the code &quot;\pgfimage[width=..., height=...]{$HOME/Figures/image.jpg}&quot; will be generated. </p>
 </dd>
<dt><code>-O</code></dt>
<dd> <p> Do not quote characters special to TeX/LaTeX. Useful to get, e.g., an italic <i>x</i>, not $x$, because it was forgotten to set the text-flag &quot;special-text&quot; in xfig. This option effectively sets the &quot;special-text&quot; flag for all text. </p>
 </dd>
<dt><code>-o</code></dt>
<dd> <p> Do not set the font size or baselineskip. Text will be rendered at the size that is in force where the tikz-code is inserted into the document, e.g., &quot;<code>\small\input fig1.tikz</code>&quot;. See also <code>-F</code> (no font properties). </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Pagemode, generate a stand-alone LaTeX-file as <i>out-file</i>. Run <i>out-file</i> through LaTeX to generate a pdf or eps of the figure. The document produced from <i>out-file</i> will have the paper size equal to the figure&#8217;s bounding box (but see the <code>-b</code> option to add a margin). The package &quot;geometry.sty&quot; is used in <i>out-file</i> to set the paper size. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> Only use TeX fonts, even where PostScript-fonts are specified. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Verbose mode. Write comment lines into the output file, usually naming the type of the object that is drawn. </p>
 </dd>
<dt><code>-W</code></dt>
<dd> <p> Do not emit code at the beginning of the file that allows one to set the figure width or height from the including TeX document. Otherwise, e.g., &quot;<code>\newdimen\XFigwidth\XFigwidth=\linewidth</code>&quot; would scale the following figures to the line width. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Remove the suffix from included graphics-files. With this option on, <i>fig2dev</i> generates code that contains, e.g., &quot;<code>\pgfimage{fig1}</code>&quot; instead of &quot;<code>\pgfimage{fig1.pdf}</code>&quot;. </p>
 </dd></dl>
<h2>TK and PTK OPTIONS (tcl/tk and Perl/tk)</h2>
<p> Arc-boxes are not supported for the tk output language, and only X bitmap pictures are supported because of the canvas limitation in tk. <br />
 Picture objects are not scaled with the magnification factor for tk output. <br />
 Because tk scales canvas items according to the X display resolution, polygons, lines, etc. may be scaled differently than imported pictures (bitmaps) which aren&#8217;t scaled at all. </p>
<dl>
<dt><code>-g color</code></dt>
<dd> <p> Use <i>color</i> for the background. </p>
 </dd>
<dt><code>-l dummy_arg</code></dt>
<dd> <p> Generate figure in landscape mode. The dummy argument is ignored, but must appear on the command line for reasons of compatibility. This option will override the orientation specification in the file (for file versions 3.0 and higher). </p>
 </dd>
<dt><code>-p dummy_arg</code></dt>
<dd> <p> Generate figure in portrait mode. The dummy argument is ignored, but must appear on the command line for reasons of compatibility. This option will override the orientation specification in the file (for file versions 3.0 and higher). This is the default for Fig files of version 2.1 or lower. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Generate canvas of full page size instead of using the bounding box of the figure&#8217;s objects. The default is to use only the bounding box. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Wrap the figure with code in order to generate a complete perl file. That is, you can do <code>fig2dev -L ptk -w f.fig f.pl; perl f.pl</code> and a widget pops up that shows the graphics contained in f.pl. Only available for ptk output. </p>
 </dd>
<dt><code>-z papersize</code></dt>
<dd> <p> Set the paper size. See the POSTSCRIPT OPTIONS for available paper sizes. This is only used when the <code>-P</code> option (use full page) is used. </p>
 </dd></dl>
<h2>TPIC OPTIONS</h2>
<dl>
<dt><code>-f font</code></dt>
<dd> <p> Set the default font used for text objects to <i>font</i>. The default is <i>rm</i>. The string <i>font</i> can be one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i>, <i>tt</i>, <i>avant</i>, <i>avantcsc</i>, <i>avantd</i>, <i>avantdi</i>, <i>avanti</i>, <i>bookd</i>, <i>bookdi</i>, <i>bookl</i>, <i>booklcsc</i>, <i>bookli</i>, <i>chanc</i>, <i>cour</i>, <i>courb</i>, <i>courbi</i>, <i>couri</i>, <i>helv</i>, <i>helvb</i>, <i>helvbi</i>, <i>helvc</i>, <i>helvcb</i>, <i>helvcbi</i>, <i>helvci</i>, <i>helvcsc</i>, <i>helvi</i>, <i>pal</i>, <i>palb</i>, <i>palbi</i>, <i>palbu</i>, <i>palc</i>, <i>palcsc</i>, <i>pali</i>, <i>palsl</i>, <i>palu</i>, <i>palx</i>, <i>times</i>, <i>timesb</i>, <i>timesbi</i>, <i>timesc</i>, <i>timescsc</i>, <i>timesi</i>, <i>timessl</i> or <i>timesx</i>. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code>pic2fig</code>(1), <code><a href="/docs/linux/man/1-transfig/">transfig</a></code>(1) </p>
<h2>BUGS and RESTRICTIONS</h2>
<p> Please send bug reports, fixes, new features etc. to: <br />
 thomas.loimer [at] tuwien.ac.at </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991 Micah Beck <br />
 Parts Copyright (c) 1985-1988 Supoj Sutantavibul <br />
 Parts Copyright (c) 1989-2015 Brian V. Smith <br />
 Parts Copyright (c) 2015-2018 by Thomas Loimer </p>
<p> Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. The authors make no representations about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty. </p>
<p> THE AUTHORS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. </p>
<h2>AUTHORS</h2>
<p> Micah Beck <br />
 Cornell University <br />
 Sept 28 1990 </p>
<p> and Frank Schmuck (then of Cornell University) <br />
 and Conrad Kwok (then of U.C. Davis). </p>
<p> Drivers contributed by <br />
 Jose Alberto Fernandez R. (U. of Maryland) <br />
 and Gary Beihl (MCC) </p>
<p> Color support, ISO-character encoding and poster support by <br />
 Herbert Bauer (heb [at] regent.e-technik.tu-muenchen.de) </p>
<p> Modified from f2p (fig to PIC), by the author of Fig <br />
 Supoj Sutanthavibul (supoj [at] sally.utexas.edu) <br />
 University of Texas at Austin. </p>
<p> MetaFont driver by <br />
 Anthony Starks (ajs [at] merck.com) </p>
<p> X-splines code by <br />
 Carole Blanc (blanc [at] labri.u-bordeaux.fr) <br />
 Christophe Schlick (schlick [at] labri.u-bordeaux.fr) <br />
 The initial implementation was done by C. Feuille, S. Grobois, L. Maziere and L. Minihot as a student practice (Universite Bordeaux, France). </p>
<p> Japanese text support for LaTeX output written by T. Sato (VEF00200 [at] niftyserve.or.jp) </p>
<p> The tk driver was written by <br />
 Mike Markowski (mm [at] udel.edu) with a little touch-up by Brian Smith </p>
<p> The CGM driver (Computer Graphics Metafile) was written by <br />
 Philippe Bekaert (Philippe.Bekaert [at] cs.kuleuven.ac.be) </p>
<p> The EMF driver (Enhanced Metafile) was written by <br />
 Michael Schrick (m_schrick [at] hotmail.com) </p>
<p> The GBX (Gerber) driver was written by <br />
 Edward Grace (ej.grace [at] imperial.ac.uk). </p>
