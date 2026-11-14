---
title: "abrt-merge-pstoreoops(1)"
name: "abrt-merge-pstoreoops"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-merge-pstoreoops/"
---

<h2 class="name">NAME</h2>
 

 abrt-merge-pstoreoops - Scans files for split oops message. Can print and/or delete them. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-merge-pstoreoops</i> [-v] [-od] FILE...

<h2>DESCRIPTION</h2>

 

 This tool takes list of files, reads all of the files, scans them for split oops messages and join oops parts to original oops message.

<h2>OPTIONS</h2>

 

 -o
<dl>
<dt>
<dd> Print found oopses</dl>
 

 -d
<dl>
<dt>
<dd> Delete files with found oopses</dl>
 

 -v, --verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


