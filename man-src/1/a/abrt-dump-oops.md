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
</dt><dd> Configuration file where user can disable detection of non-fatal MCEs</dd></dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -s
<dl>
<dt>
</dt><dd> Log to syslog</dd></dl>
 

 -o
<dl>
<dt>
</dt><dd> Print found oopses on standard output</dd></dl>
 

 -d DIR
<dl>
<dt>
</dt><dd> Create new problem directory in DIR for every oops found</dd></dl>
 

 -D
<dl>
<dt>
</dt><dd> Same as -d DumpLocation, DumpLocation is specified in abrt.conf</dd></dl>
 

 -u PROBLEM
<dl>
<dt>
</dt><dd> Save the extracted information in PROBLEM directory</dd></dl>
 

 -x
<dl>
<dt>
</dt><dd> Make the problem directory world readable. Usable only with -d/-D</dd></dl>
 

 -t
<dl>
<dt>
</dt><dd> Throttle problem directory creation to 1 per second</dd></dl>
 

 -m
<dl>
<dt>
</dt><dd> Print search string(s) for <i>abrt-watch-log</i> to stdout and exit</dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-abrt-watch-log/">abrt-watch-log</a>(1), <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
