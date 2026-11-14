---
title: "sphdistance(1)"
name: "sphdistance"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphdistance/"
description: "sphdistance – Make Voronoi distance, node, or nearest-neighbor grid on a sphere"
---

<h2>NAME</h2>
<p> sphdistance &#8211; Make Voronoi distance, node, or nearest-neighbor grid on a sphere</p>
<h2>SYNOPSIS</h2>
<p> <code>sphdistance</code> [ <i>table</i> ] <i>grdfile</i> [ ] [ <code>d</code>|<code>n</code>|<code>z</code>[<i>dist</i>] ] [ <i>increment</i> ] [ <i>unit</i> ] [ <i>nodetable</i> ] [ <i>voronoi.txt</i> ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>sphdistance</code> reads one or more ASCII [or binary] files (or standard input) containing lon, lat and performs the construction of Voronoi polygons. These polygons are then processed to calculate the nearest distance to each node of the lattice and written to the specified grid. The Voronoi algorithm used is STRIPACK. As an option, you may provide pre-calculated Voronoi polygon file in the format written by <code>sphtriangulate</code>, thus bypassing the memory- and time-consuming triangularization.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Name of the output grid to hold the computed distances.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-C</code></p>
<dd> For large data sets you can save some memory (at the expense of more processing) by only storing one form of location coordinates (geographic or Cartesian 3-D vectors) at any given time, translating from one form to the other when necessary [Default keeps both arrays in memory]. Not applicable with <code>-Q</code>.</p>
<dt><code>-Ed</code>|<code>n</code>|<code>z</code>[<i>dist</i>]</p>
<dd> Specify the quantity that should be assigned to the grid nodes. By default we compute distances to the nearest data point [<code>-Ed</code>]. Use <code>-En</code> to assign the ID numbers of the Voronoi polygons that each grid node is inside, or use <code>-Ez</code> for a nearest-neighbor grid where we assign all nodes inside the polygon the z-value of the center node. Optionally, append the resampling interval along Voronoi arcs in spherical degrees [1].</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-L</code><i>unit</i></p>
<dd> Specify the unit used for distance calculations. Choose among <code>d</code> (spherical degree), <code>e</code> (m), <code>f</code> (feet), <code>k</code> (km), <code>M</code> (mile), <code>n</code> (nautical mile) or <code>u</code> survey foot. A spherical approximation is used unless <i>PROJ_ELLIPSOID</i> is set to an actual ellipsoid.</p>
<dt><code>-N</code><i>nodetable</i></p>
<dd> Read the information pertaining to each Voronoi polygon (the unique node lon, lat and polygon area) from a separate file [Default acquires this information from the ASCII segment headers of the output file]. Required if binary input via <code>-Q</code> is used.</p>
<dt><code>-Q</code><i>voronoi.txt</i></p>
<dd> Append the name of a file with pre-calculated Voronoi polygons [Default performs the Voronoi construction on input data]. For binary data <code>-bi</code> you must specify the node information separately (via <code>-N</code>).</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>EXAMPLES</h2>
<p> To construct Voronoi polygons from the points in the file testdata.txt and then calculate distances from the data to a global 1&#215;1 degree grid, use </p>
<pre>
gmt sphdistance testdata.txt -Rg -I1 -Gglobedist.nc
</pre>
<p> To generate the same grid in two steps using <code>sphtriangulate</code> separately, try </p>
<pre>
gmt sphtriangulate testdata.txt -Qv &gt; voronoi.txt
gmt sphdistance -Qvoronoi.txt -Rg -I1 -Gglobedist.nc
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>sphtriangulate</code>, <code>triangulate</code></p>
<h2>REFERENCES</h2>
<p> Renka, R, J., 1997, Algorithm 772: STRIPACK: Delaunay Triangulation and Voronoi Diagram on the Surface of a Sphere, <i>AMC Trans. Math. Software</i>, <code><a href="/docs/linux/man/3-23/">23</a></code>(3), 416-434.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
