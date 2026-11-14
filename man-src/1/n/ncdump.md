---
title: "ncdump(1)"
name: "ncdump"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncdump/"
description: "ncdump – Convert netCDF file to text form (CDL)"
---

<h2>NAME</h2>
<p> ncdump &#8211; Convert netCDF file to text form (CDL)</p>
<h2>SYNOPSIS</h2>
<p> <code></p>
<dl>
<dt>
<dd>ncdump [-chistxw] [-v </code><i>var1,&#8230;</i>] [-b <i>lang</i>] [-f <i>lang</i>] [-l <i>len</i>] [-n <i>name</i>] [-p <i>f_digits[,d_digits]</i>] [-g <i>grp1,&#8230;</i>] <i>file</i><br />
 <code></p>
<dt>
<dd>ncdump -k </code><i>file</i></dl>
<h2>DESCRIPTION</h2>
<p> The <code>ncdump</code> utility generates a text representation of a specified netCDF file on standard output, optionally excluding some or all of the variable data in the output. The text representation is in a form called CDL (network Common Data form Language) that can be viewed, edited, or serve as input to <code>ncgen</code>, a companion program that can generate a binary netCDF file from a CDL file. Hence <code>ncgen</code> and <code>ncdump</code> can be used as inverses to transform the data representation between binary and text representations. See <code>ncgen</code> documentation for a description of CDL and netCDF representations. </p>
<p> <code>ncdump</code> may also be used to determine what kind of netCDF file is used (which variant of the netCDF file format) with the -k option. </p>
<p> If DAP support was enabled when <code>ncdump</code> was built, the file name may specify a DAP URL. This allows <code>ncdump</code> to access data sources from DAP servers, including data in other formats than netCDF. When used with DAP URLs, <code>ncdump</code> shows the translation from the DAP data model to the netCDF data model. </p>
<p> <code>ncdump</code> may also be used as a simple browser for netCDF data files, to display the dimension names and lengths; variable names, types, and shapes; attribute names and values; and optionally, the values of data for all variables or selected variables in a netCDF file. For netCDF-4 files, groups and user-defined types are also included in ncdump output. </p>
<p> <code>ncdump</code> uses `_&#8217; to represent data values that are equal to the `_FillValue&#8217; attribute for a variable, intended to represent data that has not yet been written. If a variable has no `_FillValue&#8217; attribute, the default fill value for the variable type is used unless the variable is of byte type. </p>
<p> <code>ncdump</code> defines a default display format used for each type of netCDF data, but this can be changed if a `C_format&#8217; attribute is defined for a netCDF variable. In this case, <code>ncdump</code> will use the `C_format&#8217; attribute to format each value. For example, if floating-point data for the netCDF variable `Z&#8217; is known to be accurate to only three significant digits, it would be appropriate to use the variable attribute </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>Z:C_format = &quot;%.3g&quot;</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Show the values of <i>coordinate</i> variables (1D variables with the same names as dimensions) as well as the declarations of all dimensions, variables, attribute values, groups, and user-defined types. Data values of non-coordinate variables are not included in the output. This is usually the most suitable option to use for a brief look at the structure and contents of a netCDF file.</p>
<dt><code>-h</code></p>
<dd> Show only the <i>header</i> information in the output, that is, output only the declarations for the dimensions, variables, attributes, groups, and user-defined types of the input file, but no data values for any variables. The output is identical to using the <code>-c</code> option except that the values of coordinate variables are not included. (At most one of <code>-c</code> or <code>-h</code> options may be present.)</p>
<dt><code>-v</code> <i>var1,&#8230;</i></p>
<dd> The output will include data values for the specified variables, in addition to the declarations of all dimensions, variables, and attributes. One or more variables must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command, hence cannot contain unescaped blanks or other white space characters. The named variables must be valid netCDF variables in the input-file. A variable within a group in a netCDF-4 file may be specified with an absolute path name, such as `/GroupA/GroupA2/var&#8217;. Use of a relative path name such as `var&#8217; or `grp/var&#8217; specifies all matching variable names in the file. The default, without this option and in the absence of the <code>-c</code> or <code>-h</code> options, is to include data values for <i>all</i> variables in the output.</p>
<dt><code>-b</code> <i>[c|f]</i></p>
<dd> A brief annotation in the form of a CDL comment (text beginning with the characters &#8220;//&#8221;) will be included in the data section of the output for each `row&#8217; of data, to help identify data values for multidimensional variables. If <i>lang</i> begins with `C&#8217; or `c&#8217;, then C language conventions will be used (zero-based indices, last dimension varying fastest). If <i>lang</i> begins with `F&#8217; or `f&#8217;, then Fortran language conventions will be used (one-based indices, first dimension varying fastest). In either case, the data will be presented in the same order; only the annotations will differ. This option may be useful for browsing through large volumes of multidimensional data.</p>
<dt><code>-f</code> <i>[c|f]</i></p>
<dd> Full annotations in the form of trailing CDL comments (text beginning with the characters &#8220;//&#8221;) for every data value (except individual characters in character arrays) will be included in the data section. If <i>lang</i> begins with `C&#8217; or `c&#8217;, then C language conventions will be used. If <i>lang</i> begins with `F&#8217; or `f&#8217;, then Fortran language conventions will be used. In either case, the data will be presented in the same order; only the annotations will differ. This option may be useful for piping data into other filters, since each data value appears on a separate line, fully identified. (At most one of &#8216;-b&#8217; or &#8216;-f&#8217; options may be present.)</p>
<dt><code>-l</code> <i>length</i></p>
<dd> Changes the default maximum line length (80) used in formatting lists of non-character data values.</p>
<dt><code>-n</code> <i>name</i></p>
<dd> CDL requires a name for a netCDF file, for use by <code>ncgen -b</code> in generating a default netCDF file name. By default, <i>ncdump</i> constructs this name from the last component of the file name of the input netCDF file by stripping off any extension it has. Use the <code>-n</code> option to specify a different name. Although the output file name used by <code>ncgen -b</code> can be specified, it may be wise to have <i>ncdump</i> change the default name to avoid inadvertently overwriting a valuable netCDF file when using <code>ncdump</code>, editing the resulting CDL file, and using <code>ncgen -b</code> to generate a new netCDF file from the edited CDL file.</p>
<dt><code>-p</code> <i>float_digits[,double_digits]</i></p>
<dd> Specifies default precision (number of significant digits) to use in displaying floating-point or double precision data values for attributes and variables. If specified, this value overrides the value of the C_format attribute, if any, for a variable. Floating-point data will be displayed with <i>float_digits</i> significant digits. If <i>double_digits</i> is also specified, double-precision values will be displayed with that many significant digits. In the absence of any <code>-p</code> specifications, floating-point and double-precision data are displayed with 7 and 15 significant digits respectively. CDL files can be made smaller if less precision is required. If both floating-point and double precisions are specified, the two values must appear separated by a comma (no blanks) as a single argument to the command. (To represent every last bit of precision in a CDL file for all possible floating-point values would require <code>-p 9,17</code>.)</p>
<dt><code>-k</code></p>
<dd> Show kind of netCDF file the pathname references, one of `classic&#8217;, `64-bit offset&#8217;,`netCDF-4&#8242;, or `netCDF-4 classic model&#8217;. Before version 3.6, there was only one kind of netCDF file, designated as `classic&#8217; (also know as format variant 1). Large file support introduced another variant of the format, designated as `64-bit offset&#8217; (known as format variant 2). NetCDF-4, uses a third variant of the format, `netCDF-4&#8242; (format variant 3). Another format variant, designated `netCDF-4 classic model&#8217; (format variant 4), is restricted to features supported by the netCDF-3 data model but represented using the HDF5 format, so that an unmodified netCDF-3 program can read or write the file just by relinking with the netCDF-4 library. The string output by using the `-k&#8217; option may be provided as the value of the `-k&#8217; option to <a href="/docs/linux/man/1-ncgen/">ncgen</a>(1) to specify exactly what kind of netCDF file to generate, when you want to override the default inferred from the CDL.</p>
<dt><code>-s</code></p>
<dd> Output special virtual attributes that provide performance-related information about the file format and variable properties for netCDF-4 data. These special virtual attributes are not actually part of the data, they are merely a convenient way to display miscellaneous properties of the data in CDL (and eventually NcML). They include `_ChunkSizes&#8217;, `_DeflateLevel&#8217;, `_Endianness&#8217;, `_Fletcher32&#8242;, `_Format&#8217;, `_NoFill&#8217;, `_Shuffle&#8217;, and `_Storage&#8217;. `_ChunkSizes&#8217; is a list of chunk sizes for each dimension of the variable. `_DeflateLevel&#8217; is an integer between 0 and 9 inclusive if compression has been specified for the variable. `_Endianness&#8217; is either `little&#8217; or `big&#8217;, depending on how the variable was stored when first written. `_Fletcher32&#8242; is `true&#8217; if the checksum property was set for the variable. `_Format&#8217; is a global attribute specifying the netCDF format variant, one of `classic&#8217;, `64-bit offset&#8217;, `netCDF-4&#8242;, or `netCDF-4 classic model&#8217;. `_NoFill&#8217; is `true&#8217; if the persistent NoFill property was set for the variable when it was defined. `_Shuffle&#8217; is `true&#8217; if use of the shuffle filter was specified for the variable. `_Storage&#8217; is `contiguous&#8217; or `chunked&#8217;, depending on how the variable&#8217;s data is stored.</p>
<dt><code>-t</code></p>
<dd> Controls display of time data, if stored in a variable that uses a udunits compliant time representation such as `days since 1970-01-01&#8242; or `seconds since 2009-03-15 12:01:17&#8242;, a variable identified in a &quot;bounds&quot; attribute of such a time variable, or a numeric attribute of a time variable. If this option is specified, time data values are displayed as human-readable date-time strings rather than numerical values, interpreted in terms of a `calendar&#8217; variable attribute, if specified. For numeric attributes of time variables, the human-readable time value is displayed after the actual value, in an associated CDL comment. Calendar attribute values interpreted with this option include the CF Conventions values `gregorian&#8217; or `standard&#8217;, `proleptic_gregorian&#8217;, `noleap&#8217; or `365_day&#8217;, `all_leap&#8217; or `366_day&#8217;, `360_day&#8217;, and `julian&#8217;.</p>
<dt><code>-i</code></p>
<dd> Same as the &#8216;-t&#8217; option, except output time data as date-time strings with ISO-8601 standard &#8216;T&#8217; separator, instead of a blank.</p>
<dt><code>-g</code> <i>grp1,&#8230;</i></p>
<dd> For netCDF-4 files, the output will include data values only for the specified groups. One or more groups must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command. The named groups must be valid netCDF groups in the input-file. A group in a netCDF-4 file may be specified with an absolute or relative path name. Use of a relative path name specifies all matching group names in the file. The default, without this option and in the absence of the <code>-c</code> or <code>-h</code> options, is to include data values for <i>all</i> groups in the output.</p>
<dt><code>-w</code></p>
<dd> For file names that request remote access using DAP URLs, access data with client-side caching of entire variables.</p>
<dt><code>-x</code></p>
<dd> Output XML (NcML) instead of CDL. The NcML does not include data values. The NcML output option currently only works for netCDF classic model data.</dl>
<h2>EXAMPLES</h2>
<p> Look at the structure of the data in the netCDF file `<code>foo.nc</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncdump -c foo.nc</dl>
</dl>
<p> Produce an annotated CDL version of the structure and data in the netCDF file `<code>foo.nc</code>&#8216;, using C-style indexing for the annotations:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncdump -b c foo.nc &gt; foo.cdl</dl>
</dl>
<p> Output data for only the variables `uwind&#8217; and `vwind&#8217; from the netCDF file `<code>foo.nc</code>&#8216;, and show the floating-point data with only three significant digits of precision:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncdump -v uwind,vwind -p 3 foo.nc</dl>
</dl>
<p> Produce a fully-annotated (one data value per line) listing of the data for the variable `omega&#8217;, using Fortran conventions for indices, and changing the netCDF dataset name in the resulting CDL file to `omega&#8217;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncdump -v omega -f fortran -n omega foo.nc &gt; Z.cdl</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ncgen/">ncgen</a></code>(1), <code><a href="/docs/linux/man/3-netcdf/">netcdf</a></code>(3)</p>
<h2>BUGS</h2>
<p> Character arrays that contain a null-byte are treated like C strings, so no characters after the null byte appear in the output. </p>
<p> Multidimensional character string arrays are not handled well, since the CDL syntax for breaking a long character string into several shorter lines is weak. </p>
<p> There should be a way to specify that the data should be displayed in `record&#8217; order, that is with the all the values for `record&#8217; variables together that have the same value of the record dimension. </p>
<h2>Index</h2>
