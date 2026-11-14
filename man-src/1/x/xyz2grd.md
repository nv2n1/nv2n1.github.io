---
title: "xyz2grd(1)"
name: "xyz2grd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xyz2grd/"
description: "xyz2grd – Convert data table to a grid file"
---

<h2>NAME</h2>
<p> xyz2grd &#8211; Convert data table to a grid file</p>
<h2>SYNOPSIS</h2>
<p> <code>xyz2grd</code> [ <i>table</i> ] <i>grdfile</i> <i>increment</i> <i>region</i> [ [<code>f</code>|<code>l</code>|<code>m</code>|<code>n</code>|<code>r</code>|<code>s</code>|<code>u</code>|<code>z</code>] ] [ <i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>/<i>title</i>/<i>remark</i> ] [ [<i>zfile</i>] ] [ [<i>level</i>] ] [ [<i>flags</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>xyz2grd</code> reads one or more z or xyz tables and creates a binary grid file. <code>xyz2grd</code> will report if some of the nodes are not filled in with data. Such unconstrained nodes are set to a value specified by the user [Default is NaN]. Nodes with more than one value will be set to the mean value. As an option (using <code>-Z</code>), a 1-column z-table may be read assuming all nodes are present (z-tables can be in organized in a number of formats, see <code>-Z</code> below.)</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-G</code><i>grdfile</i></p>
<dd> <i>grdfile</i> is the name of the binary output grid file. (See GRID FILE FORMAT below.)</p>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files holding z or (x,y,z) values. The xyz triplets do not have to be sorted. One-column z tables must be sorted and the <code>-Z</code> must be set.</p>
<dt><code>-A</code>[<code>f</code>|<code>l</code>|<code>m</code>|<code>n</code>|<code>r</code>|<code>s</code>|<code>u</code>|<code>z</code>]</p>
<dd> By default we will calculate mean values if multiple entries fall on the same node. Use <code>-A</code> to change this behavior, except it is ignored if <code>-Z</code> is given. Append <code>f</code> or <code>s</code> to simply keep the first or last data point that was assigned to each node. Append <code>l</code> or <code>u</code> to find the lowest (minimum) or upper (maximum) value at each node, respectively. Append <code>m</code> or <code>r</code> to compute mean or RMS value at each node, respectively. Append <code>n</code> to simply count the number of data points that were assigned to each node (this only requires two input columns <i>x</i> and <i>y</i> as <i>z</i> is not consulted). Append <code>z</code> to sum multiple values that belong to the same node.</p>
<dt><code>-D</code><i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>/<i>title</i>/<i>remark</i></p>
<dd> Give values for <i>xname</i>, <i>yname</i>, <i>zname</i> (give the names of those variables and in square bracket their units, e.g., &quot;distance [km]&quot;), <i>scale</i> (to multiply grid values after read [normally 1]), <i>offset</i> (to add to grid after scaling [normally 0]), <i>invalid</i> (a value to represent missing data [NaN]), <i>title</i> (anything you like), and <i>remark</i> (anything you like). To leave some of these values untouched, leave field blank. Empty fields in the end may be skipped. Alternatively, to allow &quot;/&quot; to be part of one of the values, use any non-alphanumeric character (and not the equal sign) as separator by both starting and ending with it. For example: <code>-D</code>:<i>xname</i>:<i>yname</i>:<i>zname</i>:<i>scale</i>:<i>offset</i>:<i>invalid</i>:<i>title</i>:<i>remark</i>: Use quotes to group texts with more than one word. Note that for geographic grids (<code>-fg</code>) <i>xname</i> and <i>yname</i> are set automatically.</p>
<dt><code>-S</code>[<i>zfile</i>]</p>
<dd> Swap the byte-order of the input only. No grid file is produced. You must also supply the <code>-Z</code> option. The output is written to <i>zfile</i> (or stdout if not supplied).</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code>[<i>flags</i>]</p>
<dd> Read a 1-column ASCII [or binary] table. This assumes that all the nodes are present and sorted according to specified ordering convention contained in <i>flags</i>. If incoming data represents rows, make <i>flags</i> start with <code>T</code>(op) if first row is y = ymax or <code>B</code>(ottom) if first row is y = ymin. Then, append <code>L</code> or <code>R</code> to indicate that first element is at left or right end of row. Likewise for column formats: start with <code>L</code> or <code>R</code> to position first column, and then append <code>T</code> or <code>B</code> to position first element in a row. Note: These two row/column indicators are only required for grids; for other tables they do not apply. For gridline registered grids: If data are periodic in x but the incoming data do not contain the (redundant) column at x = xmax, append <code>x</code>. For data periodic in y without redundant row at y = ymax, append <code>y</code>. Append <code>s</code><i>n</i> to skip the first <i>n</i> number of bytes (probably a header). If the byte-order or the words needs to be swapped, append <code>w</code>. Select one of several data types (all binary except <code>a</code>): </p>
<p> <code>A</code> ASCII representation of one or more floating point values per record </p>
<p> <code>a</code> ASCII representation of a single item per record </p>
<p> <code>c</code> int8_t, signed 1-byte character </p>
<p> <code>u</code> uint8_t, unsigned 1-byte character </p>
<p> <code>h</code> int16_t, signed 2-byte integer </p>
<p> <code>H</code> uint16_t, unsigned 2-byte integer </p>
<p> <code>i</code> int32_t, signed 4-byte integer </p>
<p> <code>I</code> uint32_t, unsigned 4-byte integer </p>
<p> <code>l</code> int64_t, long (8-byte) integer </p>
<p> <code>L</code> uint64_t, unsigned long (8-byte) integer </p>
<p> <code>f</code> 4-byte floating point single precision </p>
<p> <code>d</code> 8-byte floating point double precision </p>
<p> Default format is scanline orientation of ASCII numbers: <code>-ZTLa</code>. Note that <code>-Z</code> only applies to 1-column input. The difference between <code>A</code> and <code>a</code> is that the latter can decode both <i>date</i><code>T</code><i>clock</i> and <i>ddd:mm:ss[.xx]</i> formats while the former is strictly for regular floating point values.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns]. This option only applies to xyz input files; see <code>-Z</code> for z tables.</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN. Also sets nodes with no input xyz triplet to this value [Default is NaN].</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s). Not used with binary data.</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When writing a netCDF file, the grid is stored by default with the variable name &quot;z&quot;. To specify another variable name <i>varname</i>, append <code>?</code><i>varname</i> to the file name. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes.</p>
<h2>GEOGRAPHICAL AND TIME COORDINATES</h2>
<p> When the output grid type is netCDF, the coordinates will be labeled &quot;longitude&quot;, &quot;latitude&quot;, or &quot;time&quot; based on the attributes of the input data or grid (if any) or on the <code>-f</code> or <code>-R</code> options. For example, both <code>-f0x</code> <code>-f1t</code> and <code>-R</code>90w/90e/0t/3t will result in a longitude/time grid. When the x, y, or z coordinate is time, it will be stored in the grid as relative time since epoch as specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. In addition, the <code>unit</code> attribute of the time variable will indicate both this unit and epoch.</p>
<h2>SWAPPING LIMITATIONS</h2>
<p> All data types can be read, even 64-bit integers, but internally grids are stored using floats. Hence, integer values exceeding the float type&#8217;s 23-bit mantissa may not be represented exactly. When <code>-S</code> is used no grids are implied and we read data into an intermediate double container. This means all but 64-bit integers can be represented using the double type&#8217;s 53-bit mantissa.</p>
<h2>EXAMPLES</h2>
<p> To create a grid file from the ASCII data in hawaii_grv.xyz, use</p>
<dl>
<dt><code>gmt xyz2grd hawaii_grv.xyz -Ddegree/degree/mGal/1/0//Hawaiian Gravity/GRS-80 Ellipsoid used </code></p>
<dd> -Ghawaii_grv_new.nc -R198/208/18/25 -I5m -V </p>
<p> To create a grid file from the raw binary (3-column, single-precision scanline-oriented data raw.b, use gmt xyz2grd raw.b -Dm/m/m/1/0 -Graw.nc -R0/100/0/100 -I1 -V -Z -bi3f </p>
<p> To make a grid file from the raw binary USGS DEM (short integer scanline-oriented data topo30.b on the NGDC global relief Data CD-ROM, with values of -9999 indicate missing data, one must on some machine reverse the byte-order. On such machines (like Sun), use gmt xyz2grd topo30.b -Dm/m/m/1/0 -Gustopo.nc -R234/294/24/50 -I30s -di-9999 -ZTLhw </p>
<p> Say you have received a binary file with 4-byte floating points that were written on a machine of different byte-order than yours. You can swap the byte-order with gmt xyz2grd floats.bin -Snew_floats.bin -V -Zf</dl>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2xyz</code>, <code>grdedit</code>, <code>grdconvert</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
