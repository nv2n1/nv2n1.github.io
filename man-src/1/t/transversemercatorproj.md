---
title: "transversemercatorproj(1)"
name: "transversemercatorproj"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transversemercatorproj/"
description: "TransverseMercatorProj — perform transverse Mercator projection"
---

<p>TransverseMercatorProj &#8212; perform transverse Mercator projection </p>
<h2>Synopsis</h2>
<p><code>TransverseMercatorProj</code> [ <code>-s</code> | <code>-t</code> ] [ <code>-l</code> <i>lon0</i> ] [ <code>-k</code> <i>k0</i> ] [ <code>-r</code> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>Perform the transverse Mercator projections. Convert geodetic coordinates to transverse Mercator coordinates. The central meridian is given by <i>lon0</i>. The longitude of origin is the equator. The scale on the central meridian is <i>k0</i>. By default an implementation of the exact transverse Mercator projection is used. </p>
<p> Geodetic coordinates are provided on standard input as a set of lines containing (blank separated) <i>latitude</i> and <i>longitude</i> (decimal degrees or degrees, minutes, seconds). For each set of geodetic coordinates, the corresponding projected easting, <i>x</i>, and northing, <i>y</i>, (meters) are printed on standard output together with the meridian convergence <i>gamma</i> (degrees) and scale <i>k</i>. The meridian convergence is the bearing of the <i>y</i> axis measured clockwise from true north.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>use the sixth-order Krueger series approximation to the transverse Mercator projection instead of the exact projection.</p>
<dt><code>-t</code></p>
<dd>use the exact algorithm with the &#8220;<font SIZE="-1">EXTENDED DOMAIN&#8221;</font>.</p>
<dt><code>-l</code></p>
<dd>specify the longitude of origin <i>lon0</i> (degrees, default 0).</p>
<dt><code>-k</code></p>
<dd>specify the scale <i>k0</i> on the central meridian (default 0.9996).</p>
<dt><code>-r</code></p>
<dd>perform the reverse projection. <i>x</i> and <i>y</i> are given on standard input and each line of standard output gives <i>latitude</i>, <i>longitude</i>, <i>gamma</i>, and <i>k</i>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563. If the exact algorithm is used, <i>f</i> must be positive.</p>
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
<h2>Extended Domain</h2>
<p>The exact transverse Mercator projection has a <i>branch point</i> on the equator at longitudes (relative to <i>lon0</i>) of +/- (1 &#8211; <i>e</i>) 90, where <i>e</i> is the eccentricity of the ellipsoid. The standard convention for handling this branch point is to map positive (negative) latitudes into positive (negative) northings <i>y</i>; i.e., a branch cut is placed on the equator. With the <i>extended</i> domain, the northern sheet of the projection is extended into the south hemisphere by pushing the branch cut south from the branch points. See the reference below for details.</p>
<h2>Examples</h2>
<pre> echo 0 90 | TransverseMercatorProj
 =&gt; 25953592.84 9997964.94 90 18.40
 echo 260e5 100e5 | TransverseMercatorProj -r
 =&gt; -0.02 90.00 90.01 18.48</pre>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>TransverseMercatorProj</code> to return an exit code of 1. However, an error does not cause <code>TransverseMercatorProj</code> to terminate; following lines will be converted.</p>
<h2>Author</h2>
<p><code>TransverseMercatorProj</code> was written by Charles Karney.</p>
<h2>See Also</h2>
<p>The algorithms for the transverse Mercator projection are described in C. F. F. Karney, <i>Transverse Mercator with an accuracy of a few nanometers</i>, J. Geodesy <code><a href="/docs/linux/man/8-85/">85</a></code>(8), 475-485 (Aug. 2011); <font SIZE="-1">DOI </font>&lt;<a rel="nofollow" href="https://dx.doi.org/10.1007/s00190-011-0445-3">https://dx.doi.org/10.1007/s00190-011-0445-3</a>&gt;; preprint &lt;<a rel="nofollow" href="http://arxiv.org/abs/1002.1417">http://arxiv.org/abs/1002.1417</a>&gt;. The explanation of the extended domain of the projection with the <code>-t</code> option is given in Section 5 of this paper.</p>
<h2>History</h2>
<p><code>TransverseMercatorProj</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-01. Prior to version 1.9 it was called TransverseMercatorTest (and its interface was slightly different).</p>
