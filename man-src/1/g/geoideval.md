---
title: "geoideval(1)"
name: "geoideval"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoideval/"
description: "GeoidEval — look up geoid heights"
---

<p>GeoidEval &#8212; look up geoid heights </p>
<h2>Synopsis</h2>
<p><code>GeoidEval</code> [ <code>-n</code> <i>name</i> ] [ <code>-d</code> <i>dir</i> ] [ <code>-l</code> ] [ <code>-a</code> | <code>-c</code> <i>south</i> <i>west</i> <i>north</i> <i>east</i> ] [ <code>-g</code> ] [ <code>-z</code> <i>zone</i> ] [ <code>&#8211;msltohae</code> ] [ <code>&#8211;haetomsl</code> ] [ <code>-v</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p><code>GeoidEval</code> reads in positions on standard input and prints out the corresponding heights of the geoid above the <font SIZE="-1">WGS84</font> ellipsoid on standard output. </p>
<p> Positions are given as latitude and longitude, <font SIZE="-1">UTM/UPS,</font> or <font SIZE="-1">MGRS,</font> in any of the formats accepted by <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1). (<font SIZE="-1">MGRS</font> coordinates signify the <i>center</i> of the corresponding <font SIZE="-1">MGRS</font> square.) If the <code>-z</code> option is specified then the specified zone is prepended to each line of input (which must be in <font SIZE="-1">UTM/UPS</font> coordinates). This allows a file with <font SIZE="-1">UTM</font> eastings and northings in a single zone to be used as standard input. </p>
<p> More accurate results for the geoid height are provided by <i><a href="/docs/linux/man/1-gravity/">Gravity</a></i>(1). This utility can also compute the direction of gravity accurately. </p>
<p> The height of the geoid above the ellipsoid, <i>N</i>, is sometimes called the geoid undulation. It can be used to convert a height above the ellipsoid, <i>h</i>, to the corresponding height above the geoid (the orthometric height, roughly the height above mean sea level), <i>H</i>, using the relations </p>
<dl>
<dd><i>h</i> = <i>N</i> + <i>H</i>, &nbsp;<wbr>&nbsp;<wbr><i>H</i> = &#8211;<i>N</i> + <i>h</i>.</dl>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>use geoid <i>name</i> instead of the default <tt>&quot;egm96-5&quot;</tt>. See &#8220;<font SIZE="-1">GEOIDS&#8221;</font>.</p>
<dt><code>-d</code></p>
<dd>read geoid data from <i>dir</i> instead of the default. See &#8220;<font SIZE="-1">GEOIDS&#8221;</font>.</p>
<dt><code>-l</code></p>
<dd>use bilinear interpolation instead of cubic. See &#8220;<font SIZE="-1">INTERPOLATION&#8221;</font>.</p>
<dt><code>-a</code></p>
<dd>cache the entire data set in memory. See &#8220;<font SIZE="-1">CACHE&#8221;</font>.</p>
<dt><code>-c</code></p>
<dd>cache the data bounded by <i>south</i> <i>west</i> <i>north</i> <i>east</i> in memory. See &#8220;<font SIZE="-1">CACHE&#8221;</font>.</p>
<dt><code>-g</code></p>
<dd>print the northerly and easterly gradients after the geoid height (i.e., the rate at which the geoid height changes per unit distance along the <font SIZE="-1">WGS84</font> ellipsoid in the specified directions). As a result of the way that the geoid data is stored, the calculation of gradients can result in large quantization errors. This is particularly acute at high latitudes and for the easterly gradient. For this reason, the use of this option is <font SIZE="-1"><code>DEPRECATED</code></font>.</p>
<dt><code>-z</code></p>
<dd>prefix each line of input by <i>zone</i>, e.g., <tt>&quot;38n&quot;</tt>. This should be used when the input consists of <font SIZE="-1">UTM/UPS</font> eastings and northings.</p>
<dt><code>&#8211;msltohae</code></p>
<dd>standard input should include a final token on each line which is treated as a height (in meters) above the geoid and the output echoes the input line with the height converted to height above ellipsoid (<font SIZE="-1">HAE</font>). If <code>-z</code> <i>zone</i> is specified then the <i>third</i> token is treated as the height; this makes it possible to convert <font SIZE="-1">LIDAR</font> data where each line consists of: easting northing height intensity.</p>
<dt><code>&#8211;haetomsl</code></p>
<dd>this is similar to <code>&#8211;msltohae</code> except that the height token is treated as a height (in meters) above the ellipsoid and the output echoes the input line with the height converted to height above the geoid (<font SIZE="-1">MSL</font>).</p>
<dt><code>-v</code></p>
<dd>print information about the geoid on standard error before processing the input.</p>
<dt><code>&#8211;comment-delimiter</code></p>
<dd>set the comment delimiter to <i>commentdelim</i> (e.g., &#8220;#&#8221; or &#8220;//&#8221;). If set, the input lines will be scanned for this delimiter and, if found, the delimiter and the rest of the line will be removed prior to processing and subsequently appended to the output line (separated by a space).</p>
<dt><code>&#8211;version</code></p>
<dd>print version and exit.</p>
<dt><code>-h</code></p>
<dd>print usage, the default geoid path and name, and exit.</p>
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
<h2>Geoids</h2>
<p><code>GeoidEval</code> computes geoid heights by interpolating on the data in a regularly spaced table (see &#8220;<font SIZE="-1">INTERPOLATION&#8221;</font>). The following geoid tables are available (however, some may not be installed): </p>
<pre> bilinear error cubic error
 name geoid grid max rms max rms
 egm84-30 EGM84 30' 1.546 m 70 mm 0.274 m 14 mm
 egm84-15 EGM84 15' 0.413 m 18 mm 0.021 m 1.2 mm
 egm96-15 EGM96 15' 1.152 m 40 mm 0.169 m 7.0 mm
 egm96-5 EGM96 5' 0.140 m 4.6 mm .0032 m 0.7 mm
 egm2008-5 EGM2008 5' 0.478 m 12 mm 0.294 m 4.5 mm
 egm2008-2_5 EGM2008 2.5' 0.135 m 3.2 mm 0.031 m 0.8 mm
 egm2008-1 EGM2008 1' 0.025 m 0.8 mm .0022 m 0.7 mm</pre>
<p>By default, the <tt>&quot;egm96-5&quot;</tt> geoid is used. This may changed by setting the environment variable <tt>&quot;GEOGRAPHICLIB_GEOID_NAME&quot;</tt> or with the <code>-n</code> option. The errors listed here are estimates of the quantization and interpolation errors in the reported heights compared to the specified geoid. </p>
<p> The geoid data will be loaded from a directory specified at compile time. This may changed by setting the environment variables <tt>&quot;GEOGRAPHICLIB_GEOID_PATH&quot;</tt> or <tt>&quot;GEOGRAPHICLIB_DATA&quot;</tt>, or with the <code>-d</code> option. The <code>-h</code> option prints the default geoid path and name. Use the <code>-v</code> option to ascertain the full path name of the data file. </p>
<p> Instructions for downloading and installing geoid data are available at &lt;<a rel="nofollow" href="http://geographiclib.sf.net/html/geoid.html#geoidinst">http://geographiclib.sf.net/html/geoid.html#geoidinst</a>&gt;. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: all the geoids above apply to the <font SIZE="-1">WGS84</font> ellipsoid (<i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563) only.</p>
<h2>Interpolation</h2>
<p>Cubic interpolation is used to compute the geoid height unless <code>-l</code> is specified in which case bilinear interpolation is used. The cubic interpolation is based on a least-squares fit of a cubic polynomial to a 12-point stencil </p>
<pre> . 1 1 .
 1 2 2 1
 1 2 2 1
 . 1 1 .</pre>
<p>The cubic is constrained to be independent of longitude when evaluating the height at one of the poles. Cubic interpolation is considerably more accurate than bilinear; however it results in small discontinuities in the returned height on cell boundaries.</p>
<h2>Cache</h2>
<p>By default, the data file is randomly read to compute the geoid heights at the input positions. Usually this is sufficient for interactive use. If many heights are to be computed, use <code>-c</code> <i>south</i> <i>west</i> <i>north</i> <i>east</i> to notify <code>GeoidEval</code> to read a rectangle of data into memory; heights within the this rectangle can then be computed without any disk access. If <code>-a</code> is specified all the geoid data is read; in the case of <tt>&quot;egm2008-1&quot;</tt>, this requires about 0.5 <font SIZE="-1">GB</font> of <font SIZE="-1">RAM. </font> The evaluation of heights outside the cached area causes the necessary data to be read from disk. Use the <code>-v</code> option to verify the size of the cache. </p>
<p> Regardless of whether any cache is requested (with the <code>-a</code> or <code>-c</code> options), the data for the last grid cell in cached. This allows the geoid height along a continuous path to be returned with little disk overhead.</p>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_GEOID_NAME</code></font></p>
<dd>Override the compile-time default geoid name of <tt>&quot;egm96-5&quot;</tt>. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_GEOID_NAME</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-n</code> <i>name</i> option is used, then <i>name</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_GEOID_PATH</code></font></p>
<dd>Override the compile-time default geoid path. This is typically <tt>&quot;/usr/local/share/GeographicLib/geoids&quot;</tt> on Unix-like systems and <tt>&quot;C:/ProgramData/GeographicLib/geoids&quot;</tt> on Windows systems. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_GEOID_PATH</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-d</code> <i>dir</i> option is used, then <i>dir</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font></p>
<dd>Another way of overriding the compile-time default geoid path. If it is set (and if <font SIZE="-1"><code>GEOGRAPHICLIB_GEOID_PATH</code></font> is not set), then $<font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font>/geoids is used.</dl>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>GeoidEval</code> to return an exit code of 1. However, an error does not cause <code>GeoidEval</code> to terminate; following lines will be converted.</p>
<h2>Abbreviations</h2>
<p>The geoid is usually approximated by an &#8220;earth gravity model&#8221;. The models published by the <font SIZE="-1">NGA</font> are:</p>
<dl>
<dt><font SIZE="-1"><code>EGM84</code></font></p>
<dd>An earth gravity model published by the <font SIZE="-1">NGA</font> in 1984, &lt;<a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/wgs84_180/wgs84_180.html">http://earth-info.nga.mil/GandG/wgs84/gravitymod/wgs84_180/wgs84_180.html</a>&gt;.</p>
<dt><font SIZE="-1"><code>EGM96</code></font></p>
<dd>An earth gravity model published by the <font SIZE="-1">NGA</font> in 1996, &lt;<a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.html">http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.html</a>&gt;.</p>
<dt><font SIZE="-1"><code>EGM2008</code></font></p>
<dd>An earth gravity model published by the <font SIZE="-1">NGA</font> in 2008, &lt;<a rel="nofollow" href="http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008">http://earth-info.nga.mil/GandG/wgs84/gravitymod/egm2008</a>&gt;.</p>
<dt><font SIZE="-1"><code>WGS84</code></font></p>
<dd>World Geodetic System 1984, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/WGS84">https://en.wikipedia.org/wiki/WGS84</a>&gt;.</p>
<dt><font SIZE="-1"><code>HAE</code></font></p>
<dd>Height above the <font SIZE="-1">WGS84</font> ellipsoid.</p>
<dt><font SIZE="-1"><code>MSL</code></font></p>
<dd>Mean sea level, used as a convenient short hand for the geoid. (However, typically, the geoid differs by a few meters from mean sea level.)</dl>
<h2>Examples</h2>
<p>The height of the <font SIZE="-1">EGM96</font> geoid at Timbuktu </p>
<pre> echo 16:46:33N 3:00:34W | GeoidEval
 =&gt; 28.7068 -0.02e-6 -1.73e-6</pre>
<p>The first number returned is the height of the geoid and the 2nd and 3rd are its slopes in the northerly and easterly directions. </p>
<p> Convert a point in <font SIZE="-1">UTM</font> zone 18n from <font SIZE="-1">MSL</font> to <font SIZE="-1">HAE</font> </p>
<pre> echo 531595 4468135 23 | GeoidEval --msltohae -z 18n
 =&gt; 531595 4468135 -10.842</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1), <i><a href="/docs/linux/man/1-gravity/">Gravity</a></i>(1), <i><a href="/docs/linux/man/8-geographiclib-get-geoids/">geographiclib-get-geoids</a></i>(8). </p>
<p> An online version of this utility is availbable at &lt;<a rel="nofollow" href="http://geographiclib.sourceforge.net/cgi-bin/GeoidEval">http://geographiclib.sourceforge.net/cgi-bin/GeoidEval</a>&gt;.</p>
<h2>Author</h2>
<p><code>GeoidEval</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>GeoidEval</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in 2009-09.</p>
