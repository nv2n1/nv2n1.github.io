---
title: "gribtocdl(1)"
name: "gribtocdl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gribtocdl/"
description: "gribtocdl – create netCDF CDL-file from GRIB dataset"
---

<h2>NAME</h2>
<p> gribtocdl &#8211; create netCDF CDL-file from GRIB dataset</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code></p>
<dd>gribtocdl [-v] [-g&nbsp;<wbr></code><i>tabfile</i>] [-q&nbsp;<wbr><i>qspecs</i>] <i>gribfiles</i></dl>
<h2>DESCRIPTION</h2>
<p> This program decodes GRIB products and generates to stdout the corresponding CDL code that can be used in <code><a href="/docs/linux/man/1-gribtonc/">gribtonc</a></code>(1) to convert the GRIB products to netCDF format. The default parameter translation is made according to a definition by UCAR, but the user may supply specific translations in a separate file by the -g tabfile option. The user-supplied translations will override the default ones. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Verbose, reports decoding steps to stderr.</p>
<dt><code>-g</code><i> tabfile</i></p>
<dd> Use GRIB-netcdf translation defined in this file. The format of this file is described below.</p>
<dt><code>-q</code><i> qspecs</i></p>
<dd> Specification for how to expand so-called quasi-regular or thinned grids into rectangular grids. This argument is a comma-delimited text string that specifies the method of interpolation used (currently <code>lin</code> for linear or <code>cub</code> for cubic), and the latitude and longitude increments in degrees for the resulting grid (e.g. <code>dlat=2.5,dlon=5.0</code>). </p>
</dl>
<h2>FORMAT OF GRIB TO NETCDF TRANSLATION TABLE</h2>
<p> The format of the translation table is as follows: Each line contains</p>
<dl>
<dt>
<dd>
<pre>
GRIB parameter number
netCDF parameter name (cannot start with digit, [A-Za-z0-9_] only )
netCDF long description
netCDF units
An optional comment
</pre>
</dl>
<p> These are all separated by semicolon (&quot;;&quot;). To comment a whole line, put any letter or special character (i.e. not a digit) in front of it. Trailing spaces are ignored before each semicolon, but not after. The GRIB number may have spaces in front. Parameters found in the separate file take presidence over the default parameter table, those not listed in the separate file are unchanged. All parameters will be named with a level suffix in addition to the name assigned in the separate file. </p>
<h2>EXAMPLE</h2>
<p> The command</p>
<dl>
<dt>
<dd>
<pre>
gribtocdl -v -g my.tab sst.grib &gt; sst.cdl
</pre>
</dl>
<p> will decode the products in sst.grib and generate the corresponding CDL code into file sst.cdl. The file my.tab contains a specific conversion table to be used when naming a parameter from GRIB. Later the GRIB file may be converted to netCDF by using gribtonc:</p>
<dl>
<dt>
<dd>
<pre>
gribtonc -v -g my.tab sst.cdl sst.nc &lt; sst.grib
</pre>
</dl>
<p> The file my.tab looks like this:</p>
<dl>
<dt>
<dd>
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
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gribdump/">gribdump</a>(1), <a href="/docs/linux/man/1-gribtonc/">gribtonc</a>(1), <a href="/docs/linux/man/3-netcdf/">netcdf</a>(3), <a href="/docs/linux/man/3-udunits/">udunits</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages and log messages are written to stderr. </p>
<h2>Index</h2>
