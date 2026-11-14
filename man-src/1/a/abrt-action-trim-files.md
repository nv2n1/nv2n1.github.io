---
title: "abrt-action-trim-files(1)"
name: "abrt-action-trim-files"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-trim-files/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-trim-files - Deletes old problem directories or files in specified directories until they are smaller than specified size. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-trim-files</i> [-v] [-d SIZE:DIR]... [-f SIZE:DIR]... [-p DIR] [FILE]...

<h2>OPTIONS</h2>

 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -d SIZE:DIR
<dl>
<dt>
<dd> Delete problem directories in DIR. SIZE can be suffixed by k,m,g,t to specify kilo,mega,giga,terabytes.</dl>
 

 -f SIZE:DIR
<dl>
<dt>
<dd> Delete files in DIR</dl>
 

 -p DIR
<dl>
<dt>
<dd> Preserve DIR (never consider it for deletion)</dl>
 

 FILE
<dl>
<dt>
<dd> Preserve FILE (never consider it for deletion)</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


