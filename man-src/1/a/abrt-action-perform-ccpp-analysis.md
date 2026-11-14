---
title: "abrt-action-perform-ccpp-analysis(1)"
name: "abrt-action-perform-ccpp-analysis"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-perform-ccpp-analysis/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-perform-ccpp-analysis - Allows users to select acceptable way of core dump analysis 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-perform-ccpp-analysis</i> [-h] [-d PROBLEM_DIR]

<h2>DESCRIPTION</h2>

 

 This tool allows user to select between local and remote core dump analysis. The local analysis may require to download huge amount of data but is completely safe. On the contrary the remote analysis only needs to upload the core dump to retrace server but the core dump may contain security sensitive data.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-perform-ccpp-analysis</i> is used in the analyze step when processing C/C++ crashes 

<dl>
<dt>
<dd> <pre>
EVENT=analyze_CCpp analyzer=CCpp
    abrt-action-perform-ccpp-analysis
</pre></dl>

<h2>OPTIONS</h2>

 

 -d, --problem-dir PROBLEM_DIR
<dl>
<dt>
<dd> Problem directory [Default: current directory]</dl>
 

 -h, --help
<dl>
<dt>
<dd> Show help message</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


