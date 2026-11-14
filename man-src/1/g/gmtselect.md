---
title: "gmtselect(1)"
name: "gmtselect"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtselect/"
description: "gmtselect – Select data table subsets based on multiple spatial criteria"
---

<h2>NAME</h2>
<p> gmtselect &#8211; Select data table subsets based on multiple spatial criteria</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtselect</code> [ <i>table</i> ] [ <i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code>|<code>S</code>][<code>+r</code>|<code>l</code>][<code>p</code><i>percent</i>] ] [ <i>dist</i>[<i>unit</i>]/<i>ptfile</i> ] [ <i>resolution</i>[<code>+</code>] ] [ [<code>fn</code>] ] [ <i>polygonfile</i> ] [ <code>-I</code>[<code>cflrsz</code>] ] [ <i>parameters</i> ] [ [<code>p</code>]<i>dist</i>[<i>unit</i>]/<i>linefile</i> ] [ <i>maskvalues</i> ] [ <i>region</i> ] [ <i>min</i>[/<i>max</i>][<code>+c</code><i>col</i>] ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtselect</code> is a filter that reads (longitude, latitude) positions from the first 2 columns of <i>infiles</i> [or standard input] and uses a combination of 1-6 criteria to pass or reject the records. Records can be selected based on whether or not they are 1) inside a rectangular region (<code>-R</code> [and <code>-J</code>]), 2) within <i>dist</i> km of any point in <i>ptfile</i>, 3) within <i>dist</i> km of any line in <i>linefile</i>, 4) inside one of the polygons in the <i>polygonfile</i>, 5) inside geographical features (based on coastlines), or 6) has z-values within a given range. The sense of the tests can be reversed for each of these 6 criteria by using the <code>-I</code> option. See option <code>-:</code> on how to read (latitude,longitude) files.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><i>min_area</i>[/<i>min_level</i>/<i>max_level</i>][<code>+ag</code>|<code>i</code>|<code>s</code>|<code>S</code>][<code>+r</code>|<code>l</code>][<code>+p</code><i>percent</i>]</p>
<dd> Features with an area smaller than <i>min_area</i> in km^2 or of hierarchical level that is lower than <i>min_level</i> or higher than <i>max_level</i> will not be plotted [Default is 0/0/4 (all features)]. Level 2 (lakes) contains regular lakes and wide river bodies which we normally include as lakes; append <code>+r</code> to just get river-lakes or <code>+l</code> to just get regular lakes. By default (<code>+ai</code>) we select the ice shelf boundary as the coastline for Antarctica; append <code>+ag</code> to instead select the ice grounding line as coastline. For expert users who wish to print their own Antarctica coastline and islands via <i>psxy</i> you can use <code>+as</code> to skip all GSHHG features below 60S or <code>+aS</code> to instead skip all features north of 60S. Finally, append <code>+p</code><i>percent</i> to exclude polygons whose percentage area of the corresponding full-resolution feature is less than <i>percent</i>. See GSHHG INFORMATION below for more details. Ignored unless <code>-N</code> is set.</p>
<dt><code>-C</code><i>dist</i>[<i>unit</i>]/<i>ptfile</i></p>
<dd> Pass all records whose location is within <i>dist</i> of any of the points in the ASCII file <i>ptfile</i>. If <i>dist</i> is zero then the 3rd column of <i>ptfile</i> must have each point&#8217;s individual radius of influence. Distances are Cartesian and in user units; specify <code>-fg</code> to indicate spherical distances and append a distance unit (see UNITS). Alternatively, if <code>-R</code> and <code>-J</code> are used then geographic coordinates are projected to map coordinates (in cm, inch, or points, as determined by <i>PROJ_LENGTH_UNIT</i>) before Cartesian distances are compared to <i>dist</i>.</p>
<dt><code>-D</code><i>resolution</i>[<code>+</code>]</p>
<dd> Ignored unless <code>-N</code> is set. Selects the resolution of the coastline data set to use ((<code>f</code>)ull, (<code>h</code>)igh, (<code>i</code>)ntermediate, (<code>l</code>)ow, or (<code>c</code>)rude). The resolution drops off by ~80% between data sets. [Default is <code>l</code>]. Append (+) to automatically select a lower resolution should the one requested not be available [abort if not found]. Note that because the coastlines differ in details it is not guaranteed that a point will remain inside [or outside] when a different resolution is selected.</p>
<dt><code>-E</code>[<code>fn</code>]</p>
<dd> Specify how points exactly on a polygon boundary should be considered. By default, such points are considered to be inside the polygon. Append <code>n</code> and/or <code>f</code> to change this behavior for the <code>-F</code> and <code>-N</code> options, respectively, so that boundary points are considered to be outside.</p>
<dt><code>-F</code><i>polygonfile</i></p>
<dd> Pass all records whose location is within one of the closed polygons in the multiple-segment file <i>polygonfile</i>. For spherical polygons (lon, lat), make sure no consecutive points are separated by 180 degrees or more in longitude. Note that <i>polygonfile</i> must be in ASCII regardless of whether <code>-bi</code> is used.</p>
<dt><code>-I</code>[<code>cflrsz</code>]</p>
<dd> Reverses the sense of the test for each of the criteria specified: </p>
<p> <code>c</code> select records NOT inside any point&#8217;s circle of influence. </p>
<p> <code>f</code> select records NOT inside any of the polygons. </p>
<p> <code>l</code> select records NOT within the specified distance of any line. </p>
<p> <code>r</code> select records NOT inside the specified rectangular region. </p>
<p> <code>s</code> select records NOT considered inside as specified by <code>-N</code> (and <code>-A</code>, <code>-D</code>). </p>
<p> <code>z</code> select records NOT within the range specified by <code>-Z</code>.</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-L</code>[<code>p</code>]<i>dist</i>[<i>unit</i>]/<i>linefile</i></p>
<dd> Pass all records whose location is within <i>dist</i> of any of the line segments in the ASCII multiple-segment file <i>linefile</i>. If <i>dist</i> is zero then we will scan each sub-header in the <i>ptfile</i> for an embedded <code>-D</code><i>dist</i> setting that sets each line&#8217;s individual distance value. Distances are Cartesian and in user units; specify <code>-fg</code> to indicate spherical distances append a distance unit (see UNITS). Alternatively, if <code>-R</code> and <code>-J</code> are used then geographic coordinates are projected to map coordinates (in cm, inch, m, or points, as determined by <i>PROJ_LENGTH_UNIT</i>) before Cartesian distances are compared to <i>dist</i>. Use <code>-Lp</code> to ensure only points whose orthogonal projections onto the nearest line-segment fall within the segments endpoints [Default considers points &quot;beyond&quot; the line&#8217;s endpoints.</p>
<dt><code>-N</code><i>maskvalues</i></p>
<dd> Pass all records whose location is inside specified geographical features. Specify if records should be skipped (s) or kept (k) using 1 of 2 formats: </p>
<p> <code>-N</code><i>wet/dry</i>. </p>
<p> <code>-N</code><i>ocean/land/lake/island/pond</i>. </p>
<p> [Default is s/k/s/k/s (i.e., s/k), which passes all points on dry land].</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. If no map projection is supplied we implicitly set <code>-Jx</code>1.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-Z</code><i>min</i>[/<i>max</i>][<code>+c</code><i>col</i>]</p>
<dd> Pass all records whose 3rd column (<i>z</i>; <i>col</i> = 2) lies within the given range or is NaN (use <code>-s</code> to skip NaN records). If <i>max</i> is omitted then we test if <i>z</i> equals <i>min</i> instead. Input file must have at least three columns. To indicate no limit on min or max, specify a hyphen (-). If your 3rd column is absolute time then remember to supply <code>-f</code>2T. To specify another column, append <code>+c</code><i>col</i>, and to specify several tests just repeat the <code>Z</code> option as many times has you have columns to test. Note: when more than one <code>Z</code> option is given then the <code>Iz</code> option cannot be used.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
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
<h2>UNITS</h2>
<p> For map distance unit, append <i>unit</i> <code>d</code> for arc degree, <code>m</code> for arc minute, and <code>s</code> for arc second, or <code>e</code> for meter [Default], <code>f</code> for foot, <code>k</code> for km, <code>M</code> for statute mile, <code>n</code> for nautical mile, and <code>u</code> for US survey foot. By default we compute such distances using a spherical approximation with great circles. Prepend <code>&#8211;</code> to a distance (or the unit is no distance is given) to perform &quot;Flat Earth&quot; calculations (quicker but less accurate) or prepend <code>+</code> to perform exact geodesic calculations (slower but more accurate).</p>
<h2>ASCII FORMAT PRECISION</h2>
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting. </p>
<p> This note applies to ASCII output only in combination with binary or netCDF input or the <code>-:</code> option. See also the note below.</p>
<h2>NOTE ON PROCESSING ASCII INPUT RECORDS</h2>
<p> Unless you are using the <code>-:</code> option, selected ASCII input records are copied verbatim to output. That means that options like <code>-foT</code> and settings like <i>FORMAT_FLOAT_OUT</i> and <i>FORMAT_GEO_OUT</i> will not have any effect on the output. On the other hand, it allows selecting records with diverse content, including character strings, quoted or not, comments, and other non-numerical content.</p>
<h2>NOTE ON DISTANCES</h2>
<p> If options <code>-C</code> or <code>-L</code> are selected then distances are Cartesian and in user units; use <code>-fg</code> to imply spherical distances in km and geographical (lon, lat) coordinates. Alternatively, specify <code>-R</code> and <code>-J</code> to measure projected Cartesian distances in map units (cm, inch, or points, as determined by <i>PROJ_LENGTH_UNIT</i>). </p>
<p> This program has evolved over the years. Originally, the <code>-R</code> and <code>-J</code> were mandatory in order to handle geographic data, but now there is full support for spherical calculations. Thus, <code>-J</code> should only be used if you want the tests to be applied on projected data and not the original coordinates. If <code>-J</code> is used the distances given via <code>-C</code> and <code>-L</code> are projected distances.</p>
<h2>NOTE ON SEGMENTS</h2>
<p> Segment headers in the input files are copied to output if one or more records from a segment passes the test. Selection is always done point by point, not by segment. That means only points from a segment that pass the test will be included in the output. If you wish to clip the lines and include the new boundary points at the segment ends you must use gmtspatial instead.</p>
<h2>EXAMPLES</h2>
<p> To extract the subset of data set that is within 300 km of any of the points in pts.d but more than 100 km away from the lines in lines.d, run </p>
<pre>
gmt select lonlatfile -fg -C300k/pts.d -L100/lines.d -Il &gt; subset
</pre>
<p> Here, you must specify <code>-fg</code> so the program knows you are processing geographical data. </p>
<p> To keep all points in data.d within the specified region, except the points on land (as determined by the high-resolution coastlines), use </p>
<pre>
gmt select data.d -R120/121/22/24 -Dh -Nk/s &gt; subset
</pre>
<p> To return all points in quakes.d that are inside or on the spherical polygon lonlatpath.d, try </p>
<pre>
gmt select quakes.d -Flonlatpath.d -fg &gt; subset1
</pre>
<p> To return all points in stations.d that are within 5 cm of the point in origin.d for a certain projection, try </p>
<pre>
gmt select stations.d -C5/origin.d -R20/50/-10/20 -JM20c \
--PROJ_LENGTH_UNIT=cm &gt; subset2
</pre>
<h2>GSHHS INFORMATION</h2>
<p> The coastline database is GSHHG (formerly GSHHS) which is compiled from three sources: World Vector Shorelines (WVS), CIA World Data Bank II (WDBII), and Atlas of the Cryosphere (AC, for Antarctica only). Apart from Antarctica, all level-1 polygons (ocean-land boundary) are derived from the more accurate WVS while all higher level polygons (level 2-4, representing land/lake, lake/island-in-lake, and island-in-lake/lake-in-island-in-lake boundaries) are taken from WDBII. The Antarctica coastlines come in two flavors: ice-front or grounding line, selectable via the <code>-A</code> option. Much processing has taken place to convert WVS, WDBII, and AC data into usable form for GMT: assembling closed polygons from line segments, checking for duplicates, and correcting for crossings between polygons. The area of each polygon has been determined so that the user may choose not to draw features smaller than a minimum area (see <code>-A</code>); one may also limit the highest hierarchical level of polygons to be included (4 is the maximum). The 4 lower-resolution databases were derived from the full resolution database using the Douglas-Peucker line-simplification algorithm. The classification of rivers and borders follow that of the WDBII. See the GMT Cookbook and Technical Reference Appendix K for further details.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtconvert</code>, <code>gmtsimplify</code>, <code>gmtspatial</code>, <code>grdlandmask</code>, <code>pscoast</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
