---
title: "grdblend(1)"
name: "grdblend"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdblend/"
description: "grdblend – Blend several partially over-lapping grids into one large grid"
---

<h2>NAME</h2>
<p> grdblend &#8211; Blend several partially over-lapping grids into one large grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdblend</code> [ <i>blendfile</i> | <i>grid1</i> <i>grid2</i> &#8230; ] <i>outgrid</i> [ <i>increment</i> ] [ <i>region</i> ] [ <code>f</code>|<code>l</code>|<code>o</code>|<code>u</code> ] [ <i>nodata</i> ] [ ] [ <i>scale</i> ] [ [<i>level</i>] ] [ [<code>z</code>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdblend</code> reads a listing of grid files and blend parameters and creates a binary grid file by blending the other grids using cosine-taper weights. <code>grdblend</code> will report if some of the nodes are not filled in with data. Such unconstrained nodes are set to a value specified by the user [Default is NaN]. Nodes with more than one value will be set to the weighted average value. Any input grid that does not share the final output grid&#8217;s node registration and grid spacing will automatically be resampled via calls to grdsample. Note: Due to the row-by-row i/o nature of operations in grdblend we only support the netCDF and native binary grid formats for both input and output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>outgrid</i></p>
<dd> <i>outgrid</i> is the name of the binary output grid file. (See GRID FILE FORMATS below). Only netCDF and native binary grid formats are can be written directly. Other output format choices will be handled by reformatting the output once blending is complete.</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>blendfile</i></p>
<dd> ASCII file with one record per grid file to include in the blend. Each record may contain up to three items, separated by spaces or tabs: the gridfile name (required), the <code>-R</code>-setting for the interior region (optional), and the relative weight <i>wr</i> (optional). In the combined weighting scheme, this grid will be given zero weight outside its domain, weight = <i>wr</i> inside the interior region, and a 2-D cosine-tapered weight between those end-members in the boundary strip. However, if a negative <i>wr</i> is given then the sense of tapering is inverted (i.e., zero weight inside its domain). If the inner region should instead exactly match the grid region then specify a &#8211; instead of the <code>-R</code>-setting, or leave it off entirely. Likewise, if a weight <i>wr</i> is not specified we default to a weight of 1. If the ASCII <i>blendfile</i> file is not given <code>grdblend</code> will read standard input. Alternatively, if you have more than one grid file to blend and you wish (a) all input grids to have the same weight (1) and (b) all grids should use their actual region as the interior region, then you may simply list all the grids on the command line instead of providing a <i>blendfile</i>. You must specify at least 2 input grids for this mechanism to work. Any grid that is not co-registered with the desired output layout implied by <code>-R</code>, <code>-I</code> (and <code>-r</code>) will first be resampled via <code>grdsample</code>. Also, grids that are not in netCDF or native binary format will first be reformatted via <code>grdconvert</code>.</p>
<dt><code>-C</code></p>
<dd> Clobber mode: Instead of blending, simply pick the value of one of the grids that covers a node. Select from the following modes: <code>f</code> for the first grid to visit a node; <code>o</code> for the last grid to visit a node; <code>l</code> for the grid with the lowest value, and <code>u</code> for the grid with the uppermost value. For modes <code>f</code> and <code>o</code> the ordering of grids in the <i>blendfile</i> will dictate which grid contributes to the final result. Weights and cosine tapering are not considered when clobber mode is active.</p>
<dt><code>-N</code><i>nodata</i></p>
<dd> No data. Set nodes with no input grid to this value [Default is NaN].</p>
<dt><code>-Q</code></p>
<dd> Create a header-less grid file suitable for use with <code>grdraster</code>. Requires that the output grid file is a native format (i.e., not netCDF).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>z</code>]</p>
<dd> Do not blend, just output the weights used for each node [Default makes the blend]. Append <code>z</code> to write the weight*z sum instead.</p>
<dt><code>-Z</code><i>scale</i></p>
<dd> Scale output values by <i>scale</i> before writing to file. [1].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
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
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When writing a netCDF file, the grid is stored by default with the variable name &quot;z&quot;. To specify another variable name <i>varname</i>, append <code>?</code><i>varname</i> to the file name. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>TAPERING</h2>
<p> While the weights computed are tapered from 1 to 0, we are computing weighted averages, so if there is only a single grid given then the weighted output will be identical to the input. If you are looking for a way to taper your data grid, see grdmath&#8217;s TAPER operator.</p>
<h2>EXAMPLES</h2>
<p> To create a grid file from the four grid files piece_?.nc, giving them each the different weights, make the blendfile like this </p>
<pre>
piece_1.nc -R&lt;subregion_1&gt; 1
piece_2.nc -R&lt;subregion_2&gt; 1.5
piece_3.nc -R&lt;subregion_3&gt; 0.9
piece_4.nc -R&lt;subregion_4&gt; 1
</pre>
<p> Then run </p>
<pre>
gmt grdblend blend.job -Gblend.nc -R&lt;full_region&gt; -I&lt;dx/dy&gt; -V
</pre>
<p> To blend all the grids called MB_*.nc given them all equal weight, try </p>
<pre>
gmt grdblend MB_*.nc -Gblend.nc -R&lt;full_region&gt; -I&lt;dx/dy&gt; -V
</pre>
<h2>WARNING ON LARGE FILE SETS</h2>
<p> While grdblend can process any number of files, it works by keeping those files open that are being blended, and close files as soon as they are finished. Depending on your session, many files may remain open at the same time. Some operating systems set fairly modest default limits on how many concurrent files can be open, e.g., 256. If you run into this problem then you can change this limit; see your operating system documentation for how to change system limits.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2xyz</code>, <code>grdedit</code> <code>grdraster</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
