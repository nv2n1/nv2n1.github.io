---
title: "mapproject(1)"
name: "mapproject"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mapproject/"
description: "mapproject – Do forward and inverse map transformations, datum conversions and geodesy"
---

<h2>NAME</h2>
<p> mapproject &#8211; Do forward and inverse map transformations, datum conversions and geodesy</p>
<h2>SYNOPSIS</h2>
<p> <code>mapproject</code> [ <i>tables</i> ] <i>parameters</i> <i>region</i> [ <code>b</code>|<code>B</code>|<code>f</code>|<code>F</code>|<code>o</code>|<code>O</code>[<i>lon0</i>/<i>lat0</i>] ] [ [<i>dx</i>/<i>dy</i>] ] [ <code>c</code>|<code>i</code>|<code>p</code> ] [ [<i>datum</i>] ] [ [<i>unit</i>] ] [ [<i>x0</i>/<i>y0</i>/][[<code>+</code>|<code>&#8211;</code>]<i>unit</i>][<code>+</code>|<code>&#8211;</code>] ] [ ] [ <i>line.xy</i>[/[<code>+</code>|<code>&#8211;</code>]<i>unit</i>][<code>+</code>] ] [ [<code>a</code>|<code>c</code>|<code>g</code>|<code>m</code>] ] [ [<code>d</code>|<code>e</code> ] [ ] [ [<code>h</code>]<i>from</i>[/<i>to</i>] ] [ [<i>level</i>] ] [ [<code>w</code>|<code>h</code>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-f</code><i>&lt;flags&gt;</i> ] [ <code>-g</code><i>&lt;gaps&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-p</code><i>&lt;flags&gt;</i> ] [ <code>-s</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mapproject</code> reads (longitude, latitude) positions from <i>tables</i> [or standard input] and computes (x,y) coordinates using the specified map projection and scales. Optionally, it can read (x,y) positions and compute (longitude, latitude) values doing the inverse transformation. This can be used to transform linear (x,y) points obtained by digitizing a map of known projection to geographical coordinates. May also calculate distances along track, to a fixed point, or closest approach to a line. Finally, can be used to perform various datum conversions. Additional data fields are permitted after the first 2 columns which must have (longitude,latitude) or (x,y). See option <code>-:</code> on how to read (latitude,longitude) files.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-J</code><i>parameters</i> <i>(more &#8230;)</i></p>
<dd> Select map projection.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. Special case for the UTM projection: If <code>-C</code> is used and <code>-R</code> is not given then the region is set to coincide with the given UTM zone so as to preserve the full ellipsoidal solution (See RESTRICTIONS for more information).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-Ab</code>|<code>B</code>|<code>f</code>|<code>F</code>|<code>o</code>|<code>O</code>[<i>lon0</i>/<i>lat0</i>]</p>
<dd> <code>-Af</code> calculates the (forward) azimuth from fixed point <i>lon/lat</i> to each data point. Use <code>-Ab</code> to get back-azimuth from data points to fixed point. Use <code>-Ao</code> to get orientations (-90/90) rather than azimuths (0/360). Upper case <code>F</code>, <code>B</code> or <code>O</code> will convert from geodetic to geocentric latitudes and estimate azimuth of geodesics (assuming the current ellipsoid is not a sphere). If no fixed point is given then we compute the azimuth (or back-azimuth) from the previous point.</p>
<dt><code>-C</code>[<i>dx</i>/<i>dy</i>]</p>
<dd> Set center of projected coordinates to be at map projection center [Default is lower left corner]. Optionally, add offsets in the projected units to be added (or subtracted when <code>-I</code> is set) to (from) the projected coordinates, such as false eastings and northings for particular projection zones [0/0]. The unit used for the offsets is the plot distance unit in effect (see <i>PROJ_LENGTH_UNIT</i>) unless <code>-F</code> is used, in which case the offsets are in meters.</p>
<dt><code>-Dc</code>|<code>i</code>|<code>p</code></p>
<dd> Temporarily override <i>PROJ_LENGTH_UNIT</i> and use <code>c</code> (cm), <code>i</code> (inch), or <code>p</code> (points) instead. Cannot be used with <code>-F</code>.</p>
<dt><code>-E</code>[<i>datum</i>]</p>
<dd> Convert from geodetic (lon, lat, height) to Earth Centered Earth Fixed (ECEF) (x,y,z) coordinates (add <code>-I</code> for the inverse conversion). Append datum ID (see <code>-Qd</code>) or give <i>ellipsoid</i>:<i>dx</i>,<i>dy</i>,<i>dz</i> where <i>ellipsoid</i> may be an ellipsoid ID (see <code>-Qe</code>) or given as <i>a</i>[,*inv_f*], where <i>a</i> is the semi-major axis and <i>inv_f</i> is the inverse flattening (0 if omitted). If <i>datum</i> is &#8211; or not given we assume WGS-84.</p>
<dt><code>-F</code>[<i>unit</i>]</p>
<dd> Force 1:1 scaling, i.e., output (or input, see <code>-I</code>) data are in actual projected meters. To specify other units, append the desired unit (see UNITS). Without <code>-F</code>, the output (or input, see <code>-I</code>) are in the units specified by <i>PROJ_LENGTH_UNIT</i> (but see <code>-D</code>).</p>
<dt><code>-G</code>[<i>x0</i>/<i>y0</i>/][[<code>+</code>|<code>&#8211;</code>]<i>unit</i>][<code>+</code>|<code>&#8211;</code>]</p>
<dd> Calculate distances along track <i>or</i> to the optional point set with <code>-G</code><i>x0/y0</i>. Append the distance unit (see UNITS), including <code>c</code> (Cartesian distance using input coordinates) or <code>C</code> (Cartesian distance using projected coordinates). The <code>C</code> unit requires <code>-R</code> and <code>-J</code> to be set. With no fixed point is given we calculate cumulate distances along track. Append <code>&#8211;</code> to obtain incremental distance between successive points. Append <code>+</code> to specify the 2nd point via two extra columns in the input file.</p>
<dt><code>-I</code></p>
<dd> Do the Inverse transformation, i.e., get (longitude,latitude) from (x,y) data.</p>
<dt><code>-L</code><i>line.xy</i>[/[<code>+</code>|<code>&#8211;</code>]<i>unit</i>][<code>+</code>]</p>
<dd> Determine the shortest distance from the input data points to the line(s) given in the ASCII multisegment file <i>line.xy</i>. The distance and the coordinates of the nearest point will be appended to the output as three new columns. Append the distance unit (see UNITS), including <code>c</code> (Cartesian distance using input coordinates) or <code>C</code> (Cartesian distance using projected coordinates). The <code>C</code> unit requires <code>-R</code> and <code>-J</code> to be set. Finally, append <code>+</code> to report the line segment id and the fractional point number instead of lon/lat of the nearest point.</p>
<dt><code>-N</code>[<code>a</code>|<code>c</code>|<code>g</code>|<code>m</code>]</p>
<dd> Convert from geodetic latitudes (using the current ellipsoid; see <i>PROJ_ELLIPSOID</i>) to one of four different auxiliary latitudes (longitudes are unaffected). Choose from <code>a</code>uthalic, <code>c</code>onformal, <code>g</code>eocentric, and <code>m</code>eridional latitudes [geocentric]. Use <code>-I</code> to convert from auxiliary latitudes to geodetic latitudes.</p>
<dt><code>-Q</code>[<code>d</code>|<code>e</code></p>
<dd> List all projection parameters. To only list datums, use <code>-Qd</code>. To only list ellipsoids, use <code>-Qe</code>.</p>
<dt><code>-S</code></p>
<dd> Suppress points that fall outside the region.</p>
<dt><code>-T</code>[<code>h</code>]<i>from</i>[/<i>to</i>]</p>
<dd> Coordinate conversions between datums <i>from</i> and <i>to</i> using the standard Molodensky transformation. Use <code>-Th</code> if 3rd input column has height above ellipsoid [Default assumes height = 0, i.e., on the ellipsoid]. Specify datums using the datum ID (see <code>-Qd</code>) or give <i>ellipsoid</i>:<i>dx</i>,<i>dy</i>,<i>dz</i> where <i>ellipsoid</i> may be an ellipsoid ID (see <code>-Qe</code>) or given as <i>a</i>[,*inv_f*], where <i>a</i> is the semi-major axis and <i>inv_f</i> is the inverse flattening (0 if omitted). If <i>datum</i> is &#8211; or not given we assume WGS-84. <code>-T</code> may be used in conjunction with <code>-R</code> <code>-J</code> to change the datum before coordinate projection (add <code>-I</code> to apply the datum conversion after the inverse projection). Make sure that the <i>PROJ_ELLIPSOID</i> setting is correct for your case.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>w</code>|<code>h</code>]</p>
<dd> Prints map width and height on standard output. No input files are read. To only output the width or the height, append <code>w</code> or <code>h</code>, respectively. The units of the dimensions may be changed via <code>-D</code>.</p>
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
<dt><code>-p</code>[<code>x</code>|<code>y</code>|<code>z</code>]<i>azim</i>/<i>elev</i>[/<i>zlevel</i>][<code>+w</code><i>lon0</i>/<i>lat0</i>[/<i>z0</i>]][<code>+v</code><i>x0</i>/<i>y0</i>] <i>(more &#8230;)</i></p>
<dd> Select perspective view.</p>
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
<p> The ASCII output formats of numerical data are controlled by parameters in your <code>gmt.conf</code> file. Longitude and latitude are formatted according to <i>FORMAT_GEO_OUT</i>, whereas other values are formatted according to <i>FORMAT_FLOAT_OUT</i>. Be aware that the format in effect can lead to loss of precision in the output, which can lead to various problems downstream. If you find the output is not written with enough precision, consider switching to binary output (<code>-bo</code> if available) or specify more decimals using the <i>FORMAT_FLOAT_OUT</i> setting.</p>
<h2>EXAMPLES</h2>
<p> To convert UTM coordinates in meters to geographic locations, given a file utm.txt and knowing the UTM zone (and zone or hemisphere), try </p>
<pre>
gmt mapproject utm.txt -Ju+11/1:1 -C -I -F
</pre>
<p> To transform a file with (longitude,latitude) into (x,y) positions in cm on a Mercator grid for a given scale of 0.5 cm per degree, run </p>
<pre>
gmt mapproject lonlatfile -R20/50/12/25 -Jm0.5c &gt; xyfile
</pre>
<p> To transform several 2-column, binary, double precision files with (latitude,longitude) into (x,y) positions in inch on a Transverse Mercator grid (central longitude 75W) for scale = 1:500000 and suppress those points that would fall outside the map area, run </p>
<pre>
gmt mapproject tracks.* -R-80/-70/20/40 -Jt-75/1:500000 -: -S -Di -bo -bi2 &gt; tmfile.b
</pre>
<p> To convert the geodetic coordinates (lon, lat, height) in the file old.dat from the NAD27 CONUS datum (Datum ID 131 which uses the Clarke-1866 ellipsoid) to WGS 84, run </p>
<pre>
gmt mapproject old.dat -Th131 &gt; new.dat
</pre>
<p> To compute the closest distance (in km) between each point in the input file quakes.dat and the line segments given in the multisegment ASCII file coastline.xy, run </p>
<pre>
gmt mapproject quakes.dat -Lcoastline.xy/k &gt; quake_dist.dat
</pre>
<h2>RESTRICTIONS</h2>
<p> The rectangular input region set with <code>-R</code> will in general be mapped into a non-rectangular grid. Unless <code>-C</code> is set, the leftmost point on this grid has xvalue = 0.0, and the lowermost point will have yvalue = 0.0. Thus, before you digitize a map, run the extreme map coordinates through <code>mapproject</code> using the appropriate scale and see what (x,y) values they are mapped onto. Use these values when setting up for digitizing in order to have the inverse transformation work correctly, or alternatively, use <code>awk</code> to scale and shift the (x,y) values before transforming. </p>
<p> For some projection, a spherical solution may be used despite the user having selected an ellipsoid. This occurs when the users <code>-R</code> setting implies a region that exceeds the domain in which the ellipsoidal series expansions are valid. These are the conditions: (1) Lambert Conformal Conic (<code>-JL</code>)and Albers Equal-Area (<code>-JB</code>) will use the spherical solution when the map scale exceeds 1.0E7. (2) Transverse Mercator (<code>-JT</code>) and UTM (<code>-JU</code>) will will use the spherical solution when either the west or east boundary given in <code>-R</code> is more than 10 degrees from the central meridian, and (3) same for Cassini (<code>-JC</code>) but with a limit of only 4 degrees.</p>
<h2>ELLIPSOIDS AND SPHEROIDS</h2>
<p> GMT will use ellipsoidal formulae if they are implemented and the user have selected an ellipsoid as the reference shape (see <i>PROJ_ELLIPSOID</i>). The user needs to be aware of a few potential pitfalls: (1) For some projections, such as Transverse Mercator, Albers, and Lambert&#8217;s conformal conic we use the ellipsoidal expressions when the areas mapped are small, and switch to the spherical expressions (and substituting the appropriate auxiliary latitudes) for larger maps. The ellipsoidal formulae are used as follows: (a) Transverse Mercator: When all points are within 10 degrees of central meridian, (b) Conic projections when longitudinal range is less than 90 degrees, (c) Cassini projection when all points are within 4 degrees of central meridian. (2) When you are trying to match some historical data (e.g., coordinates obtained with a certain projection and a certain reference ellipsoid) you may find that GMT gives results that are slightly different. One likely source of this mismatch is that older calculations often used less significant digits. For instance, Snyder&#8217;s examples often use the Clarke 1866 ellipsoid (defined by him as having a flattening f = 1/294.98). From f we get the eccentricity squared to be 0.00676862818 (this is what GMT uses), while Snyder rounds off and uses 0.00676866. This difference can give discrepancies of several tens of cm. If you need to reproduce coordinates projected with this slightly different eccentricity, you should specify your own ellipsoid with the same parameters as Clarke 1866, but with f = 1/294.97861076. Also, be aware that older data may be referenced to different datums, and unless you know which datum was used and convert all data to a common datum you may experience mismatches of tens to hundreds of meters. (3) Finally, be aware that <i>PROJ_SCALE_FACTOR</i> have certain default values for some projections so you may have to override the setting in order to match results produced with other settings.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtvector</code>, <code>project</code></p>
<h2>REFERENCES</h2>
<p> Bomford, G., 1952, Geodesy, Oxford U. Press. </p>
<p> Snyder, J. P., 1987, Map Projections &#8211; A Working Manual, U.S. Geological Survey Prof. Paper 1395. </p>
<p> Vanicek, P. and Krakiwsky, E, 1982, Geodesy &#8211; The Concepts, North-Holland Publ., ISBN: 0 444 86149 1.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
