---
title: "x2sys_binlist(1)"
name: "x2sys_binlist"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_binlist/"
description: "x2sys_binlist – Create bin index listing from track data files"
---

<h2>NAME</h2>
<p> x2sys_binlist &#8211; Create bin index listing from track data files</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_binlist</code> <i>track(s)</i> <i>TAG</i> [ ] [ ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_binlist</code> reads one or more track data files and produces a multisegment ASCII track bin-index file (tbf) with the track name in the header and one data record per bin crossed; these records contain <i>lon</i>, <i>lat</i>, <i>index</i>, <i>flags</i>[, <i>dist</i>], where <i>lon</i>, <i>lat</i> are the coordinates of the center of the bin, the <i>index</i> is the 1-D number of the bin, and <i>flags</i> is a bitflag that describes which data fields were available in this bin. The optional <i>dist</i> requires . The input files can be of any format, which must be described and passed with the<br />
&nbsp;<wbr>option. The bin-index listing is a crude representation of where the track goes and is used by the data archivist to build an x2sys track data base for miscellaneous track queries, such as when needing to determine which tracks should be compared in a crossover analysis. You must run <code>x2sys_init</code> to initialize the tag before you can run the indexing.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>tracks</i></p>
<dd> Can be one or more ASCII, native binary, or COARDS netCDF 1-D data files. To supply the data files via a text file with a list of tracks (one per record), specify the name of the track list after a leading equal-sign (e.g., =tracks.lis). If the names are missing their file extension we will append the suffix specified for this <i>TAG</i>. Track files will be searched for first in the current directory and second in all directories listed in <code>$X2SYS_HOME</code>/<i>TAG</i>/<i>TAG</i>_paths.txt (if it exists). [If <code>$X2SYS_HOME</code> is not set it will default to <code>$GMT_SHAREDIR</code>/x2sys]. (Note: MGD77 files will also be looked for via <code>MGD77_HOME</code>/mgd77_paths.txt and *.gmt files will be searched for via <code>$GMT_SHAREDIR</code>/mgg/gmtfile_paths).</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code></p>
<dd> Calculate the length of track-line segments per bin [Default skips this step]. The length fragments are given as the 5th output column (after the <i>flags</i>). The length units are obtained via the TAB setting (see <code>x2sys_init</code>).</p>
<dt><code>-E</code></p>
<dd> Convert geographic data to a cylindrical equal-area projection prior to binning. Basically, we apply the projection <code>-JY</code><i>lon0</i>/37:04:17.166076/360, where <i>lon0</i> is the mid-longitude of the region. Requires <code>-D</code>, geographical data, and a global region (e.g., <code>-Rg</code> or <code>-Rd</code>). This option is useful for statistics related to track-line density but should not be used when preparing bin-index files for the x2sys track data bases.</p>
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
<p> To create a bin index file from the MGD77 file 01030061.mgd77 using the settings associated with the tag MGD77, do </p>
<pre>
gmt x2sys_binlist 01030061.mgd77 -TMGD77 &gt; 01030061.tbf
</pre>
<p> To create a track bin index file of all MGD77+ files residing in the current directory using the settings associated with the tag MGD77+ and calculate track distances, run </p>
<pre>
gmt x2sys_binlist *.nc -TMGD77+ -D &gt; all.tbf
</pre>
<h2>SEE ALSO</h2>
<p> <code>x2sys_cross</code>, <code>x2sys_datalist</code>, <code>x2sys_get</code>, <code>x2sys_init</code>, <code>x2sys_put</code>, <code>x2sys_report</code>, <code>x2sys_solve</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
