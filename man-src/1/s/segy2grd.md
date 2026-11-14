---
title: "segy2grd(1)"
name: "segy2grd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-segy2grd/"
description: "segy2grd – Converting SEGY data to a GMT grid"
---

<h2>NAME</h2>
<p> segy2grd &#8211; Converting SEGY data to a GMT grid</p>
<h2>SYNOPSIS</h2>
<p> <code>segy2grd</code> <i>segyfile</i> <i>grdfile</i> <i>increment</i> <i>region</i> [ [<code>n</code>|<code>z</code>] ] [ <i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>title</i>/<i>remark</i> ] [ [<i>nsamp</i>] ] [ [<i>ntraces</i>] ] [ <i>nodata</i> ] [ <i>&lt;mode&gt;&lt;value&gt;</i> ] [ [<i>header</i>] ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>segy2grd</code> reads an IEEE SEGY file and creates a binary grid file. Either a simple mapping (equivalent to xyz2grd -Z) or a more complicated averaging where a particular grid cell includes values from more than one sample in the SEGY file can be done. <code>segy2grd</code> will report if some of the nodes are not filled in with data. Such unconstrained nodes are set to a value specified by the user [Default is NaN]. Nodes with more than one value will be set to the average value.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> <i>segyfile</i> is an IEEE floating point SEGY file. Traces are all assumed to start at 0 time/depth.</p>
<dl>
<dt><code>-G</code><i>grdfile</i></p>
<dd> <i>grdfile</i> is the name of the binary output grid file.</p>
<dt><code>-I</code></p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Append <code>m</code> to indicate minutes or <code>s</code> to indicate seconds.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>n</code>|<code>z</code>]</p>
<dd> Add up multiple values that belong to the same node (same as <code>-Az</code>). Append <code>n</code> to simply count the number of data points that were assigned to each node. [Default (no <code>-A</code> option) will calculate mean value]. Not used for simple mapping.</p>
<dt><code>-D</code><i>xname</i>/<i>yname</i>/<i>zname</i>/<i>scale</i>/<i>offset</i>/<i>invalid</i>/<i>title</i>/<i>remark</i></p>
<dd> Give values for <i>xname</i>, <i>yname</i>, <i>zname</i> (give the names of those variables and in square bracket their units, e.g., &quot;distance [km]&quot;), <i>scale</i> (to multiply grid values after read [normally 1]), <i>offset</i> (to add to grid after scaling [normally 0]), <i>invalid</i> (a value to represent missing data [NaN]), <i>title</i> (anything you like), and <i>remark</i> (anything you like). To leave some of these values untouched, leave field blank. Empty fields in the end may be skipped. Alternatively, to allow &quot;/&quot; to be part of one of the values, use any non-alphanumeric character (and not the equal sign) as separator by both starting and ending with it. For example: <code>-D</code>:<i>xname</i>:<i>yname</i>:<i>zname</i>:<i>scale</i>:<i>offset</i>:<i>invalid</i>:<i>title</i>:<i>remark</i>: Use quotes to group texts with more than one word. Note that for geographic grids (<code>-fg</code>) <i>xname</i> and <i>yname</i> are set automatically.</p>
<dt><code>-L</code></p>
<dd> Let <i>nsamp</i> override number of samples in each trace.</p>
<dt><code>-M</code>[<i>ntraces</i>]</p>
<dd> Fix number of traces to read in. Default tries to read 10000 traces. <code>-M</code>0 will read number in binary header, <code>-M</code><i>ntraces</i> will attempt to read only <i>n</i> traces.</p>
<dt><code>-N</code><i>nodata</i></p>
<dd> No data. Set nodes with no input sample to this value [Default is NaN].</p>
<dt><code>-Q</code><i>&lt;mode&gt;&lt;value&gt;</i></p>
<dd>
<dt><code>Can be used to change two different settings depending on </code><i>mode</i>:</p>
<dd> <code>-Qx</code><i>x-scale</i> applies scalar <i>x-scale</i> to coordinates in trace header to match the coordinates specified in -R. </p>
<p> <code>-Qy</code><i>s_int</i> specifies sample interval as <i>s_int</i> if incorrect in the SEGY file.</p>
<dt><code>-S</code>[<i>header</i>]</p>
<dd> Set variable spacing; <i>header</i> is <code>c</code> for cdp, <code>o</code> for offset, or <code>b</code><i>number</i> for 4-byte float starting at byte <i>number</i>. If <code>-S</code> not set, assumes even spacing of samples at the <i>x_inc, y_inc</i> supplied with <code>-I</code>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
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
<h2>EXAMPLES</h2>
<p> To create a grid file from an even spaced SEGY file test.segy, try </p>
<pre>
gmt segy2grd test.segy -I0.1/0.1 -Gtest.nc -R198/208/18/25 -V
</pre>
<p> Note that this will read in 18-25s (or km) on each trace, but the first trace will be assumed to be at X=198 </p>
<p> To create a grid file from the SEGY file test.segy, locating traces according to the CDP number, where there are 10 CDPs per km and the sample interval is 0.1, try </p>
<pre>
gmt segy2grd test.segy -Gtest.nc -R0/100/0/10 -I0.5/0.2 -V -Qx0.1 -Qy0.1
</pre>
<p> Because the grid interval is larger than the SEGY file sampling, the individual samples will be averaged in bins</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grd2xyz</code>, <code>grdedit</code>, <code>pssegy</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
