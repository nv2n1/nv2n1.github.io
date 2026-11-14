---
title: "rotconverter(1)"
name: "rotconverter"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rotconverter/"
description: "rotconverter – Manipulate total reconstruction and stage rotations"
---

<h2>NAME</h2>
<p> rotconverter &#8211; Manipulate total reconstruction and stage rotations</p>
<h2>SYNOPSIS</h2>
<p> <code>rotconverter</code> [ <code>+</code>|<code>&#8211;</code> ] <i>rotA</i> [ <code>+</code>|<code>&#8211;</code> <i>rotB</i> ] [ <code>+</code>|<code>&#8211;</code> <i>rotC</i> ] &#8230; [ ] [ ] [ [<i>fact</i>] ] [ <i>out</i> ] [ ] [ ] [ ] [ ] [ ] [ [<i>level</i>] ] [ <code>-h</code><i>&lt;headers&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>rotconverter</code> reads one or more plate motion models (stage or total reconstruction rotations) stored in the given files. If more than one plate motion model is given we will add or subtract them in the order they were listed. The minus sign means we should first transpose the rotation and then add it to the previous rotation. If a file cannot be opened we will attempt to decode the file name as a single rotation whose parameters are separated by slashes.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>rotX</i></p>
<dd> Name of a file with a plate motion model. Separate several files with desired operator (+ or -). The very first file may also have a leading minus operator to imply a transpose. We also recognize filenames of the form A-B, where both A and B are uppercase plate abbreviations as used by GPlates, to indicate we should look up the rotation between the two plates in the GPlates rotation file (e.g., PAC-MBL). If any of the specified rotation models cannot be opened as a file, we will try to decode the file name as <i>lon/lat/tstart</i>[<i>/tstop</i>]/<i>angle</i> for a single rotation given on the command line. The <i>tstop</i> argument is required for stage poles only. For a single total reconstruction rotation without any time information, give <i>lon/lat/angle</i> only.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Indicate that times are actually just opening angles [times in Myr].</p>
<dt><code>-D</code></p>
<dd> Report longitudes use the -180/+180 range [Default is 0/360].</p>
<dt><code>-E</code>[<i>fact</i>]</p>
<dd> Scale opening angles by <i>fact</i> on output [0.5]. Typically used to get half-rates needed for flowlines. Requires stage pole output (see <code>-F</code>).</p>
<dt><code>-F</code><i>out</i></p>
<dd> Specify the output format for rotations. The <i>out</i> flag must be either <code>t</code> or <code>s</code> for total reconstruction or stage rotations, respectively. [Default is <code>-Ft</code> (output contains total reconstruction rotations)].</p>
<dt><code>-G</code></p>
<dd> Output final rotations in the Plates4 format used by GPlates [Default is spotter format].</p>
<dt><code>-N</code></p>
<dd> Place all output poles in the northern hemisphere [Default reports positive rotation angles].</p>
<dt><code>-S</code></p>
<dd> Place all output poles in the southern hemisphere [Default reports positive rotation angles].</p>
<dt><code>-T</code></p>
<dd> Transpose the final result, i.e., change the sign of the rotation angles.</p>
<dt><code>-W</code></p>
<dd> Ensure all output rotations have negative opening angles [Default reports positive rotation angles].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. Report statistics of extracted rotations.</p>
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
<h2>LIMITATIONS</h2>
<p> Note that only one of , , and can be used at the same time.</p>
<h2>EXAMPLES</h2>
<p> To convert the total reconstruction rotations in the file model_total_reconstruction.APM to stage poles, run </p>
<pre>
gmt rotconverter model_total_reconstruction.APM -Fs &gt; model_stages.APM
</pre>
<p> To obtain Nazca motion relative to Pacific hotspots by adding the motion of Nazca relative to a fixed Pacific to the Pacific-Hotspot reference model DC85_stages.d, and report the result as total reconstruction reconstruction poles in the northern hemisphere, try </p>
<pre>
gmt rotconverter DC85_stages.APM + Pac_Naz_stages.RPM -N -Ft &gt; \
                 Naz_HS_total reconstruction.APM
</pre>
<p> To add the final rotations ROT(150.1, 70.5, -20.3) and ROT (145.0, 40.0, 11.4), try </p>
<pre>
gmt rotconverter 150.1/70.5/-20.3 + 145/40/11.4
</pre>
<p> which prints out 157.32, -80.44, 11.97. </p>
<p> To make stage rotations suitable for generating flowlines (fracture zones) from a model of relative plate motions PL1-PL2.RPM, assuming symmetric spreading, try </p>
<pre>
gmt rotconverter PL1-PL2.RPM -E -Fs &gt; PL1-PL2_half.RPM
gmt rotconverter - PL1-PL2.RPM -E -Fs &gt; PL2-PL1_half.RPM
</pre>
<p> To compute rotations for India relative to a fixed Africa using the plate circuit India-Central Indian Basin-Antarctica-Africa, based on the GPlates rotations database, try </p>
<pre>
gmt rotconverter IND-CIB CIB-ANT ANT-AFR &gt; India_Africa.RPM
</pre>
<h2>NOTES</h2>
<p> GMT distributes the EarthByte rotation model Global_EarthByte_230-0Ma_GK07_AREPS.rot. To use an alternate rotation file, create an environmental parameters named <code>GPLATES_ROTATIONS</code> that points to an alternate rotation file.</p>
<h2>SEE ALSO</h2>
<p> <code>backtracker</code>, <code>grdrotater</code>, <code>grdspotter</code>, <code>hotspotter</code>, <code>originator</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
