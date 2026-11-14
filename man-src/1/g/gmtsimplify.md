---
title: "gmtsimplify(1)"
name: "gmtsimplify"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtsimplify/"
description: "gmtsimplify – Line reduction using the Douglas-Peucker algorithm"
---

<h2>NAME</h2>
<p> gmtsimplify &#8211; Line reduction using the Douglas-Peucker algorithm</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtsimplify</code> [ <i>table</i> ] <i>tolerance</i>[<i>unit</i>] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtsimplify</code> reads one or more data files and apply the Douglas-Peucker line simplification algorithm. The method recursively subdivides a polygon until a run of points can be replaced by a straight line segment, with no point in that run deviating from the straight line by more than the tolerance. Have a look at this site to get a visual insight on how the algorithm works (<i><a rel="nofollow" href="http://geometryalgorithms.com/Archive/algorithm_0205/algorithm_0205.htm">http://geometryalgorithms.com/Archive/algorithm_0205/algorithm_0205.htm</a></i>)</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-T</code><i>tolerance</i>[<i>unit</i>]</p>
<dd> Specifies the maximum mismatch tolerance in the user units. If the data is not Cartesian then append the distance unit (see UNITS).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
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
<p> To reduce the geographic line segment.d using a tolerance of 2 km, run </p>
<pre>
gmt simplify segment.d -T2k &gt; new_segment.d
</pre>
<p> To reduce the Cartesian lines xylines.d using a tolerance of 0.45 and write the reduced lines to file new_xylines.d, run </p>
<pre>
gmt simplify xylines.d -T0.45 &gt; new_xylines.d
</pre>
<h2>NOTES</h2>
<p> There is a slight difference in how gmtsimplify processes lines versus closed polygons. Segments that are explicitly closed will be considered polygons, otherwise we treat them as line segments. Hence, segments recognized as polygons may reduce to a 3-point polygon with no area; these are suppressed from the output.</p>
<h2>BUGS</h2>
<p> One known issue with the Douglas-Peucker has to do with crossovers. Specifically, it cannot be guaranteed that the reduced line does not cross itself. Depending on how many lines you are considering it is also possible that reduced lines may intersect other reduced lines. Finally, the current implementation only does Flat Earth calculations even if you specify spherical; <code>gmtsimplify</code> will issue a warning and reset the calculation mode to Flat Earth.</p>
<h2>REFERENCES</h2>
<p> Douglas, D. H., and T. K. Peucker, Algorithms for the reduction of the number of points required to represent a digitized line of its caricature, <i>Can. Cartogr.</i>, <code>10</code>, 112-122, 1973. </p>
<p> This implementation of the algorithm has been kindly provided by Dr. <i>Gary J. Robinson</i>, Department of Meteorology, University of Reading, Reading, UK; his subroutine forms the basis for this program.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtconnect</code>, <code>gmtconvert</code>, <code>gmtselect</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
