---
title: "abrt-retrace-client(1)"
name: "abrt-retrace-client"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-retrace-client/"
---

<h2 class="name">NAME</h2>
 

 abrt-retrace-client - Handles the communication with Retrace server. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-retrace-client</i> &lt;operation&gt; [options]

<h2>DESCRIPTION</h2>

 

 This tool is able to communicate with Retrace server: create a new task, ask about task's status, download log or backtrace of a finished task.

<h3>Integration with libreport events</h3>

 

 <i>abrt-retrace-client</i> can be used as an analyzer for application crashes which dump core. 

 Example usage in report_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=analyze analyzer=CCpp
        abrt-retrace-client
</pre></dl>

<h2>OPERATIONS</h2>

 

 create
<dl>
<dt>
<dd> Creates a new task. Prints task ID and password to stdout. Either -d or -c is required.</dl>
 

 status
<dl>
<dt>
<dd> Prints task's status to stdout. Both -t and -p are required.</dl>
 

 log
<dl>
<dt>
<dd> Prints finished task's log to stdout. Both -t and -p are required.</dl>
 

 backtrace
<dl>
<dt>
<dd> Print finished task's backtrace to stdout. Both -t and -p are required.</dl>
 

 batch
<dl>
<dt>
<dd> Runs all operations in one step: creates a new task, periodically asks for status (the period is specified by --status-delay option) and downloads the result when finished. If the task was successful backtrace file is saved, otherwise log is printed to stdout. Either -c or -d is required.</dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> be verbose</dl>
 

 -s, --syslog
<dl>
<dt>
<dd> log to syslog</dl>
 

 -k, --insecure
<dl>
<dt>
<dd> allow insecure connection to retrace server</dl>
 

 --url URL
<dl>
<dt>
<dd> retrace server URL</dl>
 

 --headers
<dl>
<dt>
<dd> (debug) show received HTTP headers</dl>
 

 -d, --dir DIR
<dl>
<dt>
<dd> read data from ABRT problem directory</dl>
 

 -c, --core COREDUMP
<dl>
<dt>
<dd> read data from coredump</dl>
 

 -l, --status-delay
<dl>
<dt>
<dd> delay for polling operations (seconds)</dl>
 

 --no-unlink
<dl>
<dt>
<dd> (debug) do not delete temporary archive created in /tmp</dl>
 

 -t, --task ID
<dl>
<dt>
<dd> ID of the task on server</dl>
 

 -p, --password PWD
<dl>
<dt>
<dd> password of the task on server</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


