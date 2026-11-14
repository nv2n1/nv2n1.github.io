---
title: "fslint-gui(1)"
name: "fslint-gui"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fslint-gui/"
description: "fslint-gui – A GUI wrapper for the individual fslint command line tools"
---

<h2>NAME</h2>
<p> fslint-gui &#8211; A GUI wrapper for the individual fslint command line tools</p>
<h2>SYNOPSIS</h2>
<p> <code>fslint-gui</code> [<i>OPTIONS</i>] [<i>PATHS</i>]</p>
<h2>DESCRIPTION</h2>
<p> fslint is a toolset to find various problems with filesystems, including duplicate files and problematic filenames etc. </p>
<p> Individual command line tools are available in addition to the GUI and to access them, one can change to, or add to $PATH the /usr/share/fslint/fslint directory on a standard install. Each of these commands in that directory have a &#8211;help option which further details its parameters. </p>
<p> <code>findup</code> &#8211; find DUPlicate files </p>
<p> <code>findnl</code> &#8211; find Name Lint (problems with filenames) </p>
<p> <code>findu8</code> &#8211; find filenames with invalid utf8 encoding </p>
<p> <code>findbl</code> &#8211; find Bad Links (various problems with symlinks) </p>
<p> <code>findsn</code> &#8211; find Same Name (problems with clashing names) </p>
<p> <code>finded</code> &#8211; find Empty Directories </p>
<p> <code>findid</code> &#8211; find files with dead user IDs </p>
<p> <code>findns</code> &#8211; find Non Stripped executables </p>
<p> <code>findrs</code> &#8211; find Redundant Whitespace in files </p>
<p> <code>findtf</code> &#8211; find Temporary Files </p>
<p> <code>findul</code> &#8211; find possibly Unused Libraries </p>
<p> <code>zipdir</code> &#8211; Reclaim wasted space in ext2 directory entries</p>
<h2>PARAMETERS</h2>
<p> If [PATHS] are specified, they become the default search path, otherwise the current directory becomes the default.</p>
<dl>
<dt><code>-f</code></p>
<dd> always print full paths even if only a single path is specified</p>
<dt><code>-r</code></p>
<dd> turn OFF recursion</p>
<dt><code>&#8211;version</code></p>
<dd> Display the fslint version and exit</p>
<dt><code>&#8211;help</code></p>
<dd> Display help for tool specific options</dl>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;P@draigBrady.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2009 Padraig Brady &lt;P@draigBrady.com&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details, which is available at <a rel="nofollow" href="http://www.gnu.org">www.gnu.org</a> </p>
<h2>Index</h2>
