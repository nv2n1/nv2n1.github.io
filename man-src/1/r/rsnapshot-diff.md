---
title: "rsnapshot-diff(1)"
name: "rsnapshot-diff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsnapshot-diff/"
---

<h2 class="name">NAME</h2>
 

 rsnapshot-diff - a utility for comparing the disk usage of two snapshots taken by rsnapshot 

<h2>SYNOPSIS</h2>

 rsnapshot-diff [-h|vVi] dir1 dir2

<h2>DESCRIPTION</h2>

 rsnapshot-diff is a companion utility for rsnapshot, which traverses two parallel directory structures and calculates the difference between them. By default it is silent apart from displaying summary information at the end, but it can be made more verbose. 

 In the summary, ``added'' files may very well include files which at first glance also appear at the same place in the older directory structure. However, because the files differ in some respect, they are different files. They have a different inode number. Consequently if you use -v most of its output may appear to be pairs of files with the same name being removed and added.

<h2>OPTIONS</h2>

<dl>
<dt>-h (help)
<dd> Displays help information
<dt>-H (human)
<dd> Display more human-friendly numbers - as well as showing the number of bytes changed, also show <font SIZE="-1">MB</font> and <font SIZE="-1">GB.</font>
<dt>-i (ignore)
<dd> If verbosity is turned on, -i suppresses information about symlinks, directories, and special files.
<dt>-s (show size)
<dd> Show the size of each changed file after the + or - sign. To sort the files by decreasing size, use this option and run the output through ``sort -k 2 -rn''.
<dt>-v (verbose)
<dd> Be verbose. This will spit out a list of all changes as they are encountered, apart from symlink, as well as the summary at the end.
<dt>-V (more verbose)
<dd> Be more verbose - as well as listing changed files, unchanged files and symlinks will be listed too.
<dt>dir1 and dir2
<dd> These are the only compulsory parameters, and should be the names of two directories to compare. Their order doesn't matter, rsnapshot-diff will always compare the younger to the older, so files that appear only in the older will be reported as having been removed, and files that appear only in the younger will be reported as having been added.</dl>

<h2>SEE ALSO</h2>

 rsnapshot

<h2>BUGS</h2>

 Please report bugs (and other comments) to the rsnapshot-discuss mailing list: 

 &lt;<a rel="nofollow" HREF="http://lists.sourceforge.net/lists/listinfo/rsnapshot-discuss">http://lists.sourceforge.net/lists/listinfo/rsnapshot-discuss</a>&gt;

<h2>AUTHOR</h2>

 David Cantrell &lt;david [at] cantrell.org.uk&gt;

<h2>COPYRIGHT</h2>

 Copyright 2005-2010 David Cantrell

<h2>LICENCE</h2>

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font> 

<h2>Index</h2>


