---
title: "fig2dev(1)"
name: "fig2dev"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2dev/"
description: "fig2dev – translates Fig code to various graphics languages"
---

<h2 class="name">NAME</h2>
<p> fig2dev &#8211; translates Fig code to various graphics languages</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fig2dev</code> [<code>-L</code> <i>language</i>] [<code>-m</code> <i>mag</i>] [<code>-s</code> <i>fsize</i>] [<code>-Z</code> <i>maxdimension</i>] [<code>-D</code> <i>+/-rangelist</i> [<code>-K</code>]] [<i>other options</i>] [<i>fig-file</i> [<i>out-file</i>]]</dl>
<p> <code>fig2dev -h</code>|<code>-V</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fig2dev</code></p>
<dd>translates fig code in the named <i>fig-file</i> into the specified graphics <i>language</i> and puts them in <i>out-file.</i> The graphics language is inferred from the suffix of <i>out-file,</i> or it must be given with the <code>-L</code> option. The default <i>fig-file</i> and <i>out-file</i> are standard input and standard output, respectively. A minus (-) in place of <i>fig-file</i> or <i>out-file</i> also denotes either standard input or standard output. </p>
<p> Xfig (Facility for Interactive Generation of figures) is a screen-oriented tool which runs under the X Window System, and allows the user to draw and manipulate objects interactively. This version of fig2dev is compatible with xfig versions 1.3, 1.4, 2.0, 2.1, 3.0, 3.1 and 3.2. </p>
<p> Xfig version 3.2.3 and later saves and allows the user to edit comments for each Fig object. These comments are output with several of the output languages, such as PostScript, CGM, EMF, LaTeX, MetaFont, PicTeX, (as % comments), tk (as # comments), and pic (as .\&quot; comments). </p>
<h2>GENERAL OPTIONS (all drivers)</h2>
<dl>
<dt><code>-L language</code></p>
<dd> Set the output graphics language. Valid languages are <code>box, cgm, dxf, epic, eepic, eepicemu, emf, eps, gbx (Gerber beta driver), gif, ibmgl, jpeg, latex, map (HTML image map), mf (MetaFont), mp (MetaPost), pcx, pdf, pdftex, pdftex_t, pic, pict2e, pictex, png, ppm, ps, pstex, pstex_t, pstricks, ptk (Perl/tk), shape (LaTeX shaped paragraphs), sld (AutoCad slide format), svg, textyl, tiff, tikz, tk (tcl/tk), tpic, xbm and xpm</code>. </p>
<p> Notes:<br />
 You must have ghostscript installed to get the pdf output, and ghostscript and one from the netpbm, the ImageMagick or the GraphicsMagick packages to get the bitmap formats (png, jpeg, etc.). </p>
<dt><code>-h</code></p>
<dd> Print help message with all options for all output languages then exit. </p>
<dt><code>-V</code></p>
<dd> Print the program version number and exit. </p>
<dt><code>-D +/-rangelist</code></p>
<dd> With <i>+rangelist</i>, keep only those depths in the list. With <i>-rangelist</i>, keep all depths except those in the list. The rangelist may be a list of comma-separated numbers or ranges separated by colon (:). For example, <code>-D +10,40,55:70,80</code> means keep only layers 10, 40, 55 through 70, and 80. </p>
<dt><code>-K</code></p>
<dd> The selection of the depths with the <code>-D</code><i> +/-rangelist</i> option does normally not affect the calculation of the bounding box. Thus the generated document might have a much larger bounding box than necessary. If <code>-K</code> is given then the bounding box is adjusted to include only those objects in the selected depths. </p>
<dt><code>-G minor[:major][:unit]</code></p>
<dd> Draws a grid on the page. Specify thin, or thin and thick line spacing in one of several units. For example, <code>-G .25:1cm</code> draws a thin, gray line every .25 cm and a thicker gray line every 1 cm. Specifying <code>-G 1in</code> draws a thin line every 1 inch. Fractions may be used, e.g. <code>-G :1/2in</code> will draw a thick line every 1/2 inch.<br />
 Allowable units are: i, in, inch, f, ft, feet, c, cm, mm, and m.<br />
 <code>Only allowed for PostScript, EPS, PDF, pstricks, tikz and</code> <code>bitmap (GIF, JPEG, etc) drivers.</code> </p>
<dt><code>-j</code></p>
<dd> Enable the I18N internationalization facility. </p>
<dt><code>-m mag</code></p>
<dd> Set the magnification at which the figure is rendered to <i>mag.</i> The default is 1.0. This may not be used with the maxdimension option (<code>-Z</code>). </p>
<dt><code>-s fsize</code></p>
<dd> Set the default font size (in points, 1/72 inch) for text objects to <i>fsize.</i> The default is 11*mag, and thus is scaled by the <code>-m</code> option. If there is no scaling, the default font is eleven point Roman. </p>
<dt><code>-Z maxdimension</code></p>
<dd> Scale the figure so that the maximum dimension (width or height) is <i>maxdimension</i> inches or cm, depending on whether the figure was saved with imperial or metric units. This may not be used with the magnification option (<code>-m</code>). </p>
<dt><i>other options</i></p>
<dd> The other options are specific to the choice of graphics <i>language,</i> as described below. </p>
</dl>
<h2>OPTIONS COMMON TO ALL BITMAP FORMATS</h2>
<dl>
<dt><code>-b borderwidth</code></p>
<dd> Make blank border around figure of width <i>borderwidth</i> (1/72 inch). </p>
<dt><code>-F</code></p>
<dd> Use correct font sizes (points, 1/72 inch) instead of the traditional size that xfig/fig2dev uses, which is 1/80 inch. The corresponding xfig command-line option is -correct_font_size. </p>
<dt><code>-g color</code></p>
<dd> Use <i>color</i> for the background. </p>
<dt><code>-N</code></p>
<dd> Convert all colors to grayscale. </p>
<dt><code>-S smoothfactor</code></p>
<dd> This will smooth the output by passing <i>smoothfactor</i> to ghostscript in the <i>-dTextAlphaBits</i> and <i>-dGraphicsAlphaBits</i> options to improve font rendering and graphic smoothing. A value of 2 for <i>smoothfactor</i> provides some smoothing and 4 provides more. </p>
</dl>
<h2>GIF OPTIONS</h2>
<dl>
<dt><code>-t color</code></p>
<dd> Use <i>color</i> for the transparent color in the GIF file. This must be specified in the same format that <a href="/docs/linux/man/1-ppmmake/">ppmmake</a>(1) allows. It may allow an X11 color name, but at least you may use a six-digit hexadecimal RGBvalue using the # sign, e.g. #ff0000 (Red). </p>
</dl>
<h2>JPEG OPTIONS</h2>
<dl>
<dt><code>-q image_quality</code></p>
<dd> use the integer value <i>image_quality</i> for the JPEG &quot;Quality&quot; factor. Valid values are 0 &#8211; 100, with the default being 75. </p>
</dl>
<h2>CGM OPTIONS</h2>
<p> CGM is Computer Graphics Metafile, developed by ISO and ANSI and is a vector-based plus bitmap language. Microsoft WORD, PowerPoint and probably other products can import this format <i>and display it on the screen,</i> something that they won&#8217;t do with EPS files that have an ASCII preview. </p>
<dl>
<dt><code>-a</code></p>
<dd> Generate binary output. </p>
<dt><code>-r</code></p>
<dd> Position arrowheads for CGM viewers that display rounded arrowheads. Normally, arrowheads are pointed, so fig2dev compensates for this by moving the endpoint of the line back so the tip of the arrowhead ends where the original endpoint of the line was. If the <code>-r</code> option is used, the position of arrows will <i>NOT</i> be corrected for compensating line width effects, because the rounded arrowhead doesn&#8217;t extend beyond the endpoint of the line. </p>
</dl>
<h2>DXF OPTIONS</h2>
<p> DXF is the Drawing Interchange File Format. The output to DXF is experimental. </p>
<dl>
<dt><code>-a</code></p>
<dd> Select ANSI A paper size instead of the default ISO A4. </p>
<dt><code>-d xll,yll,xur,yur</code></p>
<dd> Restrict plotting to a rectangular area of the plotter paper which has a lower left hand corner at <i>(xll,yll)</i> and a upper right hand corner at <i>(xur,yur).</i> All four numbers are in inches and follow <code>-d</code> in a comma-separated list &#8211; <i>xll,yll,xur,yur</i> &#8211; with no spaces between them. </p>
<dt><code>-P</code></p>
<dd> Rotate the figure to portrait mode. The default is landscape mode. </p>
<dt><code>-v</code></p>
<dd> Plot the figure upside-down in portrait mode or backwards in landscape mode. </p>
</dl>
<h2>EMF OPTIONS</h2>
<p> EMF is Enhanced Metafile, developed by Microsoft and is a vector-based plus bitmap language. Microsoft WORD, PowerPoint and probably other products can import this format <i>and display it on the screen,</i> something that they won&#8217;t do with EPS files that have an ASCII preview. </p>
<dl>
<dt><code>-l lang</code></p>
<dd> Set the compatibility level to <i>lang</i>, where <i>lang</i> is one of <i>win95, win98</i> or <i>winnt.</i> The default is <i>winnt</i>. </p>
<dt><code>-r</code></p>
<dd> Position arrowheads for EMF viewers that display rounded arrowheads. See the discussion of the <code>-r</code> option for the CGM output driver above. </p>
</dl>
<h2>EPIC OPTIONS</h2>
<p> EPIC is an enhancement to LaTeX picture drawing environment. </p>
<p> EEPIC is an extension to EPIC and LaTeX picture drawing environment which uses tpic specials as a graphics mechanism. It was written by Conrad Kwok of Division of Computer Science at University of California, Davis. Conrad Kwok has also written the EEPIC driver of fig2dev. </p>
<p> EEPIC-EMU is an EEPIC emulation package which does not use tpic specials. </p>
<dl>
<dt><code>-d factor</code></p>
<dd> Scale arrowheads by <i>factor.</i> The width and height of arrowheads is <i>divided</i> by this factor. This is because EPIC arrowheads are normally about double the size of TeX arrowheads. </p>
<dt><code>-E num</code></p>
<dd> Set encoding for text translation (0 = none, 1 = ISO-8859-1, 2 = ISO-8859-2; default 1). </p>
<dt><code>-F</code></p>
<dd> Don&#8217;t set the font face, series, and style; only set it&#8217;s size and the baselineskip. By default, fig2dev sets all 5 font parameters when it puts some text. The disadvantage is that you can&#8217;t set the font from your LaTeX document. With this option on, you can set the font from your LaTeX document.</p>
<dt>
<dd> If any of the pictures included in your LaTeX document has been generated with <code>-F</code>, then all pictures must be generated with this option. </p>
<dt><code>-f font</code></p>
<dd> Set the default font used for text objects to <i>font</i>, where <i>font</i> is one of <i>rm</i>, <i>bf</i>, <i>it</i>, <i>sf</i> or <i>tt</i>. The default is <i>rm</i>. </p>
<dt><code>-l lwidth</code></p>
<dd> Use &quot;<code>	hicklines</code>&quot; when the width of the line is equal or wider than <i>lwidth.</i> The default is 2. </p>
<dt><code>-P</code></p>
<dd> Generate a complete LaTeX file. In other words, the output file can be formatted without requiring any changes. </p>
<dt><code>-R dummyarg</code></p>
<dd> Allow rotated text. Rotated text will be set using the otatebox command. So, you will need to include &quot;<code>
