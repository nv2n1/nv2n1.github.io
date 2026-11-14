---
title: "project(1)"
name: "project"
section: "1"
letter: "p"
url: "/docs/linux/man/1-project/"
description: "project – Project table data onto lines or great circles, generate tracks, or translate coordinates"
---

<h2>NAME</h2>
<p> project &#8211; Project table data onto lines or great circles, generate tracks, or translate coordinates</p>
<h2>SYNOPSIS</h2>
<p> <code>project</code> [ <i>table</i> ] <i>cx</i>/<i>cy</i> [ <i>azimuth</i> ] [ <i>bx</i>/<i>by</i> ] [ <i>flags</i> ] [ <i>dist</i>[/<i>colat</i>][<code>+</code>] ] [ [<code>w</code>][<i>l_min</i>/<i>l_max</i>] ] [ ] [ ] [ ] [ <i>px</i>/<i>py</i> ] [ [<i>level</i>] ] [ <i>w_min</i>/<i>w_max</i> ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>project</code> reads arbitrary (<i>x</i>, <i>y</i>[,<i>z</i>]) data from standard input [or <i>table</i> ] and writes to standard output any combination of (<i>x</i>, <i>y</i>, <i>z</i>, <i>p</i>, <i>q</i>, <i>r</i>, <i>s</i>), where (<i>p</i>, <i>q</i>) are the coordinates in the projection, (<i>r</i>, <i>s</i>) is the position in the (<i>x</i>, <i>y</i>) coordinate system of the point on the profile (<i>q</i> = 0 path) closest to (<i>x</i>, <i>y</i>), and <i>z</i> is all remaining columns in the input (beyond the required <i>x</i> and <i>y</i> columns). </p>
<p> Alternatively, <code>project</code> may be used to generate (<i>r</i>, <i>s</i>, <i>p</i>) triples at equal increments <i>dist</i> along a profile. In this case ( <code>-G</code> option), no input is read. </p>
<p> Projections are defined in any (but only) one of three ways: </p>
<p> (Definition 1) By a Center <code>-C</code> and an Azimuth <code>-A</code> in degrees clockwise from North. </p>
<p> (Definition 2) By a Center <code>-C</code> and end point E of the projection path <code>-E</code>. </p>
<p> (Definition 3) By a Center <code>-C</code> and a roTation pole position <code>-T</code>. </p>
<p> To spherically project data along a great circle path, an oblique coordinate system is created which has its equator along that path, and the zero meridian through the Center. Then the oblique longitude (<i>p</i>) corresponds to the distance from the Center along the great circle, and the oblique latitude (<i>q</i>) corresponds to the distance perpendicular to the great circle path. When moving in the increasing (<i>p</i>) direction, (toward <i>B</i> or in the <i>azimuth</i> direction), the positive (<i>q</i>) direction is to your left. If a Pole has been specified, then the positive (<i>q</i>) direction is toward the pole. </p>
<p> To specify an oblique projection, use the <code>-T</code> option to set the Pole. Then the equator of the projection is already determined and the <code>-C</code> option is used to locate the <i>p</i> = 0 meridian. The Center <i>cx/cy</i> will be taken as a point through which the <i>p</i> = 0 meridian passes. If you do not care to choose a particular point, use the South pole (<i>ox</i> = 0, <i>oy</i> = -90). </p>
<p> Data can be selectively windowed by using the <code>-L</code> and <code>-W</code> options. If <code>-W</code> is used, the projection Width is set to use only points with <i>w_min</i> &lt; q &lt; <i>w_max</i>. If <code>-L</code> is set, then the Length is set to use only those points with <i>l_min</i> &lt; p &lt; <i>l_max</i>. If the <code>-E</code> option has been used to define the projection, then <code>-Lw</code> may be selected to window the length of the projection to exactly the span from <code>O</code> to <code>B</code>. </p>
<p> Flat Earth (Cartesian) coordinate transformations can also be made. Set <code>-N</code> and remember that <i>azimuth</i> is clockwise from North (the <i>y</i> axis), NOT the usual cartesian theta, which is counterclockwise from the <i>x</i> axis. <i>azimuth</i> = 90 &#8211; theta. </p>
<p> No assumptions are made regarding the units for <i>x</i>, <i>y</i>, <i>r</i>, <i>s</i>, <i>p</i>, <i>q</i>, <i>dist</i>, <i>l_min</i>, <i>l_max</i>, <i>w_min</i>, <i>w_max</i>. If <code>-Q</code> is selected, map units are assumed and <i>x</i>, <i>y</i>, <i>r</i>, <i>s</i> must be in degrees and <i>p</i>, <i>q</i>, <i>dist</i>, <i>l_min</i>, <i>l_max</i>, <i>w_min</i>, <i>w_max</i> will be in km. </p>
<p> Calculations of specific great-circle and geodesic distances or for back-azimuths or azimuths are better done using <code>mapproject</code>. </p>
<p> <code>project</code> is CASE SENSITIVE. Use UPPER CASE for all one-letter designators which begin optional arguments. Use lower case for the xyzpqrs letters in <code>-flags</code>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>cx</i>/<i>cy</i></p>
<dd> <i>cx/cy</i> sets the origin of the projection, in Definition 1 or 2. If Definition 3 is used (<code>-T</code>), then <i>cx/cy</i> are the coordinates of a point through which the oblique zero meridian (<i>p</i> = 0) should pass. The <i>cx/cy</i> is not required to be 90 degrees from the pole.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><i>azimuth</i></p>
<dd> <i>azimuth</i> defines the azimuth of the projection (Definition 1).</p>
<dt><code>-E</code><i>bx</i>/<i>by</i></p>
<dd> <i>bx/by</i> defines the end point of the projection path (Definition 2).</p>
<dt><code>-F</code><i>flags</i></p>
<dd> Specify your desired output using any combination of <i>xyzpqrs</i>, in any order. Do not space between the letters. Use lower case. The output will be ASCII (or binary, see <code>-bo</code>) columns of values corresponding to <i>xyzpqrs</i> [Default]. If both input and output are using ASCII format then the <i>z</i> data are treated as textstring(s). If the <code>-G</code> option is selected, the output will be <i>rsp</i>.</p>
<dt><code>-G</code><i>dist</i>[/<i>colat</i>]</p>
<dd> Generate mode. No input is read. Create (<i>r</i>, <i>s</i>, <i>p</i>) output points every <i>dist</i> units of <i>p</i>. See <code>-Q</code> option. Alternatively, append <code>/</code><i>colat</i> for a small circle instead [Default is a colatitude of 90, i.e., a great circle]. Use <code>-C</code> and <code>-E</code> to generate a circle that goes through the center and end point. Note, in this case the center and end point cannot be farther apart than 2*|<i>colat</i>|. Finally, if you append <code>+</code> the we will report the position of the pole as part of the segment header [no header].</p>
<dt><code>-L</code>[<code>w</code>][<i>l_min</i>/<i>l_max</i>]</p>
<dd> Length controls. Project only those points whose <i>p</i> coordinate is within <i>l_min</i> &lt; <i>p</i> &lt; <i>l_max</i>. If <code>-E</code> has been set, then you may use <code>-Lw</code> to stay within the distance from <code>C</code> to <code>E</code>.</p>
<dt><code>-N</code></p>
<dd> Flat Earth. Make a Cartesian coordinate transformation in the plane. [Default uses spherical trigonometry.]</p>
<dt><code>-Q</code></p>
<dd> Map type units, i.e., project assumes <i>x</i>, <i>y</i>, <i>r</i>, <i>s</i> are in degrees while <i>p</i>, <i>q</i>, <i>dist</i>, <i>l_min</i>, <i>l_max</i>, <i>w_min</i>, <i>w_max</i> are in km. If <code>-Q</code> is not set, then all these are assumed to be in the same units.</p>
<dt><code>-S</code></p>
<dd> Sort the output into increasing <i>p</i> order. Useful when projecting random data into a sequential profile.</p>
<dt><code>-T</code><i>px</i>/<i>py</i></p>
<dd> <i>px/py</i> sets the position of the rotation pole of the projection. (Definition 3).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>w_min</i>/<i>w_max</i></p>
<dd> Width controls. Project only those points whose <i>q</i> coordinate is within <i>w_min</i> &lt; <i>q</i> &lt; <i>w_max</i>.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is given by <code>-F</code> or <code>-G</code>].</p>
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
<dt><code>-s</code>[<i>cols</i>][<code>a</code>|<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Set handling of NaN records.</p>
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
<h2>EXAMPLES</h2>
<p> To generate points every 10km along a great circle from 10N,50W to 30N,10W: </p>
<pre>
gmt project -C-50/10 -E-10/30 -G10 -Q &gt; great_circle_points.xyp
</pre>
<p> (Note that great_circle_points.xyp could now be used as input for <code>grdtrack</code>, etc. ). </p>
<p> To generate points every 10km along a small circle of colatitude 60 from 10N,50W to 30N,10W: </p>
<pre>
gmt project -C-50/10 -E-10/30 -G10/60 -Q &gt; small_circle_points.xyp
</pre>
<p> To create a partial small circle of colatitude 80 about a pole at 40E,85N, with extent of 45 degrees to either side of the meridian defined by the great circle from the pole to a point 15E,15N, try </p>
<pre>
gmt project -C15/15 -T40/85 -G1/80 -L-45/45 &gt; some_circle.xyp
</pre>
<p> To project the shiptrack gravity, magnetics, and bathymetry in c2610.xygmb along a great circle through an origin at 30S, 30W, the great circle having an azimuth of N20W at the origin, keeping only the data from NE of the profile and within +/- 500 km of the origin, run: </p>
<pre>
gmt project c2610.xygmb -C-30/-30 -A-20 -W-10000/0 -L-500/500 -Fpz -Q &gt; c2610_projected.pgmb
</pre>
<p> (Note in this example that <code>-W</code>-10000/0 is used to admit any value with a large negative <i>q</i> coordinate. This will take those points which are on our right as we walk along the great circle path, or to the NE in this example.) </p>
<p> To make a Cartesian coordinate transformation of mydata.xy so that the new origin is at 5,3 and the new <i>x</i> axis (<i>p</i>) makes an angle of 20 degrees with the old <i>x</i> axis, use: </p>
<pre>
gmt project mydata.xy -C5/3 -A70 -Fpq &gt; mydata.pq
</pre>
<p> To take data in the file pacific.lonlat and transform it into oblique coordinates using a pole from the hotspot reference frame and placing the oblique zero meridian (<i>p</i> = 0 line) through Tahiti, run: </p>
<pre>
gmt project pacific.lonlat -T-75/68 -C-149:26/-17:37 -Fpq &gt; pacific.pq
</pre>
<p> Suppose that pacific_topo.nc is a grid file of bathymetry, and you want to make a file of flowlines in the hotspot reference frame. If you run: </p>
<pre>
gmt grd2xyz pacific_topo.nc | project -T-75/68 -C0/-90 -Fxyq | xyz2grd -Retc -Ietc -Cflow.nc
</pre>
<p> then flow.nc is a file in the same area as pacific_topo.nc, but flow contains the latitudes about the pole of the projection. You now can use grdcontour on flow.nc to draw lines of constant oblique latitude, which are flow lines in the hotspot frame. </p>
<p> If you have an arbitrarily rotation pole <i>px/py</i> and you would like to draw an oblique small circle on a map, you will first need to make a file with the oblique coordinates for the small circle (i.e., lon = 0-360, lat is constant), then create a file with two records: the north pole (0/90) and the origin (0/0), and find what their oblique coordinates are using your rotation pole. Now, use the projected North pole and origin coordinates as the rotation pole and center, respectively, and project your file as in the pacific example above. This gives coordinates for an oblique small circle.</p>
<h2>SEE ALSO</h2>
<p> <code>fitcircle</code>, <code>gmt</code>, <code>gmtvector</code>, <code>mapproject</code>, <code>grdproject</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
