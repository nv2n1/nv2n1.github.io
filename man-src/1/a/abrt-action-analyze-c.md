---
title: "abrt-action-analyze-c(1)"
name: "abrt-action-analyze-c"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-c/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-c - Calculate and save UUID for a problem data directory DIR with coredump. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-c</i> [-v] [-d DIR]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>coredump</i> from a problem data directory, processes it and generates a universally unique identifier (UUID). Then it saves this data as new element <i>uuid</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-c</i> can be used to generate the UUID of a newly saved coredump. 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=CCpp   abrt-action-analyze-c
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to a problem directory. Current working directory is used when this option is not provided.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


