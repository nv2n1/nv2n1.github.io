---
title: "status(1)"
name: "status"
section: "1"
letter: "s"
url: "/docs/linux/man/1-status/"
---

<h2 class="name">NAME</h2>
 

 status - query fish runtime information

<h3>Synopsis</h3>

 status [OPTION]

<h3>Description</h3>

<dl>
<dt>*
<dd> -c or --is-command-substitution returns 0 if fish is currently executing a command substitution
<dt>*
<dd> -b or --is-block returns 0 if fish is currently executing a block of code
<dt>*
<dd> -i or --is-interactive returns 0 if fish is interactive, i.e.connected to a keyboard
<dt>*
<dd> -l or --is-login returns 0 if fish is a login shell, i.e. if fish should perform login tasks such as setting up the PATH.
<dt>*
<dd> --is-full-job-control returns 0 if full job control is enabled
<dt>*
<dd> --is-interactive-job-control returns 0 if interactive job control is enabled
<dt>*
<dd> --is-no-job-control returns 0 if no job control is enabled
<dt>*
<dd> -f or --current-filename prints the filename of the currently running script
<dt>*
<dd> -n or --current-line-number prints the line number of the currently running script
<dt>*
<dd> -j CONTROLTYPE or --job-control=CONTROLTYPE set the job control type. Can be one of: none, full, interactive
<dt>*
<dd> -t or --print-stack-trace prints a stack trace of all function calls on the call stack
<dt>*
<dd> -h or --help display a help message and exit</dl>
 

 

 

<h2>Index</h2>


