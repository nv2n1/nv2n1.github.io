---
title: "grdpaste(1)"
name: "grdpaste"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdpaste/"
description: "grdpaste – Join two grids along their common edge"
---

<h2>NAME</h2>
<p> grdpaste &#8211; Join two grids along their common edge</p>
<h2>SYNOPSIS</h2>
<p> <code>grdpaste</code> <i>file_a.nc file_b.nc</i> <i>outfile.nc</i> [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdpaste</code> will combine <i>file_a.nc</i> and <i>file_b.nc</i> into <i>outfile.nc</i> by pasting them together along their common edge. Files <i>file_a.nc</i> and <i>file_b.nc</i> must have the same dx, dy and have one edge in common. If in doubt, check with <code>grdinfo</code> and use <code>grdcut</code> and/or <code>grdsample</code> if necessary to prepare the edge joint. Note: For geographical grids, you may have to use <code>-f</code> to handle periodic longitudes unless the input grids are properly recognized as such via their meta-data.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>file_a.nc</i></p>
<dd> One of two files to be pasted together.</p>
<dt><i>file_b.nc</i></p>
<dd> The other of two files to be pasted together.</p>
<dt><code>-G</code><i>outfile.nc</i></p>
<dd> The name for the combined output.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
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
<p> Suppose file_a.nc is 150E &#8211; 180E and 0 &#8211; 30N, and file_b.nc is 150E &#8211; 180E, -30S &#8211; 0, then you can make outfile.nc which will be 150 &#8211; 180 and -30S &#8211; 30N by: </p>
<pre>
gmt grdpaste file_a.nc file_b.nc -Goutfile.nc -V -fg
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdblend</code>, <code>grdclip</code>, <code>grdcut</code>, <code>grdinfo</code>, <code>grdsample</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
