---
title: "x2sys_get(1)"
name: "x2sys_get"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_get/"
description: "x2sys_get – Get track listing from the x2sys track index databases"
---

<h2>NAME</h2>
<p> x2sys_get &#8211; Get track listing from the x2sys track index databases</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_get</code> <i>TAG</i> [ ] [ <i>flags</i> ] [ ] [ [<code>+</code>][<i>list</i>] ] [ <i>flags</i> ] [ [ <i>region</i> ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_get</code> will return the names of the track data files in the x2sys data base for this TAG that match the given requirements. You may choose a specific region and optionally ask only for tracks that meet certain data criteria. Finally, you may select an option to list all possible pairs that might generate crossovers.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Instead of reporting the track names, just output the coordinates of the center of each bin that has at least one track with the specified data.</p>
<dt><code>-D</code></p>
<dd> Only report the track names [Default adds the availability of data for each field].</p>
<dt><code>-F</code><i>flags</i></p>
<dd> Give a comma-separated list of column names (as described in the definition file) that should be present. [Default selects all data columns].</p>
<dt><code>-G</code></p>
<dd> Report data flags (Y or N) for the entire track rather than just for the portion that is inside the region set by <code>-R</code> [Default].</p>
<dt><code>-L</code>[<code>+</code>][<i>list</i>]</p>
<dd> Crossover mode. Return a list of track pairs that should be checked for possible crossovers. The list is determined from the bin-index data base on the assumption that tracks occupying the same bin are very likely to intersect. By default we return all possible pairs in the data base. Append the name of a file with a list of tracks if you want to limit the output to those pairs that involve at least one of the track names in your list. The output is suitable for the <code>-A</code> option in <code>x2sys_cross</code>. By default, only external crossover pairs are listed. Use <code>-L+</code> to include internal pairs in the list.</p>
<dt><code>-N</code><i>flags</i></p>
<dd> Give a comma-separated list of column names (as described in the definition file) that must be absent.</p>
<dt><code>-R</code>[<i>unit</i>]<i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>]</p>
<dd> <i>west</i>, <i>east</i>, <i>south</i>, and <i>north</i> specify the region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively for grid creation, give <code>R</code><i>code</i><i>lon</i>/<i>lat</i>/<i>nx</i>/<i>ny</i>, where <i>code</i> is a 2-character combination of L, C, R (for left, center, or right) and T, M, B for top, middle, or bottom. e.g., BL for lower left. This indicates which point on a rectangular region the <i>lon</i>/<i>lat</i> coordinate refers to, and the grid dimensions <i>nx</i> and <i>ny</i> with grid spacings via <code>-I</code> is used to create the corresponding region. Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid. Using <code>-R</code><i>unit</i> expects projected (Cartesian) coordinates compatible with chosen <code>-J</code> and we inversely project to determine actual rectangular geographic region. For perspective view (<code>-p</code>), optionally append /<i>zmin</i>/<i>zmax</i>. In case of perspective view (<code>-p</code>), a z-range (<i>zmin</i>, <i>zmax</i>) can be appended to indicate the third dimension. This needs to be done only when using the <code>-Jz</code> option, not when using only the <code>-p</code> option. In the latter case a perspective view of the plane is plotted, with no third dimension. For Cartesian data just give <i>xmin/xmax/ymin/ymax</i>. This option limits the tracks to those that fall at least partly inside the specified domain.</p>
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
<p> To find all the tracks associated with the tag MGD77, restricted to occupy a certain region in the south Pacific, and have at least free air anomalies and bathymetry, try </p>
<pre>
gmt x2sys_get -V -TMGD77 -R180/240/-60/-30 -Ffaa,depth
</pre>
<p> To find all the tracks associated with the tag MGD77 that have depth but not twt, try </p>
<pre>
gmt x2sys_get -V -TMGD77 -Fdepth -Nwt
</pre>
<p> To find all the pairs associated with the tag MGD77 that might intersect each other, but only those pairs which involves tracks in your list new.lis, try </p>
<pre>
gmt x2sys_get -V -TMGD77 -Lnew.lis &gt; xpairs.lis
</pre>
<h2>NOTE</h2>
<p> The tracks that are returned all have the requested data (<code>-F</code>) within the specified region (<code>-R</code>). Furthermore, the columns of Y and N for other data types also reflect the content of the track portion within the selected region, unless <code>-G</code> is set.</p>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_cross</code> <code>x2sys_datalist</code>, <code>x2sys_init</code>, <code>x2sys_list</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
