---
title: "gmtconnect(1)"
name: "gmtconnect"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtconnect/"
description: "gmtconnect – Connect individual lines whose end points match within tolerance"
---

<h2>NAME</h2>
<p> gmtconnect &#8211; Connect individual lines whose end points match within tolerance</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtconnect</code> [ <i>table</i> ] [ [<i>closed</i>] ] [ [<i>template</i>] ] [ [<i>linkfile</i>] ] [ [<i>template</i>] ] [ [<i>cutoff</i>[<i>unit</i>][/<i>nn_dist</i>]] ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtconnect</code> reads standard input or one or more data files, which may be multisegment files, and examines the coordinates of the end points of all line segments. If a pair of end points are identical or closer to each other than the specified separation tolerance then the two line segments are joined into a single segment. The process repeats until all the remaining endpoints no longer pass the tolerance test; the resulting segments are then written out to standard output or specified output file. If it is not clear what the separation tolerance should be then use <code>-L</code> to get a list of all separation distances and analyze them to determine a suitable cutoff.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-C</code>[<i>closed</i>]</p>
<dd> Write all the closed polygons to <i>closed</i> [gmtconnect_closed.txt] and all other segments as they are to stdout. No connection takes place. Use <code>-T</code><i>cutoff</i> to set a minimum separation [0], and if <i>cutoff</i> is &gt; 0 then we also explicitly close the polygons on output.</p>
<dt><code>-D</code>[<i>template</i>]</p>
<dd> For multiple segment data, dump each segment to a separate output file [Default writes a single multiple segment file]. Append a format template for the individual file names; this template <code>must</code> contain a C format specifier that can format an integer argument (the segment number); this is usually %d but could be %08d which gives leading zeros, etc. Optionally, it may also contain the format %c <i>before</i> the integer; this will then be replaced by C (closed) or O (open) to indicate segment type. [Default is gmtconnect_segment_%d.txt]. Note that segment headers will be written in either case. For composite segments, a generic segment header will be written and the segment headers of individual pieces will be written out as comments to make it possible to identify where the connected pieces came from.</p>
<dt><code>-L</code>[<i>linkfile</i>]</p>
<dd> Writes the link information to the specified file [gmtconnect_link.txt]. For each segment we write the original segment id, and for the beginning and end point of the segment we report the id of the closest segment, whether it is the beginning (B) or end (E) point that is closest, and the distance between those points in units determined by <code>-T</code>.</p>
<dt><code>-Q</code>[<i>template</i>]</p>
<dd> Used with <code>-D</code> to a list file with the names of the individual output files. Optionally, append a filename template for the individual file names; this template <code>may</code> contain a C format specifier that can format an character (C or O for closed or open, respectively). [Default is gmtconnect_list.txt].</p>
<dt><code>-T</code>[<i>cutoff</i>[<i>unit</i>][/<i>nn_dist</i>]]</p>
<dd> Specifies the separation tolerance in the data coordinate units [0]; append distance unit (see UNITS). If two lines has end-points that are closer than this cutoff they will be joined. Optionally, append /<i>nn_dist</i> which adds the requirement that a link will only be made if the second closest connection exceeds the <i>nn_dist</i>. The latter distance must be given in the same units as <i>cutoff</i>. However, if no arguments are given then we close every polygon regardless of the gap between first and last point.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-g</code>[<code>a</code>]<code>x</code>|<code>y</code>|<code>d</code>|<code>X</code>|<code>Y</code>|<code>D</code>|[<i>col</i>]<code>z</code>[+|-]<i>gap</i>[<code>u</code>] <i>(more &#8230;)</i></p>
<dd> Determine data gaps and line breaks.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> To combine the digitized segment lines segment_*.txt (whose coordinates are in cm) into as few complete lines as possible, assuming the end points slop could be up to 0.1 mm, run </p>
<pre>
gmt connect segment_*.txt -Tf0.1 &gt; new_segments.txt
</pre>
<p> To combine the digitized segments in the multisegment file my_lines.txt (whose coordinates are in lon,lat) into as few complete lines as possible, assuming the end points slop could be up to 150 m, and write the complete segments to separate files called Map_segment_0001.dat, Map_segment_0002.dat, etc., run </p>
<pre>
gmt connect my_lines.txt -T150e -DMap_segment_%04d.dat
</pre>
<h2>BUGS</h2>
<p> The line connection does not work if a line only has a single point. However, gmtconnect will correctly add the point to the nearest segment. Running gmtconnect again on the new set of lines will eventually connect all close lines.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtsimplify</code>, <code>gmtspatial</code>, <code>mapproject</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
