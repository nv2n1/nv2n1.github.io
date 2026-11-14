---
title: "grdedit(1)"
name: "grdedit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdedit/"
description: "grdedit – Modify header or content of a grid"
---

<h2>NAME</h2>
<p> grdedit &#8211; Modify header or content of a grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdedit</code> <i>grid</i> [ ] [ <i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>/<i>title</i>/<i>remark</i> ] [ [<code>a</code>|<code>h</code>|<code>l</code>|<code>r</code>|<code>t</code>|<code>v</code>] ] [ <i>outgrid</i> ] [ <i>parameters</i> ] [ <i>table</i> ] [ <i>region</i> ] [ ] [ ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdedit</code> reads the header information in a binary 2-D grid file and replaces the information with values provided on the command line [if any]. As an option, global, geographical grids (with 360 degrees longitude range) can be rotated in the east-west direction, and individual nodal values can be replaced from a table of <i>x</i>, <i>y</i>, <i>z</i> values. <code>grdedit</code> only operates on files containing a grid header. Note: If it is important to retain the original data you should use <code>-G</code> to save the modified grid to a new file.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grid</i></p>
<dd> Name of the 2-D grid file to modify. (See GRID FILE FORMATS below).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> If necessary, adjust the file&#8217;s <i>x_inc</i>, <i>y_inc</i> to be compatible with its domain (or a new domain set with <code>-R</code>). Older grid files (i.e., created prior to GMT 3.1) often had excessive slop in <i>x_inc</i>, <i>y_inc</i> and an adjustment is necessary. Newer files are created correctly.</p>
<dt><code>-D</code><i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>/<i>title</i>/<i>remark</i></p>
<dd> Give values for <i>xname</i>, <i>yname</i>, <i>zname</i> (give the names of those variables and in square bracket their units, e.g., &quot;distance [km]&quot;), <i>scale</i> (to multiply grid values after read [normally 1]), <i>offset</i> (to add to grid after scaling [normally 0]), <i>invalid</i> (a value to represent missing data [NaN]), <i>title</i> (anything you like), and <i>remark</i> (anything you like). To leave some of these values untouched, leave field blank. Empty fields in the end may be skipped. Alternatively, to allow &quot;/&quot; to be part of one of the values, use any non-alphanumeric character (and not the equal sign) as separator by both starting and ending with it. For example: <code>-D</code>:<i>xname</i>:<i>yname</i>:<i>zname</i>:<i>scale</i>:<i>offset</i>:<i>invalid</i>:<i>title</i>:<i>remark</i>: Use quotes to group texts with more than one word. Note that for geographic grids (<code>-fg</code>) <i>xname</i> and <i>yname</i> are set automatically.</p>
<dt><code>-E</code>[<code>a</code>|<code>h</code>|<code>l</code>|<code>r</code>|<code>t</code>|<code>v</code>]</p>
<dd> Transform the grid in one of six ways and (for <code>l</code>|<code>r</code>|<code>t</code>) interchange the <i>x</i> and <i>y</i> information: <code>-Ea</code> will rotate the grid around 180 degrees, <code>-Eh</code> will flip the grid horizontally (left-to-right), <code>-El</code> will rotate the grid 90 degrees counter-clockwise (left), <code>-Er</code> will rotate the grid 90 degrees clockwise (right), <code>-Et</code> will transpose the grid [Default], <code>-Ev</code> will flip the grid vertically (top-to-bottom). Incompatible with the other options (except <code>-G</code>).</p>
<dt><code>-G</code><i>outgrid</i></p>
<dd> Normally, grdedit will overwrite the existing grid with the modified grid. Use <code>-G</code> to write the modified grid to the file <i>outgrid</i> instead.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection. Use the <code>-J</code> syntax to save the georeferencing info as CF-1 compliant metadata in netCDF grids. This metadata will be recognized by GDAL.</p>
<dt><code>-N</code><i>table</i></p>
<dd> Read the ASCII (or binary; see <code>-bi</code>) file <i>table</i> and replace the corresponding nodal values in the grid with these <i>x</i>,<i>y</i>,<i>z</i> values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. The new w/e/s/n values will replace those in the grid, and the <i>x_inc</i>, <i>y_inc</i> values are adjusted, if necessary.</p>
<dt><code>-S</code></p>
<dd> For global, geographical grids only. Grid values will be shifted longitudinally according to the new borders given in <code>-R</code>.</p>
<dt><code>-T</code></p>
<dd> Make necessary changes in the header to convert a gridline-registered grid to a pixel-registered grid, or vice-versa. Basically, gridline-registered grids will have their domain extended by half the x- and y-increments whereas pixel-registered grids will have their domain shrunk by the same amount.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>EXAMPLES</h2>
<p> Let us assume the file data.nc covers the area 300/310/10/30. We want to change the boundaries from geodetic longitudes to geographic and put a new title in the header. We accomplish this by </p>
<pre>
gmt grdedit data.nc -R-60/-50/10/30 -D//////&quot;Gravity Anomalies&quot;
</pre>
<p> The grid world.nc has the limits 0/360/-72/72. To shift the data so that the limits would be -180/180/-72/72, use </p>
<pre>
gmt grdedit world.nc -R-180/180/-72/72 -S
</pre>
<p> The file junk.nc was created prior to GMT 3.1 with incompatible <code>-R</code> and <code>-I</code> arguments. To reset the x- and y-increments we run </p>
<pre>
gmt grdedit junk.nc -A
</pre>
<p> The file junk.nc was created prior to GMT 4.1.3 and does not contain the required information to indicate that the grid is geographic. To add this information, run </p>
<pre>
gmt grdedit junk.nc -fg
</pre>
<p> To rotate the grid oblique.nc 90 degrees counter-clockwise and write out the rotated grid to a new file, run </p>
<pre>
gmt grdedit oblique.nc -El -Goblique_rot.nc
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2xyz</code>, <code>grdinfo</code> <code>xyz2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
