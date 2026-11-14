---
title: "netcdfperl(1)"
name: "netcdfperl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netcdfperl/"
description: "netCDFPerl – perl extension for netCDF dataset access"
---

<p>netCDFPerl &#8211; perl extension for netCDF dataset access</p>
<h2>Synopsis</h2>
<pre>use netCDF;
NetCDF::create(&quot;foo.nc&quot;, NetCDF::CLOBBER);
...</pre>
<h2>Description</h2>
<p><code>netCDFPerl</code> is a Perl 5 extension-module interface to the services provided by the netCDF version 2 API, <a href="/docs/linux/man/3-netcdf2/">netcdf2</a>(3). </p>
<p> The functions in the netCDF version 2 library can be accessed by a Perl 5 script by replacing the `<code>nc</code>&#8216; prefix of the regular netCDF version 2 C function names with <code>NetCDF::</code>. For example, the C function <code>nccreate()</code> is available to a perl script as <code>NetCDF::create</code>. </p>
<p> Each perl function matches, as closely as possible and necessary, its C counterpart:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>The number, order, and semantics of the arguments are identical. Note, however, that it is not necessary to specify the number of elements in an array because perl arrays carry that information.</p>
<dt>*</p>
<dd>The behavior is the same in terms of the netCDF dataset.</p>
<dt>*</p>
<dd>A value of <code>-1</code> is returned to indicate an error.</dl>
</dl>
<p> Scalar argument types are mapped in an obvious way: </p>
<dl COMPACT>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center>C</td>
<td ALIGN=center>Perl 5
</td>
</tr>
<tr VALIGN=top>
<td>char *</td>
<td>string
</td>
</tr>
<tr VALIGN=top>
<td>char</td>
<td>integer
</td>
</tr>
<tr VALIGN=top>
<td>short</td>
<td>integer
</td>
</tr>
<tr VALIGN=top>
<td>int</td>
<td>integer
</td>
</tr>
<tr VALIGN=top>
<td>nclong</td>
<td>integer
</td>
</tr>
<tr VALIGN=top>
<td>long</td>
<td>integer
</td>
</tr>
<tr VALIGN=top>
<td>float</td>
<td>double
</td>
</tr>
<tr VALIGN=top>
<td>double</td>
<td>double
</td>
</tr>
</table>
</dl>
<p> The individual elements of an array argument are similarly mapped. </p>
<p> Array arguments themselves are passed by reference for both input and output. For example, the following Perl 5 code will write and then read a hyperslab of values: </p>
<dl COMPACT>
<dd>
<pre>@start = (0, 0, 0);
@count = (1, 2, 3);
@out = (1, 2, 3, 4, 5, 6);
NetCDF::varput($ncid, $varid, @start, @count, @out);
NetCDF::varget($ncid, $varid, @start, @count, @in);</pre>
</dl>
<p> (The above assumes that <code>$ncid</code> and <code>$varid</code> have been appropriately set.) After this code is executed, the array <code>@in</code> will have the same values as the array <code>@out</code>. The previous contents, if any, of an array used for input are destroyed (e.g. <code>@in</code> in the above example). </p>
<p> To define a scalar variable with <code>NetCDF::vardef()</code>, use an empty dimension-ID array, e.g. </p>
<dl COMPACT>
<dd>NetCDF::vardef($ncid, &quot;scalar_variable&quot;, NetCDF::FLOAT, \());</dl>
<p> The interface doesn&#8217;t support null arguments. One cannot use a void pointer to indicate that no value is requested for a particular argument: all arguments must be present. </p>
<p> For technical reasons, output variables must be initialized, i.e. any variable argument that is to have its value set by a function must already have a value. For example, if the first occurrence of the variable <code>$attval</code> is in the following: </p>
<dl COMPACT>
<dd>
<pre>NetCDF::attget($ncid, NetCDF::GLOBAL, &quot;history&quot;, \$attval);</pre>
</dl>
<p> then a core dump will probably result. The solution is to initialize the variable before using it: </p>
<dl COMPACT>
<dd>
<pre>$attval=&quot;&quot;;
NetCDF::attget($ncid, NetCDF::GLOBAL, &quot;history&quot;, \$attval);</pre>
</dl>
<p> Two additional functions are provided for error handling. <code>NetCDF::opts(i)</code> determines the handling of errors by setting the <code>ncopts</code> variable to <code>i</code>. It returns the previous value. <code>NetCDF::err()</code> returns the value of the error code variable, <code>ncerr</code>. </p>
<p> In addition to the above functions, most C macro constants that are defined in the netCDF header file <code>netcdf.h</code> are also available to a perl script by dropping any `<code>NC_</code>&#8216; substring and using the <code>NetCDF::</code> prefix, e.g. <code>NetCDF::LONG</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/3-netcdf2/">netcdf2</a></code>(3)</p>
