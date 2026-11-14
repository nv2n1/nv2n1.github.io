---
title: "psrose(1)"
name: "psrose"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psrose/"
description: "psrose – Plot a polar histogram (rose, sector, windrose diagrams)"
---

<h2>NAME</h2>
<p> psrose &#8211; Plot a polar histogram (rose, sector, windrose diagrams)</p>
<h2>SYNOPSIS</h2>
<p> <code>psrose</code> [ <i>table</i> ] [ [<code>r</code>]<i>sector_width</i> ] [ [<code>p</code>|<code>s</code>]<i>parameters</i> ] [ [<i>mode_file</i>] ] [ ] [ <i>fill</i> ] [ ] [ ] [ [<i>wlabel</i>/<i>elabel</i>/<i>slabel</i>/<i>nlabel</i>] ] [ <i>parameters</i> ] [ ] [ ] [ <i>r0</i>/<i>r1</i>/<i>az_0</i>/<i>az_1</i> ] [ [<code>n</code>]*radial_scale* ] [ ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ [<code>v</code>]<i>pen</i> ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>u</code>|<i>scale</i> ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>psrose</code> reads (length,azimuth) pairs from <i>file</i> [or standard input] and generates PostScript code that will plot a windrose diagram. Optionally (with <code>-A</code>), polar histograms may be drawn (sector diagram or rose diagram). Options include full circle and half circle plots. The PostScript code is written to standard output. The outline of the windrose is drawn with the same color as <code>MAP_DEFAULT_PEN</code>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input. If a file with only azimuths are given, use <code>-i</code> to indicate the single column with azimuths; then all lengths are set to unity (see <code>-Zu</code> to set actual lengths to unity as well).</p>
<dt><code>-A</code>[<code>r</code>]<i>sector_width</i></p>
<dd> Gives the sector width in degrees for sector and rose diagram. [Default 0 means windrose diagram]. Use <code>-Ar</code> to draw rose diagram instead of sector diagram.</p>
<dt><code>-B</code>[<code>p</code>|<code>s</code>]<i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Set map boundary intervals. </p>
<pre>
Remember that &quot;x&quot; here is
radial distance and &quot;y&quot; is azimuth. The ylabel may be used to plot a figure caption.
</pre>
<dt><code>-C</code>[<i>mode_file</i>]</p>
<dd> Plot vectors showing the principal directions given in the <i>modes</i> file. If no file is given, compute and plot mean direction. See <code>-M</code> to control vector attributes.</p>
<dt><code>-D</code></p>
<dd> Shift sectors so that they are centered on the bin interval (e.g., first sector is centered on 0 degrees).</p>
<dt><code>-F</code></p>
<dd> Do not draw the scale length bar [Default plots scale in lower right corner]</p>
<dt><code>-G</code><i>fill</i></p>
<dd> Selects shade, color or pattern for filling the sectors [Default is no fill]K.</p>
<dt><code>-I</code></p>
<dd> Inquire. Computes statistics needed to specify useful <code>-R</code>. No plot is generated.</p>
<dt><code>-K</code> <i>(more &#8230;)</i></p>
<dd> Do not finalize the PostScript plot.</p>
<dt><code>-L</code>[<i>wlabel</i>/<i>elabel</i>/<i>slabel</i>/<i>nlabel</i>]</p>
<dd> Specify labels for the 0, 90, 180, and 270 degree marks. For full-circle plot the default is WEST/EAST/SOUTH/NORTH and for half-circle the default is 90W/90E/-/0. A &#8211; in any entry disables that label. Use <code>-L</code> with no argument to disable all four labels</p>
<dt><code>-M</code><i>parameters</i></p>
<dd> Used with <code>-C</code> to modify vector parameters. For vector heads, append vector head <i>size</i> [Default is 0, i.e., a line]. See VECTOR ATTRIBUTES for specifying additional attributes.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-R</code><i>r0</i>/<i>r1</i>/<i>az_0</i>/<i>az_1</i></p>
<dd> Specifies the &#8216;region&#8217; of interest in (r,azimuth) space. r0 is 0, r1 is max length in units. For azimuth, specify either -90/90 or 0/180 for half circle plot or 0/360 for full circle.</p>
<dt><code>-S</code>[<code>n</code>]*radial_scale*</p>
<dd> Specifies radius of circle. Use <code>-Sn</code> to normalize input radii to go from 0 to 1.</p>
<dt><code>-T</code></p>
<dd> Specifies that the input data is orientation data (has a 180 degree ambiguity) instead of true 0-360 degree directions [Default].</p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>pen</i></p>
<dd> Set pen attributes for sector outline or rose plot. [Default is no outline]. Use <code>-Wv</code><i>pen</i> to change pen used to draw vector (requires <code>-C</code>) [Default is same as sector outline]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-Z</code><i>scale</i></p>
<dd> Multiply the data radii by <i>scale</i>. E.g., use <code>-Z</code>0.001 to convert your data from m to km. To exclude the radii from consideration, set them all to unity with <code>-Zu</code> [Default is no scaling].</p>
<dt><code>-:</code></p>
<dd> Input file has (azimuth,radius) pairs rather than the expected (radius,azimuth).</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>VECTOR ATTRIBUTES</h2>
<p> Several modifiers may be appended to the vector-producing options to specify the placement of vector heads, their shapes, and the justification of the vector. Below, left and right refers to the side of the vector line when viewed from the start point to the end point of the segment: <code>+a</code><i>angle</i> sets the angle of the vector head apex [30]. </p>
<p> <code>+b</code> places a vector head at the beginning of the vector path [none]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. </p>
<p> <code>+e</code> places a vector head at the end of the vector path [none]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. </p>
<p> <code>+g</code>-|<i>fill</i> turns off vector head fill (if -) or sets the vector head fill [Default fill is used, which may be no fill]. </p>
<p> <code>+l</code> draws half-arrows, using only the left side of specified heads [both sides]. </p>
<p> <code>+m</code> places a vector head at the mid-point the vector path [none]. Append <code>f</code> or <code>r</code> for forward or reverse direction of the vector [forward]. Optionally, append <code>t</code> for a terminal line, <code>c</code> for a circle, or <code>a</code> for arrow head [Default]. Further append <code>l</code>|<code>r</code> to only draw the left or right side of this head [both sides]. Cannot be combined with <code>+b</code> or <code>+e</code>. </p>
<p> <code>+n</code><i>norm</i> scales down vector attributes (pen thickness, head size) with decreasing length, where vectors shorter than <i>norm</i> will have their attributes scaled by length/<i>norm</i> [arrow attributes remains invariant to length]. </p>
<p> <code>+o</code><i>plon</i>/<i>plat</i> specifies the oblique pole for the great or small circles. Only needed for great circles if <code>+q</code> is given. </p>
<p> <code>+p</code>[-][<i>pen</i>] sets the vector pen attributes. If <i>pen</i> has a leading &#8211; then the head outline is not drawn. [Default pen is used, and head outline is drawn] </p>
<p> <code>+q</code> means the input <i>angle</i>, <i>length</i> data instead represent the <i>start</i> and <i>stop</i> opening angles of the arc segment relative to the given point. </p>
<p> <code>+r</code> draws half-arrows, using only the right side of specified heads [both sides]. </p>
<p> <code>t</code>[<code>b</code>|<code>e</code>]<i>trim</i> will shift the beginning or end point (or both) along the vector segment by the given <i>trim</i>; append suitable unit. If the modifiers <code>b</code>|<code>e</code> are not used then <i>trim</i> may be two values separated by a slash, which is used to specify different trims for the two ends. Positive trims will shorted the vector while negative trims will lengthen it [no trim]. </p>
<p> In addition, all but circular vectors may take these modifiers: <code>+j</code><i>just</i> determines how the input <i>x</i>,<i>y</i> point relates to the vector. Choose from <code>b</code>eginning [default], <code>e</code>nd, or <code>c</code>enter. </p>
<p> <code>+s</code> means the input <i>angle</i>, <i>length</i> is instead the <i>x</i>, <i>y</i> coordinates of the vector end point. </p>
<p> Finally, Cartesian vectors may take these modifiers: <code>+z</code><i>scale</i>[<i>unit</i>] expects input <i>dx</i>,<i>dy</i> vector components and uses the <i>scale</i> to convert to polar coordinates with length in given unit.</p>
<h2>EXAMPLES</h2>
<p> To plot a half circle rose diagram of the data in the file fault_segments.az_r (containing pairs of (azimuth, length in meters), using a 10 degree bin sector width, on a circle of radius = 3 inch, grid going out to radius = 150 km in steps of 25 km with a 30 degree sector interval, radial direction annotated every 50 km, using a light blue shading outlined by a solid red pen (width = 0.75 points), draw the mean azimuth, and shown in Portrait orientation, use: </p>
<pre>
gmt psrose fault_segments.az_r -R0/150/-90/90 -Bx50g25+l&quot;Fault length&quot;
           -Byg30 -B+t&quot;Rose diagram&quot;-S3i -Ar10 -Glightblue
           -W0.75p,red -Z0.001 -C -P -T -: &gt; half_rose.ps
</pre>
<p> To plot a full circle wind rose diagram of the data in the file lines.r_az, on a circle of radius = 5 cm, grid going out to radius = 500 units in steps of 100 with a 45 degree sector interval, using a solid pen (width = 0.5 point, and shown in landscape [Default] orientation with UNIX timestamp and command line plotted, use: </p>
<pre>
gmt psrose lines.az_r -R0/500/0/360 -S5c -Bxg100 -Byg45 -B+t&quot;Windrose diagram&quot; -W0.5p -Uc | lpr
</pre>
<h2>BUGS</h2>
<p> No default radial scale and grid settings for polar histograms. User must run <code>psrose</code> <code>-I</code> to find max length in binned data set.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtcolors</code>, <code>pshistogram</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
