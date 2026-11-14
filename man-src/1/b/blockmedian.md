---
title: "blockmedian(1)"
name: "blockmedian"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blockmedian/"
description: "blockmedian – Block average (x, y, z) data tables by L1 norm"
---

<h2>NAME</h2>
<p> blockmedian &#8211; Block average (x, y, z) data tables by L1 norm</p>
<h2>SYNOPSIS</h2>
<p> <code>blockmedian</code> [ <i>table</i> ] <i>increment</i> <i>region</i> [ ] [ [<code>b</code>] ] [ <code>r</code>|<code>s</code>[<code>&#8211;</code>] ] [ ] [ <i>quantile</i> ] [ [<i>level</i>] ] [ [<code>i</code>|<code>o</code>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-r</code> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>blockmedian</code> reads arbitrarily located (<i>x</i>,<i>y</i>,<i>z</i>) triples [or optionally weighted quadruples (<i>x</i>,<i>y</i>,<i>z</i>,<i>w</i>)] from standard input [or <i>table</i>] and writes to standard output a median position and value for every non-empty block in a grid region defined by the <code>-R</code> and <code>-I</code> arguments. Either <code>blockmean</code>, <code>blockmedian</code>, or <code>blockmode</code> should be used as a pre-processor before running <code>surface</code> to avoid aliasing short wavelengths. These routines are also generally useful for decimating or averaging (<i>x</i>,<i>y</i>,<i>z</i>) data. You can modify the precision of the output format by editing the <i>FORMAT_FLOAT_OUT</i> parameter in your <code>gmt.conf</code> file, or you may choose binary input and/or output to avoid loss of precision.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-I</code><i>xinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>][/<i>yinc</i>[<i>unit</i>][<code>=</code>|<code>+</code>]]</p>
<dd> <i>x_inc</i> [and optionally <i>y_inc</i>] is the grid spacing. Optionally, append a suffix modifier. <code>Geographical (degrees) coordinates</code>: Append <code>m</code> to indicate arc minutes or <code>s</code> to indicate arc seconds. If one of the units <code>e</code>, <code>f</code>, <code>k</code>, <code>M</code>, <code>n</code> or <code>u</code> is appended instead, the increment is assumed to be given in meter, foot, km, Mile, nautical mile or US survey foot, respectively, and will be converted to the equivalent degrees longitude at the middle latitude of the region (the conversion depends on <i>PROJ_ELLIPSOID</i>). If /<i>y_inc</i> is given but set to 0 it will be reset equal to <i>x_inc</i>; otherwise it will be converted to degrees latitude. <code>All coordinates</code>: If <code>=</code> is appended then the corresponding max <i>x</i> (<i>east</i>) or <i>y</i> (<i>north</i>) may be slightly adjusted to fit exactly the given increment [by default the increment may be adjusted slightly to fit the given domain]. Finally, instead of giving an increment you may specify the <i>number of nodes</i> desired by appending <code>+</code> to the supplied integer argument; the increment is then recalculated from the number of nodes and the domain. The resulting increment value depends on whether you have selected a gridline-registered or pixel-registered grid; see <i>App-file-formats</i> for details. Note: if <code>-R</code><i>grdfile</i> is used then the grid spacing has already been initialized; use <code>-I</code> to override the values.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> 3 [or 4, see <code>-W</code>] column ASCII data table] column ASCII file(s) [or binary, see <code>-bi</code>] holding (<i>x</i>,<i>y</i>,<i>z</i>[,<i>w</i>]) data values. [<i>w</i>] is an optional weight for the data. If no file is specified, <code>blockmedian</code> will read from standard input.</p>
<dt><code>-C</code></p>
<dd> Use the center of the block as the output location [Default uses the median x and median y as location (but see <code>-Q</code>)].</p>
<dt><code>-E</code>[<code>b</code>]</p>
<dd> Provide Extended report which includes <code>s</code> (the L1 scale of the median), <code>l</code>, the lowest value, and <code>h</code>, the high value for each block. Output order becomes <i>x</i>,<i>y</i>,<i>z</i>,<i>s</i>,<i>l</i>,<i>h</i>[,<i>w</i>]. [Default outputs <i>x</i>,<i>y</i>,<i>z</i>[,<i>w</i>]. For box-and-whisker calculation, use <code>-Eb</code> which will output <i>x</i>,<i>y</i>,<i>z</i>,<i>l</i>,<i>q25</i>,<i>q75</i>,<i>h</i>[,*w*], where <i>q25</i> and <i>q75</i> are the 25% and 75% quantiles, respectively. See <code>-W</code> for <i>w</i> output.</p>
<dt><code>-E</code><code>r</code>|<code>s</code>[<code>&#8211;</code>]</p>
<dd> Provide source id <code>s</code> or record number <code>r</code> output, i.e., append the source id or record number associated with the median value. If tied then report the record number of the higher of the two values; append <code>&#8211;</code> to instead report the record number of the lower value. Note that both <code>-E</code>[<code>b</code>] and <code>-E</code><code>r</code>[<code>&#8211;</code>] may be specified. For <code>-E</code><code>s</code> we expect input records of the form <i>x</i>,<i>y</i>,<i>z</i>[,<i>w</i>],<i>sid</i>, where <i>sid</i> is an unsigned integer source id.</p>
<dt><code>-Q</code></p>
<dd> (Quicker) Finds median <i>z</i> and (<i>x</i>,<i>y</i>) at that the median <i>z</i> [Default finds median <i>x</i>, median <i>y</i> independent of <i>z</i>]. Also see <code>-C</code>.</p>
<dt><code>-T</code><i>quantile</i></p>
<dd> Sets the <i>quantile</i> of the distribution to be returned [Default is 0.5 which returns the median <i>z</i>]. Here, 0 &lt; <i>quantile</i> &lt; 1.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>i</code>|<code>o</code>]</p>
<dd> Weighted modifier[s]. Unweighted input and output has 3 columns <i>x</i>,<i>y</i>,<i>z</i>; Weighted i/o has 4 columns <i>x</i>,<i>y</i>,<i>z</i>,<i>w</i>. Weights can be used in input to construct weighted mean values in blocks. Weight sums can be reported in output for later combining several runs, etc. Use <code>-W</code> for weighted i/o, <code>-Wi</code> for weighted input only, <code>-Wo</code> for weighted output only. [Default uses unweighted i/o].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 (or 4 if <code>-Wi</code> is set)].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is 3 (or 4 if <code>-Wo</code> is set)]. <code>-E</code> adds 3 additional columns.</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-f</code>[<code>i</code>|<code>o</code>]<i>colinfo</i> <i>(more &#8230;)</i></p>
<dd> Specify data types of input and/or output columns.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
<dt><code>-r</code> <i>(more &#8230;)</i></p>
<dd> Set pixel node registration [gridline]. Each block is the locus of points nearest the grid value location. For example, with <code>-R</code>10/15/10/15 and <code>-I</code>1: with the <code>-r</code> option 10 &lt;= (<i>x</i>,<i>y</i>) &lt; 11 is one of 25 blocks; without it 9.5 &lt;= (<i>x</i>,<i>y</i>) &lt; 10.5 is one of 36 blocks.</p>
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
<p> To find 5 by 5 minute block medians from the double precision binary data in hawaii_b.xyg and output an ASCII table, run </p>
<pre>
gmt blockmedian hawaii_b.xyg -R198/208/18/25 -I5m -bi3d &gt; hawaii_5x5.xyg
</pre>
<p> To compute the shape of a data distribution per bin via a box-and-whisker diagram we need the 0%, 25%, 50%, 75%, and 100% quantiles. To do so on a global 5 by 5 degree basis from the ASCII table depths.xyz and send output to an ASCII table, run </p>
<pre>
gmt blockmedian depths.xyz -Rg -I5 -Eb -r &gt; depths_5x5.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>blockmean</code>, <code>blockmode</code>, <code>gmt</code>, <code>gmt.conf</code>, <code>greenspline</code>, <code>nearneighbor</code>, <code>surface</code>, <code>sphtriangulate</code>, <code>triangulate</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
