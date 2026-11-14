---
title: "grdpmodeler(1)"
name: "grdpmodeler"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdpmodeler/"
description: "grdpmodeler – Evaluate a plate model on a geographic grid"
---

<h2>NAME</h2>
<p> grdpmodeler &#8211; Evaluate a plate model on a geographic grid</p>
<h2>SYNOPSIS</h2>
<p> <code>grdpmodeler</code> <i>agegrdfile</i> <i>rot_file</i> <code>-S</code><i>flags</i> [ <i>polygonfile</i> ] [ <i>outgrdfile</i> ] [ <i>age</i> ] [ [<i>level</i>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdpmodeler</code> reads a geographical age grid and a plate motion model and evaluates one of several model predictions. Optionally, the user may supply a clipping polygon in multiple-segment format; then, only the part of the grid inside the polygon is used to determine the model prediction; the remainder of the grid is set to NaN.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>ingrdfile</i></p>
<dd> Name of a grid file in geographical (lon, lat) coordinates with ages in Myr.</p>
<dt><code>-E</code><i>rotfile</i></p>
<dd> Give file with rotation parameters. This file must contain one record for each rotation; each record must be of the following format: </p>
<p> <i>lon lat tstart [tstop] angle</i> [ <i>khat a b c d e f g df</i> ] </p>
<p> where <i>tstart</i> and <i>tstop</i> are in Myr and <i>lon lat angle</i> are in degrees. <i>tstart</i> and <i>tstop</i> are the ages of the old and young ends of a stage. If <i>tstop</i> is not present in the record then a total reconstruction rotation is expected and <i>tstop</i> is implicitly set to 0 and should not be specified for any of the records in the file. If a covariance matrix <code>C</code> for the rotation is available it must be specified in a format using the nine optional terms listed in brackets. Here, <code>C</code> = (<i>g</i>/<i>khat</i>)*[ <i>a b d; b c e; d e f</i> ] which shows <code>C</code> made up of three row vectors. If the degrees of freedom (<i>df</i>) in fitting the rotation is 0 or not given it is set to 10000. Blank lines and records whose first column contains # will be ignored. You may prepend a leading + to the filename to indicate you wish to invert the rotations. Alternatively, give the filename composed of two plate IDs separated by a hyphen (e.g., PAC-MBL) and we will instead extract that rotation from the GPlates rotation database. We return an error if the rotation cannot be found.</p>
<dt><code>-S</code><i>flags</i></p>
<dd> Type of model prediction(s). Append one or more items: choose from <code>a</code> for plate motion azimuth, <code>d</code> for great-circle distance between current location and its origin at the ridge (in km), <code>s</code> for plate motion model stage ID (1 is youngest), <code>v</code> for plate motion rate (in mm/yr), <code>w</code> for plate rotation rate (degree/Myr), <code>x</code> for change in longitude relative to location of crust formation, <code>y</code> for change in latitude relative to location of crust formation, <code>X</code> for longitude of crust formation, and <code>Y</code> for latitude of crust formation. If no arguments are given we default to all [<code>adsvwxyXY</code>].</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-F</code><i>polygonfile</i></p>
<dd> Specify a multisegment closed polygon file that describes the inside area of the grid where the model should be evaluated; the outside will be set to NaN [Default evaluates model on the entire grid].</p>
<dt><code>-G</code><i>outgrdfile</i></p>
<dd> Name of output grid. This is the grid with the model predictions given the specified rotations. Note: If you specified more than one model prediction in <code>-S</code> then the filename <i>must</i> be a template that contains the format %s; this will be replaced with the corresponding tags az, dist, stage, vel, omega, dlon, dlat, lon, lat. If the <code>-G</code> option is not used then we create no grids and instead write <i>lon, lat, age, predictions</i> records to standard output.</p>
<dt><code>-T</code><i>age</i></p>
<dd> Use a fixed age for model evaluation (i.e., override the ages in the age grid). This lets you evaluate the model at a snapshot in time.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 2 input columns].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
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
<h2>GEODETIC VERSUS GEOCENTRIC COORDIINATES</h2>
<p> All spherical rotations are applied to geocentric coordinates. This means that incoming data points and grids are considered to represent geodetic coordinates and must first be converted to geocentric coordinates. Rotations are then applied, and the final reconstructed points are converted back to geodetic coordinates. This default behavior can be bypassed if the ellipsoid setting <i>PROJ_ELLIPSOID</i> is changed to Sphere.</p>
<h2>EXAMPLES</h2>
<p> We will use a grid with Pacific crust ages (pac_age.nc), a plate motion model (Pac_APM.d), and a polygon that contains the outline of the present Pacific plate (pac_clip_path.d). To evaluate the plate motion azimuths at the present time for the Pacific, try </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d \
                -Gpac_dir_0.nc -Sa -T0
</pre>
<p> To determine the changes in latitude since crust formation for the entire Pacific, try </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d \
                -Gpac_dlat.nc -Sy
</pre>
<p> To determine the plate motion velocities in effect when the Pacific crust was formed, try </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d \
                -Gpac_vel.nc -Sv
</pre>
<p> To determine how far the crust has moved since formation, try </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d \
                -Gpac_dist.nc -Sd
</pre>
<p> To save the coordinates of the crust&#8217;s formation to separate grids, try </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d \
                -Gpac_origin_%s.nc -SXY
</pre>
<p> To repeat the same exercise but save output <i>lon,lat,age,xorigin,yorigin</i> to a table, use </p>
<pre>
gmt grdpmodeler pac_age.nc -EPac_APM.d -V -Fpac_clip_path.d -SXY &gt; origin.txt
</pre>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>backtracker</code>, <code>grdrotater</code>, <code>grdspotter</code>, <code>hotspotter</code>, <code>originator</code>, <code>rotconverter</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
