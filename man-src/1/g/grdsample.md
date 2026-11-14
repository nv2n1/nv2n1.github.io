---
title: "grdsample(1)"
name: "grdsample"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdsample/"
description: "grdsample – Resample a grid onto a new lattice"
---

<h2>NAME</h2>
<p> grdsample &#8211; Resample a grid onto a new lattice</p>
<h2>SYNOPSIS</h2>
<p> <code>grdsample</code> <i>in_grdfile</i> <i>out_grdfile</i> [ <i>increment</i> ] [ <i>region</i> ] [ ] [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-x</code>[[-]<i>n</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdsample</code> reads a grid file and interpolates it to create a new grid file with either: a different registration (<code>-r</code> or <code>-T</code>); or, a new grid-spacing or number of nodes (<code>-I</code>), and perhaps also a new sub-region (<code>-R</code>). A bicubic [Default], bilinear, B-spline or nearest-neighbor interpolation is used; see <code>-n</code> for settings. Note that using <code>-R</code> only is equivalent to <code>grdcut</code> or <code>grdedit -S</code>. <code>grdsample</code> safely creates a fine mesh from a coarse one; the converse may suffer aliasing unless the data are filtered using <code>grdfft</code> or <code>grdfilter</code>. </p>
<p> When <code>-R</code> is omitted, the output grid will cover the same region as the input grid. When <code>-I</code> is omitted, the grid spacing of the output grid will be the same as the input grid. Either <code>-r</code> or <code>-T</code> can be used to change the grid registration. When omitted, the output grid will have the same registration as the input grid.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>in_grdfile</i></p>
<dd> The name of the input 2-D binary grid file. (See GRID FILE FORMAT below.)</p>
<dt><code>-G</code><i>out_grdfile</i></p>
<dd> The name of the output grid file. (See GRID FILE FORMAT below.)</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
<dt><code>-T</code></p>
<dd> Translate between grid and pixel registration; if the input is grid-registered, the output will be pixel-registered and vice-versa.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
<dt><code>-x</code>[[-]<i>n</i>] <i>(more &#8230;)</i></p>
<dd> Limit number of cores used in multi-threaded algorithms (OpenMP required).</p>
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
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>HINTS</h2>
<p> If an interpolation point is not on a node of the input grid, then a NaN at any node in the neighborhood surrounding the point will yield an interpolated NaN. Bicubic interpolation [default] yields continuous first derivatives but requires a neighborhood of 4 nodes by 4 nodes. Bilinear interpolation [<code>-n</code>] uses only a 2 by 2 neighborhood, but yields only zero-order continuity. Use bicubic when smoothness is important. Use bilinear to minimize the propagation of NaNs.</p>
<h2>EXAMPLES</h2>
<p> To resample the 5 x 5 minute grid in hawaii_5by5_topo.nc onto a 1 minute grid: </p>
<pre>
gmt grdsample hawaii_5by5_topo.nc -I1m -Ghawaii_1by1_topo.nc
</pre>
<p> To translate the gridline-registered file surface.nc to pixel registration while keeping the same region and grid interval: </p>
<pre>
gmt grdsample surface.nc -T -Gpixel.nc
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdedit</code>, <code>grdfft</code>, <code>grdfilter</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
