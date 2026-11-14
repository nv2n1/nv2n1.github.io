---
title: "gmtconvert(1)"
name: "gmtconvert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtconvert/"
description: "gmtconvert – Convert, Paste, and/or Extract columns from data tables"
---

<h2>NAME</h2>
<p> gmtconvert &#8211; Convert, Paste, and/or Extract columns from data tables</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtconvert</code> [ <i>table</i> ] [ ] [ [<code>+l</code><i>min</i>][<code>+u</code><i>max</i>][<code>+i</code>]] [ [<i>template</i>] ] [ [<code>f</code>|<code>l</code>|<code>m</code><i>stride</i>] ] [ ] [ [<code>c</code>|<code>n</code>|<code>r</code>|<code>v</code>][<i>refpoint</i>] ] [ [<code>tsr</code>] ] [ [<code>~</code>]<i>selection</i>] [ [<code>~</code>]<i>&quot;search string&quot;</i> | [<code>~</code>]/<i>regexp</i>/[<code>i</code>] ] [ ] [ [<i>level</i>] ] [ <code>-a</code><i>&lt;flags&gt;</i> ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtconvert</code> reads its standard input [or input files] and writes out the desired information to standard output. It can do a combination of nine tasks: (1) convert between binary and ASCII data tables, (2) paste corresponding records from multiple files horizontally into a single file, (3) extract a subset of the available columns, (4) only extract segments whose header record matches a text pattern search, (5) only list segment headers and no data records, (6) extract first and/or last data record for each segment, (7) reverse the order of items on output, (8) output only ranges of segment numbers, and (9) output only segments whose record count matches criteria. Input (and hence output) may have multiple sub-headers, and ASCII tables may have regular headers as well.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code></p>
<dd> The records from the input files should be pasted horizontally, not appended vertically [Default]. All files must have the same number of segments and number of rows per segment. Note for binary input, all the files you want to paste must have the same number of columns (as set with <code>-bi</code>); ASCII tables can have different number of columns.</p>
<dt><code>-C</code>[<code>+l</code><i>min</i>][<code>+u</code><i>max</i>][<code>+i</code>]</p>
<dd> Only output segments whose number of records matches your given criteria: Append <code>+l</code><i>min</i> to ensure all segment must have at least <i>min</i> records to be written to output [0], and append <code>+u</code><i>max</i> to ensure all segments must have at most <i>max</i> records to be written [inf]. You may append <code>+i</code> to invert the selection, i.e., only segments with record counts outside the given range will be output.</p>
<dt><code>-D</code>[<i>template</i>]</p>
<dd> For multiple segment data, dump each segment to a separate output file [Default writes a multiple segment file to stdout]. Append a format template for the individual file names; this template <code>must</code> contain a C format specifier that can format an integer argument (the running segment number across all tables); this is usually %d but could be %08d which gives leading zeros, etc. [Default is gmtconvert_segment_%d.{txt|bin}, depending on <code>-bo</code>]. Alternatively, give a template with two C format specifiers and we will supply the table number and the segment number within the table to build the file name.</p>
<dt><code>-E</code>[<code>f</code>|<code>l</code>|<code>m</code><i>stride</i>]</p>
<dd> Only extract the first and last record for each segment of interest [Default extracts all records]. Optionally, append <code>f</code> or <code>l</code> to only extract the first or last record of each segment, respectively. Alternatively, append <code>m</code><i>stride</i> to extract only one out of <i>stride</i> records.</p>
<dt><code>-F</code>[<code>c</code>|<code>n</code>|<code>r</code>|<code>v</code>][<i>refpoint</i>]</p>
<dd> Alter the way points are connected (by specifying a <i>scheme</i>) and data are grouped (by specifying a <i>method</i>). Append one of four line connection schemes: <code>c</code>: Form continuous line segments for each group [Default]. <code>r</code>: Form line segments from a reference point reset for each group. <code>n</code>: Form networks of line segments between all points in each group. <code>v</code>: Form vector line segments suitable for psxy <code>-Sv+s</code>. Optionally, append the one of four segmentation methods to define the group: <code>a</code>: Ignore all segment headers, i.e., let all points belong to a single group, and set group reference point to the very first point of the first file. <code>f</code>: Consider all data in each file to be a single separate group and reset the group reference point to the first point of each group. <code>s</code>: Segment headers are honored so each segment is a group; the group reference point is reset to the first point of each incoming segment [Default]. <code>r</code>: Same as <code>s</code>, but the group reference point is reset after each record to the previous point (this method is only available with the <code>-Fr</code> scheme). Instead of the codes <code>a</code>|<code>f</code>|<code>s</code>|<code>r</code> you may append the coordinates of a <i>refpoint</i> which will serve as a fixed external reference point for all groups.</p>
<dt><code>-I</code>[<code>tsr</code>]</p>
<dd> Invert the order of items, i.e., output the items in reverse order, starting with the last and ending up with the first item [Default keeps original order]. Append up to three items that should be reversed: <code>t</code> will reverse the order of tables, <code>s</code> will reverse the order of segments within each table, and <code>r</code> will reverse the order of records within each segment [Default].</p>
<dt><code>-L</code></p>
<dd> Only output a listing of all segment header records and no data records (requires ASCII data).</p>
<dt><code>-Q</code>[<code>~</code>]<i>selection</i></p>
<dd> Only write segments whose number is included in <i>selection</i> and skip all others. Cannot be used with <code>-S</code>. The <i>selection</i> syntax is <i>range</i>[,<i>range</i>,&#8230;] where each <i>range</i> of items is either a single segment <i>number</i> or a range with stepped increments given via <i>start</i>[:<i>step</i>:]:<i>stop</i> (<i>step</i> is optional and defaults to 1). A leading <code>~</code> will invert the selection and write all segments but the ones listed. Instead of a list of ranges, use <code>+f</code><i>file</i> to supply a file list with one <i>range</i> per line.</p>
<dt><code>-S</code>[<code>~</code>]<i>search string</i> or <code>-S</code>[<code>~</code>]/<i>regexp</i>/[<code>i</code>]</p>
<dd> Only output those segments whose header record contains the specified text string. To reverse the search, i.e., to output segments whose headers do <i>not</i> contain the specified pattern, use <code>-S~</code>. Should your pattern happen to start with ~ you need to escape this character with a backslash [Default output all segments]. Cannot be used with <code>-Q</code>. For matching segments based on aspatial values (via OGR/GMT format), give the search string as <i>varname</i>=<i>value</i> and we will compare <i>value</i> against the value of <i>varname</i> for each segment. Note: If the features are polygons then a match of a particular polygon perimeter also means that any associated polygon holes will also be matched. For matching segment headers against extended regular expressions enclose the expression in slashes. Append <code>i</code> for case-insensitive matching. For a list of such patterns, give <code>+f</code><i>file</i> with one pattern per line. To give a single pattern starting with +f, escape it with a backslash.</p>
<dt><code>-T</code></p>
<dd> Suppress the writing of segment headers on output.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-a</code><i>col</i>=<i>name</i>[<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Set aspatial column associations <i>col</i>=<i>name</i>.</p>
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
<dt><code>-s</code>[<i>cols</i>][<code>a</code>|<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Set handling of NaN records.</p>
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
<p> To convert the binary file test.b (single precision) with 4 columns to ASCII: </p>
<pre>
gmt convert test.b -bi4f &gt; test.dat
</pre>
<p> To convert the multiple segment ASCII table test.d to a double precision binary file: </p>
<pre>
gmt convert test.d -bo &gt; test.b
</pre>
<p> You have an ASCII table with 6 columns and you want to plot column 5 versus column 0. Try </p>
<pre>
gmt convert table.d -o5,0 | psxy ...
</pre>
<p> If the file instead is the binary file results.b which has 9 single-precision values per record, we extract the last column and columns 4-6 and write ASCII with the command </p>
<pre>
gmt convert results.b -o8,4-6 -bi9s | psxy ...
</pre>
<p> You want to plot the 2nd column of a 2-column file left.d versus the first column of a file right.d: </p>
<pre>
gmt convert left.d right.d -A -o1,2 | psxy ...
</pre>
<p> To extract all segments in the file big_file.d whose headers contain the string &quot;RIDGE AXIS&quot;, try </p>
<pre>
gmt convert big_file.d -S&quot;RIDGE AXIS&quot; &gt; subset.d
</pre>
<p> To invert the selection of segments whose headers begin with &quot;profile &quot; followed by an integer number and any letter between &quot;g&quot; and &quot;l&quot;, try </p>
<pre><code>
gmt convert - S ~"/^profile [0-9]+[g-l]$/"
</code></pre>
<p> To reverse the order of segments in a file without reversing the order of records within each segment, try </p>
<pre>
gmt convert lots_of_segments.txt -Is &gt; last_segment_first.txt
</pre>
<p> To extract segments 20 to 40 in steps of 2, plus segment 0 in a file, try </p>
<pre>
gmt convert lots_of_segments.txt -Q0,20:2:40 &gt; my_segments.txt
</pre>
<p> To extract the attribute ELEVATION from an ogr gmt file like this </p>
<pre>
# @VGMT1.0 @GPOINT
...
# @NELEVATION|DISPX|DISPY
# @Tdouble|double|double
# FEATURE_DATA
# @D4.945000|-106500.00000000|-32700.00000000
-9.36890245902635 39.367156766570389
</pre>
<p> do </p>
<pre>
gmt convert file.gmt -a2=ELEVATION &gt; xyz.dat
</pre>
<p> or just </p>
<pre>
gmt convert file.gmt -aELEVATION &gt; xyz.dat
</pre>
<p> To connect all points in the file sensors.txt with the specified origin at 23.5/19, try </p>
<pre>
gmt convert sensors.txt -F23.5/19 &gt; lines.txt
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmtinfo</code>, <code>gmtselect</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
