---
title: "grdclip(1)"
name: "grdclip"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdclip/"
description: "grdclip – Clip the range of grids"
---

<h2>NAME</h2>
<p> grdclip &#8211; Clip the range of grids</p>
<h2>SYNOPSIS</h2>
<p> <code>grdclip</code> <i>ingrid</i> <i>outgrid</i> [ <i>region</i> ] [ <code>a</code><i>high/above</i> ] [ <code>b</code><i>low/below</i> ] [ <code>i</code><i>low/high/between</i> ] [ <code>r</code><i>old/new</i> ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdclip</code> will set values &lt; <i>low</i> to <i>below</i> and/or values &gt; <i>high</i> to <i>above</i>. You can also specify one or more intervals where all values should be set to IT(between), or replace individual values. Such operations are useful when you want all of a continent or an ocean to fall into one color or gray shade in image processing, when clipping of the range of data values is required, or for reclassification of data values. <i>above</i>, <i>below</i>, <i>between</i>, <i>old</i> and <i>new</i> can be any number or even NaN (Not a Number). You must choose at least one of the <code>-S</code> options. Use <code>-R</code> to only extract a subset of the <i>ingrid</i> file.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrid</i></p>
<dd> The input 2-D binary grid file.</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> <i>outgrid</i> is the modified output grid file.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of <i>ingrid</i> grid. If this subsection exceeds the boundaries of the grid, only the common region will be extracted.</p>
<dt><code>-Sa</code><i>high/above</i></p>
<dd> Set all data[i] &gt; <i>high</i> to <i>above</i>.</p>
<dt><code>-Sb</code><i>low/below</i></p>
<dd> Set all data[i] &lt; <i>low</i> to <i>below</i>.</p>
<dt><code>-Si</code><i>low/high/between</i></p>
<dd> Set all data[i] &gt;= <i>low</i> and &lt;= <i>high</i> to <i>between</i>. Repeat the option for as many intervals as are needed.</p>
<dt><code>-Sr</code><i>old/new</i></p>
<dd> Set all data[i] == <i>old</i> to <i>new</i>. This is mostly useful when your data are known to be integer values. Repeat the option for as many replacements as are needed.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
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
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>EXAMPLES</h2>
<p> To set all values &gt; 70 to NaN and all values &lt; 0 to 0 in file data.nc: </p>
<pre>
gmt grdclip data.nc -Gnew_data.nc -Sa70/NaN -Sb0/0 -V
</pre>
<p> To reclassify all values in the 25-30 range to 99, those in 35-39 to 55, exchange 17 for 11 and all values &lt; 10 to 0 in file classes.nc, try </p>
<pre>
gmt grdclip classes.nc -Gnew_classes.nc -Si25/30/99 -Si35/39/55 -Sr17/11 -Sb10/0 -V
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdlandmask</code>, <code>grdmask</code>, <code>grdmath</code>, <code>grd2xyz</code>, <code>xyz2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
