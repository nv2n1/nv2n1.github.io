---
title: "condor_ping(1)"
name: "condor_ping"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_ping/"
description: "condor_ping Attempt a security negotiation to determine if it succeeds"
---

<h2>Name</h2>
<p> <i>condor_ping</i> Attempt a security negotiation to determine if it succeeds </p>
<h2>Synopsis</h2>
<p> <i>condor_ping</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_ping</i> [ <code>-debug</code> ] [ <code>-address </code> <i>&lt;a.b.c.d:port&gt;</i> ] [ <code>-pool </code> <i>host name</i> ] [ <code>-name </code> <i>daemon name</i> ] [ <code>-type </code> <i>subsystem</i> ] [ <code>-config </code> <i>filename</i> ] [ <code>-quiet | -table | -verbose</code> ] <i>token</i> [ <i>token [&#8230; ]</i> ] </p>
<h2>Description</h2>
<p> <i>condor_ping</i> attempts a security negotiation to discover whether the configuration is set such that the negotiation succeeds. The target of the negotiation is defined by one or a combination of the <code>address</code> , <code>pool</code> , <code>name</code> , or <code>type</code> options. If no target is specified, the default target is the <i>condor_schedd</i> daemon on the local machine. </p>
<p> One or more <i>token</i> s may be listed, thereby specifying one or more authorization level to impersonate in security negotiation. A token is the value ALL , an authorization level, a command name, or the integer value of a command. The many command names and their associated integer values will more likely be used by experts, and they are defined in the file condor_includes/condor_commands.h . </p>
<p> An authorization level may be one of the following strings. If ALL is listed, then negotiation is attempted for each of these possible authorization levels. </p>
<p> <code>READ</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>WRITE</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ADMINISTRATOR</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>SOAP</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>CONFIG</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>OWNER</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>DAEMON</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>NEGOTIATOR</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ADVERTISE_MASTER</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ADVERTISE_STARTD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ADVERTISE_SCHEDD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>CLIENT</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display version information</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Print extra debugging information as the command executes.</p>
<dt>
<dd></dl>
<p> <code>-config </code> <i>filename</i></p>
<dl>
<dt>
<dd> Attempt the negotiation based on the contents of the configuration file contents in file <i>filename</i> .</p>
<dt>
<dd></dl>
<p> <code>-address </code> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Target the given IP address with the negotiation attempt.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>hostname</i></p>
<dl>
<dt>
<dd> Target the given <i>host</i> with the negotiation attempt. May be combined with specifications defined by <code>name</code> and <code>type</code> options.</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>daemonname</i></p>
<dl>
<dt>
<dd> Target the daemon given by <i>daemonname</i> with the negotiation attempt.</p>
<dt>
<dd></dl>
<p> <code>-type </code> <i>subsystem</i></p>
<dl>
<dt>
<dd> Target the daemon identified by <i>subsystem</i> , one of the values of the predefined $(SUBSYSTEM) macro.</p>
<dt>
<dd></dl>
<p> <code>-quiet</code></p>
<dl>
<dt>
<dd> Set exit status only; no output displayed.</p>
<dt>
<dd></dl>
<p> <code>-table</code></p>
<dl>
<dt>
<dd> Output is displayed with one result per line, in a table format.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Display all available output.</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> The example Unix command </p>
<p> condor_ping -address &quot;&lt;127.0.0.1:9618&gt;&quot; -table READ WRITE DAEMON </p>
<p> places double quote marks around the sinful string to prevent the less than and the greater than characters from causing redirect of input and output. The given IP address is targeted with 3 attempts to negotiate: one at the READ authorization level, one at the WRITE authorization level, and one at the DAEMON authorization level. </p>
<h2>Exit Status</h2>
<p> <i>condor_ping</i> will exit with the status value of the negotiation it attempted, where 0 (zero) indicates success, and 1 (one) indicates failure. If multiple security negotiations were attempted, the exit status will be the logical OR of all values. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
