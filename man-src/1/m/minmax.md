---
title: "minmax(1)"
name: "minmax"
section: "1"
letter: "m"
url: "/docs/linux/man/1-minmax/"
description: "minmax – Find extreme values in data tables"
---

<h2>NAME</h2>
<p> minmax &#8211; Find extreme values in data tables</p>
<h2>SYNOPSIS</h2>
<p> <code>minmax</code> [ <i>files</i>] [ <code>-C</code> ] [ <code>-EL</code>|<code>l</code>|<code>H</code>|<code>h</code><i>col</i> ] [ <code>-H</code>[<code>i</code>][<i>nrec</i>] ] [ <code>-I</code>[<code>p</code>]<i>dx</i>[/<i>dy</i>[/<i>dz</i>&#8230;] ] [ <code>-S</code>[<code>x</code>][<code>y</code>] ] [ <code>-T</code><i>dz</i>[/<i>col</i>] ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] [ <code>-bi</code>[<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> ] [ <code>-m</code>[<code>i</code>|<code>o</code>][<i>flag</i>] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>minmax</code> reads its standard input [or from files] and finds the extreme values in each of the columns. It recognizes NaNs and will print warnings if the number of columns vary from record to record. As an option, <code>minmax</code> will find the extent of the first <i>n</i> columns rounded up and down to the nearest multiple of the supplied increments. By default, this output will be in the form <code>-R</code><i>w/e/s/n</i> which can be used directly in the command line for other programs (hence only <i>dx</i> and <i>dy</i> are needed), or the output will be in column form for as many columns as there are increments provided. A similar option (<code>-T</code>) will provide a <code>-T</code><i>zmin/zmax/dz</i> string for makecpt.</p>
<dl>
<dt><i>xyzfile</i></p>
<dd> ASCII [or binary, see <code>-b</code>] file(s) holding a fixed number of data columns.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Report the min/max values per column in separate columns [Default uses &lt;min/max&gt; format].</p>
<dt><code>-E</code></p>
<dd> Returns the record whose column <i>col</i> contains the minimum (<code>l</code>) or maximum (<code>h</code>) value. Upper case (<code>L|H</code>) works on absolute value of the data. In case of multiple matches, only the first record is returned.</p>
<dt><code>-H</code></p>
<dd> Input file(s) has header record(s). If used, the default number of header records is <code>N_HEADER_RECS</code>. Use <code>-Hi</code> if only input data should have header records [Default will write out header records if the input data have them]. Blank lines and lines starting with # are always skipped.</p>
<dt><code>-I</code></p>
<dd> Report the min/max of the first <i>n</i> columns to the nearest multiple of the provided increments (separate the <i>n</i> increments by slashes), and output results in the form <code>-R</code><i>w/e/s/n</i> (unless <code>-C</code> is set). If only one increment is given we also use it for the second column (for backwards compatibility). To override this behaviour, use <code>-Ip</code><i>dx</i>.</p>
<dt><code>-S</code></p>
<dd> Add extra space for error bars. Useful together with <code>-I</code> option and when later plotting with <code>psxy</code> <code>-E</code>. <code>-Sx</code> leaves space for horizontal error bars using the values in third (2) column. <code>-Sy</code> leaves space for vertical error bars using the values in third (2) column. <code>-S</code> or <code>-Sxy</code> leaves space for both error bars using the values in third and fourth (2 and 3) columns.</p>
<dt><code>-T</code></p>
<dd> Report the min/max of the first (0&#8217;th) column to the nearest multiple of <i>dz</i> and output this in the form <code>-T</code><i>zmin/zmax/dz</i>. To use another column, append /<i>col</i>.</p>
<dt><code>-:</code></p>
<dd> Toggles between (longitude,latitude) and (latitude,longitude) input and/or output. [Default is (longitude,latitude)]. Append <code>i</code> to select input only or <code>o</code> to select output only. [Default affects both]. Only works when <code>-I</code> is selected.</p>
<dt><code>-bi</code></p>
<dd> Selects binary input. Append <code>s</code> for single precision [Default is <code>d</code> (double)]. Uppercase <code>S</code> or <code>D</code> will force byte-swapping. Optionally, append <i>ncol</i>, the number of columns in your binary input file if it exceeds the columns needed by the program. Or append <code>c</code> if the input file is netCDF. Optionally, append <i>var1</i><code>/</code><i>var2</i><code>/</code><i>&#8230;</i> to specify the variables to be read. [Default is 2 input columns].</p>
<dt><code>-f</code></p>
<dd> Special formatting of input and/or output columns (time or geographical data). Specify <code>i</code> or <code>o</code> to make this apply only to input or output [Default applies to both]. Give one or more columns (or column ranges) separated by commas. Append <code>T</code> (absolute calendar time), <code>t</code> (relative time in chosen <code>TIME_UNIT</code> since <code>TIME_EPOCH</code>), <code>x</code> (longitude), <code>y</code> (latitude), or <code>f</code> (floating point) to each column or column range item. Shorthand <code>-f</code>[<code>i</code>|<code>o</code>]<code>g</code> means <code>-f</code>[<code>i</code>|<code>o</code>]0<code>x</code>,1<code>y</code> (geographic coordinates).</p>
<dt><code>-m</code></p>
<dd> Multiple segment file(s). Segments are separated by a special record. For ASCII files the first character must be <i>flag</i> [Default is &#8216;&gt;&#8217;]. For binary files all fields must be NaN and <code>-b</code> must set the number of output columns explicitly. By default the <code>-m</code> setting applies to both input and output. Use <code>-mi</code> and <code>-mo</code> to give separate settings to input and output.</dl>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your .gmtdefaults4 file. Longitude and latitude are formatted according to <code>OUTPUT_DEGREE_FORMAT</code>, whereas other values are formatted according to <code>D_FORMAT</code>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <code>D_FORMAT</code> setting.</p>
<h2>EXAMPLES</h2>
<p> To find the extreme values in the file ship_gravity.xygd: </p>
<p> <code>minmax</code> ship_gravity.xygd </p>
<p> Output should look like </p>
<p> ship_gravity.xygd: N = 6992 &lt;326.125/334.684&gt; &lt;-28.0711/-8.6837&gt; &lt;-47.7/177.6&gt; &lt;0.6/3544.9&gt; </p>
<p> To find the extreme values in the file track.xy to the nearest 5 units and use this region to draw a line using psxy, run </p>
<p> <code>psxy</code> `<code>minmax</code> <code>-I</code>5 track.xy` track.xy <code>-Jx</code>1 <code>-B</code>5 <code>-P</code> &gt; track.ps </p>
<p> To find the min and max values for each of the first 4 columns, but rounded to integers, use </p>
<p> <code>minmax</code> junkfile <code>-C</code> <code>-I</code>1/1/1/1</p>
<h2>BUGS</h2>
<p> The <code>-I</code> option does not yet work properly with time series data (e.g., <code>-f</code>0T). Thus, such variable intervals as months and years are not calculated. Instead, specify your interval in the same units as the current setting of <code>TIME_UNIT</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1) </p>
<h2>Index</h2>
