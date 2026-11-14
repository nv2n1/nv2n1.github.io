---
title: "gmtstitch(1)"
name: "gmtstitch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtstitch/"
description: "gmtstitch – Join line segments whose end points match within tolerance"
---

<h2>NAME</h2>
<p> gmtstitch &#8211; Join line segments whose end points match within tolerance</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtstitch</code> [ <i>infiles</i> ] [ <code>-C</code>[<i>closed</i>] ] [ <code>-D</code>[<i>template</i>] ] [ <code>-H</code>[<code>i</code>][<i>nrec</i>] ] [ <code>-L</code>[<i>linkfile</i>] ] [ <code>-Q</code>[<i>template</i>] ] [ <code>-T</code><i>cutoff</i>[<code>m</code>|<code>c</code>|<code>e</code>|<code>E</code>|<code>k</code>|<code>K</code>][/<i>nn_dist</i>] ] [ <code>-V</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] [ <code>-b</code>[<code>i</code>|<code>o</code>][<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-bo</code>[<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ] [ <code>-m</code>[<code>i</code>|<code>o</code>][<i>flag</i>] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtstitch</code> reads one or more data files (which may be multisegment files; see <code>-m</code>) and examines the coordinates of the end points of all line segments. If a pair of end points are identical or closer to each other than the specified separation tolerance then the two line segments are joined into a single segment. The process repeats until all the remaining endpoints no longer pass the tolerance test; the resulting segments are then written out to standard output. It it is not clear what the separation tolerance should be then use <code>-L</code> to get a list of all separation distances and analyze them to determine a suitable cutoff.</p>
<dl>
<dt><i>file(s)</i></p>
<dd> One of more data files. If none are supplied then we read standard input.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Write all the closed polygons to <i>closed</i> [gmtstitch_closed.d] and all other segments as they are to stdout. No stitching takes place. Use <code>-T</code><i>cutoff</i> to set a minimum separation [0], and if <i>cutoff</i> is &gt; 0 then we also close the polygons on output.</p>
<dt><code>-D</code></p>
<dd> For multiple segment data, dump each segment to a separate output file [Default writes a multiple segment file to stdout]. Append a format template for the individual file names; this template <code>must</code> contain a C format specifier that can format an integer argument (the segment number); this is usually %d but could be %8.8d which gives leading zeros, etc. Optionally, it may also contain the format %c <i>before</i> the integer; this will then be replaced by C (closed) or O (open) to indicate segment type. [Default is gmtstitch_segment_%d.d]. Note that segment headers will be written in either case. For composite segments, a generic segment header will be written and the segment headers of individual pieces will be written out as comments to make it possible to identify where the stitched pieces came from.</p>
<dt><code>-H</code></p>
<dd> Input file(s) has header record(s). If used, the default number of header records is <code>N_HEADER_RECS</code>. Use <code>-Hi</code> if only input data should have header records [Default will write out header records if the input data have them]. Blank lines and lines starting with # are always skipped.</p>
<dt><code>-L</code></p>
<dd> Writes the link information to the specified file [links.d]. For each segment we write the original segment id, and for the beginning and end point of the segment we report the id of the closest segment, whether it is the beginning (B) or end (E) point that is closest, and the distance between those points in units determined by <code>-T</code>.</p>
<dt><code>-Q</code></p>
<dd> Used with <code>-D</code> to a list file with the names of the individual output files. Optionally, append a filename template for the individual file names; this template <code>may</code> contain a C format specifier that can format an character (C or O for closed or open, respectively). [Default is gmtstitch_list.d].</p>
<dt><code>-T</code></p>
<dd> Specifies the separation tolerance in the data coordinate units [0]. Append <code>m</code> or <code>c</code> for minutes or seconds, or <code>e</code> or <code>k</code> for meters or km (implies <code>-fg</code> using use flat Earth approximation. Use <code>E</code> or <code>K</code> for exact geodesic distances; however. if the current ELLIPSOID is Sphere then spherical great circle distances are used. If two lines has endpoints that are closer than this cutoff they will be joined. Optionally, append /<i>nn_dist</i> which adds the requirement that a link will only be made if the second closest connection exceeds the <i>nn_dist</i>. The latter distance is assumed to be in the same units as <i>cutoff</i>.</p>
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
<h2>EXAMPLES</h2>
<p> To combine the digitized multisegment lines segment_*.d (whose coordinates are in cm) into as few complete lines as possible, assuming the end points slop could be up to 0.1 mm, run </p>
<p> <code>gmtstitch</code> segment_*.d <code>-Tf</code>0.1 <code>-m</code> &gt; new_segments.d </p>
<p> To combine the digitized segments in the multisegment file my_lines.d (whose coordinates are in lon,lat) into as few complete lines as possible, assuming the end points slop could be up to 150 m, and write the complete segments to separate files called Map_segment_0001.dat, Map_segment_0002.dat, etc., run </p>
<p> <code>gmtstitch</code> my_lines.d <code>-Tf</code>0.15k <code>-m</code> <code>-D</code>Map_segment_%4.4d.dat </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-mapproject/">mapproject</a></i>(1) </p>
<h2>Index</h2>
