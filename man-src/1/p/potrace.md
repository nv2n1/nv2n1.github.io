---
title: "potrace(1)"
name: "potrace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-potrace/"
description: "potrace – transform bitmaps into vector graphics."
---

<h2>NAME</h2>
<p> potrace &#8211; transform bitmaps into vector graphics.</p>
<h2>SYNOPSIS</h2>
<pre><code>
potrace[options][filename...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>potrace</code> is a tool for tracing a bitmap, which means, transforming a bitmap into a smooth, scalable image. The input is a bitmap, which means, a pixel-based image composed of the two colors black and white only. The output is EPS, PDF, SVG, or one of a number of other vector formats. A typical use is to create vector graphics from scanned data, such as company or university logos, handwritten notes, etc. The resulting image is not &quot;jaggy&quot; like a bitmap, but smooth. It can then be rendered at any resolution. </p>
<p> <code>potrace</code> can read bitmaps in the following formats: PBM, PGM, PPM (collectively known as PNM, see <a href="/docs/linux/man/5-pnm/">pnm</a>(5)), as well as BMP (Windows and OS/2 bitmap formats). The input image should only use the two colors black and white. If other pixel values appear in the input, they will be converted to black and white using a simple threshold method. </p>
<p> <code>potrace</code> can currently produce the following output formats: EPS, PostScript, PDF, SVG, DXF, GeoJSON, PGM, Gimppath, and XFig. Additional backends might be added in the future.</p>
<h2>OPTIONS</h2>
<p> The following options are supported. Dimensions (arguments of type <i>dim</i>) can have optional units, e.g. 6.5in, 15cm, 100pt. The default unit is inches (or centimeters, if this was configured at compile time, see COMPILE TIME CONFIGURATION below). For pixel-based output formats such as PGM, DXF, GeoJSON, and Gimppath, the default unit is pixels.</p>
<h3>General options:</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> print help message and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> print version info and exit. This also shows the defaults that were compiled into this version of <code>potrace</code>.</p>
<dt><code>-l, &#8211;license</code></p>
<dd> print license info and exit.</dl>
<h3>Input/output options:</h3>
<dl>
<dt><i>filename</i></p>
<dd> Each file can hold an input image, or multiple concatenated input images. If filename arguments are given, then <code>potrace</code> will by default create one output file for each input filename given. The name of the output file is obtained from the input filename by changing its suffix according to the chosen backend. If changing the suffix is impossible because the names of the input and output files would be identical, then the output filename is created by adding the &quot;-out&quot; suffix to the name of the input file. If no filename arguments are given, then <code>potrace</code> acts as a filter, reading from standard input and writing to standard output. A filename of &quot;-&quot; may be given to specify reading from standard input.</p>
<dt><code>-o </code><i>filename</i>, &#8211;output <i>filename</i></p>
<dd> write output to this file. All output is directed to the specified file. If this option is used, then multiple input filenames are only allowed for multi-page backends (see BACKEND TYPES below). In this case, each input file may contain one or more bitmaps, and all the bitmaps from all the input files are processed and the output concatenated into a single file. A filename of &quot;-&quot; may be given to specify writing to standard output.</p>
<dt><code>&#8212;</code></p>
<dd> End of options. Any remaining arguments are interpreted as filenames. This also disables filter mode, even if no filenames are given. This is useful for shell scripts, because <code>potrace &#8212; $FILENAMES</code> will behave correctly even for an empty list of filenames. However, <code>&#8212;</code> with an empty list of filenames is not permitted in conjunction with the <code>-o</code> option, because this would generate a document of zero pages, which none of the backends permit.</dl>
<h3>Backend selection:</h3>
<p> For general information, see also BACKEND TYPES below.</p>
<dl>
<dt><code>-b </code><i>name</i>, &#8211;backend <i>name</i></p>
<dd> Select backend by name, where <i>name</i> is one of eps, postscript, ps, pdf, pdfpage, svg, dxf, geojson, pgm, gimppath, xfig. Backend names can be abbreviated by a prefix as long as it is unambiguous. Backend names are case insensitive.</p>
<dt><code>-e, &#8211;eps, -b eps, &#8211;backend eps</code></p>
<dd> EPS backend (default). The output is an encapsulated PostScript file. This is a single-page, variable-sized, dimension-based backend.</p>
<dt><code>-p, &#8211;postscript, -b ps, &#8211;backend ps</code></p>
<dd> PostScript backend. The output is a PostScript file. This is a multi-page, fixed-size, dimension-based backend. If the input consists of multiple bitmaps, they are each rendered on a separate page.</p>
<dt><code>-b pdf, &#8211;backend pdf</code></p>
<dd> PDF backend. The output is a file in the Portable Document Format. If the input consists of multiple bitmaps, they are each rendered on a separate page. This is a multi-page, variable-sized, dimension-based backend.</p>
<dt><code>-b pdfpage, &#8211;backend pdfpage</code></p>
<dd> The PDFPage backend is like the PDF backend, except that it is fixed-size like the PostScript backend.</p>
<dt><code>-s, &#8211;svg, -b svg, &#8211;backend svg</code></p>
<dd> SVG backend. The output is a Scalable Vector Graphics (SVG) file. This is a single-page, variable-sized, dimension-based backend. Note that unless the <code>-r</code> option is given, the resolution of the input bitmap is assumed to be 72dpi.</p>
<dt><code>-b dxf, &#8211;backend dxf</code></p>
<dd> DXF backend. The output is a file in the Drawing Interchange Format (DXF). In this backend, all Bezier curves are approximated by piecewise circular arcs; this is suitable for processing in CAD software or for machining applications using CNC tools. This is a single-page, variable-sized, pixel-based backend. The <code>-u</code> option has no effect for this backend.</p>
<dt><code>-b geojson, &#8211;backend geojson</code></p>
<dd> GeoJSON backend. The output is a file in the format used by some applications processing geographical data. In this backend, all Bezier curves are approximated by 8 straight line segments. This is a single-page, variable-sized, pixel-based backend. The <code>-u</code> option has no effect for this backend.</p>
<dt><code>-g, &#8211;pgm, -b pgm, &#8211;backend pgm</code></p>
<dd> PGM backend. The output is a portable greymap (PGM) file. It is a convenient backend for antialiasing a bitmap image. This is a multi-page, variable-sized, pixel-based backend. If the input consists of more than one image, the images are concatenated in the output.</p>
<dt><code>-b gimppath, &#8211;backend gimppath</code></p>
<dd> Gimppath backend. This backend produces output suitable to be imported as a path by the GNU Image Manipulation Program (Gimp) (in the Layers, Channels &amp; Paths dialog, select Paths, then right-click and select Import Path). The output is actually an SVG file. The differences to the SVG backend are: the <code>&#8211;opaque</code> option has no effect, the <code>&#8211;flat</code> option is always on, and the dimensions are pixel-based. This is a single-page, variable-sized, pixel-based backend.</p>
<dt><code>-b xfig, &#8211;backend xfig</code></p>
<dd> XFig backend. This is a single-page, fixed-size, dimension-based backend. The output is a file in the XFig format. Note that XFig uses X-splines instead of Bezier curves, thus it is not possible to translate the output of <code>potrace</code> into the XFig format with absolute accuracy. This backend does a reasonable approximation using two control points for each Bezier curve segment. The <code>-u</code> option has no effect for this backend, because control points are always rounded to the nearest 1/1200 of an inch in XFig. Curve optimization is disabled. Implies <code>&#8211;opaque</code>.</dl>
<h3>Algorithm options:</h3>
<p> For more detailed information on these options, see TECHNICAL DOCUMENTATION below.</p>
<dl>
<dt><code>-z </code><i>policy</i>, &#8211;turnpolicy <i>policy</i></p>
<dd> specify how to resolve ambiguities in path decomposition. Must be one of black, white, right, left, minority, majority, or random. Default is minority. Turn policies can be abbreviated by an unambiguous prefix, e.g., one can specify min instead of minority.</p>
<dt><code>-t </code><i>n</i>, &#8211;turdsize <i>n</i></p>
<dd> suppress speckles of up to this many pixels.</p>
<dt><code>-a </code><i>n</i>, &#8211;alphamax <i>n</i></p>
<dd> set the corner threshold parameter. The default value is 1. The smaller this value, the more sharp corners will be produced. If this parameter is 0, then no smoothing will be performed and the output is a polygon. If this parameter is greater than 4/3, then all corners are suppressed and the output is completely smooth.</p>
<dt><code>-n, &#8211;longcurve</code></p>
<dd> turn off curve optimization. Normally <code>potrace</code> tries to join adjacent Bezier curve segments when this is possible. This option disables this behavior, resulting in a larger file size.</p>
<dt><code>-O </code><i>n</i>, &#8211;opttolerance <i>n</i></p>
<dd> set the curve optimization tolerance. The default value is 0.2. Larger values allow more consecutive Bezier curve segments to be joined together in a single segment, at the expense of accuracy.</p>
<dt><code>-u </code><i>n</i>, &#8211;unit <i>n</i></p>
<dd> set output quantization. Coordinates in the output are rounded to 1/unit pixels. The default of 10 usually gives good results. For some of the debug modes, a value of 100 gives more accurate output. This option has no effect for the XFig backend, which always rasterizes to 1/1200 inch, or for the DXF backend. For the GeoJSON backend, this option is only a hint; the actual rounding may be more, but not less, accurate than specified.</p>
<dt><code>-d </code><i>n</i>, &#8211;debug <i>n</i></p>
<dd> produce debugging output of type n. This has different effects for different backends. For the PostScript/EPS backends, the values n=1,2,3 illustrate the intermediate stages of the <code>potrace</code> algorithm.</dl>
<h3>Scaling and placement options:</h3>
<dl>
<dt><code>-P </code><i>format</i>, &#8211;pagesize <i>format</i></p>
<dd> for fixed-size backends, set page size. The following formats can be specified: A4, A3, A5, B5, Letter, Legal, Tabloid, Statement, Executive, Folio, Quarto, 10&#215;14. Format names are case insensitive. Also, an argument of the form <i>dim</i>x<i>dim</i> is accepted to specify arbitrary dimensions. The default page size is Letter (or A4, if this was configured at compile time, see COMPILE TIME CONFIGURATION below). Page format names can be abbreviated by a prefix as long as it is unambiguous. This option has no effect for variable-sized backends.</p>
<dt><code>-W </code><i>dim</i>, &#8211;width <i>dim</i></p>
<dd> set the width of output image (before any rotation and margins). If only one of width and height is specified, the other is adjusted accordingly so that the aspect ratio is preserved.</p>
<dt><code>-H </code><i>dim</i>, &#8211;height <i>dim</i></p>
<dd> set the height of output image. See <code>-W</code> for details.</p>
<dt><code>-r </code><i>n</i>[x<i>n</i>], &#8211;resolution <i>n</i>[x<i>n</i>]</p>
<dd> for dimension-based backends, set the resolution (in dpi). One inch in the output image corresponds to this many pixels in the input. Note that a larger value results in a smaller output image. It is possible to specify separate resolutions in the x and y directions by giving an argument of the form <i>n</i>x<i>n</i>. For variable-sized backends, the default resolution is 72dpi. For fixed-size backends, there is no default resolution; the image is by default scaled to fit on the page. This option has no effect for pixel-based backends. If <code>-W</code> or <code>-H</code> are specified, they take precedence.</p>
<dt><code>-x </code><i>n</i>[x<i>n</i>], &#8211;scale <i>n</i>[x<i>n</i>]</p>
<dd> for pixel-based backends, set the scaling factor. A value greater than 1 enlarges the output, a value between 0 and 1 makes the output smaller. The default is 1. It is possible to specify separate scaling factors for the x and y directions by giving an argument of the form <i>n</i>x<i>n</i>. This option has no effect for dimension-based backends. If <code>-W</code> or <code>-H</code> are specified, they take precedence.</p>
<dt><code>-S </code><i>n</i>, &#8211;stretch <i>n</i></p>
<dd> set the aspect ratio. A value greater than 1 means the image will be stretched in the y direction. A value between 0 and 1 means the image will be compressed in the y direction.</p>
<dt><code>-A </code><i>angle</i>, &#8211;rotate <i>angle</i></p>
<dd> set the rotation angle (in degrees). The output will be rotated counterclockwise by this angle. This is useful for compensating for images that were scanned not quite upright.</p>
<dt><code>-M </code><i>dim</i>, &#8211;margin <i>dim</i></p>
<dd> set all four margins. The effect and default value of this option depend on the backend. For variable-sized backends, the margins will simply be added around the output image (or subtracted, in case of negative margins). The default margin for these backends is 0. For fixed-size backends, the margin settings can be used to control the placement of the image on the page. If only one of the left and right margin is given, the image will be placed this distance from the respective edge of the page, and similarly for top and bottom. If margins are given on opposite sides, the image is scaled to fit between these margins, unless the scaling is already determined explicitly by one or more of the <code>-W</code>, <code>-H</code>, <code>-r</code>, or <code>-x</code> options. By default, fixed-size backends use a non-zero margin whose width depends on the page size.</p>
<dt><code>-L </code><i>dim</i>, &#8211;leftmargin <i>dim</i></p>
<dd> set the left margin. See <code>-M</code> for details.</p>
<dt><code>-R </code><i>dim</i>, &#8211;rightmargin <i>dim</i></p>
<dd> set the right margin. See <code>-M</code> for details.</p>
<dt><code>-T </code><i>dim</i>, &#8211;topmargin <i>dim</i></p>
<dd> set the top margin. See <code>-M</code> for details.</p>
<dt><code>-B </code><i>dim</i>, &#8211;bottommargin <i>dim</i></p>
<dd> set the bottom margin. See <code>-M</code> for details.</p>
<dt><code>&#8211;tight</code></p>
<dd> remove whitespace around the image before scaling and margins are applied. If this option is given, calculations of the width, height, and margins are based on the actual vector outline, rather than on the outer dimensions of the input pixmap, which is the default. In particular, the <code>&#8211;tight</code> option can be used to remove any existing margins from the input image. See the file placement.pdf for a more detailed illustration.</dl>
<h3>Color options:</h3>
<p> These options are only supported by certain backends. The DXF and GeoJSON backends do not support color.</p>
<dl>
<dt><code>-C </code><i>#rrggbb</i>, &#8211;color <i>#rrggbb</i></p>
<dd> set the foreground color of the output image. The default is black.</p>
<dt><code>&#8211;fillcolor </code><i>#rrggbb</i></p>
<dd> set the fill color of the output image, i.e., the color of the &quot;white&quot; parts that are enclosed by &quot;black&quot; parts. The default is to leave these parts transparent. Implies <code>&#8211;opaque</code>. Please note that this option sets the background color; to set the foreground color, use <code>&#8211;color</code> instead.</p>
<dt><code>&#8211;opaque</code></p>
<dd> fill in the white parts of the image opaquely, instead of leaving them transparent. This only applies to interior white parts, i.e., those that are enclosed inside a black outline. Opaqueness is always in effect for the XFig backend.</dl>
<h3>SVG options:</h3>
<dl>
<dt><code>&#8211;group</code></p>
<dd> for SVG output, try to group related paths together. Each path is grouped together with all paths that are contained inside it, so that they can be moved around as a unit with an SVG editor. This makes coloring individual components slightly more cumbersome, and thus it is not the default.</p>
<dt><code>&#8211;flat</code></p>
<dd> for SVG output, put the entire image into a single path. This makes it impossible to color the components individually, and thus it is not the default. But the resulting SVG file can be more easily imported by some applications such as Gimp. In fact, the Gimppath backend is a variation of the SVG backend with the <code>&#8211;flat</code> option and pixel-based scaling. The <code>&#8211;flat</code> option has no effect if <code>&#8211;opaque</code> has been selected.</dl>
<h3>PostScript/EPS/PDF options:</h3>
<dl>
<dt><code>-c, &#8211;cleartext</code></p>
<dd> do not compress the output. This option disables the use of compression filters in the PostScript and PDF output. In the PostScript backend, if <code>-c</code> and <code>-q</code> are used together, the resulting output can be easily read by other programs or even by humans.</p>
<dt><code>-2, &#8211;level2</code></p>
<dd> use PostScript level 2 compression (default). The resulting file size is ca. 40% smaller than if the <code>-c</code> option is used.</p>
<dt><code>-3, &#8211;level3</code></p>
<dd> use PostScript level 3 compression, if available. This gives slightly smaller files than using <code>-2</code>, but the resulting files may not print on older PostScript level 2 printers. If support for PostScript level 3 compression has been disabled at compile time, a warning message is printed and level 2 compression is used instead.</p>
<dt><code>-q, &#8211;longcoding</code></p>
<dd> turn off optimized numerical coding in PostScript output. Normally, <code>potrace</code> uses a very compact numerical format to represent Bezier curves in PostScript, taking advantage of existing redundancy in the curve parameters. This option disables this behavior, resulting in longer, but more readable output (particularly if the <code>-c</code> option is also used).</dl>
<h3>PGM options:</h3>
<dl>
<dt><code>-G </code><i>n</i>, &#8211;gamma <i>n</i></p>
<dd> set the gamma value for anti-aliasing (default is 2.2). Most computer displays do not render shades of grey linearly, i.e., a grey value of 0.5 is not displayed as being exactly half-way between black and white. The gamma parameter corrects for this, and therefore leads to nicer looking output. The default value of 2.2 is appropriate for most normal CRT displays.</dl>
<h3>Frontend options:</h3>
<dl>
<dt><code>-k </code><i>n</i>, &#8211;blacklevel <i>n</i></p>
<dd> set the threshold level for converting input images to bitmaps. The <code>potrace</code> algorithm expects a bitmap, thus all pixels of the input images are converted to black or white before processing begins. Pixels whose brightness is less than <i>n</i> are converted to black, all other pixels to white. Here <i>n</i> is a number between 0 and 1. One case is treated specially: if the input is in an indexed color format with exactly 2 colors, then the blacklevel is ignored and the darker of the two colors is mapped to black. </p>
<p> Note: the method used by <code>potrace</code> for converting greymaps to bitmaps is very crude; much better results can be obtained if a separate program, such as <code><a href="/docs/linux/man/1-mkbitmap/">mkbitmap</a></code>(1), is used for this purpose. In particular, <code><a href="/docs/linux/man/1-mkbitmap/">mkbitmap</a></code>(1), which is distributed with <code>potrace</code>, has the ability to scale and interpolate the image before thresholding, which results in much better preservation of detail.</p>
<dt><code>-i, &#8211;invert</code></p>
<dd> invert the input bitmap before processing.</dl>
<h3>Progress bar options:</h3>
<dl>
<dt><code>&#8211;progress</code></p>
<dd> display a progress bar for each bitmap that is processed. This is useful for interactive use. The default behavior is not to show any progress information.</p>
<dt><code>&#8211;tty </code><i>mode</i></p>
<dd> set the terminal mode for progress bar rendering. Possible values are &quot;vt100&quot;, which requires a vt100-compatible terminal, and &quot;dumb&quot;, which uses only ASCII characters. The default is system dependent.</dl>
<h2>BACKEND TYPES</h2>
<p> Backends can be classified in several ways, which affects the available command line options and their behavior:</p>
<dl>
<dt><code>Fixed-size or variable-sized:</code></p>
<dd> For fixed-size backends, the size of the page is always the same (for example Letter or A4, as specified at compile time or by the <code>-P</code> option). By default, the image will be centered and scaled to fit the page size. For variable-size backends, the size of the page follows the size of the image. Currently the PostScript (PS), PDFPage, and XFig backends are fixed-size, and the remaining backends are variable-size.</p>
<dt><code>Dimension-based or pixel-based:</code></p>
<dd> In dimension-based backends, distances are measured in physical units such as inches or centimeters. In pixel-based backends, distances are measured in pixel units. The <code>-r</code> option only works for dimension-based backends, and the <code>-x</code> option only works for pixel-based backends. Currently, the DXF, PGM, Gimppath, and GeoJSON backends are pixel-based, and the remaining backends are dimension-based. Currently, all pixel-based backends are variable-sized.</p>
<dt><code>Single-page or multi-page:</code></p>
<dd> Single-page backends can only accept a single image. Multi-page backends can accept multiple images, typically one per page of output. Currently, the PostScript (PS), PDF, PDFPage, and PGM backends are multi-page, and the remaining backends are single-page. Note that multiple input images can be read in two ways: from multiple input files (with the <code>-o</code> option), or from a single input file that holds several concatenated images.</dl>
<h2>COMPILE TIME CONFIGURATION</h2>
<p> Certain aspects of the behavior of <code>potrace</code> can be configured at compile time by passing the following options to the ./configure script.</p>
<dl>
<dt><code>&#8211;disable-zlib</code></p>
<dd> compile <code>potrace</code> without the zlib compression library. This means PostScript level 3 compression will not be available.</p>
<dt><code>&#8211;enable-metric</code></p>
<dd> compile <code>potrace</code> with centimeters as the default unit instead of inches.</p>
<dt><code>&#8211;enable-a4</code></p>
<dd> compile <code>potrace</code> with A4 as the default page size.</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on successful completion, 1 if the command line was invalid, and 2 on any other error.</p>
<h2>VERSION</h2>
<p> 1.13</p>
<h2>AUTHOR</h2>
<p> Peter Selinger &lt;selinger at users.sourceforge.net&gt; </p>
<p> Please see the file AUTHORS for a full list of other contributors.</p>
<h2>TECHNICAL DOCUMENTATION</h2>
<p> For a detailed technical description of the <code>potrace</code> algorithm, see the file potrace.pdf, which is available from the <code>potrace</code> web site. For information on the Potrace library API, see potracelib.pdf.</p>
<h2>WEB SITE AND SUPPORT</h2>
<p> The latest version of <code>potrace</code> is available from <a rel="nofollow" href="http://potrace.sourceforge.net/.">http://potrace.sourceforge.net/.</a> This site also contains a list of frequently asked questions, as well as information on how to obtain support.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkbitmap/">mkbitmap</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001-2015 Peter Selinger </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA. See also <a rel="nofollow" href="http://www.gnu.org/.">http://www.gnu.org/.</a> </p>
<h2>Index</h2>
