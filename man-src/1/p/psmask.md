---
title: "psmask(1)"
name: "psmask"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psmask/"
description: "psmask – Use data tables to clip or mask map areas with no coverage"
---

<h2>NAME</h2>
<p> psmask &#8211; Use data tables to clip or mask map areas with no coverage</p>
<h2>SYNOPSIS</h2>
<p> <code>psmask</code> [ <i>table</i> ] <i>increment</i> <i>parameters</i> <i>region</i> [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>dumpfile</i> ] [ [<code>l</code>|<code>r</code>] ] [ <i>fill</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ [<code>+</code>|<code>&#8211;</code>]<i>nodegrid</i> ] [ ] [ ] [ ] [ <i>cut</i> ] [ <i>search_radius</i>[<i>unit</i>] ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>psmask</code> <code>-C</code> [ <code>-K</code> ] [ <code>-O</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psmask</code> reads a (<i>x</i>,<i>y</i>,<i>z</i>) file [or standard input] and uses this information to find out which grid cells are reliable. Only grid cells which have one or more data points are considered reliable. As an option, you may specify a radius of influence. Then, all grid cells that are within <i>radius</i> of a data point are considered reliable. Furthermore, an option is provided to reverse the sense of the test. Having found the reliable/not reliable points, <code>psmask</code> will either paint tiles to mask these nodes (with the <code>-T</code> switch), or use contouring to create polygons that will clip out regions of no interest. When clipping is initiated, it will stay in effect until turned off by a second call to <code>psmask</code> using the <code>-C</code> option.</p>
<h2>REQUIRED</h2>
<dl>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code></p>
<dd> Mark end of existing clip path. No input file is needed. Implicitly sets <code>-O</code>. Also supply <code>-X</code> and <code>-Y</code> settings if you have moved since the clip started.</p>
<dt><code>-D</code><i>dumpfile</i></p>
<dd> Dump the (x,y) coordinates of each clipping polygon to one or more output files (or <i>stdout</i> if <i>template</i> is not given). No plotting will take place. If <i>template</i> contains the C-format specifier %d (including modifications like %05d) then polygons will be written to different files; otherwise all polygons are written to the specified file (<i>template</i>). The files are ASCII unless <code>-bo</code> is used. See <code>-Q</code> to exclude small polygons from consideration.</p>
<dt><code>-F</code>[<code>l</code>|<code>r</code>]</p>
<dd> Force clip contours (polygons) to be oriented so that data points are to the left (<code>-Fl</code> [Default]) or right (<code>-Fr</code>) as we move along the perimeter [Default is arbitrary orientation]. Requires <code>-D</code>.</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Paint the clip polygons (or tiles) with a selected fill [Default is no fill].</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<code>+</code>|<code>&#8211;</code>]<i>nodegrid</i></p>
<dd> Save the internal grid with ones (data constraint) and zeros (no data) to the named <i>nodegrid</i> [no grid saved]. Use <code>L+</code> to convert the no data flags to NaNs before writing the grid, while <code>L-</code> will instead convert the data flags to NaNs.</p>
<dt><code>-N</code></p>
<dd> Invert the sense of the test, i.e., clip regions where there is data coverage.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Q</code></p>
<dd> Do not dump polygons with less than <i>cut</i> number of points [Dumps all polygons]. Only applicable if <code>-D</code> has been specified.</p>
<dt><code>-S</code><i>search_radius</i>[<i>unit</i>]</p>
<dd> Sets radius of influence. Grid nodes within <i>radius</i> of a data point are considered reliable. [Default is 0, which means that only grid cells with data in them are reliable]. Append the distance unit (see UNITS).</p>
<dt><code>-T</code></p>
<dd> Plot tiles instead of clip polygons. Use <code>-G</code> to set tile color or pattern. Cannot be used with <code>-D</code>.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<h2>EXAMPLES</h2>
<p> To make an overlay PostScript file that will mask out the regions of a contour map where there is no control data using clip polygons, use: </p>
<pre>
gmt psmask africa_grav.xyg -R20/40/20/40 -I5m -JM10i -O -K &gt; mask.ps
</pre>
<p> We do it again, but this time we wish to save the clipping polygons to file all_pols.txt: </p>
<pre>
gmt psmask africa_grav.xyg -R20/40/20/40 -I5m -Dall_pols.txt
</pre>
<p> A repeat of the first example but this time we use white tiling: </p>
<pre>
gmt psmask africa_grav.xyg -R20/40/20/40 -I5m -JM10i -T -O -K -Gwhite &gt; mask.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtcolors</code>, <code>grdmask</code>, <code>surface</code>, <code>psbasemap</code>, <code>psclip</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
