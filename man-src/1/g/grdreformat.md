---
title: "grdreformat(1)"
name: "grdreformat"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdreformat/"
description: "grdreformat – Converting between different grid file formats."
---

<h2>NAME</h2>
<p> grdreformat &#8211; Converting between different grid file formats.</p>
<h2>SYNOPSIS</h2>
<p> <code>grdreformat</code> <i>ingrdfile</i>[<i>=id</i>[<i>/scale/offset</i>[<i>/NaNvalue</i>]]] <i>outgrdfile</i>[<i>=id</i>[<i>/scale/offset</i>[<i>/NaNvalue</i>]]] [ <code>-N</code> ] [ <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] ] [ <code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> ] [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>grdreformat</code> reads a grid file in one format and writes it out using another format. As an option the user may select a subset of the data to be written and to specify scaling, translation, and NaN-value.</p>
<dl>
<dt><i>ingrdfile</i></p>
<dd> The grid file to be read. Append format =<i>id</i> code if not a standard COARDS-compliant netCDF grid file. If =<i>id</i> is set (see below), you may optionally append <i>scale</i> and <i>offset</i>. These options will scale the data and then offset them with the specified amounts after reading.<br />
 If <i>scale</i> and <i>offset</i> are supplied you may also append a value that represents &#8216;Not-a-Number&#8217; (for floating-point grids this is unnecessary since the IEEE NaN is used; however integers need a value which means no data available.)</p>
<dt><i>outgrdfile</i></p>
<dd> The grid file to be written. Append format =<i>id</i> code if not a standard COARDS-compliant netCDF grid file. If =<i>id</i> is set (see below), you may optionally append <i>scale</i> and <i>offset</i>. These options are particularly practical when storing the data as integers, first removing an offset and then scaling down the values. Since the scale and offset are applied in reverse order when reading, this does not affect the data values (except for round-offs).<br />
 If <i>scale</i> and <i>offset</i> are supplied you may also append a value that represents &#8216;Not-a-Number&#8217; (for floating-point grids this is unnecessary since the IEEE NaN is used; however integers need a value which means no data available.)</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-N</code></p>
<dd> Suppress the writing of the <code>GMT</code> header structure. This is useful when you want to write a native grid to be used by <code>grdraster</code>. It only applies to native grids and is ignored for netCDF output.</p>
<dt><code>-R</code></p>
<dd> <i>xmin</i>, <i>xmax</i>, <i>ymin</i>, and <i>ymax</i> specify the Region of interest. For geographic regions, these limits correspond to <i>west, east, south,</i> and <i>north</i> and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. For calendar time coordinates you may either give (a) relative time (relative to the selected <code>TIME_EPOCH</code> and in the selected <code>TIME_UNIT</code>; append <code>t</code> to <code>-JX</code>|<code>x</code>), or (b) absolute time of the form [<i>date</i>]<code>T</code>[<i>clock</i>] (append <code>T</code> to <code>-JX</code>|<code>x</code>). At least one of <i>date</i> and <i>clock</i> must be present; the <code>T</code> is always required. The <i>date</i> string must be of the form [-]yyyy[-mm[-dd]] (Gregorian calendar) or yyyy[-Www[-d]] (ISO week calendar), while the <i>clock</i> string must be of the form hh:mm:ss[.xxx]. The use of delimiters and their type and positions must be exactly as indicated (however, input, output and plot formats are customizable; see <code>gmtdefaults</code>).</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-f</code></p>
<dd> Special formatting of input and/or output columns (time or geographical data). Specify <code>i</code> or <code>o</code> to make this apply only to input or output [Default applies to both]. Give one or more columns (or column ranges) separated by commas. Append <code>T</code> (absolute calendar time), <code>t</code> (relative time in chosen <code>TIME_UNIT</code> since <code>TIME_EPOCH</code>), <code>x</code> (longitude), <code>y</code> (latitude), or <code>f</code> (floating point) to each column or column range item. Shorthand <code>-f</code>[<code>i</code>|<code>o</code>]<code>g</code> means <code>-f</code>[<code>i</code>|<code>o</code>]0<code>x</code>,1<code>y</code> (geographic coordinates).</dl>
<h2>FORMAT IDENTIFIER</h2>
<p> By default, grids will be written as floating point data stored in binary files using the netCDF format and meta-data structure. This format is conform the COARDS conventions. <code>GMT</code> versions prior to 4.1 produced netCDF files that did not conform to these conventions. Although these files are still supported, their use is deprecated. To write other than floating point COARDS-compliant netCDF files, append the =<i>id</i> suffix to the filename <i>outgrdfile</i>.<br />
 When reading files, <code>grdreformat</code> and other <code>GMT</code> programs will automatically recognize any type of netCDF grid file. These can be in either COARDS-compliant or pre-4.1 format, and contain floating-point or integer data. To read other types of grid files, append the =<i>id</i> suffix to the filename <i>ingrdfile</i>. </p>
<p> <i>id<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT 3 netCDF legacy formats </i></p>
<p> <code>cb</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (byte) (deprecated) </p>
<p> <code>cs</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (short) (deprecated) </p>
<p> <code>ci</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (int) (deprecated) </p>
<p> <code>cf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (float) (deprecated) </p>
<p> <code>cd</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (double) (deprecated) </p>
<p> <i>id<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native binary formats </i></p>
<p> <code>bm</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (bit-mask) </p>
<p> <code>bb</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (byte) </p>
<p> <code>bs</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (short) </p>
<p> <code>bi</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (int) </p>
<p> <code>bf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (float) </p>
<p> <code>bd</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT native, C-binary format (double) </p>
<p> <i>id<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT 4 netCDF standard </i></p>
<p> <code>nb</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (byte) (COARDS-compliant) </p>
<p> <code>ns</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (short) (COARDS-compliant) </p>
<p> <code>ni</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (int) (COARDS-compliant) </p>
<p> <code>nf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (float) (COARDS-compliant) [DEFAULT]</p>
<p> <code>nd</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GMT netCDF format (double) (COARDS-compliant) </p>
<p> <i>id<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Misc formats </i></p>
<p> <code>rb</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SUN rasterfile format (8-bit standard) </p>
<p> <code>rf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GEODAS grid format GRD98 (NGDC) </p>
<p> <code>sf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Golden Software Surfer format 6 (float) </p>
<p> <code>sd</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Golden Software Surfer format 7 (double, read-only) </p>
<p> <code>af</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Atlantic Geoscience Center format AGC (float) </p>
<p> <code>gd</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Import through GDAL (convert to float) &#8212; NON-STANDARD </p>
<h2>GMT STANDARD NETCDF FILES</h2>
<p> The standard format used for gdrfiles is based on netCDF and conforms to the COARDS conventions. Files written in this format can be read by numerous third-party programs and are platform-independent. Some disk-space can be saved by storing the data as bytes or shorts in stead of integers. Use the <i>scale</i> and <i>offset</i> parameters to make this work without loss of data range or significance. For more details, see Appendix B. </p>
<p> <code>Multi-variable grid files</code><br />
 By default, <code>GMT</code> programs will read the first 2-dimensional grid contained in a COARDS-compliant netCDF file. Alternatively, use <i>ingrdfile</i><code>?</code><i>varname</i> (ahead of any optional suffix <code>=</code><i>id</i>) to specify the requested variable <i>varname</i>. Since <code>?</code> has special meaning as a wildcard, escape this meaning by placing the full filename and suffix between quotes. </p>
<p> <code>Multi-dimensional grids</code><br />
 To extract one <i>layer</i> or <i>level</i> from a 3-dimensional grid stored in a COARDS-compliant netCDF file, append both the name of the variable and the index associated with the layer (starting at zero) in the form: <i>ingrdfile</i><code>?</code><i>varname</i><code>[</code><i>layer</i><code>]</code>. Alternatively, specify the value associated with that layer using parentheses in stead of brackets: <i>ingridfile</i><code>?</code><i>varname</i><code>(</code><i>level</i><code>)</code>.<br />
 In a similar way layers can be extracted from 4- or even 5-dimensional grids. For example, if a grid has the dimensions (parameter, time, depth, latitude, longitude), a map can be selected by using: <i>ingridfile</i><code>?</code><i>varname</i><code>(</code><i>parameter,time,depth</i><code>)</code>.<br />
 Since question marks, brackets and parentheses have special meanings on the command line, escape these meanings by placing the full filename and suffix between quotes.</p>
<h2>NATIVE BINARY FILES</h2>
<p> For binary native <code>GMT</code> files the size of the <code>GMT</code> grdheader block is <i>hsize</i> = 892 bytes, and the total size of the file is <i>hsize</i> + <i>nx</i> * <i>ny</i> * <i>item_size</i>, where <i>item_size</i> is the size in bytes of each element (1, 2, 4). Bit grids are stored using 4-byte integers, each holding 32 bits, so for these files the size equation is modified by using ceil (<i>nx</i> / 32) * 4 instead of <i>nx</i>. Note that these files are platform-dependent. Files written on Little Endian machines (e.g. PCs) can not be read on Big Endian machines (e.g. most workstations). Also note that it is not possible for <code>GMT</code> to determine uniquely if a 4-byte grid is float or int; in such cases it is best to use the <i>=ID</i> mechanism to specify the file format. For header and grid details, see Appendix B.</p>
<h2>GRID VALUES PRECISION</h2>
<p> Regardless of the precision of the input data, GMT programs that create grid files will internally hold the grids in 4-byte floating point arrays. This is done to conserve memory and furthermore most if not all real data can be stored using 4-byte floating point values. Data with higher precision (i.e., double precision values) will lose that precision once GMT operates on the grid or writes out new grids. To limit loss of precision when processing data you should always consider normalizing the data prior to processing.</p>
<h2>EXAMPLES</h2>
<p> To extract the second layer from a 3-dimensional grid named temp from a COARDS-compliant netCDF file climate.grd: </p>
<p> <code>grdreformat</code> climate.grd?temp[1] temp.grd <code>-V</code> </p>
<p> To create a 4-byte native floating point grid from the COARDS-compliant netCDF file data.grd: </p>
<p> <code>grdreformat</code> data.grd ras_data.b4=bf <code>-V</code> </p>
<p> To make a 2-byte short integer file, scale it by 10, subtract 32000, setting NaNs to -9999, do </p>
<p> <code>grdreformat</code> values.grd shorts.i2=bs/10/-32000/-9999 <code>-V</code> </p>
<p> To create a Sun standard 8-bit rasterfile for a subset of the data file image.grd, assuming the range in image.grd is 0-1 and we need 0-255, run </p>
<p> <code>grdreformat</code> image.grd <code>-R</code>-60/-40/-40/-30 image.ras8=rb/255/0 <code>-V</code> </p>
<p> To convert etopo2.grd to etopo2.i2 that can be used by <code>grdraster</code>, try </p>
<p> <code>grdreformat</code> etopo2.grd etopo2.i2=bs <code>-N</code> <code>-V</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-grdmath/">grdmath</a></i>(1) </p>
<h2>Index</h2>
