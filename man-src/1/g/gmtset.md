---
title: "gmtset(1)"
name: "gmtset"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtset/"
description: "gmtset – Change individual GMT default parameters"
---

<h2>NAME</h2>
<p> gmtset &#8211; Change individual GMT default parameters</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtset</code> [ | [<code>s</code>|<code>u</code>] | <i>defaultsfile</i> ] [ <code>&#8211;</code>[<code>BJRXxYycp</code>]<i>value</i> ] PARAMETER1 [=] <i>value1</i> PARAMETER2 [=] <i>value2</i> PARAMETER3 [=] <i>value3</i> </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtset</code> will adjust individual GMT defaults settings in the current directory&#8217;s <code>gmt.conf</code> file. If no such file exists one will be created. The main purpose of <code>gmtset</code> is temporarily to change certain parameters inside a shell script, e.g., set the dots-per-inch to 72, run the script, and reset to 1200 dpi. Optionally, you can specify one or more temporary changes directly on any GMT command line with the syntax <code>&#8211;</code><code>-PARAMETER</code>=<i>VALUE</i>; such changes are only in effect for that command and do not permanently change the default settings on disk.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><code>PARAMETER </code><i>value</i></p>
<dd> Provide one or several pairs of parameter/value combinations that you want to modify. For a complete listing of available parameters and their meaning, see the <code>gmt.conf</code> man page.</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code></p>
<dd> Convert a .gmtdefaults4 file created by GMT4 to a <code>gmt.conf</code> file used by GMT5. The original file is retained.</p>
<dt><code>-D</code>[<code>s</code>|<code>u</code>]</p>
<dd> Modify the GMT defaults based on the system settings. Append <code>u</code> for US defaults or <code>s</code> for SI defaults. [<code>-D</code> alone gives the version selected at compile time]</p>
<dt><code>-G</code><i>defaultsfile</i></p>
<dd> Name of specific <code>gmt.conf</code> file to read and modify [Default looks first in current directory, then in your home directory, then in ~/.gmt and finally in the system defaults].</p>
<dt><code>&#8211;</code>[<code>BJRXxYycp</code>]<i>value</i></p>
<dd> Set the expansion of any of these shorthand options.</p>
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
<p> To change annotation font to 12-point Helvetica, select grid-crosses of size 0.1 inch, and set annotation offset to 0.2 cm: </p>
<pre>
gmt set FONT_ANNOT_PRIMARY 12p,Helvetica \
        MAP_GRID_CROSS_SIZE_PRIMARY 0.1i MAP_ANNOT_OFFSET_PRIMARY 0.2c
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code>, <code>gmtdefaults</code>, <code>gmtget</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
