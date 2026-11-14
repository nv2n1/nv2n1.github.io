---
title: "filter1d(1)"
name: "filter1d"
section: "1"
letter: "f"
url: "/docs/linux/man/1-filter1d/"
description: "filter1d – Do time domain filtering of 1-D data tables"
---

<h2>NAME</h2>
<p> filter1d &#8211; Do time domain filtering of 1-D data tables</p>
<h2>SYNOPSIS</h2>
<p> <code>filter1d</code> [ <i>table</i> ] <i>type&lt;width&gt;</i>[<i>mode</i>] [ <i>increment</i> ] [ ] [ <i>ignore_val</i> ] [ <i>lack_width</i> ] [ <i>t_col</i> ] [ <i>q_factor</i> ] [ <i>symmetry_factor</i> ] [ <i>t_min/t_max/t_inc</i>[<code>+</code>] ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>filter1d</code> is a general time domain filter for multiple column time series data. The user specifies which column is the time (i.e., the independent variable). (See <code>-N</code> option below). The fastest operation occurs when the input time series are equally spaced and have no gaps or outliers and the special options are not needed. <code>filter1d</code> has options <code>-L</code>, <code>-Q</code>, and <code>-S</code> for unevenly sampled data with gaps.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-F</code><i>type&lt;width&gt;</i>[<i>mode</i>]</p>
<dd> Sets the filter <i>type</i>. Choose among convolution and non-convolution filters. Append the filter code followed by the full filter <i>&lt;width&gt;</i> in same units as time column. Available convolution filters are: </p>
<p> (<code>b</code>) Boxcar: All weights are equal. </p>
<p> (<code>c</code>) Cosine Arch: Weights follow a cosine arch curve. </p>
<p> (<code>g</code>) Gaussian: Weights are given by the Gaussian function. </p>
<p> (<code>f</code>) Custom: Instead of <i>width</i> give name of a one-column file with your own weight coefficients. </p>
<p> Non-convolution filters are: </p>
<p> (<code>m</code>) Median: Returns median value. </p>
<p> (<code>p</code>) Maximum likelihood probability (a mode estimator): Return modal value. If more than one mode is found we return their average value. Append &#8211; or + to the filter width if you rather want to return the smallest or largest of the modal values. </p>
<p> (<code>l</code>) Lower: Return the minimum of all values. </p>
<p> (<code>L</code>) Lower: Return minimum of all positive values only. </p>
<p> (<code>u</code>) Upper: Return maximum of all values. </p>
<p> (<code>U</code>) Upper: Return maximum or all negative values only. </p>
<p> Upper case type <code>B</code>, <code>C</code>, <code>G</code>, <code>M</code>, <code>P</code>, <code>F</code> will use robust filter versions: i.e., replace outliers (2.5 L1 scale off median) with median during filtering. </p>
<p> In the case of <code>L</code>|<code>U</code> it is possible that no data passes the initial sign test; in that case the filter will return 0.0.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-D</code><i>increment</i></p>
<dd> <i>increment</i> is used when series is NOT equidistantly sampled. Then <i>increment</i> will be the abscissae resolution, i.e., all abscissae will be rounded off to a multiple of <i>increment</i>. Alternatively, resample data with <code>sample1d</code>.</p>
<dt><code>-E</code></p>
<dd> Include Ends of time series in output. Default loses half the filter-width of data at each end.</p>
<dt><code>-I</code><i>ignore_val</i></p>
<dd> To ignore values; If an input value equals <i>ignore_val</i> it will be set to NaN.</p>
<dt><code>-L</code><i>lack_width</i></p>
<dd> Checks for Lack of data condition. If input data has a gap exceeding <i>width</i> then no output will be given at that point [Default does not check Lack].</p>
<dt><code>-N</code><i>t_col</i></p>
<dd> Indicates which column contains the independent variable (time). The left-most column is # 0, the right-most is # (<i>n_cols</i> &#8211; 1). [Default is 0].</p>
<dt><code>-Q</code><i>q_factor</i></p>
<dd> Assess Quality of output value by checking mean weight in convolution. Enter <i>q_factor</i> between 0 and 1. If mean weight &lt; <i>q_factor</i>, output is suppressed at this point [Default does not check Quality].</p>
<dt><code>-S</code><i>symmetry_factor</i></p>
<dd> Checks symmetry of data about window center. Enter a factor between 0 and 1. If ( (abs(n_left &#8211; n_right)) / (n_left + n_right) ) &gt; <i>factor</i>, then no output will be given at this point [Default does not check Symmetry].</p>
<dt><code>-T</code><i>t_min/t_max/t_inc</i>[<code>+</code>]</p>
<dd> Make evenly spaced time-steps from <i>t_min</i> to <i>t_max</i> by <i>t_inc</i> [Default uses input times]. Append <code>+</code> to <i>t_inc</i> if you are specifying the number of equidistant points instead.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input.</p>
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
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> To filter the data set in the file cruise.gmtd containing evenly spaced gravity, magnetics, topography, and distance (in m) with a 10 km Gaussian filter, removing outliers, and output a filtered value every 2 km between 0 and 100 km: </p>
<pre>
gmt filter1d cruise.gmtd -T0/1.0e5/2000 -FG10000 -N3 -V &gt; filtered_cruise.gmtd
</pre>
<p> Data along track often have uneven sampling and gaps which we do not want to interpolate using <code>sample1d</code>. To find the median depth in a 50 km window every 25 km along the track of cruise v3312, stored in v3312.dt, checking for gaps of 10km and asymmetry of 0.3: </p>
<pre>
gmt filter1d v3312.dt -FM50 -T0/100000/25 -L10 -S0.3 &gt; v3312_filt.dt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code> , <code>sample1d</code> , <code>splitxyz</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
