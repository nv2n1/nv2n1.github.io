---
title: "nc2xy(1)"
name: "nc2xy"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nc2xy/"
description: "nc2xy – Converting netCDF column file(s) to ASCII xy data"
---

<h2>NAME</h2>
<p> nc2xy &#8211; Converting netCDF column file(s) to ASCII xy data</p>
<h2>SYNOPSIS</h2>
<p> <code>nc2xy</code> <i>files</i> [ <code>-F</code><i>var1/var2/&#8230;</i> ] [ <code>-S</code>[<code>r</code>] ] [ <code>-V</code> ] [ <code>-f</code><i>colinfo</i> ] [ <code>-b</code><code>o</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nc2xy</code> reads one or more netCDF files with column data and writes out those columns in ASCII format to standard output, so that they can be used by <code>psxy</code>, <code>psxyz</code>, or <code>xyz2grd</code>. Modify the precision of the ASCII output format by editing the <code>D_FORMAT</code> parameter in your .gmtdefaults4 file or use <code>&#8211;D_FORMAT</code>=<i>value</i> on the command line.</p>
<dl>
<dt><i>files</i></p>
<dd> Names of netCDF files to be converted.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code></p>
<dd> Specify up to 10 names of the variables (separated by slashes) to be printed out. All variables to be 1-dimensional and be of equal length. When omited, the first two variables in the netCDF file will be printed.</p>
<dt><code>-S</code></p>
<dd> Suppress output for records with one or more NaN values [Default outputs all nodes]. Append <code>r</code> to reverse the suppression, i.e., only output the records with at least one NaN value.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-bo</code></p>
<dd> Selects binary output. Append <code>s</code> for single precision [Default is <code>d</code> (double)]. Uppercase <code>S</code> or <code>D</code> will force byte-swapping. Optionally, append <i>ncol</i>, the number of desired columns in your binary output file.</p>
<dt><code>-f</code></p>
<dd> Special formatting of input and/or output columns (time or geographical data). Specify <code>i</code> or <code>o</code> to make this apply only to input or output [Default applies to both]. Give one or more columns (or column ranges) separated by commas. Append <code>T</code> (absolute calendar time), <code>t</code> (relative time in chosen <code>TIME_UNIT</code> since <code>TIME_EPOCH</code>), <code>x</code> (longitude), <code>y</code> (latitude), or <code>f</code> (floating point) to each column or column range item. Shorthand <code>-f</code>[<code>i</code>|<code>o</code>]<code>g</code> means <code>-f</code>[<code>i</code>|<code>o</code>]0<code>x</code>,1<code>y</code> (geographic coordinates). See also <code>TIME COORDINATES</code> below.</dl>
<h2>TIME COORDINATES</h2>
<p> Time coordinates in netCDF files will be recognized as such. The variable&#8217;s <code>unit</code> attribute is parsed to determine the unit and epoch of the time coordinate in the grid. Values are then converted to the internal time system specified by <code>TIME_UNIT</code> and <code>TIME_EPOCH</code> in the .gmtdefaults file or on the command line. The default output is relative time in that time system, or absolute time when using the option <code>-f0T</code>, <code>-f1T</code>, etc.</p>
<h2>EXAMPLES</h2>
<p> To print out latitude, longitude and height in a netCDF file as ASCII records, while suppressing all NaN values: </p>
<p> <code>nc2xy</code> <code>-F</code>lat/lon/height <code>-S</code> trackfile.nc &gt; trackfile.xy</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmtdefaults/">gmtdefaults</a></i>(1), <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-psxy/">psxy</a></i>(1), <i><a href="/docs/linux/man/1-psxyz/">psxyz</a></i>(1), <i><a href="/docs/linux/man/1-xyz2grd/">xyz2grd</a></i>(1) </p>
<h2>Index</h2>
