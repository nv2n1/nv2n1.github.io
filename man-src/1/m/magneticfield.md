---
title: "magneticfield(1)"
name: "magneticfield"
section: "1"
letter: "m"
url: "/docs/linux/man/1-magneticfield/"
description: "MagneticField — compute the earth’s magnetic field"
---

<p>MagneticField &#8212; compute the earth&#8217;s magnetic field </p>
<h2>Synopsis</h2>
<p><code>MagneticField</code> [ <code>-n</code> <i>name</i> ] [ <code>-d</code> <i>dir</i> ] [ <code>-t</code> <i>time</i> | <code>-c</code> <i>time</i> <i>lat</i> <i>h</i> ] [ <code>-r</code> ] [ <code>-T</code> <i>tguard</i> ] [ <code>-H</code> <i>hguard</i> ] [ <code>-p</code> <i>prec</i> ] [ <code>-v</code> ] [ <code>&#8211;comment-delimiter</code> <i>commentdelim</i> ] [ <code>&#8211;version</code> | <code>-h</code> | <code>&#8211;help</code> ] [ <code>&#8211;input-file</code> <i>infile</i> | <code>&#8211;input-string</code> <i>instring</i> ] [ <code>&#8211;line-separator</code> <i>linesep</i> ] [ <code>&#8211;output-file</code> <i>outfile</i> ]</p>
<h2>Description</h2>
<p><code>MagneticField</code> reads in times and positions on standard input and prints out the geomagnetic field on standard output and, optionally, its rate of change. </p>
<p> The input line is of the form <i>time</i> <i>lat</i> <i>lon</i> <i>h</i>. <i>time</i> is a date of the form 2012-07-03, a fractional year such as 2012.5, or the string &#8220;now&#8221;. <i>lat</i> and <i>lon</i> are the latitude and longitude expressed as decimal degrees or degrees, minutes, and seconds; see <i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1) for details. <i>h</i> is the height above the ellipsoid in meters; this is optional and defaults to zero. Alternatively, <i>time</i> can be given on the command line as the argument to the <code>-t</code> option, in which case it should not be included on the input lines. Finally, the magnetic field can be computed at various points on a circle of latitude (constant <i>time</i>, <i>lat</i>, and <i>h</i>) via the <code>-c</code> option; in this case only the longitude should be given on the input lines. </p>
<p> The output consists of the following 7 items: </p>
<pre> the declination (the direction of the horizontal component of
 the magnetic field measured clockwise from north) in degrees,
 the inclination (the direction of the magnetic field measured
 down from the horizontal) in degrees,
 the horizontal field in nanotesla (nT),
 the north component of the field in nT,
 the east component of the field in nT,
 the vertical component of the field in nT (down is positive),
 the total field in nT.</pre>
<p>If the <code>-r</code> option is given, a second line is printed giving the rates of change of these quantities in degrees/yr and nT/yr. </p>
<p> The <font SIZE="-1">WGS84</font> ellipsoid is used, <i>a</i> = 6378137 m, <i>f</i> = 1/298.257223563.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>use magnetic field model <i>name</i> instead of the default <tt>&quot;wmm2015&quot;</tt>. See &#8220;<font SIZE="-1">MODELS&#8221;</font>.</p>
<dt><code>-d</code></p>
<dd>read magnetic models from <i>dir</i> instead of the default. See &#8220;<font SIZE="-1">MODELS&#8221;</font>.</p>
<dt><code>-t</code></p>
<dd>evaluate the field at <i>time</i> instead of reading the time from the input lines.</p>
<dt><code>-c</code></p>
<dd>evaluate the field on a circle of latitude given by <i>time</i>, <i>lat</i>, <i>h</i> instead of reading these quantities from the input lines. In this case, <code>MagneticField</code> can calculate the field considerably more quickly.</p>
<dt><code>-r</code></p>
<dd>toggle whether to report the rates of change of the field.</p>
<dt><code>-T</code></p>
<dd>signal an error if <i>time</i> lies <i>tguard</i> years (default 50 yr) beyond the range for the model.</p>
<dt><code>-H</code></p>
<dd>signal an error if <i>h</i> lies <i>hguard</i> meters (default 500000 m) beyond the range for the model.</p>
<dt><code>-p</code></p>
<dd>set the output precision to <i>prec</i> (default 1). Fields are printed with precision with <i>prec</i> decimal places; angles use <i>prec</i> + 1 places.</p>
<dt><code>-v</code></p>
<dd>print information about the magnetic model on standard error before processing the input.</p>
<dt><code>&#8211;comment-delimiter</code></p>
<dd>set the comment delimiter to <i>commentdelim</i> (e.g., &#8220;#&#8221; or &#8220;//&#8221;). If set, the input lines will be scanned for this delimiter and, if found, the delimiter and the rest of the line will be removed prior to processing and subsequently appended to the output line (separated by a space).</p>
<dt><code>&#8211;version</code></p>
<dd>print version and exit.</p>
<dt><code>-h</code></p>
<dd>print usage, the default magnetic path and name, and exit.</p>
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
<p><code>MagneticField</code> computes the geomagnetic field using one of the following models </p>
<pre> wmm2010, the World Magnetic Model 2010, which approximates the
 main magnetic field for the period 2010-2015. See
 <a rel="nofollow" href="http://ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml">http://ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml</a>
 wmm2015, the World Magnetic Model 2015, which approximates the
 main magnetic field for the period 2015-2020. See
 <a rel="nofollow" href="http://ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml">http://ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml</a>
 igrf11, the International Geomagnetic Reference Field (11th
 generation), which approximates the main magnetic field for
 the period 1900-2015. See
 <a rel="nofollow" href="http://ngdc.noaa.gov/IAGA/vmod/igrf.html">http://ngdc.noaa.gov/IAGA/vmod/igrf.html</a>
 igrf12, the International Geomagnetic Reference Field (12th
 generation), which approximates the main magnetic field for
 the period 1900-2020. See
 <a rel="nofollow" href="http://ngdc.noaa.gov/IAGA/vmod/igrf.html">http://ngdc.noaa.gov/IAGA/vmod/igrf.html</a>
 emm2010, the Enhanced Magnetic Model 2010, which approximates
 the main and crustal magnetic fields for the period 2010-2015.
 See <a rel="nofollow" href="http://ngdc.noaa.gov/geomag/EMM/index.html">http://ngdc.noaa.gov/geomag/EMM/index.html</a>
 emm2015, the Enhanced Magnetic Model 2015, which approximates
 the main and crustal magnetic fields for the period 2000-2020.
 See <a rel="nofollow" href="http://ngdc.noaa.gov/geomag/EMM/index.html">http://ngdc.noaa.gov/geomag/EMM/index.html</a></pre>
<p>These models approximate the magnetic field due to the earth&#8217;s core and (in the case of emm2010) its crust. They neglect magnetic fields due to the ionosphere, the magnetosphere, nearby magnetized materials, electrical machinery, etc. </p>
<p> By default, the <tt>&quot;wmm2015&quot;</tt> magnetic model is used. This may changed by setting the environment variable <tt>&quot;GEOGRAPHICLIB_MAGNETIC_NAME&quot;</tt> or with the <code>-n</code> option. </p>
<p> The magnetic models will be loaded from a directory specified at compile time. This may changed by setting the environment variables <tt>&quot;GEOGRAPHICLIB_MAGNETIC_PATH&quot;</tt> or <tt>&quot;GEOGRAPHICLIB_DATA&quot;</tt>, or with the <code>-d</code> option. The <code>-h</code> option prints the default magnetic path and name. Use the <code>-v</code> option to ascertain the full path name of the data file. </p>
<p> Instructions for downloading and installing magnetic models are available at &lt;<a rel="nofollow" href="http://geographiclib.sf.net/html/magnetic.html#magneticinst">http://geographiclib.sf.net/html/magnetic.html#magneticinst</a>&gt;.</p>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_MAGNETIC_NAME</code></font></p>
<dd>Override the compile-time default magnetic name of <tt>&quot;wmm2015&quot;</tt>. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_MAGNETIC_NAME</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-n</code> <i>name</i> option is used, then <i>name</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_MAGNETIC_PATH</code></font></p>
<dd>Override the compile-time default magnetic path. This is typically <tt>&quot;/usr/local/share/GeographicLib/magnetic&quot;</tt> on Unix-like systems and <tt>&quot;C:/ProgramData/GeographicLib/magnetic&quot;</tt> on Windows systems. The <code>-h</code> option reports the value of <font SIZE="-1"><code>GEOGRAPHICLIB_MAGNETIC_PATH</code></font>, if defined, otherwise it reports the compile-time value. If the <code>-d</code> <i>dir</i> option is used, then <i>dir</i> takes precedence.</p>
<dt><font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font></p>
<dd>Another way of overriding the compile-time default magnetic path. If it is set (and if <font SIZE="-1"><code>GEOGRAPHICLIB_MAGNETIC_PATH</code></font> is not set), then $<font SIZE="-1"><code>GEOGRAPHICLIB_DATA</code></font>/magnetic is used.</dl>
<h2>Errors</h2>
<p>An illegal line of input will print an error message to standard output beginning with <tt>&quot;ERROR:&quot;</tt> and causes <code>MagneticField</code> to return an exit code of 1. However, an error does not cause <code>MagneticField</code> to terminate; following lines will be converted. If <i>time</i> or <i>h</i> are outside the recommended ranges for the model (but inside the ranges increase by <i>tguard</i> and <i>hguard</i>), a warning is printed on standard error and the field (which may be inaccurate) is returned in the normal way.</p>
<h2>Examples</h2>
<p>The magnetic field from <font SIZE="-1">WMM2015</font> in Timbuktu on 2016-01-01 </p>
<pre> echo 2016-01-01 16:46:33N 3:00:34W 300 | MagneticField -r
 =&gt; -2.12 12.15 33871.9 33848.7 -1251.4 7293.9 34648.3
 0.09 -0.08 31.8 33.8 53.7 -41.4 22.3</pre>
<p>The first two numbers returned are the declination and inclination of the field. The second line gives the annual change.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-geoconvert/">GeoConvert</a></i>(1), <i><a href="/docs/linux/man/8-geographiclib-get-magnetic/">geographiclib-get-magnetic</a></i>(8).</p>
<h2>Author</h2>
<p><code>MagneticField</code> was written by Charles Karney.</p>
<h2>History</h2>
<p><code>MagneticField</code> was added to GeographicLib, &lt;<a rel="nofollow" href="http://geographiclib.sf.net">http://geographiclib.sf.net</a>&gt;, in version 1.15.</p>
