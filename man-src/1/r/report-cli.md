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
</dt><dd> List possible events [which start with PREFIX]</dd></dl>
 

 -e EVENT
<dl>
<dt>
</dt><dd> Run EVENT on PROBLEM_DIR</dd></dl>
 

 -a, --analyze
<dl>
<dt>
</dt><dd> Run analyze event(s) on PROBLEM_DIR</dd></dl>
 

 -c, --collect
<dl>
<dt>
</dt><dd> Run collect event(s) on PROBLEM_DIR</dd></dl>
 

 -r, --report
<dl>
<dt>
</dt><dd> Analyze, collect and report problem data in PROBLEM_DIR</dd></dl>
 

 -d, --delete
<dl>
<dt>
</dt><dd> Remove PROBLEM_DIR after reporting</dd></dl>
 

 -y, --always
<dl>
<dt>
</dt><dd> Noninteractive: don't ask questions, assume positive answer to all of them</dd></dl>
 

 -o, --report-only
<dl>
<dt>
</dt><dd> With -r: do not run analyzers, run only reporters</dd></dl>
 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be verbose</dd></dl>
 

 -s
<dl>
<dt>
</dt><dd> Log to syslog</dd></dl>
 

 -p
<dl>
<dt>
</dt><dd> Add program names to log</dd></dl>
 

 -V, --version
<dl>
<dt>
</dt><dd> Display version and exit</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
 

<h2>Index</h2>


