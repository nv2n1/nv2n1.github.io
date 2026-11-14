---
title: "grdtrack(1)"
name: "grdtrack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdtrack/"
description: "grdtrack – Sample grids at specified (x,y) locations"
---

<h2>NAME</h2>
<p> grdtrack &#8211; Sample grids at specified (x,y) locations</p>
<h2>SYNOPSIS</h2>
<p> <code>grdtrack</code> [ <i>xyfile</i> ] <i>grd1</i> <i>grd2</i> &#8230; [ <code>f</code>|<code>p</code>|<code>m</code>|<code>r</code>|<code>R</code>[<code>+l</code>] ] [ <i>length</i>[<code>u</code>]/<i>ds</i>[<i>spacing</i>][<code>+a</code>] ] [<i>dfile</i> ] [ <i>line</i>[,<i>line</i>,&#8230;][<code>+a</code><i>az</i>][<code>+d</code>][<code>+i</code><i>inc</i>[<code>u</code>]][<code>+l</code><i>length</i>[<code>u</code>]][<code>+n</code><i>np</i>][<code>+o</code><i>az</i>][<code>+r</code><i>radius</i>[<code>u</code>] ] [ ] [ <i>region</i> ] [ <i>method</i>/<i>modifiers</i> ] [ [<i>radius</i>[<code>u</code>]][<code>+e</code>|<code>p</code>]] [ [<i>level</i>] ] [ ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdtrack</code> reads one or more grid files (or a Sandwell/Smith IMG files) and a table (from file or standard input; but see <code>-E</code> for exception) with (x,y) [or (lon,lat)] positions in the first two columns (more columns may be present). It interpolates the grid(s) at the positions in the table and writes out the table with the interpolated values added as (one or more) new columns. Alternatively (<code>-C</code>), the input is considered to be line-segments and we create orthogonal cross-profiles at each data point or with an equidistant separation and sample the grid(s) along these profiles. A bicubic [Default], bilinear, B-spline or nearest-neighbor (see <code>-n</code>) interpolation is used, requiring boundary conditions at the limits of the region (see <code>-n</code>; Default uses &quot;natural&quot; conditions (second partial derivative normal to edge is zero) unless the grid is automatically recognized as periodic.)</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>gridfile</i></p>
<dd> <i>grdfile</i> is a 2-D binary grid file with the function f(x,y). If the specified grid is in Sandwell/Smith Mercator format you must append a comma-separated list of arguments that includes a scale to multiply the data (usually 1 or 0.1), the mode which stand for the following: (0) Img files with no constraint code, returns data at all points, (1) Img file with constraints coded, return data at all points, (2) Img file with constraints coded, return data only at constrained points and NaN elsewhere, and (3) Img file with constraints coded, return 1 at constraints and 0 elsewhere, and optionally the max latitude in the IMG file [80.738]. You may repeat <code>-G</code> as many times as you have grids you wish to sample. Alternatively, use <code>-G+l</code><i>list</i> to pass a list of file names. The grids are sampled and results are output in the order given. (See GRID FILE FORMAT below.)</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>xyfile</i></p>
<dd> This is an ASCII (or binary, see <code>-bi</code>) file where the first 2 columns hold the (x,y) positions where the user wants to sample the 2-D data set.</p>
<dt><code>-A</code><code>f</code>|<code>p</code><code>m</code>|<code>r</code>|<code>R</code></p>
<dd> For track resampling (if <code>-C</code> is set) we can select how this is to be performed. Append <code>f</code> to keep original points, but add intermediate points if needed [Default], <code>m</code> as <code>f</code>, but first follow meridian (along y) then parallel (along x), <code>p</code> as <code>f</code>, but first follow parallel (along y) then meridian (along x), <code>r</code> to resample at equidistant locations; input points are not necessarily included in the output, and <code>R</code> as <code>r</code>, but adjust given spacing to fit the track length exactly. Finally, append <code>+l</code> if distances should be measured along rhumb lines (loxodromes). Ignored unless <code>-C</code> is used.</p>
<dt><code>-C</code><i>length</i>[<code>u</code>]/<i>ds</i>[<i>spacing</i>][<code>+a</code>]</p>
<dd> Use input line segments to create an equidistant and (optionally) equally-spaced set of crossing profiles along which we sample the grid(s) [Default simply samples the grid(s) at the input locations]. Specify two length scales that control how the sampling is done: <i>length</i> sets the full length of each cross-profile, while <i>ds</i> is the sampling spacing along each cross-profile. Optionally, append <code>/</code><i>spacing</i> for an equidistant spacing between cross-profiles [Default erects cross-profiles at the input coordinates]. By default, all cross-profiles have the same direction. Append <code>+a</code> to alternate the direction of cross-profiles. Append suitable units to <i>length</i>; it sets the unit used for <i>ds</i> [and <i>spacing</i>] (See UNITS below). The default unit for geographic grids is meter while Cartesian grids implies the user unit. The output columns will be <i>lon</i>, <i>lat</i>, <i>dist</i>, <i>azimuth</i>, <i>z1</i>, <i>z2</i>, &#8230;, <i>zn</i> (The <i>zi</i> are the sampled values for each of the <i>n</i> grids)</p>
<dt><code>-D</code><i>dfile</i></p>
<dd> In concert with <code>-C</code> we can save the (possibly resampled) original lines to the file <i>dfile</i> [Default only saves the cross-profiles]. The columns will be <i>lon</i>, <i>lat</i>, <i>dist</i>, <i>azimuth</i>, <i>z1</i>, <i>z2</i>, &#8230; (sampled value for each grid)</p>
<dt><code>-E</code><i>line</i>[,<i>line</i>,&#8230;][<code>+a</code><i>az</i>][<code>+d</code>][<code>+i</code><i>inc</i>[<code>u</code>]][<code>+l</code><i>length</i>[<code>u</code>]][<code>+n</code><i>np</i>][<code>+o</code><i>az</i>][<code>+r</code><i>radius</i>[<code>u</code>]</p>
<dd> Instead of reading input track coordinates, specify profiles via coordinates and modifiers. The format of each <i>line</i> is <i>start</i>/<i>stop</i>, where <i>start</i> or <i>stop</i> are either <i>lon</i>/<i>lat</i> (<i>x</i>/<i>y</i> for Cartesian data) or a 2-character XY key that uses the &quot;pstext&quot;-style justification format format to specify a point on the map as [LCR][BMT]. In addition, you can use Z-, Z+ to mean the global minimum and maximum locations in the grid (only available if only one grid is given). Instead of two coordinates you can specify an origin and one of <code>+a</code>, <code>+o</code>, or <code>+r</code>. You may append <code>+i</code><i>inc</i>[<code>u</code>] to set the sampling interval; if not given then we default to half the minimum grid interval. The <code>+a</code> sets the azimuth of a profile of given length starting at the given origin, while <code>+o</code> centers the profile on the origin; both require <code>+l</code>. For circular sampling specify <code>+r</code> to define a circle of given radius centered on the origin; this option requires either <code>+n</code> or <code>+i</code>. The <code>+n</code><i>np</i> sets the desired number of points, while <code>+l</code><i>length</i> gives the total length of the profile. Append <code>+d</code> to output the along-track distances after the coordinates. Note: No track file will be read. Also note that only one distance unit can be chosen. Giving different units will result in an error. If no units are specified we default to great circle distances in km (if geographic). If working with geographic data you can prepend &#8211; (Flat Earth) or + (Geodesic) to <i>inc</i>, <i>length</i>, or <i>radius</i> to change the mode of distance calculation [Great Circle].</p>
<dt><code>-N</code></p>
<dd> Do <i>not</i> skip points that fall outside the domain of the grid(s) [Default only output points within grid domain].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-S</code><i>method</i>/<i>modifiers</i></p>
<dd> In conjunction with <code>-C</code>, compute a single stacked profile from all profiles across each segment. Append how stacking should be computed: <code>a</code> = mean (average), <code>m</code> = median, <code>p</code> = mode (maximum likelihood), <code>l</code> = lower, <code>L</code> = lower but only consider positive values, <code>u</code> = upper, <code>U</code> = upper but only consider negative values [<code>a</code>]. The <i>modifiers</i> control the output; choose one or more among these choices: <code>+a</code> : Append stacked values to all cross-profiles. <code>+d</code> : Append stack deviations to all cross-profiles. <code>+d</code> : Append data residuals (data &#8211; stack) to all cross-profiles. <code>+s</code>[<i>file</i>] : Save stacked profile to <i>file</i> [grdtrack_stacked_profile.txt]. <code>+c</code><i>fact</i> : Compute envelope on stacked profile as +/- <i>fact</i> *<i>deviation</i> [2]. Notes: (1) Deviations depend on <i>method</i> and are st.dev (<code>a</code>), L1 scale (<code>m</code> and <code>p</code>), or half-range (upper-lower)/2. (2) The stacked profile file contains 1 plus groups of 4-6 columns, one group for each sampled grid. The first column holds cross distance, while the first 4 in a group hold stacked value, deviation, min value, and max value. If <i>method</i> is one of <code>a</code>|<code>m</code>|<code>p</code> then we also write the lower and upper confidence bounds (see <code>+c</code>). When one or more of <code>+a</code>, <code>+d</code>, and <code>+r</code> are used then we append the results to the end of each row for all cross-profiles. The order is always stacked value (<code>+a</code>), followed by deviations (<code>+d</code>) and residuals (<code>+r</code>). When more than one grid is sampled this sequence of 1-3 columns are repeated for each grid.</p>
<dt><code>-T</code>[<i>radius</i>[<code>u</code>]][<code>+e</code>|<code>p</code>]</p>
<dd> To be used with normal grid sampling, and limited to a single, non-IMG grid. If the nearest node to the input point is NaN, search outwards until we find the nearest non-NaN node and report that value instead. Optionally specify a search radius which limits the consideration to points within this distance from the input point. To report the location of the nearest node and its distance from the input point, append <code>+e</code>. To instead replace the input point with the coordinates of the nearest node, append <code>+p</code>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code></p>
<dd> Only write out the sampled z-values [Default writes all columns].</p>
<dt><code>-:</code></p>
<dd> Toggles between (longitude,latitude) and (latitude,longitude) input/output. [Default is (longitude,latitude)].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is one more than input].</p>
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
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
<dt><code>-s</code>[<i>cols</i>][<code>a</code>|<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Set handling of NaN records.</p>
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
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>HINTS</h2>
<p> If an interpolation point is not on a node of the input grid, then a NaN at any node in the neighborhood surrounding the point will yield an interpolated NaN. Bicubic interpolation [default] yields continuous first derivatives but requires a neighborhood of 4 nodes by 4 nodes. Bilinear interpolation [<code>-n</code>] uses only a 2 by 2 neighborhood, but yields only zeroth-order continuity. Use bicubic when smoothness is important. Use bilinear to minimize the propagation of NaNs, or lower <i>threshold</i>.</p>
<h2>EXAMPLES</h2>
<p> To sample the file hawaii_topo.nc along the SEASAT track track_4.xyg (An ASCII table containing longitude, latitude, and SEASAT-derived gravity, preceded by one header record): </p>
<pre>
grdtrack track_4.xyg -Ghawaii_topo.nc -h &gt; track_4.xygt
</pre>
<p> To sample the Sandwell/Smith IMG format file topo.8.2.img (2 minute predicted bathymetry on a Mercator grid) and the Muller et al age grid age.3.2.nc along the lon,lat coordinates given in the file cruise_track.xy, try </p>
<pre>
grdtrack cruise_track.xy -Gtopo.8.2.img,1,1 -Gage.3.2.nc &gt; depths-age.d
</pre>
<p> To sample the Sandwell/Smith IMG format file grav.18.1.img (1 minute free-air anomalies on a Mercator grid) along 100-km-long cross-profiles that are orthogonal to the line segment given in the file track.xy, erecting cross-profiles every 25 km and sampling the grid every 3 km, try </p>
<pre>
grdtrack track.xy -Ggrav.18.1.img,0.1,1 -C100k/3/25 -Ar &gt; xprofiles.txt
</pre>
<p> To sample the grid data.nc along a line from the lower left to the upper right corner, using a grid spacing of 1 km, and output distances as well, try </p>
<pre>
grdtrack -ELB/RT+i1k+d -Gdata.nc &gt; profiles.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtconvert</code>, <code>sample1d</code>, <code>surface</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
