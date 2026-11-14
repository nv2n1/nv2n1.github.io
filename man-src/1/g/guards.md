---
title: "guards(1)"
name: "guards"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guards/"
---

<h2 class="name">NAME</h2>
 

 guards - select from a list of files guarded by conditions 

<h2>SYNOPSIS</h2>

 <i>guards</i> [--prefix=<i>dir</i>] [--path=<i>dir1:dir2:...</i>] [--default=&lt;0|1&gt;] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> [--check|--list] [--invert-match] [--with-guards] [--config=&lt;file&gt;]
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <i>symbol</i> ...

<h2>DESCRIPTION</h2>

 The script reads a configuration file that may contain so-called guards, file names, and comments, and writes those file names that satisfy all guards to standard output. The script takes a list of symbols as its arguments. Each line in the configuration file is processed separately. Lines may start with a number of guards. The following guards are defined: 

<dl>
<dt>
<dd> +<i>xxx</i> Include the file(s) on this line if the symbol <i>xxx</i> is defined. 

 -<i>xxx</i> Exclude the file(s) on this line if the symbol <i>xxx</i> is defined. 

 +!<i>xxx</i> Include the file(s) on this line if the symbol <i>xxx</i> is not defined. 

 -!<i>xxx</i> Exclude the file(s) on this line if the symbol <i>xxx</i> is not defined. 

 - Exclude this file. Used to avoid spurious <i>--check</i> messages.</dl>
 

 The guards are processed left to right. The last guard that matches determines if the file is included. If no guard is specified, the <i>--default</i> setting determines if the file is included. 

 If no configuration file is specified, the script reads from standard input. 

 The <i>--check</i> option is used to compare the specification file against the file system. If files are referenced in the specification that do not exist, or if files are not enlisted in the specification file warnings are printed. The <i>--path</i> option can be used to specify which directory or directories to scan. Multiple directories are separated by a colon (<tt>&quot;:&quot;</tt>) character. The <i>--prefix</i> option specifies the location of the files. 

 Use <i>--list</i> to list all files independent of any rules. Use <i>--invert-match</i> to list only the excluded patches. Use <i>--with-guards</i> to also include all inclusion and exclusion rules.

<h2>AUTHOR</h2>

 Andreas Gruenbacher &lt;agruen [at] suse.de&gt;, <font SIZE="-1">SUSE</font> Labs 

<h2>Index</h2>


