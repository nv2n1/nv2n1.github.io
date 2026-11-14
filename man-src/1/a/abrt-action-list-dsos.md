---
title: "abrt-action-list-dsos(1)"
name: "abrt-action-list-dsos"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-list-dsos/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-list-dsos - Prints out DSO from mapped memory regions. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-list-dsos</i> [-o OUTFILE] -m PROC_PID_MAP_FILE

<h2>DESCRIPTION</h2>

 

 The tool reads a file containing the mapped memory regions. Output is printed to <i>stdout</i> or <i>file</i>. 

 Output format: 

<dl>
<dt>
<dd> <pre>
%p %n %v %i
</pre></dl>
 

 where 

 <i>%p</i>
<dl>
<dt>
<dd> path to library or binary file, which is mapped in memory region</dl>
 

 <i>%n</i>
<dl>
<dt>
<dd> name, version, release, architecture of package, where <i>%p</i> belongs</dl>
 

 <i>%v</i>
<dl>
<dt>
<dd> vendor of package</dl>
 

 <i>%i</i>
<dl>
<dt>
<dd> installation time</dl>

<h2>OPTIONS</h2>

 

 -o OUTFILE
<dl>
<dt>
<dd> Output file, if not specified, it is printed to <i>stdout</i></dl>
 

 -m PROC_PID_MAP_FILE
<dl>
<dt>
<dd> File containing the mapped memory regions</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


