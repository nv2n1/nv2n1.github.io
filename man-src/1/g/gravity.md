---
title: "gravity(1)"
name: "gravity"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gravity/"
description: "Gravity — compute the earth’s gravity field"
---

<p>Gravity &#8212; compute the earth&#8217;s gravity field </p>
<h2>Synopsis</h2>
<p><code>Gravity</code> [ <code>-n</code> <i>name</i> ] [ <code>-d</code> <i>dir</i> ] [ <code>-G</code> | <code>-D</code> | <code>-A</code> | <code>-H</code> ] [ <code>-c</code> <i>lat</i> <i>h</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>-v</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p><code>Gravity</code> reads in positions on standard input and prints out the gravitational field on standard output. </p>
<p> The input line is of the form <i>lat</i> <i>lon</i> <i>h</i>. <i>lat</i> and <i>lon</i> are the latitude and longitude expressed as decimal degrees or degrees, minutes, and seconds; see <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1) for details. <i>h</i> is the height above the ellipsoid in meters; this quantity is optional and defaults to 0. Alternatively, the gravity field can be computed at various points on a circle of latitude (constant <i>lat</i> and <i>h</i>) via the <code>-c</code> option; in this case only the longitude should be given on the input lines. The quantities printed out are governed by the <code>-G</code> (default), <code>-D</code>, <code>-A</code>, or <code>-H</code> options. </p>
<p> All the supported gravity models, except for grs80, use <font SIZE="-1">WGS84</font> as the reference ellipsoid <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563, <i>omega</i> = 7292115e-11 rad/s, and <i></i><font SIZE="-1"><i>GM</i></font><i></i> = 3986004.418e8 m^3/s^2.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>use gravity field model <i>name</i> instead of the default <tt>&quot;egm96&quot;</tt>. See &#8220;<font SIZE="-1">MODELS&#8221;</font>.</p>
<dt><code>-d</code></p>
<dd>read gravity models from <i>dir</i> instead of the default. See &#8220;<font SIZE="-1">MODELS&#8221;</font>.</p>
<dt><code>-G</code></p>
<dd>compute the acceleration due to gravity (including the centrifugal acceleration due the the earth&#8217;s rotation) <code>g</code>. The output consists of <i>gx</i> <i>gy</i> <i>gz</i> (all in m/s^2), where the <i>x</i>, <i>y</i>, and <i>z</i> components are in easterly, northerly, and up directions, respectively. Usually <i>gz</i> is negative.</p>
<dt><code>-D</code></p>
<dd>compute the gravity disturbance <code>delta</code> = <code>g</code> &#8211; <code>gamma</code>, where <code>gamma</code> is the &#8220;normal&#8221; gravity due to the reference ellipsoid . The output consists of <i>deltax</i> <i>deltay</i> <i>deltaz</i> (all in mGal, 1 mGal = 10^-5 m/s^2), where the <i>x</i>, <i>y</i>, and <i>z</i> components are in easterly, northerly, and up directions, respectively. Note that <i>deltax</i> = <i>gx</i>, because <i>gammax</i> = 0.</p>
<dt><code>-A</code></p>
<dd>computes the gravitational anomaly. The output consists of 3 items <i>Dg01</i> <i>xi</i> <i>eta</i>, where <i>Dg01</i> is in mGal (1 mGal = 10^-5 m/s^2) and <i>xi</i> and <i>eta</i> are in arcseconds. The gravitational anomaly compares the gravitational field <code>g</code> at <i>P</i> with the normal gravity <code>gamma</code> at <i>Q</i> where the <i>P</i> is vertically above <i>Q</i> and the gravitational potential at <i>P</i> equals the normal potential at <i>Q</i>. <i>Dg01</i> gives the difference in the magnitudes of these two vectors and <i>xi</i> and <i>eta</i> give the difference in their directions (as northerly and easterly components). The calculation uses a spherical approximation to match the results of the <font SIZE="-1">NGA</font>&#8216;s synthesis programs.</p>
<dt><code>-H</code></p>
<dd>compute the height of the geoid above the reference ellipsoid (in meters). In this case, <i>h</i> should be zero. The results accurately match the results of the <font SIZE="-1">NGA</font>&#8216;s synthesis programs. <i><a href="/docs/linux/man/1-geoideval/">GeoidEval</a></i>(1) can compute geoid heights much more quickly by interpolating on a grid of precomputed results; however the results from <i><a href="/docs/linux/man/1-geoideval/">GeoidEval</a></i>(1) are only accurate to a few millimeters.</p>
<dt><code>-c</code></p>
<dd>evaluate the field on a circle of latitude given by <i>lat</i> and <i>h</i> instead of reading these quantities from the input lines. In this case, <code>Gravity</code> can calculate the field considerably more quickly. If geoid heights are being computed (the <code>-H</code> option), then <i>h</i> must be zero.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i>. By default <i>prec</i> is 5 for acceleration due to gravity, 3 for the gravity disturbance and anomaly, and 4 for the geoid height.</p>
<dt><code>-v</code></p>
<dd>print information about the gravity model on standard error before processing the input.</p>
<dt><code>&#8211;comment-delimiter</code></p>
<dd>set the comment delimiter to <i>commentdelim</i> (e.g., &#8220;#&#8221; or &#8220;//&#8221;). If set, the input lines will be scanned for this delimiter and, if found, the delimiter and the rest of the line will be removed prior to processing and subsequently appended to the output line (separated by a space).</p>
<dt><code>&#8211;version</code></p>
<dd>print version and exit.</p>
<dt><code>-h</code></p>
<dd>print usage, the default gravity path and name, and exit.</p>
<dt><code>&#8211;help</code></p>
<dd>print full documentation and exit.</p>
<dt><code>&#8211;input-file</code></p>
<dd>read input from the file <i>infile</i> instead of from standard input; a file name of &#8220;-&#8221; stands for standard input.</p>
<dt><code>&#8211;input-string</code></p>
<dd>read input from the string <i>instring</i> instead of from standard input. All occurrences of the line separator character (default is a semicolon) in <i>instring</i> are converted to newlines before the reading begins.</p>
<dt><code>&#8211;line-separator</code></p>
<dd>set the line separator character to <i>linesep</i>. By default this is a semicolon.</p>
<dt><code>&#8211;output-file</code></p>
<dd>write output to the file <i>outfile</i> instead of to standard output; a file name of &#8220;-&#8221; stands for standard output.</dl>
<h2>Models</h2>
<p><code>Gravity</code> computes the gravity field using one of the following models </p>
<pre> egm84, earth gravity model 1984. See
 <a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/wgs84_180/wgs84_180.html">http://earth-info.nga.mil/GandG/wgs84/gravitymod/wgs84_180/wgs84_180.html</a>
 egm96, earth gravity model 1996. See
 <a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.html">http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.html</a>
 egm2008, earth gravity model 2008. See
 <a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008">http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008</a>
 wgs84, world geodetic system 1984. This returns the normal
 gravity for the WGS84 ellipsoid.
 grs80, geodetic reference system 1980. This returns the normal
 gravity for the GRS80 ellipsoid.</pre>
<p>These models approximate the gravitation field above the surface of the earth. By default, the <tt>&quot;egm96&quot;</tt> gravity model is used. This may changed by setting the environment variable <tt>&quot;GEOGRAPHICLIB_GRAVITY_NAME&quot;</tt> or with the <code>-n</code> option. </p>
<p> The gravity models will be loaded from a directory specified at compile time. This may changed by setting the environment variables <tt>&quot;GEOGRAPHICLIB_GRAVITY_PATH&quot;</tt> or <tt>&quot;GEOGRAPHICLIB_DATA&quot;</tt>, or with the <code>-d</code> option. The <code>-h</code> option prints the default gravity path and name. Use the <code>-v</code> option to ascertain the full path name of the data file. </p>
<p> Instructions for downloading and installing gravity models are available at &lt;<a rel="nofollow" href="http://geographiclib.sf.net/html/gravity.html#gravityinst">http://geographiclib.sf.net/html/gravity.html#gravityinst</a>&gt;.</p>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_GRAVITY_NAME</code></font></p>
<dd>Override the compile-time default gravity name of <tt>&quot;egm96&quot;</tt>. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_GRAVITY_NAME</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-n</code> <i>name</i> option is used, then <i>name</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_GRAVITY_PATH</code></font></p>
<dd>Override the compile-time default gravity path. This is typically <tt>&quot;/usr/local/share/GeographicLib/gravity&quot;</tt> on Unix-like systems and <tt>&quot;C:/ProgramData/GeographicLib/gravity&quot;</tt> on Windows systems. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_GRAVITY_PATH</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-d</code> <i>dir</i> option is used, then <i>dir</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font></p>
<dd>Another way of overriding the compile-time default gravity path. If it is set (and if <font SIZE="-1"><code>GEOGRAPHICLIB_GRAVITY_PATH</code></font> is not set), then $<font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font>/gravity is used.</dl>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>Gravity</code> to return an exit code of 1. However, an error does not cause <code>Gravity</code> to terminate; following lines will be converted.</p>
<h2>Examples</h2>
<p>The gravity field from <font SIZE="-1">EGM2008</font> at the top of Mount Everest </p>
<pre> echo 27:59:17N 86:55:32E 8820 | Gravity -n egm2008
 =&gt; -0.00001 0.00103 -9.76782</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1), <i><a href="/docs/linux/man/1-geoideval/">GeoidEval</a></i>(1), <i><a href="/docs/linux/man/8-geographiclib-get-gravity/">geographiclib-get-gravity</a></i>(8).</p>
<h2>Author</h2>
<p><code>Gravity</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>Gravity</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in version 1.16.</p>
