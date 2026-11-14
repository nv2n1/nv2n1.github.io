---
title: "x2sys_put(1)"
name: "x2sys_put"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x2sys_put/"
description: "x2sys_put – Update track index database from track bin file"
---

<h2>NAME</h2>
<p> x2sys_put &#8211; Update track index database from track bin file</p>
<h2>SYNOPSIS</h2>
<p> <code>x2sys_put</code> [ <i>info.tbf</i> ] <i>TAG</i> [ ] [ ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>x2sys_put</code> accepts a track bin-index file created by <code>x2sys_binlist</code> and adds this information about the data tracks to the relevant data base. You may chose to overwrite existing data with new information for older tracks (<code>-F</code>) and even completely remove information for certain tracks (<code>-D</code>). The x2sys <i>TAG</i> must match the tag encoded in the <i>info.tbf</i> file. To inquire about tracks in the data base, use <code>x2sys_get</code>.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>info.tbf</i></p>
<dd> Name of a single track bin file. If not given, <i>stdin</i> will be read.</p>
<dt><code>-T</code><i>TAG</i></p>
<dd> Specify the x2sys <i>TAG</i> which tracks the attributes of this data type.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code></p>
<dd> Delete all tracks found in the track bin file [Default will try to add them as new track entries].</p>
<dt><code>-F</code></p>
<dd> Replace any existing database information for these tracks with the new information in the track bin file [Default refuses to process tracks already in the database].</p>
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
<p> To add the information stored in the track bin-index file latest.tbf to the track data bases associated with the tag MGD77, and replace any exiting information for these tracks, try </p>
<pre>
gmt x2sys_put latest.tbf -F -V -TMGD77
</pre>
<h2>X2SYS DATABASES</h2>
<p> The <code>x2sys_put</code> utility adds new information to the x2sys data bases. These consists of two files: The first file contains a listing of all the tracks that have been added to the system; it is named <i>TAG</i>_tracks.d and is in ASCII format. The second file is named <i>TAG</i>_index.b and is in native binary format. It contains information on which tracks cross each of the bins, and what data sets were observed while crossing the bin. The bins are defined by the and options passed to <code>x2sys_init</code> when the <i>TAG</i> was first initiated. Both data base files are stored in the <code>$X2SYS_HOME</code>/<i>TAG</i> directory. Do not attempt to edit these files by hand.</p>
<h2>SEE ALSO</h2>
<p> <code>x2sys_binlist</code>, <code>x2sys_get</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
