---
title: "planimeter(1)"
name: "planimeter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-planimeter/"
description: "Planimeter — compute the area of geodesic polygons"
---

<p>Planimeter &#8212; compute the area of geodesic polygons </p>
<h2>Synopsis</h2>
<p><code>Planimeter</code> [ <code>-r</code> ] [ <code>-s</code> ] [ <code>-l</code> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>-G</code> | <code>-E</code> | <code>-Q</code> | <code>-R</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>Measure the area of a geodesic polygon. Reads polygon vertices from standard input, one per line. Vertices may be given as latitude and longitude, <font SIZE="-1">UTM/UPS,</font> or <font SIZE="-1">MGRS</font> coordinates, interpreted in the same way as <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1). (<font SIZE="-1">MGRS</font> coordinates signify the center of the corresponding <font SIZE="-1">MGRS</font> square.) The end of input, a blank line, or a line which can&#8217;t be interpreted as a vertex signals the end of one polygon and the start of the next. For each polygon print a summary line with the number of points, the perimeter (in meters), and the area (in meters^2). </p>
<p> The edges of the polygon are given by the <i>shortest</i> geodesic between consecutive vertices. In certain cases, there may be two or many such shortest geodesics, and in that case, the polygon is not uniquely specified by its vertices. This only happens with very long edges (for the <font SIZE="-1">WGS84</font> ellipsoid, any edge shorter than 19970 km is uniquely specified by its end points). In such cases, insert an additional vertex near the middle of the long edge to define the boundary of the polygon. </p>
<p> By default, polygons traversed in a counter-clockwise direction return a positive area and those traversed in a clockwise direction return a negative area. This sign convention is reversed if the <code>-r</code> option is given. </p>
<p> Of course, encircling an area in the clockwise direction is equivalent to encircling the rest of the ellipsoid in the counter-clockwise direction. The default interpretation used by <code>Planimeter</code> is the one that results in a smaller magnitude of area; i.e., the magnitude of the area is less than or equal to one half the total area of the ellipsoid. If the <code>-s</code> option is given, then the interpretation used is the one that results in a positive area; i.e., the area is positive and less than the total area of the ellipsoid. </p>
<p> Only simple (i.e., non-self-intersecting) polygons are supported for the area computation. Polygons may include one or both poles. There is no need to close the polygon.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code></p>
<dd>toggle whether counter-clockwise traversal of the polygon returns a positive (the default) or negative result.</p>
<dt><code>-s</code></p>
<dd>toggle whether to return a signed result (the default) or not.</p>
<dt><code>-l</code></p>
<dd>toggle whether the vertices represent a polygon (the default) or a polyline. For a polyline, the number of points and the length of the path joining them is returned; the path is not closed and the area is not reported.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563. If entering vertices as <font SIZE="-1">UTM/UPS</font> or <font SIZE="-1">MGRS</font> coordinates, use the default ellipsoid, since the conversion of these coordinates to latitude and longitude always uses the <font SIZE="-1">WGS84</font> parameters.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 6); the perimeter is given (in meters) with <i>prec</i> digits after the decimal point; the area is given (in meters^2) with (<i>prec</i> &#8211; 5) digits after the decimal point.</p>
<dt><code>-G</code></p>
<dd>use the series formulation for the geodesics. This is the default option and is recommended for terrestrial applications. This option, <code>-G</code>, and the following three options, <code>-E</code>, <code>-Q</code>, and <code>-R</code>, are mutually exclusive.</p>
<dt><code>-E</code></p>
<dd>use &#8220;exact&#8221; algorithms (based on elliptic integrals) for the geodesic calculations. These are more accurate than the (default) series expansions for |<i>f</i>| &gt; 0.02. (But note that the implementation of areas in GeodesicExact uses a high order series and this is only accurate for modest flattenings.)</p>
<dt><code>-Q</code></p>
<dd>perform the calculation on the authalic sphere. The area calculation is accurate even if the flattening is large, <i>provided</i> the edges are sufficiently short. The perimeter calculation is not accurate.</p>
<dt><code>-R</code></p>
<dd>The lines joining the vertices are rhumb lines instead of geodesics.</p>
<dt><code>&#8211;comment-delimiter</code></p>
<dd>set the comment delimiter to <i>commentdelim</i> (e.g., &#8220;#&#8221; or &#8220;//&#8221;). If set, the input lines will be scanned for this delimiter and, if found, the delimiter and the rest of the line will be removed prior to processing. For a given polygon, the last such string found will be appended to the output line (separated by a space).</p>
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
<p>Example (the area of the 100km <font SIZE="-1">MGRS</font> square 18SWK) </p>
<pre> Planimeter &lt;&lt;EOF
 18n 500000 4400000
 18n 600000 4400000
 18n 600000 4500000
 18n 500000 4500000
 EOF
 =&gt; 4 400139.53295860 10007388597.1913</pre>
<p>The following code takes the output from gdalinfo and reports the area covered by the data (assuming the edges of the image are geodesics). </p>
<pre> #! /bin/sh
 egrep '^((Upper|Lower) (Left|Right)|Center) ' |
 sed -e 's/d /d/g' -e &quot;s/' /'/g&quot; | tr -s '(),	' ' ' | awk '{
 if ($1 $2 == &quot;UpperLeft&quot;)
 ul = $6 &quot; &quot; $5;
 else if ($1 $2 == &quot;LowerLeft&quot;)
 ll = $6 &quot; &quot; $5;
 else if ($1 $2 == &quot;UpperRight&quot;)
 ur = $6 &quot; &quot; $5;
 else if ($1 $2 == &quot;LowerRight&quot;)
 lr = $6 &quot; &quot; $5;
 else if ($1 == &quot;Center&quot;) {
 printf &quot;%s
%s
%s
%s

&quot;, ul, ll, lr, ur;
 ul = ll = ur = lr = &quot;&quot;;
 }
 }
 ' | Planimeter | cut -f3 -d' '</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1), <i><a href="/docs/linux/man/1-geodsolve/">GeodSolve</a></i>(1). </p>
<p> An online version of this utility is availbable at &lt;<a rel="nofollow" href="http://geographiclib.sourceforge.net/cgi-bin/Planimeter">http://geographiclib.sourceforge.net/cgi-bin/Planimeter</a>&gt;. </p>
<p> The algorithm for the area of geodesic polygon is given in Section 6 of C. F. F. Karney, <i>Algorithms for geodesics</i>, J. Geodesy 87, 43-55 (2013); <font SIZE="-1">DOI </font>&lt;<a rel="nofollow" href="https://dx.doi.org/10.1007/s00190-012-0578-z">https://dx.doi.org/10.1007/s00190-012-0578-z</a>&gt;; addenda: &lt;<a rel="nofollow" href="http://geographiclib.sf.net/geod-addenda.html">http://geographiclib.sf.net/geod-addenda.html</a>&gt;.</p>
<h2>Author</h2>
<p><code>Planimeter</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>Planimeter</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in version 1.4.</p>
