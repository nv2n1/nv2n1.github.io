---
title: "psconvert(1)"
name: "psconvert"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psconvert/"
description: "psconvert – Convert [E]PS file(s) to other formats using GhostScript"
---

<h2>NAME</h2>
<p> psconvert &#8211; Convert [E]PS file(s) to other formats using GhostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>psconvert</code> <i>psfile(s)</i> [ [<code>u</code>][<i>margins</i>][<code>&#8211;</code>][<code>+g</code><i>paint</i>][<code>+p</code>[<i>pen</i>]][<code>+r</code>][<code>+s</code>[<code>m</code>]|<code>S</code><i>width</i>[<code>u</code>]/<i>height</i>[<code>u</code>]] ] [ <i>gs_option</i> ] [ <code>-D</code><i>outdir</i> ] [ <code>-E</code><i>resolution</i> ] [ <code>-F</code><i>&lt;out_name&gt;</i> ] [ <i>ghost_path</i> ] [ ] [ <i>listfile</i> ] [ ] [ [<code>g</code>|<code>t</code>][1|2|4] ] [ <code>-S</code> ] [ <code>b</code>|<code>e</code>|<code>E</code>|<code>f</code>|<code>F</code>|<code>j</code>|<code>g</code>|<code>G</code>|<code>m</code>|<code>s</code> |<code>t</code> ] [ [<i>level</i>] ] [ [<code>+g</code>][<code>+k</code>][<code>+t</code><i>docname</i>][<code>+n</code><i>layername</i>][<code>+o</code><i>foldername</i>][<code>+a</code><i>altmode</i>[<i>alt</i>]][<code>+l</code><i>minLOD/maxLOD</i>][<code>+f</code><i>minfade/maxfade</i>][<code>+u</code><i>URL</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psconvert</code> converts one or more PostScript files to other formats (BMP, EPS, JPEG, PDF, PNG, PPM, SVG, TIFF) using GhostScript. Input file names are read from the command line or from a file that lists them. The size of the resulting images is determined by the BoundingBox (or HiResBoundingBox, if present). As an option, a tight (HiRes)BoundingBox may be computed first. As another option, it can compute ESRI type world files used to reference, for instance, tif files and make them be recognized as geotiff. Note: If the PostScript file calls on any of the Adobe PDF transparency extensions <i>and</i> PDF is not the selected output format, then the file will first be converted to a temporary PDF file (for the transparency to take effect) before converting the PDF to the desired output format.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>psfiles</i></p>
<dd> Names of PostScript files to be converted. The output files will have the same name (unless <code>-F</code> is used) but with the conventional extension name associated to the raster format (e.g., .jpg for the jpeg format). Use <code>-D</code> to redirect the output to a different directory.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>u</code>][<i>margins</i>][<code>&#8211;</code>][<code>+g</code><i>paint</i>][<code>+p</code>[<i>pen</i>]][<code>+r</code>][<code>+s</code>[<code>m</code>]|<code>S</code><i>width</i>[<code>u</code>]/<i>height</i>[<code>u</code>]]</p>
<dd> Adjust the BoundingBox and HiResBoundingBox to the minimum required by the image content. Append <code>u</code> to first remove any GMT-produced time-stamps. Optionally, append extra margins to the bounding box. Give either one (uniform), two (x and y) or four (individual sides) margins; append unit [Default is set by <i>PROJ_LENGTH_UNIT</i>]. Alternatively, use <code>-A-</code> to override any automatic setting of <code>-A</code> by <code>-W</code>. </p>
<p> Use the <code>-A+s</code><i>new_width</i> to resize the output image to exactly <i>new_width</i> units. The default is to use what is set by <i>PROJ_LENGTH_UNIT</i> but you can append a new unit and/or impose different width and height. What happens here is that GhostScript will do the re-interpolation work and the final image will retain the DPI resolution set by <code>-E</code>. Use <code>-A+sm</code> to set a maximum size and the new width are only imposed if the original figure width exceeds it. Append /<i>new_height</i> to also also impose a maximum height in addition to the width. Alternatively use <code>-A+S</code><i>scale</i> to scale the image by a constant factor. </p>
<p> Use the <code>-A+r</code> to round the HighRes BoundingBox instead of using the <i>ceil</i> function. This is going against Adobe Law but can be useful when creating very small images where the difference of one pixel might matter. If <code>-V</code> is used we also report the dimensions of the illustration. Use <code>-A+g</code><i>paint</i>to paint the BoundingBox behind the illustration and use <code>-A+p</code>[<i>pen</i>] to draw the BoundingBox outline (append a pen or accept the default pen of 0.25p,black).</p>
<dt><code>-C</code><i>gs_option</i></p>
<dd> Specify a single, custom option that will be passed on to GhostScript as is. Repeat to add several options [none].</p>
<dt><code>-D</code><i>outdir</i></p>
<dd> Sets an alternative output directory (which must exist) [Default is the same directory as the PS files]. Use <code>-D.</code> to place the output in the current directory instead.</p>
<dt><code>-E</code><i>resolution</i></p>
<dd> Set raster resolution in dpi [default = 720 for PDF, 300 for others].</p>
<dt><code>-F</code><i>out_name</i></p>
<dd> Force the output file name. By default output names are constructed using the input names as base, which are appended with an appropriate extension. Use this option to provide a different name, but without extension. Extension is still determined automatically.</p>
<dt><code>-G</code><i>ghost_path</i></p>
<dd> Full path to your GhostScript executable. NOTE: For Unix systems this is generally not necessary. Under Windows, the GhostScript path is now fetched from the registry. If this fails you can still add the GS path to system&#8217;s path or give the full path here. (e.g., <code>-G</code>c:\programs\gs\gs9.02in\gswin64c). WARNING: because of the poor decision of embedding the bits on the gs exe name we cannot satisfy both the 32 and 64 bits GhostScript executable names. So in case of &#8216;get from registry&#8217; failure the default name (when no <code>-G</code> is used) is the one of the 64 bits version, or gswin64c</p>
<dt><code>-I</code></p>
<dd> Enforce gray-shades by using ICC profiles. GhostScript versions &gt;= 9.00 change gray-shades by using ICC profiles. GhostScript 9.05 and above provide the &#8216;-dUseFastColor=true&#8217; option to prevent that and that is what <code>psconvert</code> does by default, unless option <code>-I</code> is set. Note that for GhostScript &gt;= 9.00 and &lt; 9.05 the gray-shade shifting is applied to all but PDF format. We have no solution to offer other than upgrade GhostScript.</p>
<dt><code>-L</code><i>listfile</i></p>
<dd> The <i>listfile</i> is an ASCII file with the names of the PostScript files to be converted.</p>
<dt><code>-N</code></p>
<dd> This option is obsolete. Use <code>-S</code> to print the GhostScript command, if applicable. Use <code>-Te</code> to save the intermediate EPS file.</p>
<dt><code>-P</code></p>
<dd> Force Portrait mode. All Landscape mode plots will be rotated back so that they show unrotated in Portrait mode. This is practical when converting to image formats or preparing EPS or PDF plots for inclusion in documents.</p>
<dt><code>-Q</code>[<code>g</code>|<code>t</code>][1|2|4]</p>
<dd> Set the anti-aliasing options for <code>g</code>raphics or <code>t</code>ext. Append the size of the subsample box (1, 2, or 4) [4]. Default is no anti-aliasing (same as <i>bits</i> = 1).</p>
<dt><code>-S</code></p>
<dd> Print to standard error the GhostScript command after it has been executed. This option also prevent all intermediate files from being removed.</p>
<dt><code>-Tb</code>|<code>e</code>|<code>E</code>|<code>f</code>|<code>F</code>|<code>j</code>|<code>g</code>|<code>G</code>|<code>m</code>|<code>s</code>|<code>t</code></p>
<dd> Sets the output format, where <code>b</code> means BMP, <code>e</code> means EPS, <code>E</code> means EPS with PageSize command, <code>f</code> means PDF, <code>F</code> means multi-page PDF, <code>j</code> means JPEG, <code>g</code> means PNG, <code>G</code> means transparent PNG (untouched regions are transparent), <code>m</code> means PPM, <code>s</code> means SVG, and <code>t</code> means TIFF [default is JPEG]. To <code>bjgt</code> you can append <code>&#8211;</code> in order to get a grayscale image. The EPS format can be combined with any of the other formats. For example, <code>-Tef</code> creates both an EPS and a PDF file. The <code>-TF</code> creates a multi-page PDF file from the list of input PS or PDF files. It requires the <code>-F</code> option.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>+g</code>][<code>+k</code>][<code>+t</code><i>docname</i>][<code>+n</code><i>layername</i>][<code>+o</code><i>foldername</i>][<code>+a</code><i>altmode</i>[<i>alt</i>]][<code>+l</code><i>minLOD/maxLOD</i>][<code>+f</code><i>minfade/maxfade</i>][<code>+u</code><i>URL</i>]</p>
<dd> Write a ESRI type world file suitable to make (e.g) .tif files be recognized as geotiff by software that know how to do it. Be aware, however, that different results are obtained depending on the image contents and if the <code>-B</code> option has been used or not. The trouble with the <code>-B</code> option is that it creates a frame and very likely its annotations. That introduces pixels outside the map data extent, and therefore the map extents estimation will be wrong. To avoid this problem use <i>&#8211;</i><i>&#8211;</i>MAP_FRAME_TYPE=inside option which plots all annotations and ticks inside the image and therefore does not compromise the coordinate computations. Pay attention also to the cases when the plot has any of the sides with whites only because than the algorithm will fail miserably as those whites will be eaten by the GhostScript. In that case you really must use <code>-B</code> or use a slightly off-white color. </p>
<p> Together with <code>-V</code> it prints on screen the gdal_translate (gdal_translate is a command line tool from the GDAL package) command that reads the raster + world file and creates a true geotiff file. Use <code>-W+g</code> to do a system call to gdal_translate and create a geoTIFF image right away. The output file will have a </p>
<p> The world file naming follows the convention of jamming a &#8216;w&#8217; in the file extension. So, if output is tif <code>-Tt</code> the world file is a sets <code>-A</code> <code>-P</code>. </p>
<p> Use <code>-W+k</code> to create a minimalist KML file that allows loading the image in GoogleEarth. Note that for this option the image must be in geographical coordinates. If not, a warning is issued but the KML file is created anyway. Several modifier options are available to customize the KML file in the form of <code>+</code><i>opt</i> strings. Append <code>+t</code><i>title</i> to set the document title [GMT KML Document], <code>+n</code><i>layername</i> to set the layer name, and <code>+a</code><i>/altmode</i>[<i>altitude</i>] to select one of 5 altitude modes recognized by Google Earth that determines the altitude (in m) of the image: <code>G</code> clamped to the ground, <code>g</code> append altitude relative to ground, <code>a</code> append absolute altitude, <code>s</code> append altitude relative to seafloor, and <code>S</code> clamp it to the seafloor. Control visibility of the layer with the <code>+l</code><i>minLOD/maxLOD</i> and <code>+f</code><i>minfade/maxfade</i> options. Finally, if you plan to leave the image itself on a server and only distribute the KML, use <code>+u</code><i>URL</i> to prepend the URL to the image reference. If you are building a multi-component KML file then you can issue a KML snipped without the KML header and trailer by using the <code>+o</code><i>foldername</i> modification; it will enclose the image and associated KML code within a KML folder of the specified name. See the KML documentation for further explanation (<i><a rel="nofollow" href="http://code.google.com/apis/kml/documentation/">http://code.google.com/apis/kml/documentation/</a></i>). </p>
<p> Further notes on the creation of georeferenced rasters. <code>psconvert</code> can create a georeferenced raster image with a world file OR uses GDAL to convert the GMT PostScript file to geotiff. GDAL uses Proj.4 for its projection library. To provide with the information it needs to do the georeferencing, GMT 4.5 embeds a comment near the start of the PostScript file defining the projection using Proj.4 syntax. Users with pre-GMT v4.5 PostScript files, or even non-GMT ps files, can provide the information <code>psconvert</code> requires by manually editing a line into the PostScript file, prefixed with %%PROJ. </p>
<p> For example the command </p>
<pre>
    gmt pscoast -JM0/12c -R-10/-4/37/43 -W1 -Di -Bg30m --MAP_FRAME_TYPE=inside &gt; cara.ps
adds this comment line
</pre>
<pre>
    %%PROJ: merc -10.0 -4.0 37.0 43.0 -1113194.908 -445277.963
    4413389.889 5282821.824 +proj=merc +lon_0=0 +k=-1 +x_0=0 +y_0=0
    +a=6378137.0 +b=6356752.314245 +ellps=WGS84 +datum=WGS84 +units=m +no_defs
where 'merc' is the keyword for the coordinate conversion; the 2 to
5th elements contain the map limits, 6 to 9th the map limits in
projected coordinates and the rest of the line has the regular proj4
string for this projection.
</pre>
<dt><code>-Z</code></p>
<dd> Remove the input PostScript file(s) after the conversion. The input file(s) will <code>not</code> be removed in case of failures.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>NOTES</h2>
<p> The conversion to raster images (BMP, JPEG, PNG, PPM or TIFF) inherently results in loss of details that are available in the original PostScript file. Choose a resolution that is large enough for the application that the image will be used for. For web pages, smaller dpi values suffice, for Word documents and PowerPoint presentations a higher dpi value is recommended. <code>psconvert</code> uses the loss-less DEFLATE compression technique when creating PDF and PNG files and LZW compression for TIFF images. </p>
<p> EPS is a vector, not a raster format. Therefore, the <code>-E</code> option has no effect on the creation of EPS files. Using the option <code>-Te</code> will remove PageSize commands from the PostScript file and will adjust the BoundingBox when the <code>-A</code> option is used. Note the original and required BoundingBox is limited to integer points, hence Adobe added the optional HiResBoundingBox to add more precision in sizing. The <code>-A</code> option calculates both and writes both to the EPS file used in the rasterization (and output if <code>-Te</code> is set). </p>
<p> Although PDF and SVG are also vector formats, the <code>-E</code> option has an effect on the resolution of pattern fills and fonts that are stored as bitmaps in the document. <code>psconvert</code> therefore uses a larger default resolution when creating PDF and SVG files. <code>-E</code> also determines the resolution of the boundingbox values used to indicate the size of the output PDF. In order to obtain high-quality PDF or SVG files, the <i>/prepress</i> options are in effect, allowing only loss-less DEFLATE compression of raster images embedded in the PostScript file. </p>
<p> Although <code>psconvert</code> was developed as part of the GMT, it can be used to convert PostScript files created by nearly any graphics program. However, <code>-Au</code> is GMT-specific. </p>
<p> The <code>ghostscript</code> program continues to be developed and occasionally its developers make decisions that affect <code>psconvert</code>. As of version 9.16 the SVG device has been removed. Fortunately, quality SVG graphics can be obtained by first converting to PDF and then install and use the package <code>pdf2svg</code>. </p>
<p> See <i>include-gmt-graphics</i> of the <code>GMT Technical Reference and Cookbook</code> for more information on how <code>psconvert</code> is used to produce graphics that can be inserted into other documents (articles, presentations, posters, etc.).</p>
<h2>EXAMPLES</h2>
<p> To convert the file psfile.ps to PNG using a tight BoundingBox and rotating it back to normal orientation in case it was in Landscape mode: </p>
<pre>
gmt psconvert psfile.ps -A -P -Tg
</pre>
<p> To convert the file map.ps to PDF, extend the BoundingBox by 0.2 cm, fill it with lightblue paint and draw outline with a thick pen: </p>
<pre>
gmt psconvert map.ps -A0.2c+glightblue+pthick -Tf
</pre>
<p> To create a 5 cm PNG version at 300 dpi of our example_01.ps file </p>
<pre>
gmt psconvert example_01.ps -A+s5c -Tg
</pre>
<p> To create a 3 pages PDF file from 3 individual PS files </p>
<pre>
gmt psconvert -TF -Fabc a.ps b.ps c.ps
</pre>
<p> To create a simple linear map with pscoast and convert it to tif with a </p>
<pre>
gmt pscoast -JX12cd -R-10/-4/37/43 -W1 -Di -Bg30m -P -G200 --MAP_FRAME_TYPE=inside &gt; cara.ps
gmt psconvert cara.ps -Tt -W
</pre>
<p> To create a Mercator version of the above example and use GDAL to produce a true geotiff file. </p>
<pre>
gmt pscoast -JM0/12c -R-10/-4/37/43 -W1 -Di -Bg30m -P -G200 --MAP_FRAME_TYPE=inside &gt; cara.ps
gdalwarp -s_srs +proj=merc cara.tif carageo.tiff
</pre>
<p> To create a Polar Stereographic geotiff file of Patagonia </p>
<pre>
gmt pscoast -JS-55/-60/15c -R-77/-55/-57.5/-48r -Di -Gred -P -Bg2 --MAP_FRAME_TYPE=inside &gt; patagonia.ps
gmt psconvert patagonia.ps -Tt -W+g -V
</pre>
<p> To create a simple KMZ file for use in Google Earth, try </p>
<pre>
gmt grdimage lonlatgrid.nc -Jx1 -Ccolors.cpt -P -B0g2 --MAP_FRAME_TYPE=inside &gt; tile.ps
gmt psconvert tile.ps -Tg -W+k+t&quot;my title&quot;+l256/-1 -V
</pre>
<p> (These commands assume that GhostScript can be found in your system&#8217;s path.)</p>
<h2>GHOSTSCRIPT OPTIONS</h2>
<p> Most of the conversions done in <code>psconvert</code> are handled by GhostScript. On most Unixes this program is available as <code>gs</code>; for Windows there is a version called <code>gswin32c</code>. GhostScript accepts a rich selection of command-line options that modify its behavior. Many of these are set indirectly by the options available above. However, hard-core usage may require some users to add additional options to fine-tune the result. Use <code>-S</code> to examine the actual command used, and add custom options via one or more instances of the <code>-C</code> option. For instance, to turn on image interpolation for all images, improving image quality for scaled images at the expense of speed, use <code>-C</code>-dDOINTERPOLATE. See <a rel="nofollow" href="http://www.ghostscript.com">www.ghostscript.com</a> for complete documentation.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
