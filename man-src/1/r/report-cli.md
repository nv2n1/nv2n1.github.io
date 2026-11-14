---
title: "report-cli(1)"
name: "report-cli"
section: "1"
letter: "r"
url: "/docs/linux/man/1-report-cli/"
---

<h2 class="name">NAME</h2>
 

 report-cli - Work with ABRT problem directories from command line. 

<h2>SYNOPSIS</h2>

 

 <i>report-cli</i> [-vsp] -L[PREFIX] [PROBLEM_DIR] 

 <i>report-cli</i> [-vsp] -e EVENT PROBLEM_DIR 

 <i>report-cli</i> [-vsp] -a[y] PROBLEM_DIR 

 <i>report-cli</i> [-vsp] -c[y] PROBLEM_DIR 

 <i>report-cli</i> [-vsp] -r[y|o|d] PROBLEM_DIR

<h2>DESCRIPTION</h2>

 

 <i>report-cli</i> is a command line tool that manages application crashes and other problems caught by abrtd daemon, or created by other programs using libreport. It enables access to, manipulation of problem data, and reporting.

<h2>OPTIONS</h2>

 

 -L[PREFIX]
<dl>
<dt>
<dd> List possible events [which start with PREFIX]</dl>
 

 -e EVENT
<dl>
<dt>
<dd> Run EVENT on PROBLEM_DIR</dl>
 

 -a, --analyze
<dl>
<dt>
<dd> Run analyze event(s) on PROBLEM_DIR</dl>
 

 -c, --collect
<dl>
<dt>
<dd> Run collect event(s) on PROBLEM_DIR</dl>
 

 -r, --report
<dl>
<dt>
<dd> Analyze, collect and report problem data in PROBLEM_DIR</dl>
 

 -d, --delete
<dl>
<dt>
<dd> Remove PROBLEM_DIR after reporting</dl>
 

 -y, --always
<dl>
<dt>
<dd> Noninteractive: don't ask questions, assume positive answer to all of them</dl>
 

 -o, --report-only
<dl>
<dt>
<dd> With -r: do not run analyzers, run only reporters</dl>
 

 -v, --verbose
<dl>
<dt>
<dd> Be verbose</dl>
 

 -s
<dl>
<dt>
<dd> Log to syslog</dl>
 

 -p
<dl>
<dt>
<dd> Add program names to log</dl>
 

 -V, --version
<dl>
<dt>
<dd> Display version and exit</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


