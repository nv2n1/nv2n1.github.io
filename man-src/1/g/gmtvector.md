---
title: "gmtvector(1)"
name: "gmtvector"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtvector/"
description: "gmtvector – Basic manipulation of Cartesian vectors"
---

<h2>NAME</h2>
<p> gmtvector &#8211; Basic manipulation of Cartesian vectors</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtvector</code> [ <i>tables</i> ] [ <code>m</code>[<i>conf</i>]|<i>vector</i> ] [ [<code>i</code>|<code>o</code>] ] [ ] [ ] [ <i>vector</i> ] [ <code>a</code>|<code>d</code>|<code>D</code>|<code>p</code><i>az</i>|<code>r</code>[<i>arg</i>|<code>R</code>|<code>s</code>|<code>x</code>] ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtvector</code> reads either (x, y), (x, y, z), (r, theta) or (lon, lat) [or (lat,lon); see <code>-:</code>] coordinates from the first 2-3 columns on standard input [or one or more <i>tables</i>]. If <code>-fg</code> is selected and only two items are read (i.e., lon, lat) then these coordinates are converted to Cartesian three-vectors on the unit sphere. Otherwise we expect (r, theta) unless <code>-Ci</code> is in effect. If no file is found we expect a single vector to be given as argument to <code>-A</code>; this argument will also be interpreted as an x/y[/z], lon/lat, or r/theta vector. The input vectors (or the one provided via <code>-A</code>) are denoted the prime vector(s). Several standard vector operations (angle between vectors, cross products, vector sums, and vector rotations) can be selected; most require a single second vector, provided via <code>-S</code>. The output vectors will be converted back to (lon, lat) or (r, theta) unless <code>-Co</code> is set which requests (x, y[, z]) Cartesian coordinates.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] file containing lon,lat [lat,lon if <code>-:</code>] values in the first 2 columns (if <code>-fg</code> is given) or (r, theta), or perhaps (x, y[, z]) if <code>-Ci</code> is given). If no file is specified, <code>gmtvector</code>, will read from standard input.</p>
<dt><code>-A</code><code>m</code>[<i>conf</i>]|<i>vector</i></p>
<dd> Specify a single, primary vector instead of reading <i>tables</i>; see <i>tables</i> for possible vector formats. Alternatively, append <code>m</code> to read <i>tables</i> and set the single, primary vector to be the mean resultant vector first. We also compute the confidence ellipse for the mean vector (azimuth of major axis, major axis, and minor axis; for geographic data the axes will be reported in km). You may optionally append the confidence level in percent [95]. These three parameters are reported in the final three output columns.</p>
<dt><code>-C</code>[<code>i</code>|<code>o</code>]</p>
<dd> Select Cartesian coordinates on input and output. Append <code>i</code> for input only or <code>o</code> for output only; otherwise both input and output will be assumed to be Cartesian [Default is polar r/theta for 2-D data and geographic lon/lat for 3-D].</p>
<dt><code>-E</code></p>
<dd> Convert input geographic coordinates from geodetic to geocentric and output geographic coordinates from geocentric to geodetic. Ignored unless <code>-fg</code> is in effect, and is bypassed if <code>-C</code> is selected.</p>
<dt><code>-N</code></p>
<dd> Normalize the resultant vectors prior to reporting the output [No normalization]. This only has an effect if <code>-Co</code> is selected.</p>
<dt><code>-S</code>[<i>vector</i>]</p>
<dd> Specify a single, secondary vector in the same format as the first vector. Required by operations in <code>-T</code> that need two vectors (average, bisector, dot product, cross product, and sum).</p>
<dt><code>-T</code><code>a</code>|<code>d</code>|<code>D</code>|<code>p</code><i>az</i>|<code>s</code>|<code>r</code>[<i>arg</i>|<code>R</code>|<code>x</code>]</p>
<dd> Specify the vector transformation of interest. Append <code>a</code> for average, <code>b</code> for the pole of the two points bisector, <code>d</code> for dot product (use <code>D</code> to get angle in degrees between the two vectors), <code>p</code><i>az</i> for the pole to the great circle specified by input vector and the circle&#8217;s <i>az</i> (no second vector used), <code>s</code> for vector sum, <code>r</code><i>par</i> for vector rotation (here, <i>par</i> is a single angle for 2-D Cartesian data and <i>lon/lat/angle</i> for a 3-D rotation pole and angle), <code>R</code> will instead rotate the fixed secondary vector by the rotations implied by the input records, and <code>x</code> for cross-product. If <code>-T</code> is not given then no transformation takes place; the output is determined by other options such as <code>-A</code>, <code>-C</code>, <code>-E</code>, and <code>-N</code>.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 or 3 input columns].</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> Suppose you have a file with lon, lat called points.txt. You want to compute the spherical angle between each of these points and the location 133/34. Try </p>
<pre>
gmt vector points.txt -S133/34 -TD -fg &gt; angles.txt
</pre>
<p> To rotate the same points 35 degrees around a pole at 133/34, and output Cartesian 3-D vectors, use </p>
<pre>
gmt vector points.txt -Tr133/34/35 -Co -fg &gt; reconstructed.txt
</pre>
<p> To rotate the point 65/33 by all rotations given in file rots.txt, use </p>
<pre>
gmt vector rots.txt -TR -S64/33 -fg &gt; reconstructed.txt
</pre>
<p> To compute the cross-product between the two Cartesian vectors 0.5/1/2 and 1/0/0.4, and normalizing the result, try </p>
<pre>
gmt vector -A0.5/1/2 -Tx -S1/0/0.4 -N -C &gt; cross.txt
</pre>
<p> To rotate the 2-D vector, given in polar form as r = 2 and theta = 35, by an angle of 120, try </p>
<pre>
gmt vector -A2/35 -Tr120 &gt; rotated.txt
</pre>
<p> To find the mid-point along the great circle connecting the points 123/35 and -155/-30, use </p>
<pre>
gmt vector -A123/35 -S-155/-30 -Ta -fg &gt; midpoint.txt
</pre>
<p> To find the mean location of the geographical points listed in points.txt, with its 99% confidence ellipse, use </p>
<pre>
gmt vector points.txt -Am99 -fg &gt; centroid.txt
</pre>
<p> To find the pole corresponding to the great circle that goes through the point -30/60 at an azimuth of 105 degrees, use </p>
<pre>
gmt vector -A-30/60 -Tp105 -fg &gt; pole.txt
</pre>
<h2>ROTATIONS</h2>
<p> For more advanced 3-D rotations as used in plate tectonic reconstructions, see the GMT &quot;spotter&quot; supplement.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>project</code>, <code>mapproject</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
