---
title: "grdview(1)"
name: "grdview"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdview/"
description: "grdview – Create 3-D perspective image or surface mesh from a grid"
---

<h2>NAME</h2>
<p> grdview &#8211; Create 3-D perspective image or surface mesh from a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdview</code> <i>relief_file</i> <i>parameters</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<i>cpt</i>]] [ <i>drapefile</i> | <i>grd_r</i>,<i>grd_g</i>,<i>grd_b</i> ] [ <i>intensfile</i>|<i>intensity</i> ] [ <code>-Jz</code>|<code>Z</code><i>parameters</i> ] [ <code>-K</code> ] [ <i>level</i>[<code>+g</code><i>fill</i>] ] [ <code>-O</code> ] [ <code>-P</code> ] [ <i>args</i>[<code>+m</code>] ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ <i>smooth</i> ] [ [<code>s</code>][<code>o</code>[<i>pen</i>]] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ <code>type</code><i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdview</code> reads a 2-D grid file and produces a 3-D perspective plot by drawing a mesh, painting a colored/grayshaded surface made up of polygons, or by scanline conversion of these polygons to a raster image. Options include draping a data set on top of a surface, plotting of contours on top of the surface, and apply artificial illumination based on intensities provided in a separate grid file.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>relief_file</i></p>
<dd> 2-D gridded data set to be imaged (the relief of the surface). (See GRID FILE FORMAT below.)</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code>[<i>cpt</i>]</p>
<dd> name of the CPT file. Must be present if you want (1) mesh plot with contours (<code>-Qm</code>), or (2) shaded/colored perspective image (<code>-Qs</code> or <code>-Qi</code>). For <code>-Qs</code>: You can specify that you want to skip a z-slice by setting red = -; to use a pattern give red = <code>P|p</code><i>dpi/pattern</i>[:<code>F</code><i>color</i>[<code>B</code><i>color</i>]]. Alternatively, supply the name of a GMT color master CPT [rainbow] and let <code>grdview</code> automatically determine a 16-level continuous CPT from the grid&#8217;s z-range.</p>
<dt><code>-G</code><i>drapefile</i> | <code>-G</code><i>grd_r</i>,<i>grd_g</i>,<i>grd_b</i></p>
<dd> Drape the image in <i>drapefile</i> on top of the relief provided by <i>relief_file</i>. [Default is <i>relief_file</i>]. Note that <code>-Jz</code> and <code>-N</code> always refers to the <i>relief_file</i>. The <i>drapefile</i> only provides the information pertaining to colors, which is looked-up via the CPT file (see <code>-C</code>). Alternatively, give three grid files separated by commas. These files must contain the red, green, and blue colors directly (in 0-255 range) and no CPT file is needed. The <i>drapefile</i> may be of higher resolution than the <i>relief_file</i>.</p>
<dt><code>-I</code><i>intensfile</i>|<i>intensity</i></p>
<dd> Gives the name of a grid file with intensities in the (-1,+1) range, or a constant intensity to apply everywhere. [Default is no illumination].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-N</code><i>level</i>[<code>+g</code><i>fill</i>]</p>
<dd> Draws a plane at this z-level. If the optional <i>color</i> is provided via the <code>+g</code> modifier, the frontal facade between the plane and the data perimeter is colored. See <code>-Wf</code> for setting the pen used for the outline.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code><i>args</i>[<code>+m</code>]</p>
<dd> Select one of following settings. For any of these choices, you may force a monochrome image by appending the modifier <code>+m</code>. Colors are then converted to shades of gray using the (monochrome television) YIQ transformation</p>
<dt>1.</p>
<dd> Specify <code>m</code> for mesh plot [Default], and optionally append <i>color</i> for a different mesh paint [white].</p>
<dt>2.</p>
<dd> Specify <code>mx</code> or <code>my</code> for waterfall plots (row or column profiles). Specify color as for plain <code>m</code></p>
<dt>3.</p>
<dd> Specify <code>s</code> for surface plot, and optionally append <code>m</code> to have mesh lines drawn on top of surface.</p>
<dt>4.</p>
<dd> Specify <code>i</code> for image plot, and optionally append the effective dpi resolution for the rasterization [100].</p>
<dt>5.</p>
<dd> Specify <code>c</code>. Same as <code>-Qi</code> but will make nodes with z = NaN transparent, using the colormasking feature in PostScript Level 3 (the PS device must support PS Level 3). .</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i> This option may be used to indicate the range used for the 3-D axes [Default is region given by the <i>relief_file</i>]. You may ask for a larger <i>w/e/s/n</i> region to have more room between the image and the axes. A smaller region than specified in the <i>relief_file</i> will result in a subset of the grid.</p>
<dt><code>-S</code><i>smooth</i></p>
<dd> Smooth the contours before plotting (see <code>grdcontour</code>) [Default is no smoothing].</p>
<dt><code>-T</code>[<code>s</code>][<code>o</code>[<i>pen</i>]]</p>
<dd> Plot image without any interpolation. This involves converting each node-centered bin into a polygon which is then painted separately. Append <code>s</code> to skip nodes with z = NaN. This option is useful for categorical data where interpolating between values is meaningless. Optionally, append <code>o</code> to draw the tile outlines, and specify a custom pen if the default pen is not to your liking. As this option produces a flat surface it cannot be combined with <code>-JZ</code> or <code>-Jz</code>.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-W</code><code>type</code><i>pen</i></p>
<dt><code>-Wc</code></p>
<dd> Draw contour lines on top of surface or mesh (not image). Append pen attributes used for the contours. [Default: width = 0.75p, color = black, style = solid].</p>
<dt><code>-Wm</code></p>
<dd> Sets the pen attributes used for the mesh. [Default: width = 0.25p, color = black, style = solid]. You must also select <code>-Qm</code> or <code>-Qsm</code> for meshlines to be drawn.</p>
<dt><code>-Wf</code></p>
<dd> Sets the pen attributes used for the facade. [Default: width = 0.25p, color = black, style = solid]. You must also select <code>-N</code> for the facade outline to be drawn. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
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
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Except for Cartesian cases, we need to resample your geographic grid onto an equidistant projected grid. In doing so various algorithms come into play that projects data from one lattice to another while avoiding anti-aliasing, leading to possible distortions. One expected effect of resampling with splines is the tendency for the new resampled grid to slightly exceed the global min/max limits of the original grid. If this is coupled with tight CPT file limits you may find that some map areas may show up with fore- or background color due to the resampling. In that case you have two options: (1) Modify your CPT file to fit the resampled extrema (reported with <code>-V</code>) or (2) Impose clipping of resampled values so they do not exceed the input min/max values (add <code>+c</code> to your <code>-n</code> option).</p>
<h2>EXAMPLES</h2>
<p> To make a mesh plot from the file hawaii_grav.nc and drawing the contours given in the CPT file hawaii.cpt on a Lambert map at 1.5 cm/degree along the standard parallels 18 and 24, with vertical scale 20 mgal/cm, and looking at the surface from SW at 30 degree elevation, run </p>
<pre>
gmt grdview hawaii_grav.nc -Jl18/24/1.5c -Chawaii.cpt \
            -Jz0.05c -Qm -N-100 -p225/30 -Wc &gt; hawaii_grav_image.ps
</pre>
<p> To create a illuminated color perspective plot of the gridded data set image.nc, using the CPT file color.rgb, with linear scaling at 10 cm/x-unit and tickmarks every 5 units, with intensities provided by the file intens.nc, and looking from the SE, use </p>
<pre>
gmt grdview image.nc -Jx10.0c -Ccolor.rgb -Qs -p135/30 -Iintens.nc &gt; image3D.ps
</pre>
<p> To make the same plot using the rastering option with dpi = 50, use </p>
<pre>
gmt grdview image.nc -Jx10.0c -Ccolor.rgb -Qi50 -p135/30 -Iintens.nc &gt; image3D.ps
</pre>
<p> To create a color PostScript perspective plot of the gridded data set magnetics.nc, using the CPT file mag_intens.cpt, draped over the relief given by the file topography.nc, with Mercator map width of 6 inch and tickmarks every 1 degree, with intensities provided by the file topo_intens.nc, and looking from the SE, run </p>
<pre>
gmt grdview topography.nc -JM6i -Gmagnetics.nc -Cmag_intens.cpt \
            -Qs -p140/30 -Itopo_intens.nc &gt; draped3D.ps
</pre>
<p> Given topo.nc and the Landsat image veggies.ras, first run <code>grd2rgb</code> to get the red, green, and blue grids, and then drape this image over the topography and shade the result for good measure. The commands are </p>
<pre>
gmt grd2rgb veggies.ras -Glayer_%c.nc
gmt grdview topo.nc -JM6i -Qi -p140/30 -Itopo_intens.nc \
           -Glayer_r.nc,layer_g.nc,layer_b.nc &gt; image.ps
</pre>
<h2>REMARKS</h2>
<p> For the <code>-Qs</code> option: PostScript provides no way of smoothly varying colors within a polygon, so colors can only vary from polygon to polygon. To obtain smooth images this way you may resample the grid file(s) using <code>grdsample</code> or use a finer grid size when running gridding programs like <code>surface</code> or <code>nearneighbor</code>. Unfortunately, this produces huge PostScript files. The alternative is to use the <code>-Qi</code> option, which computes bilinear or bicubic continuous color variations within polygons by using scanline conversion to image the polygons.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2rgb</code>, <code>gmtcolors</code>, <code>grdcontour</code>, <code>grdimage</code>, <code>nearneighbor</code>, <code>psbasemap</code>, <code>pscontour</code>, <code>pstext</code>, <code>surface</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
