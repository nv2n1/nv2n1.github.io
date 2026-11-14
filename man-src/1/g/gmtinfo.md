---
title: "gmtinfo(1)"
name: "gmtinfo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtinfo/"
description: "gmtinfo – Return information about data tables"
---

<h2>NAME</h2>
<p> gmtinfo &#8211; Return information about data tables</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtinfo</code> [ <i>table</i> ] [ <code>a</code>|<code>f</code>|<code>s</code> ] [ ] [ [<i>dx</i>[/<i>dy</i>]] ] [ <code>L</code>|<code>l</code>|<code>H</code>|<code>h</code><i>col</i> ] [ [<code>p</code>|<code>f</code>|<code>s</code>]<i>dx</i>[/<i>dy</i>[/<i>dz</i>&#8230;] ] [ [<code>x</code>][<code>y</code>] ] [ <i>dz</i>[/<i>col</i>] ] [ [<i>level</i>] ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtinfo</code> reads its standard input [or from files] and finds the extreme values in each of the columns. It recognizes NaNs and will print warnings if the number of columns vary from record to record. As an option, <code>gmtinfo</code> will find the extent of the first <i>n</i> columns rounded up and down to the nearest multiple of the supplied increments. By default, this output will be in the form <code>-R</code><i>w/e/s/n</i> which can be used directly in the command line for other programs (hence only <i>dx</i> and <i>dy</i> are needed), or the output will be in column form for as many columns as there are increments provided. A similar option (<code>-T</code>) will provide a <code>-T</code><i>zmin/zmax/dz</i> string for makecpt.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><code>a</code>|<code>f</code>|<code>s</code></p>
<dd> Specify how the range should be reported. Choose <code>-Aa</code> for the range of all files combined, <code>-Af</code> to report the range for each file separately, and <code>-As</code> to report the range for each segment (in multisegment files) separately. [Default is <code>-Aa</code>].</p>
<dt><code>-C</code></p>
<dd> Report the min/max values per column in separate columns [Default uses &lt;min/max&gt; format]. When used, users may also use <code>-o</code> to limit which output columns should be reported [all].</p>
<dt><code>-D</code></p>
<dd> Modifies results obtained by <code>-I</code> by shifting the region to better align with the center of the data. Optionally, append granularity for this shift [Default performs an exact shift].</p>
<dt><code>-EL</code>|<code>l</code>|<code>H</code>|<code>h</code><i>col</i></p>
<dd> Returns the record whose column <i>col</i> contains the minimum (<code>l</code>) or maximum (<code>h</code>) value. Upper case (<code>L|H</code>) works on absolute value of the data. In case of multiple matches, only the first record is returned. If <i>col</i> is not specified we default to the last column in the data.</p>
<dt><code>-I</code>[<code>p</code>|<code>f</code>|<code>s</code>]<i>dx</i>[/<i>dy</i>[/<i>dz</i>&#8230;]</p>
<dd> Report the min/max of the first <i>n</i> columns to the nearest multiple of the provided increments (separate the <i>n</i> increments by slashes), and output results in the form <code>-R</code><i>w/e/s/n</i> (unless <code>-C</code> is set). If only one increment is given we also use it for the second column (for backwards compatibility). To override this behavior, use <code>-Ip</code><i>dx</i>. If the input <i>x</i>&#8211; and <i>y</i>-coordinates all have the same phase shift relative to the <i>dx</i> and <i>dy</i> increments then we use those phase shifts in determining the region, and you may use <code>-r</code> to switch from gridline-registration to pixel-registration. For irregular data both phase shifts are set to 0 and the <code>-r</code> is ignored. Use <code>-If</code><i>dx</i>[/<i>dy</i>] to report an extended region optimized to give grid dimensions for fastest results in programs using FFTs. Use <code>-Is</code><i>dx</i>[/<i>dy</i>] to report an extended region optimized to give grid dimensions for fastest results in programs like surface. If <i>dx</i> is given as &#8211; then the actual min/max of the input is given in the <code>-R</code> string.</p>
<dt><code>-S</code>[<code>x</code>][<code>y</code>]</p>
<dd> Add extra space for error bars. Useful together with <code>-I</code> option and when later plotting with <code>psxy</code> <code>-E</code>. <code>-Sx</code> leaves space for horizontal error bars using the values in third (2) column. <code>-Sy</code> leaves space for vertical error bars using the values in third (2) column. <code>-S</code> or <code>-Sxy</code> leaves space for both error bars using the values in third and fourth (2 and 3) columns.</p>
<dt><code>-T</code><i>dz</i>[/<i>col</i>]</p>
<dd> Report the min/max of the first (0&#8217;th) column to the nearest multiple of <i>dz</i> and output this in the form <code>-T</code><i>zmin/zmax/dz</i>. To use another column, append /<i>col</i>. Only works when <code>-I</code> is selected.</p>
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
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline].</p>
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
<p> To find the extreme values in the file ship_gravity.xygd: </p>
<pre>
gmt info ship_gravity.xygd
</pre>
<p> Output should look like </p>
<pre>
ship_gravity.xygd: N = 6992 &lt;326.125/334.684&gt; &lt;-28.0711/-8.6837&gt; &lt;-47.7/177.6&gt; &lt;0.6/3544.9&gt;
</pre>
<p> To find the extreme values in the file track.xy to the nearest 5 units but shifted to within 1 unit of the data center, and use this region to draw a line using psxy, run </p>
<pre>
gmt psxy `gmt info -I5 -D1 track.xy` track.xy -Jx1 -B5 -P &gt; track.ps
</pre>
<p> To find the min and max values for each of the first 4 columns, but rounded to integers, and return the result individually for each data file, use </p>
<pre>
gmt info profile_*.txt -C -I1/1/1/1
</pre>
<h2>BUGS</h2>
<p> The <code>-I</code> option does not yet work properly with time series data (e.g., <code>-f</code>0T). Thus, such variable intervals as months and years are not calculated. Instead, specify your interval in the same units as the current setting of <i>TIME_UNIT</i>.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtconvert</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
