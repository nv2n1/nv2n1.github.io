---
title: "conicproj(1)"
name: "conicproj"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conicproj/"
description: "ConicProj — perform conic projections"
---

<p>ConicProj &#8212; perform conic projections </p>
<h2>Synopsis</h2>
<p><code>ConicProj</code> ( <code>-c</code> | <code>-a</code> ) <i>lat1</i> <i>lat2</i> [ <code>-l</code> <i>lon0</i> ] [ <code>-k</code> <i>k1</i> ] [ <code>-r</code> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>Perform one of two conic projections geodesics. Convert geodetic coordinates to either Lambert conformal conic or Albers equal area coordinates. The standard latitudes <i>lat1</i> and <i>lat2</i> are specified by that the <code>-c</code> option (for Lambert conformal conic) or the <code>-a</code> option (for Albers equal area). At least one of these options must be given (the last one given is used). Specify <i>lat1</i> = <i>lat2</i>, to obtain the case with a single standard parallel. The central meridian is given by <i>lon0</i>. The longitude of origin is given by the latitude of minimum (azimuthal) scale for Lambert conformal conic (Albers equal area). The (azimuthal) scale on the standard parallels is <i>k1</i>. </p>
<p> Geodetic coordinates are provided on standard input as a set of lines containing (blank separated) <i>latitude</i> and <i>longitude</i> (decimal degrees or degrees, minutes, seconds). For each set of geodetic coordinates, the corresponding projected easting, <i>x</i>, and northing, <i>y</i>, (meters) are printed on standard output together with the meridian convergence <i>gamma</i> (degrees) and (azimuthal) scale <i>k</i>. For Albers equal area, the radial scale is 1/<i>k</i>. The meridian convergence is the bearing of the <i>y</i> axis measured clockwise from true north. </p>
<p> Special cases of the Lambert conformal projection are the Mercator projection (the standard latitudes equal and opposite) and the polar stereographic projection (both standard latitudes correspond to the same pole). Special cases of the Albers equal area projection are the cylindrical equal area projection (the standard latitudes equal and opposite), the Lambert azimuthal equal area projection (both standard latitude corresponds to the same pole), and the Lambert equal area conic projection (one standard parallel is at a pole).</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>use the Lambert conformal conic projection with standard parallels <i>lat1</i> and <i>lat2</i>.</p>
<dt><code>-a</code></p>
<dd>use the Albers equal area projection with standard parallels <i>lat1</i> and <i>lat2</i>.</p>
<dt><code>-l</code></p>
<dd>specify the longitude of origin <i>lon0</i> (degrees, default 0).</p>
<dt><code>-k</code></p>
<dd>specify the (azimuthal) scale <i>k1</i> on the standard parallels (default 1).</p>
<dt><code>-r</code></p>
<dd>perform the reverse projection. <i>x</i> and <i>y</i> are given on standard input and each line of standard output gives <i>latitude</i>, <i>longitude</i>, <i>gamma</i>, and <i>k</i>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 6). <i>prec</i> is the number of digits after the decimal point for lengths (in meters). For latitudes and longitudes (in degrees), the number of digits after the decimal point is <i>prec</i> + 5. For the convergence (in degrees) and scale, the number of digits after the decimal point is <i>prec</i> + 6.</p>
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
<pre> echo 39.95N 75.17W | ConicProj -c 40d58 39d56 -l 77d45W
 =&gt; 220445 -52372 1.67 1.0
 echo 220445 -52372 | ConicProj -c 40d58 39d56 -l 77d45W -r
 =&gt; 39.95 -75.17 1.67 1.0</pre>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>ConicProj</code> to return an exit code of 1. However, an error does not cause <code>ConicProj</code> to terminate; following lines will be converted.</p>
<h2>Author</h2>
<p><code>ConicProj</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>ConicProj</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in version 1.9.</p>
