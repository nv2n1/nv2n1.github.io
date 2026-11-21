---

title: "abrt-retrace-client(1)"
name: "abrt-retrace-client"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-retrace-client/"
---

abrt-retrace-client - Handles the communication with Retrace server. 

<i>abrt-retrace-client</i> &lt;operation&gt; [options]

This tool is able to communicate with Retrace server: create a new task, ask about task's status, download log or backtrace of a finished task.

<h3>Integration with libreport events</h3>

 

 <i>abrt-retrace-client</i> can be used as an analyzer for application crashes which dump core. 

 Example usage in report_event.conf: 

<dl>
<dt>
</dt><dd> <pre>
EVENT=analyze analyzer=CCpp
        abrt-retrace-client
</pre></dd></dl>

<h2>OPERATIONS</h2>

 

 create
<dl>
<dt>
</dt><dd> Creates a new task. Prints task ID and password to stdout. Either -d or -c is required.</dd></dl>
 

 status
<dl>
<dt>
</dt><dd> Prints task's status to stdout. Both -t and -p are required.</dd></dl>
 

 log
<dl>
<dt>
</dt><dd> Prints finished task's log to stdout. Both -t and -p are required.</dd></dl>
 

 backtrace
<dl>
<dt>
</dt><dd> Print finished task's backtrace to stdout. Both -t and -p are required.</dd></dl>
 

 batch
<dl>
<dt>
</dt><dd> Runs all operations in one step: creates a new task, periodically asks for status (the period is specified by --status-delay option) and downloads the result when finished. If the task was successful backtrace file is saved, otherwise log is printed to stdout. Either -c or -d is required.</dd></dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
</dt><dd> be verbose</dd></dl>
 

 -s, --syslog
<dl>
<dt>
</dt><dd> log to syslog</dd></dl>
 

 -k, --insecure
<dl>
<dt>
</dt><dd> allow insecure connection to retrace server</dd></dl>
 

 --url URL
<dl>
<dt>
</dt><dd> retrace server URL</dd></dl>
 

 --headers
<dl>
<dt>
</dt><dd> (debug) show received HTTP headers</dd></dl>
 

 -d, --dir DIR
<dl>
<dt>
</dt><dd> read data from ABRT problem directory</dd></dl>
 

 -c, --core COREDUMP
<dl>
<dt>
</dt><dd> read data from coredump</dd></dl>
 

 -l, --status-delay
<dl>
<dt>
</dt><dd> delay for polling operations (seconds)</dd></dl>
 

 --no-unlink
<dl>
<dt>
</dt><dd> (debug) do not delete temporary archive created in /tmp</dd></dl>
 

 -t, --task ID
<dl>
<dt>
</dt><dd> ID of the task on server</dd></dl>
 

 -p, --password PWD
<dl>
<dt>
</dt><dd> password of the task on server</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
