---
title: "x2sys_cross(1)"
name: "x2sys_cross"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_cross/"
description: "x2sys_cross – Calculate crossovers between track data files"
---

<h2>NAME</h2>
<p> x2sys_cross &#8211; Calculate crossovers between track data files</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_cross</code> <i>track(s)</i> <i>TAG</i> [ <i>combi.lis</i> ] [ [<i>runtimes</i>] ] [ <code>l</code>|<code>a</code>|<code>c</code> ] [ <i>parameters</i> ] [ <code>e</code>|<code>i</code> ] [ <code>l</code>|<code>u</code>|<code>h</code><i>speed</i> ] [ [<i>level</i>] ] [ <i>size</i> ] [ ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_cross</code> is used to determine all intersections between (&quot;external cross-overs&quot;) or within (&quot;internal cross-overs&quot;) tracks (Cartesian or geographic), and report the time, position, distance along track, heading and speed along each track segment, and the crossover error (COE) and mean values for all observables. The names of the tracks are passed on the command line. By default, <code>x2sys_cross</code> will look for both external and internal COEs. As an option, you may choose to project all data using one of the map-projections prior to calculating the COE.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>tracks</i></p>
<dd> Can be one or more ASCII, native binary, or COARDS netCDF 1-D data files. To supply the data files via a text file with a list of tracks (one per record), specify the name of the track list after a leading equal-sign (e.g., =tracks.lis). If the names are missing their file extension we will append the suffix specified for this <i>TAG</i>. Track files will be searched for first in the current directory and second in all directories listed in <code>$X2SYS_HOME</code>/<i>TAG</i>/<i>TAG</i>_paths.txt (if it exists). [If <code>$X2SYS_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/x2sys]. (Note: MGD77 files will also be looked for via <code>MGD77_HOME</code>/mgd77_paths.txt and *.gmt files will be searched for via <code>$GMT_SHAREDIR</code>/mgg/gmtfile_paths).</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>combi.lis</i></p>
<dd> Only process the pair-combinations found in the file <i>combi.lis</i> [Default process all possible combinations among the specified files]. The file <i>combi.lis</i> created by <code>x2sys_get</code> -L option</p>
<dt><code>-C</code>[<i>runtimes</i>]</p>
<dd> Compute and append the processing run-time for each pair to the progress message. Append a filename to save these run-times to file. The idea here is to use the knowledge of run-times to split the main process in a number of sub-processes that can each be launched in a different processor of your multi-core machine. See the MATLAB function <i>split_file4coes.m</i> that lives in the x2sys supplement source code.</p>
<dt><code>-Il</code>|<code>a</code>|<code>c</code></p>
<dd> Sets the interpolation mode for estimating values at the crossover. Choose among: </p>
<p> <code>l</code> Linear interpolation [Default]. </p>
<p> <code>a</code> Akima spline interpolation. </p>
<p> <code>c</code> Cubic spline interpolation.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-Qe</code>|<code>i</code></p>
<dd> Append <code>e</code> for external COEs only, and <code>i</code> for internal COEs only [Default is all COEs].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option limits the COEs to those that fall inside the specified domain.</p>
<dt><code>-Sl</code>|<code>u</code>|<code>h</code><i>speed</i></p>
<dd> Defines window of track speeds. If speeds are outside this window we do not calculate a COE. Specify </p>
<p> <code>-Sl</code> sets lower speed [Default is 0]. </p>
<p> <code>-Su</code> sets upper speed [Default is Infinity]. </p>
<p> <code>-Sh</code> does not limit the speed but sets a lower speed below which headings will not be computed (i.e., set to NaN) [Default calculates headings regardless of speed].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>size</i></p>
<dd> Give the maximum number of data points on either side of the crossover to use in the spline interpolation [3].</p>
<dt><code>-Z</code></p>
<dd> Report the values of each track at the crossover [Default reports the crossover value and the mean value].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
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
<h2>REMARKS</h2>
<p> The COEs found are printed out to standard output in ASCII format (unless <code>-bo</code> is set). When ASCII is chosen, the output format depends on whether or not old-style XOVER output (<code>-L</code>) has been selected [See the <i>x_over</i> man page for more details]. If ASCII, then the first record contains the name of the tag used, the second records specifies the exact command line used for this run, and the third record contains the names of each column. For each track pair, there will be a segment header record containing the two file names and their start/stop/dist information (start/stop is absolute time or NaN if unavailable while dist is the total track length), whereas subsequent records have the data for each COE encountered. The fields written out are x, y, time along track #1 and #2, distance along track #1 and #2, heading along track #1 and #2, velocity along track #1 and #2, and then pairs of columns for each selected observable. These are either pairs of (COE, average value) for each data type (or track-values #1 and #2; see <code>-Z</code>). It is recommended that the Akima spline is used instead of the natural cubic spline, since it is less sensitive to outliers that tend to introduce wild oscillations in the interpolation.</p>
<h2>SIGN CONVENTION</h2>
<p> If track_a and track_b are passed on the command line, then the COE value is Value (track_a) &#8211; Value (track_b).</p>
<h2>PRECISION AND FORMAT</h2>
<p> The output format of individual columns are controlled by <i>FORMAT_FLOAT_OUT</i> except for geographic coordinates (<i>FORMAT_GEO_OUT</i>) and absolute calendar time (<i>FORMAT_DATE_OUT</i>, <i>FORMAT_CLOCK_OUT</i>). Make sure these are setto give you enough significant digits to achieve the desired precision.</p>
<h2>EXAMPLES</h2>
<p> To compute all internal crossovers in the gmt-formatted file c2104.gmt, and using the tag GMT, try </p>
<pre>
gmt x2sys_cross c2104.gmt -TGMT &gt; c2104.d
</pre>
<p> To find the crossover locations with bathymetry between the two MGD77 files A13232.mgd77 and A99938.mgd77, using the MGD77 tag, try </p>
<pre>
gmt x2sys_cross A13232.mgd77 A99938.mgd77 -Qe -TMGD77 &gt; crossovers.d
</pre>
<h2>REFERENCES</h2>
<p> Wessel, P. (2010), Tools for analyzing intersecting tracks: the x2sys package. <i>Computers and Geosciences</i>, <code>36</code>, 348-354. </p>
<p> Wessel, P. (1989), XOVER: A cross-over error detector for track data, <i>Computers and Geosciences</i>, <code><a href="/docs/linux/man/3-15/">15</a></code>(3), 333-346.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>x2sys_binlist</code>, <code>x2sys_init</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code>, <i>x_over</i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
