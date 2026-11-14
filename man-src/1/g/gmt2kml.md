---
title: "gmt2kml(1)"
name: "gmt2kml"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmt2kml/"
description: "gmt2kml – Convert GMT data tables to KML files for Google Earth"
---

<h2>NAME</h2>
<p> gmt2kml &#8211; Convert GMT data tables to KML files for Google Earth</p>
<h2>SYNOPSIS</h2>
<p> <code>gmt2kml</code> [ <i>table</i> ] [ <code>a</code>|<code>g</code>|<code>s</code>[<i>alt</i>|<code>x</code><i>scale</i>] ] [ <i>cpt</i> ] [ <i>descriptfile</i> ] [ [<i>altitude</i>] ] [ <code>e</code>|<code>s</code>|<code>t</code>|<code>l</code>|<code>p</code> ] [ <code>f|n</code><code>&#8211;</code>|<i>fill</i> ] [ <i>icon</i> ] [ <code>-K</code>] [ <i>col1:name1</i>,<i>col2:name2</i>,&#8230; ] [ [+|*name_template*|<i>name</i>] ] [ <code>-O</code>] [ <code>a</code>|<i>w/e/s/n</i> ] [ <code>c</code>|<code>n</code><i>scale</i>] ] [ <i>title</i>[/<i>foldername</i>] ] [ [<i>level</i>] ] [ [<code>&#8211;</code>|<code>+</code>]<i>pen</i> ] [ <i>args</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] [ &gt; <i>output.kml</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmt2kml</code> reads one or more GMT table file and converts them to a single output file using Google Earth&#8217;s KML format. Data may represent points, lines, or polygons, and you may specify additional attributes such as title, altitude mode, colors, pen widths, transparency, regions, and data descriptions. You may also extend the feature down to ground level (assuming it is above it) and use custom icons for point symbols. </p>
<p> The input files should contain the following columns: </p>
<p> <i>lon</i> <i>lat</i> [ <i>alt</i> ] [ <i>timestart</i> [ <i>timestop</i> ] ] </p>
<p> where <i>lon</i> and <i>lat</i> are required for all features, <i>alt</i> is optional for all features (see also <code>-A</code> and <code>-C</code>), and <i>timestart</i> and <i>timestop</i> apply to events and timespan features.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code><code>a</code>|<code>g</code>|<code>s</code>[<i>alt</i>|<code>x</code><i>scale</i>]</p>
<dd> Select one of three altitude modes recognized by Google Earth that determines the altitude (in m) of the feature: <code>a</code> absolute altitude, <code>g</code> altitude relative to sea surface or ground, <code>s</code> altitude relative to seafloor or ground. To plot the features at a fixed altitude, append an altitude <i>alt</i> (in m). Use 0 to clamp the features to the chosen reference surface. Append <code>x</code><i>scale</i> to scale the altitude from the input file by that factor. If no value is appended, the altitude (in m) is read from the 3rd column of the input file. [By default the features are clamped to the sea surface or ground].</p>
<dt><code>-C</code><i>cpt</i></p>
<dd> Use the CPT file for assigning colors to the symbol, event, or timespan icons, based on the value in the 3rd column of the input file. For lines or polygons we examine the segment header for -Z&lt;value&gt; statements and obtain the color via the cpt lookup. Note only discrete colors are possible.</p>
<dt><code>-D</code><i>descriptfile</i></p>
<dd> File with HTML snippets that will be included as part of the main description content for the KML file [no description]. See SEGMENT INFORMATION below for feature-specific descriptions.</p>
<dt><code>-E</code>[<i>altitude</i>]</p>
<dd> Extrude feature down to ground level [no extrusion].</p>
<dt><code>-F</code><code>e</code>|<code>s</code>|<code>t</code>|<code>l</code>|<code>p</code></p>
<dd> Sets the feature type. Choose from points (<code>e</code>vent, <code>s</code>ymbol, or <code>t</code>imespan), <code>l</code>ine, or <code>p</code>olygon [symbol]. The first two columns of the input file should contain (<i>lon</i>, <i>lat</i>). When altitude or value is required (i.e., no <i>altitude</i> value was given with <code>-A</code>, or <code>-C</code> is set), the third column needs to contain the <i>altitude</i> (in m) or <i>value</i>. The event (<code>-Fe</code>) is a symbol that should only be active at a particular <i>time</i>, given in the next column. Timespan (<code>-Ft</code>) is a symbol that should only be active during a particular time period indicated by the next two columns (<i>timestart</i>, <i>timestop</i>). Use NaN to indicate unbounded time limits. If used, times should be in ISO format yyyy-mm-ddThh:mm:ss[.xxx] or in GMT relative time format (see <code>-f</code>).</p>
<dt><code>-G</code><code>f|n</code><i>fill</i></p>
<dd> Set fill color for symbols, extrusions and polygons (<code>-Gf</code>) [Default is light orange at 75% transparency] or text labels (<code>-Gn</code>) [Default is white]. Optionally, use <code>-Gf-</code> to turn off polygon fill, and <code>-Gn-</code> to disable labels.</p>
<dt><code>-I</code><i>icon</i></p>
<dd> Specify the URL to an alternative icon that should be used for the symbol [Default is a Google Earth circle]. If the URL starts with + then we will prepend <i><a rel="nofollow" href="http://maps.google.com/mapfiles/kml/">http://maps.google.com/mapfiles/kml/</a></i> to the name. To turn off icons entirely (e.g., when just wanting a text label), use <code>-I</code>-. [Default is a local icon with no directory path].</p>
<dt><code>-K</code></p>
<dd> Allow more KML code to be appended to the output later [finalize the KML file].</p>
<dt><code>-L</code><i>name1</i>,<i>name2</i>,&#8230;</p>
<dd> Extended data given. Append one or more column names separated by commas. We will expect the listed data columns to exist in the input immediately following the data coordinates and they will be encoded in the KML file as Extended Data sets, whose attributes will be available in the Google Earth balloon when the item is selected. This option is not available unless input is an ASCII file.</p>
<dt><code>-N</code>[-|+|<i>name_template</i>|<i>name</i>]</p>
<dd> By default, if segment headers contain a <code>-L</code>&quot;label string&quot; then we use that for the name of the KML feature (polygon, line segment or set of symbols). Default names for these segments are &quot;Line %d&quot; and &quot;Point Set %d&quot;, depending on the feature, where %d is a sequence number of line segments within a file. Each point within a line segment will be named after the line segment plus a sequence number. Default is simply &quot;Point %d&quot;. Alternatively, select one of these options: (1) append <code>&#8211;</code> to supply individual symbol labels (single word) via the field immediately following the data coordinates, (2) append <code>+</code> to supply individual symbol labels as the rest the end of the data record following the data coordinates, (3) append a string that may include %d or a similar integer format to assign unique name IDs for each feature, with the segment number (for lines and polygons) or point number (symbols) appearing where %d is placed, (4) give no arguments to turn symbol labeling off; line segments will still be named. Note: if <code>-N-</code> is used with <code>-L</code> then the label must appear before the extended data columns. Also note that options (1) and (2) are not available unless input is an ASCII file.</p>
<dt><code>-O</code></p>
<dd> Appended KML code to an existing KML file [initialize a new KML file].</p>
<dt><code>-Ra</code>|<i>w/e/s/n</i></p>
<dd> Issue a single Region tag. Append <i>w/e/s/n</i> to set a particular region (will ignore points outside the region), or append <code>a</code> to determine and use the actual domain of the data (single file only) [no region tags issued].</p>
<dt><code>-S</code><code>c</code>|<code>n</code><i>scale</i>]</p>
<dd> Scale icons or labels. Here, <code>-Sc</code> sets a scale for the symbol icon, whereas <code>-Sn</code> sets a scale for the name labels [1 for both].</p>
<dt><code>-T</code><i>title</i>[/<i>foldername</i>]</p>
<dd> Sets the document title [default is unset]. Optionally, append /<i>FolderName</i>; this allows you, with <code>-O</code>, <code>-K</code>, to group features into folders within the KML document. [The default folder name is &quot;<i>Name</i> Features&quot;, where <i>Name</i> is Point, Event, Timespan, Line, or Polygon].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>&#8211;</code>|<code>+</code>]<i>pen</i></p>
<dd> Set pen attributes for lines or polygon outlines. Append pen attributes to use [Defaults: width = default, color = black, style = solid]. If <code>-C</code> is given you may optionally use <code>-W-</code> to apply the cpt color to the polygon outline only (fill determined by <code>-G</code>) or <code>-W+</code> to use the cpt color for both polygon fill and outline. Note that for KML the pen width is given as integer pixel widths so you must specify pen width as <i>n</i><code>p</code>, where <i>n</i> is an integer.</p>
<dt><code>-Z</code><i>args</i></p>
<dd> Set one or more attributes of the Document and Region tags. Append <code>+a</code><i>alt_min/alt_max</i> to specify limits on visibility based on altitude. Append <code>+l</code><i>lod_min/lod_max</i> to specify limits on visibility based on Level Of Detail, where <i>lod_max</i> == -1 means it is visible to infinite size. Append <code>+f</code><i>fade_min/fade_max</i> to fade in and out over a ramp [abrupt]. Append <code>+v</code> to make a feature <i>not</i> visible when loaded [visible]. Append <code>+o</code> to open a folder or document in the sidebar when loaded [closed].</p>
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
<p> To convert a file with point locations (lon, lat) into a KML file with red circle symbols, try </p>
<pre>
gmt2kml mypoints.txt -Gfred -Fs &gt; mypoints.kml
</pre>
<p> To convert a multisegment file with lines (lon, lat) separated by segment headers that contain a <code>-L</code>labelstring with the feature name, selecting a thick white pen, and title the document, try </p>
<pre>
gmt2kml mylines.txt -Wthick,white -Fl -T&quot;Lines from here to there&quot; &gt; mylines.kml
</pre>
<p> To convert a multisegment file with polygons (lon, lat) separated by segment headers that contain a <code>-L</code>labelstring with the feature name, selecting a thick black pen and semi-transparent yellow fill, giving a title to the document, and prescribing a particular region limit, try </p>
<pre>
gmt gmt2kml mypolygons.txt -Gfyellow@50 -Fp -T&quot;My polygons&quot; -R30/90/-20/40 &gt; mypolygons.kml
</pre>
<p> To convert a file with point locations (lon, lat, time) into a KML file with green circle symbols that will go active at the specified time and stay active going forward, try </p>
<pre>
awk '{print $1, $2, $3, &quot;NaN&quot;}' mypoints.txt | gmt gmt2kml -Gfgreen -Ft &gt; mytimepoints.kml
</pre>
<p> To extract contours and labels every 10 units from the grid temp.nc and plot them in KML, using red lines at 75% transparency and red labels (no transparency), try </p>
<pre>
gmt grdcontour temp.nc -Jx1id -A10+tlabel.txt -C10 -Dcontours.txt
gmt gmt2kml    contours.txt -Fl -W1p,red@75 -K &gt; contours.kml
gmt gmt2kml    -O -N+ -Fs -Sn2 -Gnred@0 label.txt -I- &gt;&gt; contours.kml
</pre>
<p> To instead plot the contours as lines with colors taken from the cpt file contours.cpt, try </p>
<pre>
gmt gmt2kml contours.txt -Fl -Ccontours.cpt &gt; contours.kml
</pre>
<h2>LIMITATIONS</h2>
<p> Google Earth has trouble displaying filled polygons across the Dateline. For now you must manually break any polygon crossing the dateline into a west and east polygon and plot them separately.</p>
<h2>MAKING KMZ FILES</h2>
<p> Using the KMZ format is preferred as it takes less space. KMZ is simply a KML file and any data files, icons, or images referenced by the KML, contained in a zip archive. One way to organize large data sets is to split them into groups called Folders. A Document can contain any number of folders. Using scripts you can create a composite KML file using the <code>-K</code>, <code>-O</code> options just like you do with GMT plots. See <code>-T</code> for switching between folders and documents.</p>
<h2>KML HIERARCHY</h2>
<p> GMT stores the different features in hierarchical folders by feature type (when using <code>-O</code>, <code>-K</code> or <code>-T/</code><i>foldername</i>), by input file (if not standard input), and by line segment (using the name from the segment header, or <code>-N</code>). This makes it more easy in Google Earth to switch on or off parts of the contents of the Document. The following is a crude example: </p>
<p> [ KML header information; not present if <code>-O</code> was used ] </p>
<p> &lt;Document&gt;&lt;name&gt;GMT Data Document&lt;/name&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;Point Features&lt;/name&gt; </p>
<p> &lt;!&#8211;This level of folder is inserted only when using -O, -K&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;file1.dat&lt;/name&gt; </p>
<p> &lt;!&#8211;One folder for each input file (not when standard input)&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;Point Set 0&lt;/name&gt; </p>
<p> &lt;!&#8211;One folder per line segment&gt; </p>
<p> &lt;!&#8211;Points from the first line segment in file file1.dat go here&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;Point Set 1&lt;/name&gt; </p>
<p> &lt;!&#8211;Points from the second line segment in file file1.dat go here&gt; </p>
<p> &lt;/Folder&gt; </p>
<p> &lt;/Folder&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;Line Features&lt;/name&gt; </p>
<p> &lt;Folder&gt;&lt;name&gt;file1.dat&lt;/name&gt; </p>
<p> &lt;!&#8211;One folder for each input file (not when standard input)&gt; </p>
<p> &lt;Placemark&gt;&lt;name&gt;Line 0&lt;/name&gt; </p>
<p> &lt;!&#8211;Here goes the first line segment&gt; </p>
<p> &lt;/Placemark&gt; </p>
<p> &lt;Placemark&gt;&lt;name&gt;Line 1&lt;/name&gt; </p>
<p> &lt;!&#8211;Here goes the second line segment&gt; </p>
<p> &lt;/Placemark&gt; </p>
<p> &lt;/Folder&gt; </p>
<p> &lt;Folder&gt; </p>
<p> &lt;/Document&gt; </p>
<p> [ KML trailer information; not present if <code>-K</code> was used ]</p>
<h2>SEGMENT INFORMATION</h2>
<p> <code>gmt2kml</code> will scan the segment headers for substrings of the form <code>-L</code>&quot;<i>some label</i>&quot; [also see <code>-N</code> discussion] and <code>-T</code>&quot;<i>some text description</i>&quot;. If present, these are parsed to supply name and description tags, respectively, for the current feature.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code> , <code>gmt.conf</code>, <code>img2google</code>, <code>kml2gmt</code> , <code>psconvert</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
