---
title: "x2sys_datalist(1)"
name: "x2sys_datalist"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_datalist/"
description: "x2sys_datalist – Extract content of track data files"
---

<h2>NAME</h2>
<p> x2sys_datalist &#8211; Extract content of track data files</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_datalist</code> <i>track(s)</i> <code>-T</code><i>TAG</i> [ ] [ ] [ <i>name1</i>,<i>name2</i>,&#8230;) ] [ [<i>list</i>] ] [ [<i>corrtable</i>] ] [ <i>region</i> ] [ ] [ [ [<i>level</i>] ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_datalist</code> reads one or more files and produces a single ASCII [or binary] table. The files can be of any format, which must be described and passed with the option. You may limit the output to a geographic region, and insist that the output from several files be separated by a multiple segment header. Only the named data fields will be output [Default selects all columns].</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>tracks</i></p>
<dd> Can be one or more ASCII, native binary, or COARDS netCDF 1-D data files. To supply the data files via a text file with a list of tracks (one per record), specify the name of the track list after a leading equal-sign (e.g., =tracks.lis). If the names are missing their file extension we will append the suffix specified for this <i>TAG</i>. Track files will be searched for first in the current directory and second in all directories listed in <code>$X2SYS_HOME</code>/<i>TAG</i>/<i>TAG</i>_paths.txt (if it exists). [If <code>$X2SYS_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/x2sys]. (Note: MGD77 files will also be looked for via <code>MGD77_HOME</code>/mgd77_paths.txt and *.gmt files will be searched for via <code>$GMT_SHAREDIR</code>/mgg/gmtfile_paths).</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Eliminate COEs by distributing the COE between the two tracks in proportion to track weight. These (dist, adjustment) spline knots files for each track and data column are called <i>track.column</i>.adj and are expected to be in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory. The adjustments are only applied if the corresponding adjust file can be found [No residual adjustments]</p>
<dt><code>-E</code></p>
<dd> Enhance ASCII output by writing GMT segment headers between data from each track [no segment headers].</p>
<dt><code>-F</code><i>name1</i>,<i>name2</i>,&#8230;)</p>
<dd> Give a comma-separated sub-set list of column names defined in the definition file. [Default selects all data columns].</p>
<dt><code>-I</code>[<i>list</i>]</p>
<dd> Name of ASCII file with a list of track names (one per record) that should be excluded from consideration [Default includes all tracks].</p>
<dt><code>-L</code>[<i>corrtable</i>]</p>
<dd> Apply optimal corrections to columns where such corrections are available. Append the correction table to use [Default uses the correction table <i>TAG</i>_corrections.txt which is expected to reside in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory]. For the format of this file, see CORRECTIONS below.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option limits the COEs to those that fall inside the specified domain.</p>
<dt><code>-S</code></p>
<dd> Suppress output records where all the data columns are NaN [Default will output all records].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
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
<p> To extract all data from the old-style MGG supplement file c2104.gmt, recognized by the tag GMT: </p>
<pre>
gmt x2sys_datalist c2104.gmt -TGMT &gt; myfile
</pre>
<p> To make lon,lat, and depth input for <code>blockmean</code> and <code>surface</code> using all the files listed in the file tracks.lis and define by the tag TRK, but only the data that are inside the specified area, and make output binary, run </p>
<pre>
gmt x2sys_datalist =tracks.lis -TTRK -Fon,lat,depth -R40/-30/25/35 -bo &gt; alltopo_bin.xyz
</pre>
<h2>CORRECTIONS</h2>
<p> The correction table is an ASCII file with coefficients and parameters needed to carry out corrections. This table is usually produced by <code>x2sys_solve</code>. Comment records beginning with # are allowed. All correction records are of the form </p>
<p> <i>trackID observation correction</i> </p>
<p> where <i>trackID</i> is the track name, <i>observation</i> is one of the abbreviations for an observed field contained in files under this TAG, and <i>correction</i> consists of one or more white-space-separated <i>term</i>s that will be <code>subtracted</code> from the observation before output. Each <i>term</i> must have this exact syntax: </p>
<p> <i>factor</i>[*[<i>function</i>]([<i>scale</i>](<i>abbrev</i>[-<i>origin</i>]))[^<i>power</i>]] </p>
<p> where terms in brackets are optional (the brackets themselves are not used but regular parentheses must be used exactly as indicated). No spaces are allowed except between <i>term</i>s. The <i>factor</i> is the amplitude of the basis function, while the optional <i>function</i> can be one of sin, cos, or exp. The optional <i>scale</i> and <i>origin</i> can be used to translate the argument (before giving it to the optional function). The argument <i>abbrev</i> is one of the abbreviations for columns known to this TAG. However, it can also be one of the three auxiliary terms <code>dist</code> (for along-track distances), <code>azim</code> for along-track azimuths, and <code>vel</code> (for along-track speed); these are all sensitive to the <code>-C</code> and <code>-N</code> settings used when defining the TAB; furthermore, <code>vel</code> requires <code>time</code> to be present in the data. If <i>origin</i> is given as <code>T</code> it means that we should replace it with the value of <i>abbrev</i> for the very first record in the file (this is usually only done for <i>time</i>). If the first data record entry is NaN we revert <i>origin</i> to zero. Optionally, raise the entire expression to the given <i>power</i>, before multiplying by <i>factor</i>. The following is an example of fictitious corrections to the track ABC, implying the <code>z</code> column should have a linear trend removed, the field <code>obs</code> should be corrected by a strange dependency on latitude, <code>weight</code> needs to have 1 added (hence correction is given as -1), and <code>fuel</code> should be reduced by a linear distance term: </p>
<p> ABC z 7.1 1e-4*((time-T)) </p>
<p> ABC obs 0.5*exp(-1e-3(lat))^1.5 </p>
<p> ABC weight -1 </p>
<p> ABC fuel 0.02*((dist))</p>
<h2>SEE ALSO</h2>
<p> <code>blockmean</code>, <code>gmt</code>, <code>surface</code>, <code>x2sys_init</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
