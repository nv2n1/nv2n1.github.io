---
title: "simplevisor(1)"
name: "simplevisor"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simplevisor/"
description: "simplevisor 1.2 – simple daemons supervisor"
---

<h2 class="name">NAME</h2>
<p> simplevisor 1.2 &#8211; simple daemons supervisor </p>
<h2>SYNOPSIS</h2>
<p> <code>simplevisor</code> [&#8211;conf <font SIZE="-1">CONF</font>][&#8211;conftype <font SIZE="-1">CONFTYPE</font>][&#8211;daemon][&#8211;interval <font SIZE="-1">INTERVAL</font>][-h][&#8211;log <font SIZE="-1">LOG</font>][&#8211;logfile <font SIZE="-1">LOGFILE</font>][&#8211;loglevel <font SIZE="-1">LOGLEVEL</font>][&#8211;logname <font SIZE="-1">LOGNAME</font>][-p <font SIZE="-1">PIDFILE</font>][&#8211;store <font SIZE="-1">STORE</font>][&#8211;version] command [path]</p>
<h2>DESCRIPTION</h2>
<p> Simplevisor is a simple daemons supervisor, it is inspired by Erlang <font SIZE="-1">OTP</font> and it can supervise hierarchies of services. </p>
<p> <font SIZE="-1">COMMANDS</font> </p>
<p> If a path is given or only one service entry is given: </p>
<p> for a given X command<br />
&nbsp;<wbr>run the service X command where service is the only entry provided<br />
&nbsp;<wbr>or the entry identified by its path </p>
<p> If a path is given and the root entry is a supervisor: </p>
<p> restart_child<br />
&nbsp;<wbr>tell a running simplevisor process to restart the child identified<br />
&nbsp;<wbr>by the given path;&nbsp;<wbr>it is different from the restart command as<br />
&nbsp;<wbr>described above because, this way, we are sure that the running<br />
&nbsp;<wbr>simplevisor will not attempt to check/start/stop the child while<br />
&nbsp;<wbr>we restart it </p>
<p> If a path is not given and the root entry is a supervisor: </p>
<p> start<br />
&nbsp;<wbr>start the simplevisor process which start the supervision.<br />
&nbsp;<wbr>It can be used with &#8211;daemon if you want it as daemon </p>
<p> stop<br />
&nbsp;<wbr>stop the simplevisor process and all its children, if running </p>
<p> status<br />
&nbsp;<wbr>return the status of the simplevisor process </p>
<p> check<br />
&nbsp;<wbr>return the comparison between the expected state and the actual state.<br />
&nbsp;<wbr>0 -&gt;&nbsp;<wbr>everything is fine<br />
&nbsp;<wbr>1 -&gt;&nbsp;<wbr>warning, not expected </p>
<p> single<br />
&nbsp;<wbr>execute one cycle of supervision and exit.<br />
&nbsp;<wbr>Useful to be run in a cron script </p>
<p> wake_up<br />
&nbsp;<wbr>tell a running simplevisor process to wake up and supervise </p>
<p> stop_supervisor<br />
&nbsp;<wbr>only stop the simplevisor process but not the children </p>
<p> stop_children<br />
&nbsp;<wbr>only stop the children but not the simplevisor process </p>
<p> check_configuration<br />
&nbsp;<wbr>only check the configuration file </p>
<p> pod<br />
&nbsp;<wbr>generate pod format help to be used by pod2man to generate man page </p>
<p> rst<br />
&nbsp;<wbr>generate rst format help to be used in the web doc </p>
<p> help<br />
&nbsp;<wbr>same as -h/&#8211;help, print help page</p>
<h2>OPTIONS</h2>
<p> <code>positional arguments:</code> </p>
<dl>
<dt>
<dd> <code>command</code> check, check_configuration, help, pod, restart, restart_child, rst, single, start, status, stop, stop_children, stop_supervisor, wake_up </p>
<p> <code>path</code> path to a service, subset of commands available: start, stop, status, check, restart</dl>
<p> <code>optional arguments:</code> </p>
<dl>
<dt>
<dd> <code>&#8211;conf </code><font SIZE="-1"><code>CONF</code></font> configuration file </p>
<p> <code>&#8211;conftype </code><font SIZE="-1"><code>CONFTYPE</code></font> configuration file type (default: apache) </p>
<p> <code>&#8211;daemon</code> daemonize, <font SIZE="-1">ONLY</font> with start </p>
<p> <code>&#8211;interval </code><font SIZE="-1"><code>INTERVAL</code></font> interval to wait between supervision cycles (default: 60) </p>
<p> <code>-h, &#8211;help</code> print the help page </p>
<p> <code>&#8211;log </code><font SIZE="-1"><code>LOG</code></font> available: null, file, syslog, stdout (default: stdout) </p>
<p> <code>&#8211;logfile </code><font SIZE="-1"><code>LOGFILE</code></font> log file, <font SIZE="-1">ONLY</font> for file </p>
<p> <code>&#8211;loglevel </code><font SIZE="-1"><code>LOGLEVEL</code></font> log level (default: warning) </p>
<p> <code>&#8211;logname </code><font SIZE="-1"><code>LOGNAME</code></font> log name (default: simplevisor) </p>
<p> <code>-p, &#8211;pidfile </code><font SIZE="-1"><code>PIDFILE</code></font> the pidfile </p>
<p> <code>&#8211;store </code><font SIZE="-1"><code>STORE</code></font> file where to store the state, it is not mandatory, however recommended to store the simplevisor nodes status between restarts </p>
<p> <code>&#8211;version</code> print the program version</dl>
<h2>EXAMPLES</h2>
<p> Create and edit the main configuration file: </p>
<pre>
    ## look for simplevisor.conf.example in the examples.
</pre>
<p> Run it: </p>
<pre>
    simplevisor --conf /path/to/simplevisor.conf start
</pre>
<p> to run it in daemon mode: </p>
<pre>
    simplevisor --conf /path/to/simplevisor.conf --daemon start
</pre>
<p> For other commands: </p>
<pre>
    simplevisor --help
</pre>
<p> Given the example configuration, to start the httpd service: </p>
<pre>
    simplevisor --conf /path/to/simplevisor.conf start svisor1/httpd
</pre>
<h2>AUTHOR</h2>
<p> Massimo Paladin &lt;massimo.paladin [at] gmail.com&gt; </p>
<p> Copyright (C) <font SIZE="-1">CERN 2013-2016</font> </p>
<h2>Index</h2>
