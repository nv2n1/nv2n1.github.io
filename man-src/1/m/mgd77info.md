---
title: "mgd77info(1)"
name: "mgd77info"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77info/"
description: "mgd77info – Extract information about MGD77 files"
---

<h2>NAME</h2>
<p> mgd77info &#8211; Extract information about MGD77 files</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77info</code> <i>NGDC-ids</i> [ [<code>m</code>|<code>e</code>] ] [ [<code>m</code>|<code>e</code>] ] [ <code>-I</code><i>ignore</i> ] [ <code>f</code>[<i>item</i>]|<code>r</code>|<code>e</code>|<code>h</code> ] [ [<code>v</code>] ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77info</code> reads &lt;legid&gt;.[mgd77|nc] files and produces a single record of information about each cruise specified. The information includes beginning and end times, total track distances in km, longitude and latitude range, and the total number of geophysical observations. Optionally, choose instead to see the original MGD77 header meta-data section or its individual members. </p>
<p> If you need to know which tracks are crossing through a given region and what kinds of geophysical observations are available, consider using the x2sys tools to set up a tracks index data base (see <code>x2sys_init</code> for more information).</p>
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
<dt><code>-C</code>[<code>m</code>|<code>e</code>]</p>
<dd> List abbreviations for all columns present in the MGD77[+] files. Append <code>m</code> or <code>e</code> to limit the display to the MGD77 standard or MGD77+ extended set only.</p>
<dt><code>-E</code>[<code>m</code>|<code>e</code>]</p>
<dd> Give a one-line summary for each cruise listed.</p>
<dt><code>-Mf</code>[<i>item</i>]|<code>r</code>|<code>e</code>|<code>h</code></p>
<dd> List the meta-data (header) and (if present) the MGD77+ history for each cruise. Append <code>f</code> for a formatted display. This will list individual parameters and their values, one entry per output line, in a format that can be searched using standard UNIX text tools. Alternatively, append the name of a particular parameter (you only need to give enough characters &#8211; starting at the beginning &#8211; to uniquely identify the item). Give &#8211; to display the list of all parameter names. You may also specify the number of a parameter. For the raw, punchcard-formatted MGD77 original header block, append <code>r</code> instead. For the MGD77+ E77 status, append <code>e</code> instead. Finally, for the MGD77+ history, append <code>h</code> instead.</p>
<dt><code>-I</code><i>ignore</i></p>
<dd> Ignore certain data file formats from consideration. Append <code>a|c|t</code> to ignore MGD77 ASCII, MGD77+ netCDF, or plain tab-separated ASCII table files, respectively. The option may be repeated to ignore more than one format. [Default ignores none].</p>
<dt><code>-L</code>[<code>v</code>]</p>
<dd> No cruise information is listed. Instead, we just display a list of the GEODAS institution 2-character codes and their names. Optionally, append <code>v</code> to also display the vessels and their 4-character codes for each institution. The following is the list of institutions: (01) LAMONT (LDEO), (02) WOODS HOLE O.I., (03) NOAA, (04) US ARMY, (05) NEW ZEALAND, (06) US GEOL. SURVEY, (07) OREGON ST. UNIV, (08) U.HAWAII SOEST, (09) US NAVY, (10) UNIV OF TEXAS, (11) RICE UNIV., (12) CANADA, (13) UNIV OF CONN., (14) U.MIAMI (RSMAS), (15) SCRIPPS INST.OC, (16) CHINA, (17) U RHODE ISLAND, (18) DUKE UNIVERSITY, (19) UNITED KINGDOM, (20) U.WASHINGTON, (22) WESTERN GEOPHY., (23) TEXAS A&amp;M UNIV., (24) AUSTRALIA, (25) MONACO, (29) RUSSIA, (30) SPAIN, (35) NIMA, (58) NETHERLANDS, (60) MIN MGMT SVC, (63) ISRAEL, (67) FRANCE, (71) SOUTH AFRICA, (75) US COAST GUARD, (76) BRAZIL, (77) INT. GRAV. BUR, (83) GERMANY, (84) ORSTOM NEW CAL, (86) CUBA, (87) ARGENTINA, (88) US NSF, (89) INDIA, (90) PORTUGAL, (92) FINLAND, (93) CHILE, (J1) HYDR DEPT JAPAN, (J2) GEOL SRVY JAPAN, (J4) UNIV TOKYO, (J5) KOBE UNIV, (J7) UNIV OF RYUKYUS, (J8) J.O.D.C. JAPAN, (J9) CHIBA UNIV, (JA) INST.POLAR RES., (ZZ) INST NOT CODED.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
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
<h2>EXAMPLES</h2>
<p> To get one-line summary information about the cruises 01010047.mgd77 and 01010008.mgd77, try </p>
<pre>
gmt mgd77info 01010047 01010008 -E &gt; listing.lis
</pre>
<p> To see the original raw MGD77 header meta-data for cruise 01010047.mgd77, run </p>
<pre>
gmt mgd77info 01010047 -Mr
</pre>
<p> To determine all the parameters related to Gravity during cruise 01010047.mgd77, run </p>
<pre>
gmt mgd77info 01010047 -Mf | grep Gravity
</pre>
<p> To determine the Magnetic sampling rate used during cruise 01010047.mgd77, run </p>
<pre>
gmt mgd77info 01010047 -MfMagnetics_Sampling_Rate
</pre>
<p> To see all the columns that the MGD77+ cruise 01010047.nc contains, run </p>
<pre>
gmt mgd77info 01010047 -C
</pre>
<p> To see the E77 status of all MGD77+ cruises collected by the University of Hawaii (institution 08), run </p>
<pre>
gmt mgd77info 08 -Ia -Me
</pre>
<h2>SEE ALSO</h2>
<p> <code>mgd77list</code>, <code>mgd77manage</code>, <code>mgd77path</code>, <code>mgd77track</code>, <code>x2sys_init</code></p>
<h2>REFERENCES</h2>
<p> The Marine Geophysical Data Exchange Format &#8211; MGD77, see <i><a rel="nofollow" href="http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt.">http://www.ngdc.noaa.gov/mgg/dat/geodas/docs/mgd77.txt.</a></i></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
