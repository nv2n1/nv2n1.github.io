---
title: "fc-scan(1)"
name: "fc-scan"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-scan/"
---

<h2 class="name">NAME</h2>
 

 fc-scan - scan font files or directories 

<h2>SYNOPSIS</h2>

 

 <b>fc-scan</b> [ <b>-Vh</b> ] 

 
&nbsp;[&nbsp;<b>&nbsp;[&nbsp;-f&nbsp;</b><i>format</i><b>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;--format&nbsp;</b><i>format</i><b>&nbsp;]&nbsp;</b>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<b>--version</b>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<b>--help</b>&nbsp;]&nbsp;<wbr>&nbsp;<i>file</i><i>...</i>

<h2>DESCRIPTION</h2>

 

 <b>fc-scan</b> scans <i>file</i>(s) recursively and prints out font pattern for each face found.

<h2>OPTIONS</h2>

 

 This program follows the usual GNU command line syntax, with long options starting with two dashes (`-'). A summary of options is included below.
<dl>
<dt><b>-f</b>
<dd> Format output according to the format specifier <i>format</i>.
<dt><b>-V</b>
<dd> Show version of the program and exit.
<dt><b>-h</b>
<dd> Show summary of options.
<dt><i>file</i>
<dd> Scan <i>file</i> recursively for font faces.</dl>

<h2>RETURN CODES</h2>

 

 <b>fc-scan</b> returns error code 0 if at least one font was found or 1 otherwise.

<h2>SEE ALSO</h2>

 

 <b><a HREF="/docs/linux/man/1-fc-query/">fc-query</a></b>(1) <b><a HREF="/docs/linux/man/3-fcfilescan/">FcFileScan</a></b>(3) <b><a HREF="/docs/linux/man/3-fcdirscan/">FcDirScan</a></b>(3) <b><a HREF="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></b>(3) <b><a HREF="/docs/linux/man/1-fc-cat/">fc-cat</a></b>(1) <b><a HREF="/docs/linux/man/1-fc-cache/">fc-cache</a></b>(1) <b><a HREF="/docs/linux/man/1-fc-list/">fc-list</a></b>(1) <b><a HREF="/docs/linux/man/1-fc-match/">fc-match</a></b>(1) <b><a HREF="/docs/linux/man/1-fc-pattern/">fc-pattern</a></b>(1) 

 The fontconfig user's guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.

<h2>AUTHOR</h2>

 

 This manual page was updated by Behdad Esfahbod &lt;behdad [at] behdad.org&gt;. 

<h2>Index</h2>


