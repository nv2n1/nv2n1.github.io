---
title: "abrt-action-analyze-core(1)"
name: "abrt-action-analyze-core"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-core/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-core - Extracts builds from a core dump 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-core</i> [-v] [-o OUTFILE] -c COREFILE

<h2>DESCRIPTION</h2>

 

 The tool reads a core dump and extracts build ids of loaded modules and prints the list to the standard output if the OUTFILE file is not configured.

<h2>OPTIONS</h2>

 

 -c COREFILE
<dl>
<dt>
<dd> Path to a core dump.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -o OUTFILE
<dl>
<dt>
<dd> Output file</dl>
 

 -h, --help
<dl>
<dt>
<dd> Prints help text</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


