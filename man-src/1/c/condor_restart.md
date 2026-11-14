---
title: "condor_restart(1)"
name: "condor_restart"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_restart/"
description: "condor_restart Restart a set of HTCondor daemons"
---

<h2>Name</h2>
<p> <i>condor_restart</i> Restart a set of HTCondor daemons </p>
<h2>Synopsis</h2>
<p> <i>condor_restart</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_restart</i> [ <code>-debug</code> ] [ <code>-graceful -fast -peaceful</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>hostname</i> <i>hostname</i> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> <i>&lt;a.b.c.d:port&gt;</i> <code>-constraint </code> <i>expression</i> <code>-all</code> ] [ <code>-daemon </code> <i>daemonname</i> ] </p>
<h2>Description</h2>
<p> <i>condor_restart</i> restarts a set of HTCondor daemons on a set of machines. The daemons will be put into a consistent state, killed, and then invoked anew. </p>
<p> If, for example, the <i>condor_master</i> needs to be restarted again with a fresh state, this is the command that should be used to do so. If the DAEMON_LIST variable in the configuration file has been changed, this command is used to restart the <i>condor_master</i> in order to see this change. The <i>condor_reconfigure</i> command cannot be used in the case where the DAEMON_LIST expression changes. </p>
<p> The command <i>condor_restart</i> with no arguments or with the <code>-daemon </code> <i>master</i> option will safely shut down all running jobs and all submitted jobs from the machine(s) being restarted, then shut down all the child daemons of the <i>condor_master</i> , and then restart the <i>condor_master</i> . This, in turn, will allow the <i>condor_master</i> to start up other daemons as specified in the DAEMON_LIST configuration file entry. </p>
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
<p> <code>-graceful</code></p>
<dl>
<dt>
<dd> Gracefully shutdown daemons (the default) before restarting them</p>
<dt>
<dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
<dd> Quickly shutdown daemons before restarting them</p>
<dt>
<dd></dl>
<p> <code>-peaceful</code></p>
<dl>
<dt>
<dd> Wait indefinitely for jobs to finish before shutting down daemons, prior to restarting them</p>
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
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_restart</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To restart the <i>condor_master</i> and all its children on the local host: </p>
<p> % condor_restart </p>
<p> To restart only the <i>condor_startd</i> on a named machine: </p>
<p> % condor_restart -name bluejay -daemon startd </p>
<p> To restart a machine within a pool other than the local pool, use the <code>-pool</code> option. The argument is the name of the central manager for the pool. Note that one or more machines within the pool must be specified as the targets for the command. This command restarts the single machine named <code>cae17</code> within the pool of machines that has <code>condor.cae.wisc.edu</code> as its central manager: </p>
<p> % condor_restart -pool condor.cae.wisc.edu -name cae17 </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
