---
title: "grdinfo(1)"
name: "grdinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdinfo/"
description: "grdinfo – Extract information from grids"
---

<h2>NAME</h2>
<p> grdinfo &#8211; Extract information from grids</p>
<h2>SYNOPSIS</h2>
<p> <code>grdinfo</code> <i>grdfiles</i> [ ] [ ] [ [<i>dx</i>[/<i>dy</i>]|<code>r</code>|<code>b</code>] ] [ [<code>0</code>|<code>1</code>|<code>2</code>] ] [ ] [ <i>region</i> ] [ [<code>s</code>]<i>dz</i> ] [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdinfo</code> reads a 2-D binary grid file and reports metadata and various statistics for the (<i>x</i>,<i>y</i>,<i>z</i>) data in the grid file(s). The output information contains the minimum/maximum values for <i>x</i>, <i>y</i>, and <i>z</i>, where the min/max of <i>z</i> occur, the <i>x</i>&#8211; and <i>y</i>-increments, and the number of <i>x</i> and <i>y</i> nodes, and [optionally] the mean, standard deviation, and/or the median, L1 scale of <i>z</i>, and number of nodes set to NaN. We also report if the grid is pixel- or gridline-registered and if it is a Cartesian or Geographic data set (based on metadata in the file).</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grdfile</i></p>
<dd> The name of one or several 2-D grid files. (See GRID FILE FORMATS below.)</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Formats the report using tab-separated fields on a single line. The output is <i>w e s n z0 z1 dx dy nx ny</i>[ <i>x0 y0 x1 y1</i> ] [ <i>med scale</i> ] [<i>mean std rms</i>] [<i>n_nan</i>]. The data in brackets are output only if the corresponding options <code>-M</code>, <code>-L1</code>, <code>-L2</code>, and <code>-M</code> are used, respectively. If the <code>-I</code> option is used, the output format is instead <i>NF w e s n z0 z1</i>, where <i>NF</i> is the total number of grids read and <i>w e s n</i> are rounded off (see <code>-I</code>).</p>
<dt><code>-F</code></p>
<dd> Report grid domain and x/y-increments in world mapping format [Default is generic]. Does not apply to the <code>-C</code> option.</p>
<dt><code>-I</code>[<i>dx</i>[/<i>dy</i>]|<code>r</code>|<code>b</code>]</p>
<dd> Report the min/max of the region to the nearest multiple of <i>dx</i> and <i>dy</i>, and output this in the form <code>-R</code><i>w/e/s/n</i> (unless <code>-C</code> is set). To report the actual grid region, select <code>-Ir</code>. If no argument is given then we report the grid increment in the form <code>-I</code><i>xinc/yinc</i>. If <code>-Ib</code> is given we write each grid&#8217;s bounding box polygon instead.</p>
<dt><code>-L</code>[<code>0</code> | <code>1</code> | <code>2</code>]</p>
<dd>
<dt><code>-L0</code></p>
<dd> Report range of z after actually scanning the data, not just reporting what the header says.</p>
<dt><code>-L1</code></p>
<dd> Report median and L1 scale of z (L1 scale = 1.4826 * Median Absolute Deviation (MAD)).</p>
<dt><code>-L2</code></p>
<dd> Report mean, standard deviation, and root-mean-square (rms) of z.</p>
<dt><code>-M</code></p>
<dd> Find and report the location of min/max z-values, and count and report the number of nodes set to NaN, if any.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of the input grid(s). If this subsection exceeds the boundaries of the grid, only the common region will be extracted.</p>
<dt><code>-T</code><i>dz</i></p>
<dd> Determine min and max z-value, round off to multiples of <i>dz</i>, and report as the text string <code>-T</code><i>zmin/zmax/dz</i> for use by <code>makecpt</code>. To get a symmetrical range about zero, using the max absolute multiple of <i>dz</i>, use <code>-Ts</code><i>dz</i> instead.</p>
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
<p> To obtain all the information about the data set in file hawaii_topo.nc: </p>
<pre>
gmt grdinfo -L1 -L2 -M hawaii_topo.nc
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2cpt</code>, <code>grd2xyz</code>, <code>grdedit</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
