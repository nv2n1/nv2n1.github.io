---
title: "originator(1)"
name: "originator"
section: "1"
letter: "o"
url: "/docs/linux/man/1-originator/"
description: "originator – Associate seamounts with nearest hotspot point sources"
---

<h2>NAME</h2>
<p> originator &#8211; Associate seamounts with nearest hotspot point sources</p>
<h2>SYNOPSIS</h2>
<p> <code>originator</code> [ <i>tables</i> ] [<code>+</code>]<i>rotfile</i> [<code>+</code>]<i>hs_file</i> [ <i>d_km</i> ] [ [<i>flag</i>] ] [ <i>upper_age</i> ] [ <i>r/t</i> ] [ [<i>n_hs</i>] ] [ ] [ [<i>level</i>] ] [ <i>maxdist</i> ] [ ] [ <code>-bi</code><i>&lt;binary&gt;</i> ] [ <code>-di</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>originator</code> reads (longitude, latitude, height, radius, crustal_age) records from <i>tables</i> [or standard input] and uses the given Absolute Plate Motion (APM) stage or total reconstruction rotation file and the list of hotspot locations to determine the most likely origin (hotspot) for each seamount. It does so by calculating flowlines back in time and determining the closest approach to all hotspots. The output consists of the input records with four additional fields added for each of the <i>n_hs</i> closest hotspots. The four fields are the hotspot id (e.g., HWI), the stage id of the flowline segment that came closest, the pseudo-age of the seamount, and the closest distance to the hotspot (in km). See option <code>-:</code> on how to read (latitude, longitude,height, radius, crustal_age) files.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-E</code><i>rotfile</i></p>
<dd> Give file with rotation parameters. This file must contain one record for each rotation; each record must be of the following format: </p>
<p> <i>lon lat tstart [tstop] angle</i> [ <i>khat a b c d e f g df</i> ] </p>
<p> where <i>tstart</i> and <i>tstop</i> are in Myr and <i>lon lat angle</i> are in degrees. <i>tstart</i> and <i>tstop</i> are the ages of the old and young ends of a stage. If <i>tstop</i> is not present in the record then a total reconstruction rotation is expected and <i>tstop</i> is implicitly set to 0 and should not be specified for any of the records in the file. If a covariance matrix <code>C</code> for the rotation is available it must be specified in a format using the nine optional terms listed in brackets. Here, <code>C</code> = (<i>g</i>/<i>khat</i>)*[ <i>a b d; b c e; d e f</i> ] which shows <code>C</code> made up of three row vectors. If the degrees of freedom (<i>df</i>) in fitting the rotation is 0 or not given it is set to 10000. Blank lines and records whose first column contains # will be ignored. You may prepend a leading + to the filename to indicate you wish to invert the rotations. Alternatively, give the filename composed of two plate IDs separated by a hyphen (e.g., PAC-MBL) and we will instead extract that rotation from the GPlates rotation database. We return an error if the rotation cannot be found. Prepend <code>+</code> if you want to invert the rotations prior to use.</p>
<dt><code>-F</code><i>file</i></p>
<dd> Give file with hotspot locations. This file must contain one record for each hotspot to be considered; each record must be of the following format: </p>
<p> lon lat hs_abbrev hs_id r t_off t_on create fit plot name </p>
<p> E.g., for Hawaii this may look like </p>
<p> 205 20 HWI 1 25 0 90 Y Y Y Hawaii </p>
<p> Most applications only need the first 4 columns which thus represents the minimal hotspot information record type. The abbreviation may be maximum 3 characters long. The id must be an integer from 1-32. The positional uncertainty of the hotspot is given by r (in km). The t_off and t_on variables are used to indicate the active time-span of the hotspot. The create, fit, and plot indicators are either Y or N and are used by some programs to indicate if the hotspot is included in the ID-grids used to determine rotations, if the hotspot chain will be used to determine rotations, and if the hotspot should be included in various plots. The name is a 32-character maximum text string with the full hotspot name. Blank lines and records whose first column contains # will be ignored. Prepend <code>+</code> if we should look for hotspot drift tables whose name must be <i>hs_abbrev</i>_drift.txt. Such files may be located in the current directory, the same directory as <i>hs_file</i>, or in the directories pointed to by GMT_DATADIR. If found then we interpolate to get hotspot location as a function of time [fixed].</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-D</code><i>d_km</i></p>
<dd> Sets the flowline sampling interval in km. [Default is 5].</p>
<dt><code>-L</code>[<i>flag</i>]</p>
<dd> Output closest approach for nearest hotspot only (ignores <code>-S</code>). Choose <code>-Lt</code> for (<i>time</i>, <i>dist</i>, <i>z</i>) [Default], <code>-Lw</code> for (<i>omega</i>, <i>dist</i>, <i>z</i>), and <code>-Ll</code> for (lon, lat, time, dist, z). Normally, <i>dist</i> is in km; use upper case modifiers <code>TWL</code> to get <i>dist</i> in spherical degrees.</p>
<dt><code>-N</code><i>upper_age</i></p>
<dd> Set the maximum age to extend the oldest stage back in time [no extension].</p>
<dt><code>-Q</code><i>r/t</i></p>
<dd> Input files only has (<i>x</i>,<i>y</i>,<i>z</i>); specify constant values for <i>r</i>,<i>t</i> that will be implied for each record.</p>
<dt><code>-S</code>[<i>n_hs</i>]</p>
<dd> Set the number of closest hotspots to report [Default is 1].</p>
<dt><code>-T</code></p>
<dd> Truncate seamount ages exceeding the upper age set with <code>-N</code> [no truncation].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code><i>maxdist</i></p>
<dd> Only report those seamounts whose flowlines came within <i>maxdist</i> to any hotspot [Default reports all seamounts].</p>
<dt><code>-Z</code></p>
<dd> Use the hotspot ID number rather than the name tag in output records.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 5 input columns].</p>
<dt><code>-di</code><i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-:</code>[<code>i</code>|<code>o</code>] <i>(more &#8230;)</i></p>
<dd> Swap 1st and 2nd column on input and/or output.</p>
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
<h2>GEODETIC VERSUS GEOCENTRIC COORDIINATES</h2>
<p> All spherical rotations are applied to geocentric coordinates. This means that incoming data points and grids are considered to represent geodetic coordinates and must first be converted to geocentric coordinates. Rotations are then applied, and the final reconstructed points are converted back to geodetic coordinates. This default behavior can be bypassed if the ellipsoid setting <i>PROJ_ELLIPSOID</i> is changed to Sphere.</p>
<h2>EXAMPLES</h2>
<p> To find the likely (hotspot) origins of the seamounts represented by the (x,y,z,r,tc) points in the file seamounts.d, using the DC85.d Euler poles and the pac_hs.d list of possible hotspots, and report the 2 most likely hotspot candidates for each seamount, run </p>
<pre>
gmt originator seamounts.d -S2 -EDC85.d -Fpac_hs.d &gt; origins.d
</pre>
<p> To determine the predicted age of a seamount, distances to the closest hotspot, and echo the observed age given its location, observed age, and a rotation model, try </p>
<pre>
echo &quot;1.55 -8.43 52.3&quot; | gmt originator -FONeill_2005_hotspots.txt \
-EOMS2005_APM_fixed.txt -Q1/120 -Lt
</pre>
<p> where 52.3 Ma is observed age. The output is 70 -95.486 52.3. To repeat the same exercise with a moving hotspot model, try </p>
<pre>
echo &quot;1.55 -8.43 52.3&quot; | gmt originator -F+ONeill_2005_hotspots.txt \
-EOMS2005_APM_smooth.txt -Q1/120 -Lt
</pre>
<p> Now the output is 80 -213.135 52.3. Negative distances means the closest approach was east of the hotspot.</p>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>grdrotater</code>, <code>grdspotter</code>, <code>project</code>, <code>mapproject</code>, <code>backtracker</code>, <code>hotspotter</code></p>
<h2>REFERENCES</h2>
<p> Wessel, P., 1999, &quot;Hotspotting&quot; tools released, EOS Trans. AGU, 80 (29), p. 319.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
