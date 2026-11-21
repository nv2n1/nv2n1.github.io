---

title: "gribdump(1)"
name: "gribdump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gribdump/"
description: "gribdump – Decode GRIB products and display as text"
---

<p> gribdump &#8211; Decode GRIB products and display as text</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code></dt>
<dd>gribdump [-h] [-b] [-p&nbsp;<wbr></code><i>precision</i>] [-e&nbsp;<wbr><i>errpath</i>] [-g&nbsp;<wbr><i>tabfile</i>] [-q&nbsp;<wbr><i>qspecs</i>] [<i>files &#8230;</i>]</dd></dl>
<h2>DESCRIPTION</h2>
<p> This program decodes GRIB products (embedded in WMO product envelopes) on the NWS High-Resolution Data Service (HRS) feed, writing textual representations of the products or summaries of the products to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Headers only. Information from the Product Description Section and Grid Description Section is output, but no data values are output. The default is to output both headers and data values.</dd>
<dt><code>-b</code></dt>
<dd> Brief output. Only one line is output for each product, providing summary information of the parameter, grid, model, levels, time ranges, and other information.</dd>
<dt><code>-p</code><i> precision</i></dt>
<dd> Precision used for printing floating-point values, if other than the 7-significant figure default is desired.</dd>
<dt><code>-e</code><i> errpath</i></dt>
<dd> If a GRIB product cannot be decoded, perhaps because it is truncated or otherwise corrupted, it is appended to this file. </dd>
<dt><code>-g</code><i> tabfile</i></dt>
<dd> Use GRIB-netcdf translation defined in this file. The format of this file is:</dd></dl>
<pre><code>
Grib;
netCDF;
long name;
units;
comments 31;
CI;
Sea - ice cover;
none;
(0 - 1)34;
SSTK;
Sea surface temperature;
K;
151;
MSL;
Mean sea - level pressure;
Pa;
167;
T2M;
2 metre temperature;
K;
</code></pre>
<dl>
<dt><code>-q</code><i> qspecs</i></dt>
<dd> Specification for how to expand so-called quasi-regular or thinned grids into rectangular grids. This argument is a comma-delimited text string that specifies the method of interpolation used (currently <code>lin</code> for linear or <code>cub</code> for cubic), and the latitude and longitude increments in degrees for the resulting grid (e.g. <code>dlat=2.5,dlon=5.0</code>).</dd>
<dt><i>files</i></dt>
<dd> The path name of one or more files of GRIB products used as input. If no filenames are provided, GRIB products are read from standard input.</dd></dl>
<h2>EXAMPLE</h2>
<p> The command</p>
<dl>
<dt>
</dt><dd>
<pre>
gribdump -q &quot;lin,dlat=2.5,dlon=5.0&quot; avn-x.wmo
</pre>
</dd></dl>
<p> will decode and display values for the products in avn-x.wmo If the data contain quasi-regular grids, they will be expanded to full regular grids on a 2.5 by 5.0 degree grid before being written into the output file.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gribtonc/">gribtonc</a>(1), <a href="/docs/linux/man/3-netcdf/">netcdf</a>(3), pqact(1), udunits(3), ulog(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages and log messages are written to the log file. </p>
