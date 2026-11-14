---
title: "nad2nad(1)"
name: "nad2nad"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nad2nad/"
description: "nad2nad – North American Datum conversion filter"
---

<h2>NAME</h2>
<p> nad2nad &#8211; North American Datum conversion filter</p>
<h2>SYNOPSIS</h2>
<p> <code>nad2nad</code> [ <code>-eEfihortwW</code> [ <i>args</i> ] ] [ <code>+args</code> ] file[s]</p>
<h2>DESCRIPTION</h2>
<p> Program <code>nad2nad</code> is a filter to convert data between North America Datum 1927 (NAD27) and North American Datum 1983. <code>nad2nad</code> can optionally process both State Plane Coordinate System (SPCS) and Universal Transverse Mercator (UTM) grid data as well as geographic data for both input and output. This can also be accomplished with the <i>cs2cs</i> program. </p>
<p> The following control parameters can appear in any order:</p>
<dl>
<dt><code>-[i|o]</code><i> keyword[,keyword]</i></p>
<dd> The <code>-i</code> and <code>-o</code> option expect keyword arguments which define various characteristics and processing modes of the respective input data. Usage allows multiple arguments to be included with a &#8211; operator when separated by commas. Datum conversion requires the data to be in geographic coordinates, but <code>nad2nad</code> will allow conversion of data to and from SPCS or UTM grid systems. The following are keywords and arguments recognized by both the <code>-i</code> and <code>-o</code> that will apply to respective input and output conversion of user data to internal geographic coordinates:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>27|83</code></p>
<dd> datum of data</p>
<dt><code>utm=</code><i>n</i></p>
<dd> <code>UTM</code> coordinates in meters for zone <i>n</i></p>
<dt><code>spcs=</code><i>n</i></p>
<dd> for data in <code>SPCS</code> coordinates, where <i>n</i> is state zone number.</p>
<dt><code>feet</code></p>
<dd> data units are in U.S. Surveyor&#8217;s feet. This is allowed only when the <i>spcs</i> option been previously used. Default coordinates are in meters.</p>
<dt><code>bin</code></p>
<dd> for data in binary form.</p>
<dt><code>rev</code></p>
<dd> data in lat-lon order rather than default lon-lat order.</p>
<dt><code>hp=</code><i>ss</i></p>
<dd> use high precision conversion zone <i>ss.</i> Certain States have ancillary correction tables to further refine the basic conus table. <i>Ss</i> key and States are:</p>
<dl>
<dt>
<dd> FL Florida<br />
 MD Maryland<br />
 TN Tennessee<br />
 WI Wisconsin<br />
 WO Washington, Oregon and northern part of California.</dl>
</dl>
</dl>
<dt><code>-t</code><i>a</i></p>
<dd> <i>A</i> specifies a character employed as the first character to denote a control line to be passed through without processing. This option applicable to ascii input only. (# is the default value).</p>
<dt><code>-e</code><i> string</i></p>
<dd> <i>String</i> is an arbitrary string to be output if an error is detected during data transformations. The default value is: *	*. Note that if the <code>-o bin</code> option is employed, an error is output as HUGE_VAL for both values.</p>
<dt><code>-r</code><i> region</i></p>
<dd> specifies which regional conversion table to employ which are identified by the following:</p>
<dl>
<dt>
<dd> conus &#8211; conterminous 48 States<br />
 alaska &#8211; State of Alaska<br />
 hawaii &#8211; State of Hawaii<br />
 prvi &#8211; Puerto Rico and Virgin Islands<br />
 stgeorge &#8211; St. George Is, Alaska<br />
 stpaul &#8211; St. Paul Is, Alaska<br />
 stlrnc &#8211; St. Lawrence Is, Alaska</p>
<dl>
<dt><code>-E</code></p>
<dd> Input coordinates are echoed to output before ouput values.</dl>
</dl>
<dt><code>-f</code><i> format</i></p>
<dd> <i>Format</i> is a <i>printf</i> format string to control the form of the output values. For inverse projections, the output will be in degrees when this option is employed. If a format is specified for inverse projection the output data will be in decimal degrees. The default format is &#8220;%.2f&#8221; for forward projection and DMS for inverse.</p>
<dt><code>-[w|W]</code><i>n</i></p>
<dd> <i>N</i> is the number of significant fractional digits to employ for seconds output (when the option is not specified, <code>-w3</code> is assumed). When <code>-W</code> is employed the fields will be constant width and with leading zeroes.</dl>
<p> One or more <i>files</i> (processed in left to right order) specify the source of data to be transformed. A &#8211; will specify the location of processing standard input. If no files are specified, the input is assumed to be from <i>stdin.</i> For ASCII input data the two data values must be in the first two white space separated fields and when both input and output are ASCII all trailing portions of the input line are appended to the output line. </p>
<p> Input geographic data (longitude and latitude) must be in DMS format when neither <i>utm</i> nor <i>spcs</i> is specified, otherwise in meters or feet (<i>feet</i> option used). Input data fields must be separated by white space and not have imbedded white space. </p>
<p> Output data will be in tab separated fields of DMS or grid coordinates in meters or feet. </p>
<p> Any data after the two input values are echoed after the two output data values.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1U-cs2cs/">cs2cs</a>(1U), <a href="//www.systutorials.com/docs/linux/man/1U-proj/">proj</a>(1U),</code><br />
 <i>Cartographic Projection Procedures for the UNIX Environment&#8212;A User&#8217;s Manual,</i> (Evenden, 1990, Open-file report 90-284).</p>
<h2>HOME PAGE</h2>
<p> <a rel="nofollow" href="http://www.remotesensing.org/proj">http://www.remotesensing.org/proj</a> </p>
<h2>Index</h2>
