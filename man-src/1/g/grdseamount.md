---
title: "grdseamount(1)"
name: "grdseamount"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdseamount/"
description: "grdseamount – Compute synthetic seamount (Gaussian or cone, circular or elliptical) bathymetry"
---

<h2>NAME</h2>
<p> grdseamount &#8211; Compute synthetic seamount (Gaussian or cone, circular or elliptical) bathymetry</p>
<h2>SYNOPSIS</h2>
<p> <code>grdseamount</code> [ <i>intable</i> ] <i>increment</i> <i>region</i> [ [<i>out</i>/<i>in</i>] ] [ <code>c</code>|<code>d</code>|<code>g</code>|<code>p</code> ] [ [<i>unit</i>] ] [ ] [ [<i>flattening</i>] ] [ <i>grdfile</i> ] [ [<i>cut</i>] ] [ <i>list</i> ] [ <i>norm</i> ] [ <i>bmode</i>/<i>qmode</i> ] [ <i>scale</i> ] [ <i>t0</i>[<code>u</code>][/<i>t1</i>[<code>u</code>]/<i>dt</i>[<code>u</code>]|<i>n</i>][<code>+l</code>] ] [ <i>level</i> ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-fg</code> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdseamount</code> will compute the combined shape of multiple synthetic seamounts given their individual shape parameters. We read a list with seamount locations and sizes and can evaluate either Gaussian, parabolic, conical, or disc shapes, which may be circular or elliptical, and optionally truncated. Various scaling options are available to modify the result, including an option to add in a background depth (more complicated backgrounds may be added via <code>grdmath</code>). The input must contain <i>lon</i>, <i>lat</i>, <i>radius</i>, <i>height</i> for each seamount. For elliptical features (<code>-E</code>) we expect <i>lon</i>, <i>lat</i>, <i>azimuth</i>, <i>semi-major</i>, <i>semi-minor</i>, <i>height</i> instead. If flattening is specified (<code>-F</code>) with no value appended then a final column with flattening is expected (cannot be used for plateaus). For temporal evolution of topography the <code>-T</code> option may be used, in which case the data file must have two final columns with the start and stop time of seamount construction. In this case you may choose to write out a cumulative shape or just the increments produced by each time step (see <code>-Q</code>).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<i>out/in</i>]</p>
<dd> Build a mask grid, append outside/inside values [1/NaN]. Here, height is ignored and <code>-L</code>, <code>-N</code> and <code>-Z</code> are disallowed</p>
<dt><code>-C</code></p>
<dd> Select shape function: choose among <code>c</code> (cone), <code>d</code> (disc), <code>g</code> (Gaussian) and <code>p</code> (parabolic) shape [Default is Gaussian].</p>
<dt><code>-D</code><i>unit</i></p>
<dd> Append the unit used for horizontal distances in the input file (see UNITS). Does not apply for geographic data (<code>-fg</code>) which we convert to km.</p>
<dt><code>-E</code></p>
<dd> Elliptical data format [Default is Circular]. Read lon, lat, azimuth, major, minor, height (m) for each seamount.</p>
<dt><code>-F</code>[<i>flattening</i>]</p>
<dd> Seamounts are to be truncated to guyots. Append <i>flattening</i>, otherwise we expect to find it in last input column [no truncation]. Ignored if used with <code>-Cd</code>.</p>
<dt><code>-G</code><i>grdfile</i></p>
<dd> Specify the name of the output grid file; see GRID FILE FORMATS below). If <code>-T</code> is set then <i>grdfile</i> must be a filename template that contains a floating point format (C syntax). If the filename template also contains either %s (for unit name) or %c (for unit letter) then we use the corresponding time (in units specified in <code>-T</code>) to generate the individual file names, otherwise we use time in years with no unit.</p>
<dt><code>-L</code>[<i>cut</i>]</p>
<dd> List area, volume, and mean height for each seamount; NO grid is created. Optionally, append the noise-floor cutoff level below which we ignore area and volume [0].</p>
<dt><code>-M</code><i>list</i></p>
<dd> Write the names of all grids that were created to the text file <i>list</i>. Requires <code>-T</code>.</p>
<dt><code>-N</code><i>norm</i></p>
<dd> Normalize grid so maximum grid height equals <i>norm</i>.</p>
<dt><code>-Q</code><i>bmode</i>/<i>qmode</i></p>
<dd> Only to be used in conjunction with <code>-T</code>. Append two different modes settings: The <i>bmode</i> determines how we construct the surface. Specify <code>c</code> for cumulative volume through time, or <code>i</code> for incremental volume added for each time slice. The <i>qmode</i> determines the volume flux curve. Give <code>g</code> for a Gaussian volume flux history or <code>l</code> for a linear volume flux history between the start and stop times of each feature.</p>
<dt><code>-S</code><i>scale</i></p>
<dd> Sets optional scale factor for radii [1].</p>
<dt><code>-T</code><i>t0</i>[<code>u</code>][/<i>t1</i>[<code>u</code>]/<i>dt</i>[<code>u</code>]|<i>n</i>][<code>+l</code>]</p>
<dd> Specify <i>t0</i>, <i>t1</i>, and time increment (<i>dt</i>) for sequence of calculations [Default is one step, with no time dependency]. For a single specific time, just give start time <i>t0</i>. The unit is years; append <code>k</code> for kyr and <code>M</code> for Myr. For a logarithmic time scale, append <code>+l</code> and specify <i>n</i> steps instead of <i>dt</i>. Alternatively, give a file with the desired times in the first column (these times may have individual units appended, otherwise we assume year). Note that the grid for <i>t0</i> (if a range is given) is not written as it is zero and marks the start of the building history.</p>
<dt><code>-Z</code><i>level</i></p>
<dd> Set the background depth [0].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 4 input columns].</p>
<dt><code>-fg</code></p>
<dd> Geographic grids (dimensions of longitude, latitude) will be converted to km via a &quot;Flat Earth&quot; approximation using the current ellipsoid parameters.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
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
<h2>EXAMPLES</h2>
<p> To compute the incremental loads from two elliptical, truncated Gaussian seamounts being constructed from 3 Ma to 2 Ma and 2.8 M to 1.9 Ma using a linear volumetric production rate, and output an incremental grid every 0.1 Myr from 3 Ma to 1.9 Ma, we can try: </p>
<pre>
cat &lt;&lt; EOF &gt; t.txt
#lon lat azimuth, semi-major, semi-minor, height tstart tend
0   0       -20     120     60      5000    3.0M    2M
50  80      -40     110     50      4000    2.8M    21.9M
EOF
gmt grdseamount -Rk-1024/1022/-1122/924 -I2000 -Gsmt_%3.1f_%s.nc t.txt -T3M/1.9M/0.1M -Qi/l -Dk -E -F0.2 -Cg -Ml.lis
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt.conf</code>, <code>gmt</code>, <code>grdmath</code>, <code>gravfft</code>, <code>gmtflexure</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
