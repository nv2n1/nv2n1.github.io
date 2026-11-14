---
title: "abrt-action-analyze-vmcore(1)"
name: "abrt-action-analyze-vmcore"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-vmcore/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-analyze-vmcore - Extracts the oops message from the kernel core and install the kernel debuginfo if needed 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-analyze-vmcore</i> [-v] [-d PROBLEM_DIR] [--tmpdir=TMPDIR] [--cache=DIR1[:DIR2]]

<h2>DESCRIPTION</h2>

 

 The tool reads the file named <i>vmcore</i> from a problem data directory, processes it and the oops message from it. Then it saves this data as new element <i>backtrace</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-vmcore</i> can be used as an analyzer for critical kernel crashes which dump core. 

 Example usage in report_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=analyze_VMcore analyzer=vmcore
        abrt-action-analyze-vmcore
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
 

 --core=VMCORE
<dl>
<dt>
<dd> Path to vmcore to analyze (Default: ./vmcore)</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


