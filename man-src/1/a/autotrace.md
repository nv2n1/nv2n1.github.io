---

title: "autotrace(1)"
name: "autotrace"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autotrace/"
description: "autotrace – converts bitmap image data into vector graphics"
---

<p> autotrace &#8211; converts bitmap image data into vector graphics</p>
<h2>SYNOPSIS</h2>
<p> <code>autotrace</code> [<code>-background-color</code> <i> hexvalue</i>] [<code>-centerline</code>] [<code>-color-count</code> <i> int</i>] [<code>-corner-always-threshold</code> <i> angle</i>] [<code>-corner-surround</code> <i> int</i>] [<code>-corner-threshold</code> <i> angle</i>] [<code>-despeckle-level</code> <i> int</i>] [<code>-despeckle-tightness</code> <i> real</i>] [<code>-dpi</code> <i> int</i>] [<code>-error-threshold</code> <i> real</i>] [<code>-filter-iterations</code> <i> int</i>] [<code>-help</code>] [<code>-input-format</code> <i> format</i>] [<code>-line-reversion-threshold</code> <i> real</i>] [<code>-line-threshold</code> <i> real</i>] [<code>-list-input-formats</code>] [<code>-list-output-formats</code>] [<code>-log</code>] [<code>-output-file</code> <i> file</i>] [<code>-output-format</code> <i> format</i>] [<code>-preserve-width</code>] [<code>-remove-adjacent-corners</code>] [<code>-report-progress</code>] [<code>-debug-arch</code>] [<code>-debug-bitmap</code>] [<code>-tangent-surround</code> <i> int</i>] [<code>-version</code>] [<code>-width-factor</code> <i> real</i>] <i>inputfile</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>autotrace</i> program accepts bitmap graphics from the file <i>inputfile</i> specified on the command line, and as output produces a collection of splines approximating the original image, the converting the image from bitmap to vector format. It behaves in a manner similar to the commercial software known as *tream*ine or *orel*race. The result is sent to standard output unless the <code>-output-file</code> option is active.</p>
<h2>OPTIONS</h2>
<p> Options can begin with either <code>&#8212;</code> or <code>&#8211;</code>. Any unambiguous abbreviation can be used for the option name. Option names and values can be separated with either a space or equal sign (=).</p>
<dl>
<dt><code>-background-color</code><i> hexvalue</i></dt>
<dd> Employ the color specified by the hexadecimal code <i>hexcode</i> as the background that should be ignored, for example FFFFFF (default: no background color).</dd>
<dt><code>-centerline</code></dt>
<dd> Trace an object&#8217;s centerline (default: employ its outline).</dd>
<dt><code>-color-count</code><i> int</i></dt>
<dd> Reduce the bitmap to using the number of colors specified by the unsigned integer <i>int</i> (range: 1-256). The default value of 0 indicates that no color reduction is to be done. Does not work with grayscale images.</dd>
<dt><code>-corner-always-threshold</code><i> angle</i></dt>
<dd> Consider any angle at a pixel which falls below the specified <i>angle</i> (in degrees) as a corner, even if it is bordered by other corner pixels (default: 60).</dd>
<dt><code>-corner-surround</code><i> int</i></dt>
<dd> Consider the specified number of pixels on either side of a point when determining if that point is a corner (default: 4).</dd>
<dt><code>-corner-threshold</code><i> angle</i></dt>
<dd> Consider any pixel which forms an angle with its predecessor(s) and successor(s) that is smaller than the specified <i>angle </i> (in degrees) as a corner (default: 100).</dd>
<dt><code>-despeckle-level</code><i> int</i></dt>
<dd> Employ the specified integer (range: 1-20) as the value for despeckling (default: no despeckling).</dd>
<dt><code>-despeckle-tightness</code><i> real</i></dt>
<dd> Employ the specified real number (range: 0.0-8.0) as the value for despeckle tightness (default: 2.0).</dd>
<dt><code>-dpi</code><i> int</i></dt>
<dd> The dots per inch value in the input image, affects scaling of mif output image.</dd>
<dt><code>-error-threshold</code><i> real</i></dt>
<dd> Subdivide fitted curves that are offset by a number of pixels exceeding the specified real number (default: 2.0).</dd>
<dt><code>-filter-iterations</code><i> int</i></dt>
<dd> Smooth the curve the specified number of times prior to fitting (default: 4).</dd>
<dt><code>-help</code></dt>
<dd> Print a help message and exit.</dd>
<dt><code>-input-format</code><i> format</i></dt>
<dd> Employ the specified input format, where <i>format</i> is one of:</dd>
<dl>
<dl>
<dt><code>BMP</code> (Windows bitmap format)</dt>
<dd>
</dd><dt><code>PBM</code> (Portable BitMap format)</dt>
<dd>
</dd><dt><code>PGM</code> (Portable Graymap format)</dt>
<dd>
</dd><dt><code>PNM</code> (Portable Anymap format)</dt>
<dd>
</dd><dt><code>PPM</code> (Portable Pixmap format)</dt>
<dd>
</dd><dt><code>TGA</code> (Targa format)</dt>
<dd></dd></dl>
</dl>
<dt>
</dt><dd> The supported input formats are determined when the application is built and depend upon the availability of other software (the <code>-list-input-formats</code> command can be used to determine which are supported locally).</dd>
<dt><code>-line-reversion-threshold</code><i> real</i></dt>
<dd> When a spline is closer to a straight line than the specified real number weighted by the square of the curve length (default: .01), maintain it as a straight line, even if it is a list with curves.</dd>
<dt><code>-line-threshold</code><i> real</i></dt>
<dd> If a spline does not deviate from the straight line defined by its endpoints by more than the specified number of pixels, then treat it as a straight line (default: 1).</dd>
<dt><code>-list-input-formats</code></dt>
<dd> Send a list of the supported input formats to stderr.</dd>
<dt><code>-list-output-formats</code></dt>
<dd> Send a list of the supported output formats to stderr.</dd>
<dt><code>-log</code></dt>
<dd> Send a detailed progress report to the file <i>inputfile</i>.log.</dd>
<dt><code>-output-file</code><i> file</i></dt>
<dd> Send the output to the specified file.</dd>
<dt><code>-output-format</code><i> format</i></dt>
<dd> Employ the specified output format, where <i>format</i> is one of:</dd>
<dl>
<dl>
<dt><code>ai</code>(Adobe Illustrator)</dt>
<dd>
</dd><dt><code>cgm</code>(Computer Graphics Metafile)</dt>
<dd>
</dd><dt><code>dr2d</code>(IFF DR2D format, used almost exclusively on Amiga platforms)</dt>
<dd>
</dd><dt><code>dxf</code>(AutoCAD Drawing Exchange format)</dt>
<dd>
</dd><dt><code>emf</code>(Windows Enhanced Metafile format)</dt>
<dd>
</dd><dt><code>epd</code>(Encapsulated Vectorial Graphics format)</dt>
<dd>
</dd><dt><code>eps</code>(Encapsulated )</dt>
<dd>
</dd><dt><code>er</code>(Elastic Reality Shape format)</dt>
<dd>
</dd><dt><code>fig</code>(<i>xfig</i> (1) 3.2)</dt>
<dd>
</dd><dt><code>mif</code>(FrameMaker MIF format)</dt>
<dd>
</dd><dt><code>pdf</code>(Portable Data Format)</dt>
<dd>
</dd><dt><code>p2e</code>(<i>pstoedit</i> (1) frontend)</dt>
<dd>
</dd><dt><code>sk</code>(Sketch)</dt>
<dd>
</dd><dt><code>svg</code>(Scalable Vector Graphics)</dt>
<dd>
</dd><dt><code>swf</code>(Shockwave Flash 3)</dt>
<dd></dd></dl>
</dl>
<dt>
</dt><dd> The supported output formats are determined when the application is built and depend upon the availability of other software (the <code>-list-output-formats</code> command can be used to determine which are supported locally).</dd>
<dt><code>-preserve-width</code></dt>
<dd> Whether to preserve line width prior to thinning.</dd>
<dt><code>-remove-adjacent-corners</code></dt>
<dd> Remove adjacent corners.</dd>
<dt><code>-report-progress</code></dt>
<dd> Report tracing status in real time.</dd>
<dt><code>-debug-arch</code></dt>
<dd> Print the type of cpu.</dd>
<dt><code>-debug-bitmap</code></dt>
<dd> Dump loaded bitmap to &lt;input_name&gt;.bitmap.</dd>
<dt><code>-tangent-surround</code><i> int</i></dt>
<dd> Consider the specified number of points to either side of a point when computing the tangent at that point (default: 3).</dd>
<dt><code>-version</code></dt>
<dd> Print the version number of the program and exit.</dd>
<dt><code>-width-factor</code><i> real</i></dt>
<dd> Weight factor for fitting the linewidth.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>/depot/bin/autotrace</dt>
<dd> binary</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gimp/">gimp</a>(1), <a href="/docs/linux/man/1-imagemagick/">ImageMagick</a>(1), pbm(1), pgm(1), pnm(1), <a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a>(1), <a href="/docs/linux/man/1-pstoedit/">pstoedit</a>(1), pstoepd(1), sketch(1), <a href="/docs/linux/man/1-xfig/">xfig</a>(1), <a href="/docs/linux/man/1-xv/">xv</a>(1)</p>
<h2>AUTHORS</h2>
<p> Martin Weber (martweb [at] gmx.net) </p>
<p> Manual page by R. P. C. Rodgers, Lister Hill National Center for Biomedical Communications, U.S. National Library of Medicine (rodgers [at] nlm.nih.gov). </p>
