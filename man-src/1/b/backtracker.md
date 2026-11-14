---
title: "backtracker(1)"
name: "backtracker"
section: "1"
letter: "b"
url: "/docs/linux/man/1-backtracker/"
description: "backtracker – Generate forward and backward flowlines and hotspot tracks"
---

<h2>NAME</h2>
<p> backtracker &#8211; Generate forward and backward flowlines and hotspot tracks</p>
<h2>SYNOPSIS</h2>
<p> <code>backtracker</code> [ <i>table</i> ] <i>rot_file</i>|<i>lon</i>/<i>lat</i>/<i>angle</i> [ [<i>young</i>/<i>old</i>] ] [ <code>f</code>|<code>b</code> ] [ <i>drift.txt</i> ] [ <code>f</code>|<code>b</code><i>step</i> ] [ <i>upper_age</i> ] [ <i>fixed_age</i> ] [ <i>filestem</i> ] [ <i>zero_age</i> ] [ [<i>level</i>] ] [ [<code>a</code>|<code>t</code>] ] [ <code>-b</code><i>&lt;binary&gt;</i> ] [ <code>-d</code><i>&lt;nodata&gt;</i> ] [ <code>-h</code><i>&lt;headers&gt;</i> ] [ <code>-i</code><i>&lt;flags&gt;</i> ] [ <code>-o</code><i>&lt;flags&gt;</i> ] [ <code>-:</code>[<code>i</code>|<code>o</code>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>backtracker</code> reads (longitude, latitude, age) positions from <i>infiles</i> [or standard input] and computes rotated (x,y,t) coordinates using the specified rotation parameters. It can either calculate final positions [Default] or create a sampled track (flowline or hotspot track) between the initial and final positions. The former mode allows additional data fields after the first 3 columns which must have (longitude,latitude,age). See option <code>-:</code> on how to read (latitude,longitude,age) files.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-E</code><i>rotfile</i></p>
<dd> Give file with rotation parameters. This file must contain one record for each rotation; each record must be of the following format: </p>
<p> <i>lon lat tstart [tstop] angle</i> [ <i>khat a b c d e f g df</i> ] </p>
<p> where <i>tstart</i> and <i>tstop</i> are in Myr and <i>lon lat angle</i> are in degrees. <i>tstart</i> and <i>tstop</i> are the ages of the old and young ends of a stage. If <i>tstop</i> is not present in the record then a total reconstruction rotation is expected and <i>tstop</i> is implicitly set to 0 and should not be specified for any of the records in the file. If a covariance matrix <code>C</code> for the rotation is available it must be specified in a format using the nine optional terms listed in brackets. Here, <code>C</code> = (<i>g</i>/<i>khat</i>)*[ <i>a b d; b c e; d e f</i> ] which shows <code>C</code> made up of three row vectors. If the degrees of freedom (<i>df</i>) in fitting the rotation is 0 or not given it is set to 10000. Blank lines and records whose first column contains # will be ignored. You may prepend a leading + to the filename to indicate you wish to invert the rotations. Alternative 1: Give the filename composed of two plate IDs separated by a hyphen (e.g., PAC-MBL) and we will instead extract that rotation from the GPlates rotation database. We return an error if the rotation cannot be found. Alternative 2: Specify <i>lon</i>/<i>lat</i>/<i>angle</i>, i.e., the longitude, latitude, and opening angle (all in degrees and separated by /) for a single total reconstruction rotation.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>table</i></p>
<dd> One or more ASCII (or binary, see <code>-bi</code>[<i>ncols</i>][<i>type</i>]) data table file(s) holding a number of data columns. If no tables are given then we read from standard input.</p>
<dt><code>-A</code>[<i>young</i>/<i>old</i>]</p>
<dd> Used in conjunction with <code>-Lb</code>|<code>f</code> to limit the track output to those sections whose predicted ages lie between the specified <i>young</i> and <i>old</i> limits. If <code>-LB</code>|<code>F</code> is used instead then the limits apply to the stage ids (id 1 is the youngest stage). If no limits are specified then individual limits for each record are expected in columns 4 and 5 of the input file.</p>
<dt><code>-Df</code>|<code>b</code></p>
<dd> Set the direction to go: <code>-Df</code> will go backward in time (from younger to older positions), while <code>-Db</code> will go forward in time (from older to younger positions) [Default]. Note: For <code>-Db</code> you are specifying the age at the given location, whereas for <code>-Df</code> you are not; instead you specify the age at the reconstructed point.</p>
<dt><code>-F</code><i>drift.txt</i></p>
<dd> Supply a file with lon, lat, age records that describe the history of hotspot motion for the current hotspot. The reconstructions will only use the 3rd data input column (i.e., the age) to obtain the location of the hotspot at that time, via an interpolation of the hotspot motion history. This adjusted location is then used to reconstruct the point or path [No drift].</p>
<dt><code>-Lf</code>|<code>b</code><i>step</i></p>
<dd> Specify a sampled path between initial and final position: <code>-Lf</code> will draw particle flowlines, while <code>-Lb</code> will draw backtrack (hotspot track) paths. Append sampling interval in km. If <i>step</i> &lt; 0 then only the rotation times will be returned. When <code>-LF</code> or <code>-LB</code> is used, the third output column will contain the stage id (1 is youngest) [Default is along-track predicted ages]. You can control the direction of the paths by using <code>-D</code>.</p>
<dt><code>-N</code><i>upper_age</i></p>
<dd> Set the maximum age to extend the oldest stage rotation back in time [Default is no extension].</p>
<dt><code>-Q</code><i>fixed_age</i></p>
<dd> Assign a fixed age to all positions. Only lon, lat input is expected [Default expects longitude, latitude, age]. Useful when the input are points defining isochrons.</p>
<dt><code>-S</code><i>filestem</i></p>
<dd> When <code>-L</code> is set, the tracks are normally written to <i>stdout</i> as a multisegment file. Specify a <i>filestem</i> to have each track written to <i>filestem.#</i>, where <i>#</i> is the track number. The track number is also copied to the 4th output column.</p>
<dt><code>-T</code><i>zero_age</i></p>
<dd> Set the current time [Default is 0 Ma].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<code>a</code>|<code>t</code>]</p>
<dd> Rotates the given input (lon,lat,t) and calculates the confidence ellipse for the projected point. The input point <i>must</i> have a time coordinate that exactly matches a particular total reconstruction rotation time, otherwise the point will be skipped. Append <code>t</code> or <code>a</code> to output time or angle, respectively, after the projected lon, lat. After these 2-3 items, we write azimuth, major, minor (in km) for the 95% confidence ellipse. See <code>-D</code> for the direction of rotation.</p>
<dt><code>-bi</code>[<i>ncols</i>][<code>t</code>] <i>(more &#8230;)</i></p>
<dd> Select native binary input. [Default is 3 input columns].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output. [Default is same as input].</p>
<dt><code>-d</code>[<code>i</code>|<code>o</code>]<i>nodata</i> <i>(more &#8230;)</i></p>
<dd> Replace input columns that equal <i>nodata</i> with NaN and do the reverse on output.</p>
<dt><code>-h</code>[<code>i</code>|<code>o</code>][<i>n</i>][<code>+c</code>][<code>+d</code>][<code>+r</code><i>remark</i>][<code>+r</code><i>title</i>] <i>(more &#8230;)</i></p>
<dd> Skip or produce header record(s).</p>
<dt><code>-i</code><i>cols</i>[<code>l</code>][<code>s</code><i>scale</i>][<code>o</code><i>offset</i>][,<i>&#8230;</i>] <i>(more &#8230;)</i></p>
<dd> Select input columns (0 is first column).</p>
<dt><code>-o</code><i>cols</i>[,&#8230;] <i>(more &#8230;)</i></p>
<dd> Select output columns (0 is first column).</p>
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
<p> To backtrack the (x,y,t) points in the file seamounts.txt to their origin (presumably the hotspot), using the DC85.txt Euler poles, run </p>
<pre>
gmt backtracker seamounts.txt -Db -EDC85.txt &gt; newpos.txt
</pre>
<p> To project flowlines forward from the (x,y,t) points stored in several 3-column, binary, double precision files, run </p>
<pre>
gmt backtracker points.gmt \* -Df -EDC85.txt -Lf25 -bo -bi3 &gt; lines.b
</pre>
<p> This file can then be plotted with <code>psxy</code>. To compute the predicted Hawaiian hotspot track from 0 to 80 Ma every 1 Ma, given a history of hotspot motion file (HIdrift.txt) and a set of total reconstruction rotations for the plate (PAC_APM.txt), try </p>
<pre>
echo 204 19 80 | gmt backtracker -Df -EPAC_APM.txt -Lb1 &gt; path.txt
</pre>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code> , <code>project</code> , <code>grdrotater</code>, <code>grdspotter</code>, <code>mapproject</code>, <code>hotspotter</code>, <code>originator</code></p>
<h2>REFERENCES</h2>
<p> Wessel, P., 1999, &quot;Hotspotting&quot; tools released, EOS Trans. AGU, 80 (29), p. 319.</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
