---
title: "cartconvert(1)"
name: "cartconvert"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cartconvert/"
description: "CartConvert — convert geodetic coordinates to geocentric or local cartesian"
---

<p>CartConvert &#8212; convert geodetic coordinates to geocentric or local cartesian </p>
<h2>Synopsis</h2>
<p><code>CartConvert</code> [ <code>-r</code> ] [ <code>-l</code> <i>lat0</i> <i>lon0</i> <i>h0</i> ] [ <code>-e</code> <i>a</i> <i>f</i> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p>Convert geodetic coordinates to either geocentric or local cartesian coordinates. Geocentric coordinates have the origin at the center of the earth, with the <i>z</i> axis going thru the north pole, and the <i>x</i> axis thru <i>latitude</i> = 0, <i>longitude</i> = 0. By default, the conversion is to geocentric coordinates. Specifying <code>-l</code> <i>lat0</i> <i>lon0</i> <i>h0</i> causes a local coordinate system to be used with the origin at <i>latitude</i> = <i>lat0</i>, <i>longitude</i> = <i>lon0</i>, <i>height</i> = <i>h0</i>, <i>z</i> normal to the ellipsoid and <i>y</i> due north. </p>
<p> Geodetic coordinates are provided on standard input as a set of lines containing (blank separated) <i>latitude</i>, <i>longitude</i> (decimal degrees or degrees, minutes and seconds), and <i>height</i> above the ellipsoid (meters). For each set of geodetic coordinates, the corresponding cartesian coordinates <i>x</i>, <i>y</i>, <i>z</i> (meters) are printed on standard output.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code></p>
<dd>perform the reverse projection. <i>x</i>, <i>y</i>, <i>z</i> are given on standard input and each line of standard output gives <i>latitude</i>, <i>longitude</i>, <i>height</i>.</p>
<dt><code>-e</code></p>
<dd>specify the ellipsoid via <i>a</i> <i>f</i>; the equatorial radius is <i>a</i> and the flattening is <i>f</i>. Setting <i>f</i> = 0 results in a sphere. Specify <i>f</i> &lt; 0 for a prolate ellipsoid. A simple fraction, e.g., 1/297, is allowed for <i>f</i>. (Also, if <i>f</i> &gt; 1, the flattening is set to 1/<i>f</i>.) By default, the <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
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
<pre> echo 33.3 44.4 6000 | CartConvert
 =&gt; 3816209.60 3737108.55 3485109.57
 echo 33.3 44.4 6000 | CartConvert -l 33 44 20
 =&gt; 37288.97 33374.29 5783.64
 echo 30000 30000 0 | CartConvert -r
 =&gt; 6.483 45 -6335709.73</pre>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>CartConvert</code> to return an exit code of 1. However, an error does not cause <code>CartConvert</code> to terminate; following lines will be converted.</p>
<h2>See Also</h2>
<p>The algorithm for converting geocentric to geodetic coordinates is given in Appendix B of C. F. F. Karney, <i>Geodesics on an ellipsoid of revolution</i>, Feb. 2011; preprint &lt;<a rel="nofollow" href="http://arxiv.org/abs/1102.1215">http://arxiv.org/abs/1102.1215</a>&gt;.</p>
<h2>Author</h2>
<p><code>CartConvert</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>CartConvert</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-02. Prior to 2009-03 it was called ECEFConvert.</p>
