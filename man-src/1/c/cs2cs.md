---
title: "cs2cs(1)"
name: "cs2cs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cs2cs/"
description: "cs2cs – cartographic coordinate system filter"
---

<h2>NAME</h2>
<p> cs2cs &#8211; cartographic coordinate system filter</p>
<h2>SYNOPSIS</h2>
<p> <code>cs2cs</code> [ <code>-eEfIlrstvwW</code> [ <i>args</i> ] ] [ <code>+opts[=arg]</code> ] </p>
<p>[&nbsp;<wbr><code>+to</code>&nbsp;<wbr>[<code>+opts</code>[<code>=arg</code>]]&nbsp;<wbr>] file[s]</p>
<h2>DESCRIPTION</h2>
<p> <i>Cs2cs</i> performs transformation between the source and destination cartographic coordinate system on a set of input points. The coordinate system transformation can include translation between projected and geographic coordinates as well as the application of datum shifts. </p>
<p> The following control parameters can appear in any order:</p>
<dl>
<dt><code>-I</code></p>
<dd> method to specify inverse translation, convert from <code>+to</code> coordinate system to the primary coordinate system defined.</p>
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
<dt><code>-f</code><i> format</i></p>
<dd> <i>Format</i> is a <i>printf</i> format string to control the form of the output values. For inverse projections, the output will be in degrees when this option is employed. If a format is specified for inverse projection the output data will be in decimal degrees. The default format is &quot;%.2f&quot; for forward projection and DMS for inverse.</p>
<dt><code>-[w|W]</code><i>n</i></p>
<dd> <i>N</i> is the number of significant fractional digits to employ for seconds output (when the option is not specified, <code>-w3</code> is assumed). When <code>-W</code> is employed the fields will be constant width and with leading zeroes.</p>
<dt><code>-v</code></p>
<dd> causes a listing of cartographic control parameters tested for and used by the program to be printed prior to input data.</dl>
<p> The <code>+args</code> run-line arguments are associated with cartographic parameters and usage varies with projection and for a complete description see <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual )</i> and supplementary documentation for Release 4. </p>
<p> The <i>cs2cs</i> program requires two coordinate system definitions. The first (or primary is defined based on all projection parameters not appearing after the <code>+to</code> argument. All projection parameters appearing after the <code>+to</code> argument are considered the definition of the second coordinate system. If there is no second coordinate system defined, a geographic coordinate system based on the datum and ellipsoid of the source coordinate system is assumed. Note that the source and destination coordinate system can both be projections, both be geographic, or one of each and may have the same or different datums. </p>
<p> Additional projection control parameters may be contained in two auxiliary control files: the first is optionally referenced with the <code>+init=</code><i>file:id</i> and the second is always processed after the name of the projection has been established from either the run-line or the contents of <code>+init</code> file. The environment parameter <code>PROJ_LIB</code> establishes the default directory for a file reference without an absolute path. This is also used for supporting files like datum shift files. </p>
<p> One or more <i>files</i> (processed in left to right order) specify the source of data to be transformed. A &#8211; will specify the location of processing standard input. If no files are specified, the input is assumed to be from <i>stdin.</i> For input data the two data values must be in the first two white space separated fields and when both input and output are ASCII all trailing portions of the input line are appended to the output line. </p>
<p> Input geographic data (longitude and latitude) must be in DMS format and input cartesian data must be in units consistent with the ellipsoid major axis or sphere radius units. Output geographic coordinates will be in DMS (if the <code>-w</code> switch is not employed) and precise to 0.001&quot; with trailing, zero-valued minute-second fields deleted.</p>
<h2>EXAMPLE</h2>
<p> The following script</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>cs2cs&nbsp;<wbr>+proj=latlong&nbsp;<wbr>+datum=NAD83&nbsp;<wbr><br />
&nbsp;<wbr>+to&nbsp;<wbr>+proj=utm&nbsp;<wbr>+zone=10&nbsp;<wbr>+datum=NAD27 -r&nbsp;<wbr>&lt;&lt;EOF<br />
&nbsp;<wbr>45d15'33.1&quot;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>111.5W</p>
<p>&nbsp;<wbr>45d15.551666667N<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-111d30</p>
<p>&nbsp;<wbr>+45.25919444444<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>111d30'000w</p>
<p>&nbsp;<wbr>EOF</tt></dl>
<p> will transform the input NAD83 geographic coordinates into NAD27 coordinates in the UTM projection with zone 10 selected. The geographic values of this example are equivalent and meant as examples of various forms of DMS input. The x-y output data will appear as three lines of:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr><tt>1402285.99&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5076292.42 0.000</dl>
<p> </tt></p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1U-proj/">proj</a>(1U),</code><br />
 <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual,</i> (Evenden, 1990, Open-file report 90-284).<br />
 <i>Map Projections Used by the U. S. Geological Survey</i> (Snyder, 1984, USGS Bulletin 1532).<br />
 <i>Map Projections&#8212;A Working Manual</i> (Snyder, 1988, USGS Prof. Paper 1395).<br />
 <i>An Album of Map Projections</i> (Snyder &amp; Voxland, 1989, USGS Prof. Paper 1453).</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://www.remotesensing.org/proj">http://www.remotesensing.org/proj</a> </p>
<h2>Index</h2>
