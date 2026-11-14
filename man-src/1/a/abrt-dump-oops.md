---
title: "abrt-dump-oops(1)"
name: "abrt-dump-oops"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-dump-oops/"
---

<h2 class="name">NAME</h2>
 

 abrt-dump-oops - Extract oops from FILE (or standard input) 

<h2>SYNOPSIS</h2>

 

 <i>abrt-dump-oops</i> [-vusoxtm] [-d DIR]/[-D] [FILE]

<h2>DESCRIPTION</h2>

 

 This tool creates problem directory from, updates problem directory with or prints oops extracted from FILE or standard input.

<h2>FILES</h2>

 

 /etc/abrt/plugins/oops.conf
<dl>
<dt>
<dd> Configuration file where user can disable detection of non-fatal MCEs</dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -s
<dl>
<dt>
<dd> Log to syslog</dl>
 

 -o
<dl>
<dt>
<dd> Print found oopses on standard output</dl>
 

 -d DIR
<dl>
<dt>
<dd> Create new problem directory in DIR for every oops found</dl>
 

 -D
<dl>
<dt>
<dd> Same as -d DumpLocation, DumpLocation is specified in abrt.conf</dl>
 

 -u PROBLEM
<dl>
<dt>
<dd> Save the extracted information in PROBLEM directory</dl>
 

 -x
<dl>
<dt>
<dd> Make the problem directory world readable. Usable only with -d/-D</dl>
 

 -t
<dl>
<dt>
<dd> Throttle problem directory creation to 1 per second</dl>
 

 -m
<dl>
<dt>
<dd> Print search string(s) for <i>abrt-watch-log</i> to stdout and exit</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-abrt-watch-log/">abrt-watch-log</a>(1), <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


