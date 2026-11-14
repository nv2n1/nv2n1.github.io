---
title: "grdproject(1)"
name: "grdproject"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdproject/"
description: "grdproject – Forward and inverse map transformation of grids"
---

<h2>NAME</h2>
<p> grdproject &#8211; Forward and inverse map transformation of grids</p>
<h2>SYNOPSIS</h2>
<p> <code>grdproject</code> <i>in_grdfile</i> <i>out_grdfile</i> <i>parameters</i> [ [<i>dx/dy</i>] ] [ <i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]] ] [ <i>dpi</i> ] [ [<code>c|i|p|e|f|k|M|n|u</code>] ] [ ] [ <code>c</code>|<code>i</code>|<code>p</code> ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdproject</code> will do one of two things depending whether <code>-I</code> has been set. If set, it will transform a gridded data set from a rectangular coordinate system onto a geographical system by resampling the surface at the new nodes. If not set, it will project a geographical gridded data set onto a rectangular grid. To obtain the value at each new node, its location is inversely projected back onto the input grid after which a value is interpolated between the surrounding input grid values. By default bi-cubic interpolation is used. Aliasing is avoided by also forward projecting the input grid nodes. If two or more nodes are projected onto the same new node, their average will dominate in the calculation of the new node value. Interpolation and aliasing is controlled with the <code>-n</code> option. The new node spacing may be determined in one of several ways by specifying the grid spacing, number of nodes, or resolution. Nodes not constrained by input data are set to NaN. </p>
<p> The <code>-R</code> option can be used to select a map region larger or smaller than that implied by the extent of the grid file.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>in_grdfile</i></p>
<dd> 2-D binary grid file to be transformed. (See GRID FILE FORMATS below.)</p>
<dt><code>-G</code><i>out_grdfile</i></p>
<dd> Specify the name of the output grid file. (See GRID FILE FORMATS below.)</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code>[<i>dx/dy</i>]</p>
<dd> Let projected coordinates be relative to projection center [Default is relative to lower left corner]. Optionally, add offsets in the projected units to be added (or subtracted when <code>-I</code> is set) to (from) the projected coordinates, such as false eastings and northings for particular projection zones [0/0].</p>
<dt><code>-D</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> Set the grid spacing for the new grid. Append <code>m</code> for arc minute, <code>s</code> for arc second. If neither <code>-D</code> nor <code>-E</code> are set then we select the same number of output nodes as there are input nodes.</p>
<dt><code>-E</code><i>dpi</i></p>
<dd> Set the resolution for the new grid in dots per inch.</p>
<dt><code>-F</code>[<code>c|i|p|e|f|k|M|n|u</code>]</p>
<dd> Force 1:1 scaling, i.e., output (or input, see <code>-I</code>) data are in actual projected meters [<code>e</code>]. To specify other units, append <code>f</code> (foot), <code>k</code> (km), <code>M</code> (statute mile), <code>n</code> (nautical mile), <code>u</code> (US survey foot), <code>i</code> (inch), <code>c</code> (cm), or <code>p</code> (point). Without <code>-F</code>, the output (or input, see <code>-I</code>) are in the units specified by <i>PROJ_LENGTH_UNIT</i> (but see <code>-M</code>).</p>
<dt><code>-I</code></p>
<dd> Do the Inverse transformation, from rectangular to geographical.</p>
<dt><code>-Mc</code>|<code>i</code>|<code>p</code></p>
<dd> Append <code>c</code>, <code>i</code>, or <code>p</code> to indicate that cm, inch, or point should be the projected measure unit [Default is set by <i>PROJ_LENGTH_UNIT</i> in <code>gmt.conf</code>]. Cannot be used with <code>-F</code>.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. You may ask to project only a subset of the grid by specifying a smaller input <i>w/e/s/n</i> region [Default is the region given by the grid file].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
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
<h2>EXAMPLES</h2>
<p> To transform the geographical grid dbdb5.nc onto a pixel Mercator grid at 300 dpi, run </p>
<pre>
gmt grdproject dbdb5.nc -R20/50/12/25 -Jm0.25i -E300 -r -Gdbdb5_merc.nc
</pre>
<p> To inversely transform the file topo_tm.nc back onto a geographical grid, use </p>
<pre>
gmt grdproject topo_tm.nc -R-80/-70/20/40 -Jt-75/1:500000 -I -D5m -V -Gtopo.nc
</pre>
<p> This assumes, of course, that the coordinates in topo_tm.nc were created with the same projection parameters. </p>
<p> To inversely transform the file topo_utm.nc (which is in UTM meters) back to a geographical grid we specify a one-to-one mapping with meter as the measure unit: </p>
<pre>
gmt grdproject topo_utm.nc -R203/205/60/65 -Ju5/1:1 -I -Mm -Gtopo.nc -V
</pre>
<p> To inversely transform the file data.nc (which is in Mercator meters with Greenwich as the central longitude and a false easting of -4 and produced on the ellipse WGS-72) back to a geographical grid we specify a one-to-one mapping with meter as the measure unit: </p>
<pre>
gmt grdproject data.nc -Jm/1:1 -I -F -C-4/0 -Gdata_geo.nc -V --PROJ_ELLIPSOID=WGS-72
</pre>
<h2>RESTRICTIONS</h2>
<p> The boundaries of a projected (rectangular) data set will not necessarily give rectangular geographical boundaries (Mercator is one exception). In those cases some nodes may be unconstrained (set to NaN). To get a full grid back, your input grid may have to cover a larger area than you are interested in.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>mapproject</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
