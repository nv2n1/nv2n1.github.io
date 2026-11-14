---
title: "ps2raster(1)"
name: "ps2raster"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2raster/"
description: "ps2raster – Converts one or several PostScript file(s) to other formats using GhostScript"
---

<h2>NAME</h2>
<p> ps2raster &#8211; Converts one or several <i>PostScript</i> file(s) to other formats using GhostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>ps2raster</code> <i>psfile(s)</i> [ <code>-A</code>[<code>u</code>|-] ] [ <code>-C</code><i>gs_option</i>] [ <code>-D</code><i>outdir</i> ] [ <code>-E</code><i>resolution</i> ] [ <code>-G</code><i>ghost_path</i> ] [ <code>-L</code><i>listfile</i>] [ <code>-P</code> ] [ <code>-Q</code>[<code>g</code>|<code>t</code>][1|2|4] ] [ <code>-S</code> ] [ <code>-Tb</code>|<code>e</code>|<code>f</code>|<code>j</code>|<code>g</code>|<code>G</code>|<code>m</code>|<code>t</code> ] [ <code>-V</code> ] [ <code>-W</code>[<code>+g</code>][<code>+t</code><i>docname</i>][<code>+n</code><i>layername</i>][<code>+a</code><i>altmode</i>[<i>alt</i>]][<code>+l</code><i>minLOD/maxLOD</i>][<code>+f</code><i>minfade/maxfade</i>][<code>+u</code><i>URL</i>] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ps2raster</code> converts one or more <i>PostScript</i> files to other formats (BMP, EPS, JPEG, PDF, PNG, PPM, TIFF) using GhostScript. Input file names are read from the command line or from a file that lists them. The size of the resulting images is determined by the BoundingBox (or HiResBoundingBox, if present). As an option, a tight (HiRes)BoundingBox may be computed first. As another option, it can compute ESRI type world files used to reference, for instance, tif files and make them be recognized as geotiff.</p>
<dl>
<dt><i>psfiles</i></p>
<dd> Names of <i>PostScript</i> files to be converted. The output files will have the same name (unless <code>-F</code> is used) but with the conventional extension name associated to the raster format (e.g. .jpg for the jpeg format). Use <code>-D</code> to redirect the output to a different directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Adjust the BoundingBox and HiResBoundingBox to the minimum required by the image content. Append <code>u</code> to first remove any GMT-produced time-stamps. Use <code>-A-</code> to override any automatic setting of <code>-A</code> by <code>-W</code>.</p>
<dt><code>-C</code></p>
<dd> Specify a single, custom option that will be passed on to GhostScript as is. Repeat to add several options [none].</p>
<dt><code>-D</code></p>
<dd> Sets an alternative output directory (which must exist) [Default is the same directory as the PS files]. Use <code>-D.</code> to place the output in the current directory instead.</p>
<dt><code>-E</code></p>
<dd> Set raster resolution in dpi [default = 720 for PDF, 300 for others].</p>
<dt><code>-F</code></p>
<dd> Force the output file name. By default output names are constructed using the input names as base, which are appended with an appropriate extension. Use this option to provide a different name, but without extension. Extension is still determined automatically.</p>
<dt><code>-G</code></p>
<dd> Full path to your GhostScript executable. NOTE: For Unix systems this is generally not necessary. However, under Windows, GhostScript is not added to the system&#8217;s path. So either you do it yourself,or give the full path here. (e.g., <code>-G</code>c:\programs\gs\gs7.05in\gswin32c).</p>
<dt><code>-L</code></p>
<dd> The <i>listfile</i> is an ASCII file with the names of the <i>PostScript</i> files to be converted.</p>
<dt><code>-N</code></p>
<dd> This option is obsolete. Use <code>-S</code> to print the GhostScript command, if applicable. Use <code>-Te</code> to save the intermediate EPS file.</p>
<dt><code>-P</code></p>
<dd> Force Portrait mode. All Landscape mode plots will be rotated back so that they show unrotated in Portrait mode. This is practical when converting to image formats or preparing EPS or PDF plots for inclusion in documents.</p>
<dt><code>-Q</code></p>
<dd> Set the anti-aliasing options for <code>g</code>raphics or <code>t</code>ext. Append the size of the subsample box (1, 2, or 4) [4]. Default is no anti-aliasing (same as <i>bits</i> = 1).</p>
<dt><code>-S</code></p>
<dd> Print to standard output the GhostScript command after it has been executed.</p>
<dt><code>-T</code></p>
<dd> Sets the output format, where <code>b</code> means BMP, <code>e</code> means EPS, <code>f</code> means PDF, <code>j</code> means JPEG, <code>g</code> means PNG, <code>G</code> means transparent PNG (untouched regions are transparent), <code>m</code> means PPM, and <code>t</code> means TIFF [default is JPEG]. For <code>bjgt</code> you can append &#8211; to get a grayscale image only. The EPS format can be combined with any of the other formats. For example, <code>-Tef</code> creates both an EPS and a PDF file.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-W</code></p>
<dd> Write a ESRI type world file suitable to make (e.g) .tif files be recognized as geotiff by softwares that know how to do it. Be aware, however, that different results are obtained depending on the image contents and if the <code>-B</code> option has been used or not. The trouble with the <code>-B</code> option is that it creates a frame and very likely its annotations. That introduces pixels outside the map data extent, and therefore the map extents estimation will be wrong. To avoid this problem use &#8211;BASEMAP_TYPE=inside option which plots all annotations and ticks inside the image and therefore does not compromise the coordinate computations. Pay attention also to the cases when the plot has any of the sides with whites only because than the algorithm will fail miserably as those whites will be eaten by the GhostScript. In that case you really must use <code>-B</code> or use a slightly off-white color.<br />
 Together with <code>-V</code> it prints on screen the gdal_translate (gdal_translate is a command line tool from the GDAL package) command that reads the raster + world file and creates a true geotiff file. Use <code>-W+g</code> to do a system call to gdal_translate and create a geoTIFF image right away. The output file will have a .tiff extension.<br />
 The world file naming follows the convention of jamming a &#8216;w&#8217; in the file extension. So, if output is tif <code>-Tt</code> the world file is a .tfw, for jpeg we have a .jgw and so on. This option automatically sets <code>-A</code> <code>-P</code>.<br />
 Use <code>-W+k</code> to create a minimalist KML file that allows loading the image in GoogleEarth. Note that for this option the image must be in geographical coordinates. If not, a warning is issued but the KML file is created anyway. Several modifier options are available to customize the KML file in the form of <code>+</code><i>opt</i> strings. Append <code>+t</code><i>title</i> to set the document title [GMT KML Document], <code>+n</code><i>layername</i> to set the layer name, and <code>+a</code><i>/altmode</i>[<i>altitude</i>] to select one of 5 altitude modes recognized by Google Earth that determines the altitude (in m) of the image: <code>G</code> clamped to the ground, <code>g</code> append altitude relative to ground, <code>a</code> append absolute altitude, <code>s</code> append altitude relative to seafloor, and <code>S</code> clamp it to the seafloor. Control visibility of the layer with the <code>+l</code><i>minLOD/maxLOD</i> and <code>+f</code><i>minfade/maxfade</i> options. FInally, if you plan to leave the image itself on a server and only distribute the KML, use <code>+u</code><i>URL</i> to prepend the URL to the image reference. See the KML documentation for further explanation (<a rel="nofollow" href="http://code.google.com/apis/kml/documentation/">http://code.google.com/apis/kml/documentation/</a>).<br />
 Further notes on the creation of georeferenced rasters. <code>ps2raster</code> can create a georeferenced raster image with a world file OR uses GDAL to convert the GMT <i>PostScript</i> file to geotiff. GDAL uses Proj.4 for it&#8217;s projection library. To provide with the information it needs to do the georeferencing, GMT 4.5 embeds a comment near the start of the <i>PostScript</i> file defining the projection using Proj.4 syntax. Users with pre-GMT v4.5 <i>PostScript</i> files, or even non-GMT ps files, can provide the information <code>ps2raster</code> requires by manually editing a line into the <i>PostScript</i> file, prefixed with %%PROJ.<br />
 For example the command <code>pscoast</code> <code>-JM0/12c</code> <code>-R</code>-10/-4/37/43 <code>-W1</code> <code>-Di</code> <code>-Bg30m</code> &#8211;BASEMAP_TYPE=inside &gt; cara.ps<br />
 adds this comment line<br />
 %%PROJ: merc -10.0 -4.0 37.0 43.0 -1113194.908 -445277.963 4413389.889 5282821.824 +proj=merc +lon_0=0 +k=-1 +x_0=0 +y_0=0 +a=6378137.0 +b=6356752.314245<br />
 where &#8216;merc&#8217; is the keyword for the coordinate conversion; the 2 to 5th elements contain the map limits, 6 to 9th the map limits in projected coordinates and the rest of the line has the regular proj4 string for this projection.</dl>
<h2>NOTES</h2>
<p> The conversion to raster images (BMP, JPEG, PNG, PPM or TIFF) inherently results in loss of details that are available in the original <i>PostScript</i> file. Choose a resolution that is large enough for the application that the image will be used for. For web pages, smaller dpi values suffice, for Word documents and PowerPoint presentations a higher dpi value is recommended. <code>ps2raster</code> uses the loss-less Flate compression technique when creating JPEG, PNG and TIFF images. </p>
<p> EPS is a vector, not a raster format. Therefore, the <code>-E</code> option has no effect on the creation of EPS files. Using the option <code>-Te</code> will remove PageSize commands from the <i>PostScript</i> file and will adjust the BoundingBox when the <code>-A</code> option is used. Note the original and required BoundingBox is limited to integer points, hence Adobe added the optional HiResBoundingBox to add more precision in sizing. The <code>-A</code> option calculates both and writes both to the EPS file used in the rasterization (and output if <code>-Te</code> is set). </p>
<p> Although PDF is also a vector format, the <code>-E</code> option has an effect on the resolution of pattern fills and fonts that are stored as bitmaps in the document. <code>ps2raster</code> therefore uses a larger default resolution when creating PDF files. In order to obtain high-quality PDF files, the <i>/prepress</i> options are in effect, allowing only loss-less Flate compression of raster images embedded in the <i>PostScript</i> file. </p>
<p> Although <code>ps2raster</code> was developed as part of the <code>GMT</code>, it can be used to convert <i>PostScript</i> files created by nearly any graphics program. However, <code>-Au</code> is <code>GMT</code>-specific. </p>
<p> See Appendix C of the <code>GMT Technical Reference and Cookbook</code> for more information on how <code>ps2raster</code> is used to produce graphics that can be inserted into other documents (articles, presentations, posters, etc.).</p>
<h2>EXAMPLES</h2>
<p> To convert the file psfile.ps to PNG using a tight BoundingBox and rotating it back to normal orientation in case it was in Landscape mode: </p>
<p> <code>ps2raster</code> psfile.ps <code>-A</code> <code>-P</code> <code>-Tg</code> </p>
<p> To create a simple linear map with pscoast and convert it to tif with a .tfw the tight BoundingBox computation. </p>
<p> <code>pscoast</code> <code>-JX12cd</code> <code>-R</code>-10/-4/37/43 <code>-W1</code> <code>-Di</code> <code>-Bg30m</code> <code>-P</code> <code>-G200</code> &#8211;BASEMAP_TYPE=inside &gt; cara.ps </p>
<p> <code>ps2raster</code> cara <code>-Tt</code> <code>-W</code> </p>
<p> To create a Mercator version of the above example and use GDAL to produce a true geotiff file. </p>
<p> <code>pscoast</code> <code>-JM0/12c</code> <code>-R</code>-10/-4/37/43 <code>-W1</code> <code>-Di</code> <code>-Bg30m</code> <code>-P</code> <code>-G200</code> &#8211;BASEMAP_TYPE=inside &gt; cara.ps </p>
<p> <code>gdalwarp</code> -s_srs +proj=merc cara.tif carageo.tiff </p>
<p> To create a Polar Stereographic geotiff file of Patagonia </p>
<p> pscoast -JS-55/-60/15c -R-77/-55/-57.5/-48r -Di -Gred -P -Bg2 &#8211;BASEMAP_TYPE=inside &gt; patagonia.ps </p>
<p> ps2raster patagonia.ps -Tt -W+g -V </p>
<p> To create a simple KMZ file for use in Google Earth, try </p>
<p> grdimage lonlatgrid.nc -Jx1 -Ccolors.cpt -P -B0g2 &#8211;BASEMAP_TYPE=inside &gt; tile.ps </p>
<p> ps2raster tile.ps -Tg -W+k+t&quot;my title&quot;+l256/-1 -V </p>
<p> (These commands assume that GhostScript can be found in your system&#8217;s path.)</p>
<h2>BINARY DATA</h2>
<p> <code>GMT</code> programs can produce binary <i>PostScript</i> image data and this is determined by the default setting PS_IMAGE_FORMAT. Because <code>ps2raster</code> needs to process the input files on a line-by-line basis you need to make sure the image format is set to <i>ascii</i> and not <i>bin</i>.</p>
<h2>GHOSTSCRIPT OPTIONS</h2>
<p> Most of the conversions done in <code>ps2raster</code> are handled by GhostScript. On most Unixes this program is available as <code>gs</code>; for Windows there is a version called <code>gswin32c</code>. GhostScript accepts a rich selection of command-line options that modify its behavior. Many of these are set indirectly by the options available above. However, hard-core usage may require some users to add additional options to fine-tune the result. Use <code>-S</code> to examine the actual command used, and add custom options via one or more instances of the <code>-C</code> option. For instance, to turn on image interpolation for all images, improving image quality for scaled images at the expense of speed, use <code>-C</code>-dDOINTERPOLATE. See <a rel="nofollow" href="http://www.ghostscript.com">www.ghostscript.com</a> for complete documentation.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gs/">gs</a></i>(1) </p>
<h2>Index</h2>
