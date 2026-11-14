---
title: "x2sys_report(1)"
name: "x2sys_report"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_report/"
description: "x2sys_report – Report statistics from crossover data base"
---

<h2>NAME</h2>
<p> x2sys_report &#8211; Report statistics from crossover data base</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_report</code> <i>column</i> <i>TAG</i> [ <i>coedbase.txt</i> ] [ ] [ [<i>list</i>] ] [ [<i>corrtable</i>] ] [ <i>nx_min</i> ] [ <code>e</code>|<code>i</code> ] [ [ <i>region</i> ] [ <i>track</i> ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_report</code> will read the input crossover ASCII data base <i>coedbase.txt</i> (or <i>stdin</i>) and report on the statistics of crossovers (<i>n</i>, <i>mean</i>, <i>stdev</i>, <i>rms</i>, <i>weight</i>) for each track. Options are available to let you exclude tracks and limit the output.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>coedbase.txt</i></p>
<dd> The name of the input ASCII crossover error data base as produced by <code>x2sys_cross</code>. If not given we read standard input instead.</p>
<dt><code>-C</code><i>column</i></p>
<dd> Specify which data column you want to process. Crossovers related to this column name must be present in the crossover data base.</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Eliminate COEs by distributing the COE between the two tracks in proportion to track weight and producing (dist, adjustment) spline knots files for each track (for the selected <i>column</i>). Such adjustments may be used by <code>x2sys_datalist</code>. The adjustment files are called <i>track.column</i>.adj and are placed in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory. For background information on how these adjustments are designed, see <i>Mittal</i> [1984].</p>
<dt><code>-I</code>[<i>list</i>]</p>
<dd> Name of ASCII file with a list of track names (one per record) that should be excluded from consideration [Default includes all tracks].</p>
<dt><code>-L</code>[<i>corrtable</i>]</p>
<dd> Apply optimal corrections to the chosen observable. Append the correction table to use [Default uses the correction table <i>TAG</i>_corrections.txt which is expected to reside in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory]. For the format of this file, see <code>x2sys_solve</code>.</p>
<dt><code>-N</code><i>nx_min</i></p>
<dd> Only report data from tracks involved in at least <i>nx_min</i> crossovers [all tracks].</p>
<dt><code>-Qe</code>|<code>i</code></p>
<dd> Append <code>e</code> for external crossovers or <code>i</code> for internal crossovers only [Default is external].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option bases the statistics on those COE that fall inside the specified domain.</p>
<dt><code>-S</code><i>track</i></p>
<dd> Name of a single track. If given we restrict output to those crossovers involving this track [Default output is crossovers involving any track pair].</p>
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
<p> To report statistics of all the external magnetic crossovers associated with the tag MGD77 from the file COE_data.txt, restricted to occupy a certain region in the south Pacific, try </p>
<pre>
gmt x2sys_report COE_data.txt -V -TMGD77 -R180/240/-60/-30 -Cmag &gt;
                 mag_report.txt
</pre>
<p> To report on the faa crossovers globally that involves track 12345678, try </p>
<pre>
gmt x2sys_report COE_data.txt -V -TMGD77 -Cfaa -S2345678 &gt; faa_report.txt
</pre>
<h2>REFERENCES</h2>
<p> Mittal, P. K. (1984), Algorithm for error adjustment of potential field data along a survey network, <i>Geophysics</i>, <code><a href="/docs/linux/man/4-49/">49</a></code>(4), 467-469.</p>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code> <code>x2sys_cross</code> <code>x2sys_datalist</code> <code>x2sys_get</code> <code>x2sys_init</code> <code>x2sys_list</code> <code>x2sys_put</code> <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
