---
title: "surface(1)"
name: "surface"
section: "1"
letter: "s"
url: "/docs/linux/man/1-surface/"
description: "surface – Grid table data using adjustable tension continuous curvature splines"
---

<h2>NAME</h2>
<p> surface &#8211; Grid table data using adjustable tension continuous curvature splines</p>
<h2>SYNOPSIS</h2>
<p> <code>surface</code> [ <i>table</i> ] <i>outputfile.nc</i> <i>increment</i> <i>region</i> [ <i>aspect_ratio</i> ] [ <i>convergence_limit</i> ] [ <code>l</code><i>lower</i> ] [ <code>-Lu</code><i>upper</i> ] [ <i>max_iterations</i> ] [ ] [ <i>search_radius</i>[<code>m</code>|<code>s</code>] ] [ [<code>i</code>|<code>b</code>]<i>tension_factor</i> ] [ [<i>level</i>] ] [ <i>over-relaxation_factor</i> ] [ <code>-a</code><i>&lt;flags&gt;</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>surface</code> reads randomly-spaced (x,y,z) triples from standard input [or <i>table</i>] and produces a binary grid file of gridded values z(x,y) by solving: (1 &#8211; T) * L (L (z)) + T * L (z) = 0 </p>
<p> where T is a tension factor between 0 and 1, and L indicates the Laplacian operator. T = 0 gives the &quot;minimum curvature&quot; solution which is equivalent to SuperMISP and the ISM packages. Minimum curvature can cause undesired oscillations and false local maxima or minima (See Smith and Wessel, 1990), and you may wish to use T &gt; 0 to suppress these effects. Experience suggests T ~ 0.25 usually looks good for potential field data and T should be larger (T ~ 0.35) for steep topography data. T = 1 gives a harmonic surface (no maxima or minima are possible except at control data points). It is recommended that the user pre-process the data with <code>blockmean</code>, <code>blockmedian</code>, or <code>blockmode</code> to avoid spatial aliasing and eliminate redundant data. You may impose lower and/or upper bounds on the solution. These may be entered in the form of a fixed value, a grid with values, or simply be the minimum/maximum input data values. Natural boundary conditions are applied at the edges, except for geographic data with 360-degree range where we apply periodic boundary conditions in the longitude direction.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>outputfile.nc</i></p>
<dd> Output file name. Output is a binary 2-D <i>.nc</i> file. Note that the smallest grid dimension must be at least 4.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><i>aspect_ratio</i></p>
<dd> Aspect ratio. If desired, grid anisotropy can be added to the equations. Enter <i>aspect_ratio</i>, where dy = dx / <i>aspect_ratio</i> relates the grid dimensions. [Default = 1 assumes isotropic grid.]</p>
<dt><code>-C</code><i>convergence_limit</i>[%]</p>
<dd> Convergence limit. Iteration is assumed to have converged when the maximum absolute change in any grid value is less than <i>convergence_limit</i>. (Units same as data z units). Alternatively, give limit in percentage of rms deviation by appending %. [Default is scaled to 1e-4 of the root-mean-square deviation of the data from a best-fit (least-squares) plane.]. This is the final convergence limit at the desired grid spacing; for intermediate (coarser) grids the effective convergence limit is scaled by the grid spacing multiplier.</p>
<dt><code>-Ll</code><i>lower</i> and <code>-Lu</code><i>upper</i></p>
<dd> Impose limits on the output solution. <code>l</code><i>lower</i> sets the lower bound. <i>lower</i> can be the name of a grid file with lower bound values, a fixed value, <code>d</code> to set to minimum input value, or <code>u</code> for unconstrained [Default]. <code>u</code><i>upper</i> sets the upper bound and can be the name of a grid file with upper bound values, a fixed value, <code>d</code> to set to maximum input value, or <code>u</code> for unconstrained [Default]. Grid files used to set the limits may contain NaNs. In the presence of NaNs, the limit of a node masked with NaN is unconstrained.</p>
<dt><code>-N</code><i>max_iterations</i></p>
<dd> Number of iterations. Iteration will cease when <i>convergence_limit</i> is reached or when number of iterations reaches <i>max_iterations</i>. This is the final iteration limit at the desired grid spacing; for intermediate (coarser) grids the effective iteration limit is scaled by the grid spacing multiplier. [Default is 500.]</p>
<dt><code>-Q</code></p>
<dd> Suggest grid dimensions which have a highly composite greatest common factor. This allows surface to use several intermediate steps in the solution, yielding faster run times and better results. The sizes suggested by <code>-Q</code> can be achieved by altering <code>-R</code> and/or <code>-I</code>. You can recover the <code>-R</code> and <code>-I</code> you want later by using <code>grdsample</code> or <code>grdcut</code> on the output of <code>surface</code>.</p>
<dt><code>-S</code><i>search_radius</i>[<code>m</code>|<code>s</code>]</p>
<dd> Search radius. Enter <i>search_radius</i> in same units as x,y data; append <code>m</code> to indicate arc minutes or <code>s</code> for arc seconds. This is used to initialize the grid before the first iteration; it is not worth the time unless the grid lattice is prime and cannot have regional stages. [Default = 0.0 and no search is made.]</p>
<dt><code>-T</code>[<code>i</code>|<code>b</code>]<i>tension_factor</i></p>
<dd> Tension factor[s]. These must be between 0 and 1. Tension may be used in the interior solution (above equation, where it suppresses spurious oscillations) and in the boundary conditions (where it tends to flatten the solution approaching the edges). Using zero for both values results in a minimum curvature surface with free edges, i.e., a natural bicubic spline. Use <code>-Ti</code><i>tension_factor</i> to set interior tension, and <code>-Tb</code><i>tension_factor</i> to set boundary tension. If you do not prepend <code>i</code> or <code>b</code>, both will be set to the same value. [Default = 0 for both gives minimum curvature solution.]</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. <code>-V3</code> will report the convergence after each iteration; <code>-V</code> will report only after each regional grid is converged.</p>
<dt><code>-Z</code><i>over-relaxation_factor</i></p>
<dd> Over-relaxation factor. This parameter is used to accelerate the convergence; it is a number between 1 and 2. A value of 1 iterates the equations exactly, and will always assure stable convergence. Larger values overestimate the incremental changes during convergence, and will reach a solution more rapidly but may become unstable. If you use a large value for this factor, it is a good idea to monitor each iteration with the <code>-Vl</code> option. [Default = 1.4 converges quickly and is almost always stable.]</p>
<dt><code>-a</code><i>col</i>=<i>name</i>[<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Set aspatial column associations <i>col</i>=<i>name</i>.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>EXAMPLES</h2>
<p> To grid 5 by 5 minute gravity block means from the ASCII data in hawaii_5x5.xyg, using a <i>tension_factor</i> = 0.25, a <i>convergence_limit</i> = 0.1 milligal, writing the result to a file called hawaii_grd.nc, and monitoring each iteration, try: </p>
<pre>
gmt surface hawaii_5x5.xyg -R198/208/18/25 -I5m -Ghawaii_grd.nc -T0.25 -C0.1 -Vl
</pre>
<h2>BUGS</h2>
<p> <code>surface</code> will complain when more than one data point is found for any node and suggest that you run <code>blockmean</code>, <code>blockmedian</code>, or <code>blockmode</code> first. If you did run <code>blockm*</code> and still get this message it usually means that your grid spacing is so small that you need more decimals in the output format used by <code>blockm*</code>. You may specify more decimal places by editing the parameter <code>FORMAT_FLOAT_OUT</code> in your <code>gmt.conf</code> file prior to running <code>blockm*</code>, or choose binary input and/or output using single or double precision storage. </p>
<p> Note that only gridline registration is possible with <code>surface</code>. If you need a pixel-registered grid you can resample a gridline registered grid using <code>grdsample</code> <code>-T</code>.</p>
<h2>SEE ALSO</h2>
<p> <code>blockmean</code>, <code>blockmedian</code>, <code>blockmode</code>, <code>gmt</code>, <code>greenspline</code>, <code>nearneighbor</code>, <code>triangulate</code>, <code>sphtriangulate</code></p>
<h2>REFERENCES</h2>
<p> Smith, W. H. F, and P. Wessel, 1990, Gridding with continuous curvature splines in tension, <i>Geophysics</i>, 55, 293-305.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
