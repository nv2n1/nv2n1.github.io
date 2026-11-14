---
title: "abrt-action-generate-backtrace(1)"
name: "abrt-action-generate-backtrace"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-generate-backtrace/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-generate-backtrace - Analyzes coredump, generates and saves backtrace. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-generate-backtrace</i> [-v] [-d DIR] [-i DIR1[:DIR2]...] [-t NUM]

<h2>DESCRIPTION</h2>

 

 This tool runs <a HREF="/docs/linux/man/1-gdb/">gdb</a>(1) on a file named <i>coredump</i> in problem directory DIR. <a HREF="/docs/linux/man/1-gdb/">gdb</a>(1) generates backtrace and other diagnostic information about the state of the application at the moment when coredump was generated. Then the tool saves it as new element <i>backtrace</i> in this problem directory.

<h3>Integration with libreport events</h3>

 

 <i>abrt-action-generate-backtrace</i> can be used as an analyzer for application crashes which dump core. 

 Example usage in report_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=analyze analyzer=CCpp
        abrt-action-generate-backtrace
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to problem directory.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -i DIR1[:DIR2]
<dl>
<dt>
<dd> Additional debuginfo directories</dl>
 

 -t NUM
<dl>
<dt>
<dd> Kill gdb if it runs for more than NUM seconds</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


