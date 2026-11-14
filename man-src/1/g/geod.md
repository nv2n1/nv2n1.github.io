---
title: "geod(1)"
name: "geod"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geod/"
description: "geod – direct geodesic computations invgeod – inverse geodesic computations"
---

<h2>NAME</h2>
<p> geod &#8211; direct geodesic computations<br />
 invgeod &#8211; inverse geodesic computations</p>
<h2>SYNOPSIS</h2>
<p> <code>geod</code> <code>+ellps=&lt;ellipse&gt;</code> [ <code>-afFIlptwW</code> [ <i>args</i> ] ] [ <code>+args</code> ] file[s]<br />
 <code>invgeod</code> <code>+ellps=&lt;ellipse&gt;</code> [ <code>-afFIlptwW</code> [ <i>args</i> ] ] [ <code>+args</code> ] file[s]</p>
<h2>DESCRIPTION</h2>
<p> <i>Geod</i> (direct) and <i>invgeod</i> (inverse) perform geodesic (&#8220;Great Circle&#8221;) computations for determining latitude, longitude and back azimuth of a terminus point given a initial point latitude, longitude, azimuth and distance (direct) or the forward and back azimuths and distance between an initial and terminus point latitudes and longitudes (inverse). </p>
<p> The following runline control parameters can appear in any order:</p>
<dl>
<dt><code>-I</code></p>
<dd> Specifies that the inverse geodesic computation is to be performed. May be used with execution of <code>goed</code> as an alternative to <code>invgeod</code> execution.</p>
<dt><code>-a</code></p>
<dd> Latitude and longitudes of the initial and terminal points, forward and back azimuths and distance are output.</p>
<dt><code>-t</code><i>a</i></p>
<dd> <i>A</i> specifies a character employed as the first character to denote a control line to be passed through without processing.</p>
<dt><code>-le</code></p>
<dd> Gives a listing of all the ellipsoids that may be selected with the <code>+ellps=</code> option.</p>
<dt><code>-lu</code></p>
<dd> Gives a listing of all the units that may be selected with the <code>+units=</code> option.</p>
<dt><code>-[f|F]</code><i> format</i></p>
<dd> <i>Format</i> is a <i>printf</i> format string to control the output form of the geographic coordinate values (<code>f</code>) or distance value (<code>F</code>). The default mode is DMS for geographic coordinates and &quot;%.3f&quot; for distance.</p>
<dt><code>-[w|W]</code><i>n</i></p>
<dd> <i>N</i> is the number of significant fractional digits to employ for seconds output (when the option is not specified, <code>-w3</code> is assumed). When <code>-W</code> is employed the fields will be constant width with leading zeroes.</p>
<dt><code>-p</code></p>
<dd> This option causes the azimuthal values to be output as unsigned DMS numbers between 0 and 360 degrees. Also note -f.</dl>
<p> The <code>+args</code> run-line arguments are associated with geodetic parameters for specifying the ellipsoidal or sphere to use. See <code>proj</code> documentation for full list of these parameters and controls. The options are processed in left to right order from the run line. Reentry of an option is ignored with the first occurrence assumed to be the desired value. </p>
<p> One or more <i>files</i> (processed in left to right order) specify the source of data to be transformed. A &#8211; will specify the location of processing standard input. If no files are specified, the input is assumed to be from <i>stdin.</i> </p>
<p> For direct determinations input data must be in latitude, longitude, azimuth and distance order and output will be latitude, longitude and back azimuth of the terminus point. Latitude, longitude of the initial and terminus point are input for the inverse mode and respective forward and back azimuth from the initial and terminus points are output along with the distance between the points. </p>
<p> Input geographic coordinates (latitude and longitude) and azimuthal data must be in DMS format and input distance data must be in units consistent with the ellipsoid major axis or sphere radius units. Output geographic coordinates will be in DMS (if the <code>-f</code> switch is not employed) to 0.001&quot; with trailing, zero-valued minute-second fields deleted. Output distance data will be in the same units as the ellipsoid or sphere radius. </p>
<p> The Earth&#8217;s ellipsoidal figure may be selected in the same manner as program <code>proj</code> by using <code>+ellps=, +a=, +es=,</code> etc. </p>
<p> <i>Geod</i> may also be used to determine intermediate points along either a geodesic line between two points or along an arc of specified distance from a geographic point. In both cases an initial point must be specified with <code>+lat_1=</code><i>lat</i> and <code>+lon_1=</code><i>lon</i> parameters and either a terminus point <code>+lat_2=</code><i>lat</i> and <code>+lon_2=</code><i>lon</i> or a distance and azimuth from the initial point with <code>+S=</code><i>distance</i> and <code>+A=</code><i>azimuth</i> must be specified. </p>
<p> If points along a geodesic are to be determined then either <code>+n_S=</code><i>integer</i> specifying the number of intermediate points and/or <code>+del_S=</code><i>distance</i> specifying the incremental distance between points must be specified. </p>
<p> To determine points along an arc equidistant from the initial point both <code>+del_A=</code><i>angle</i> and <code>+n_A=</code><i>integer</i> must be specified which determine the respective angular increments and number of points to be determined.</p>
<h2>EXAMPLE</h2>
<p> The following script determines the geodesic azimuths and distance in U.S. stature miles from Boston, MA, to Portland, OR:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>geod&nbsp;<wbr>+ellps=clrk66&nbsp;<wbr>&lt;&lt;EOF -I&nbsp;<wbr>+units=us-mi<br />
&nbsp;<wbr>42d15'N 71d07'W 45d31'N 123d41'W<br />
&nbsp;<wbr>EOF</tt></dl>
<p> which gives the results:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>-66d31'50.141&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>75d39'13.083&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2587.504</dl>
<p> where the first two values are the azimuth from Boston to Portland, the back azimuth from Portland to Boston followed by the distance. </p>
<p> An example of forward geodesic use is to use the Boston location and determine Portland's location by azimuth and distance:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>geod&nbsp;<wbr>+ellps=clrk66&nbsp;<wbr>&lt;&lt;EOF&nbsp;<wbr>+units=us-mi<br />
&nbsp;<wbr>42d15'N 71d07'W -66d31'50.141&quot;&nbsp;<wbr>2587.504<br />
&nbsp;<wbr>EOF</tt></dl>
<p> which gives:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>45d31'0.003&quot;N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123d40'59.985&quot;W 75d39'13.094&quot;</tt></dl>
<p> Note: lack of precision in the distance value compromises the precision of the Portland location.</p>
<h2>SEE ALSO</h2>
<p> Thomas, P.D., 1970, <i>Spheroidal Geodesics, Reference Systems &amp; Local Geometry:</i> U.S. Naval Oceanographic Office, S-138.</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://www.remotesensing.org/proj">http://www.remotesensing.org/proj</a> </p>
<h2>Index</h2>
