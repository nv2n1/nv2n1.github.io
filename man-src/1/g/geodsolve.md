---
title: "geodsolve(1)"
name: "geodsolve"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geodsolve/"
description: "GeodSolve — perform geodesic calculations"
---

<p>GeodSolve &#8212; perform geodesic calculations </p>
<h2>Synopsis</h2>
<p><code>GeodSolve</code> [ <code>-i</code> | <code>-l</code> <i>lat1</i> <i>lon1</i> <i>azi1</i> ] [ <code>-a</code> ] [ <code>-e</code> <i>a</i> <i>f</i> ] <code>-u</code> ] [ <code>-d</code> | <code>-:</code> ] [ <code>-b</code> ] [ <code>-f</code> ] [ <code>-p</code> <i>prec</i> ] [ <code>-E</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>The shortest path between two points on the ellipsoid at (<i>lat1</i>, <i>lon1</i>) and (<i>lat2</i>, <i>lon2</i>) is called the geodesic. Its length is <i>s12</i> and the geodesic from point 1 to point 2 has forward azimuths <i>azi1</i> and <i>azi2</i> at the two end points. </p>
<p> <code>GeodSolve</code> operates in one of three modes:</p>
<dl>
<dt>1.</p>
<dd>By default, <code>GeodSolve</code> accepts lines on the standard input containing <i>lat1</i> <i>lon1</i> <i>azi1</i> <i>s12</i> and prints <i>lat2</i> <i>lon2</i> <i>azi2</i> on standard output. This is the direct geodesic calculation.</p>
<dt>2.</p>
<dd>Command line arguments <code>-l</code> <i>lat1</i> <i>lon1</i> <i>azi1</i> specify a geodesic line. <code>GeodSolve</code> then accepts a sequence of <i>s12</i> values (one per line) on standard input and prints <i>lat2</i> <i>lon2</i> <i>azi2</i> for each. This generates a sequence of points on a single geodesic.</p>
<dt>3.</p>
<dd>With the <code>-i</code> command line argument, <code>GeodSolve</code> performs the inverse geodesic calculation. It reads lines containing <i>lat1</i> <i>lon1</i> <i>lat2</i> <i>lon2</i> and prints the corresponding values of <i>azi1</i> <i>azi2</i> <i>s12</i>.</dl>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>perform an inverse geodesic calculation (see 3 above).</p>
<dt><code>-l</code></p>
<dd>line mode (see 2 above); generate a sequence of points along the geodesic specified by <i>lat1</i> <i>lon1</i> <i>azi1</i>.</p>
<dt><code>-a</code></p>
<dd>arc mode; on input <i>and</i> output <i>s12</i> is replaced by <i>a12</i> the arc length (in degrees) on the auxiliary sphere. See &#8220;<font SIZE="-1">AUXILIARY SPHERE&#8221;</font>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
<dt><code>-u</code></p>
<dd>unroll the longitude. On input longitudes must lie in [-540deg,540deg) and, normally, on output longitudes are reduced to lie in [-180deg,180deg). However with this option, the returned longitude <i>lon2</i> is &#8220;unrolled&#8221; so that <i>lon2</i> &#8211; <i>lon1</i> indicates how often and in what sense the geodesic has encircled the earth.</p>
<dt><code>-d</code></p>
<dd>output angles as degrees, minutes, seconds instead of decimal degrees.</p>
<dt><code>-:</code></p>
<dd>like <code>-d</code>, except use : as a separator instead of the d, &#8216;, and &quot; delimiters.</p>
<dt><code>-b</code></p>
<dd>report the <i>back</i> azimuth at point 2 instead of the forward azimuth.</p>
<dt><code>-f</code></p>
<dd>full output; each line of output consists of 12 quantities: <i>lat1</i> <i>lon1</i> <i>azi1</i> <i>lat2</i> <i>lon2</i> <i>azi2</i> <i>s12</i> <i>a12</i> <i>m12</i> <i>M12</i> <i>M21</i> <i>S12</i>. <i>a12</i> is described in &#8220;<font SIZE="-1">AUXILIARY SPHERE&#8221;</font>. The four quantities <i>m12</i>, <i>M12</i>, <i>M21</i>, and <i>S12</i> are described in &#8220;<font SIZE="-1">ADDITIONAL QUANTITIES&#8221;</font>.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 3); <i>prec</i> is the precision relative to 1 m. See &#8220;<font SIZE="-1">PRECISION&#8221;</font>.</p>
<dt><code>-E</code></p>
<dd>use &#8220;exact&#8221; algorithms (based on elliptic integrals) for the geodesic calculations. These are more accurate than the (default) series expansions for |<i>f</i>| &gt; 0.02.</p>
<dt><code>&#8211;comment-delimiter</code></p>
<dd>set the comment delimiter to <i>commentdelim</i> (e.g., &#8220;#&#8221; or &#8220;//&#8221;). If set, the input lines will be scanned for this delimiter and, if found, the delimiter and the rest of the line will be removed prior to processing and subsequently appended to the output line (separated by a space).</p>
<dt><code>&#8211;version</code></p>
<dd>print version and exit.</p>
<dt><code>-h</code></p>
<dd>print usage and exit.</p>
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
<h2>Input</h2>
<p><code>GeodSolve</code> measures all angles in degrees and all lengths (<i>s12</i>) in meters. On input angles (latitude, longitude, azimuth, arc length) can be as decimal degrees or degrees (d), minutes (&#8216;), seconds (&#8220;). A decimal point can only appear in the least significant component and the designator (d, &#8216;, or &#8221;) for this component is optional; thus <tt>&quot;40d30&quot;</tt>, <tt>&quot;40d30'&quot;</tt>, <tt>&quot;40.5d&quot;</tt>, and <tt>40.5</tt> are all equivalent. By default, latitude precedes longitude for each point; however on input either may be given first by appending (or prepending) <i>N</i> or <i>S</i> to the latitude and <i>E</i> or <i>W</i> to the longitude. Azimuths are measured clockwise from north; however this may be overridden with <i>E</i> or <i>W</i>. </p>
<p> See the <tt>&quot;QUOTING&quot;</tt> section of <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1) for how to quote the <font SIZE="-1">DMS</font> designators &#8216; and &quot;.</p>
<h2>Auxiliary Sphere</h2>
<p>Geodesics on the ellipsoid can be transferred to the <i>auxiliary sphere</i> on which the distance is measured in terms of the arc length <i>a12</i> (measured in degrees) instead of <i>s12</i>. In terms of <i>a12</i>, 180 degrees is the distance from one equator crossing to the next or from the minimum latitude to the maximum latitude. Geodesics with <i>a12</i> &gt; 180 degrees do not correspond to shortest paths. With the <code>-a</code> flag, <i>s12</i> (on both input and output) is replaced by <i>a12</i>. The <code>-a</code> flag does <i>not</i> affect the full output given by the <code>-f</code> flag (which always includes both <i>s12</i> and <i>a12</i>).</p>
<h2>Additional Quantities</h2>
<p>The <code>-f</code> flag reports four additional quantities. </p>
<p> The reduced length of the geodesic, <i>m12</i>, is defined such that if the initial azimuth is perturbed by d<i>azi1</i> (radians) then the second point is displaced by <i>m12</i> d<i>azi1</i> in the direction perpendicular to the geodesic. <i>m12</i> is given in meters. On a curved surface the reduced length obeys a symmetry relation, <i>m12</i> + <i>m21</i> = 0. On a flat surface, we have <i>m12</i> = <i>s12</i>. </p>
<p> <i>M12</i> and <i>M21</i> are geodesic scales. If two geodesics are parallel at point 1 and separated by a small distance <i>dt</i>, then they are separated by a distance <i>M12</i> <i>dt</i> at point 2. <i>M21</i> is defined similarly (with the geodesics being parallel to one another at point 2). <i>M12</i> and <i>M21</i> are dimensionless quantities. On a flat surface, we have <i>M12</i> = <i>M21</i> = 1. </p>
<p> If points 1, 2, and 3 lie on a single geodesic, then the following addition rules hold, <i>s13</i> = <i>s12</i> + <i>s23</i>, <i>a13</i> = <i>a12</i> + <i>a23</i>, <i>S13</i> = <i>S12</i> + <i>S23</i>, <i>m13</i> = <i>m12</i> <i>M23</i> + <i>m23</i> <i>M21</i>, <i>M13</i> = <i>M12</i> <i>M23</i> &#8211; (1 &#8211; <i>M12</i> <i>M21</i>) <i>m23</i> / <i>m12</i>, and <i>M31</i> = <i>M32</i> <i>M21</i> &#8211; (1 &#8211; <i>M23</i> <i>M32</i>) <i>m12</i> / <i>m23</i>. </p>
<p> Finally, <i>S12</i> is the area between the geodesic from point 1 to point 2 and the equator; i.e., it is the area, measured counter-clockwise, of the geodesic quadrilateral with corners (<i>lat1</i>,<i>lon1</i>), (0,<i>lon1</i>), (0,<i>lon2</i>), and (<i>lat2</i>,<i>lon2</i>). It is given in meters^2.</p>
<h2>Precision</h2>
<p><i>prec</i> gives precision of the output with <i>prec</i> = 0 giving 1 m precision, <i>prec</i> = 3 giving 1 mm precision, etc. <i>prec</i> is the number of digits after the decimal point for lengths. For decimal degrees, the number of digits after the decimal point is <i>prec</i> + 5. For <font SIZE="-1">DMS </font>(degree, minute, seconds) output, the number of digits after the decimal point in the seconds component is <i>prec</i> + 1. The minimum value of <i>prec</i> is 0 and the maximum is 10.</p>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>GeodSolve</code> to return an exit code of 1. However, an error does not cause <code>GeodSolve</code> to terminate; following lines will be converted.</p>
<h2>Accuracy</h2>
<p>Using the (default) series solution, GeodSolve is accurate to about 15 nm (15 nanometers) for the <font SIZE="-1">WGS84</font> ellipsoid. The approximate maximum error (expressed as a distance) for an ellipsoid with the same major radius as the <font SIZE="-1">WGS84</font> ellipsoid and different values of the flattening is </p>
<pre> |f| error
 0.01 25 nm
 0.02 30 nm
 0.05 10 um
 0.1 1.5 mm
 0.2 300 mm</pre>
<p>If <code>-E</code> is specified, GeodSolve is accurate to about 40 nm (40 nanometers) for the <font SIZE="-1">WGS84</font> ellipsoid. The approximate maximum error (expressed as a distance) for an ellipsoid with a quarter meridian of 10000 km and different values of the <i>a/b</i> = 1 &#8211; <i>f</i> is </p>
<pre> 1-f error (nm)
 1/128 387
 1/64 345
 1/32 269
 1/16 210
 1/8 115
 1/4 69
 1/2 36
 1 15
 2 25
 4 96
 8 318
 16 985
 32 2352
 64 6008
 128 19024</pre>
<h2>Multiple Solutions</h2>
<p>The shortest distance returned for the inverse problem is (obviously) uniquely defined. However, in a few special cases there are multiple azimuths which yield the same shortest distance. Here is a catalog of those cases:</p>
<dl>
<dt><i>lat1</i> = &#8211;<i>lat2</i> (with neither point at a pole)</p>
<dd>If <i>azi1</i> = <i>azi2</i>, the geodesic is unique. Otherwise there are two geodesics and the second one is obtained by setting [<i>azi1</i>,<i>azi2</i>] = [<i>azi2</i>,<i>azi1</i>], [<i>M12</i>,<i>M21</i>] = [<i>M21</i>,<i>M12</i>], <i>S12</i> = &#8211;<i>S12</i>. (This occurs when the longitude difference is near +/-180 for oblate ellipsoids.)</p>
<dt><i>lon2</i> = <i>lon1</i> +/- 180 (with neither point at a pole)</p>
<dd>If <i>azi1</i> = 0 or +/-180, the geodesic is unique. Otherwise there are two geodesics and the second one is obtained by setting [<i>azi1</i>,<i>azi2</i>] = [-<i>azi1</i>,-<i>azi2</i>], <i>S12</i> = &#8211;<i>S12</i>. (This occurs when <i>lat2</i> is near &#8211;<i>lat1</i> for prolate ellipsoids.)</p>
<dt>Points 1 and 2 at opposite poles</p>
<dd>There are infinitely many geodesics which can be generated by setting [<i>azi1</i>,<i>azi2</i>] = [<i>azi1</i>,<i>azi2</i>] + [<i>d</i>,-<i>d</i>], for arbitrary <i>d</i>. (For spheres, this prescription applies when points 1 and 2 are antipodal.)</p>
<dt><i>s12</i> = 0 (coincident points)</p>
<dd>There are infinitely many geodesics which can be generated by setting [<i>azi1</i>,<i>azi2</i>] = [<i>azi1</i>,<i>azi2</i>] + [<i>d</i>,<i>d</i>], for arbitrary <i>d</i>.</dl>
<h2>Examples</h2>
<p>Route from <font SIZE="-1">JFK</font> Airport to Singapore Changi Airport: </p>
<pre> echo 40:38:23N 073:46:44W 01:21:33N 103:59:22E |
 GeodSolve -i -: -p 0
 003:18:29.9 177:29:09.2 15347628</pre>
<p>Waypoints on the route at intervals of 2000km: </p>
<pre> for ((i = 0; i &lt;= 16; i += 2)); do echo ${i}000000;done |
 GeodSolve -l 40:38:23N 073:46:44W 003:18:29.9 -: -p 0
 40:38:23.0N 073:46:44.0W 003:18:29.9
 58:34:45.1N 071:49:36.7W 004:48:48.8
 76:22:28.4N 065:32:17.8W 010:41:38.4
 84:50:28.0N 075:04:39.2E 150:55:00.9
 67:26:20.3N 098:00:51.2E 173:27:20.3
 49:33:03.2N 101:06:52.6E 176:07:54.3
 31:34:16.5N 102:30:46.3E 177:03:08.4
 13:31:56.0N 103:26:50.7E 177:24:55.0
 04:32:05.7S 104:14:48.7E 177:28:43.6</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1). </p>
<p> An online version of this utility is availbable at &lt;<a rel="nofollow" href="http://geographiclib.sourceforge.net/cgi-bin/GeodSolve">http://geographiclib.sourceforge.net/cgi-bin/GeodSolve</a>&gt;. </p>
<p> The algorithms are described in C. F. F. Karney, <i>Algorithms for geodesics</i>, J. Geodesy 87, 43-55 (2013); <font SIZE="-1">DOI: </font>&lt;<a rel="nofollow" href="https://dx.doi.org/10.1007/s00190-012-0578-z">https://dx.doi.org/10.1007/s00190-012-0578-z</a>&gt;; addenda: &lt;<a rel="nofollow" href="http://geographiclib.sf.net/geod-addenda.html">http://geographiclib.sf.net/geod-addenda.html</a>&gt;. </p>
<p> The Wikipedia page, Geodesics on an ellipsoid, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid">https://en.wikipedia.org/wiki/Geodesics_on_an_ellipsoid</a>&gt;.</p>
<h2>Author</h2>
<p><code>GeodSolve</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>GeodSolve</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-03. Prior to version 1.30, it was called <code>Geod</code>. (The name was changed to avoid a conflict with the <code>geod</code> utility in <i>proj.4</i>.)</p>
