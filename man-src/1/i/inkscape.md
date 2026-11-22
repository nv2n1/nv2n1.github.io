---

title: "inkscape(1)"
name: "inkscape"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape/"
description: "Inkscape – an SVG (Scalable Vector Graphics) editing program."
---

<p> Inkscape &#8211; an SVG (Scalable Vector Graphics) editing program. </p>
<h2>SYNOPSIS</h2>
<p> <tt>&quot;inkscape [options] [filename_1 filename_2 ...]&quot;</tt> </p>
<p> options: </p>
<pre><code>
- ?, --help - V, --version-- debug - info-- system - data - directory-- user - data - directory - p, --pipe-- pdf - page = PAGE-- pdf - poppler-- convert - dpi - method = METHOD-- no - convert - text - baseline - spacing - o, --export - filename = FILENAME-- export - overwrite-- export - type = TYPE[, TYPE] *--export - extension = EXTENSION - ID - C, --export - area - page - D, --export - area - drawing - a, --export - area = x0 : y0:x1:y1-- export - area - snap - d, --export - dpi = DPI - w, --export - width = WIDTH - h, --export - height = HEIGHT-- export - margin = MARGIN - i, --export - id = OBJECT - ID[; OBJECT - ID] * -j, --export - id - only - l, --export - plain - svg-- export - ps - level = LEVEL-- export - pdf - version = VERSION - T, --export - text - to - path-- export - latex-- export - ignore - filters - t, --export - use - hints - b, --export - background = COLOR - y, --export - background - opacity = VALUE - I, --query - id = OBJECT - ID[, OBJECT - ID] * -S, --query - all - X, --query - x - Y, --query - y - W, --query - width - H, --query - height-- vacuum - defs-- select = OBJECT - ID[, OBJECT - ID] *--actions = ACTION(:ARG)[; ACTION(:ARG)] *--action - list-- verb = VERB[; VERB] *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      --verb -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  list - g,
                                                                                                                    --with - gui-- batch - process-- shell
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Inkscape</code> is a Free and open source vector graphics editor. It offers a rich set of features and is widely used for both artistic and technical illustrations such as cartoons, clip art, logos, typography, diagramming and flowcharting. It uses vector graphics to allow for sharp printouts and renderings at unlimited resolution and is not bound to a fixed number of pixels like raster graphics. Inkscape uses the standardized <code>SVG</code> file format as its main format, which is supported by many other applications including web browsers. </p>
<p> The interface is designed to be comfortable and efficient for skilled users, while remaining conformant to <code>GNOME</code> standards so that users familiar with other GNOME applications can learn its interface rapidly. </p>
<p> <code>SVG</code> is a W3C standard XML format for 2D vector drawing. It allows defining objects in the drawing using points, paths, and primitive shapes. Colors, fonts, stroke width, and so forth are specified as `style&#8217; attributes to these objects. The intent is that since SVG is a standard, and since its files are text/xml, it will be possible to use SVG files in a sizeable number of programs and for a wide range of uses. </p>
<p> <code>Inkscape</code> uses SVG as its native document format, and has the goal of becoming the most fully compliant drawing program for SVG files available in the Open Source community.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Shows a help message.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Shows the Inkscape version and build date.</dd>
<dt><code>&#8211;debug-info</code></dt>
<dd> Prints technical information including Inkscape version, dependency versions and operating system. This Information is useful when debugging issues with Inkscape and should be included whenever filing a bug report.</dd>
<dt><code>&#8211;system-data-directory</code></dt>
<dd> Prints the system data directory where data files that ship with Inkscape are stored. This includes files which Inkscape requires to run (like unit definitions, built-in key maps, files describing UI layout, icon themes, etc.), core extensions, stock resources (filters, fonts, markers, color palettes, symbols, templates) and documentation (SVG example files, tutorials). </dd>
<p> The location in which Inkscape expects the system data directory can be overridden with the INKSCAPE_DATADIR environment variable.</p>
<dt><code>&#8211;user-data-directory</code></dt>
<dd> Prints the user profile directory where user-specific data files and preferences are stored. Custom extensions and resources (filters, fonts, markers, color palettes, symbols, templates) should be installed into their respective subdirectories in this directory. In addition placing a file with a name identical to one in the system data directory here allows to override most presets from the system data directory (e.g. default templates, UI files, etc.). </dd>
<p> The default location of the profile directory can be overridden with the INKSCAPE_PROFILE_DIR environment variable.</p>
<dt><code>-p</code>, <code>&#8211;pipe</code></dt>
<dd> Reads input file from standard input (stdin).</dd>
<dt><code>&#8211;pdf-page</code>=<i></i><i>PAGE</i><i></i></dt>
<dd> Imports the given page of a pdf file. Numbering starts with 1.</dd>
<dt><code>&#8211;pdf-poppler</code></dt>
<dd> By default Inkscape imports PDF files via an internal (poppler-derived) library. Text is stored as text. Meshes are converted to tiles. Use &#8211;pdf-poppler to import via an external (poppler with cairo backend) library instead. Text consists of groups containing cloned glyphs where each glyph is a path. Images are stored internally. Meshes cause entire document to be rendered as a raster image.</dd>
<dt><code>&#8211;convert-dpi-method</code>=<i></i><i>METHOD</i><i></i></dt>
<dd> Choose method used to rescale legacy (pre-0.92) files which render slightly smaller due to the switch from 90 DPI to 96 DPI when interpreting lengths expressed in units of pixels. Possible values are &#8220;none&#8221; (no change, document will render at 94% of its original size), &#8220;scale-viewbox&#8221; (document will be rescaled globally, individual lengths will stay untouched) and &#8220;scale-document&#8221; (each length will be re-scaled individually).</dd>
<dt><code>&#8211;no-convert-text-baseline-spacing</code></dt>
<dd> Do not automatically fix text baselines in legacy (pre-0.92) files on opening. Inkscape 0.92 adopts the CSS standard definition for the &#8216;line-height&#8217; property, which differs from past versions. By default, the line height values in files created prior to Inkscape 0.92 will be adjusted on loading to preserve the intended text layout. This command line option will skip that adjustment.</dd>
<dt><code>-o</code>, <code>&#8211;export-filename</code>=<i></i><i>FILENAME</i><i></i></dt>
<dd> Sets the name of the output file. The default is to re-use the name of the input file. If &#8211;export-type is also used, the file extension will be adjusted (or added) as appropriate. Otherwise the file type to export will be inferred from the extension of the specified filename. </dd>
<p> Usage of the special filename &#8220;-&#8221; makes Inkscape write the image data to standard output (stdout).</p>
<dt><code>&#8211;export-overwrite</code></dt>
<dd> Overwrites input file.</dd>
<dt><code>&#8211;export-type</code>=<i>TYPE[,TYPE]*</i></dt>
<dd> Specify the file type to export. Possible values: svg, png, ps, eps, pdf, emf, wmf and every file type for which an export extension exists. It is possible to export more than one file type at a time. </dd>
<p> Note that PostScript does not support transparency, so any transparent objects in the original SVG will be automatically rasterized. Used fonts are subset and embedded. The default export area is page; you can set it to drawing by &#8211;export-area-drawing. </p>
<p> Note that PDF format preserves the transparency in the original SVG.</p>
<dt><code>&#8211;export-extension</code>=<i>EXTENSION-ID</i></dt>
<dd> Allows to specify an output extension that will be used for exporting, which is especially relevant if there is more than one export option for a given file type. If set, the file extension in &#8211;export-filename and &#8211;export-type may be omitted. Additionally, if set, only one file type may be given in &#8211;export-type.</dd>
<dt><code>-C</code>, <code>&#8211;export-area-page</code></dt>
<dd> In SVG, PNG, PDF, PS exported area is the page. This is the default for SVG, PNG, PDF, and PS, so you don&#8217;t need to specify this unless you are using &#8211;export-id to export a specific object. For EPS this option is currently not supported.</dd>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></dt>
<dd> In SVG, PNG, PDF, PS, and EPS export, exported area is the drawing (not page), i.e. the bounding box of all objects of the document (or of the exported object if &#8211;export-id is used). With this option, the exported image will display all the visible objects of the document without margins or cropping. This is the default export area for EPS. For PNG, it can be used in combination with &#8211;export-use-hints.</dd>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></dt>
<dd> In PNG export, set the exported area in SVG user units (anonymous length units normally used in Inkscape SVG). The default is to export the entire document page. The point (0,0) is the lower-left corner.</dd>
<dt><code>&#8211;export-area-snap</code></dt>
<dd> For PNG export, snap the export area outwards to the nearest integer SVG user unit (px) values. If you are using the default export resolution of 96 dpi and your graphics are pixel-snapped to minimize antialiasing, this switch allows you to preserve this alignment even if you are exporting some object&#8217;s bounding box (with &#8211;export-id or &#8211;export-area-drawing) which is itself not pixel-aligned.</dd>
<dt><code>-d</code> <i></i><i>DPI</i><i></i>, <code>&#8211;export-dpi</code>=<i></i><i>DPI</i><i></i></dt>
<dd> The resolution used for PNG export. It is also used for fallback rasterization of filtered objects when exporting to PS, EPS, or PDF (unless you specify &#8211;export-ignore-filters to suppress rasterization). The default is 96 dpi, which corresponds to 1 SVG user unit (px, also called &#8220;user unit&#8221;) exporting to 1 bitmap pixel. This value overrides the DPI hint if used with &#8211;export-use-hints.</dd>
<dt><code>-w</code> <i></i><i>WIDTH</i><i></i>, <code>&#8211;export-width</code>=<i></i><i>WIDTH</i><i></i></dt>
<dd> The width of generated bitmap in pixels. This value overrides the &#8211;export-dpi setting (or the DPI hint if used with &#8211;export-use-hints).</dd>
<dt><code>-h</code> <i></i><i>HEIGHT</i><i></i>, <code>&#8211;export-height</code>=<i></i><i>HEIGHT</i><i></i></dt>
<dd> The height of generated bitmap in pixels. This value overrides the &#8211;export-dpi setting (or the DPI hint if used with &#8211;export-use-hints).</dd>
<dt><code>&#8211;export-margin</code>=<i></i><i>MARGIN</i><i></i></dt>
<dd> Adds a margin around the exported area. The size of the margin is specified in units of page size (for SVG) or millimeters (for PS/PDF). The option currently has no effect for other export formats.</dd>
<dt><code>-i</code> <i></i><i>ID</i><i></i>, <code>&#8211;export-id</code>=<i>OBJECT-ID[;OBJECT-ID]*</i></dt>
<dd> For PNG, PS, EPS, PDF and plain SVG export, the id attribute value of the object(s) that you want to export from the document; all other objects are not exported. By default the exported area is the bounding box of the object; you can override this using &#8211;export-area (PNG only) or &#8211;export-area-page. </dd>
<p> If you specify many values with a semicolon separated list of objects, each one will be exported separately. In this case the exported files will be named this way: [input_filename]_[ID].[export_type]</p>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></dt>
<dd> For PNG and plain SVG, only export the object whose id is given in &#8211;export-id. All other objects are hidden and won&#8217;t show in export even if they overlay the exported object. Without &#8211;export-id, this option is ignored. For PDF export, this is the default, so this option has no effect.</dd>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code></dt>
<dd> Export document(s) to plain SVG format, without sodipodi: or inkscape: namespaces and without RDF metadata. Use the &#8211;export-filename option to specify the filename.</dd>
<dt><code>&#8211;export-ps-level</code>=<i></i><i>LEVEL</i><i></i></dt>
<dd> Set language version for PS and EPS export. PostScript level 2 or 3 is supported. Default is 3.</dd>
<dt><code>&#8211;export-pdf-version</code>=<i></i><i>VERSION</i><i></i></dt>
<dd> Select the PDF version of the exported PDF file. This option basically exposes the PDF version selector found in the PDF-export dialog of the GUI. You must provide one of the versions from that combo-box, e.g. &#8220;1.4&#8221;. The default pdf export version is &#8220;1.4&#8221;.</dd>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></dt>
<dd> Convert text objects to paths on export, where applicable (for PS, EPS, PDF and SVG export).</dd>
<dt><code>&#8211;export-latex</code></dt>
<dd> (for PS, EPS, and PDF export) Used for creating images for LaTeX documents, where the image&#8217;s text is typeset by LaTeX. When exporting to PDF/PS/EPS format, this option splits the output into a PDF/PS/EPS file (e.g. as specified by &#8211;export-type) and a LaTeX file. Text will not be output in the PDF/PS/EPS file, but instead will appear in the LaTeX file. This LaTeX file includes the PDF/PS/EPS. Inputting (\input{image.tex}) the LaTeX file in your LaTeX document will show the image and all text will be typeset by LaTeX. See the resulting LaTeX file for more information. Also see GNUPlot&#8217;s `epslatex&#8217; output terminal.</dd>
<dt><code>&#8211;export-ignore-filters</code></dt>
<dd> Export filtered objects (e.g. those with blur) as vectors, ignoring the filters (for PS, EPS, and PDF export). By default, all filtered objects are rasterized at &#8211;export-dpi (default 96 dpi), preserving the appearance.</dd>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></dt>
<dd> While exporting to PNG, use export filename and DPI hints stored in the exported object (only with &#8211;export-id). These hints are set automatically when you export selection from within Inkscape. So, for example, if you export a shape with id=&#8220;path231&#8221; as /home/me/shape.png at 300 dpi from document.svg using Inkscape GUI, and save the document, then later you will be able to reexport that shape to the same file with the same resolution simply with </dd>
<pre>
    inkscape -i path231 -t document.svg
</pre>
<p> If you use &#8211;export-dpi, &#8211;export-width, or &#8211;export-height with this option, then the DPI hint will be ignored and the value from the command line will be used. If you use &#8211;export-filename with this option, then the filename hint will be ignored and the filename from the command line will be used.</p>
<dt><code>-b</code> <i></i><i>COLOR</i><i></i>, <code>&#8211;export-background</code>=<i></i><i>COLOR</i><i></i></dt>
<dd> Background color of exported PNG. This may be any SVG supported color string, for example &#8220;#ff007f&#8221; or &#8220;rgb(255, 0, 128)&#8221;. If not set, then the page color set in Inkscape in the Document Properties dialog will be used (stored in the pagecolor= attribute of sodipodi:namedview).</dd>
<dt><code>-y</code> <i></i><i>VALUE</i><i></i>, <code>&#8211;export-background-opacity</code>=<i></i><i>VALUE</i><i></i></dt>
<dd> Opacity of the background of exported PNG. This may be a value either between 0.0 and 1.0 (0.0 meaning full transparency, 1.0 full opacity) or greater than 1 up to 255 (255 meaning full opacity). If not set and the -b option is not used, then the page opacity set in Inkscape in the Document Properties dialog will be used (stored in the inkscape:pageopacity= attribute of sodipodi:namedview). If not set but the -b option is used, then the value of 255 (full opacity) will be used.</dd>
<dt><code>-I</code>, <code>&#8211;query-id</code>=<i>OBJECT-ID[,OBJECT-ID]*</i></dt>
<dd> Set the ID(s) of the object(s) whose dimensions are queried in a comma-separated list. If not set, query options will return the dimensions of the drawing (i.e. all document objects), not the page or viewbox. </dd>
<p> If you specify many values with a comma separated list of objects, any geometry query (e.g. &#8211;query-x) will return a comma separated list of values corresponding to the list of objects in <i>&#8211;query-id</i>.</p>
<dt><code>-S</code>, <code>&#8211;query-all</code></dt>
<dd> Prints a comma delimited listing of all objects in the SVG document with IDs defined, along with their x, y, width, and height values.</dd>
<dt><code>-X</code>, <code>&#8211;query-x</code></dt>
<dd> Query the X coordinate of the drawing or, if specified, of the object with &#8211;query-id. The returned value is in px (SVG user units).</dd>
<dt><code>-Y</code>, <code>&#8211;query-y</code></dt>
<dd> Query the Y coordinate of the drawing or, if specified, of the object with &#8211;query-id. The returned value is in px (SVG user units).</dd>
<dt><code>-W</code>, <code>&#8211;query-width</code></dt>
<dd> Query the width of the drawing or, if specified, of the object with &#8211;query-id. The returned value is in px (SVG user units).</dd>
<dt><code>-H</code>, <code>&#8211;query-height</code></dt>
<dd> Query the height of the drawing or, if specified, of the object with &#8211;query-id. The returned value is in px (SVG user units).</dd>
<dt><code>&#8211;vacuum-defs</code></dt>
<dd> Remove all unused items from the <tt>&quot;&lt;defs&gt;&quot;</tt> section of the SVG file. If this option is invoked in conjunction with &#8211;export-plain-svg, only the exported file will be affected. If it is used alone, the specified file will be modified in place.</dd>
<dt><code>&#8211;select</code>=<i>OBJECT-ID[,OBJECT-ID]*</i></dt>
<dd> The &#8211;select command will cause objects that have the ID specified to be selected. You can select many objects width a comma separated list. This allows various verbs to act upon them. To remove all the selections use <tt>&quot;--verb=EditDeselect&quot;</tt>. The object IDs available are dependent on the document specified to load.</dd>
<dt><code>&#8211;actions</code>=<i></i><i>ACTION</i><i>(:ARG)[;ACTION(:ARG)]*</i></dt>
<dd> Actions are a new method to call functions with an optional single parameter. To get a list of the action IDs available, use the &#8211;action-list command line option. Eventually all verbs will be replaced by actions. Temporarily, any verb can be used as an action (without a parameter). Note, most verbs require a GUI (even if they don&#8217;t use it). To close the GUI automatically at the end of processing, use &#8211;batch-process. In addition all export options have matching actions (remove the &#8216;&#8211;&#8216; in front of the option and replace &#8216;=&#8217; with &#8216;:&#8217;). </dd>
<p> If only actions are used &#8211;batch-process must be used. </p>
<p> Export can be forced at any point with the export-do action. This allows one to do multiple exports on a single file.</p>
<dt><code>&#8211;action-list</code></dt>
<dd> Prints a list of all available actions.</dd>
<dt><code>&#8211;verb</code>=<i>VERB[;VERB]*</i></dt>
<dd> The &#8211;verb command will execute a specific verb or list of verbs as if they were called from a menu or button. Dialogs will appear if that is part of the verb. To get a list of the verb IDs available, use the &#8211;verb-list command line option. </dd>
<p> Note that the &#8211;verb command requires a GUI. </p>
<p> Together with &#8211;select provides some basic scripting for Inkscape from the command line. They both can receive many arguments as needed on the command line and are executed in order on every document.</p>
<dt><code>&#8211;verb-list</code></dt>
<dd> Lists all the verbs that are available in Inkscape by ID. This ID can be used in defining keymaps or menus. It can also be used with the &#8211;verb command line option.</dd>
<dt><code>-g</code>, <code>&#8211;with-gui</code></dt>
<dd> Try to use the GUI (on Unix, use the X server even if <tt>$DISPLAY</tt> is not set).</dd>
<dt><code>&#8211;batch-process</code></dt>
<dd> Close GUI after executing all actions or verbs.</dd>
<dt><code>&#8211;shell</code></dt>
<dd> With this parameter, Inkscape will enter an interactive command line shell mode. In this mode, you type in commands at the prompt and Inkscape executes them, without you having to run a new copy of Inkscape for each command. This feature is mostly useful for scripting and server uses: it adds no new capabilities but allows you to improve the speed and memory requirements of any script that repeatedly calls Inkscape to perform command line tasks (such as export or conversions). </dd>
<p> In shell mode Inkscape expects a sequence of actions (or verbs) as input. They will be processed line by line, that means typically when pressing enter. It is possible (but not necessary) to put all actions on a single line. </p>
<p> The following example opens a file and exports it into two different formats, then opens another file and exports a single object: </p>
<p>file &#8211; open : file1.svg;<br/>
export &#8211; type : pdf;<br/>
export &#8211; do;<br/>
export &#8211; type : png;<br/>
export &#8211; do file &#8211; open : file2.svg;<br/>
export &#8211; id : rect2;<br/>
export &#8211; id &#8211; only;<br/>
export &#8211; filename : rect_only.svg;<br/>
export &#8211; do
</dl>
<h2>CONFIGURATION</h2>
<p> The main configuration file is located in ~/.config/inkscape/preferences.xml; it stores a variety of customization settings that you can change in Inkscape (mostly in the Inkscape Preferences dialog). Also in the subdirectories there, you can place your own: </p>
<p> $HOME/.config/inkscape/extensions/ &#8211; extension effects. </p>
<p> $HOME/.config/inkscape/icons/ &#8211; icons. </p>
<p> $HOME/.config/inkscape/keys/ &#8211; keyboard maps. </p>
<p> $HOME/.config/inkscape/templates/ &#8211; new file templates.</p>
<h2>DIAGNOSTICS</h2>
<p> The program returns zero on success or non-zero on failure. </p>
<p> A variety of error messages and warnings may be printed to STDERR or STDOUT. If the program behaves erratically with a particular SVG file or crashes, it is useful to look at this output for clues.</p>
<h2>EXAMPLES</h2>
<p> While obviously <code>Inkscape</code> is primarily intended as a GUI application, it can be used for doing SVG processing on the command line as well. </p>
<p> Open an SVG file in the GUI: </p>
<pre>
    inkscape filename.svg
</pre>
<p> Export an SVG file into PNG with the default resolution of 96 dpi (one SVG user unit translates to one bitmap pixel): </p>
<pre>
    inkscape --export-filename=filename.png filename.svg
</pre>
<p> Same, but force the PNG file to be 600&#215;400 pixels: </p>
<pre>
    inkscape --export-filename=filename.png -w 600 -h 400 filename.svg
</pre>
<p> Same, but export the drawing (bounding box of all objects), not the page: </p>
<pre>
    inkscape --export-filename=filename.png --export-area-drawing filename.svg
</pre>
<p> Export two different files into four distinct file formats each: </p>
<pre>
    inkscape --export-type=png,ps,eps,pdf filename1.svg filename2.svg
</pre>
<p> Export to PNG the object with id=&#8220;text1555&#8221;, using the output filename and the resolution that were used for that object last time when it was exported from the GUI: </p>
<pre>
    inkscape --export-id=text1555 --export-use-hints filename.svg
</pre>
<p> Same, but use the default 96 dpi resolution, specify the filename, and snap the exported area outwards to the nearest whole SVG user unit values (to preserve pixel-alignment of objects and thus minimize aliasing): </p>
<pre>
    inkscape --export-id=text1555 --export-filename=text.png --export-area-snap filename.svg
</pre>
<p> Convert an Inkscape SVG document to plain SVG: </p>
<pre>
    inkscape --export-plain-svg --export-filename=filename2.svg filename1.svg
</pre>
<p> Convert an SVG document to EPS, converting all texts to paths: </p>
<pre>
    inkscape --export-filename=filename.eps --export-text-to-path filename.svg
</pre>
<p> Query the width of the object with id=&#8220;text1555&#8221;: </p>
<pre>
    inkscape --query-width --query-id=text1555 filename.svg
</pre>
<p> Duplicate the objects with id=&#8220;path1555&#8221; and id=&#8220;rect835&#8221;, rotate the duplicates 90 degrees, save SVG, and quit: </p>
<p>inkscape&#8211; select = path1555, rect835&#8211; verb = &#8220;EditDuplicate;ObjectRotate90;FileSave;FileQuit&#8221; filename.svg</p>
<p> Select all objects with ellipse tag, rotate them 30 degrees, save the file, and quit. </p>
<p>inkscape&#8211; actions = &#8220;select-by-element:ellipse;transform-rotate:30;FileSave;FileClose&#8221; &#8211;batch &#8211; process filename.svg</p>
<p> Export the object with the ID MyTriangle with a semi transparent purple background to the file triangle_purple.png and with a red background to the file triangle_red.png. </p>
<pre><code>
inkscape-- actions = "export-id:MyTriangle; export-id-only; export-background:purple; export-background-opacity:0.5;export-filename:triangle_purple.png; export-do; export-background:red; export-background-opacity:1; export-filename:triangle_red.png" filename.svg
</code></pre>
<p> Read an SVG from standard input (stdin) and export it to PDF format: </p>
<pre>
    cat filename.svg | inkscape --pipe --export-filename=filename.pdf
</pre>
<p> Export an SVG to PNG format and write it to standard output (stdout), then convert it to JPG format with ImageMagick&#8217;s convert program: </p>
<pre>
    inkscape --export-type=png --export-filename=- filename.svg | convert - filename.jpg
</pre>
<p> Same as above, but also reading from a pipe (&#8211;export-filename can be omitted in this case) </p>
<pre>
    cat filename.svg | inkscape --pipe --export-type=png | convert - filename.jpg
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>INKSCAPE_PROFILE_DIR</code></dt>
<dd> Set a custom location for the user profile directory.</dd>
<dt><code>INKSCAPE_DATADIR</code></dt>
<dd> Set a custom location for the Inkscape data directory (e.g. $PREFIX/share if Inkscape&#8217;s shared files are in $PREFIX/share/inkscape).</dd>
<dt><code>INKSCAPE_LOCALEDIR</code></dt>
<dd> Set a custom location for the translation catalog.</dd></dl>
<p> For more details see also &lt;<a rel="nofollow" href="http://wiki.inkscape.org/wiki/index.php/Environment_variables">http://wiki.inkscape.org/wiki/index.php/Environment_variables</a>&gt;</p>
<h2>THEMES</h2>
<p> To load different icons sets instead of the default $PREFIX/share/inkscape/icons/icons.svg file, the directory $HOME/.config/inkscape/icons/ is used. Icons are loaded by name (e.g. <i>fill_none.svg</i>), or if not found, then from <i>icons.svg</i>. If the icon is not loaded from either of those locations, it falls back to the default system location. </p>
<p> The needed icons are loaded from SVG files by searching for the SVG id with the matching icon name. (For example, to load the &#8220;fill_none&#8221; icon from a file, the bounding box seen for SVG id &#8220;fill_none&#8221; is rendered as the icon, whether it comes from <i>fill_none.svg</i> or <i>icons.svg</i>.)</p>
<h2>OTHER INFO</h2>
<p> The canonical place to find <code>Inkscape</code> info is at &lt;<a rel="nofollow" href="https://www.inkscape.org/">https://www.inkscape.org/</a>&gt;. The website has news, documentation, tutorials, examples, mailing list archives, the latest released version of the program, bugs and feature requests databases, forums, and more.</p>
<h2>SEE ALSO</h2>
<p> potrace, cairo, rsvg, batik, ghostscript, pstoedit. </p>
<p> SVG compliance test suite: &lt;<a rel="nofollow" href="https://www.w3.org/Graphics/SVG/WG/wiki/Test_Suite_Overview">https://www.w3.org/Graphics/SVG/WG/wiki/Test_Suite_Overview</a>&gt; </p>
<p> SVG validator: &lt;<a rel="nofollow" href="https://validator.w3.org/">https://validator.w3.org/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><i>SVG</i><i>) 1.1 Specification</i> <i>W3C Recommendation 16 August 2011</i> &lt;<a rel="nofollow" href="https://www.w3.org/TR/SVG11/">https://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><i>SVG</i><i>) 1.2 Specification</i> <i>W3C Working Draft 13 April 2005</i> &lt;<a rel="nofollow" href="https://www.w3.org/TR/SVG12/">https://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><i>SVG</i><i>) 2 Specification</i> <i>W3C Candidate Recommendation 15 September 2016</i> &lt;<a rel="nofollow" href="https://www.w3.org/TR/SVG2/">https://www.w3.org/TR/SVG2/</a>&gt; </p>
<p> <i>Document Object Model (</i><i>DOM</i><i>): Level 2 Core</i> <i>W3C Recommendation 13 November 2000</i> &lt;<a rel="nofollow" href="https://www.w3.org/TR/DOM-Level-2-Core/">https://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>GUI NOTES</h2>
<p> To learn Inkscape&#8217;s GUI operation, read the manual in Help &gt; Inkscape manual, and the tutorials in Help &gt; Tutorials. </p>
<p> Apart from SVG, Inkscape can import (File &gt; Import) most bitmap formats (PNG, BMP, JPG, XPM, GIF, etc.), plain text (requires Perl), PS and EPS (requires Ghostscript), PDF and AI format (AI version 9.0 or newer). </p>
<p> Inkscape exports 32-bit PNG images (File &gt; Export PNG Image) as well as AI, PS, EPS, PDF, DXF, and several other formats via File &gt; Save as. </p>
<p> Inkscape can use the pressure and tilt of a graphic tablet pen for width, angle, and force of action of several tools, including the Calligraphic pen. </p>
<p> Inkscape includes a GUI front-end to the Potrace bitmap tracing engine (&lt;<a rel="nofollow" href="http://potrace.sf.net">http://potrace.sf.net</a>&gt;) which is embedded into Inkscape. </p>
<p> Inkscape can use external scripts (stdin-to-stdout filters) that are represented by commands in the Extensions menu. A script can have a GUI dialog for setting various parameters and can get the IDs of the selected objects on which to act via the command line. Inkscape comes with an assortment of effects written in Python.</p>
<h2>KEYBINDINGS</h2>
<p> To get a complete list of keyboard and mouse shortcuts, view doc/keys.html, or use the Keys and Mouse command in Help menu.</p>
<h2>BUGS</h2>
<p> Many bugs are known; please refer to the website (&lt;<a rel="nofollow" href="https://www.inkscape.org/">https://www.inkscape.org/</a>&gt;) for reviewing the reported ones and to report newly found issues. See also the Known Issues section in the Release Notes for your version (file `NEWS&#8216;).</p>
<h2>HISTORY</h2>
<p> The codebase that would become Inkscape began life in 1999 as the program Gill, the GNOME Illustrator application, created by Raph Levien. The stated objective for Gill was to eventually support all of SVG. Raph implemented the PostScript bezier imaging model, including stroking and filling, line cap style, line join style, text, etc. Raph&#8217;s Gill page is at &lt;<a rel="nofollow" href="http://www.levien.com/svg/">http://www.levien.com/svg/</a>&gt;. Work on Gill appears to have slowed or ceased in 2000. </p>
<p> The next incarnation of the codebase was to become the highly popular program Sodipodi, led by Lauris Kaplinski. The codebase was turned into a powerful illustration program over the course of several year&#8217;s work, adding several new features, multi-lingual support, porting to Windows and other operating systems, and eliminating dependencies. </p>
<p> Inkscape was formed in 2003 by four active Sodipodi developers, Bryce Harrington, MenTaLguY, Nathan Hurst, and Ted Gould, wanting to take a different direction with the codebase in terms of focus on SVG compliance, interface look-and-feel, and a desire to open development opportunities to more participants. The project progressed rapidly, gaining a number of very active contributors and features. </p>
<p> Much work in the early days of the project focused on code stabilization and internationalization. The original renderer inherited from Sodipodi was laced with a number of mathematical corner cases which led to unexpected crashes when the program was pushed beyond routine uses; this renderer was replaced with Livarot which, while not perfect either, was significantly less error prone. The project also adopted a practice of committing code frequently, and encouraging users to run developmental snapshots of the program; this helped identify new bugs swiftly, and ensure it was easy for users to verify the fixes. As a result, Inkscape releases have generally earned a reputation for being robust and reliable. </p>
<p> Similarly, efforts were taken to internationalize and localize the interface, which has helped the program gain contributors worldwide. </p>
<p> Inkscape has had a beneficial impact on the visual attractiveness of Open Source in general, by providing a tool for creating and sharing icons, splash screens, website art, and so on. In a way, despite being &#8220;just an drawing program&#8221;, Inkscape has played an important role in making Open Source more visually stimulating to larger audiences.</p>
<h2>AUTHORS</h2>
<p> This codebase owes its existence to a large number of contributors throughout its various incarnations. The following list is certainly incomplete, but serves to recognize the many shoulders on which this application sits: </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, Adam Belis, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Adrian Boguszewski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Brynn, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Moritz Eberl, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Sebastian Faubel, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, René de Hesselle, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, Marc Jeanmougin, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Patrick McDermott, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Jean Franco Amoni Rodríguez, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Markus Schwienbacher, Danilo Šegan, Abhishek Sharma, Tim Sheridan, Shivaken, Michael Sloan, John Smith, Sandra Snan, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Patrick Storz, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Parcly Taxel, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, Masatake Yamato, David Yip</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> <code>Copyright (C)</code> 1999-2020 by Authors. </p>
<p> <code>Inkscape</code> is free software; you can redistribute it and/or modify it under the terms of the GPL version 3 or later. </p>
