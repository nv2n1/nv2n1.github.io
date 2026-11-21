---

title: "kml2gmt(1)"
name: "kml2gmt"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kml2gmt/"
description: "kml2gmt – Extract GMT table data from Google Earth KML files"
---

<h2>NAME</h2>
<p> kml2gmt &#8211; Extract GMT table data from Google Earth KML files</p>
<p> <code>kml2gmt</code> [ <i>kmlfiles</i> ] [ <code>s</code>|<code>l</code>|<code>p</code> ] [ [<i>level</i>] ] [ ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<p> <code>kml2gmt</code> reads a Google Earth KML file and outputs a GMT table file. Only KML files that contain points, lines, or polygons can be processed. This is a bare-bones operation that aims to extract coordinates and possibly the name and description tags of each feature. The main use intended is to capture coordinates modified in Google Earth and then reinsert the modified data into the original GMT data file. For a more complete reformatting, consider using <code>ogr2ogr -f</code> &quot;GMT&quot; somefile.gmt somefile.kml.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>kmlfiles</i></dt>
<dd> Name of one or more KML files to work on. If not are given, then standard input is read.</dd>
<dt><code>-F</code><code>s</code>|<code>l</code>|<code>p</code></dt>
<dd> Specify a particular feature type to output. Choose from points (<code>s</code>), <code>l</code>ine, or <code>p</code>olygon. By default we output all geometries.</dd>
<dt><code>-Z</code></dt>
<dd> Output the altitude coordinates as GMT z coordinates [Default will output just longitude and latitude].</dd>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></dt>
<dd> Select verbosity level [c].</dd>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></dt>
<dd> Select native binary output.</dd>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></dt>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</dd>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></dt>
<dd> Swap 1st and 2nd column on input and/or output.</dd>
<dt><code>-^</code> or just <code>&#8211;</code></dt>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</dd>
<dt><code>-+</code> or just <code>+</code></dt>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</dd>
<dt><code>-?</code> or no arguments</dt>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</dd>
<dt><code>&#8211;</code><code>-version</code></dt>
<dd> Print GMT version and exit.</dd>
<dt><code>&#8211;</code><code>-show-datadir</code></dt>
<dd> Print full path to GMT share directory and exit.</dd></dl>
<h2>EXAMPLES</h2>
<p> To extract the lon,lat values from the KML file google.kml, try gmt kml2gmt google.kml -V &gt; google.txt </p>
<p> To separate the point and polygon geometries from the KML file google.kml, try gmt kml2gmt google.kml -Fp -V &gt; polygons.txt gmt kml2gmt google.kml -Fs -V &gt; points.txt</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>img2google</code>, <code>psconvert</code>, <code>gmt2kml</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
