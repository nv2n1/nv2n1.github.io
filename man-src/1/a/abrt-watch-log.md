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
</dt><dd> Don't run PROG if STRs aren't found</dd></dl>
 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -s
<dl>
<dt>
</dt><dd> Log to syslog</dd></dl>
 

 FILE
<dl>
<dt>
</dt><dd> Watched file</dd></dl>
 

 PROG
<dl>
<dt>
</dt><dd> Path to an executable</dd></dl>
 

 ARGS
<dl>
<dt>
</dt><dd> Arguments for PROG</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
 

<h2>Index</h2>


