---
title: "gmtspatial(1)"
name: "gmtspatial"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtspatial/"
description: "gmtspatial – Do geospatial operations on lines and polygons"
---

<h2>NAME</h2>
<p> gmtspatial &#8211; Do geospatial operations on lines and polygons</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtspatial</code> [ <i>table</i> ] [ [<code>a</code><i>min_dist</i>][<i>unit</i>]] [ ] [ [<code>+f</code><i>file</i>][<code>+a</code><i>amax</i>][<code>+d</code><i>dmax</i>][<code>+c|C</code><i>cmax</i>][<code>+s</code><i>fact</i>] ] [ <code>+</code>|<code>&#8211;</code> ] [ [<code>l</code>] ] [ <code>-I</code>[<code>e</code>|<code>i</code>] ] [ <i>pfile</i>[<code>+a</code>][<code>+p</code><i>start</i>][<code>+r</code>][<code>+z</code>] ] [ [[<code>&#8211;</code>|<code>+</code>]*unit*][<code>+h</code>][<code>+l</code>][<code>+p</code>] ] [ <i>region</i> ] [ <code>i</code>|<code>u</code>|<code>s</code>|<code>j</code> ] [ [<i>clippolygon</i>] ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtspatial</code> reads one or more data files (which may be multisegment files) that contains closed polygons and operates of these polygons in the specified way. Operations include area calculation, handedness reversals, and polygon intersections.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code>[<code>a</code><i>min_dist</i>][<i>unit</i>]</p>
<dd> Perform spatial nearest neighbor (NN) analysis: Determine the nearest neighbor of each point and report the NN distances and the point IDs involved in each pair (IDs are the input record numbers starting at 0). Use <code>-Aa</code> to decimate a data set so that no NN distance is lower than the threshold <i>min_dist</i>. In this case we write out the (possibly averaged) coordinates and the updated NN distances and point IDs. A negative point number means the original point was replaced by a weighted average (the absolute ID value gives the ID of the first original point ID to be included in the average.)</p>
<dt><code>-C</code></p>
<dd> Clips polygons to the map region, including map boundary to the polygon as needed. The result is a closed polygon (see <code>-T</code> for truncation instead). Requires <code>-R</code>.</p>
<dt><code>-D</code>[<code>+f</code><i>file</i>][<code>+a</code><i>amax</i>][<code>+d</code><i>dmax</i>][<code>+c|C</code><i>cmax</i>][<code>+s</code><i>fact</i>]</p>
<dd> Check for duplicates among the input lines or polygons, or, if <i>file</i> is given via <code>+f</code>, check if the input features already exist among the features in <i>file</i>. We consider the cases of exact (same number and coordinates) and approximate matches (average distance between nearest points of two features is less than a threshold). We also consider that some features may have been reversed. Features are considered approximate matches if their minimum distance is less than <i>dmax</i> [0] (see UNITS) and their closeness (defined as the ratio between the average distance between the features divided by their average length) is less than <i>cmax</i> [0.01]. For each duplicate found, the output record begins with the single letter Y (exact match) or ~ (approximate match). If the two matching segments differ in length by more than a factor of 2 then we consider the duplicate to be either a subset (-) or a superset (+). Finally, we also note if two lines are the result of splitting a continuous line across the Dateline (|). For polygons we also consider the fractional difference in areas; duplicates must differ by less than <i>amax</i> [0.01]. By default, we compute the mean line separation. Use <code>+C</code><i>cmin</i> to instead compute the median line separation and therefore a robust closeness value. Also by default we consider all distances between points on one line and another. Append <code>+p</code> to limit the comparison to points that project perpendicularly to points on the other line (and not its extension).</p>
<dt><code>-E</code><code>+</code>|<code>&#8211;</code> ]</p>
<dd> Reset the handedness of all polygons to match the given <code>+</code> (counter-clockwise) or <code>&#8211;</code> (clockwise). Implies <code>-Q+</code>.</p>
<dt><code>-F</code>[<code>l</code>]</p>
<dd> Force input data to become polygons on output, i.e., close them explicitly if not already closed. Optionally, append <code>l</code> to force line geometry.</p>
<dt><code>-I</code>[<code>e</code>|<code>i</code>]</p>
<dd> Determine the intersection locations between all pairs of polygons. Append <code>i</code> to only compute internal (i.e., self-intersecting polygons) crossovers or <code>e</code> to only compute external (i.e., between paris of polygons) crossovers [Default is both].</p>
<dt><code>-N</code><i>pfile</i>[<code>+a</code>][<code>+p</code><i>start</i>][<code>+r</code>][<code>+z</code>]</p>
<dd> Determine if one (or all, with <code>+a</code>) points of each feature in the input data are inside any of the polygons given in the <i>pfile</i>. If inside, then report which polygon it is; the polygon ID is either taken from the aspatial value assigned to Z, the segment header (first <code>-Z</code>, then <code>-L</code> are scanned), or it is assigned the running number that is initialized to <i>start</i> [0]. By default the input segment that are found to be inside a polygon are written to stdout with the polygon ID encoded in the segment header as <code>-Z</code><i>ID</i>. Alternatively, append <code>+r</code> to just report which polygon contains a feature or <code>+z</code> to have the IDs added as an extra data column on output. Segments that fail to be inside a polygon are not written out. If more than one polygon contains the same segment we skip the second (and further) scenario.</p>
<dt><code>-Q</code>[[<code>&#8211;</code>|<code>+</code>]*unit*][<code>+h</code>][<code>+l</code>][<code>+p</code>]</p>
<dd> Measure the area of all polygons or length of line segments. Use <code>-Q+h</code> to append the area to each polygons segment header [Default simply writes the area to stdout]. For polygons we also compute the centroid location while for line data we compute the mid-point (half-length) position. Append a distance unit to select the unit used (see UNITS). Note that the area will depend on the current setting of <i>PROJ_ELLIPSOID</i>; this should be a recent ellipsoid to get accurate results. The centroid is computed using the mean of the 3-D Cartesian vectors making up the polygon vertices, while the area is obtained via an equal-area projection. For line lengths you may prepend <code>&#8211;</code>|<code>+</code> to the unit and the calculation will use Flat Earth or Geodesic algorithms, respectively [Default is great circle distances]. By default, we consider open polygons as lines. Append <code>+p</code> to close open polygons and thus consider all input as polygons, or append <code>+l</code> to consider all input as lines, even if closed.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. Clips polygons to the map region, including map boundary to the polygon as needed. The result is a closed polygon.</p>
<dt><code>-S</code><code>i</code>|<code>j</code>|<code>s</code>|<code>u</code></p>
<dd> Spatial processing of polygons. Choose from <code>-Si</code> which returns the intersection of polygons (closed), <code>-Su</code> which returns the union of polygons (closed), <code>-Ss</code> which will split polygons that straddle the Dateline, and <code>-Sj</code> which will join polygons that were split by the Dateline. Note: Only <code>-Ss</code> has been implemented.</p>
<dt><code>-T</code>[<i>clippolygon</i>]</p>
<dd> Truncate polygons against the specified polygon given, possibly resulting in open polygons. If no argument is given to <code>-T</code> we create a clipping polygon from <code>-R</code> which then is required. Note that when the <code>-R</code> clipping is in effect we will also look for polygons of length 4 or 5 that exactly match the <code>-R</code> clipping polygon.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLE</h2>
<p> To turn all lines in the multisegment file lines.txt into closed polygons, run </p>
<pre>
gmt spatial lines.txt -F &gt; polygons.txt
</pre>
<p> To compute the area of all geographic polygons in the multisegment file polygons.txt, run </p>
<pre>
gmt spatial polygons.txt -Q &gt; areas.txt
</pre>
<p> Same data, but now orient all polygons to go counter-clockwise and write their areas to the segment headers, run </p>
<pre>
gmt spatial polygons.txt -Q+h -E+ &gt; areas.txt
</pre>
<p> To determine the intersections between the polygons A.txt and B.txt, run </p>
<pre>
gmt spatial A.txt B.txt -Ce &gt; crossovers.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtconvert</code>, <code>gmtselect</code>, <code>gmtsimplify</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
