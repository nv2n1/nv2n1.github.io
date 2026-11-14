---
title: "nearneighbor(1)"
name: "nearneighbor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nearneighbor/"
description: "nearneighbor – \"Grid table data using a \"\"Nearest neighbor\"\" algorithm\""
---

<h2>NAME</h2>
<p> nearneighbor &#8211; &quot;Grid table data using a &quot;&quot;Nearest neighbor&quot;&quot; algorithm&quot;</p>
<h2>SYNOPSIS</h2>
<p> <code>nearneighbor</code> [ <i>table</i> ] <i>out_grdfile</i> <i>increment</i> <i>sectors</i>[/<i>min_sectors</i>] <i>region</i> [ <i>search_radius</i>[<i>unit</i>] [ <i>empty</i> ] [ [<i>level</i>] ] [ ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>nearneighbor</code> reads arbitrarily located (x,y,z[,w]) triples [quadruplets] from standard input [or <i>table</i>] and uses a nearest neighbor algorithm to assign an average value to each node that have one or more points within a radius centered on the node. The average value is computed as a weighted mean of the nearest point from each sector inside the search radius. The weighting function used is w(r) = 1 / (1 + d ^ 2), where d = 3 * r / search_radius and r is distance from the node. This weight is modulated by the weights of the observation points [if supplied].</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>out_grdfile</i></p>
<dd> Give the name of the output grid file.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-N</code><i>sectors</i>[/<i>min_sectors</i>]</p>
<dd> The circular area centered on each node is divided into <i>sectors</i> sectors. Average values will only be computed if there is at least one value inside each of at least <i>min_sectors</i> of the sectors for a given node. Nodes that fail this test are assigned the value NaN (but see <code>-E</code>). If <i>min_sectors</i> is omitted it is set to be at least 50% of <i>sectors</i> (i.e., rounded up to next integer). [Default is a quadrant search with 100% coverage, i.e., <i>sectors</i> = <i>min_sectors</i> = 4]. Note that only the nearest value per sector enters into the averaging; the more distant points are ignored.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-S</code><i>search_radius</i>[<i>unit</i>]</p>
<dd> Sets the <i>search_radius</i> that determines which data points are considered close to a node. Append the distance unit (see UNITS).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> 3 [or 4, see <code>-W</code>] column ASCII file(s) [or binary, see <code>-bi</code>] holding (x,y,z[,w]) data values. If no file is specified, <code>nearneighbor</code> will read from standard input.</p>
<dt><code>-E</code><i>empty</i></p>
<dd> Set the value assigned to empty nodes [NaN].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code></p>
<dd> Input data have a 4th column containing observation point weights. These are multiplied with the geometrical weight factor to determine the actual weights used in the calculations.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 (or 4 if <code>-W</code> is set) columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+t</code><i>threshold</i>]</p>
<dd> Append <code>+b</code><i>BC</i> to set any boundary conditions to be used, adding <code>g</code> for geographic, <code>p</code> for periodic, or <code>n</code> for natural boundary conditions. For the latter two you may append <code>x</code> or <code>y</code> to specify just one direction, otherwise both are assumed. [Default is geographic if grid is geographic].</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>EXAMPLES</h2>
<p> To create a gridded data set from the file seaMARCII_bathy.lon_lat_z using a 0.5 min grid, a 5 km search radius, using an octant search with 100% sector coverage, and set empty nodes to -9999: </p>
<pre>
gmt nearneighbor seaMARCII_bathy.lon_lat_z -R242/244/-22/-20 -I0.5m \
                 -E-9999 -Gbathymetry.nc -S5k -N8/8
</pre>
<p> To make a global grid file from the data in geoid.xyz using a 1 degree grid, a 200 km search radius, spherical distances, using an quadrant search, and set nodes to NaN only when fewer than two quadrants contain at least one value: </p>
<pre>
gmt nearneighbor geoid.xyz -R0/360/-90/90 -I1 -Lg -Ggeoid.nc -S200k -N4
</pre>
<h2>SEE ALSO</h2>
<p> <code>blockmean</code>, <code>blockmedian</code>, <code>blockmode</code>, <code>gmt</code>, <code>greenspline</code>, <code>sphtriangulate</code>, <code>surface</code>, <code>triangulate</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
