---
title: "ps2eps(1)"
name: "ps2eps"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2eps/"
description: "ps2eps – convert PostScript to EPS (Encapsulated PostScript) files"
---

<h2 class="name">NAME</h2>
<p> ps2eps &#8211; convert PostScript to EPS (Encapsulated PostScript) files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ps2eps</code> [<code>-f</code>] [<code>-q</code>] [<code>-N</code>] [<code>-O</code>] [<code>-n</code>] [<code>-P</code>] [<code>-c</code>] [<code>-C</code>] [<code>-m</code>] [<code>-B</code>] [<code>-E</code>] [<code>-s&nbsp;</code><i>pagedim</i>] [<code>-t&nbsp;</code><i>offset</i>] [<code>-r&nbsp;</code><i>resolution</i>] [<code>-R&nbsp;</code><i>+|-|^</i>] [<code>-l</code>] [<code>-g</code>] [<code>-H</code>] [<code>-d</code>] [<code>-h|&#8211;help</code>] [<code>-a</code>] [<code>-W</code>] [<code>-L</code>] [<code>-V|&#8211;version</code>] [<code>&#8212;</code>] [<i>psfile1</i>] [<i>psfile2</i>] [<i>&#8230;</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents <code>ps2eps</code> version 1.68. </p>
<p> <code>ps2eps</code> is a tool (written in Perl) to produce Encapsulated PostScript Files (EPS/EPSF) from usual one-paged Postscript documents. It calculates correct Bounding Boxes for those EPS files and filters some special postscript command sequences that can produce erroneous results on printers. EPS files are often needed for including (scalable) graphics of high quality into TeX/LaTeX (or even Word) documents. </p>
<p> Without any argument, ps2eps reads from standard input and writes to standard output. If filenames are given as arguments they are processed one by one and output files are written to filenames with extension .eps. If input filenames have the extension .ps or .prn, this extension is replaced with .eps. In all other cases .eps is appended to the input filename. Please note that PostScript files for input should contain only one single page (you can possibly use the <code>psselect</code> from the psutils package to extract a single page from a document that contains multiple pages). </p>
<p> If BoundingBox in output seems to be wrong, please try options <code>&#8211;size</code> or <code>&#8211;ignoreBB</code>. See also section TROUBLESHOOTING. </p>
<h2>OPTIONS</h2>
<p> <code>ps2eps</code> follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Force overwriting existing files. <code>ps2eps</code> will not overwrite files by default to avoid deleting original EPS files accidently.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> quiet operation (no output while processing files, except errors).</dl>
<p> <code>-N</code>, <code>&#8211;noinsert</code></p>
<dl>
<dt>
<dd> do not insert any postscript code. Normally a few postscript instructions are added around the original postscript code by <code>ps2eps</code> which can be turned off by this option.</dl>
<p> <code>-O</code>, <code>&#8211;preserveorientation</code></p>
<dl>
<dt>
<dd> do not filter %%Orientation: header comment.</dl>
<p> <code>-n</code>, <code>&#8211;nofix</code></p>
<dl>
<dt>
<dd> do not try to fix postscript code by filtering some instructions.</dl>
<p> <code>-P</code>, <code>&#8211;removepreview</code></p>
<dl>
<dt>
<dd> remove preview image (smaller file, but no preview anymore).</dl>
<p> <code>-F</code>, <code>&#8211;fixps</code></p>
<dl>
<dt>
<dd> fix postscript code unconditionally. Otherwise, filtering is usually triggered by detection of certain drivers only.</dl>
<p> <code>-c</code>, <code>&#8211;comments</code></p>
<dl>
<dt>
<dd> preserve document structure comments.</dl>
<p> <code>-C</code>, <code>&#8211;clip</code></p>
<dl>
<dt>
<dd> insert postscript code for clipping. Unless <code>&#8211;nohires</code> is specified, the HiResBoundingBox (enlarged by 0.1 points) is used for clipping.</dl>
<p> <code>-m</code>, <code>&#8211;mono</code></p>
<dl>
<dt>
<dd> use black/white bitmap as base for calculation (default: off).</dl>
<p> <code>-s</code>, <code>&#8211;size</code>=<i>pagedim</i></p>
<dl>
<dt>
<dd> where <i>pagedim</i> is a pre-defined standard page size (e.g., a4,a0,b0,letter,&#8230;) or explicitly specified in a format <i>pagedim</i>:=<i>X</i>x<i>Y</i>[cm|in], where <i>X</i> and <i>Y</i> are numbers (floating points are accepted) followed by units centimeter (cm) or inch (in), (default: cm). Use <code>&#8211;size=list</code> to list pre-defined pagesizes. See also environment variable <i>PS2EPS_SIZE</i>.</dl>
<p> <code>-t</code>, <code>&#8211;translate=x,y</code></p>
<dl>
<dt>
<dd> specify an x,y offset (may be negative) in postscript points (1/72 dpi) for drawing. This option may be required if your drawing has negative coordinates which usually lets ghostscript cut the negative part of your picture, because it starts to render at positive coordinates. The resulting output will also be shifted.</dl>
<p> <code>-r</code>, <code>&#8211;resolution=dpi</code></p>
<dl>
<dt>
<dd> specify a resolution in dpi (dots per inch) for drawing under ghostscript. Default resolution is 144 dpi which is the double of the typical 72 dpi. This option may help if there is a hardware dependent resolution encoded in the postscript, e.g., 600dpi. Example: <code>ps2eps -l -r 600 test.ps</code></dl>
<p> <code>-R</code>, <code>&#8211;rotate=direction</code></p>
<dl>
<dt>
<dd> This option rotates the resulting EPS output. The parameter <i>direction</i> determines the direction of rotation: + means +90 degrees (clockwise),- means -90 degrees (counter-clockwise), and ^ means 180 degrees (up-side down).</dl>
<p> <code>-l</code>, <code>&#8211;loose</code></p>
<dl>
<dt>
<dd> expand the original tight bounding box by one point in each direction.</dl>
<p> <code>-B</code>, <code>&#8211;ignoreBB</code></p>
<dl>
<dt>
<dd> do not use existing bounding box as page size for rendering.</dl>
<p> <code>-E</code>, <code>&#8211;ignoreEOF</code></p>
<dl>
<dt>
<dd> do not use %%EOF as hint for end of file. Otherwise, <code>ps2eps</code> assumes that postscript code ends after the last %%EOF comment, because some drivers add trailing binary &#8220;garbage&#8221; code which gets deleted by <code>ps2eps</code> by default.</dl>
<p> <code>-g</code>, <code>&#8211;gsbbox</code></p>
<dl>
<dt>
<dd> use internal bbox device of ghostscript instead of the external C program <code>bbox</code>. The internal bbox device of ghostscript generates different values (sometimes even incorrect), so using the provided <code>bbox</code> should be more robust. See also environment variable <i>PS2EPS_GSBBOX</i>.</dl>
<p> <code>-H</code>, <code>&#8211;nohires</code></p>
<dl>
<dt>
<dd> do not generate a %%HiResBoundingBox comment for output.</dl>
<p> <code>-a</code>, <code>&#8211;accuracy</code></p>
<dl>
<dt>
<dd> increase the accuracy by turning subsample antialiasing on (may be slower)</dl>
<p> <code>-L</code>, <code>&#8211;license</code></p>
<dl>
<dt>
<dd> show licensing information.</dl>
<p> <code>-d</code>, <code>&#8211;debuggs</code></p>
<dl>
<dt>
<dd> show ghostscript call. This may be helpful for solving problems that occur during a ghostscript call.</dl>
<p> <code>-W</code>, <code>&#8211;warnings</code></p>
<dl>
<dt>
<dd> show warnings about sanity of generated EPS file. Certain postscript commands should not be contained in an EPS file. With this option set <code>ps2eps</code> will issue a warning if it detects at least one of them.</dl>
<h2>TROUBLESHOOTING</h2>
<p> Based on the given postscript source code (in most cases generated by some postscript printer driver) there are many potential obstacles or problems that may occur when trying to create proper EPS files. Please read this section carefully to be aware of common pitfalls.</p>
<h3>Incomplete/Clipped Images</h3>
<p> or how to determine the right size for ghostscript. </p>
<p> If you have documents that are larger than your ghostscript default (usually A4 or US letter), you have to specify the page dimensions explicitly using the <code>-s</code> option. Otherwise your EPS might be cut off during rasterizing by ghostscript resulting in a wrongly calculated bounding box. You can pass all pre-defined page sizes to <code>-s</code> that ghostscript understands. These are currently: 11&#215;17, ledger, legal, letter, lettersmall, archA, archB, archC, archD, archE a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, isob0, isob1, isob2, isob3, isob4, isob5, isob6, b0, b1, b2, b3, b4, b5, c0, c1, c2, c3, c4, c5, c6, jisb0, jisb1, jisb2, jisb3, jisb4, jisb5, jisb6, flsa, flse, halfletter. Unfortunately, all sizes are currently only available in portrait orientation (not landscape). </p>
<p> By default, <code>ps2eps</code> uses an already given %%BoundingBox from the source file, which often corresponds to the size of the physical page format for which the document was printed. However, you should be aware that this already specified bounding box may be not correct, thus resulting in a wrongly cropped (or even no usable) .eps-file. <code>ps2eps</code> can only do as good as ghostscript does in rendering the original postscript file (though <code>ps2eps</code> even works with negative and fractional values are contained in the original bounding box by using automatic translation). Therefore, if the given bounding box is to small or incorrect anyway, you can ignore the existing bounding box with the <code>-B</code> option, which will cause ghostscript to use its internal default size (or use <code>-s</code>). However, if the BoundingBox has negative coordinates, which is not allowed by the specification, <code>ps2eps</code> will shift the output to positive values. </p>
<p> Hint: to avoid rotating the picture if you have the original drawing in landscape format, you may use the &#8220;Encapsulated Postscript&#8221; option in the printer driver which should generate an EPS file (but with a bounding box of the sheet size!). But some Windows printer drivers are drawing the image with an offset from the bottom of the portrait page, so that a part of it is drawn outside the landscape oriented page. In this case, you&#8217;ll have to specify a square size of the page using the maximum length, e.g., 29.7cm x 29.7cm for an A4 page.</p>
<h3>Clipping</h3>
<p> or why gets some of my text deleted above the included .eps file? </p>
<p> Some postscript drivers draw a white rectangle from the top left corner of the page to the right lower corner of the object. This may erase some or even all text above your imported/included EPS file, which is very annoying. In order to prevent this, most programs have a clipping option for imported .eps files (within LaTeX you can use \includegraphics*{}) for this purpose. If this is unfortunately not the case, you can use the <code>-C</code> option of <code>ps2eps</code> which will (hopefully) do it for you. Unfortunately, PScript.dll 5.2 (Windows XP) introduced new very badly behaving Postscript code (initclip) which will even override the outer clipping! Thus, a new filter had to be installed in <code>ps2eps</code> which will fix it. </p>
<p> However, because most programs clip directly on the bounding box, you still may loose some pixels of your image, because the bounding box is described in the coarse resolution of postscript points, i.e. 72 dpi. In order to prevent this, you can use the <code>-l</code> option or <code>-C</code> option (for the latter, clipping by the importing program should be disabled then) to allow for a 1 point larger bounding box. <code>-C</code> clips around a 1 point enlarged bounding box and <code>-l</code> enlarges the bounding box values by 1 point (you can also combine both options).</p>
<h3>Included Filters</h3>
<p> Some postscript sequences, e.g., for using specific printer features (featurebegin &#8230;), are not working well within an .eps file, so <code>ps2eps</code> tries to filter them out. But please note that filters for postscript code may not work properly for your printer driver (<code>ps2eps</code> was mainly tested with HP and Adobe printer drivers, although it may work for all printers using the PScript.dll). In this case you can try to turn of filtering by using option <code>-n</code>, or try to find the bad sequence in the postscript code and adapt the filter rule in the <code>ps2eps</code> script (variables $linefilter, $rangefilter_begin, $rangefilter_end; linefilter is an expression for filtering single lines, rangefilter_&#8230; are expressions that filter all lines between a pattern matching $rangefilter_begin and $rangefilter_end; drop me an e-mail with your modifications). However, things may change as the printer drivers (e.g., PScript.dll) or postscript language evolve. </p>
<p> Some applications or drivers generate postscript code with leading or trailing binary code, which often confuses older postscript interpreters. <code>ps2eps</code> tries to remove such code, but it may sometimes make a wrong guess about start and end of the real postscript code (drop me an e-mail with a zipped postscript source, see section BUGS). </p>
<p> Comment lines or even blank lines are removed (which is the default to make .eps files smaller), which may corrupt your output. Please check the next section how to fix this. <code>ps2eps</code> removes blank lines and also &lt;CR&gt; (carriage ceturn &#8220;&#8221;) at the end of lines. However, nicely formatted postscript code gives a hint by using &#8220;%%BeginBinary&#8221; &#8220;%%EndBinary&#8221; comments. When <code>ps2eps</code> detects these comments it will refrain from any filtering action within the marked binary sections. </p>
<p> <code>ps2eps</code> filters also %%Orientation: comments by default (you can use option <code>-O</code> to turn off filtering), because ghostscript may &#8220;automagically&#8221; rotate images when generating PDF images, which is not desired in most cases. Hint: you can turn off that feature in ghostscript unconditionally by specifying -dAutoRotatePages=/None.</p>
<h3>Corrupted Output</h3>
<p> Some postscript code may get corrupted when comment lines or even blank lines are removed (which is the default to make .eps files smaller), because those files may contain encoded images which also have a % as first character in a line or use a special comment as end of image delimiter. If this is the case, use the <code>-c</code> option to prevent filtering comments.</p>
<h3>Color and memory</h3>
<p> <code>ps2eps</code> supports colored postscript, consequently letting ghostscript consume more resources for drawing its bitmap (roughly 6MBytes for an A4 page). <code>bbox</code> is reading the bitmap line by line so it consumes only minimal memory. If you experience problems with memory consumption of ghostscript, you may use the <code>-m</code> option for using a monochrome image. But this will probably result in wrongly determined bounding boxes with colored images, because ghostscript has to do black/white dithering and may thus suppress objects drawn in light colors. </p>
<p> Another option in case of memory problems and too long run times is to use the much more memory efficient internal ghostscript bbox by using the <code>-g</code> option.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Please note that a command line option always takes precedence over the related environment variable. </p>
<p> The environment variable <i>PS2EPS_SIZE</i> can be used to specify a default page size and take any argument that <code>&#8211;size</code> accepts. Examples: <code>export PS2EPS_SIZE=a0</code> (bash-like syntax) or <code>setenv PS2EPS_SIZE letter</code> (csh syntax). </p>
<p> If the environment variable <i>PS2EPS_GSBBOX</i> is set the internal bbox device of ghostscript will be used instead of the external command <code>bbox</code>. Examples: <code>export PS2EPS_GSBBOX=true</code> (bash-like syntax) or <code>setenv PS2EPS_GSBBOX 1</code> (csh syntax).</p>
<h2>EXAMPLES</h2>
<p> The usual call is simply: <code>ps2eps -l </code><i>file</i> </p>
<p> A relatively failsafe call would be (if your postscript is smaller than iso b0 [100cm x 141.4cm] and you have a fast computer with enough memory): <code>ps2eps -l -B -s b0 -c -n </code><i>file</i> </p>
<p> If output is not correct try: <code>ps2eps -l -B -s b0 -F </code><i>file</i></p>
<h2>AUTHOR</h2>
<p> <code>ps2eps</code> was written by Roland Bless.</p>
<h3>WHY?</h3>
<p> Other programs like <code>ps2epsi</code> do not calculate the bounding box always correctly (because the values are put on the postscript stack which may get corrupted by bad postscript code) or rounded it off so that clipping the EPS cut off some part of the image. <code>ps2eps</code> uses a double precision resolution of 144 dpi and appropriate rounding to get a proper bounding box. The internal bbox device of ghostscript generates different values (sometimes even incorrect), so using the provided <code>bbox</code> should be more robust. However, because normal clipping has only a resolution of 1/72dpi (postscript point), the clipping process may still erase parts of your EPS image. In this case please use the <code>-l</code> option to add an additional point of white space around the tight bounding box.</p>
<h3>ACKNOWLEDGMENTS</h3>
<p> Some people contributed code or suggestions to improve <code>ps2eps</code>. Here are at least some names (sorry if I forgot your name): Christophe Druet, Hans Ecke, Berend Hasselman, Erik Joergensen, Koji Nakamaru, Hans Fredrik Nordhaug, Michael Sharpe. Special thanks goes to Michael Sharpe from UCSD who suggested a lot of useful features for ps2eps and who fixed bbox to become more precise and robust. </p>
<p> An earlier version of this manual page was originally written by Rafael Laboissiere &lt;rafael at debian.org&gt; for the Debian system. Thank you Rafael! </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
<h2>BUGS</h2>
<p> If you experience problems, please check carefully all hints in the section TROUBLESHOOTING first. Otherwise, check for an updated version at m[blue]<code>idm388</code>m[] or send a gzipped file of relevant postscript source code with your error description and <code>ps2eps</code> version number to &lt;roland at bless.de&gt; (please allow some time to reply).</p>
<h2>SEE ALSO</h2>
<p> bbox (1), gs (1), ps2epsi (1)</p>
<h2>AUTHOR</h2>
<p> <code>Roland Bless</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Roland Bless </p>
<h2>Index</h2>
