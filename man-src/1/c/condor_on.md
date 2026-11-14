---
title: "condor_on(1)"
name: "condor_on"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_on/"
description: "condor_on Start up HTCondor daemons"
---

<h2>Name</h2>
<p> <i>condor_on</i> Start up HTCondor daemons </p>
<h2>Synopsis</h2>
<p> <i>condor_on</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_on</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>hostname</i> <i>hostname</i> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> <i>&lt;a.b.c.d:port&gt;</i> <code>-constraint </code> <i>expression</i> <code>-all</code> ] [ <code>-daemon </code> <i>daemonname</i> ] </p>
<h2>Description</h2>
<p> <i>condor_on</i> starts up a set of the HTCondor daemons on a set of machines. This command assumes that the <i>condor_master</i> is already running on the machine. If this is not the case, <i>condor_on</i> will fail complaining that it cannot find the address of the master. The command <i>condor_on</i> with no arguments or with the <code>-daemon </code> <i>master</i> option will tell the <i>condor_master</i> to start up the HTCondor daemons specified in the configuration variable DAEMON_LIST . If a daemon other than the <i>condor_master</i> is specified with the <code>-daemon</code> option, <i>condor_on</i> starts up only that daemon. </p>
<p> This command cannot be used to start up the <i>condor_master</i> daemon. </p>
<p> For security reasons of authentication and authorization, this command requires ADMINISTRATOR level of access. </p>
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
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>hostname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>hostname</i></p>
<dt>
<dd></dl>
<p> <i>hostname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>hostname</i></p>
<dt>
<dd></dl>
<p> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine&#8217;s master located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Apply this command only to machines matching the given ClassAd <i>expression</i></p>
<dt>
<dd></dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Send the command to all machines in the pool</p>
<dt>
<dd></dl>
<p> <code>-daemon </code> <i>daemonname</i></p>
<dl>
<dt>
<dd> Send the command to the named daemon. Without this option, the command is sent to the <i>condor_master</i> daemon.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_on</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To begin running all daemons (other than <i>condor_master</i> ) given in the configuration variable DAEMON_LIST on the local host: </p>
<p> % condor_on </p>
<p> To start up only the <i>condor_negotiator</i> on two named machines: </p>
<p> % condor_on robin cardinal -daemon negotiator </p>
<p> To start up only a daemon within a pool of machines other than the local pool, use the <code>-pool</code> option. The argument is the name of the central manager for the pool. Note that one or more machines within the pool must be specified as the targets for the command. This command starts up only the <i>condor_schedd</i> daemon on the single machine named <code>cae17</code> within the pool of machines that has <code>condor.cae.wisc.edu</code> as its central manager: </p>
<p> % condor_on -pool condor.cae.wisc.edu -name cae17 -daemon schedd </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
