---
title: "triangulate(1)"
name: "triangulate"
section: "1"
letter: "t"
url: "/docs/linux/man/1-triangulate/"
description: "triangulate – Do optimal (Delaunay) triangulation and gridding of Cartesian table data [method]"
---

<h2>NAME</h2>
<p> triangulate &#8211; Do optimal (Delaunay) triangulation and gridding of Cartesian table data [method]</p>
<h2>SYNOPSIS</h2>
<p> <code>triangulate</code> [ <i>table</i> ] [ <code>x</code>|<code>y</code> ] [ <i>empty</i> ] [ <i>grdfile</i> ] [ <i>increment</i> ] [ <i>parameters</i> ] [ ] [ ] [ ] [ <i>region</i> ] [ ] [ [<i>level</i>] ] [ ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>triangulate</code> reads one or more ASCII [or binary] files (or standard input) containing x,y[,z] and performs Delaunay triangulation, i.e., it find how the points should be connected to give the most equilateral triangulation possible. If a map projection (give <code>-R</code> and <code>-J</code>) is chosen then it is applied before the triangulation is calculated. By default, the output is triplets of point id numbers that make up each triangle and is written to standard output. The id numbers refer to the points position (line number, starting at 0 for the first line) in the input file. As an option, you may choose to create a multiple segment file that can be piped through <code>psxy</code> to draw the triangulation network. If <code>-G</code> <code>-I</code> are set a grid will be calculated based on the surface defined by the planar triangles. The actual algorithm used in the triangulations is either that of Watson [1982] [Default] or Shewchuk [1996] (if installed; type <code>triangulate &#8211;</code> to see which method is selected). This choice is made during the GMT installation.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-Dx</code>|<code>y</code></p>
<dd> Take either the <i>x</i>&#8211; or <i>y</i>-derivatives of surface represented by the planar facets (only used when <code>-G</code> is set).</p>
<dt><code>-E</code><i>empty</i></p>
<dd> Set the value assigned to empty nodes when <code>-G</code> is set [NaN].</p>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Use triangulation to grid the data onto an even grid (specified with <code>-R</code> <code>-I</code>). Append the name of the output grid file. The interpolation is performed in the original coordinates, so if your triangles are close to the poles you are better off projecting all data to a local coordinate system before using <code>triangulate</code> (this is true of all gridding routines).</p>
<dt><code>-I</code></p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] sets the grid size for optional grid output (see <code>-G</code>). Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-M</code></p>
<dd> Output triangulation network as multiple line segments separated by a segment header record.</p>
<dt><code>-N</code></p>
<dd> Used in conjunction with <code>-G</code> to also write the triplets of the ids of all the Delaunay vertices [Default only writes the grid].</p>
<dt><code>-Q</code></p>
<dd> Output the edges of the Voronoi cells instead [Default is Delaunay triangle edges]. Requires <code>-R</code> and is only available if linked with the Shewchuk [1996] library. Note that <code>-Z</code> is ignored on output.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-S</code></p>
<dd> Output triangles as polygon segments separated by a segment header record. Requires Delaunay triangulation.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code></p>
<dd> Controls whether we read (x,y) or (x,y,z) data and if z should be output when <code>-M</code> or <code>-S</code> are used [Read (x,y) only].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input]. Node ids are stored as double triplets.</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline]. (Only valid with <code>-G</code>).</p>
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
<p> To triangulate the points in the file samples.xyz, store the triangle information in a binary file, and make a grid for the given area and spacing, use </p>
<pre>
gmt triangulate samples.xyz -bo -R0/30/0/30 -I2 -Gsurf.nc &gt; samples.ijk
</pre>
<p> To draw the optimal Delaunay triangulation network based on the same file using a 15-cm-wide Mercator map, use </p>
<pre>
gmt triangulate samples.xyz -M -R-100/-90/30/34 -JM15c | gmt psxy \
    -R-100/-90/30/34 -JM15c -W0.5p -B1 &gt; network.ps
</pre>
<p> To instead plot the Voronoi cell outlines, try </p>
<pre>
gmt triangulate samples.xyz -M -Q -R-100/-90/30/34 -JM15c | \
    gmt psxy -R-100/-90/30/34 -JM15c -W0.5p -B1 &gt; cells.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>greenspline</code>, <code>nearneighbor</code>, <code>pscontour</code>, <code>sphinterpolate</code>, <code>sphtriangulate</code>, <code>surface</code></p>
<h2>REFERENCES</h2>
<p> Watson, D. F., 1982, Acord: Automatic contouring of raw data, <i>Comp. &amp; Geosci.</i>, <code>8</code>, 97-101. </p>
<p> Shewchuk, J. R., 1996, Triangle: Engineering a 2D Quality Mesh Generator and Delaunay Triangulator, First Workshop on Applied Computational Geometry (Philadelphia, PA), 124-133, ACM, May 1996. </p>
<p> <i>Shewchuk&#8217;s Homepage</i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
