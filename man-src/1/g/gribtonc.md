---
title: "gribtonc(1)"
name: "gribtonc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gribtonc/"
description: "gribtonc – GRIB to netCDF decoder"
---

<h2>NAME</h2>
<p> gribtonc &#8211; GRIB to netCDF decoder</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code></p>
<dd>gribtonc [-l&nbsp;<wbr></code><i>logpath</i>] [-v] [-t&nbsp;<wbr><i>timeout</i>] [-e&nbsp;<wbr><i>errpath</i>] [-g&nbsp;<wbr><i>userparams.tbl</i>] [-q&nbsp;<wbr><i>qspecs</i>] <i>CDL_path</i> <i>netCDF_path</i></dl>
<h2>DESCRIPTION</h2>
<p> This program decodes GRIB products (embedded in WMO product envelopes) on the NWS High-Resolution Data Service (HRS) feed, writing the decoded products into a single netCDF output file, specified by <i>netCDF_path</i>. In case the output netCDF file does not already exist, the <i>CDL_path</i> must be supplied to specify the structure for the desired netCDF file, which <code>gribtonc</code> creates. The default parameter translation is made according to a definition by UCAR, but the user may supply specific translations in a separate file by the -g tabfile option. The user-supplied translations will override the default ones. GRIB products are converted to the units specified for the appropriate netCDF variable, if this differs from the units used for the GRIB parameter. A set of CDL files for all the model outputs appearing on the HRS data stream is provided with <code>gribtonc</code> for use in decoding HRS GRIB data. </p>
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
<p> <code>gribtonc</code> can run as a subprocess of the LDM <code><a href="/docs/linux/man/1-pqact/">pqact</a></code>(1) program, receiving a stream of GRIB products from standard input and decoding them as they arrive. <code>gribtonc</code> can also be used as a standalone decoder, decoding products on its standard input into netCDF form, as specified by <i>netCDF_file</i> GRIB products that do not conform to the specified file structure (e.g. they are defined on a different grid or contain a grid parameter not included in the specified netCDF file) are skipped. </p>
<p> To use <code>gribtonc</code> from the LDM <code><a href="/docs/linux/man/1-pqact/">pqact</a></code>(1) program requires adding entries to the <code>pqact</code> configuration file that invoke <code>gribtonc</code> on appropriate HRS products. The PIPE action should be used in pattern-action entries. The form of such an entry is:</p>
<dl>
<dt>
&nbsp;<wbr>&nbsp;<wbr>HRS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>pattern</i><tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PIPE<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>gribtonc-executable</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>gribtonc-options</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>cdl-file</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>netcdf-file</i>
</dl>
<dd>where <i>pattern</i> is a regular expression pattern matching product identifiers of products that are to be decoded and written to the output file <i>netcdf-file</i>. </p>
<p> Any directories that do not exist in <i>netcdf-file</i> will be created as needed, so date components, for example, may be part of the output file path, specified by using matched parts of the regular expression <i>pattern</i>. In case the output <i>netcdf-file</i> does not already exist, it will be created from the CDL specification in the file specified by <i>cdl-file</i>. </p>
<p> The path of the executable for <code>gribtonc</code> must be specified as the first argument to the PIPE command, and should be either an absolute path name or in a directory in the executable search path of <code>pqact</code>. </p>
<p> An example <code>pqact.conf</code> entry for decoding GRIB products from the ETA model as they appear on the HRS data stream is:</p>
<dl>
<dt> # ETA model on Lambert conformal grid to yyyymmddhh_eta.nc</p>
<dd>HRS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>^Y.Q&#8230; KWBC (..)(..).*/mETA<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PIPE<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/local/ldm/decoders/gribtonc<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>etc/eta.cdl<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>data/GRIB/(1:yyyy)(1:mm)12_eta.nc
</dl>
<p> Since <code>gribtonc</code> reads GRIB products from its standard input, it may be invoked independently of <code><a href="/docs/linux/man/1-pqact/">pqact</a></code>(1) by using I/O redirection.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l </code><i>logpath</i></p>
<dd> Log file pathname. The program uses Unidata&#8217;s <code><a href="/docs/linux/man/3-ulog/">ulog</a></code>(3) package to write error and log messages. The default is to write to the <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) daemon. If this option is specified, however, then messages will be written to the file <i>logpath</i> unless that pathname is &quot;-&quot;, in which case all messages will be written to standard error.</p>
<dt><code>-v</code></p>
<dd> Verbose logging. Informative messages (level <code>LOG_INFO</code>) are logged, including a line for each GRIB product decoded. By default, only messages of severity <code>LOG_NOTICE</code> and greater are logged.</p>
<dt><code>-t</code><i> timeout</i></p>
<dd> Timeout in seconds (default is 600). If there has been no input available on stdin for the duration of the specified timeout, the program exits gracefully.</p>
<dt><code>-e</code><i> errpath</i></p>
<dd> If a GRIB product cannot be decoded, perhaps because it is truncated or otherwise corrupted, it is appended to this file.</p>
<dt><code>-g</code><i> tabfile</i></p>
<dd> Use GRIB-netcdf translation defined in this file. The format of this file is described below.</p>
<dt><code>-q</code><i> qspecs</i></p>
<dd> Specification for how to expand so-called quasi-regular or thinned grids into rectangular grids. This argument is a comma-delimited text string that specifies the method of interpolation used (currently <code>lin</code> for linear or <code>cub</code> for cubic), and the latitude and longitude increments in degrees for the resulting grid (e.g. <code>dlat=2.5,dlon=5.0</code>).</p>
<dt><code>CDL_path</code></p>
<dd> The path name of a file to be used as a template for the netCDF file, if the netCDF file specified as output does not exist. If the netCDF output file does exist, this argument is ignored. A path name relative to the directory specified by the LDM_ETCDIR environment variable may be used, but you must make sure this environment variable is defined in <code>gribtonc</code></p>
<dt><code>netCDF_path</code></p>
<dd> The path name of the netCDF output file. This may be specified as an absolute path name or (more typically) relative to the directory from which <code>gribtonc</code> is invoked. Directories that do not exist in the path name of the output file will be created as needed. </p>
</dl>
<h2>EXAMPLE</h2>
<p> The command</p>
<dl>
<dt>
<dd>
<pre>
gribtonc -v -l- -q &quot;lin,dlat=2.5,dlon=5.0&quot; avn-x.cdl avn-x.nc &lt; avn-x.wmo
</pre>
</dl>
<p> will decode the products in avn-x.wmo into the netCDF file avn-x.nc, creating the latter file if it does not already exist from the ASCII CDL template file avn-x.cdl. If the data contain quasi-regular grids, they will be expanded to full regular grids on a 2.5 by 5.0 degree grid before being written into the output file.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gribdump/">gribdump</a>(1), <a href="/docs/linux/man/3-netcdf/">netcdf</a>(3), <a href="/docs/linux/man/1-pqact/">pqact</a>(1), <a href="/docs/linux/man/3-udunits/">udunits</a>(3), <a href="/docs/linux/man/3-ulog/">ulog</a>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages and log messages are written to the log file. </p>
<h2>Index</h2>
