---
title: "gmtwhich(1)"
name: "gmtwhich"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtwhich/"
description: "gmtwhich – Find full path to specified files"
---

<h2>NAME</h2>
<p> gmtwhich &#8211; Find full path to specified files</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtwhich</code> <i>files</i> [ ] [ ] [ ] [ [<i>level</i>] ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtwhich</code> reports the full paths to the files given on the command line. We look for the file in (1) the current directory, (2) in $GMT_USERDIR (if defined), (3) in $GMT_DATADIR (if defined). If found we print the full path name to the file, just the directory (see <code>-D</code>), or a confirmation (see <code>-C</code>). The $GMT_USERDIR and $GMT_DATADIR environment variables can be colon-separated list of directories, and we search recursively down any directory that ends with / (i.e., /export/data is a single directory whereas /export/data/ will be searched recursively.)</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>files</i></p>
<dd> One or more file names of any data type (grids, tables, etc.).</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Only consider files that the user has permission to read [Default consider all files found].</p>
<dt><code>-C</code></p>
<dd> Instead of reporting the paths, print the confirmation Y if the file is found and N if it is not.</p>
<dt><code>-D</code></p>
<dd> Instead of reporting the paths, print the directories that contains the files.</p>
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
<h2>SEE ALSO</h2>
<p> <code>gmt</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
