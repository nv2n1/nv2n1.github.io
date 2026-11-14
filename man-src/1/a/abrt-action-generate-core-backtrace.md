---
title: "abrt-action-generate-core-backtrace(1)"
name: "abrt-action-generate-core-backtrace"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-generate-core-backtrace/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-generate-core-backtrace - Generates coredump-level backtrace 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-generate-core-backtrace</i> [-v] [-r] [-d DIR]

<h2>DESCRIPTION</h2>

 

 This tool uses coredump from the file <i>coredump</i> and binary at the path stored in file <i>executable</i> in the problem directory to generate coredump-level backtrace. 

 Coredump-level backtrace resembles ordinary backtrace in that it contains information about call frames present on the stack at the time of the crash. However, it only contains information that can be obtained from the coredump without debugging symbols available - mainly relative addresses of the stored instruction pointers. Such backtrace can still be useful for reporting and reproducing the bug and does not require debugging information files to be installed. 

 The result is saved in the problem directory in a file named <i>core_backtrace</i>.

<h3>Integration with libreport events</h3>

 

 <i>abrt-action-generate-core-backtrace</i> can be used as an analyzer for application crashes which dump core. 

 Example usage in report_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=analyze analyzer=CCpp
        abrt-action-generate-core-backtrace
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to problem directory.</dl>
 

 -r
<dl>
<dt>
<dd> Do not hash function fingerprints. Useful for debugging.</dl>
 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


