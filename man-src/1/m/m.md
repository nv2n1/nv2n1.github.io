---
title: "m(1)"
name: "m"
section: "1"
letter: "m"
url: "/docs/linux/man/1-m/"
description: "m.proj – Convert coordinates from one projection to another (cs2cs frontend)."
---

<h2>NAME</h2>
<p> <i></i><code>m.proj</code> &#8211; Convert coordinates from one projection to another (cs2cs frontend).</p>
<h2>KEYWORDS</h2>
<p> miscellaneous, projection</p>
<h2>SYNOPSIS</h2>
<p> <code>m.proj</code><br />
 <code>m.proj help</code><br />
 <code>m.proj</code> [-<code>iodv</code>] [<code>input</code>=<i>filename</i>] [<code>output</code>=<i>filename</i>] [<code>fs</code>=<i>character</i>] [<code>proj_in</code>=<i>string</i>] [<code>proj_out</code>=<i>string</i>] [&#8211;<code>verbose</code>] [&#8211;<code>quiet</code>]</p>
<h3>Flags:</h3>
<dl>
<dt><code>-i</code></p>
<dd>
 Use LL WGS84 as input and current location as output projection</p>
<dt><code>-o</code></p>
<dd>
 Use current location as input and LL WGS84 as output projection</p>
<dt><code>-d</code></p>
<dd>
 Output long/lat in decimal degrees or other projections with many decimal places</p>
<dt><code>-v</code></p>
<dd>
 Verbose mode (print projection parameters and filenames to stderr)</p>
<dt><code>&#8211;verbose</code></p>
<dd>
 Verbose module output</p>
<dt><code>&#8211;quiet</code></p>
<dd>
 Quiet module output</dl>
<h3>Parameters:</h3>
<dl>
<dt><code>input</code>=<i>filename</i></p>
<dd>
 Input coordinate file (omit to read from stdin)</p>
<dt><code>output</code>=<i>filename</i></p>
<dd>
 Output coordinate file (omit to send to stdout)</p>
<dt><code>fs</code>=<i>character</i></p>
<dd>
 Field separator<br />
 Default: <i>|</i></p>
<dt><code>proj_in</code>=<i>string</i></p>
<dd>
 Input projection parameters (PROJ.4 style)</p>
<dt><code>proj_out</code>=<i>string</i></p>
<dd>
 Output projection parameters (PROJ.4 style)</dl>
<h2>DESCRIPTION</h2>
<p> This program allows a user to convert coordinates from one projection to another. Coordinates can be read from one file, converted, and results written to another file. Alternatively, if the <code>input</code> and/or <code>output</code> options are omitted, eastings and northings may be passed to the program directly from stdin and results sent directly to stdout. In this way <i>m.proj</i> can be used as a simple frontend to the PROJ.4 <i>cs2cs</i> utility. The <code>-i</code> or <code>-o</code> flags make the task especially easy for the common problem of converting to or from lat/long WGS84. </p>
<p> <i>Note</i>: This program does not transform GRASS maps, it is designed to determine the equivalent coordinate values of an individual position or list of positions. Use <i>v.proj</i> or <i>r.proj</i> to reproject GRASS maps.</p>
<h2>NOTES</h2>
<p> <i>cs2cs</i> expects input data to formatted as &quot;x y&quot;, so if working with latitude-longitude data be sure to send the x value first, i.e., &quot;longitude latitude&quot;. Output data will be exported using the same convention. </p>
<p> <i>cs2cs</i> will treat a third data column as a z value (elevation) and will modify the value accordingly. This usually translates into small but real differences in that data column. </p>
<p> <i>cs2cs</i> does not expect the input stream to contain column headings, only numbers. If your data file has lines you wish to have passed through without being processed, they must start with the &#8216;#&#8217; character. </p>
<p> If sending <i>m.proj</i> data from stdin, be aware that the data is first stored to a temporary file before being processed with <i>cs2cs</i>. It is therefore not advisable to send <i>m.proj</i> data from an open data stream. The module will stop listening for incoming data after 2 seconds of inactivity. You may use the projection parameters gleaned from <i>m.proj</i>&#8216;s verbose mode (<code>-v</code>) with <i>cs2cs</i> directly in this case. </p>
<p> Custom projection parameters can be used via the <code>proj_in</code> and <code>proj_out</code> options. Full documentation of the projection parameter format may be found on the PROJ.4 website. Using these options will fully override the default parameters the module would normally use. </p>
<p> By using the <code>-v</code> verbose flag, the user can see exactly what projection parameters will be used in the conversion as well as some other informative messages. </p>
<p> If output is to lat/long, it will be formatted using PROJ.4&#8217;s Degree:Minute:Second (DMS) convention of DDDdMM&#8217;SSS.SS&quot;H. This can be handy if you wish to quickly convert lat/long decimal degree data into its DMS equivalent.<br />
 Alternatively, to have <i>m.proj</i> output data in decimal degrees, use the <code>-d</code> flag. This flag can also be used with non-lat/long data to force a higher number of decimal places (the <i>cs2cs</i> default is 2). </p>
<p> Lat/long output can be converted to GRASS&#8217;s DMS convention (DDD:MM:SSS.SSSH) by piping the results of <i>m.proj</i> through the <i>sed</i> stream editor as follows.<br />
 m.proj -o | sed -e &#8216;s/d/:/g&#8217; -e &quot;s/&#8217;/:/g&quot; -e &#8216;s/&quot;//g&#8217; </p>
<p> The <i>m.proj</i> module is designed to work seamlessly with point data exported from the GIS with <i>v.out.ascii</i>, as the following example shows.<br />
 v.out.ascii bugsites | m.proj -o </p>
<h2>EXAMPLES</h2>
<p> To convert a WGS84 long/lat coordinate to the current map projection using the <code>-i</code> flag to set projection parameters automaticlly:<br />
 GRASS&gt; echo &quot;170.510125 -45.868537&quot; | m.proj -i<br />
 2316541.70 5479193.51 1.23 </p>
<p> The same, but load points from a file named &quot;waypoints.txt&quot; and continue on to import the results into a GRASS vector points map in the current map projection:<br />
 m.proj -i in=waypoints.txt | cut -f1 -d&#8217; &#8216; | v.in.ascii out=test_pt fs=tab<br />
 Here the standard UNIX <i>cut</i> tool is used to discard the z residual. </p>
<p> To convert all coordinates from a vector points map in the current projection to WGS84 long/lat, with output in decimal form:<br />
 v.out.ascii bugsites | m.proj -od </p>
<p> To transform points from a UTM projection into the Gauss-Kr�ger Grid System, importing and exporting to files:<br />
 m.proj <code>proj_in</code>=&quot;+proj=utm +name=utm +a=6378137.0 +es=0.006694380 rs </p>
<p>&nbsp;<wbr>+zone=32&nbsp;<wbr>+unfact=1.0&quot;&nbsp;<wbr><code>proj_out</code>=&quot;+proj=tmerc&nbsp;<wbr>+name=tmerc rs </p>
<p>&nbsp;<wbr>+a=6377397.155&nbsp;<wbr>+es=0.0066743720&nbsp;<wbr>+lat_0=0.0&nbsp;<wbr>+lon_0=9.0&nbsp;<wbr>+k=1.0 rs </p>
<p>&nbsp;<wbr>+x_0=3500000.0&quot;&nbsp;<wbr><code>input</code>=utm.coord.txt&nbsp;<wbr><code>output</code>=new.gk.coord.txt </p>
<p> Projection parameters provided in the above case: &quot;+proj&quot; (projection type), &quot;+name&quot; (projection name), &quot;+a&quot; (ellipsoid: equatorial radius), &quot;+es&quot; (ellipsoid: eccentricity squared), &quot;+zone&quot; (zone for the area), &quot;+unfact&quot; (conversion factor from meters to other units, e.g. feet), &quot;+lat_0&quot; (standard parallel), &quot;+lon_0&quot; (central meridian), &quot;+k&quot; (scale factor) and &quot;+x_0&quot; (false easting). Sometimes false northing is needed which is coded as &quot;+y_0&quot;. Internally, the underlying PROJ.4 projection library performs an inverse projection to latitude-longitude and then projects the coordinate list to the target projection. </p>
<p> Datum conversions are automatically handled by the PROJ.4 library if dq+datum&quot; setings are specified on <code>both</code> the input <code>and</code> output projections on the command line. The &quot;+towgs84&quot; parameter can be used to define either 3 or 7 term datum transform coefficients, satisfying this requirement. </p>
<p> If a datum is specified there is no need for the &#8216;+ellps=&#8217; or underlying parameters, &#8216;+a=&#8217;, &#8216;+es=&#8217;, etc. </p>
<h3>Another custom parameter usage example:</h3>
<p> m.proj <code>proj_in</code>=&quot;+proj=tmerc +datum=ire65 +lat_0=53.5 +lon_0=-8 +x_0=200000 rs </p>
<p>&nbsp;<wbr>+y_0=250000&nbsp;<wbr>+k=1.000035&quot;&nbsp;<wbr><code>proj_out</code>=&quot;+proj=ll&nbsp;<wbr>+datum=wgs84&quot;&nbsp;<wbr><code>input</code>=wpt.txt<br />
 or without datum transformation:<br />
 m.proj <code>proj_in</code>=&quot;+proj=tmerc +ellps=modif_airy +lat_0=53.5 +lon_0=-8 +x_0=200000 rs </p>
<p>&nbsp;<wbr>+y_0=250000&nbsp;<wbr>+k=1.000035&quot;&nbsp;<wbr><code>proj_out</code>=&quot;+proj=ll&nbsp;<wbr>+datum=wgs84&quot;&nbsp;<wbr><code>input</code>=wpt.txt </p>
<p> In this example no datum transformation will take place as a datum was not specified for the input projection. The datum specified for the output projection will thus be silently ignored and may be left out; all that is achieved a simple conversion from projected to geodetic co-ordinates, keeping the same datum (and thus also the same ellipsoid). </p>
<p> For more usage examples, see the documentation for the PROJ.4 <i>cs2cs</i> program.</p>
<h2>REFERENCES</h2>
<p> [1] Evenden, G.I. (1990) Cartographic projection procedures for the UNIX environment &#8211; a user&#8217;s manual. USGS Open-File Report 90-284 (OF90-284.pdf) See also there: Interim Report and 2nd Interim Report on Release 4, Evenden 1994). </p>
<p> [2] PROJ.4 Cartographic Projection Library</p>
<h2>SEE ALSO</h2>
<p> <i> v.proj, r.proj, g.proj, g.setproj, i.rectify, v.in.ascii, v.out.ascii </i></p>
<h2>AUTHOR</h2>
<p> M. Hamish Bowman, Dept. Marine Science, Otago University, New Zealand<br />
 Functionality inspired by the <i>m.proj</i> and <i>m.proj2</i> modules for GRASS GIS 5. </p>
<p> <i>Last changed: $Date: 2006-08-31 10:47:06 +0200 (Thu, 31 Aug 2006) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
