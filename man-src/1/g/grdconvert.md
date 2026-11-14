---
title: "grdconvert(1)"
name: "grdconvert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdconvert/"
description: "grdconvert – Convert between different grid formats"
---

<h2>NAME</h2>
<p> grdconvert &#8211; Convert between different grid formats</p>
<h2>SYNOPSIS</h2>
<p> <code>grdconvert</code> <i>ingrdfile</i>[<i>=id</i>[<i>/scale/offset</i>[<i>/NaNvalue</i>]]] <i>outgrdfile</i>[<i>=id</i>[<i>/scale/offset</i>[<i>/NaNvalue</i>]][<i>:driver</i>[<i>/datatype</i>]]] [ ] [ <i>region</i> ] [ [<i>level</i>] ] [ <code>-f</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdconvert</code> reads a grid file in one format and writes it out using another format. As an option the user may select a subset of the data to be written and to specify scaling, translation, and NaN-value.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrdfile</i></p>
<dd> The grid file to be read. Append format =<i>id</i> code if not a standard COARDS-compliant netCDF grid file. If =<i>id</i> is set (see below), you may optionally append <i>scale</i> and <i>offset</i>. These options will scale the data and then offset them with the specified amounts after reading. If <i>scale</i> and <i>offset</i> are supplied you may also append a value that represents &#8216;Not-a-Number&#8217; (for floating-point grids this is unnecessary since the IEEE NaN is used; however integers need a value which means no data available). The <i>scale</i> and <i>offset</i> modifiers may be left empty to select default values (scale = 1, offset = 0).</p>
<dt><i>outgrdfile</i></p>
<dd> The grid file to be written. Append format =<i>id</i> code if not a standard COARDS-compliant netCDF grid file. If =<i>id</i> is set (see below), you may optionally append <i>scale</i> and <i>offset</i>. These options are particularly practical when storing the data as integers, first removing an offset and then scaling down the values. Since the scale and offset are applied in reverse order when reading, this does not affect the data values (except for round-offs). </p>
<p> If <i>scale</i> and <i>offset</i> are supplied you may also append a value that represents &#8216;Not-a-Number&#8217; (for floating-point grids this is unnecessary since the IEEE NaN is used; however integers need a value which means no data available). The <i>scale</i> and <i>offset</i> modifiers may be left empty to select default values (scale = 1, offset = 0), or you may specify <i>a</i> for auto-adjusting the scale and/or offset of packed integer grids (=<i>id/a</i> is a shorthand for =<i>id/a/a</i>). When <i>id</i>=<i>gd</i>, the file will be saved using the GDAL library. Append the format <i>:driver</i> and optionally the output <i>datatype</i>. The driver names are those used by GDAL itself (e.g., netCDF, GTiFF, etc.), and the data type is one of <i>u8</i>|<i>u16</i>|<i>i16</i>|<i>u32</i>|<i>i32</i>|<i>float32</i>, where &#8216;i&#8217; and &#8216;u&#8217; denote signed and unsigned integers respectively. The default type is <i>float32</i>. Note also that both driver names and data types are case insensitive. </p>
<p> Consider setting <i>IO_NC4_DEFLATION_LEVEL</i> to reduce file size and to further increase read/write performance. Especially when working with subsets of global grids, masks, and grids with repeating grid values, the improvement is usually significant.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-N</code></p>
<dd> Suppress the writing of the GMT header structure. This is useful when you want to write a native grid to be used by <code>grdraster</code>. It only applies to native grids and is ignored for netCDF output.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</p>
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
<h2>FORMAT IDENTIFIER</h2>
<p> By default, grids will be written as floating point data stored in binary files using the netCDF format and meta-data structure. This format is conform the COARDS conventions. GMT versions prior to 4.1 produced netCDF files that did not conform to these conventions. Although these files are still supported, their use is deprecated. To write other than floating point COARDS-compliant netCDF files, append the =<i>id</i> suffix to the filename <i>outgrdfile</i>. </p>
<p> When reading files, <code>grdconvert</code> and other GMT programs will try to automatically recognize the type of the input grid file. If this fails you may append the =<i>id</i> suffix to the filename <i>ingrdfile</i>. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ID </td>
<td> Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>nb</code> </td>
<td> GMT netCDF format (8-bit integer, COARDS, CF-1.5)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ns</code> </td>
<td> GMT netCDF format (16-bit integer, COARDS, CF-1.5)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ni</code> </td>
<td> GMT netCDF format (32-bit integer, COARDS, CF-1.5)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>nf</code> </td>
<td> GMT netCDF format (32-bit float, COARDS, CF-1.5)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>nd</code> </td>
<td> GMT netCDF format (64-bit float, COARDS, CF-1.5)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cb</code> </td>
<td> GMT netCDF format (8-bit integer, deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cs</code> </td>
<td> GMT netCDF format (16-bit integer, deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ci</code> </td>
<td> GMT netCDF format (32-bit integer, deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cf</code> </td>
<td> GMT netCDF format (32-bit float, deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cd</code> </td>
<td> GMT netCDF format (64-bit float, deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bm</code> </td>
<td> GMT native, C-binary format (bit-mask)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bb</code> </td>
<td> GMT native, C-binary format (8-bit integer)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bs</code> </td>
<td> GMT native, C-binary format (16-bit integer)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bi</code> </td>
<td> GMT native, C-binary format (32-bit integer)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bf</code> </td>
<td> GMT native, C-binary format (32-bit float)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>bd</code> </td>
<td> GMT native, C-binary format (64-bit float)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rb</code> </td>
<td> SUN rasterfile format (8-bit standard)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rf</code> </td>
<td> GEODAS grid format GRD98 (NGDC)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sf</code> </td>
<td> Golden Software Surfer format 6 (32-bit float)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sd</code> </td>
<td> Golden Software Surfer format 7 (64-bit float, read-only)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>af</code> </td>
<td> Atlantic Geoscience Center format AGC (32-bit float)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ei</code> </td>
<td> ESRI Arc/Info ASCII Grid Interchange format (ASCII integer)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ef</code> </td>
<td> ESRI Arc/Info ASCII Grid Interchange format (ASCII float)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>gd</code> </td>
<td> Import/export through GDAL
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>GMT STANDARD NETCDF FILES</h2>
<p> The standard format used for grdfiles is based on netCDF and conforms to the COARDS conventions. Files written in this format can be read by numerous third-party programs and are platform-independent. Some disk-space can be saved by storing the data as bytes or shorts in stead of integers. Use the <i>scale</i> and <i>offset</i> parameters to make this work without loss of data range or significance. For more details, see <i>App-file-formats</i>. </p>
<p> <code>Multi-variable grid files</code> </p>
<p> By default, GMT programs will read the first 2-dimensional grid contained in a COARDS-compliant netCDF file. Alternatively, use <i>ingrdfile</i><code>?</code><i>varname</i> (ahead of any optional suffix <code>=</code><i>id</i>) to specify the requested variable <i>varname</i>. Since <code>?</code> has special meaning as a wildcard, escape this meaning by placing the full filename and suffix between quotes. </p>
<p> <code>Multi-dimensional grids</code> </p>
<p> To extract one <i>layer</i> or <i>level</i> from a 3-dimensional grid stored in a COARDS-compliant netCDF file, append both the name of the variable and the index associated with the layer (starting at zero) in the form: <i>ingrdfile</i><code>?</code><i>varname</i><code>[</code><i>layer</i><code>]</code>. Alternatively, specify the value associated with that layer using parentheses in stead of brackets: <i>ingridfile</i><code>?</code><i>varname</i><code>(</code><i>layer</i><code>)</code>. </p>
<p> In a similar way layers can be extracted from 4- or even 5-dimensional grids. For example, if a grid has the dimensions (parameter, time, depth, latitude, longitude), a map can be selected by using: <i>ingridfile</i><code>?</code><i>varname</i><code>(</code><i>parameter</i>,<i>time</i>,<i>depth</i><code>)</code>. </p>
<p> Since question marks, brackets and parentheses have special meanings on the command line, escape these meanings by placing the full filename and suffix between quotes.</p>
<h2>NATIVE BINARY FILES</h2>
<p> For binary native GMT files the size of the GMT grid header block is <i>hsize</i> = 892 bytes, and the total size of the file is <i>hsize</i> + <i>nx</i> * <i>ny</i> * <i>item_size</i>, where <i>item_size</i> is the size in bytes of each element (1, 2, 4). Bit grids are stored using 4-byte integers, each holding 32 bits, so for these files the size equation is modified by using ceil (<i>nx</i> / 32) * 4 instead of <i>nx</i>. Note that these files are platform-dependent. Files written on Little Endian machines (e.g., PCs) can not be read on Big Endian machines (e.g., most workstations). Also note that it is not possible for GMT to determine uniquely if a 4-byte grid is float or int; in such cases it is best to use the <i>=ID</i> mechanism to specify the file format. In all cases a native grid is considered to be signed (i.e., there are no provision for unsigned short ints or unsigned bytes). For header and grid details, see <i>App-file-formats</i>.</p>
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>EXAMPLES</h2>
<p> To extract the second layer from a 3-dimensional grid named temp from a COARDS-compliant netCDF file climate.nc: </p>
<pre>
gmt grdconvert climate.nc?temp[1] temp.nc -V
</pre>
<p> To create a 4-byte native floating point grid from the COARDS-compliant netCDF file data.nc: </p>
<pre>
gmt grdconvert data.nc ras_data.b4=bf -V
</pre>
<p> To make a 2-byte short integer file, scale it by 10, subtract 32000, setting NaNs to -9999, do </p>
<pre>
gmt grdconvert values.nc shorts.i2=bs/10/-32000/-9999 -V
</pre>
<p> To create a Sun standard 8-bit rasterfile for a subset of the data file image.nc, assuming the range in image.nc is 0-1 and we need 0-255, run </p>
<pre>
gmt grdconvert image.nc -R-60/-40/-40/-30 image.ras8=rb/255/0 -V
</pre>
<p> To convert etopo2.nc to etopo2.i2 that can be used by <code>grdraster</code>, try </p>
<pre>
gmt grdconvert etopo2.nc etopo2.i2=bs -N -V
</pre>
<p> To creat a dumb file saved as a 32 bits float GeoTiff using GDAL, run </p>
<pre>
gmt grdmath -Rd -I10 X Y MUL = lixo.tiff=gd:GTiff
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt.conf</code>, <code>gmt</code>, <code>grdmath</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
