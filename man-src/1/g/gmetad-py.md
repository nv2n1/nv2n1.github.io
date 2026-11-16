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
<dt><code>&#8211;version</code></dt>
<dd>show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>show this help message and exit</dd>
<dt><code>-d</code> DEBUG, <code>&#8211;debug</code>=<i>DEBUG</i></dt>
<dd>Debug level. If five (5) or greater, daemon will stay in foreground. Values are: 0 &#8211; FATAL 1 &#8211; CRITICAL 2 &#8211; ERROR (default) 3 &#8211; WARNING 4 &#8211; INFO 5 &#8211; DEBUG</dd>
<dt><code>-p</code> PID_FILE, <code>&#8211;pid_file</code>=<i>PID_FILE</i></dt>
<dd>Write process-id to file</dd>
<dt><code>-c</code> CONF, <code>&#8211;conf</code>=<i>CONF</i></dt>
<dd>Location of gmetad configuration file (default=&#8217;/etc/ganglia/gmetad-python.conf&#8217;)</dd>
<dt><code>-l</code> LOGFILE, <code>&#8211;logfile</code>=<i>LOGFILE</i></dt>
<dd>Log messages to this path in addition to syslog; overrides configuration</dd>
<dt><code>-i</code> INTERACTIVE_PORT, <code>&#8211;interactive_port</code>=<i>INTERACTIVE_PORT</i></dt>
<dd>Interactive port to listen on (default=8652)</dd>
<dt><code>-x</code> XML_PORT, <code>&#8211;xml_port</code>=<i>XML_PORT</i></dt>
<dd>XML port to listen on (default=8651) </dd>
</dl>
