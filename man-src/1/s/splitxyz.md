---
title: "splitxyz(1)"
name: "splitxyz"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splitxyz/"
description: "splitxyz – Split xyz[dh] data tables into individual segments"
---

<h2>NAME</h2>
<p> splitxyz &#8211; Split xyz[dh] data tables into individual segments</p>
<h2>SYNOPSIS</h2>
<p> <code>splitxyz</code> [ <i>table</i> ] [ <i>azimuth</i>/<i>tolerance</i> ] [ <i>course_change</i>] [ <i>minimum_distance</i> ] [ <i>xy_filter</i>/<i>z_filter</i> ] [ <i>template</i> ] [ <i>flags</i> ] [ ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>splitxyz</code> reads a series of (x,y[,z]) records [or optionally (x,y,z,d,h); see <code>-S</code> option] from standard input [or <i>xyz[dh]file</i>] and splits this into separate lists of (x,y[,z]) series, such that each series has a nearly constant azimuth through the x,y plane. There are options to choose only those series which have a certain orientation, to set a minimum length for series, and to high- or low-pass filter the z values and/or the x,y values. <code>splitxyz</code> is a useful filter between data extraction and <code>pswiggle</code> plotting, and can also be used to divide a large x,y[,z] dataset into segments.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> none.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files with 2, 3, or 5 columns holding (x,y,[z[,d,h]]) data values. To use (x,y,z,d,h) input, sorted so that d is non-decreasing, specify the <code>-S</code> option; default expects (x,y,z) only. If no files are specified, <code>splitxyz</code> will read from standard input.</p>
<dt><code>-A</code><i>azimuth</i>/<i>tolerance</i></p>
<dd> Write out only those segments which are within +/- <i>tolerance</i> degrees of <i>azimuth</i> in heading, measured clockwise from North, [0 &#8211; 360]. [Default writes all acceptable segments, regardless of orientation].</p>
<dt><code>-C</code><i>course_change</i></p>
<dd> Terminate a segment when a course change exceeding <i>course_change</i> degrees of heading is detected [ignore course changes].</p>
<dt><code>-D</code><i>minimum_distance</i></p>
<dd> Do not write a segment out unless it is at least <i>minimum_distance</i> units long [0]</p>
<dt><code>-F</code><i>xy_filter</i>/<i>z_filter</i></p>
<dd> Filter the z values and/or the x,y values, assuming these are functions of d coordinate. <i>xy_filter</i> and <i>z_filter</i> are filter widths in distance units. If a filter width is zero, the filtering is not performed. The absolute value of the width is the full width of a cosine-arch low-pass filter. If the width is positive, the data are low-pass filtered; if negative, the data are high-pass filtered by subtracting the low-pass value from the observed value. If <i>z_filter</i> is non-zero, the entire series of input z values is filtered before any segmentation is performed, so that the only edge effects in the filtering will happen at the beginning and end of the complete data stream. If <i>xy_filter</i> is non-zero, the data is first divided into segments and then the x,y values of each segment are filtered separately. This may introduce edge effects at the ends of each segment, but prevents a low-pass x,y filter from rounding off the corners of track segments. [Default = no filtering].</p>
<dt><code>-N</code><i>template</i></p>
<dd> Write each segment to a separate output file [Default writes a multiple segment file to stdout]. Append a format template for the individual file names; this template <code>must</code> contain a C format specifier that can format an integer argument (the running segment number across all tables); this is usually %d but could be %08d which gives leading zeros, etc. [Default is splitxyz_segment_%d.{txt|bin}, depending on <code>-bo</code>]. Alternatively, give a template with two C format specifiers and we will supply the table number and the segment number within the table to build the file name.</p>
<dt><code>-Q</code><i>flags</i></p>
<dd> Specify your desired output using any combination of <i>xyzdh</i>, in any order. Do not space between the letters. Use lower case. The output will be ASCII (or binary, see <code>-bo</code>) columns of values corresponding to <i>xyzdh</i> [Default is <code>-Q</code><i>xyzdh</i> (<code>-Q</code><i>xydh</i> if only 2 input columns)].</p>
<dt><code>-S</code></p>
<dd> Both d and h are supplied. In this case, input contains x,y,z,d,h. [Default expects (x,y,z) input, and d,h are computed from delta x, delta y. Use <code>-fg</code> to indicate map data; then x,y are assumed to be in degrees of longitude, latitude, distances are considered to be in kilometers, and angles are actually azimuths. Otherwise, distances are Cartesian in same units as x,y and angles are counter-clockwise from horizontal].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2, 3, or 5 input columns as set by <code>-S</code>].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 1-5 output columns as set by <code>-Q</code>].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks. Do not let a segment have a gap exceeding <i>gap</i>; instead, split it into two segments. [Default ignores gaps].</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>DISTANCE CALCULATIONS</h2>
<p> The type of input data is dictated by the <code>-f</code> option. If <code>-fg</code> is given then x,y are in degrees of longitude, latitude, distances are in kilometers, and angles are azimuths. Otherwise, distances are Cartesian in same units as x,y and angles are counter-clockwise from horizontal.</p>
<h2>EXAMPLES</h2>
<p> Suppose you want to make a wiggle plot of magnetic anomalies on segments oriented approximately east-west from a NGDC-supplied cruise called JA020015 in the region <code>-R</code>300/315/12/20. You want to use a 100 km low-pass filter to smooth the tracks and a 500km high-pass filter to detrend the magnetic anomalies. Try this: </p>
<pre>
gmt mgd77list JA020015 -R300/315/12/20 -Flon,lat,mag,dist,azim | gmt splitxyz -A90/15 -F100/-500 \
    -D100 -S -V -fg | gmt pswiggle -R300/315/12/20 -Jm0.6i -Baf -B+tJA020015 -T1 \
    -W0.75p -Ggray -Z200 &gt; JA020015_wiggles.ps
</pre>
<p> MGD-77 users: For this application we recommend that you extract dist,azim from <code>mgd77list</code> rather than have <code>splitxyz</code> compute them separately. </p>
<p> Suppose you have been given a binary, double-precision file containing lat, lon, gravity values from a survey, and you want to split it into profiles named <i>survey</i>_<i>###.txt</i> (when gap exceeds 100 km). Try this: </p>
<pre>
gmt splitxyz survey.bin -Nsurvey_%03d.txt -V -gd100k -D100 -: -fg -bi3d
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>filter1d</code>, <code>mgd77list</code>, <code>pswiggle</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
