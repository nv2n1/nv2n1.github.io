---
title: "grdimage(1)"
name: "grdimage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdimage/"
description: "grdimage – Project grids or images and plot them on maps"
---

<h2>NAME</h2>
<p> grdimage &#8211; Project grids or images and plot them on maps</p>
<h2>SYNOPSIS</h2>
<p> <code>grdimage</code> <i>grd_z</i> | <i>grd_r grd_g grd_b</i> [ <i>out_img</i><code>=</code><i>driver</i> ] [ <i>cpt</i> ] [ [<code>r</code>] ] [ <code>i</code>[|<i>dpi</i>] ] <i>parameters</i> [ [<code>f</code>|<code>b</code>]<i>color</i> ] [ <i>intensfile</i>|<i>intensity</i> ] [ <code>z</code>|<code>-Z</code><i>parameters</i> ] [ ] [ ] [ ] [ ] [ ] [ ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-tr</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdimage</code> reads one 2-D grid file and produces a gray-shaded (or colored) map by plotting rectangles centered on each grid node and assigning them a gray-shade (or color) based on the z-value. Alternatively, <code>grdimage</code> reads three 2-D grid files with the red, green, and blue components directly (all must be in the 0-255 range). Optionally, illumination may be added by providing a file with intensities in the (-1,+1) range. Values outside this range will be clipped. Such intensity files can be created from the grid using <code>grdgradient</code> and, optionally, modified by <code>grdmath</code> or <code>grdhisteq</code>. Yet as a third alternative available when GMT is build with GDAL support the grd_z file can be an image referenced or not (than see <code>-Dr</code>). In this case the images can be illuminated with the file provided via the <code>-I</code> option. Here if image has no coordinates those of the intensity file will be used. </p>
<p> When using map projections, the grid is first resampled on a new rectangular grid with the same dimensions. Higher resolution images can be obtained by using the <code>-E</code> option. To obtain the resampled value (and hence shade or color) of each map pixel, its location is inversely projected back onto the input grid after which a value is interpolated between the surrounding input grid values. By default bi-cubic interpolation is used. Aliasing is avoided by also forward projecting the input grid nodes. If two or more nodes are projected onto the same pixel, their average will dominate in the calculation of the pixel value. Interpolation and aliasing is controlled with the <code>-n</code> option. </p>
<p> The <code>-R</code> option can be used to select a map region larger or smaller than that implied by the extent of the grid. </p>
<p> A (color) PostScript file is output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grd_z</i> | <i>grd_r grd_g grd_b</i></p>
<dd> 2-D gridded data set (or red, green, blue grids) to be imaged (See GRID FILE FORMATS below.)</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>out_img</i><code>=</code><i>driver</i></p>
<dd> With GDAL aware versions: save image in a raster format instead of PostScript. Append <i>out_img</i><code>=</code><i>driver</i> to select the file name and image format. The <i>driver</i> is the driver code name used by GDAL. For example, <code>-A</code>img.tif=GTiff will write a GeoTiff image if the subset of GMT syntax projections that is currently possible to translate into the PROJ4 syntax allows it, or a plain tiff file otherwise. Note: any vector elements are lost.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Name of the CPT file (for <i>grd_z</i> only). Alternatively, supply the name of a GMT color master CPT [rainbow] and let <code>grdimage</code> automatically determine a 16-level continuous CPT from the grid&#8217;s z-range. Yet another option is to specify -Ccolor1,color2[,color3,&#8230;] to build a linear continuous CPT from those colors automatically. In this case <i>color</i><code>n</code> can be a r/g/b triplet, a color name, or an HTML hexadecimal color (e.g. #aabbcc ).</p>
<dt><code>-D</code>[<code>r</code>]</p>
<dd> Specifies that the grid supplied is an image file to be read via GDAL. Obviously this option will work only with GMT versions built with GDAL support. The image can be indexed or true color (RGB) and can be an URL of a remotely located file. That is <code>-D</code> <i><a rel="nofollow" href="http://www.somewhere.com/image.jpg">http://www.somewhere.com/image.jpg</a></i> is a valid file syntax. Note, however, that to use it this way you must not be blocked by a proxy. If you are, chances are good that it can work by setting the environmental variable <i>http_proxy</i> with the value &#8216;your_proxy:port&#8217; Append <code>r</code> to use the region specified by <code>-R</code> to apply to the image. For example, if you have used <code>-Rd</code> then the image will be assigned the limits of a global domain. The interest of this mode is that you can project a raw image (an image without referencing coordinates).</p>
<dt><code>-Ei</code>[|<i>dpi</i>]</p>
<dd> Sets the resolution of the projected grid that will be created if a map projection other than Linear or Mercator was selected [100]. By default, the projected grid will be of the same size (rows and columns) as the input file. Specify <code>i</code> to use the PostScript image operator to interpolate the image at the device resolution.</p>
<dt><code>-G</code>[<code>f</code>|<code>b</code>]<i>color</i></p>
<dd> This option only applies when the resulting image otherwise would consist of only two colors: black (0) and white (255). If so, this option will instead use the image as a transparent mask and paint the mask (or its inverse, with <code>-Gb</code>) with the given color combination.</p>
<dt><code>-I</code><i>intensfile</i>|<i>intensity</i></p>
<dd> Gives the name of a grid file with intensities in the (-1,+1) range, or a constant intensity to apply everywhere. [Default is no illumination].</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-M</code></p>
<dd> Force conversion to monochrome image using the (television) YIQ transformation. Cannot be used with <code>-Q</code>.</p>
<dt><code>-N</code></p>
<dd> Do not clip the image at the map boundary (only relevant for non-rectangular maps).</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Make grid nodes with z = NaN transparent, using the colormasking feature in PostScript Level 3 (the PS device must support PS Level 3).</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i> You may ask for a larger <i>w/e/s/n</i> region to have more room between the image and the axes. A smaller region than specified in the grid file will result in a subset of the grid [Default is the region given by the grid file].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>IMAGING GRIDS WITH NANS</h2>
<p> Be aware that if your input grid contains patches of NaNs, these patches can become larger as a consequence of the resampling that must take place with most map projections. Because <code>grdimage</code> uses the PostScript colorimage operator, for most non-linear projections we must resample your grid onto an equidistant rectangular lattice. If you find that the NaN areas are not treated adequately, consider (a) use a linear projection, or (b) use <code>grdview</code> <code>-Ts</code> instead.</p>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Except for Cartesian cases, we need to resample your geographic grid onto an equidistant projected grid. In doing so various algorithms come into play that projects data from one lattice to another while avoiding anti-aliasing, leading to possible distortions. One expected effect of resampling with splines is the tendency for the new resampled grid to slightly exceed the global min/max limits of the original grid. If this is coupled with tight CPT file limits you may find that some map areas may show up with fore- or background color due to the resampling. In that case you have two options: (1) Modify your CPT file to fit the resampled extrema (reported with <code>-V</code>) or (2) Impose clipping of resampled values so they do not exceed the input min/max values (add <code>+c</code> to your <code>-n</code> option).</p>
<h2>EXAMPLES</h2>
<p> For a quick-and-dirty color map of the data in the file stuff.nc, with the maximum map dimension limited to be 6 inches, try </p>
<pre>
gmt grdimage stuff.nc -JX6i+ &gt; quick.ps
</pre>
<p> To gray-shade the file hawaii_grav.nc with shades given in shades.cpt on a Lambert map at 1.5 cm/degree along the standard parallels 18 and 24, and using 1 degree tickmarks: </p>
<pre>
gmt grdimage hawaii_grav.nc -Jl18/24/1.5c -Cshades.cpt -B1 &gt; hawaii_grav_image.ps
</pre>
<p> To create an illuminated color PostScript plot of the gridded data set image.nc, using the intensities provided by the file intens.nc, and color levels in the file colors.cpt, with linear scaling at 10 inch/x-unit, tickmarks every 5 units: </p>
<pre>
gmt grdimage image.nc -Jx10i -Ccolors.cpt -Iintens.nc -B5 &gt; image.ps
</pre>
<p> To create an false color PostScript plot from the three grid files red.nc, green.nc, and blue.nc, with linear scaling at 10 inch/x-unit, tickmarks every 5 units: </p>
<pre>
gmt grdimage red.nc green.nc blue.nc -Jx10i -B5 &gt; rgbimage.ps
</pre>
<p> When GDAL support is built in: To create a sinusoidal projection of a remotely located Jessica Rabbit </p>
<pre>
gmt grdimage -JI15c -Rd -Dr
    <a rel="nofollow" href="http://larryfire.files.wordpress.com/2009/07/untooned_jessicarabbit.jpg">http://larryfire.files.wordpress.com/2009/07/untooned_jessicarabbit.jpg</a> \
    -P &gt; jess.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>grd2rgb</code>, <code>grdcontour</code>, <code>grdview</code>, <code>grdgradient</code>, <code>grdhisteq</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
