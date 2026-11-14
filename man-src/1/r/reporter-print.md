---
title: "reporter-print(1)"
name: "reporter-print"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-print/"
---

<h2 class="name">NAME</h2>
 

 reporter-print - Prints problem information to standard output or FILE. 

<h2>SYNOPSIS</h2>

 

 <i>reporter-print</i> [-v] [-d DIR] [-o FILE] [-a yes/no] [-r]

<h2>DESCRIPTION</h2>

 

 The tool reads problem directory DIR and prints its text representation to stdout or to a specified FILE.

<h3>Integration with ABRT events</h3>

 

 <i>reporter-print</i> can be used as a reporter, to allow users to report problems by writing them to a file. Example: 

<dl>
<dt>
<dd> <pre>
EVENT=report  reporter-print -o &quot;${Log_File:-/tmp/abrt.log}&quot;
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
 

 -o FILE
<dl>
<dt>
<dd> Output file</dl>
 

 -a yes/no
<dl>
<dt>
<dd> If -o FILE is specified, controls whether FILE is appended to, or overwritten. (default: no)</dl>
 

 -r
<dl>
<dt>
<dd> Add a record to <i>reported_to</i> in DIR which specifies that this problem was reported. Some tools use this to differentiate between problems which were and weren't yet reported.</dl>

<h3>Output format</h3>

 

 The output is designed to be machine-parsable. The elements which have only one line are printed in the form 

<dl>
<dt>
<dd> <pre>
NAME:&lt;whitespace&gt;VALUE
</pre></dl>
 

 Elements which have more than one line are printed in the form 

<dl>
<dt>
<dd> <pre>
NAME:
:LINE1
:LINE2
:LINE3
</pre></dl>
 

 Output may contain empty lines for better readability.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-print_event-conf/">print_event.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


