---
title: "mgd77sniffer(1)"
name: "mgd77sniffer"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77sniffer/"
description: "mgd77sniffer – Along-track quality control of MGD77 cruises"
---

<h2>NAME</h2>
<p> mgd77sniffer &#8211; Along-track quality control of MGD77 cruises</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77sniffer</code> <i>NGDC-ids</i> [ <i>fieldabbrev</i>,<i>scale</i>,<i>offset</i> ] [ <i>maxspd</i> ] [ <code>d</code>|<code>e</code>|<code>E</code>|<code>f</code>|<code>l</code>|<code>m</code>|<code>s</code>|<code>v</code>[<i>r</i>] ] [ <i>fieldabbrev</i>,<i>imggrid</i>,<i>scale</i>,<i>mode</i> or <i>fieldabbrev</i>,<i>grid</i> ] [ ] [ <i>fieldabbrev</i>,<i>rec1</i>,<i>recN</i> ] [ ] [ <i>custom-limits-file</i> ] [ ] [ <i>region</i> ] [ <code>d</code>|<code>s</code>|<code>t</code> ] [ <i>gap</i> ] [ [<i>level</i>] ] [ <code>c</code>|<code>g</code>|<code>o</code>|<code>s</code>|<code>t</code>|<code>v</code>|<code>x</code> ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] [ <code>-do</code><i>&lt;nodata&gt;</i> ] [ <code>-n</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77sniffer</code> scans old (pre-Y2K) and new format ASCII MGD77 files for errors using point-by-point sanity checking, along-track detection of excessive slopes, and optional comparison of cruise data with global gravity and predicted bathymetry grids. Detected data problems are output by default as verbose descriptions of each detected error, often resulting in multiple messages per scanned record. Data problems are optionally output (<code>-De</code> option) using a computer-parseable format (see E77 ERROR FORMAT description below). Default error thresholds are derived from histograms of all MGD77 geophysical data collected between 1952 and January, 2006. Thresholds are adjustable with the <code>-L</code> option.</p>
<h2>REQUIREMENTS</h2>
<p> The mgd77sniffer links with Generic Mapping Tools 4.0 or later along with the supplemental GMT packages x2sys and mgd77. See <i><a rel="nofollow" href="http://gmt.soest.hawaii.edu">http://gmt.soest.hawaii.edu</a></i> for GMT details. Grids for comparison with cruise data may be downloaded via the web.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>NGDC-ids</i></p>
<dd> Can be one or more of five kinds of specifiers:</p>
<dt>1.</p>
<dd> 8-character NGDC IDs, e.g., 01010083, JA010010etc., etc.</p>
<dt>2.</p>
<dd> 2-character &lt;agency&gt; codes which will return all cruises from each agency.</p>
<dt>3.</p>
<dd> 4-character &lt;agency&gt;&lt;vessel&gt; codes, which will return all cruises from those vessels.</p>
<dt>4.</p>
<dd> =&lt;list&gt;, where &lt;list&gt; is a table with NGDC IDs, one per line.</p>
<dt>5.</p>
<dd> If nothing is specified we return all cruises in the data base. </p>
<p> (See mgd77info <code>-L</code> for agency and vessel codes). The &quot;.mgd77&quot; or &quot;.nc&quot; extensions will automatically be appended, if needed (use <code>-I</code> to ignore certain file types). Cruise files will be looked for first in the current directory and second in all directories listed in <code>$MGD77_HOME</code>/mgd77_paths.txt [If <code>$MGD77_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/mgd77].</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code><i>fieldabbrev</i>,<i>scale</i>,<i>offset</i></p>
<dd> Apply scale factor and DC adjustment to specified data field. Allows adjustment of cruise data prior to along-track analysis. CAUTION: data must be thoroughly examined before applying these global data adjustments. May not be used for multiple cruises.</p>
<dt><code>-C</code><i>maxspd</i></p>
<dd> Set maximum ship speed in m/s, or knots with <code>-N</code> option. Ship speeds exceeding 10 m/s (~20 knots) are flagged as excessive by default.</p>
<dt><code>-D</code><code>d</code>|<code>e</code>|<code>E</code>|<code>f</code>|<code>l</code>|<code>m</code>|<code>s</code>|<code>v</code>[<i>r</i>]</p>
<dd> Suppress default warning output and only dump cruise data row-by-row such as values, gradients, grid-cruise differences, E77 error summaries for each record, re-created MGD77 records or sniffer limits. Append r to include all records (default omits records where navigation errors were detected). </p>
<p> <code>-Dd</code> output differences between cruise and grid data. Requires <code>-G</code> option. Output columns include: </p>
<p> <i>lat lon dist cruiseZ gridZ diff [cruiseZ2 gridZ2 diff2 &#8230;]</i> </p>
<p> Note: grid values are subtracted from cruise data so a positive difference implies cruise &gt; grid. For multiple grid comparison, <i>cruiseZ gridZ diff</i> are repeated for each grid comparison in command line order. </p>
<p> <code>-De</code> output E77 error classification format. Error output is divided into (1) a header containing information globally applicable to the cruise and (2) individual error records summarizing all errors encountered in each cruise record. mgd77sniffer writes E77 directly to &lt;ngdc_id.e77&gt; file handle. See <code>E77 ERROR FORMAT</code> below for additional details. </p>
<p> <code>-DE</code> Same as <code>-De</code> but no regression tests will be carried out. </p>
<p> <code>-Df</code> output delta Z (change in geophysical field) column and delta S (change in distance) for each geophysical field. Distance between observations often differ for different fields depending on instrument sampling rate, so ds is included for each geophysical observation. Output columns include: </p>
<p> <i>d[twt] ds d[depth] ds d[mtf1] ds d[mtf2] ds d[mag] ds d[diur] ds d[msd] ds d[gobs] ds d[eot] ds d[faa] ds</i> </p>
<p> <code>-Dl</code> display mgd77sniffer limits. Customize this output to create a custom limits file for the <code>-L</code> option. No additional arguments are required. Output columns include: </p>
<p> <i>fieldabbrev min max maxSlope maxArea</i> </p>
<p> <code>-Dm</code> output MGD77 format records in Y2K-compliant MGD77 format </p>
<p> <code>-Dn</code> output distance to coast for each record. Requires the <code>-Gnav</code> option. Output columns include: </p>
<p> <i>lat lon dist distToCoast</i> </p>
<p> <code>-Ds</code> output calculated gradients for speed and geophysical fields. Gradients correspond to the gradient type selected in the <code>-S</code> option (spatial derivatives by default). Output columns include: </p>
<p> <i>speed d[twt] d[depth] d[mtf1] d[mtf2] d[mag] d[diur] d[msd] d[gobs] d[eot] d[faa]</i> </p>
<p> See <code>MGD77 FIELD INFO</code> below for field and abbreviations descriptions. </p>
<p> <code>-Dv</code> display values for the twelve position and geophysical fields for each MGD77 data record (in this order): </p>
<p> <i>lat lon twt depth mtf1 mtf2 mag diur msens gobs eot faa</i> </p>
<p> See below for <code>MGD77 FIELD INFO</code>.</p>
<dt><code>-G</code><i>information</i></p>
<dd> Compare cruise data to GMT or IMG grids. Use one of the formats below. <code>-G</code><i>fieldabbrev</i>,<i>imggrid</i>,<i>scale</i>,<i>mode</i> Compare cruise data to the specified grid in Sandwell/Smith Mercator format. Requires a valid MGD77 field abbreviation (see <code>MGD77 FIELD INFO</code> below) followed by a comma, the path (if not in current directory) and grid filename, a scale to multiply the data (1 or 0.1), and mode which stand for the following: (0) Img files with no constraint code, returns data at all points, (1) Img file with constraints coded, return data at all points, (2) Img file with constraints coded, return data only at constrained points and NaN elsewhere, and (3) Img file with constraints coded, return 1 at constraints and 0 elsewhere. <code>-G</code><i>fieldabbrev</i>,<i>grid</i> Compare cruise data to the specified grid. Requires a valid MGD77 field abbreviation (see <code>MGD77 FIELD INFO</code> below) followed by a comma, then the path (if not in current directory) and grid filename. Multiple grid comparison is supported by using separate <code>-G</code> calls for each grid. See <code>GRID FILE INFO</code> below. </p>
<p> Grid comparison activates several additional error checks. (1) Re-weighted Least Squares Regression of ship versus grid data determines slope and DC shift, which when differing from expected 1 and 0, respectively, may indicate incorrectly scaled ship data, including incorrect units or instrument drift as well as erroneous gravity tie-in. (2) Accumulated ship grid offsets are computed along-track and excessive offsets are flagged according to <i>maxArea</i> threshold (use <code>-L</code> option to adjust <i>maxArea</i>). Warning: predicted bathymetry grids are constrained by cruise data so grids and cruise data are not always independent. Comparison of cruise bathymetry with predicted bathymetry grids also activates a &quot;navigation crossing over land&quot; check.</p>
<dt><code>-H</code></p>
<dd> (with <code>-G</code>|<code>g</code> only) disable (or force) decimation during RLS analysis of ship and gridded data. By default mgd77sniffer analyses both the full and decimated data sets then reports RLS statistics for the higher correlation regression. </p>
<p> <code>-Hb</code> analyze both (default), report better of two. </p>
<p> <code>-Hd</code> to disable data decimation (equivalent to -H with no argument). </p>
<p> <code>-Hf</code> to force data decimation.</p>
<dt><code>-I</code><i>fieldabbrev</i>,<i>rec1</i>,<i>recN</i></p>
<dd> Append a field abbreviation and the first and last record in a range of records that should be flagged as bad (and set to NaN prior to the analysis). Repeat as many times as needed. May not be used for multiple cruises.</p>
<dt><code>-K</code></p>
<dd> Reverse navigation quality flags (good to bad and vice versa). May be necessary when a majority of navigation fixes are erroneously flagged bad, which can happen when a cruise&#8217;s first navigation fix is extremely erroneous. Caution! This will affect sniffer output and should only be attempted after careful manual navigation review.</p>
<dt><code>-L</code><i>custom-limits-file</i></p>
<dd> Override mgd77sniffer default error detection limits. Supply path and filename to the custom limits file. Rows not beginning with a valid MGD77 field abbreviation are ignored. Field abbreviations are listed below in exact form under MGD77 FIELD INFO. Multiple field limits may be modified using one default file, one field per line. Field min, max, max slope and max area may be changed for each field. Max slope pertains to the gradient type selected using the <code>-S</code> option. Max area is used by the <code>-G</code> option as the threshold for flagging excessive offsets from the specified grid. Dump defaults <code>-Dl</code> to view syntax or to quickly create an editable custom limits file. </p>
<p> Example custom default file contents (see below for units): <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> # abbrev </td>
<td> min </td>
<td> max </td>
<td> maxSlope </td>
<td> maxArea
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> twt </td>
<td> 0 </td>
<td> 15 </td>
<td> 1 </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> depth </td>
<td> 0 </td>
<td> 11000 </td>
<td> 500 </td>
<td> 5000
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> mag </td>
<td> -800 </td>
<td> 800 </td>
<td> &#8212; </td>
<td> &#8212;
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> faa </td>
<td> -300 </td>
<td> 300 </td>
<td> 100 </td>
<td> 2500
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Use a dash &#8216;-&#8216; to retain a default limit. Hint: to test your custom limits, try: mgd77sniffer <code>-Dl</code> <code>-L</code>&lt;yourlimitsfile&gt;</p>
<dt><code>-N</code></p>
<dd> Use nautical units.</p>
<dt><code>-P</code></p>
<dd> Flag regression statistics that are outside the specified confidence level. (i.e., -P5 flags coefficients m, b, rms, and r that fall outside 95%.)</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension.</p>
<dt><code>-S</code><code>d</code>|<code>s</code>|<code>t</code></p>
<dd> Specify gradient type for along-track excessive slope checking. <code>-Sd</code> Calculate change in z values along track (dz). Output is given in geophysical units, e.g., mGal. <code>-Ss</code> Calculate spatial gradients (dz/ds). Output is given in geophysical units per km along the survey track, e.g., mGal/km. <code>-St</code> Calculate time gradients (dz/dt) [default]. Output is given in geophysical units per second along the survey track, e.g., mGal/sec.</p>
<dt><code>-T</code><i>gap</i></p>
<dd> Adjusts mgd77sniffer gap handling. By default, data gaps greater than 5 km are skipped. Set to zero to de-activate gap skipping.</p>
<dt><code>-W</code><code>c</code>|<code>g</code>|<code>o</code>|<code>s</code>|<code>t</code>|<code>v</code>|<code>x</code></p>
<dd> Print out only certain warning types for verbose error messages. Comma delimit any combination of <code>c|g|o|s|t|v|x</code>: where (<code>c</code>) type code warnings, (<code>g</code>)radient out of range, (<code>o</code>)ffsets from grid (requires <code>-G</code>|<code>g</code>), (<code>s</code>)peed out of range, (<code>t</code>)ime warnings, (<code>v</code>)alue out of range, (<code>x</code>) warning summaries. By default ALL warning messages are printed.Not compatible with any <code>-D</code> options.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. Output binary data for <code>-D</code>d|f|s|v option.</p>
<dt><code>-do</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace output columns that equal NaN with <i>nodata</i>.</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>MGD77 FIELD INFO</h2>
<p> <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>Field</i> </td>
<td> <i>Abbreviation</i> </td>
<td> <i>Units</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Two-way </td>
<td> Travel </td>
<td> Time
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Corrected </td>
<td> Depth </td>
<td> depth
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Mag </td>
<td> Total </td>
<td> Field1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Mag </td>
<td> Total </td>
<td> Field2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Residual </td>
<td> Magnetic </td>
<td> mag
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Diurnal </td>
<td> Correction </td>
<td> diur
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Mag </td>
<td> Sensor </td>
<td> Depth/Alt
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Observed </td>
<td> Gravity </td>
<td> gobs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Eotvos </td>
<td> Correction </td>
<td> eot
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Free </td>
<td> Air </td>
<td> Anomaly
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>GRID FILE INFO</h2>
<p> For the grids must eitehr be in the format used by Sandwell &amp; Smith, which is a spherical Mercator 2-byte grid with no header, or any grid type supported by GMT and therefore must contain a GMT header. A correctly formatted *.i2 grid file can be generated using grdraster as shown below. </p>
<p> gmtset GRIDFILE_SHORTHAND TRUE </p>
<p> Create/edit .gmt_io file to include the following rows: </p>
<p> # GMT I/O shorthand file </p>
<p> # suffix format_id scale offset NaN </p>
<p> grd 0 &#8211; &#8211; &#8211; &#8211; </p>
<p> i2 2 &#8211; &#8211; 32767 </p>
<pre>
gmt grdraster 1 -R0/359:55/-90/90 -Getopo5_hdr.i2
</pre>
<p> The new grid, etopo5_hdr.i2 in this example, contains a GMT header and can be used in the <code>-G</code> option to compare cruise depth with grid values.</p>
<h2>E77 ERROR FORMAT</h2>
<dl>
<dt><code>Header</code></p>
<dd> Information pertaining to an entire cruise, such as NGDC and survey institution identification codes, cruise examination time, two-way travel time corrector information, data precision warnings, as well as systematic scales, DC shifts and correlation coefficients from global grid comparisons are reported as E77 header information. </p>
<p> <code>Sample</code> </p>
<p> # Cruise 08010039 ID 74010908 MGD77 FILE VERSION: 19801230 N_RECS: 3066 </p>
<p> # Examined: Wed Oct 3 16:30:13 2007 by mtchandl </p>
<p> # Arguments: -De -Gdepth,/data/GRIDS/etopo5_hdr.i2 </p>
<p> N Errata table verification status </p>
<p> # mgd77manage applies corrections if the errata table is verified (toggle &#8216;N&#8217; above to &#8216;Y&#8217; after review) </p>
<p> # For instructions on E77 format and usage, see <i><a rel="nofollow" href="http://gmt.soest.hawaii.edu/mgd77/errata.php">http://gmt.soest.hawaii.edu/mgd77/errata.php</a></i> </p>
<p> # Verified by: </p>
<p> # Comments: </p>
<p> # Errata: Header </p>
<p> Y-E-08010039-H13-02: Invalid Magnetics Sampling Rate: (99) [ ] </p>
<p> Y-W-08010039-H13-10: Survey year (1975) outside magnetic reference field IGRF 1965 time range (1965-1970) </p>
<p> Y-I-08010039-depth-00: RLS m: 1.00053 b: 0 rms: 127.851 r: 0.973422 significant: 1 decimation: 0 </p>
<p> Y-W-08010039-twt-09: More recent bathymetry correction table available </p>
<p> Y-W-08010039-mtf1-10: Integer precision </p>
<p> Y-W-08010039-mag-10: Integer precision</p>
<dt><code>Error Record</code></p>
<dd> Individual error records have strict format. Included is a time or distance column followed by record number, a formatted error code string, and finally a verbose description of errors detected in the record. Three error classes are encoded into the error code string with different alphabetic characters representing unique error types. See below for error code format description. </p>
<p> <code>Format</code> &lt;time/distance&gt; &lt;record number&gt; &lt;error code string&gt; &lt;description&gt; </p>
<p> <code>Sample</code> </p>
<p> # Errata: Data </p>
<p> Y 08010039 1975-05-10T22:16:05.88 74 C-0-0 NAV: excessive speed</p>
<dt><code>Error Code Description</code></p>
<dd> Each of the three error classes is separated by a dash <code>&#8211;</code> and described by a combination of alphabetic characters or 0 signifying no detected problems. </p>
<p> Error classes: NAV-VAL-GRAD </p>
<p> <code>Error Class Descriptions</code> </p>
<p> NAV (navigation): </p>
<p> 0 &#8211; fine </p>
<p> A &#8211; time out of range </p>
<p> B &#8211; time decreasing </p>
<p> C &#8211; excessive speed </p>
<p> D &#8211; above sea level </p>
<p> E &#8211; lat undefined </p>
<p> F &#8211; lon undefined </p>
<p> VAL (value): </p>
<p> 0 &#8211; fine </p>
<p> K &#8211; twt invalid </p>
<p> L &#8211; depth invalid </p>
<p> O &#8211; mtf1 invalid </p>
<p> etc. </p>
<p> GRAD (gradient): </p>
<p> 0 &#8211; fine </p>
<p> K &#8211; d[twt] excessive </p>
<p> L &#8211; d[depth] excessive</p>
<dt><code>O &#8211; d[mtf1] excessive</code></p>
<dd> etc. </p>
<p> The NAV error class has unique cases while VAL and GRAD classes are described by alphabetic characters for each of the 24 numeric fields in MGD77 format order. </p>
<p> MGD77 bit-pattern w/ E77 alpha characters </p>
<p> |&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-|&#8212;&#8212;&#8212;-| </p>
<p> | X W V U T S R Q P O N M L K J I H G F E D C B A | E77 Code | </p>
<p> | &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; | &#8211; &#8211; &#8211; &#8211; -| </p>
<p> | n f e g m d m m m m b b d t p l l m h d m y t d | F I | </p>
<p> | q a o o s i s a t t t c e w t o a i o a o e z r | i D | </p>
<p> | c a t b d u e g f f c c p t c n t n u y n a t | e | </p>
<p> | s r n 2 1 t r t r | l | </p>
<p> | s h h | d | </p>
<p> | &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; &#8211; | &#8211; &#8211; &#8211; &#8211; -| </p>
<p> | 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | Bit place| </p>
<p> | &#8211; G C G C C &#8211; G G G &#8211; &#8211; G G &#8211; &#8211; &#8211; T T T T T &#8211; &#8211; | Bit type | </p>
<p> |&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-|&#8212;&#8212;&#8212;-| </p>
<p> Bit types: (G)eophysical, (C)orrection, (T)ime</dl>
<h2>EXAMPLES</h2>
<p> To scan for excessive values or gradients, try </p>
<pre>
gmt mgd77sniffer 08010001
</pre>
<p> To dump cruise gradients, try </p>
<pre>
gmt mgd77sniffer 08010001 -Ds
</pre>
<p> To compare cruise depth with ETOPO5 bathymetry and gravity with Sandwell/Smith 2 min gravity version 11, try </p>
<pre>
mgd77sniffer 08010001 -Gdepth,/data/GRIDS/etopo5_hdr.i2 \
             -Gfaa,/data/GRIDS/grav.11.2.img,0.1,1
</pre>
<h2>SEE ALSO</h2>
<p> <code>mgd77list</code>, <code>mgd77track</code> <code>x2sys_init</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt.">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt.</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
