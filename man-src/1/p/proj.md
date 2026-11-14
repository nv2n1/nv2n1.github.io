---
title: "proj(1)"
name: "proj"
section: "1"
letter: "p"
url: "/docs/linux/man/1-proj/"
description: "proj – forward cartographic projection filter invproj – inverse cartographic projection filter"
---

<h2>NAME</h2>
<p> proj &#8211; forward cartographic projection filter<br />
 invproj &#8211; inverse cartographic projection filter</p>
<h2>SYNOPSIS</h2>
<p> <code>proj</code> [ <code>-bceEfiIlmorsStTvVwW</code> [ <i>args</i> ] ] [ <code>+args</code> ] file[s]<br />
 <code>invproj</code> [ <code>-bceEfiIlmorsStTwW</code> [ <i>args</i> ] ] [ <code>+args</code> ] file[s]</p>
<h2>DESCRIPTION</h2>
<p> <i>Proj</i> and <i>invproj</i> perform respective forward and inverse transformation of cartographic data to or from cartesian data with a wide range of selectable projection functions. </p>
<p> The following control parameters can appear in any order:</p>
<dl>
<dt><code>-b</code></p>
<dd> Special option for binary coordinate data input and output through standard input and standard output. Data is assumed to be in system type <i>double</i> floating point words. This option is to be used when <code>proj</code> is a <i>son</i> process and allows bypassing formatting operations.</p>
<dt><code>-i</code></p>
<dd> Selects binary input only (see <code>-b option).</code></p>
<dt><code>-I</code></p>
<dd> alternate method to specify inverse projection. Redundant when used with <code>invproj.</code></p>
<dt><code>-o</code></p>
<dd> Selects binary output only (see <code>-b option).</code></p>
<dt><code>-t</code><i>a</i></p>
<dd> <i>A</i> specifies a character employed as the first character to denote a control line to be passed through without processing. This option applicable to ascii input only. (# is the default value).</p>
<dt><code>-e</code><i> string</i></p>
<dd> <i>String</i> is an arbitrary string to be output if an error is detected during data transformations. The default value is: *	*. Note that if the <code>-b,</code> <code>-i</code> or <code>-o</code> options are employed, an error is returned as HUGE_VAL value for both return values.</p>
<dt><code>-E</code></p>
<dd> causes the input coordinates to be copied to the output line prior to printing the converted values.</p>
<dt><code>-l</code><i>[p|P|=|e|u|d]</i><code>id</code></p>
<dd> List projection identifiers with <code>-l,</code> <code>-lp</code> or <code>-lP (expanded)</code> that can be selected with <code>+proj.</code> <code>-l=</code><i>id</i> gives expanded description of projection <i>id.</i> List ellipsoid identifiers with <code>-le,</code> that can be selected with <code>+ellps,</code> <code>-lu</code> list of cartesian to meter conversion factors that can be selected with <code>+units</code> or <code>-ld</code> list of datums that can be selected with <code>+datum.</code></p>
<dt><code>-r</code></p>
<dd> This options reverses the order of the expected input from longitude-latitude or x-y to latitude-longitude or y-x.</p>
<dt><code>-s</code></p>
<dd> This options reverses the order of the output from x-y or longitude-latitude to y-x or latitude-longitude.</p>
<dt><code>-S</code></p>
<dd> Causes estimation of <i>meridinal</i> and <i>parallel</i> scale factors, <i>area</i> scale factor and <i>angular distortion,</i> and <i>maximum</i> and <i>minimum</i> scale factors to be listed between &lt;&gt; for each input point. For conformal projections meridinal and parallel scales factors will be equal and angular distortion zero. Equal area projections will have an area factor of 1.</p>
<dt><code>-m</code><i> mult</i></p>
<dd> The cartesian data may be scaled by the <i>mult</i> parameter. When processing data in a forward projection mode the cartesian output values are multiplied by <i>mult</i> otherwise the input cartesian values are divided by <i>mult</i> before inverse projection. If the first two characters of <i>mult</i> are 1/ or 1: then the reciprocal value of <i>mult</i> is employed.</p>
<dt><code>-f</code><i> format</i></p>
<dd> <i>Format</i> is a <i>printf</i> format string to control the form of the output values. For inverse projections, the output will be in degrees when this option is employed. The default format is &quot;%.2f&quot; for forward projection and DMS for inverse.</p>
<dt><code>-[w|W]</code><i>n</i></p>
<dd> <i>N</i> is the number of significant fractional digits to employ for seconds output (when the option is not specified, <code>-w3</code> is assumed). When <code>-W</code> is employed the fields will be constant width and with leading zeroes.</p>
<dt><code>-v</code></p>
<dd> causes a listing of cartographic control parameters tested for and used by the program to be printed prior to input data. Should not be used with the <code>-T</code> option.</p>
<dt><code>-V</code></p>
<dd> This option causes an expanded annotated listing of the characteristics of the projected point. <code>-v is implied with this option.</code></p>
<dt><code>-T</code><i> ulow,uhi,vlow,vhi,res[,umax,vmax]</i></p>
<dd> This option creates a set of bivariate Chebyshev polynomial coefficients that approximate the selected cartographic projection on <i>stdout.</i> The values <i>low</i> and <i>hi</i> denote the range of the input where the <i>u</i> or <i>v</i> prefixes apply to respective longitude-x or latitude-y depending upon whether a forward or inverse projection is selected. <i>Res</i> is an integer number specifying the power of 10 precision of the approximation. For example, a <i>res</i> of -3 specifies an approximation with an accuracy better than .001. <i>Umax,</i> and <i>vmax</i> specify maximum degree of the polynomials (default: 15). See also: <code><a href="/docs/linux/man/1-fproj/">fproj</a>(1).</code></dl>
<p> The <code>+args</code> run-line arguments are associated with cartographic parameters and usage varies with projection and for a complete description see <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual )</i> and supplementary documentation for Release 4. </p>
<p> Additional projection control parameters may be contained in two auxiliary control files: the first is optionally referenced with the <code>+init=</code><i>file:id</i> and the second is always processed after the name of the projection has been established from either the run-line or the contents of <code>+init</code> file. The environment parameter <code>PROJ_LIB</code> establishes the default directory for a file reference without an absolute path. This is also used for supporting files like datum shift files. </p>
<p> One or more <i>files</i> (processed in left to right order) specify the source of data to be transformed. A &#8211; will specify the location of processing standard input. If no files are specified, the input is assumed to be from <i>stdin.</i> For ASCII input data the two data values must be in the first two white space separated fields and when both input and output are ASCII all trailing portions of the input line are appended to the output line. </p>
<p> Input geographic data (longitude and latitude) must be in DMS format and input cartesian data must be in units consistent with the ellipsoid major axis or sphere radius units. Output geographic coordinates will be in DMS (if the <code>-w</code> switch is not employed) and precise to 0.001&quot; with trailing, zero-valued minute-second fields deleted.</p>
<h2>EXAMPLE</h2>
<p> The following script</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>proj&nbsp;<wbr>+proj=utm&nbsp;<wbr>+lon_0=112w&nbsp;<wbr>+ellps=clrk66 -r&nbsp;<wbr>&lt;&lt;EOF<br />
&nbsp;<wbr>45d15'33.1&quot;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>111.5W</p>
<p>&nbsp;<wbr>45d15.551666667N<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-111d30</p>
<p>&nbsp;<wbr>+45.25919444444<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>111d30'000w</p>
<p>&nbsp;<wbr>EOF</tt></dl>
<p> will perform UTM forward projection with a standard UTM central meridian nearest longitude 112&#176;W. The geographic values of this example are equivalent and meant as examples of various forms of DMS input. The x-y output data will appear as three lines of:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>460769.27<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>5011648.45
</dl>
<p> </tt></p>
<h2>OTHER PROGRAMS</h2>
<p> The <i>proj</i> program is limited to converting between geographic and projection coordinates within one datum. </p>
<p> The <i>cs2cs</i> program operates similarly, but allows translation between any pair of definable coordinate systems, including support for datum translation. </p>
<p> The <i>nad2nad</i> program provides for translation between NAD27 and NAD83 (also available in cs2cs<i>) in a convenient manner. </p>
<p> The geod</i> program provides the ability to compute geodesic (Great Circle) computations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1U-cs2cs/">cs2cs</a>(1U), <a href="//www.systutorials.com/docs/linux/man/1U-nad2nad/">nad2nad</a>(1U), <a href="//www.systutorials.com/docs/linux/man/1U-geod/">geod</a>(1U), <a href="//www.systutorials.com/docs/linux/man/3U-pj_init/">pj_init</a>(3U),</code><br />
 <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual,</i> (Evenden, 1990, Open-file report 90-284).<br />
 <i>Map Projections Used by the U. S. Geological Survey</i> (Snyder, 1984, USGS Bulletin 1532).<br />
 <i>Map Projections&#8212;A Working Manual</i> (Snyder, 1988, USGS Prof. Paper 1395).<br />
 <i>An Album of Map Projections</i> (Snyder &amp; Voxland, 1989, USGS Prof. Paper 1453).</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://www.remotesensing.org/proj">http://www.remotesensing.org/proj</a> </p>
<h2>Index</h2>
