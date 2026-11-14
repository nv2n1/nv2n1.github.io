---
title: "grdmask(1)"
name: "grdmask"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdmask/"
description: "grdmask – Create mask grid from polygons or point coverage"
---

<h2>NAME</h2>
<p> grdmask &#8211; Create mask grid from polygons or point coverage</p>
<h2>SYNOPSIS</h2>
<p> <code>grdmask</code> <i>pathfiles</i> <i>mask_grd_file</i>] <i>increment</i> <i>region</i> [ [<code>m</code>|<code>p</code>|<code>x</code>|<code>y</code>] ] [ [<code>z</code>|<code>Z</code>|<code>p</code>|<code>P</code>]<i>values</i> ] [ <i>search_radius</i>[<i>unit</i>] ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-x</code>[[-]<i>n</i>] ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdmask</code> can operate in two different modes. 1. It reads one or more <i>pathfiles</i> that each define a closed polygon. The nodes defined by the specified region and lattice spacing will be set equal to one of three possible values depending on whether the node is outside, on the polygon perimeter, or inside the polygon. The resulting mask may be used in subsequent operations involving <code>grdmath</code> to mask out data from polygonal areas. 2. The <i>pathfiles</i> simply represent data point locations and the mask is set to the inside or outside value depending on whether a node is within a maximum distance from the nearest data point. If the distance specified is zero then only the nodes nearest each data point are considered &quot;inside&quot;.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>pathfiles</i></p>
<dd> The name of 1 or more ASCII [or binary, see <code>-bi</code>] files holding the polygon(s) or data points.</p>
<dt><code>-G</code><i>mask_grd_file</i>]</p>
<dd> Name of resulting output mask grid file. (See GRID FILE FORMATS below).</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>m</code>|<code>p</code>|<code>x</code>|<code>y</code>]</p>
<dd> If the input data are geographic (as indicated by <code>-f</code>) then the sides in the polygons will be approximated by great circle arcs. When using the <code>-A</code> sides will be regarded as straight lines. Alternatively, append <code>m</code> to have sides first follow meridians, then parallels. Or append <code>p</code> to first follow parallels, then meridians. For Cartesian data, points are simply connected, unless you append <code>x</code> or <code>y</code> to construct stair-case paths whose first move is along <i>x</i> or <i>y</i>, respectively.</p>
<dt><code>-N</code>[<code>z</code>|<code>Z</code>|<code>p</code>|<code>P</code>]<i>values</i></p>
<dd> Sets the <i>out/edge/in</i> that will be assigned to nodes that are <i>out</i>side the polygons, on the <i>edge</i>, or <i>in</i>side. Values can be any number, including the textstring NaN [Default is 0/0/1]. Optionally, use <code>Nz</code> to set polygon insides to the z-value obtained from the data (either segment header <code>-Z</code><i>zval</i>, <code>-L</code><i>header</i> or via <code>-a</code>Z=<i>name</i>); use <code>-NZ</code> to consider the polygon boundary as part of the inside. Alternatively, use <code>-Np</code> to use a running number as polygon ID; optionally append start of the sequence [0]. Here, <code>-NP</code> includes the polygon perimeter as inside. Note: <code>-N</code><code>z</code>|<code>Z</code>|<code>p</code>|<code>P</code> cannot be used in conjunction with <code>-S</code>; they also all optionally accept /<i>out</i> [0].</p>
<dt><code>-S</code><i>search_radius</i>[<i>unit</i>]</p>
<dd> Set nodes to inside, on edge, or outside depending on their distance to the nearest data point. Nodes within <i>radius</i> [0] from the nearest data point are considered inside; append a distance unit (see UNITS). If <i>radius</i> is given as <code>z</code> then we instead read individual radii from the 3rd input column. If <code>-S</code> is not set then we consider the input data to define closed polygon(s) instead.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
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
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When writing a netCDF file, the grid is stored by default with the variable name &quot;z&quot;. To specify another variable name <i>varname</i>, append <code>?</code><i>varname</i> to the file name. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>EXAMPLES</h2>
<p> To set all nodes inside and on the polygons coastline_*.xy to 0, and outside points to 1, do </p>
<pre>
gmt grdmask coastline_*.xy -R-60/-40/-40/-30 -I5m -N1/0/0 -Gland_mask.nc=nb -V
</pre>
<p> To set nodes within 50 km of data points to 1 and other nodes to NaN, do </p>
<pre>
gmt grdmask data.xyz -R-60/-40/-40/-30 -I5m -NNaN/1/1 -S50k -Gdata_mask.nc=nb -V
</pre>
<p> To assign polygon IDs to the gridnodes using the insides of the polygons in plates.gmt, based on the attribute POL_ID, do </p>
<pre>
gmt grdmask plates.gmt -R-40/40/-40/40 -I2m -Nz -Gplate_IDs.nc -aZ=POL_ID -V
</pre>
<p> Same exercise, but instead compute running polygon IDs starting at 100, do </p>
<pre>
gmt grdmask plates.gmt -R-40/40/-40/40 -I2m -Np100 -Gplate_IDs.nc -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdlandmask</code>, <code>grdmath</code>, <code>grdclip</code>, <code>psmask</code>, <code>psclip</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
