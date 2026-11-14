---
title: "geoconvert(1)"
name: "geoconvert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoconvert/"
description: "GeoConvert — convert geographic coordinates"
---

<p>GeoConvert &#8212; convert geographic coordinates </p>
<h2>Synopsis</h2>
<p><code>GeoConvert</code> [ <code>-g</code> | <code>-d</code> | <code>-:</code> | <code>-u</code> | <code>-m</code> | <code>-c</code> ] [ <code>-p</code> <i>prec</i> ] [ <code>-z</code> <i>zone</i> | <code>-s</code> | <code>-t</code> ] [ <code>-n</code> ] [ <code>-w</code> ] [ <code>-l</code> | <code>-a</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p><code>GeoConvert</code> reads from standard input interpreting each line as a geographic coordinate and prints the coordinate in the format specified by the options on standard output. The input is interpreted in one of three different ways depending on how many space or comma delimited tokens there are on the line. The options <code>-g</code>, <code>-d</code>, <code>-u</code>, and <code>-m</code> govern the format of output. In all cases, the <font SIZE="-1">WGS84</font> model of the earth is used (<i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563).</p>
<dl>
<dt><code>geographic</code></p>
<dd>2 tokens (output options <code>-g</code>, <code>-d</code>, or <code>-:</code>) given as <i>latitude</i> <i>longitude</i> using decimal degrees or degrees minutes seconds. d, &#8216;, and &quot; are used to denote degrees, minutes, and seconds, with the least significant designator optional. (See &#8220;<font SIZE="-1">QUOTING&#8221;</font> for how to quote the characters &#8216; and &#8220; when entering coordinates on the command line.) Various unicode characters (encoded with <font SIZE="-1">UTF-8</font>) may also be used to denote degrees, minutes, and seconds, e.g., the degree, prime, and double prime symbols; in addition two single quotes can be used to represent &#8221;. Alternatively, : (colon) may be used to separate the various components. Latitude is given first (unless the <code>-w</code> option is given); however, on input, either may be given first by appending or prepending <i>N</i> or <i>S</i> to the latitude and <i>E</i> or <i>W</i> to the longitude. For example, the following are all equivalent </p>
<pre> 33.3 44.4
 E44.4 N33.3
 33d18'N 44d24'E
 44d24 33d18N
 33:18 44:24</pre>
<p>It is also possible to carry out addition or subtraction operations in geographic coordinates. For example the point 15&quot; east of 39N 70W is </p>
<pre> 39N 70W+0:0:15E</pre>
<dt><font SIZE="-1"><code>UTM/UPS</code></font></p>
<dd>3 tokens (output option <code>-u</code>) given as <i>zone</i>+<i>hemisphere</i> <i>easting</i> <i>northing</i> or <i>easting</i> <i>northing</i> <i>zone</i>+<i>hemisphere</i>, where <i>hemisphere</i> is either <i>n</i> (or <i>north</i>) or <i>s</i> (or <i>south</i>). The <i>zone</i> is absent for a <font SIZE="-1">UPS</font> specification. For example, </p>
<pre> 38n 444140.54 3684706.36
 444140.54 3684706.36 38n
 s 2173854.98 2985980.58
 2173854.98 2985980.58 s</pre>
<dt><font SIZE="-1"><code>MRGS</code></font></p>
<dd>1 token (output option <code>-m</code>) is used to specify the center of an <font SIZE="-1">MGRS</font> grid square. For example, </p>
<pre> 38SMB4484
 38SMB44140847064</pre>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-g</code></p>
<dd>output latitude and longitude using decimal degrees. Default output mode.</p>
<dt><code>-d</code></p>
<dd>output latitude and longitude using degrees, minutes, and seconds (<font SIZE="-1">DMS</font>).</p>
<dt><code>-:</code></p>
<dd>like <code>-d</code>, except use : as a separator instead of the d, &#8216;, and &quot; delimiters.</p>
<dt><code>-u</code></p>
<dd>output <font SIZE="-1">UTM</font> or <font SIZE="-1">UPS.</font></p>
<dt><code>-m</code></p>
<dd>output <font SIZE="-1">MGRS.</font></p>
<dt><code>-c</code></p>
<dd>output meridian convergence and scale for the corresponding <font SIZE="-1">UTM</font> or <font SIZE="-1">UPS</font> projection. Convergence is the bearing of grid north given as degrees clockwise from true north.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 0); <i>prec</i> is the precision relative to 1 m. See &#8220;<font SIZE="-1">PRECISION&#8221;</font>.</p>
<dt><code>-z</code></p>
<dd>set the zone to <i>zone</i> for output. Use either 0 &lt; <i>zone</i> &lt;= 60 for a <font SIZE="-1">UTM</font> zone or <i>zone</i> = 0 for <font SIZE="-1">UPS. </font> Alternatively use a <i>zone</i>+<i>hemisphere</i> designation, e.g., 38n. See &#8220;<font SIZE="-1">ZONE&#8221;</font>.</p>
<dt><code>-s</code></p>
<dd>use the standard <font SIZE="-1">UPS</font> and <font SIZE="-1">UTM</font> zones.</p>
<dt><code>-t</code></p>
<dd>similar to <code>-s</code> but forces <font SIZE="-1">UPS</font> regions to the closest <font SIZE="-1">UTM</font> zone.</p>
<dt><code>-n</code></p>
<dd>on input, <font SIZE="-1">MGRS</font> coordinates refer to the south-west corner of the <font SIZE="-1">MGRS</font> square instead of the center; see &#8220;<font SIZE="-1">MGRS&#8221;</font>.</p>
<dt><code>-w</code></p>
<dd>on input and output, longitude precedes latitude (except that on input this can be overridden by a hemisphere designator, <i>N</i>, <i>S</i>, <i>E</i>, <i>W</i>).</p>
<dt><code>-l</code></p>
<dd>on output, <font SIZE="-1">UTM/UPS</font> uses the long forms <i>north</i> and <i>south</i> to designate the hemisphere instead of <i>n</i> or <i>s</i>.</p>
<dt><code>-a</code></p>
<dd>on output, <font SIZE="-1">UTM/UPS</font> uses the abbreviations <i>n</i> and <i>s</i> to designate the hemisphere instead of <i>north</i> or <i>south</i>; this is the default representation.</p>
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
<h2>Precision</h2>
<p><i>prec</i> gives precision of the output with <i>prec</i> = 0 giving 1 m precision, <i>prec</i> = 3 giving 1 mm precision, etc. <i>prec</i> is the number of digits after the decimal point for <font SIZE="-1">UTM/UPS. </font> The number of digits per coordinate for <font SIZE="-1">MGRS</font> is 5 + <i>prec</i>. For decimal degrees, the number of digits after the decimal point is 5 + <i>prec</i>. For <font SIZE="-1">DMS </font>(degree, minute, seconds) output, the number of digits after the decimal point in the seconds components is 1 + <i>prec</i>; if this is negative then use minutes (<i>prec</i> = -2 or -3) or degrees (<i>prec</i> &lt;= -4) as the least significant component. Print convergence, resp. scale, with 5 + <i>prec</i>, resp. 7 + <i>prec</i>, digits after the decimal point. The minimum value of <i>prec</i> is -5 and the maximum is 9 for <font SIZE="-1">UTM/UPS, 9</font> for decimal degrees, 10 for <font SIZE="-1">DMS, 6</font> for <font SIZE="-1">MGRS,</font> and 8 for convergence and scale.</p>
<h2>Mgrs</h2>
<p><font SIZE="-1">MGRS</font> coordinates represent a square patch of the earth, thus <tt>&quot;38SMB4488&quot;</tt> is in zone <tt>&quot;38n&quot;</tt> with 444km &lt;= <i>easting</i> &lt; 445km and 3688km &lt;= <i>northing</i> &lt; 3689km. Consistent with this representation, coordinates are <i>truncated</i> (instead of <i>rounded</i>) to the requested precision. Similarly, on input an <font SIZE="-1">MGRS</font> coordinate represents the <i>center</i> of the square (<tt>&quot;38n 444500 3688500&quot;</tt> in the example above). However, if the <code>-n</code> option is given then the south-west corner of the square is returned instead (<tt>&quot;38n 444000 3688000&quot;</tt> in the example above).</p>
<h2>Zone</h2>
<p>If the input is <code>geographic</code>, <code>GeoConvert</code> uses the standard rules of selecting <font SIZE="-1">UTM</font> vs <font SIZE="-1">UPS</font> and for assigning the <font SIZE="-1">UTM</font> zone (with the Norway and Svalbard exceptions). If the input is <font SIZE="-1"><code>UTM/UPS</code></font> or <font SIZE="-1"><code>MGRS</code></font>, then the choice between <font SIZE="-1">UTM</font> and <font SIZE="-1">UPS</font> and the <font SIZE="-1">UTM</font> zone mirrors the input. The <code>-z</code> <i>zone</i>, <code>-s</code>, and <code>-t</code> options allow these rules to be overridden with <i>zone</i> = 0 being used to indicate <font SIZE="-1">UPS. </font> For example, the point </p>
<pre> 79.9S 6.1E</pre>
<p>corresponds to possible <font SIZE="-1">MGRS</font> coordinates </p>
<pre> 32CMS4324728161 (standard UTM zone = 32)
 31CEM6066227959 (neighboring UTM zone = 31)
 BBZ1945517770 (neighboring UPS zone)</pre>
<p>then </p>
<pre> echo 79.9S 6.1E | GeoConvert -p -3 -m =&gt; 32CMS4328
 echo 31CEM6066227959 | GeoConvert -p -3 -m =&gt; 31CEM6027
 echo 31CEM6066227959 | GeoConvert -p -3 -m -s =&gt; 32CMS4328
 echo 31CEM6066227959 | GeoConvert -p -3 -m -z 0 =&gt; BBZ1917</pre>
<p>Is <i>zone</i> is specified with a hemisphere, then this is honored when printing <font SIZE="-1">UTM</font> coordinates: </p>
<pre> echo -1 3 | GeoConvert -u =&gt; 31s 500000 9889470
 echo -1 3 | GeoConvert -u -z 31 =&gt; 31s 500000 9889470
 echo -1 3 | GeoConvert -u -z 31s =&gt; 31s 500000 9889470
 echo -1 3 | GeoConvert -u -z 31n =&gt; 31n 500000 -110530</pre>
<p><font SIZE="-1"><code>NOTE</code></font>: the letter in the zone specification for <font SIZE="-1">UTM</font> is a hemisphere designator <i>n</i> or <i>s</i> and <i>not</i> an <font SIZE="-1">MGRS</font> latitude band letter. Convert the <font SIZE="-1">MGRS</font> latitude band letter to a hemisphere as follows: replace <i>C</i> thru <i>M</i> by <i>s</i> (or <i>south</i>); replace <i>N</i> thru <i>X</i> by <i>n</i> (or <i>north</i>).</p>
<h2>Quoting</h2>
<p>Unfortunately the characters &#8216; and &#8220; have special meanings in many shells and have to be entered with care. However note (1) that the trailing designator is optional and that (2) you can use colons as a separator character. Thus 10d20&#8217; can be entered as 10d20 or 10:20 and 10d20&#8217;30&#8221; can be entered as 10:20:30.</p>
<dl>
<dt>Unix shells (sh, bash, tsch)</p>
<dd>The characters &#8216; and &#8220; can be quoted by preceding them with a \ (backslash); or you can quote a string containing &#8216; with a pair of &#8221;s. The two alternatives are illustrated by </p>
<pre> echo 10d20\'30\&quot; &quot;20d30'40&quot; | GeoConvert -d -p -1
 =&gt; 10d20'30&quot;N 020d30'40&quot;E</pre>
<p>Quoting of command line arguments is similar </p>
<pre> GeoConvert -d -p -1 --input-string &quot;10d20'30\&quot; 20d30'40&quot;
 =&gt; 10d20'30&quot;N 020d30'40&quot;E</pre>
<dt>Windows command shell (cmd)</p>
<dd>The &#8216; character needs no quoting; the &quot; character can either be quoted by a ^ or can be represented by typing &#8216; twice. (This quoting is usually unnecessary because the trailing designator can be omitted.) Thus </p>
<pre> echo 10d20'30'' 20d30'40 | GeoConvert -d -p -1
 =&gt; 10d20'30&quot;N 020d30'40&quot;E</pre>
<p>Use \ to quote the &quot; character in a command line argument </p>
<pre> GeoConvert -d -p -1 --input-string &quot;10d20'30\&quot; 20d30'40&quot;
 =&gt; 10d20'30&quot;N 020d30'40&quot;E</pre>
<dt>Input from a file</p>
<dd>No quoting need be done if the input from a file. Thus each line of the file <tt>&quot;input.txt&quot;</tt> should just contain the plain coordinates. </p>
<pre> GeoConvert -d -p -1 &lt; input.txt</pre>
</dl>
<h2>Examples</h2>
<pre> echo 38SMB4488 | GeoConvert =&gt; 33.33424 44.40363
 echo 38SMB4488 | GeoConvert -: -p 1 =&gt; 33:20:03.25N 044:2413.06E
 echo 38SMB4488 | GeoConvert -u =&gt; 38n 444500 3688500
 echo E44d24 N33d20 | GeoConvert -m -p -3 =&gt; 38SMB4488</pre>
<p>GeoConvert can be used to do simple arithmetic using degree, minutes, and seconds. For example, sometimes data is tiled in 15 second squares tagged by the <font SIZE="-1">DMS</font> representation of the <font SIZE="-1">SW</font> corner. The tags of the tile at 38:59:45N 077:02:00W and its 8 neighbors are then given by </p>
<pre> t=0:0:15
 for y in -$t +0 +$t; do
 for x in -$t +0 +$t; do
 echo 38:59:45N$y 077:02:00W$x
 done
 done | GeoConvert -: -p -1 | tr -d ': '
 =&gt;
 385930N0770215W
 385930N0770200W
 385930N0770145W
 385945N0770215W
 385945N0770200W
 385945N0770145W
 390000N0770215W
 390000N0770200W
 390000N0770145W</pre>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>GeoConvert</code> to return an exit code of 1. However, an error does not cause <code>GeoConvert</code> to terminate; following lines will be converted.</p>
<h2>Abbreviations</h2>
<dl>
<dt><font SIZE="-1"><code>UTM</code></font></p>
<dd>Universal Transverse Mercator, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system">https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system</a>&gt;.</p>
<dt><font SIZE="-1"><code>UPS</code></font></p>
<dd>Universal Polar Stereographic, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Universal_Polar_Stereographic">https://en.wikipedia.org/wiki/Universal_Polar_Stereographic</a>&gt;.</p>
<dt><font SIZE="-1"><code>MGRS</code></font></p>
<dd>Military Grid Reference System, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Military_grid_reference_system">https://en.wikipedia.org/wiki/Military_grid_reference_system</a>&gt;.</p>
<dt><font SIZE="-1"><code>WGS84</code></font></p>
<dd>World Geodetic System 1984, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/WGS84">https://en.wikipedia.org/wiki/WGS84</a>&gt;.</dl>
<h2>See Also</h2>
<p>An online version of this utility is availbable at &lt;<a rel="nofollow" href="http://geographiclib.sourceforge.net/cgi-bin/GeoConvert">http://geographiclib.sourceforge.net/cgi-bin/GeoConvert</a>&gt;. </p>
<p> The algorithms for the transverse Mercator projection are described in C. F. F. Karney, <i>Transverse Mercator with an accuracy of a few nanometers</i>, J. Geodesy <code><a href="/docs/linux/man/8-85/">85</a></code>(8), 475-485 (Aug. 2011); <font SIZE="-1">DOI </font>&lt;<a rel="nofollow" href="https://dx.doi.org/10.1007/s00190-011-0445-3">https://dx.doi.org/10.1007/s00190-011-0445-3</a>&gt;; preprint &lt;<a rel="nofollow" href="http://arxiv.org/abs/1002.1417">http://arxiv.org/abs/1002.1417</a>&gt;.</p>
<h2>Author</h2>
<p><code>GeoConvert</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>GeoConvert</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-01.</p>
