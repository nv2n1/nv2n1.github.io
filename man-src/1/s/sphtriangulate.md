---
title: "sphtriangulate(1)"
name: "sphtriangulate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sphtriangulate/"
description: "sphtriangulate – Delaunay or Voronoi construction of spherical lon,lat data"
---

<h2>NAME</h2>
<p> sphtriangulate &#8211; Delaunay or Voronoi construction of spherical lon,lat data</p>
<h2>SYNOPSIS</h2>
<p> <code>sphtriangulate</code> [ <i>table</i> ] [ ] [ ] [ ] [ <i>unit</i> ] [ <i>nfile</i> ] [ <code>d</code>|<code>v</code> ] [ ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>sphtriangulate</code> reads one or more ASCII [or binary] files (or standard input) containing lon, lat and performs a spherical Delaunay triangulation, i.e., it find how the points should be connected to give the most equilateral triangulation possible on the sphere. Optionally, you may choose <code>-Qv</code> which will do further processing to obtain the Voronoi polygons. Normally, either set of polygons will be written as fillable segment output; use <code>-T</code> to write unique arcs instead. As an option, compute the area of each triangle or polygon. The algorithm used is STRIPACK.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code></p>
<dd> Compute the area of the spherical triangles (<code>-Qd</code>) or polygons (<code>-Qv</code>) and write the areas (in chosen units; see <code>-L</code>) in the output segment headers [no areas calculated].</p>
<dt><code>-C</code></p>
<dd> For large data set you can save some memory (at the expense of more processing) by only storing one form of location coordinates (geographic or Cartesian 3-D vectors) at any given time, translating from one form to the other when necessary [Default keeps both arrays in memory].</p>
<dt><code>-D</code></p>
<dd> Used to skip the last (repeated) input vertex at the end of a closed segment if it equals the first point in the segment. [Default uses all points].</p>
<dt><code>-L</code><i>unit</i></p>
<dd> Specify the unit used for distance and area calculations. Choose among <code>e</code> (m), <code>f</code> (foot), <code>k</code> (km), <code>m</code> (mile), <code>n</code> (nautical mile), <code>u</code> (survey foot), or <code>d</code> (spherical degree). A spherical approximation is used unless <i>PROJ_ELLIPSOID</i> is set to an actual ellipsoid, in which case we convert latitudes to authalic latitudes before calculating areas. When degree is selected the areas are given in steradians.</p>
<dt><code>-N</code><i>nfile</i></p>
<dd> Write the information pertaining to each polygon. For Delaunay: the three node number and the triangle area (if <code>-A</code> was set); for Voronoi the unique node lon, lat and polygon area (if <code>-A</code> was set)) to a separate file. This information is also encoded in the segment headers of ASCII output files. Required if binary output is needed.</p>
<dt><code>-Q</code><code>d</code>|<code>v</code></p>
<dd> Append <code>d</code> for Delaunay triangles or <code>v</code> for Voronoi polygons [Delaunay]. If <code>-bo</code> is used then <code>-N</code> may be used to specify a separate file where the polygon information normally is written.</p>
<dt><code>-T</code></p>
<dd> Write the unique arcs of the construction [Default writes fillable triangles or polygons]. When used with <code>-A</code> we store arc length in the segment header in chosen unit (see <code>-L</code>).</p>
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
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> To triangulate the points in the file testdata.txt, and make a Voronoi diagram via <code>psxy</code>, use </p>
<pre>
gmt sphtriangulate testdata.txt -Qv | psxy -Rg -JG30/30/6i -L -P -W1p -B0g30 | gv -
</pre>
<p> To compute the optimal Delaunay triangulation network based on the multiple segment file globalnodes.d and save the area of each triangle in the header record, try </p>
<pre>
gmt sphtriangulate globalnodes.d -Qd -A &gt; global_tri.d
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>triangulate</code>, <code>sphdistance</code></p>
<h2>REFERENCES</h2>
<p> Renka, R, J., 1997, Algorithm 772: STRIPACK: Delaunay Triangulation and Voronoi Diagram on the Surface of a Sphere, <i>AMC Trans. Math. Software</i>, <code><a href="/docs/linux/man/3-23/">23</a></code>(3), 416-434.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
