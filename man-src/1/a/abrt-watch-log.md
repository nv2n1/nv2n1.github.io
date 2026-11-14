---
title: "abrt-watch-log(1)"
name: "abrt-watch-log"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-watch-log/"
---

<h2 class="name">NAME</h2>
 

 abrt-watch-log - Watch log file and run command when it grows or is replaced 

<h2>SYNOPSIS</h2>

 

 <i>abrt-watch-log</i> [-vs] [-F STR] ... FILE PROG [ARGS]

<h2>OPTIONS</h2>

 

 -F STR
<dl>
<dt>
<dd> Don't run PROG if STRs aren't found</dl>
 

 -v, --verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -s
<dl>
<dt>
<dd> Log to syslog</dl>
 

 FILE
<dl>
<dt>
<dd> Watched file</dl>
 

 PROG
<dl>
<dt>
<dd> Path to an executable</dl>
 

 ARGS
<dl>
<dt>
<dd> Arguments for PROG</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


