---
title: "grdcut(1)"
name: "grdcut"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdcut/"
description: "grdcut – Extract subregion from a grid"
---

<h2>NAME</h2>
<p> grdcut &#8211; Extract subregion from a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdcut</code> <i>ingrid</i> <i>outgrid</i> <i>region</i> [ [<i>nodata</i>] ] [ [<code>n</code>]<i>lon/lat/radius</i>[<i>unit</i>] ] [ [<i>level</i>] ] [ [<code>n</code>|<code>r</code>]<i>min/max</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdcut</code> will produce a new <i>outgrid</i> file which is a subregion of <i>ingrid</i>. The subregion is specified with <code>-R</code> as in other programs; the specified range must not exceed the range of <i>ingrid</i> (but see <code>-N</code>). If in doubt, run <code>grdinfo</code> to check range. Alternatively, define the subregion indirectly via a range check on the node values or via distances from a given point. Complementary to <code>grdcut</code> there is <code>grdpaste</code>, which will join together two grid files along a common edge.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrid</i></p>
<dd> This is the input grid file.</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> This is the output grid file.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-N</code>[<i>nodata</i>]</p>
<dd> Allow grid to be extended if new <code>-R</code> exceeds existing boundaries. Append <i>nodata</i> value to initialize nodes outside current region [Default is NaN].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. This defines the subregion to be cut out.</p>
<dt><code>-S</code>[<code>n</code>]<i>lon/lat/radius</i>[<i>unit</i>]</p>
<dd> Specify an origin and radius; append a distance unit (see UNITS) and we determine the corresponding rectangular region so that all grid nodes on or inside the circle are contained in the subset. If <code>-Sn</code> is used we set all nodes outside the circle to NaN.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code>[<code>n</code>|<code>r</code>]<i>min/max</i></p>
<dd> Determine the new rectangular region so that all nodes <i>outside</i> this region are also outside the given <i>z</i>-range [-inf/+inf]. To indicate no limit on min or max, specify a hyphen (-). Normally, any NaNs encountered are simply skipped and not considered in the decision. Use <code>-Zn</code> to consider a NaN to be outside the <i>z</i>-range. This means the new subset will be NaN-free. Alternatively, use <code>-Zr</code> to consider NaNs to be within the data range. In this case we stop shrinking the boundaries once a NaN is found [Default simply skips NaNs when making the range decision].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>EXAMPLES</h2>
<p> Suppose you have used <code>surface</code> to grid ship gravity in the region between 148E &#8211; 162E and 8N &#8211; 32N, and you do not trust the gridding near the edges, so you want to keep only the area between 150E &#8211; 160E and 10N &#8211; 30N, then: </p>
<pre>
gmt grdcut grav_148_162_8_32.nc -Ggrav_150_160_10_30.nc -R150/160/10/30 -V
</pre>
<p> To return the subregion of a grid such that any boundary strips where all values are entirely above 0 are excluded, try </p>
<pre>
gmt grdcut bathy.nc -Gtrimmed_bathy.nc -Z-/0 -V
</pre>
<p> To return the subregion of a grid that contains all nodes within a distance of 500 km from the point 45,30 try </p>
<pre>
gmt grdcut bathy.nc -Gsubset_bathy.nc -S45/30/500k -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdclip</code>, <code>grdpaste</code>, <code>grdinfo</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
