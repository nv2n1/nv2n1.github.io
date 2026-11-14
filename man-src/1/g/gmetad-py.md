---
title: "gmetad-py(1)"
name: "gmetad-py"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmetad-py/"
description: "gmetad.py – Ganglia Meta Daemon in Python"
---

<p>gmetad.py &#8211; Ganglia Meta Daemon in Python</p>
<h2>Synopsis</h2>
<p><code>gmetad.py</code> [<i>options</i>]</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-d</code> DEBUG, <code>&#8211;debug</code>=<i>DEBUG</i></p>
<dd>Debug level. If five (5) or greater, daemon will stay in foreground. Values are: 0 &#8211; FATAL 1 &#8211; CRITICAL 2 &#8211; ERROR (default) 3 &#8211; WARNING 4 &#8211; INFO 5 &#8211; DEBUG</p>
<dt><code>-p</code> PID_FILE, <code>&#8211;pid_file</code>=<i>PID_FILE</i></p>
<dd>Write process-id to file</p>
<dt><code>-c</code> CONF, <code>&#8211;conf</code>=<i>CONF</i></p>
<dd>Location of gmetad configuration file (default=&#8217;/etc/ganglia/gmetad-python.conf&#8217;)</p>
<dt><code>-l</code> LOGFILE, <code>&#8211;logfile</code>=<i>LOGFILE</i></p>
<dd>Log messages to this path in addition to syslog; overrides configuration</p>
<dt><code>-i</code> INTERACTIVE_PORT, <code>&#8211;interactive_port</code>=<i>INTERACTIVE_PORT</i></p>
<dd>Interactive port to listen on (default=8652)</p>
<dt><code>-x</code> XML_PORT, <code>&#8211;xml_port</code>=<i>XML_PORT</i></p>
<dd>XML port to listen on (default=8651) </p>
</dl>
