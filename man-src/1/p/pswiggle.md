---
title: "pswiggle(1)"
name: "pswiggle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pswiggle/"
description: "pswiggle – Plot z = f(x,y) anomalies along tracks"
---

<h2>NAME</h2>
<p> pswiggle &#8211; Plot z = f(x,y) anomalies along tracks</p>
<h2>SYNOPSIS</h2>
<p> <code>pswiggle</code> [ <i>table</i> ] <i>parameters</i> <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] <i>scale</i> [ <i>azimuth</i> ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <i>center</i> ] [ [<code>+</code>|<code>&#8211;</code>|<code>=</code>]<i>fill</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ <i>fix_az</i> ] [ ] [ ] [ <code>-P</code> ] [ [<code>x</code>]<i>lon0</i>/<i>lat0</i>/<i>length</i>[/<i>units</i>] ] [ <i>pen</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>pswiggle</code> reads (<i>x</i>,<i>y</i>,<i>z</i>) triplets from files [or standard input] and plots z as a function of distance along track. This means that two consecutive (<i>x</i>,<i>y</i>) points define the local distance axis, and the local <i>z</i> axis is then perpendicular to the distance axis. The user may set a preferred positive anomaly plot direction, and if the positive normal is outside the plus/minus 90 degree window around the preferred direction, then 180 degrees are added to the direction. Either the positive or the negative wiggle may be shaded. The resulting PostScript code is written to standard output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></p>
<dt><code>-Z</code><i>scale</i></p>
<dd> Gives anomaly scale in data-units/distance-unit.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><i>azimuth</i></p>
<dd> Sets the preferred positive azimuth. Positive wiggles will &quot;gravitate&quot; towards that direction.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><i>center</i></p>
<dd> Subtract <i>center</i> from the data set before plotting [0].</p>
<dt><code>-G</code>[<code>+</code>|<code>&#8211;</code>|<code>=</code>]<i>fill</i></p>
<dd> Set fill shade, color or pattern for positive and/or negative wiggles [Default is no fill]. Optionally, prepend <code>+</code> to fill positive areas (this is the default behavior). Prepend <code>&#8211;</code> to fill negative areas. Prepend <code>=</code> to fill both positive and negative areas with the same fill.</p>
<dt><code>-I</code><i>fix_az</i></p>
<dd> Set a fixed azimuth projection for wiggles [Default uses track azimuth, but see <code>-A</code>].</p>
<dt><code>-Jz</code>|<code>Z</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set z-axis scaling; same syntax as <code>-Jx</code>.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-S</code>[<code>x</code>]<i>lon0</i>/<i>lat0</i>/<i>length</i>[/<i>units</i>]</p>
<dd> Draws a simple vertical scale centered on <i>lon0/lat0</i>. Use <code>-Sx</code> to specify cartesian coordinates instead. <i>length</i> is in z units, append unit name for labeling. <code>FONT_ANNOT_PRIMARY</code> is used as font.</p>
<dt><code>-T</code><i>pen</i></p>
<dd> Draw track [Default is no track]. Append pen attributes to use [Defaults: width = 0.25p, color = black, style = solid].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-W</code><i>pen</i></p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
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
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<h2>EXAMPLES</h2>
<p> To plot the magnetic anomaly stored in the file track.xym along track @ 1000 nTesla/cm (after removing a mean value of 32000 nTesla), using a 15-cm-wide Polar Stereographic map ticked every 5 degrees in Portrait mode, with positive anomalies in red on a blue track of width 0.25 points, use </p>
<pre>
gmt pswiggle track.xym -R-20/10/-80/-60 -JS0/90/15c -Z1000 -B5 \
             -C32000 -P -Gred -T0.25p,blue -S1000 -V &gt; track_xym.ps
</pre>
<h2>BUGS</h2>
<p> Sometimes the (x,y) coordinates are not printed with enough significant digits, so the local perpendicular to the track swings around a lot. To see if this is the problem, you should do this: </p>
<pre><code>
awk '{ if (NR &gt; 1) print atan2(y-$1, x-$2); y=$1; x=$2; }' yourdata.xyz | more
</code></pre>
<p> (note that output is in radians; on some machines you need &quot;nawk&quot; to do this). Then if these numbers jump around a lot, you may do this: </p>
<pre>
awk '{ print NR, $0 }' yourdata.xyz | filter1d -Fb5 -N4/0 \
--FORMAT_FLOAT_OUT=%.12g &gt; smoothed.xyz
</pre>
<p> and plot this data set instead.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtcolors</code>, <code>filter1d</code>, <code>psbasemap</code>, <code>splitxyz</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
