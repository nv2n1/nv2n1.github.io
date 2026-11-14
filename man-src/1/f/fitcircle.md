---
title: "fitcircle(1)"
name: "fitcircle"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fitcircle/"
description: "fitcircle – find mean position and pole of best-fit great [or small] circle to points on a sphere."
---

<h2>NAME</h2>
<p> fitcircle &#8211; find mean position and pole of best-fit great [or small] circle to points on a sphere.</p>
<h2>SYNOPSIS</h2>
<p> <code>fitcircle</code> [ <i>table</i> ] <i>norm</i> [ <i>flags</i> ] [ [<i>lat</i>] ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>fitcircle</code> reads lon,lat [or lat,lon] values from the first two columns on standard input [or <i>table</i>]. These are converted to Cartesian three-vectors on the unit sphere. Then two locations are found: the mean of the input positions, and the pole to the great circle which best fits the input positions. The user may choose one or both of two possible solutions to this problem. The first is called <code>-L1</code> and the second is called <code>-L2</code>. When the data are closely grouped along a great circle both solutions are similar. If the data have large dispersion, the pole to the great circle will be less well determined than the mean. Compare both solutions as a qualitative check. </p>
<p> The <code>-L1</code> solution is so called because it approximates the minimization of the sum of absolute values of cosines of angular distances. This solution finds the mean position as the Fisher average of the data, and the pole position as the Fisher average of the cross-products between the mean and the data. Averaging cross-products gives weight to points in proportion to their distance from the mean, analogous to the &quot;leverage&quot; of distant points in linear regression in the plane. </p>
<p> The <code>-L2</code> solution is so called because it approximates the minimization of the sum of squares of cosines of angular distances. It creates a 3 by 3 matrix of sums of squares of components of the data vectors. The eigenvectors of this matrix give the mean and pole locations. This method may be more subject to roundoff errors when there are thousands of data. The pole is given by the eigenvector corresponding to the smallest eigenvalue; it is the least-well represented factor in the data and is not easily estimated by either method.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-L</code><i>norm</i></p>
<dd> Specify the desired <i>norm</i> as 1 or 2, or use <code>-L</code> or <code>-L3</code> to see both solutions.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII [or binary, see <code>-bi</code>] files containing lon,lat [or lat,lon; see <code>-:</code>[<code>i</code>|<code>o</code>]] values in the first 2 columns. If no file is specified, <code>fitcircle</code> will read from standard input.</p>
<dt><code>-F</code><code>f</code>|<code>m</code>|<code>n</code>|<code>s</code>|<code>c</code></p>
<dd> Normally, <code>fitcircle</code> will write its results in the form of a text report, with the values intermingled with report sentences. Use <code>-F</code> to only return data coordinates, and append <i>flags</i> to specify which coordinates you would like. You can choose from <code>f</code> (Flat Earth mean location), <code>m</code> (mean location), <code>n</code> (north pole of great circle), <code>s</code> (south pole of great circle), and <code>c ** (pole of small circle and its colatitude, which requires **-S</code>).</p>
<dt><code>-S</code>[<i>lat</i>]</p>
<dd> Attempt to fit a small circle instead of a great circle. The pole will be constrained to lie on the great circle connecting the pole of the best-fit great circle and the mean location of the data. Optionally append the desired fixed latitude of the small circle [Default will determine the latitude].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
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
<p> Suppose you have lon,lat,grav data along a twisty ship track in the file ship.xyg. You want to project this data onto a great circle and resample it in distance, in order to filter it or check its spectrum. Do the following: </p>
<pre>
gmt fitcircle ship.xyg -L2
gmt project ship.xyg -Cox/oy -Tpx/py -S -Fpz | sample1d -S-100 -I1 &gt; output.pg
</pre>
<p> Here, <i>ox</i>/<i>oy</i> is the lon/lat of the mean from <code>fitcircle</code>, and <i>px</i>/<i>py</i> is the lon/lat of the pole. The file output.pg has distance, gravity data sampled every 1 km along the great circle which best fits ship.xyg </p>
<p> If you have lon, lat points in the file data.txt and wish to return the northern hemisphere great circle pole location using the L2 norm, try </p>
<pre>
gmt fitcircle data.txt -L2 -Fn &gt; pole.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtvector</code>, <code>project</code>, <code>mapproject</code>, <code>sample1d</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
