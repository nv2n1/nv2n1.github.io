---
title: "grd2xyz(1)"
name: "grd2xyz"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grd2xyz/"
description: "grd2xyz – Convert grid file to data table"
---

<h2>NAME</h2>
<p> grd2xyz &#8211; Convert grid file to data table</p>
<h2>SYNOPSIS</h2>
<p> <code>grd2xyz</code> <i>grid</i> [ [<code>f</code>|<code>i</code>] ] [ <i>region</i> ] [ [<i>level</i>] ] [ [<i>weight</i>] ] [ [<i>flags</i>] ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-ho</code>[<i>n</i>] ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grd2xyz</code> reads one or more binary 2-D grid files and writes out xyz-triplets in ASCII [or binary] format to standard output. Modify the precision of the ASCII output format by editing the <i>FORMAT_FLOAT_OUT</i> parameter in your <code>gmt.conf</code> file or use <code>&#8211;</code><code>-D_FORMAT</code>=<i>format</i> on the command line, or choose binary output using single or double precision storage. As an option you may output z-values without the (x,y) coordinates; see <code>-Z</code> below.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>grid</i></p>
<dd> Names of 2-D binary grid files to be converted. (See GRID FILE FORMATS below.)</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code>[<code>f</code>|<code>i</code>]</p>
<dd> Replace the x- and y-coordinates on output with the corresponding column and row numbers. These start at 0 (C-style counting); append <code>f</code> to start at 1 (Fortran-style counting). Alternatively, append <code>i</code> to write just the two columns <i>index</i> and <i>z</i>, where <i>index</i> is the 1-D indexing that GMT uses when referring to grid nodes.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Using the <code>-R</code> option will select a subsection of the grid. If this subsection exceeds the boundaries of the grid, only the common region will be output.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<i>weight</i>]</p>
<dd> Write out x,y,z,w, where w is the supplied <i>weight</i> (or 1 if not supplied) [Default writes x,y,z only].</p>
<dt><code>-Z</code>[<i>flags</i>]</p>
<dd> Write a 1-column ASCII [or binary] table. Output will be organized according to the specified ordering convention contained in <i>flags</i>. If data should be written by rows, make <i>flags</i> start with <code>T</code> (op) if first row is y = ymax or <code>B</code> (ottom) if first row is y = ymin. Then, append <code>L</code> or <code>R</code> to indicate that first element should start at left or right end of row. Likewise for column formats: start with <code>L</code> or <code>R</code> to position first column, and then append <code>T</code> or <code>B</code> to position first element in a row. For gridline registered grids: If grid is periodic in x but the written data should not contain the (redundant) column at x = xmax, append <code>x</code>. For grid periodic in y, skip writing the redundant row at y = ymax by appending <code>y</code>. If the byte-order needs to be swapped, append <code>w</code>. Select one of several data types (all binary except <code>a</code>):</p>
<dt>&bull;</p>
<dd> <code>a</code> ASCII representation of a single item per record</p>
<dt>&bull;</p>
<dd> <code>c</code> int8_t, signed 1-byte character</p>
<dt>&bull;</p>
<dd> <code>u</code> uint8_t, unsigned 1-byte character</p>
<dt>&bull;</p>
<dd> <code>h</code> int16_t, short 2-byte integer</p>
<dt>&bull;</p>
<dd> <code>H</code> uint16_t, unsigned short 2-byte integer</p>
<dt>&bull;</p>
<dd> <code>i</code> int32_t, 4-byte integer</p>
<dt>&bull;</p>
<dd> <code>I</code> uint32_t, unsigned 4-byte integer</p>
<dt>&bull;</p>
<dd> <code>l</code> int64_t, long (8-byte) integer</p>
<dt>&bull;</p>
<dd> <code>L</code> uint64_t, unsigned long (8-byte) integer</p>
<dt>&bull;</p>
<dd> <code>f</code> 4-byte floating point single precision</p>
<dt>&bull;</p>
<dd> <code>d</code> 8-byte floating point double precision </p>
<p> Default format is scanline orientation of ASCII numbers: <code>-ZTLa</code>. Note that <code>-Z</code> only applies to 1-column output.</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 3]. This option only applies to xyz output; see <code>-Z</code> for z table output.</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns. See also <code>TIME COORDINATES</code> below. <code>-h</code> Output 1 header record based on information in the first grid file header. Ignored if binary output is selected. [Default is no header].</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>GRID FILE FORMATS</h2>
<p> By default GMT writes out grid as single precision floats in a COARDS-complaint netCDF file format. However, GMT is able to produce grid files in many other commonly used grid file formats and also facilitates so called &quot;packing&quot; of grids, writing out floating point data as 1- or 2-byte integers. To specify the precision, scale and offset, the user should add the suffix <code>=</code><i>id</i>[<code>/</code><i>scale</i><code>/</code><i>offset</i>[<code>/</code><i>nan</i>]], where <i>id</i> is a two-letter identifier of the grid type and precision, and <i>scale</i> and <i>offset</i> are optional scale factor and offset to be applied to all grid values, and <i>nan</i> is the value used to indicate missing data. In case the two characters <i>id</i> is not provided, as in <code>=/</code><i>scale</i> than a <i>id</i><code>=</code><i>nf</i> is assumed. When reading grids, the format is generally automatically recognized. If not, the same suffix can be added to input grid file names. See <code>grdconvert</code> and Section <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information. </p>
<p> When reading a netCDF file that contains multiple grids, GMT will read, by default, the first 2-dimensional grid that can find in that file. To coax GMT into reading another multi-dimensional variable in the grid file, append <code>?</code><i>varname</i> to the file name, where <i>varname</i> is the name of the variable. Note that you may need to escape the special meaning of <code>?</code> in your shell program by putting a backslash in front of it, or by placing the filename and suffix between quotes or double quotes. The <code>?</code><i>varname</i> suffix can also be used for output grids to specify a variable name different from the default: &quot;z&quot;. See <code>grdconvert</code> and Sections <i>modifiers-for-CF</i> and <i>grid-file-format</i> of the GMT Technical Reference and Cookbook for more information, particularly on how to read splices of 3-, 4-, or 5-dimensional grids.</p>
<h2>TIME COORDINATES</h2>
<p> Time coordinates in netCDF grids, be it the x, y, or z coordinate, will be recognized as such. The variable&#8217;s <code>unit</code> attribute is parsed to determine the unit and epoch of the time coordinate in the grid. Values are then converted to the internal time system specified by <i>TIME_UNIT</i> and <i>TIME_EPOCH</i> in the <code>gmt.conf</code> file or on the command line. The default output is relative time in that time system, or absolute time when using the option <code>-f0T</code>, <code>-f1T</code>, or <code>-f2T</code> for x, y, or z coordinate, respectively.</p>
<h2>EXAMPLES</h2>
<p> To edit individual values in the 5&#8242; by 5&#8242; hawaii_grv.nc file, dump the .nc to ASCII: </p>
<pre>
gmt grd2xyz hawaii_grv.nc &gt; hawaii_grv.xyz
</pre>
<p> To write a single precision binary file without the x,y positions from the file raw_data.nc file, using scanline orientation, run </p>
<pre>
gmt grd2xyz raw_data.nc -ZTLf &gt; hawaii_grv.b
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt.conf</code>, <code>gmt</code>, <code>grdedit</code>, <code>grdconvert</code>, <code>xyz2grd</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
