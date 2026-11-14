---
title: "x2sys_list(1)"
name: "x2sys_list"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_list/"
description: "x2sys_list – Extract subset from crossover data base"
---

<h2>NAME</h2>
<p> x2sys_list &#8211; Extract subset from crossover data base</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_list</code> <i>column</i> <i>TAG</i> [ <i>coedbase.txt</i> ] [ <i>asymm_max</i> ] [ ] [ <i>acdhiInNtTvwxyz</i> ] [ [<i>list</i>] ] [ [<i>corrtable</i>] ] [ <i>nx_min</i> ] [ <code>e</code>|<code>i</code> ] [ <i>region</i> ] [ <i>track</i> ] [ [<i>level</i>] ] [ [<i>list</i>] ] [ <code>-bo</code><i>&lt;binary&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_list</code> will read the crossover ASCII data base <i>coedbase.txt</i> (or <i>stdin</i>) and extract a subset of the crossovers based on the other arguments. The output may be ASCII or binary.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>column</i></p>
<dd> Specify which data column you want to process. Crossovers related to this column name must be present in the crossover data base.</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><i>coedbase.txt</i></p>
<dd> The name of the input ASCII crossover error data base as produced by <code>x2sys_cross</code>. If not given we read standard input instead.</p>
<dt><code>-A</code><i>asymm_max</i></p>
<dd> Specifies maximum asymmetry in the distribution of crossovers relative to the mid point in time (or distance, if not time is available). Asymmetry is computed as (n_right &#8211; n_left)/(n_right + n_left), referring the the number of crossovers that falls in the left or right half of the range. Symmetric distributions will have values close to zero. If specified, we exclude tracks whose asymmetry exceeds the specify cutoff in absolute value [1, i.e., include all].</p>
<dt><code>-E</code></p>
<dd> Enhance ASCII output by writing GMT segment headers with name of the two tracks and their total number of cross-overs [no segment headers].</p>
<dt><code>-F</code><i>acdhiInNtTvwxyz</i></p>
<dd> Specify your desired output using any combination of <i>acdhiInNtTvwxyz</i>, in any order. Do not use space between the letters, and note your selection is case-sensitive. The output will be ASCII (or binary, <code>-bo</code>) columns of values. Description of codes: <code>a</code> is the angle (&lt; 90) defined by the crossing tracks, <code>c</code> is crossover value of chosen observation (see <code>-C</code>), <code>d</code> is distance along track, <code>h</code> is heading along track, <code>i</code> is the signed time interval between the visit at the crossover of the two tracks involved, <code>I</code> is same as <code>i</code> but is unsigned, <code>n</code> is the names of the two tracks, <code>N</code> is the id numbers of the two tracks, <code>t</code> is time along track in <i>date</i><code>T</code><i>clock</i> format (NaN if not available), <code>T</code> is elapsed time since start of track along track (NaN if not available), <code>v</code> is speed along track, <code>w</code> is the composite weight, <code>x</code> is <i>x</i>-coordinate (or longitude), <code>y</code> is <i>y</i>-coordinate (or latitude), and <code>z</code> is observed value (see <code>-C</code>) along track. If <code>-S</code> is not specified then <code>d</code>,<code>h</code>,<code>n</code>,<code>N</code>,<code>t</code>,<code>T</code>,<code>v</code> results in two output columns each: first for track one and next for track two (in lexical order of track names); otherwise, they refer to the specified track only (except for <code>n</code>,<code>N</code> which then refers to the other track). The sign convention for <code>c</code>,<code>i</code> is track one minus track two (lexically sorted). Time intervals will be returned according to the <code>TIME_UNIT</code> GMT defaults setting.</p>
<dt><code>-I</code>[<i>list</i>]</p>
<dd> Name of ASCII file with a list of track names (one per record) that should be excluded from consideration [Default includes all tracks].</p>
<dt><code>-L</code>[<i>corrtable</i>]</p>
<dd> Apply optimal corrections to the chosen observable. Append the correction table to use [Default uses the correction table <i>TAG</i>_corrections.txt which is expected to reside in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory]. For the format of this file, see <code>x2sys_solve</code>.</p>
<dt><code>-N</code><i>nx_min</i></p>
<dd> Only report data from pairs that generated at least <i>nx_min</i> crossovers between them [use all pairs].</p>
<dt><code>-Qe</code>|<code>i</code></p>
<dd> Append <code>e</code> for external crossovers or <code>i</code> for internal crossovers only [Default is all crossovers].</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option bases the statistics on those COE that fall inside the specified domain.</p>
<dt><code>-S</code><i>track</i></p>
<dd> Name of a single track. If given we restrict output to those crossovers involving this track [Default output is crossovers involving any track pair].</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-W</code>[<i>list</i>]</p>
<dd> Name of ASCII file with a list of track names and their relative weights (one track per record) that should be used to calculate the composite crossover weight (output code <code>w</code> above). [Default sets weights to 1].</p>
<dt><code>-bo</code>[<i>ncols</i>][<i>type</i>] <i>(more &#8230;)</i></p>
<dd> Select native binary output.</p>
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
<p> To find all the magnetic crossovers associated with the tag MGD77 from the file COE_data.txt, restricted to occupy a certain region in the south Pacific, and return location, time, and crossover value, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -R180/240/-60/-30 -Cmag -Fxytz &gt; mag_coe.txt
</pre>
<p> To find all the faa crossovers globally that involves track 12345678 and output time since start of the year, using a binary double precision format, try </p>
<pre>
gmt x2sys_list COE_data.txt -V -TMGD77 -Cfaa -S12345678 -FTz -bod &gt; faa_coe.b
</pre>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_cross</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_init</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
