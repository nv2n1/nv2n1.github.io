---
title: "abrt-harvest-pstoreoops(1)"
name: "abrt-harvest-pstoreoops"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-harvest-pstoreoops/"
---

<h2 class="name">NAME</h2>
 

 abrt-harvest-pstoreoops - Reconstruct oops from /sys/fs/pstore/* files, create ABRT problems and remove the files 

<h2>SYNOPSIS</h2>

 

 <i>abrt-harvest-pstoreoops</i>

<h2>DESCRIPTION</h2>

 

 This script is meant to be run once at system startup after abrtd is up and running. It scans /sys/fs/pstore/*, reconstructs oops text(s) from these files, creates ABRT problem directories from them, then removes the files (pstore storage is a limited resource).

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-abrt-merge-pstoreoops/">abrt-merge-pstoreoops</a>(1)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


