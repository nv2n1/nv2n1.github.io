---
title: "gmtdp(1)"
name: "gmtdp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtdp/"
description: "gmtdp – Line reduction using the Douglas-Peucker algorithm"
---

<h2>NAME</h2>
<p> gmtdp &#8211; Line reduction using the Douglas-Peucker algorithm</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtdp</code> <i>infiles</i> <code>-T</code><i>tolerance</i> [ <code>-H</code>[<code>i</code>][<i>nrec</i>] ] [ <code>-V</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] [ <code>-b</code>[<code>i</code>|<code>o</code>][<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-bo</code>[<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-m</code>[<code>i</code>|<code>o</code>][<i>flag</i>] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtdp</code> reads one or more data files (which may be multisegment files; see <code>-m</code>) and apply the Douglas-Peucker line simplification algorithm. The method recursively subdivides a polygon until a run of points can be replaced by a straight line segment, with no point in that run deviating from the straight line by more than the tolerance. Have a look at this site to get a visual insight on how the algorithm works <a rel="nofollow" href="http://geometryalgorithms.com/Archive/algorithm_0205/algorithm_0205.htm">http://geometryalgorithms.com/Archive/algorithm_0205/algorithm_0205.htm</a> WARNING: currently this program should be used only with geographical coordinates.</p>
<dl>
<dt><i>file(s)</i></p>
<dd> One of more data files. If none are supplied then we read standard input.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-T</code></p>
<dd> Specifies the maximum mismatch tolerance in km.</p>
<dt><code>-H</code></p>
<dd> Input file(s) has header record(s). If used, the default number of header records is <code>N_HEADER_RECS</code>. Use <code>-Hi</code> if only input data should have header records [Default will write out header records if the input data have them]. Blank lines and lines starting with # are always skipped.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-:</code></p>
<dd> Toggles between (longitude,latitude) and (latitude,longitude) input and/or output. [Default is (longitude,latitude)]. Append <code>i</code> to select input only or <code>o</code> to select output only. [Default affects both].</p>
<dt><code>-bi</code></p>
<dd> Selects binary input. Append <code>s</code> for single precision [Default is <code>d</code> (double)]. Uppercase <code>S</code> or <code>D</code> will force byte-swapping. Optionally, append <i>ncol</i>, the number of columns in your binary input file if it exceeds the columns needed by the program. Or append <code>c</code> if the input file is netCDF. Optionally, append <i>var1</i><code>/</code><i>var2</i><code>/</code><i>&#8230;</i> to specify the variables to be read. [Default is 2 input columns].</p>
<dt><code>-bo</code></p>
<dd> Selects binary output. Append <code>s</code> for single precision [Default is <code>d</code> (double)]. Uppercase <code>S</code> or <code>D</code> will force byte-swapping. Optionally, append <i>ncol</i>, the number of desired columns in your binary output file. [Default is same as input].</p>
<dt><code>-f</code></p>
<dd> Special formatting of input and/or output columns (time or geographical data). Specify <code>i</code> or <code>o</code> to make this apply only to input or output [Default applies to both]. Give one or more columns (or column ranges) separated by commas. Append <code>T</code> (absolute calendar time), <code>t</code> (relative time in chosen <code>TIME_UNIT</code> since <code>TIME_EPOCH</code>), <code>x</code> (longitude), <code>y</code> (latitude), or <code>f</code> (floating point) to each column or column range item. Shorthand <code>-f</code>[<code>i</code>|<code>o</code>]<code>g</code> means <code>-f</code>[<code>i</code>|<code>o</code>]0<code>x</code>,1<code>y</code> (geographic coordinates).</p>
<dt><code>-m</code></p>
<dd> Multiple segment file(s). Segments are separated by a special record. For ASCII files the first character must be <i>flag</i> [Default is &#8216;&gt;&#8217;]. For binary files all fields must be NaN and <code>-b</code> must set the number of output columns explicitly. By default the <code>-m</code> setting applies to both input and output. Use <code>-mi</code> and <code>-mo</code> to give separate settings to input and output.</dl>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your .gmtdefaults4 file. Longitude and latitude are formatted according to <code>OUTPUT_DEGREE_FORMAT</code>, whereas other values are formatted according to <code>D_FORMAT</code>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <code>D_FORMAT</code> setting.</p>
<h2>EXAMPLE</h2>
<p> To reduce the line segment.d using a tolerance of 2 km, run </p>
<p> <code>gmtdp</code> segment.d <code>-T</code>2 &gt; new_segment.d </p>
<h2>REFERENCES</h2>
<p> Douglas, D. H., and T. K. Peucker, Algorithms for the reduction of the number of points required to represent a digitized line of its caricature, <i>Can. Cartogr., 10</i>, 112-122, 1973.<br />
 This implementation of the algorithm has been kindly provided by Dr. Gary J. Robinson, Environmental Systems Science Centre, University of Reading, Reading, UK (gazza [at] mail.nerc-essc.ac.uk); his subroutine forms the basis for this program.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1) </p>
<h2>Index</h2>
