---
title: "rhumbsolve(1)"
name: "rhumbsolve"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rhumbsolve/"
description: "RhumbSolve — perform rhumb line calculations"
---

<p>RhumbSolve &#8212; perform rhumb line calculations </p>
<h2>Synopsis</h2>
<p><code>RhumbSolve</code> [ <code>-i</code> | <code>-l</code> <i>lat1</i> <i>lon1</i> <i>azi12</i> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>-d</code> | <code>-:</code> ] [ <code>-p</code> <i>prec</i> ] [ <code>-s</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>The path with constant heading between two points on the ellipsoid at (<i>lat1</i>, <i>lon1</i>) and (<i>lat2</i>, <i>lon2</i>) is called the rhumb line or loxodrome. Its length is <i>s12</i> and the rhumb line has a forward azimuth <i>azi12</i> along its length. Also computed is <i>S12</i> is the area between the rhumb line from point 1 to point 2 and the equator; i.e., it is the area, measured counter-clockwise, of the geodesic quadrilateral with corners (<i>lat1</i>,<i>lon1</i>), (0,<i>lon1</i>), (0,<i>lon2</i>), and (<i>lat2</i>,<i>lon2</i>). A point at a pole is treated as a point a tiny distance away from the pole on the given line of longitude. The longitude becomes indeterminate when a rhumb line passes through a pole, and <code>RhumbSolve</code> reports NaNs for the longitude and the area in this case. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> the rhumb line is <code>not</code> the shortest path between two points; that is the geodesic and it is calculated by <i><a href="/docs/linux/man/1-geodsolve/">GeodSolve</a></i>(1). </p>
<p> <code>RhumbSolve</code> operates in one of three modes:</p>
<dl>
<dt>1.</p>
<dd>By default, <code>RhumbSolve</code> accepts lines on the standard input containing <i>lat1</i> <i>lon1</i> <i>azi12</i> <i>s12</i> and prints <i>lat2</i> <i>lon2</i> <i>S12</i> on standard output. This is the direct calculation.</p>
<dt>2.</p>
<dd>Command line arguments <code>-l</code> <i>lat1</i> <i>lon1</i> <i>azi12</i> specify a rhumb line. <code>RhumbSolve</code> then accepts a sequence of <i>s12</i> values (one per line) on standard input and prints <i>lat2</i> <i>lon2</i> <i>S12</i> for each. This generates a sequence of points on a rhumb line.</p>
<dt>3.</p>
<dd>With the <code>-i</code> command line argument, <code>RhumbSolve</code> performs the inverse calculation. It reads lines containing <i>lat1</i> <i>lon1</i> <i>lat2</i> <i>lon2</i> and prints the values of <i>azi12</i> <i>s12</i> <i>S12</i> for the corresponding shortest rhumb lines. If the end points are on opposite meridians, there are two shortest rhumb lines and the east-going one is chosen.</dl>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>perform an inverse calculation (see 3 above).</p>
<dt><code>-l</code></p>
<dd>line mode (see 2 above); generate a sequence of points along the rhumb line specified by <i>lat1</i> <i>lon1</i> <i>azi12</i>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
<dt><code>-d</code></p>
<dd>output angles as degrees, minutes, seconds instead of decimal degrees.</p>
<dt><code>-:</code></p>
<dd>like <code>-d</code>, except use : as a separator instead of the d, &#8216;, and &quot; delimiters.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 3); <i>prec</i> is the precision relative to 1 m. See &#8220;<font SIZE="-1">PRECISION&#8221;</font>.</p>
<dt><code>-s</code></p>
<dd>By default, the rhumb line calculations are carried out exactly in terms of elliptic integrals. This includes the use of the addition theorem for elliptic integrals to compute the divided difference of the isometric and rectifying latitudes. If <code>-s</code> is supplied this divided difference is computed using Krueger series for the transverse Mercator projection which is only accurate for |<i>f</i>| &lt; 0.01. See &#8220;<font SIZE="-1">ACCURACY&#8221;</font>.</p>
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
<p><code>RhumbSolve</code> measures all angles in degrees, all lengths (<i>s12</i>) in meters, and all areas (<i>S12</i>) in meters^2. On input angles (latitude, longitude, azimuth) can be as decimal degrees or degrees (d), minutes (&#8216;), seconds (&#8220;). A decimal point can only appear in the least significant component and the designator (d, &#8216;, or &#8221;) for this component is optional; thus <tt>&quot;40d30&quot;</tt>, <tt>&quot;40d30'&quot;</tt>, <tt>&quot;40.5d&quot;</tt>, and <tt>40.5</tt> are all equivalent. By default, latitude precedes longitude for each point; however on input either may be given first by appending (or prepending) <i>N</i> or <i>S</i> to the latitude and <i>E</i> or <i>W</i> to the longitude. Azimuths are measured clockwise from north; however this may be overridden with <i>E</i> or <i>W</i>. </p>
<p> See the <tt>&quot;QUOTING&quot;</tt> section of <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1) for how to quote the <font SIZE="-1">DMS</font> designators &#8216; and &quot;.</p>
<h2>Precision</h2>
<p><i>prec</i> gives precision of the output with <i>prec</i> = 0 giving 1 m precision, <i>prec</i> = 3 giving 1 mm precision, etc. <i>prec</i> is the number of digits after the decimal point for lengths. For decimal degrees, the number of digits after the decimal point is <i>prec</i> + 5. For <font SIZE="-1">DMS </font>(degree, minute, seconds) output, the number of digits after the decimal point in the seconds component is <i>prec</i> + 1. The minimum value of <i>prec</i> is 0 and the maximum is 10.</p>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>RhumbSolve</code> to return an exit code of 1. However, an error does not cause <code>RhumbSolve</code> to terminate; following lines will be converted.</p>
<h2>Accuracy</h2>
<p>The algorithm used by <code>RhumbSolve</code> uses exact formulas for converting between the latitude, rectifying latitude (<i>mu</i>), and isometric latitude (<i>psi</i>). These formulas are accurate for any value of the flattening. The computation of rhumb lines involves the ratio (<i>psi1</i> &#8211; <i>psi2</i>) / (<i>mu1</i> &#8211; <i>mu2</i>) and this is subject to large round-off errors if <i>lat1</i> is close to <i>lat2</i>. So this ratio is computed using divided differences using one of two methods: by default, this uses the addition theorem for elliptic integrals (accurate for all values of <i>f</i>); however, with the <code>-s</code> options, it is computed using the series expansions used by <i><a href="/docs/linux/man/1-transversemercatorproj/">TransverseMercatorProj</a></i>(1) for the conversions between rectifying and conformal latitudes (accurate for |<i>f</i>| &lt; 0.01). For the <font SIZE="-1">WGS84</font> ellipsoid, the error is about 10 nanometers using either method.</p>
<h2>Examples</h2>
<p>Route from <font SIZE="-1">JFK</font> Airport to Singapore Changi Airport: </p>
<pre> echo 40:38:23N 073:46:44W 01:21:33N 103:59:22E |
 RhumbSolve -i -: -p 0
 103:34:58.2 18523563</pre>
<p>N.B. This is <code>not</code> the route typically taken by aircraft because it&#8217;s considerably longer than the geodesic given by <i><a href="/docs/linux/man/1-geodsolve/">GeodSolve</a></i>(1). </p>
<p> Waypoints on the route at intervals of 2000km: </p>
<pre> for ((i = 0; i &lt;= 20; i += 2)); do echo ${i}000000;done |
 RhumbSolve -l 40:38:23N 073:46:44W 103:34:58.2 -: -p 0
 40:38:23.0N 073:46:44.0W
 36:24:30.3N 051:28:26.4W
 32:10:26.8N 030:20:57.3W
 27:56:13.2N 010:10:54.2W
 23:41:50.1N 009:12:45.5E
 19:27:18.7N 027:59:22.1E
 15:12:40.2N 046:17:01.1E
 10:57:55.9N 064:12:52.8E
 06:43:07.3N 081:53:28.8E
 02:28:16.2N 099:24:54.5E
 01:46:36.0S 116:52:59.7E</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1), <i><a href="/docs/linux/man/1-geodsolve/">GeodSolve</a></i>(1), <i><a href="/docs/linux/man/1-transversemercatorproj/">TransverseMercatorProj</a></i>(1). </p>
<p> An online version of this utility is availbable at &lt;<a rel="nofollow" href="http://geographiclib.sourceforge.net/cgi-bin/RhumbSolve">http://geographiclib.sourceforge.net/cgi-bin/RhumbSolve</a>&gt;. </p>
<p> The Wikipedia page, Rhumb line, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Rhumb_line">https://en.wikipedia.org/wiki/Rhumb_line</a>&gt;.</p>
<h2>Author</h2>
<p><code>RhumbSolve</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>RhumbSolve</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in version 1.37.</p>
