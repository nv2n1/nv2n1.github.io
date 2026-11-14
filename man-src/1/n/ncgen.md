---
title: "ncgen(1)"
name: "ncgen"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncgen/"
description: "ncgen – From a CDL file generate a netCDF-3 file, a netCDF-4 file or a C program"
---

<h2>NAME</h2>
<p> ncgen &#8211; From a CDL file generate a netCDF-3 file, a netCDF-4 file or a C program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>ncgen [-b] [-c] [-f] [-k <i>format_name</i>] [-<i>format_code</i>] [-l <i>output language</i>] [-n] [-o <i>netcdf_filename</i>] [-x] [<i>input_file</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ncgen</code> generates either a netCDF-3 (i.e. classic) binary .nc file, a netCDF-4 (i.e. enhanced) binary .nc file or a file in some source language that when executed will construct the corresponding binary .nc file. The input to <code>ncgen</code> is a description of a netCDF file in a small language known as CDL (network Common Data form Language), described below. Input is read from standard input if no input_file is specified. If no options are specified in invoking <code>ncgen</code>, it merely checks the syntax of the input CDL file, producing error messages for any violations of CDL syntax. Other options can be used, for example, to create the corresponding netCDF file, or to generate a C program that uses the netCDF C interface to create the netCDF file. </p>
<p> Note that this version of ncgen was originally called ncgen4. The older ncgen program has been renamed to ncgen3. </p>
<p> <code>ncgen</code> may be used with the companion program <code>ncdump</code> to perform some simple operations on netCDF files. For example, to rename a dimension in a netCDF file, use <code>ncdump</code> to get a CDL version of the netCDF file, edit the CDL file to change the name of the dimensions, and use <code>ncgen</code> to generate the corresponding netCDF file from the edited CDL file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Create a (binary) netCDF file. If the <code>-o</code> option is absent, a default file name will be constructed from the basename of the CDL file, with any suffix replaced by the `.nc&#8217; extension. If a file already exists with the specified name, it will be overwritten.</p>
<dt><code>-c</code></p>
<dd> Generate <code>C</code> source code that will create a netCDF file matching the netCDF specification. The C source code is written to standard output; equivalent to -lc.</p>
<dt><code>-f</code></p>
<dd> Generate <code>FORTRAN 77</code> source code that will create a netCDF file matching the netCDF specification. The source code is written to standard output; equivalent to -lf77.</p>
<dt><code>-o</code> netcdf_file</p>
<dd> Name of the file to pass to calls to &quot;nc_create()&quot;. If this option is specified it implies (in the absence of any explicit -l flag) the &quot;<code>-b</code>&quot; option. This option is necessary because netCDF files cannot be written directly to standard output, since standard output is not seekable.</p>
<dt><code>-k </code><i>format_name</i></p>
<dd>
<dt><code>&#8211;</code><i>format_code</i></p>
<dd> The -k flag specifies the format of the file to be created and, by inference, the data model accepted by ncgen (i.e. netcdf-3 (classic) versus netcdf-4). As a shortcut, a numeric <i>format_code</i> may be specified instead. The possible <i>format_name</i> values for the -k option are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8216;classic&#8217; or &#8216;nc3&#8217; =&gt; netCDF classic format</p>
<dd>
<dt>&#8217;64-bit offset&#8217; or &#8216;nc6&#8217; =&gt; netCDF 64-bit format</p>
<dd>
<dt>&#8216;netCDF-4&#8217; 0r &#8216;nc4&#8217; =&gt; netCDF-4 format (enhanced data model)</p>
<dd>
<dt>&#8216;netCDF-4 classic model&#8217; or &#8216;nc7&#8217; =&gt; netCDF-4 classic model format</p>
<dd></dl>
</dl>
</dl>
<p> Accepted <i>format_number</i> arguments, just shortcuts for format_names, are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>3 =&gt; netcdf classic format</p>
<dd>
<dt>6 =&gt; netCDF 64-bit format</p>
<dd>
<dt>4 =&gt; netCDF-4 format (enhanced data model)</p>
<dd>
<dt>7 =&gt; netCDF-4 classic model format</p>
<dd></dl>
</dl>
</dl>
<p> The numeric code &quot;7&quot; is used because &quot;7=3+4&quot;, a mnemonic for the format that uses the netCDF-3 data model for compatibility with the netCDF-4 storage format for performance. Credit is due to NCO for use of these numeric codes instead of the old and confusing format numbers.</dl>
<p> Note: The old version format numbers &#8216;1&#8217;, &#8216;2&#8217;, &#8216;3&#8217;, &#8216;4&#8217;, equivalent to the format names &#8216;nc3&#8217;, &#8216;nc6&#8217;, &#8216;nc4&#8217;, or &#8216;nc7&#8217; respectively, are also still accepted but deprecated, due to easy confusion between format numbers and format names. Various old format name aliases are also accepted but deprecated, e.g. &#8216;hdf5&#8217;, &#8216;enhanced-nc3&#8217;, etc. Also, note that -v is accepted to mean the same thing as -k for backward compatibility.</p>
<dl>
<dt><code>-x</code></p>
<dd> Don&#8217;t initialize data with fill values. This can speed up creation of large netCDF files greatly, but later attempts to read unwritten data from the generated file will not be easily detectable.</p>
<dt><code>-l </code>output_language</p>
<dd> The -l flag specifies the output language to use when generating source code that will create or define a netCDF file matching the netCDF specification. The output is written to standard output. The currently supported languages have the following flags.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>c|C&#8217; =&gt; C language output.</p>
<dd>
<dt>f77|fortran77&#8242; =&gt; FORTRAN 77 language output</p>
<dd> ; note that currently only the classic model is supported.</p>
<dt>j|java&#8217; =&gt; (experimental) Java language output</p>
<dd> ; targets the existing Unidata Java interface, which means that only the classic model is supported.</dl>
</dl>
</dl>
</dl>
<h2>Choosing the output format</h2>
<p> The choice of output format is determined by three flags.</p>
<dl>
<dt><code>-k flag.</code></p>
<dd>
<dt><code>_Format attribute (see below).</code></p>
<dd>
<dt><code>Occurrence of netcdf-4 constructs in the input CDL.</code></p>
<dd> The term &quot;netCDF-4 constructs&quot; means constructs from the enhanced data model, not just special performance-related attributes such as<br />
&nbsp;<wbr>_ChunkSizes,&nbsp;<wbr>_DeflateLevel,&nbsp;<wbr>_Endianness, etc.</dl>
<p> The rules are as follows, in order of application.</p>
<dl>
<dt><code>1.</code></p>
<dd> If either Fortran or Java output is specified, then -k flag value of 1 (classic model) will be used. Conflicts with the use of enhanced constructs in the CDL will report an error.</p>
<dt><code>2.</code></p>
<dd> If both the -k flag and _Format attribute are specified, the _Format flag will be ignored. If no -k flag is specified, and a _Format attribute value is specified, then the -k flag value will be set to that of the _Format attribute. Otherwise the -k flag is undefined.</p>
<dt><code>3.</code></p>
<dd> If the -k option is defined and is consistent with the CDL, ncgen will output a file in the requested form, else an error will be reported.</p>
<dt><code>4.</code></p>
<dd> If the -k flag is undefined, and if there are netCDF-4 constructs in the CDL, a -k flag value of 3 (enhanced model) will be used.</p>
<dt><code>5.</code></p>
<dd> If special performance-related attributes are specified in the CDL, a -k flag value of 4 (netCDF-4 classic model) will be used.</p>
<dt><code>6.</code></p>
<dd> Otherwise ncgen will set the -k flag to 1 (classic model).</dl>
<h2>EXAMPLES</h2>
<p> Check the syntax of the CDL file `<code>foo.cdl</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen foo.cdl</dl>
</dl>
<p> From the CDL file `<code>foo.cdl</code>&#8216;, generate an equivalent binary netCDF file named `<code>x.nc</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen -o x.nc foo.cdl</dl>
</dl>
<p> From the CDL file `<code>foo.cdl</code>&#8216;, generate a C program containing the netCDF function invocations necessary to create an equivalent binary netCDF file named `<code>x.nc</code>&#8216;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>ncgen -lc foo.cdl &gt;x.c</dl>
</dl>
<h2>USAGE</h2>
<h3>CDL Syntax Overview</h3>
<p> Below is an example of CDL syntax, describing a netCDF file with several named dimensions (lat, lon, and time), variables (Z, t, p, rh, lat, lon, time), variable attributes (units, long_name, valid_range, _FillValue), and some data. CDL keywords are in boldface. (This example is intended to illustrate the syntax; a real CDL file would have a more complete set of attributes so that the data would be more completely self-describing.)</p>
<dl>
<dt>
<dd>
<pre><code>
netcdf foo
{ // an example netCDF specification in CDL
types:
    ubyte enum enum_t { Clear = 0,
                        Cumulonimbus = 1,
                        Stratus = 2 };
    opaque(11) opaque_t;
    int(*) vlen_t;
dimensions:
    lat = 10, lon = 5, time = unlimited;
variables:
    long lat(lat), lon(lon), time(time);
    float Z(time, lat, lon), t(time, lat, lon);
    double p(time, lat, lon);
    long rh(time, lat, lon);
    string country(time, lat, lon);
    ubyte tag;
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
    // typed variable attributes
    string Z : units = "geopotential meters";
    float Z : valid_range = 0., 5000.;
    double p : _FillValue = -9999.;
    long rh : _FillValue = -1;
vlen_t:
    globalatt = {17, 18, 19};
data:
    lat = 0, 10, 20, 30, 40, 50, 60, 70, 80, 90;
    lon = -140, -118, -96, -84, -52;
group:
    g
    {
    types:
        compound cmpd_t
        {
            vlen_t f1;
            enum_t f2;
        };
    } // group g
group:
    h
    {
    variables:
        / g / cmpd_t compoundvar;
    data:
        compoundvar = &#123;&#123;3, 4, 5}, enum_t.Stratus};
    } // group h
}
</code></pre>
</dl>
<p> All CDL statements are terminated by a semicolon. Spaces, tabs, and newlines can be used freely for readability. Comments may follow the characters `//&#8217; on any line. </p>
<p> A CDL description consists of five optional parts: <i>types</i>, <i>dimensions</i>, <i>variables</i>, <i>data</i>, beginning with the keyword <code>`types:&#8217;</code>, <code>`dimensions:&#8217;</code>, <code>`variables:&#8217;</code>, and <code>`data:&#8217;,</code> respectively. Note several things: (1) the keyword includes the trailing colon, so there must not be any space before the colon character, and (2) the keywords are required to be lower case. </p>
<p> The <code>variables:</code> section may contain <i>variable declarations</i> and <i>attribute assignments</i>. All sections may contain global attribute assignments. </p>
<p> In addition, after the <code>data:</code> section, the user may define a series of groups (see the example above). Groups themselves can contain types, dimensions, variables, data, and other (nested) groups. </p>
<p> The netCDF <code>types:</code> section declares the user defined types. These may be constructed using any of the following types: <code>enum</code>, <code>vlen</code>, <code>opaque</code>, or <code>compound</code>. </p>
<p> A netCDF <i>dimension</i> is used to define the shape of one or more of the multidimensional variables contained in the netCDF file. A netCDF dimension has a name and a size. A dimension can have the <code>unlimited</code> size, which means a variable using this dimension can grow to any length in that dimension. </p>
<p> A <i>variable</i> represents a multidimensional array of values of the same type. A variable has a name, a data type, and a shape described by its list of dimensions. Each variable may also have associated <i>attributes</i> (see below) as well as data values. The name, data type, and shape of a variable are specified by its declaration in the <i>variable</i> section of a CDL description. A variable may have the same name as a dimension; by convention such a variable is one-dimensional and contains coordinates of the dimension it names. Dimensions need not have corresponding variables. </p>
<p> A netCDF <i>attribute</i> contains information about a netCDF variable or about the whole netCDF dataset. Attributes are used to specify such properties as units, special values, maximum and minimum valid values, scaling factors, offsets, and parameters. Attribute information is represented by single values or arrays of values. For example, &quot;units&quot; is an attribute represented by a character array such as &quot;celsius&quot;. An attribute has an associated variable, a name, a data type, a length, and a value. In contrast to variables that are intended for data, attributes are intended for metadata (data about data). Unlike netCDF-3, attribute types can be any user defined type as well as the usual built-in types. </p>
<p> In CDL, an attribute is designated by a a type, a variable, a &#8216;:&#8217;, and then an attribute name. The type is optional and if missing, it will be inferred from the values assigned to the attribute. It is possible to assign <i>global</i> attributes not associated with any variable to the netCDF as a whole by omitting the variable name in the attribute declaration. Notice that there is a potential ambiguity in a specification such as </p>
<pre>
x : a = ...
</pre>
<p> In this situation, x could be either a type for a global attribute, or the variable name for an attribute. Since there could both be a type named x and a variable named x, there is an ambiguity. The rule is that in this situation, x will be interpreted as a type if possible, and otherwise as a variable. </p>
<p> If not specified, the data type of an attribute in CDL is derived from the type of the value(s) assigned to it. The length of an attribute is the number of data values assigned to it, or the number of characters in the character string assigned to it. Multiple values are assigned to non-character attributes by separating the values with commas. All values assigned to an attribute must be of the same type. </p>
<p> The names for CDL dimensions, variables, attributes, types, and groups may contain any non-control utf-8 character except the forward slash character (`/&#8217;). However, certain characters must escaped if they are used in a name, where the escape character is the backward slash `\&#8217;. In particular, if the leading character off the name is a digit (0-9), then it must be preceded by the escape character. In addition, the characters ` !&quot;#$%&amp;()*,:;&lt;=&gt;?[]^`'{}|~\&#8217; must be escaped if they occur anywhere in a name. Note also that attribute names that begin with an underscore (`_&#8217;) are reserved for the use of Unidata and should not be used in user defined attributes. </p>
<p> Note also that the words `variable&#8217;, `dimension&#8217;, `data&#8217;, `group&#8217;, and `types&#8217; are legal CDL names, but be careful that there is a space between them and any following colon character when used as a variable name. This is mostly an issue with attribute declarations. For example, consider this.</p>
<dl>
<dt>
<dl>
<dt>
<dd>
netcdf&#8230;<br />
{<br />
    &#8230; variables : int dimensions;<br />
dimensions:<br />
    attribute = 0; // this will cause an error<br />
dimensions:<br />
    attribute = 0; // this is ok.<br />
    &#8230;<br />
}
</dl>
</dl>
<dd>The optional <code>data:</code> section of a CDL specification is where netCDF variables may be initialized. The syntax of an initialization is simple: a variable name, an equals sign, and a comma-delimited list of constants (possibly separated by spaces, tabs and newlines) terminated with a semicolon. For multi-dimensional arrays, the last dimension varies fastest. Thus row-order rather than column order is used for matrices. If fewer values are supplied than are needed to fill a variable, it is extended with a type-dependent `fill value&#8217;, which can be overridden by supplying a value for a distinguished variable attribute named `_FillValue&#8217;. The types of constants need not match the type declared for a variable; coercions are done to convert integers to floating point, for example. The constant `_&#8217; can be used to designate the fill value for a variable. If the type of the variable is explicitly `string&#8217;, then the special constant `NIL` can be used to represent a nil string, which is not the same as a zero length string.</p>
<h3>Primitive Data Types</h3>
<dl>
<dt>
<dd>
char characters<br />
        byte 8 &#8211;<br />
    bit data short 16 &#8211; bit signed integers int 32 &#8211; bit signed integers long(synonymous with int) int64 64 &#8211; bit signed integers float IEEE single precision floating point(32 bits) real(synonymous with float) double IEEE double precision floating point(64 bits) ubyte unsigned 8 &#8211; bit data ushort 16 &#8211; bit unsigned integers uint 32 &#8211; bit unsigned integers uint64 64 &#8211; bit unsigned integers string arbitrary length strings
</dl>
<p> CDL supports a superset of the primitive data types of C. The names for the primitive data types are reserved words in CDL, so the names of variables, dimensions, and attributes must not be primitive type names. In declarations, type names may be specified in either upper or lower case. </p>
<p> Bytes are intended to hold a full eight bits of data, and the zero byte has no special significance, as it mays for character data. <code>ncgen</code> converts <code>byte</code> declarations to <code>char</code> declarations in the output C code and to the nonstandard <code>BYTE</code> declaration in output Fortran code. </p>
<p> Shorts can hold values between -32768 and 32767. <code>ncgen</code> converts <code>short</code> declarations to <code>short</code> declarations in the output C code and to the nonstandard <code>INTEGER*2</code> declaration in output Fortran code. </p>
<p> Ints can hold values between -2147483648 and 2147483647. <code>ncgen</code> converts <code>int</code> declarations to <code>int</code> declarations in the output C code and to <code>INTEGER</code> declarations in output Fortran code. <code>long</code> is accepted as a synonym for <code>int</code> in CDL declarations, but is deprecated since there are now platforms with 64-bit representations for C longs. </p>
<p> Int64 can hold values between -9223372036854775808 and 9223372036854775807. <code>ncgen</code> converts <code>int64</code> declarations to <code>longlong</code> declarations in the output C code. </p>
<p> Floats can hold values between about -3.4+38 and 3.4+38. Their external representation is as 32-bit IEEE normalized single-precision floating point numbers. <code>ncgen</code> converts <code>float</code> declarations to <code>float</code> declarations in the output C code and to <code>REAL</code> declarations in output Fortran code. <code>real</code> is accepted as a synonym for <code>float</code> in CDL declarations. </p>
<p> Doubles can hold values between about -1.7+308 and 1.7+308. Their external representation is as 64-bit IEEE standard normalized double-precision floating point numbers. <code>ncgen</code> converts <code>double</code> declarations to <code>double</code> declarations in the output C code and to <code>DOUBLE PRECISION</code> declarations in output Fortran code. </p>
<p> The unsigned counterparts of the above integer types are mapped to the corresponding unsigned C types. Their ranges are suitably modified to start at zero. </p>
<p> The technical interpretation of the char type is that it is an unsigned 8-bit value. The encoding of the 256 possible values is unspecified by default. A variable of char type may be marked with an &quot;_Encoding&quot; attribute to indicate the character set to be used: US-ASCII, ISO-8859-1, etc. Note that specifying the encoding of UTF-8 is equivalent to specifying US-ASCII This is because multi-byte UTF-8 characters cannot be stored in an 8-bit character. The only legal single byte UTF-8 values are by definition the 7-bit US-ASCII encoding with the top bit set to zero. </p>
<p> Strings are assumed by default to be encoded using UTF-8. Note that this means that multi-byte UTF-8 encodings may be present in the string, so it is possible that the number of distinct UTF-8 characters in a string is smaller than the number of 8-bit bytes used to store the string. </p>
<h3>CDL Constants</h3>
<p> Constants assigned to attributes or variables may be of any of the basic netCDF types. The syntax for constants is similar to C syntax, except that type suffixes must be appended to shorts and floats to distinguish them from longs and doubles. </p>
<p> A <i>byte</i> constant is represented by<br />
&nbsp;<wbr>an integer constant with a&nbsp;<wbr>`b&#8217;&nbsp;<wbr>(or `B&#8217;) appended. In the old netCDF-2 API, byte constants could also be represented using single characters or standard C character escape sequences such as `a&#8217; or `. This is still supported for backward compatibility, but deprecated to make the distinction clear between the numeric byte type and the textual char type. Example byte constants include:</p>
<dl>
<dt>
<dd>
<pre>
 0b             // a zero byte
 -1b            // -1 as an 8-bit byte
 255b           // also -1 as a signed 8-bit byte
</pre>
</dl>
<p> <i>short</i> integer constants are intended for representing 16-bit signed quantities. The form of a <i>short</i> constant is an integer constant with an `s&#8217; or `S&#8217; appended. If a <i>short</i> constant begins with `0&#8242;, it is interpreted as octal, except that if it begins with `0x&#8217;, it is interpreted as a hexadecimal constant. For example:</p>
<dl>
<dt>
<dd>
<pre>
-2s     // a short -2
0123s   // octal
0x7ffs  //hexadecimal
</pre>
</dl>
<p> <i>int</i> integer constants are intended for representing 32-bit signed quantities. The form of an <i>int</i> constant is an ordinary integer constant, although it is acceptable to append an optional `l&#8217; or `L&#8217; (again, deprecated). If an <i>int</i> constant begins with `0&#8242;, it is interpreted as octal, except that if it begins with `0x&#8217;, it is interpreted as a hexadecimal constant (but see opaque constants below). Examples of valid <i>int</i> constants include:</p>
<dl>
<dt>
<dd>
<pre>
-2
1234567890L
0123            // octal
0x7ff           // hexadecimal
</pre>
</dl>
<p> <i>int64</i> integer constants are intended for representing 64-bit signed quantities. The form of an <i>int64</i> constant is an integer constant with an `ll&#8217; or `LL&#8217; appended. If an <i>int64</i> constant begins with `0&#8242;, it is interpreted as octal, except that if it begins with `0x&#8217;, it is interpreted as a hexadecimal constant. For example:</p>
<dl>
<dt>
<dd>
<pre>
-2ll    // an unsigned -2
0123LL  // octal
0x7ffLL  //hexadecimal
</pre>
</dl>
<p> Floating point constants of type <i>float</i> are appropriate for representing floating point data with about seven significant digits of precision. The form of a <i>float</i> constant is the same as a C floating point constant with an `f&#8217; or `F&#8217; appended. For example the following are all acceptable <i>float</i> constants:</p>
<dl>
<dt>
<dd>
<pre>
-2.0f
3.14159265358979f       // will be truncated to less precision
1.f
</pre>
</dl>
<p> Floating point constants of type <i>double</i> are appropriate for representing floating point data with about sixteen significant digits of precision. The form of a <i>double</i> constant is the same as a C floating point constant. An optional `d&#8217; or `D&#8217; may be appended. For example the following are all acceptable <i>double</i> constants:</p>
<dl>
<dt>
<dd>
<pre>
-2.0
3.141592653589793
1.0e-20
1.d
</pre>
</dl>
<p> Unsigned integer constants can be created by appending the character &#8216;U&#8217; or &#8216;u&#8217; between the constant and any trailing size specifier. Thus one could say 10U, 100us, 100000ul, or 1000000ull, for example. </p>
<p> Single character constants may be enclosed in single quotes. If a sequence of one or more characters is enclosed in double quotes, then its interpretation must be inferred from the context. If the dataset is created using the netCDF classic model, then all such constants are interpreted as a character array, so each character in the constant is interpreted as if it were a single character. If the dataset is netCDF extended, then the constant may be interpreted as for the classic model or as a true string (see below) depending on the type of the attribute or variable into which the string is contained. </p>
<p> The interpretation of char constants is that those that are in the printable ASCII range (&#8216; &#8216;..&#8217;~&#8217;) are assumed to be encoded as the 1-byte subset ofUTF-8, which is equivalent to US-ASCII. In all cases, the usual C string escape conventions are honored for values from 0 thru 127. Values greater than 127 are allowed, but their encoding is undefined. For netCDF extended, the use of the char type is deprecated in favor of the string type. </p>
<p> Some character constant examples are as follows.</p>
<dl>
<dt>
<dd>
<pre>
 'a'            // ASCII `a'
 &quot;a&quot;            // equivalent to 'a'
 &quot;Two
lines
&quot; // a 10-character string with two embedded newlines
 &quot;a bell:&quot;  // a string containing an ASCII bell
</pre>
</dl>
<p> Note that the netCDF character array &quot;a&quot; would fit in a one-element variable, since no terminating NULL character is assumed. However, a zero byte in a character array is interpreted as the end of the significant characters by the <code>ncdump</code> program, following the C convention. Therefore, a NULL byte should not be embedded in a character string unless at the end: use the <i>byte</i> data type instead for byte arrays that contain the zero byte. </p>
<p> <i>String</i> constants are, like character constants, represented using double quotes. This represents a potential ambiguity since a multi-character string may also indicate a dimensioned character value. Disambiguation usually occurs by context, but care should be taken to specify the<i>string</i> type to ensure the proper choice. String constants are assumed to always be UTF-8 encoded. This specifically means that the string constant may actually contain multi-byte UTF-8 characters. The special constant `NIL` can be used to represent a nil string, which is not the same as a zero length string. </p>
<p> <i>Opaque</i> constants are represented as sequences of hexadecimal digits preceded by 0X or 0x: 0xaa34ffff, for example. These constants can still be used as integer constants and will be either truncated or extended as necessary.</p>
<h3>Compound Constant Expressions</h3>
<p> In order to assign values to variables (or attributes) whose type is user-defined type, the constant notation has been extended to include sequences of constants enclosed in curly brackets (e.g. &quot;{&quot;&#8230;&quot;}&quot;). Such a constant is called a compound constant, and compound constants can be nested. </p>
<p> Given a type &quot;T(*) vlen_t&quot;, where T is some other arbitrary base type, constants for this should be specified as follows.<br />
vlen_t var[2] = {t11, t12, &#8230; t1N}, {t21, t22, &#8230; t2m};<br />
 The values tij, are assumed to be constants of type T. </p>
<p> Given a type &quot;compound cmpd_t {T1 f1; T2 f2&#8230;Tn fn}&quot;, where the Ti are other arbitrary base types, constants for this should be specified as follows.<br />
cmpd_t var[2] = {t11, t12, &#8230; t1N}, {t21, t22, &#8230; t2n};<br />
 The values tij, are assumed to be constants of type Ti. If the fields are missing, then they will be set using any specified or default fill value for the field&#8217;s base type. </p>
<p> The general set of rules for using braces are defined in the <code>Specifying</code> <code>Datalists</code> section below. </p>
<h3>Scoping Rules</h3>
<p> With the addition of groups, the name space for defined objects is no longer flat. References (names) of any type, dimension, or variable may be prefixed with the absolute path specifying a specific declaration. Thus one might say </p>
<pre>
    variables:
        /g1/g2/t1 v1;
</pre>
<p> The type being referenced (t1) is the one within group g2, which in turn is nested in group g1. The similarity of this notation to Unix file paths is deliberate, and one can consider groups as a form of directory structure. </p>
<p> When name is not prefixed, then scope rules are applied to locate the specified declaration. Currently, there are three rules: one for dimensions, one for types and enumeration constants, and one for all others.</p>
<dl>
<dt>
<dd>When an unprefixed name of a dimension is used (as in a variable declaration), ncgen first looks in the immediately enclosing group for the dimension. If it is not found there, then it looks in the group enclosing this group. This continues up the group hierarchy until the dimension is found, or there are no more groups to search.</p>
<dt>
<dd>2. When an unprefixed name of a type or an enumeration constant is used, ncgen searches the group tree using a pre-order depth-first search. This essentially means that it will find the matching declaration that precedes the reference textually in the cdl file and that is &quot;highest&quot; in the group hierarchy.</p>
<dt>
<dd>3. For all other names, only the immediately enclosing group is searched.</dl>
<p> One final note. Forward references are not allowed. This means that specifying, for example, /g1/g2/t1 will fail if this reference occurs before g1 and/or g2 are defined.</p>
<h3>Specifying Enumeration Constants</h3>
<p> References to Enumeration constants (in data lists) can be ambiguous since the same enumeration constant name can be defined in more than one enumeration. If a cdl file specified an ambiguous constant, then ncgen will signal an error. Such constants can be disambiguated in two ways.</p>
<dl>
<dt><code>1.</code></p>
<dd> Prefix the enumeration constant with the name of the enumeration separated by a dot: <i>enum.econst</i>, for example.</p>
<dt><code>2.</code></p>
<dd> If case one is not sufficient to disambiguate the enumeration constant, then one must specify the precise enumeration type using a group path: <i>/g1/g2/enum.econst</i>, for example.</dl>
<h3>Special Attributes</h3>
<p> Special, virtual, attributes can be specified to provide performance-related information about the file format and about variable properties. The file must be a netCDF-4 file for these to take effect. </p>
<p> These special virtual attributes are not actually part of the file, they are merely a convenient way to set miscellaneous properties of the data in CDL </p>
<p> The special attributes currently supported are as follows: `_Format&#8217;, `_Fletcher32, `_ChunkSizes&#8217;, `_Endianness&#8217;, `_DeflateLevel&#8217;, `_Shuffle&#8217;, and `_Storage&#8217;. </p>
<p> `_Format&#8217; is a global attribute specifying the netCDF format variant. Its value must be a single string matching one of `classic&#8217;, `64-bit offset&#8217;, `netCDF-4&#8242;, or `netCDF-4 classic model&#8217;. </p>
<p> The rest of the special attributes are all variable attributes. Essentially all of then map to some corresponding `nc_def_var_XXX&#8217; function as defined in the netCDF-4 API. For the atttributes that are essentially boolean (_Fletcher32, _Shuffle, and _NOFILL), the value true can be specified by using the strings `true&#8217; or `1&#8242;, or by using the integer 1. The value false expects either `false&#8217;, `0&#8242;, or the integer 0. The actions associated with these attributes are as follows.</p>
<dl>
<dt>1.</p>
<dd> `_Fletcher32 sets the `fletcher32&#8242; property for a variable.</p>
<dt>2.</p>
<dd> `_Endianness&#8217; is either `little&#8217; or `big&#8217;, depending on how the variable is stored when first written.</p>
<dt>3.</p>
<dd> `_DeflateLevel&#8217; is an integer between 0 and 9 inclusive if compression has been specified for the variable.</p>
<dt>4.</p>
<dd> `_Shuffle&#8217; specifies if the the shuffle filter should be used.</p>
<dt>5.</p>
<dd> `_Storage&#8217; is `contiguous&#8217; or `chunked&#8217;.</p>
<dt>6.</p>
<dd> `_ChunkSizes&#8217; is a list of chunk sizes for each dimension of the variable</dl>
<p> Note that attributes such as &quot;add_offset&quot; or &quot;scale_factor&quot; have no special meaning to ncgen. These attributes are currently conventions, handled above the library layer by other utility packages, for example NCO. </p>
<h3>Specifying Datalists</h3>
<p> Specifying datalists for variables in the `data:` section can be somewhat complicated. There are some rules that must be followed to ensure that datalists are parsed correctly by ncgen. </p>
<p> First, the top level is automatically assumed to be a list of items, so it should not be inside {&#8230;}. That means that if the variable is a scalar, there will be a single top-level element and if the variable is an array, there will be N top-level elements. For each element of the top level list, the following rules should be applied.</p>
<dl>
<dt>1.</p>
<dd> Instances of UNLIMITED dimensions (other than the first dimension) must be surrounded by {&#8230;} in order to specify the size.</p>
<dt>2.</p>
<dd> Compound instances must be embedded in {&#8230;}</p>
<dt>3.</p>
<dd> Non-scalar fields of compound instances must be embedded in {&#8230;}.</p>
<dt>4.</p>
<dd> Instances of vlens must be surrounded by {&#8230;} in order to specify the size.</dl>
<p> Datalists associated with attributes are implicitly a vector (i.e., a list) of values of the type of the attribute and the above rules must apply with that in mind.</p>
<dl>
<dt>7.</p>
<dd> No other use of braces is allowed.</dl>
<p> Note that one consequence of these rules is that arrays of values cannot have subarrays within braces. Consider, for example, int var(d1)(d2)&#8230;(dn), where none of d2&#8230;dn are unlimited. A datalist for this variable must be a single list of integers, where the number of integers is no more than D=d1*d2*&#8230;dn values; note that the list can be less than D, in which case fill values will be used to pad the list. </p>
<p> Rule 6 about attribute datalist has the following consequence. If the type of the attribute is a compound (or vlen) type, and if the number of entries in the list is one, then the compound instances must be enclosed in braces. </p>
<h3>Specifying Character Datalists</h3>
<p> Specifying datalists for variables of type char also has some complications. consider, for example</p>
<dl>
<dt>
<dd>
dimensions : u = UNLIMITED;<br />
d1 = 1;<br />
d2 = 2;<br />
d3 = 3;<br />
d4 = 4;<br />
d5 = 5;<br />
u2 = UNLIMITED;<br />
variables : char var(d4, d5);<br />
datalist : var = &#8220;1&#8221;, &#8220;two&#8221;, &#8220;three&#8221;;
</dl>
<p> We have twenty elements of var to fill (d5 X d4) and we have three strings of length 1, 3, 5. How do we assign the characters in the strings to the twenty elements? </p>
<p> This is challenging because it is desirable to mimic the original ncgen (ncgen3). The core algorithm is notionally as follows.</p>
<dl>
<dt>1.</p>
<dd> Assume we have a set of dimensions D1..Dn, where D1 may optionally be an Unlimited dimension. It is assumed that the sizes of the Di are all known (including unlimited dimensions).</p>
<dt>2.</p>
<dd> Given a sequence of string or character constants C1..Cm, our goal is to construct a single string whose length is the cross product of D1 thru Dn. Note that for purposes of this algorithm, character constants are treated as strings of size 1.</p>
<dt>3.</p>
<dd> Construct Dx = cross product of D1 thru D(n-1).</p>
<dt>4.</p>
<dd> For each constant Ci, add fill characters as needed so that its length is a multiple of Dn.</p>
<dt>5.</p>
<dd> Concatenate the modified C1..Cm to produce string S.</p>
<dt>6.</p>
<dd> Add fill characters to S to make its length be a multiple of Dn.</p>
<dt>8.</p>
<dd> If S is longer than the Dx * Dn, then truncate and generate a warning.</dl>
<p> There are three other cases of note.</p>
<dl>
<dt>1.</p>
<dd> If there is only a single, unlimited dimension, then all of the constants are concatenated and fill characers are added to the end of the resulting string to make its length be that of the unlimited dimension. If the length is larger than the unlimited dimension, then it is truncated with a warning.</p>
<dt>2.</p>
<dd> For the case of character typed vlen, &quot;char(*) vlen_t&quot; for example. we simply concatenate all the constants with no filling at all.</p>
<dt>3.</p>
<dd> For the case of a character typed attribute, we simply concatenate all the constants.</dl>
<p> In netcdf-4, dimensions other than the first can be unlimited. Of course by the rules above, the interior unlimited instances must be delimited by {&#8230;}. For example.<br />
variables : char var(u, u2);<br />
datalist : var = {&#8220;1&#8221;, &#8220;two&#8221;}, {&#8220;three&#8221;};<br />
 In this case u will have the effective length of two. Within each instance of u2, the rules above will apply, leading to this. datalist: var={&quot;1&quot;,&quot;t&quot;,&quot;w&quot;,&quot;o&quot;}, {&quot;t&quot;,&quot;h&quot;,&quot;r&quot;,&quot;e&quot;,&quot;e&quot;}; The effective size of u2 will be the max of the two instance lengths (five in this case) and the shorter will be padded to produce this. datalist: var={&quot;1&quot;,&quot;t&quot;,&quot;w&quot;,&quot;o&quot;,&quot;
