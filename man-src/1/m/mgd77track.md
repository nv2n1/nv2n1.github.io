---
title: "mgd77track(1)"
name: "mgd77track"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77track/"
description: "mgd77track – Plot track-line map of MGD77 cruises"
---

<h2>NAME</h2>
<p> mgd77track &#8211; Plot track-line map of MGD77 cruises</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77track</code> <i>NGDC-ids</i> <i>region</i> <i>parameters</i> [ [<code>c</code>][<i>size</i>][,<i>spacing</i>] ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ <code>f</code>|<code>g</code>|<code>e</code> ] [ <code>-Da</code><i>startdate</i> ] [ <code>b</code><i>stopdate</i> ] [ ] [ <code>d</code>|<code>t</code>|<code>n</code><i>gap</i> ] [ <i>ignore</i> ] [ ] [ <i>trackticks</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>a</code><i>startdist</i>[<code>u</code>] ] [ <code>b</code><i>stopdist</i>[<code>u</code>] ] [ <code>T</code>|<code>t</code>|<code>d</code><i>ms</i>,<i>mc</i>,<i>mfs</i>,<i>mf</i>,<i>mfc</i> ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<code>&#8211;</code>|<code>+</code>][<i>pen</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77track</code> reads NGDC MGD77 cruises and creates PostScript code that will plot one or more ship tracks on a map using the specified projection. The PostScript code is written to standard output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>NGDC-ids</i></p>
<dd> Can be one or more of five kinds of specifiers:</p>
<dt>1.</p>
<dd> 8-character NGDC IDs, e.g., 01010083, JA010010etc., etc.</p>
<dt>2.</p>
<dd> 2-character &lt;agency&gt; codes which will return all cruises from each agency.</p>
<dt>3.</p>
<dd> 4-character &lt;agency&gt;&lt;vessel&gt; codes, which will return all cruises from those vessels.</p>
<dt>4.</p>
<dd> =&lt;list&gt;, where &lt;list&gt; is a table with NGDC IDs, one per line.</p>
<dt>5.</p>
<dd> If nothing is specified we return all cruises in the data base. </p>
<p> (See mgd77info <code>-L</code> for agency and vessel codes). The &quot;.mgd77&quot; or &quot;.nc&quot; extensions will automatically be appended, if needed (use <code>-I</code> to ignore certain file types). Cruise files will be looked for first in the current directory and second in all directories listed in <code>$MGD77_HOME</code>/mgd77_paths.txt [If <code>$MGD77_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/mgd77].</p>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>c</code>][<i>size</i>][,<i>spacing</i>]</p>
<dd> Append <code>c</code> to annotate using the MGD77 cruise ID [Default uses the filename prefix]. Optional <i>size</i> is the font size in points. The leg annotation font is controlled by <i>FONT_LABEL</i>. By default, each leg is annotated every time it enters the map region. Alternatively, append ,<i>spacing</i> to place this label every <i>spacing</i> units apart along the track. Append one of the units <code>k</code> (km), <code>n</code> (nautical mile), <code>d</code> (day), or <code>h</code> (hour).</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals.</p>
<dt><code>-C</code><code>f</code>|<code>g</code>|<code>e</code></p>
<dd>
<dt><code>Select procedure for along-track distance calculation:</code></p>
<dd> <code>f</code> Flat Earth distances. <code>g</code> Great circle distances [Default]. <code>e</code> Geodesic distances on current GMT ellipsoid.</p>
<dt><code>-Da</code><i>startdate</i></p>
<dd> Do not plot data collected before <i>startdate</i> (yyyy-mm-dd<code>T</code>[hh:mm:ss]) [Default is first day].</p>
<dt><code>-Db</code><i>stopdate</i></p>
<dd> Do not plot data collected after <i>stopdate</i> (yyyy-mm-dd<code>T</code>[hh:mm:ss]). [Default is last day].</p>
<dt><code>-F</code></p>
<dd> Do not apply the error bit flags if present in a MGD77+ file [Default will apply these flags upon reading the data].</p>
<dt><code>-G</code><code>d</code>|<code>t</code>|<code>n</code><i>gap</i></p>
<dd> Let successive point separations exceeding <code>d</code><i>gap</i> (km) or <code>t</code><i>gap</i> (minutes) indicate a break in the track where we should not draw a line [no gaps recognized]. Repeat to use both types of gap checking. The <code>n</code><i>N</i> form is used to plot only one every other <i>N</i> points. This is useful to reduce plot file size bat cannot be used (will be ignored) with the other two gap types.</p>
<dt><code>-I</code><i>ignore</i></p>
<dd> Ignore certain data file formats from consideration. Append <code>a|c|t</code> to ignore MGD77 ASCII, MGD77+ netCDF, or plain table files, respectively. The option may be repeated to ignore more than one format. [Default ignores none].</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code><i>trackticks</i></p>
<dd> To put time/distance log-marks on the track. E.g. <code>a</code>500<code>ka</code>24<code>ht</code>6<code>h</code> means (<code>a</code>)nnotate every 500 km (<code>k</code>) and 24 <code>h</code>(ours), with (<code>t</code>)ickmarks every 500 km and 6 hours. Alternatively you may use the modifiers <code>d</code> (days) and <code>n</code> (nautical miles).</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-Sa</code><i>startdist</i>[<code>u</code>]</p>
<dd> Do not plot data that are less than <i>startdist</i> meter along track from port of departure. Append <code>k</code> for km, <code>m</code> for miles, or <code>n</code> for nautical miles [Default is 0 meters].</p>
<dt><code>-Sb</code><i>stopdist</i>[<code>u</code>]</p>
<dd> Do not plot data that are more than <i>stopdist</i> meter along track from port of departure. Append <code>k</code> for km, <code>m</code> for miles, or <code>n</code> for nautical miles [Default is end of track].</p>
<dt><code>-TT</code>|<code>t</code>|<code>d</code><i>ms</i>,<i>mc</i>,<i>mfs</i>,<i>mf</i>,<i>mfc</i></p>
<dd> Controls the attributes of the three kinds of markers (<code>T</code> for the first time marker in a new day, <code>t</code> for additional time markers in the same day, and <code>d</code> for distance markers). For each of these you can specify the 5 comma-separated attributes <i>markersize</i>, <i>markercolor</i>, <i>markerfontsize</i>, <i>markerfont</i>, and <i>markerfontcolor</i>. Repeat the <code>-T</code> option for each marker type.</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-W</code>[<code>&#8211;</code>|<code>+</code>][<i>pen</i>]</p>
<dd> Append <i>pen</i> used for the trackline. [Defaults: width = default, color = black, style = solid]. A leading <code>+</code> will use the lookup color (via <code>-C</code>) for both symbol fill and outline pen color, while a leading <code>&#8211;</code> will set outline pen color and turn off symbol fill. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
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
<p> To generate a Mercator plot of the track of the cruise 01010007 in the area 70W to 20E, 40S to 20N, using a Mercator scale of 0.1inch/degree, label the tracks with 10 points characters, annotate the boundaries every 10 degrees, draw gridlines every 5 degrees, and mark the track every day and 1000 km, with ticks every 6 hours and 250 km, and send the plot to the default printer, enter the following command: </p>
<pre>
gmt mgd77track 01010007 -R70W/20E/40S/20N -Jm0.1 -B10g5 -A10 \
               -La1da1000kf6hf250k \| lpr
</pre>
<h2>SEE ALSO</h2>
<p> <code>mgd77info</code>, <code>psbasemap</code>, <code>mgd77list</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
