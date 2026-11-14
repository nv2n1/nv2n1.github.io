---
title: "geodesicproj(1)"
name: "geodesicproj"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geodesicproj/"
description: "GeodesicProj — perform projections based on geodesics"
---

<p>GeodesicProj &#8212; perform projections based on geodesics </p>
<h2>Synopsis</h2>
<p><code>GeodesicProj</code> ( <code>-z</code> | <code>-c</code> | <code>-g</code> ) <i>lat0</i> <i>lon0</i> [ <code>-r</code> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>Perform projections based on geodesics. Convert geodetic coordinates to either azimuthal equidistant, Cassini-Soldner, or gnomonic coordinates. The center of the projection (<i>lat0</i>, <i>lon0</i>) is specified by either the <code>-c</code> option (for Cassini-Soldner), the <code>-z</code> option (for azimuthal equidistant), or the <code>-g</code> option (for gnomonic). At least one of these options must be given (the last one given is used). </p>
<p> Geodetic coordinates are provided on standard input as a set of lines containing (blank separated) <i>latitude</i> and <i>longitude</i> (decimal degrees or degrees, minutes, seconds). For each set of geodetic coordinates, the corresponding projected coordinates <i>x</i>, <i>y</i> (meters) are printed on standard output together with the azimuth <i>azi</i> (degrees) and reciprocal scale <i>rk</i>. For Cassini-Soldner, <i>azi</i> is the bearing of the easting direction and the scale in the easting direction is 1 and the scale in the northing direction is 1/<i>rk</i>. For azimuthal equidistant and gnomonic, <i>azi</i> is the bearing of the radial direction and the scale in the azimuthal direction is 1/<i>rk</i>. For azimuthal equidistant and gnomonic, the scales in the radial direction are 1 and 1/<i>rk</i>^2, respectively.</p>
<h2>Options</h2>
<dl>
<dt><code>-z</code></p>
<dd>use the azimuthal equidistant projection centered at latitude = <i>lat0</i>, longitude = <i>lon0</i>.</p>
<dt><code>-c</code></p>
<dd>use the Cassini-Soldner projection centered at latitude = <i>lat0</i>, longitude = <i>lon0</i>.</p>
<dt><code>-g</code></p>
<dd>use the ellipsoidal gnomonic projection centered at latitude = <i>lat0</i>, longitude = <i>lon0</i>.</p>
<dt><code>-r</code></p>
<dd>perform the reverse projection. <i>x</i> and <i>y</i> are given on standard input and each line of standard output gives <i>latitude</i>, <i>longitude</i>, <i>azi</i>, and <i>rk</i>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 6). <i>prec</i> is the number of digits after the decimal point for lengths (in meters). For latitudes, longitudes, and azimuths (in degrees), the number of digits after the decimal point is <i>prec</i> + 5. For the scale, the number of digits after the decimal point is <i>prec</i> + 6.</p>
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
<h2>Examples</h2>
<pre> echo 48.648 -2.007 | GeodesicProj -c 48.836 2.337
 =&gt; -319919 -11791 86.7 0.999
 echo -319919 -11791 | GeodesicProj -c 48.836 2.337 -r
 =&gt; 48.648 -2.007 86.7 0.999</pre>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>GeodesicProj</code> to return an exit code of 1. However, an error does not cause <code>GeodesicProj</code> to terminate; following lines will be converted.</p>
<h2>See Also</h2>
<p>The ellipsoidal gnomonic projection is derived in Section 8 of C. F. F. Karney, <i>Algorithms for geodesics</i>, J. Geodesy 87, 43-55 (2013); <font SIZE="-1">DOI </font>&lt;<a rel="nofollow" href="https://dx.doi.org/10.1007/s00190-012-0578-z">https://dx.doi.org/10.1007/s00190-012-0578-z</a>&gt;; addenda: &lt;<a rel="nofollow" href="http://geographiclib.sf.net/geod-addenda.html">http://geographiclib.sf.net/geod-addenda.html</a>&gt;.</p>
<h2>Author</h2>
<p><code>GeodesicProj</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>GeodesicProj</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-08. Prior to version 1.9 it was called EquidistantTest.</p>
