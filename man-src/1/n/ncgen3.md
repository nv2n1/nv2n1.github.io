---
title: "ncgen3(1)"
name: "ncgen3"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncgen3/"
description: "ncgen3 – From a CDL file generate a netCDF classic or 64 bit classicfile, a C program, or a Fortran program"
---

<h2>NAME</h2>
<p> ncgen3 &#8211; From a CDL file generate a netCDF classic or 64 bit classicfile, a C program, or a Fortran program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>ncgen3 [-b] [-c] [-f] [-k <i>kind_of_file</i>] [-x] [-n] [-o <i>netcdf_filename</i>] <i>input_file</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ncgen3</code> generates either a netCDF file, or C or Fortran source code to create a netCDF file. The input to <code>ncgen3</code> is a description of a netCDF file in a small language known as CDL (network Common Data form Language), described below. If no options are specified in invoking <code>ncgen3</code>, it merely checks the syntax of the input CDL file, producing error messages for any violations of CDL syntax. Other options can be used to create the corresponding netCDF file, to generate a C program that uses the netCDF C interface to create the netCDF file, or to generate a Fortran program that uses the netCDF Fortran interface to create the same netCDF file. </p>
<p> <code>ncgen3</code> may be used with the companion program <code>ncdump</code> to perform some simple operations on netCDF files. For example, to rename a dimension in a netCDF file, use <code>ncdump</code> to get a CDL version of the netCDF file, edit the CDL file to change the name of the dimensions, and use <code>ncgen3</code> to generate the corresponding netCDF file from the edited CDL file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Create a (binary) netCDF file. If the <code>-o</code> option is absent, a default file name will be constructed from the netCDF name (specified after the <code>netcdf</code> keyword in the input) by appending the `.nc&#8217; extension. If a file already exists with the specified name, it will be overwritten.</p>
<dt><code>-c</code></p>
<dd> Generate <code>C</code> source code that will create a netCDF file matching the netCDF specification. The C source code is written to standard output.</p>
<dt><code>-f</code></p>
<dd> Generate <code>Fortran</code> source code that will create a netCDF file matching the netCDF specification. The Fortran source code is written to standard output.</p>
<dt><code>-o</code> netcdf_file</p>
<dd> Name for the binary netCDF file created. If this option is specified, it implies the &quot;<code>-b</code>&quot; option. (This option is necessary because netCDF files cannot be written directly to standard output, since standard output is not seekable.)</p>
<dt><code>-k </code>kind_of_file</p>
<dd> Using -k2 or -k &quot;64-bit offset&quot; specifies that generated file (or program) should use version 2 of format that employs 64-bit file offsets. The default is to use version 1 (&quot;classic&quot;) format with 32-bit file offsets, although this limits the size of the netCDF file, variables, and records to the sizes supported by the classic format. (NetCDF-4 will support additional kinds of netCDF files, &quot;netCDF-4&quot; and &quot;netCDF-4 classic model&quot;.) Note: -v is also accepted to mean the same thing as -k for backward compatibility, but -k is preferred, to match the corresponding ncdump option.</p>
<dt><code>-x</code></p>
<dd> Don&#8217;t initialize data with fill values. This can speed up creation of large netCDF files greatly, but later attempts to read unwritten data from the generated file will not be easily detectable.</dl>
<h2>EXAMPLES</h2>
<p> Check the syntax of the CDL file `<code>foo.cdl</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen3 foo.cdl</dl>
</dl>
<p> From the CDL file `<code>foo.cdl</code>&#8216;, generate an equivalent binary netCDF file named `<code>x.nc</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen3 -o x.nc foo.cdl</dl>
</dl>
<p> From the CDL file `<code>foo.cdl</code>&#8216;, generate a C program containing the netCDF function invocations necessary to create an equivalent binary netCDF file named `<code>x.nc</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen3 -c -o x.nc foo.cdl</dl>
</dl>
<h2>USAGE</h2>
<h3>CDL Syntax Summary</h3>
<p> Below is an example of CDL syntax, describing a netCDF file with several named dimensions (lat, lon, and time), variables (Z, t, p, rh, lat, lon, time), variable attributes (units, long_name, valid_range, _FillValue), and some data. CDL keywords are in boldface. (This example is intended to illustrate the syntax; a real CDL file would have a more complete set of attributes so that the data would be more completely self-describing.) </p>
<dl>
<dt>
<dd>
<pre><code>
netcdf foo
{ // an example netCDF specification in CDL
dimensions:
    lat = 10, lon = 5, time = unlimited;
variables:
    long lat(lat), lon(lon), time(time);
    float Z(time, lat, lon), t(time, lat, lon);
    double p(time, lat, lon);
    long rh(time, lat, lon);
// variable attributes
lat:
    long_name = "latitude";
lat:
    units = "degrees_north";
lon:
    long_name = "longitude";
lon:
    units = "degrees_east";
time:
    units = "seconds since 1992-1-1 00:00:00";
Z:
    units = "geopotential meters";
Z:
    valid_range = 0., 5000.;
p:
    _FillValue = -9999.;
rh:
    _FillValue = -1;
data:
    lat = 0, 10, 20, 30, 40, 50, 60, 70, 80, 90;
    lon = -140, -118, -96, -84, -52;
}
</code></pre>
</dl>
<p> All CDL statements are terminated by a semicolon. Spaces, tabs, and newlines can be used freely for readability. Comments may follow the characters `//&#8217; on any line. </p>
<p> A CDL description consists of three optional parts: <i>dimensions</i>, <i>variables</i>, and <i>data</i>, beginning with the keyword <code>dimensions:</code>, <code>variables:</code>, and <code>data</code>, respectively. The variable part may contain <i>variable declarations</i> and <i>attribute assignments</i>. </p>
<p> A netCDF <i>dimension</i> is used to define the shape of one or more of the multidimensional variables contained in the netCDF file. A netCDF dimension has a name and a size. At most one dimension in a netCDF file can have the <code>unlimited</code> size, which means a variable using this dimension can grow to any length (like a record number in a file). </p>
<p> A <i>variable</i> represents a multidimensional array of values of the same type. A variable has a name, a data type, and a shape described by its list of dimensions. Each variable may also have associated <i>attributes</i> (see below) as well as data values. The name, data type, and shape of a variable are specified by its declaration in the <i>variable</i> section of a CDL description. A variable may have the same name as a dimension; by convention such a variable is one-dimensional and contains coordinates of the dimension it names. Dimensions need not have corresponding variables. </p>
<p> A netCDF <i>attribute</i> contains information about a netCDF variable or about the whole netCDF dataset. Attributes are used to specify such properties as units, special values, maximum and minimum valid values, scaling factors, offsets, and parameters. Attribute information is represented by single values or arrays of values. For example, &quot;units&quot; is an attribute represented by a character array such as &quot;celsius&quot;. An attribute has an associated variable, a name, a data type, a length, and a value. In contrast to variables that are intended for data, attributes are intended for metadata (data about data). </p>
<p> In CDL, an attribute is designated by a variable and attribute name, separated by `:&#8217;. It is possible to assign <i>global</i> attributes not associated with any variable to the netCDF as a whole by using `:&#8217; before the attribute name. The data type of an attribute in CDL is derived from the type of the value assigned to it. The length of an attribute is the number of data values assigned to it, or the number of characters in the character string assigned to it. Multiple values are assigned to non-character attributes by separating the values with commas. All values assigned to an attribute must be of the same type. </p>
<p> The names for CDL dimensions, variables, and attributes must begin with an alphabetic character or `_&#8217;, and subsequent characters may be alphanumeric or `_&#8217; or `-&#8216;. </p>
<p> The optional <i>data</i> section of a CDL specification is where netCDF variables may be initialized. The syntax of an initialization is simple: a variable name, an equals sign, and a comma-delimited list of constants (possibly separated by spaces, tabs and newlines) terminated with a semicolon. For multi-dimensional arrays, the last dimension varies fastest. Thus row-order rather than column order is used for matrices. If fewer values are supplied than are needed to fill a variable, it is extended with a type-dependent `fill value&#8217;, which can be overridden by supplying a value for a distinguished variable attribute named `_FillValue&#8217;. The types of constants need not match the type declared for a variable; coercions are done to convert integers to floating point, for example. The constant `_&#8217; can be used to designate the fill value for a variable.</p>
<h3>Primitive Data Types</h3>
<dl>
<dt>
<dd>
<pre><code>
char characters
        byte 8 -
    bit data short 16 - bit signed integers long 32 - bit signed integers int(synonymous with long) float IEEE single precision floating point(32 bits) real(synonymous with float) double IEEE double precision floating point(64 bits)
</code></pre>
</dl>
<p> Except for the added data-type <code>byte</code> and the lack of <code>unsigned</code>, CDL supports the same primitive data types as C. The names for the primitive data types are reserved words in CDL, so the names of variables, dimensions, and attributes must not be type names. In declarations, type names may be specified in either upper or lower case. </p>
<p> Bytes differ from characters in that they are intended to hold a full eight bits of data, and the zero byte has no special significance, as it does for character data. <code>ncgen3</code> converts <code>byte</code> declarations to <code>char</code> declarations in the output C code and to the nonstandard <code>BYTE</code> declaration in output Fortran code. </p>
<p> Shorts can hold values between -32768 and 32767. <code>ncgen3</code> converts <code>short</code> declarations to <code>short</code> declarations in the output C code and to the nonstandard <code>INTEGER*2</code> declaration in output Fortran code. </p>
<p> Longs can hold values between -2147483648 and 2147483647. <code>ncgen3</code> converts <code>long</code> declarations to <code>long</code> declarations in the output C code and to <code>INTEGER</code> declarations in output Fortran code. <code>int</code> and <code>integer</code> are accepted as synonyms for <code>long</code> in CDL declarations. Now that there are platforms with 64-bit representations for C longs, it may be better to use the <code>int</code> synonym to avoid confusion. </p>
<p> Floats can hold values between about -3.4+38 and 3.4+38. Their external representation is as 32-bit IEEE normalized single-precision floating point numbers. <code>ncgen3</code> converts <code>float</code> declarations to <code>float</code> declarations in the output C code and to <code>REAL</code> declarations in output Fortran code. <code>real</code> is accepted as a synonym for <code>float</code> in CDL declarations. </p>
<p> Doubles can hold values between about -1.7+308 and 1.7+308. Their external representation is as 64-bit IEEE standard normalized double-precision floating point numbers. <code>ncgen3</code> converts <code>double</code> declarations to <code>double</code> declarations in the output C code and to <code>DOUBLE PRECISION</code> declarations in output Fortran code. </p>
<h3>CDL Constants</h3>
<p> Constants assigned to attributes or variables may be of any of the basic netCDF types. The syntax for constants is similar to C syntax, except that type suffixes must be appended to shorts and floats to distinguish them from longs and doubles. </p>
<p> A <i>byte</i> constant is represented by a single character or multiple character escape sequence enclosed in single quotes. For example,</p>
<dl>
<dt>
<dd>
<pre>
 'a'            // ASCII `a'
 '
