---
title: "mgd77list(1)"
name: "mgd77list"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77list/"
description: "mgd77list – Extract data from MGD77 files"
---

<h2>NAME</h2>
<p> mgd77list &#8211; Extract data from MGD77 files</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77list</code> <i>NGDC-ids</i> <i>columns</i>[,<i>logic</i>][:<i>bittests</i>] [ [<code>+</code>]<code>c</code>|<code>d</code>|<code>f</code>|<code>m</code>|<code>t</code><i>code</i> ] [ <code>f</code>|<code>g</code>|<code>e</code> ] [ <code>A</code>|<code>a</code><i>startdate</i> ] [ <code>B</code>|<code>b</code><i>stopdate</i> ] [ ] [ <code>a</code><i>startrec</i> ] [ <code>b</code><i>stoprec</i> ] [ <i>ignore</i> ] [ [<i>corrtable</i>] ] [ <code>d</code>|<code>s</code><i>unit</i> ] [ <code>a</code>|<code>c</code>|<code>v</code><i>min</i>/<i>max</i> ] [ <i>region</i> ] [ <code>a</code><i>startdist</i>[unit] ] [ <code>b</code><i>stopdist</i>[unit] ] [ [<code>m</code>|<code>e</code>] ] [ [<i>level</i>] ] [ <i>weight</i> ] [ <i>+</i>|<code>&#8211;</code> ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77list</code> reads &lt;NGDC-id&gt;.[mgd77|nc] files and produces an ASCII [or binary] table. The &lt;NGDC-id&gt;.[mgd77|nc] files contain track information such as leg-id, time and position, geophysical observables such as gravity, magnetics, and bathymetry, and control codes and corrections such as Eotvos and diurnal corrections. The MGD77+ extended netCDF files may also contain additional user columns (for a listing of available columns, use <code>mgd77info</code> <code>-C</code>, and to learn how to add your own custom columns, see <code>mgd77manage</code>). The user may extract any combination of these parameters, any of 8 computed quantities (distance, heading, course-change, velocity, Carter correction, Eotvos correction and gravity and magnetic global reference fields), calendar sub-units of time (year, month, day, hour, min, sec), the NGDC id, and finally a preset weight (see <code>-W</code>). A sub-section can be specified by passing time- or distance-intervals along track or by selecting a geographical region. Finally, each output record may be required to pass any number of logical tests involving data values or bit flags. If multiple cruises are requested then they are separated by segment headers.</p>
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
<dt><code>-F</code><i>columns</i>[,<i>logic</i>][:<i>bittests</i>]</p>
<dd> The required <i>columns</i> string must be a comma-separated list of parameter abbreviations given in the desired output order. Any parameters given in UPPER case must not be NaN in a record for output to occur. Unless specified separately, the output format (if ASCII) is controlled by the GMT parameter <i>FORMAT_FLOAT_OUT</i>. The available column abbreviations for information stored in the files (some columns may be NaN) are:</p>
<dt><code>recno</code></p>
<dd> The record number counter.</p>
<dt><code>drt</code></p>
<dd> The digital record type, usually 3 or 5 (for Y2K-compliant cruises).</p>
<dt><code>id</code></p>
<dd> The survey ID string (leg name).</p>
<dt><code>ngdcid</code></p>
<dd> The 8-character NGDC cruise ID string (usually the file prefix).</p>
<dt><code>time</code></p>
<dd> Choose between Absolute calendar time (<code>atime</code>, the default) in the format dictated by the GMT parameters <i>FORMAT_DATE_OUT</i> and <i>FORMAT_CLOCK_OUT</i>, Relative time (<code>rtime</code>) in the format dictated by the GMT parameters <i>FORMAT_FLOAT_OUT</i> and <i>TIME_SYSTEM</i> (or <i>TIME_EPOCH</i> and <i>TIME_UNIT</i>)), or Fractional year (<code>ytime</code>) in the format dictated by <i>FORMAT_FLOAT_OUT</i>.</p>
<dt><code>lon</code></p>
<dd> Longitude in the format dictated by the GMT parameter <i>FORMAT_GEO_OUT</i>.</p>
<dt><code>lat</code></p>
<dd> Longitude in the format dictated by the GMT parameter <i>FORMAT_GEO_OUT</i>.</p>
<dt><code>twt</code></p>
<dd> Two-Way Travel time (in s).</p>
<dt><code>depth</code></p>
<dd> Corrected bathymetry (in m, positive below sea level).</p>
<dt><code>mtf1</code></p>
<dd> Magnetic Total Field intensity from sensor 1 (in nTesla).</p>
<dt><code>mtf2</code></p>
<dd> Magnetic Total Field intensity from sensor 2 (in nTesla).</p>
<dt><code>mag</code></p>
<dd> Residual magnetic anomaly (in nTesla).</p>
<dt><code>gobs</code></p>
<dd> Observed gravity (in mGal).</p>
<dt><code>faa</code></p>
<dd> Free-air gravity anomaly (in mGal).</p>
<dt><code>ptc</code></p>
<dd> Position Type Code (1 = fix, 3 = interpolated, 9 = unspecified).</p>
<dt><code>bcc</code></p>
<dd> Bathymetric Correction Code, indicating the procedure used to convert travel time to depth. (01-55 = Matthews&#8217; zone used to correct the depth, 59 = Matthews&#8217; corrections used but the zones is unspecified in the data record, 60 = S. Kuwahara formula for T-S, 61 = Wilson formula for T-S, 62 = Del Grosso formula for T-S, 63 = Carter&#8217;s tables, 88 = Other, described in header sections, 99 = unspecified).</p>
<dt><code>btc</code></p>
<dd> Bathymetric Type Code, indicating how the bathymetry value was obtained (1 = observed, 3 = interpolated, 9 = unspecified).</p>
<dt><code>msens</code></p>
<dd> Magnetic sensor for used to evaluate the residual field (1 = 1st or leading sensor, 2 = 2nd or trailing sensor, 9 = unspecified).</p>
<dt><code>msd</code></p>
<dd> Depth (or altitude) of the magnetic sensor (in m, positive below sealevel).</p>
<dt><code>diur</code></p>
<dd> Magnetic diurnal correction (in nTesla).</p>
<dt><code>eot</code></p>
<dd> Eotvos correction (in mGal).</p>
<dt><code>sln</code></p>
<dd> Seismic Line Number string.</p>
<dt><code>sspn</code></p>
<dd> Seismic Shot Point Number string.</p>
<dt><code>nqc</code></p>
<dd> Navigation Quality Code (5 = suspected, by source institution, 6 = suspected, by NGDC, 9 = no problems identified). </p>
<p> In addition, the following derived navigational quantities can be requested:</p>
<dt><code>year</code></p>
<dd> The year of each record.</p>
<dt><code>month</code></p>
<dd> The month of each record.</p>
<dt><code>day</code></p>
<dd> The day of the month of each record.</p>
<dt><code>hour</code></p>
<dd> The hour of each record.</p>
<dt><code>min</code></p>
<dd> The minutes of each record.</p>
<dt><code>sec</code></p>
<dd> The decimal seconds of each record.</p>
<dt><code>dist</code></p>
<dd> Along-track distance from start of leg. For method of calculation, see <code>-C</code> [spherical great circle distances], and for distance units, see <code>-N</code> [km].</p>
<dt><code>az</code></p>
<dd> Ship azimuth (heading) measured clockwise from north (in degrees).</p>
<dt><code>cc</code></p>
<dd> Ship course change (change in heading) measured clockwise from north (in degrees).</p>
<dt><code>vel</code></p>
<dd> Ship speed; see <code>-N</code> for units [m/s]. </p>
<p> Finally, the following computed quantities can be requested:</p>
<dt><code>weight</code></p>
<dd> Weight assigned to this data set (see <code>-W</code>).</p>
<dt><code>carter</code></p>
<dd> Carter depth correction, if <code>twt</code> is present in file (in m). Sign: Correction is to be added to uncorrected depths to yield a corrected depth.</p>
<dt><code>igrf</code></p>
<dd> International geomagnetic reference field (total field) (in nTesla).</p>
<dt><code>ngrav</code></p>
<dd> International Gravity reference Field (&quot;normal gravity&quot;) (in mGal). Field is selected based on the parameter Gravity Theoretical Formula Code in the cruise&#8217;s MGD77 header. If this is not set or is invalid we default to the IGF 1980. Alternatively, specify the field directly using <code>-Af</code> (see that option for more details).</p>
<dt><code>ceot</code></p>
<dd> Calculated Eotvos correction from navigation, using E = 7.5038 * V * cos(lat) * sin(az) + 0.004154 * V^2 (in mGal). Sign: Correction is to be added to uncorrected faa to yield a corrected faa. </p>
<p> The following short-hand flags are also recognized:</p>
<dt><code>mgd77</code></p>
<dd> This results in all 27 MGD77 fields being written out in the official MGD77 order.</p>
<dt><code>mgd77t</code></p>
<dd> The full set of all 26 columns in the MGD77T specification.</p>
<dt><code>geo</code></p>
<dd> This limits the output to 10 fields (<code>time</code>, <code>lon</code>, <code>lat</code> plus the seven geophysical observations <code>twt</code>, <code>depth</code>, <code>mtf1</code>, <code>mtf2</code>, <code>mag</code>, <code>gobs</code>, and <code>faa</code>). By appending <code>+</code> to either of these set we will also append <code>dist</code>, <code>azim</code>, <code>cc</code>, <code>vel</code>, and <code>weight</code> as listed above.</p>
<dt><code>all</code></p>
<dd> This returns all data columns in the file.</p>
<dt><code>allt</code></p>
<dd> As mgd77t but with time items written as a date-time string. </p>
<p> As an option, logical tests may be added for any of the observations by appending ,<i>logic</i>, which is itself composed of one or more comma-separated instructions of the form <i>par</i><code>OP</code><i>value</i>, where <i>par</i> is one of the parameters listed above, <code>OP</code> is a logical operator (&lt;, &lt;=, =, !=, &gt;=, &gt;, |), and <i>value</i> is a constant used in the comparison. Floating point parameters are compared numerically; character parameters are compared lexically (after leading and trailing blanks have been removed). The bit comparison (|) means that at least one of the bits in <i>value</i> must be turned on in <i>par</i>. At least one of the tests must be true for the record to be output, except for tests using UPPER case parameters which all must be true for output to occur. Note that specifying a test does not imply that the corresponding column will be included in the output stream; it must be present in <i>columns</i> for that to occur. Note: some of the operators are special UNIX characters and you are advised to place quotes around the entire argument to <code>-F</code>. </p>
<p> Finally, for MGD77+ files you may optionally append :<i>bittests</i> which is : (a colon) followed by one or more comma-separated +-<i>col</i> terms. This compares specific bitflags only for each listed column. Here, + means the chosen bit must be 1 (ON) whereas &#8211; means it must be 0 (OFF). All bit tests given must be passed. By default, MGD77+ files that have the special <code>MGD77_flags</code> column present will use those flags, and observations associated with ON-bits (meaning they are flagged as bad) will be set to NaN; append : with no trailing information to turn this behavior off (i.e., no bit flags will be consulted).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code>[<code>+</code>]<code>c</code>|<code>d</code>|<code>f</code>|<code>m</code>|<code>t</code><i>code</i></p>
<dd> By default, corrected depth (<code>depth</code>), magnetic residual anomaly (<code>mag</code>), free-air gravity anomaly (<code>faa</code>), and the derived quantity Carter depth correction (<code>carter</code>) are all output as is (if selected in <code>-F</code>); this option adjusts that behavior. For each of these columns there are 2-4 ways to adjust the data. Append <code>c</code>(arter), <code>d</code>(epth), <code>f</code>(aa), or <code>m</code>(ag) and select the <i>code</i> for the procedure you want applied. You may select more than one procedure for a data column by summing their numerical <i>code</i>s (1, 2, 4, and 8). E.g., <code>-Ac</code>3 will first try method <code>-Ac</code>1 to estimate a Carter correction but if <code>depth</code> is NaN we will next try <code>-Ac</code>2 which only uses <code>twt</code>. In all cases, if any of the values required by an adjustment procedure is NaN then the result will be NaN. This is also true if the original anomaly is NaN. Specify <code>-A+</code> to recalculate anomalies even if the anomaly in the file is NaN. Additionally, you can use <code>-At</code> to create fake times for cruises that has no time; these are based on distances and cruise duration.</p>
<dt><code>-Ac</code></p>
<dd> Determines how the <code>carter</code> correction term is calculated. Below, C(<code>twt</code>) stands for the Carter-corrected depth (it also depends on <code>lon</code>, <code>lat</code>), U(<code>twt</code>, <i>v</i>) is the uncorrected depth (= <code>twt</code> * <i>v</i> / 2) using as <i>v</i> the &quot;Assumed Sound Velocity&quot; parameter in the MGD77 header (if it is a valid velocity, otherwise we default to 1500 m/s); alternatively, append your preferred velocity <i>v</i> in m/s, TU(<code>depth</code>, <i>v</i>) is the 2-way travel time estimated from the (presumably) uncorrected <code>depth</code>, and TC(<code>depth</code>) is the 2-way travel time obtained by inverting the (presumably) corrected <code>depth</code> using the Carter correction formula. Select from </p>
<p> <code>-Ac1</code>[,<i>v</i>] returns difference between U(<code>twt</code>, <i>v</i>) and <code>depth</code> [Default]. </p>
<p> <code>-Ac2</code>[,<i>v</i>] returns difference between U(<code>twt</code>, <i>v</i>) and Carter (<code>twt</code>). </p>
<p> <code>-Ac4</code>[,<i>v</i>] returns difference between (assumed uncorrected) <code>depth</code> and Carter (TU(<code>depth</code>)). </p>
<p> <code>-Ac8</code>[,<i>v</i>] returns difference between U(TC(<code>depth</code>), <i>v</i>) and <code>depth</code>.</p>
<dt><code>-Ad</code></p>
<dd> Determines how the <code>depth</code> column output is obtained: </p>
<p> <code>-Ad1</code> returns <code>depth</code> as stored in the data set [Default]. </p>
<p> <code>-Ad2</code>[,<i>v</i>] returns calculated uncorrected depth U(<code>twt</code>, <i>v</i>). </p>
<p> <code>-Ad4</code> returns calculated corrected depth C(<code>twt</code>).</p>
<dt><code>-Af</code></p>
<dd> Determines how the <code>faa</code> column output is obtained. If <code>ngrav</code> (i.e., the International Gravity reference Field (IGF), or &quot;normal gravity&quot;) is required it is selected based on the MGD77 header parameter &quot;Theoretical Gravity Formula Code&quot;; if this code is not present or is invalid we default to 4. Alternatively, append the preferred <i>field</i> (1-4) to select 1 (Heiskanen 1924), 2 (IGF 1930), 3 (IGF 1967) or 4 (IGF 1980). Select from </p>
<p> <code>-Af1</code>[,<i>field</i>] returns <code>faa</code> as stored in the data set [Default]. Optionally, sets the IGF <i>field</i> to use if you also have requested <code>ngrav</code> as an output column in <code>-F</code>. </p>
<p> <code>-Af2</code>[,<i>field</i>] returns the difference between <code>gobs</code> and <code>ngrav</code> (with optional <i>field</i> directive). </p>
<p> <code>-Af4</code>[,<i>field</i>] returns the combination of <code>gobs</code> + <code>eot</code> &#8211; <code>ngrav</code> (with optional <i>field</i> directive). </p>
<p> <code>-Af8</code>[,<i>field</i>] returns the combination of <code>gobs</code> + <code>pred_eot</code> &#8211; <code>ngrav</code> (with optional <i>field</i> directive).</p>
<dt><code>-Am</code></p>
<dd> Determines how the <code>mag</code> column output is obtained. There may be one or two total field measurements in the file (<code>mtf1</code> and <code>mtf2</code>), and the column <code>msens</code> may state which one is the leading sensor (1 or 2; it may also be undefined). Select from </p>
<p> <code>-Am1</code> returns <code>mag</code> as stored in the data set [Default]. </p>
<p> <code>-Am2</code> returns the difference between <code>mgfx</code> and <code>igrf</code>, where <code>x</code> is the leading sensor (<code>1</code> or <code>2</code>) indicated by the <code>msens</code> data field (defaults to <code>1</code> if unspecified). </p>
<p> <code>-Am4</code> returns the difference between <code>mgfx</code> and <code>igrf</code>, where <code>x</code> is the sensor (<code>2</code> or <code>1</code>) <i>not</i> indicated by the <code>msens</code> data field (defaults to <code>2</code> if unspecified). </p>
<p> <code>-Amc&lt;offset&gt;[unit]</code> Apply a correction that tries to compensate the fact that the magnetic field was not acquired at the same position as the navigation refer (ship&#8217;s position). This is accomplished by re-interpolating the total magnetic field to what it would have had if it was measured at the ship&#8217;s position (remember, it probably was measured &lt;offset&gt; meters behind). Due to this interpolation step, bad navigation, namely too many repeated points, may cause troubles. Measures are taken to minimize this effect but they aren&#8217;t 100% full prof. The interpolation method is controlled by the GMT default GMT_INTERPOLANT. Append <code>e</code> for meter, <code>f</code> for feet, <code>k</code> for km, <code>m</code> for miles, <code>n</code> for nautical miles, or <code>u</code> for survey feet [Default is e (meters)].</p>
<dt><code>-C</code><code>f</code>|<code>g</code>|<code>e</code></p>
<dd> Append a one-letter code to select the procedure for along-track distance calculation (see <code>-N</code> for selecting units): </p>
<p> <code>f</code> Flat Earth distances. </p>
<p> <code>g</code> Great circle distances [Default]. </p>
<p> <code>e</code> Geodesic distances on current GMT ellipsoid.</p>
<dt><code>-Da</code><i>startdate</i></p>
<dd> Do not list data collected before <i>startdate</i> (yyyy-mm-ddBD(T)[hh:mm:ss]) [Default is start of cruise]. Use <code>-DA</code> to exclude records whose time is undefined (i.e., NaN). [Default reports those records].</p>
<dt><code>-Db</code><i>stopdate</i></p>
<dd> Do not list data collected on or after <i>stopdate</i> (yyyy-mm-ddBD(T)[hh:mm:ss]). [Default is end of cruise]. Use <code>-DB</code> to exclude records whose time is undefined (i.e., NaN). [Default reports those records].</p>
<dt><code>-E</code></p>
<dd> Exact match: Only output records that match all the requested geophysical columns [Default outputs records that matches at least one of the observed columns].</p>
<dt><code>-Ga</code><i>startrec</i></p>
<dd> Do not list records before <i>startrec</i> [Default is 0, the first record].</p>
<dt><code>-Gb</code><i>stoprec</i></p>
<dd> Do not list data after <i>stoprec</i>. [Default is the last record].</p>
<dt><code>-I</code><i>ignore</i></p>
<dd> Ignore certain data file formats from consideration. Append <code>a|c|t</code> to ignore MGD77 ASCII, MGD77+ netCDF, or plain tab-separated ASCII table files, respectively. The option may be repeated to ignore more than one format. [Default ignores none].</p>
<dt><code>-L</code>[<i>corrtable</i>]</p>
<dd> Apply optimal corrections to columns where such corrections are available. Append the correction table to use [Default uses the correction table mgd77_corrections.txt in the <code>$MGD77_HOME</code> directory]. For the format of this file, see CORRECTIONS below.</p>
<dt><code>-n</code></p>
<dd> Issue a segment header record with cruise ID for each cruise.</p>
<dt><code>-Nd</code>|<code>s</code><i>unit</i></p>
<dd> Append <code>d</code> for distance or <code>s</code> for speed, then give the desired <i>unit</i> as <code>e</code> (meter or m/s), <code>f</code> (feet or feet/s), <code>k</code> (km or km/hr), <code>m</code> (miles or miles/hr), <code>n</code> (nautical miles or knots), or <code>u</code> (survey feet or sfeet/s). [Default is <code>-Ndk</code> <code>-Nse</code> (km and m/s)].</p>
<dt><code>-Qa</code><i>min</i>/<i>max</i></p>
<dd> Specify an accepted range (<i>min</i>/<i>max</i>) of azimuths. Records whose track azimuth falls outside this range are ignored [0/360].</p>
<dt><code>-Qc</code><i>min</i>/<i>max</i></p>
<dd> Specify an accepted range (<i>min</i>/<i>max</i>) of course changes. Records whose track course change falls outside this range are ignored [-360/+360]. Use <code>-QC</code> to take the absolute value of the course change before the test [Default uses signed course changes].</p>
<dt><code>-Qv</code><i>min</i>/<i>max</i></p>
<dd> Specify an accepted range (<i>min</i>/<i>max</i>; or just <i>min</i> if there is no upper limit) of velocities. Records whose track speed falls outside this range are ignored [0/infinity].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-Sa</code><i>startdist</i>[unit]</p>
<dd> Do not list data that are less than <i>startdist</i> meter along track from port of departure. Append <code>e</code> for meter, <code>f</code> for feet, <code>k</code> for km, <code>m</code> for miles, <code>n</code> for nautical miles, or <code>u</code> for survey feet [Default is 0e (meters)].</p>
<dt><code>-Sb</code><i>stopdist</i>[unit]</p>
<dd> Do not list data that are <i>stopdist</i> or more meters along track from port of departure. Append <code>e</code> for meter, <code>f</code> for feet, <code>k</code> for km, <code>m</code> for miles, <code>n</code> for nautical miles, or <code>u</code> for survey feet [Default is end of track].</p>
<dt><code>-T</code>[<code>m</code>|<code>e</code>]</p>
<dd> Turns OFF the otherwise automatic adjustment of values based on correction terms that are stored in the MGD77+ file and used to counteract such things as wrong units used by the source institution when creating the original MGD77 file from which the MGD77+ file derives (the option has no effect on plain MGD77 ASCII files). Append <code>m</code> or <code>e</code> to limit the option to the MGD77 or extended columns set only [Default applies to both].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>weight</i></p>
<dd> Set the weight for these data. Weight output option must be set in <code>-F</code>. This is useful if the data are to be processed with the weighted averaging techniques offered by <code>blockmean</code>, <code>blockmedian</code>, and <code>blockmode</code> [1].</p>
<dt><code>-Z</code><i>+</i>|<code>&#8211;</code></p>
<dd> Append the sign you want for <code>depth</code>, <code>carter</code>, and <code>msd</code> values below sea level (<code>-Z-</code> gives negative bathymetry) [Default is positive down].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. ignored if <code>-bo</code> is selected. Likewise, string-fields cannot be selected. Note that if time is one of the binary output columns it will be stored as Unix-time (seconds since 1970). To read this information in GMT to obtain absolute calendar time will require you to use <code>&#8211;</code><code>-TIME_SYSTEM=1</code>.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
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
<p> To get a (distance, heading, gravity, bathymetry) listing from 01010047.mgd77, starting at June 3 1971 20:45 and ending at distance = 5000 km, use the following command: </p>
<pre>
gmt mgd77list 01010047 -Da1971-06-03T20:45 -Sb5000 -Fdist,azim,faa,depth &gt; myfile.d
</pre>
<p> To make input for <code>blockmean</code> and <code>surface</code> using free-air anomalies from all the cruises listed in the file cruises.lis, but only the data that are inside the specified area, and make the output binary: </p>
<pre>
gmt mgd77list `cat cruises.lis` -Flon,lat,faa -R-40/-30/25/35 -bo &gt; allgrav.b
</pre>
<p> To extract the locations of depths exceeding 9000 meter that were not interpolated (<code>btc</code> != 1) from all the cruises listed in the file cruises.lis: </p>
<pre>
gmt mgd77list `cat cruises.lis` -F&quot;depth,DEPTH&gt;9000,BTC!=1&quot; &gt; really_deep.d
</pre>
<p> To extract dist, faa, and grav12_2 from records whose depths are shallower than 3 km and where none of the requested fields are NaN, from all the MGD77+ netCDF files whose cruise ids are listed in the file cruises.lis, we try </p>
<pre>
gmt mgd77list `cat cruises.lis` -E -Ia -F&quot;dist,faa,grav12_2,depth&lt;3000&quot; &gt; \
    shallow_grav.d
</pre>
<p> To extract dist, faa, and grav12_2 from all the MGD77+ netCDF files whose cruise ids are listed in the file cruises.lis, but only retrieve records whose bitflag for faa indicates BAD values, we try </p>
<pre>
gmt mgd77list `cat cruises.lis` -E -Ia -F&quot;dist,faa,grav12_2:+faa&quot; &gt; bad_grav.d
</pre>
<p> To output lon, lat, mag, and faa from all the cruises listed in the file cruises.lis, but recalculate the two residuals based on the latest reference fields, try: </p>
<pre>
gmt mgd77list `cat cruises.lis` -Flon,lat,mag,faa -Af2,4 -Am2 &gt; data.d
</pre>
<h2>RECALCULATED ANOMALIES</h2>
<p> When recalculated anomalies are requested (either explicitly via the <code>-A</code> option or implicitly via E77 metadata in the MGD77+ file) we only do so for the records whose original anomaly was not a NaN. This restriction is implemented since many anomaly columns contains corrections, usually in the form of hand-edited changes, that cannot be duplicated from the corresponding observation.</p>
<h2>IGRF</h2>
<p> The IGRF calculations are based on a Fortran program written by Susan Macmillan, British Geological Survey, translated to C via f2c by Joaquim Luis, U Algarve, and adapted to GMT-style by Paul Wessel.</p>
<h2>IGF</h2>
<p> The equations used are reproduced here using coefficients extracted directly from the source code (let us know if you find errors): </p>
<p> (1) g = 978052.0 * [1 + 0.005285 * sin^2(lat) &#8211; 7e-6 * sin^2(2*lat) + 27e-6 * cos^2(lat) * cos^2(lon-18)] </p>
<p> (2) g = 978049.0 * [1 + 0.0052884 * sin^2(lat) &#8211; 0.0000059 * sin^2(2*lat)] </p>
<p> (3) g = 978031.846 * [1 + 0.0053024 * sin^2(lat) &#8211; 0.0000058 * sin^2(2*lat)] </p>
<p> (4) g = 978032.67714 * [(1 + 0.00193185138639 * sin^2(lat)) / sqrt (1 &#8211; 0.00669437999013 * sin^2(lat))]</p>
<h2>CORRECTIONS</h2>
<p> The correction table is an ASCII file with coefficients and parameters needed to carry out corrections. Comment records beginning with # are allowed. All correction records are of the form </p>
<p> <i>cruiseID observation correction</i> </p>
<p> where <i>cruiseID</i> is a NGDC prefix, <i>observation</i> is one of the abbreviations for geophysical observations listed under <code>-F</code> above, and <i>correction</i> consists of one or more <i>term</i>s that will be summed up and then <code>subtracted</code> from the observation before output. Each <i>term</i> must have this exact syntax: </p>
<p> <i>factor</i>[*[<i>function</i>]([<i>scale</i>](<i>abbrev</i>[-<i>origin</i>]))[^<i>power</i>]] </p>
<p> where terms in brackets are optional (the brackets themselves are not used but regular parentheses must be used as indicated). No spaces are allowed except between <i>term</i>s. The <i>factor</i> is the amplitude of the basis function, while the optional <i>function</i> can be one of sin, cos, or exp. The optional <i>scale</i> and <i>origin</i> can be used to translate the argument (before giving it to the optional function). The argument <i>abbrev</i> is one of the abbreviations for observations listed above. If <i>origin</i> is given as <code>T</code> it means that we should replace it with the value of <i>abbrev</i> for the very first record in the file (this is usually only done for <i>time</i>). If the first record entry is NaN we revert <i>origin</i> to zero. Optionally, raise the entire expression to the given <i>power</i>, before multiplying by the amplitude. The following is an example of fictitious corrections to the cruise 99999999, implying the <code>depth</code> should have the Carter correction removed, <code>faa</code> should have a linear trend removed, the magnetic anomaly (<code>mag</code>) should be corrected by a strange dependency on ship heading and latitude, and <code>gob</code>s needs to have 10 mGal added (hence given as -10): </p>
<p> 99999999 depth 1.0*((carter)) </p>
<p> 99999999 faa 14.1 1e-5*((time-T)) </p>
<p> 99999999 mag 0.5*cos(0.5*(azim-19))^2 1.0*exp(-1e-3(lat))^1.5 </p>
<p> 99999999 gobs -10</p>
<h2>SEE ALSO</h2>
<p> <code>mgd77convert</code>, <code>mgd77info</code>, <code>mgd77manage</code>, <code>mgd77track</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt</a></i> </p>
<p> IGRF, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/IAGA/vmod/igrf/">http://www.ngdc.noaa.gov/IAGA/vmod/igrf/</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
