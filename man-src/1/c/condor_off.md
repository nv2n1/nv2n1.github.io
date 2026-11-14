---
title: "condor_off(1)"
name: "condor_off"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_off/"
description: "condor_off Shutdown HTCondor daemons"
---

<h2>Name</h2>
<p> <i>condor_off</i> Shutdown HTCondor daemons </p>
<h2>Synopsis</h2>
<p> <i>condor_off</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_off</i> [ <code>-graceful -fast -peaceful -force-graceful</code> ] [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>hostname</i> <i>hostname</i> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> <i>&lt;a.b.c.d:port&gt;</i> <code>-constraint </code> <i>expression</i> <code>-all</code> ] [ <code>-daemon </code> <i>daemonname</i> ] </p>
<h2>Description</h2>
<p> <i>condor_off</i> shuts down a set of the HTCondor daemons running on a set of one or more machines. It does this cleanly so that checkpointable jobs may gracefully exit with minimal loss of work. </p>
<p> The command <i>condor_off</i> without any arguments will shut down all daemons except <i>condor_master</i> . The <i>condor_master</i> can then handle both local and remote requests to restart the other HTCondor daemons if need be. To restart HTCondor running on a machine, see the <i>condor_on</i> command. </p>
<p> With the <code>-daemon </code> <i>master</i> option, <i>condor_off</i> will shut down all daemons including the <i>condor_master</i> . Specification using the <code>-daemon</code> option will shut down only the specified daemon. </p>
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
<p> <code>-graceful</code></p>
<dl>
<dt>
<dd> Gracefully shutdown daemons (the default)</p>
<dt>
<dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
<dd> Quickly shutdown daemons. A minimum of the first two characters of this option must be specified, to distinguish it from the <code>-force-graceful</code> command.</p>
<dt>
<dd></dl>
<p> <code>-peaceful</code></p>
<dl>
<dt>
<dd> Wait indefinitely for jobs to finish</p>
<dt>
<dd></dl>
<p> <code>-force-graceful</code></p>
<dl>
<dt>
<dd> Force a graceful shutdown, even after issuing a <code>-peaceful</code> command. A minimum of the first two characters of this option must be specified, to distinguish it from the <code>-fast</code> command.</p>
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
<p> <i>condor_off</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To shut down all daemons (other than <i>condor_master</i> ) on the local host: </p>
<p> % condor_off </p>
<p> To shut down only the <i>condor_collector</i> on three named machines: </p>
<p> % condor_off cinnamon cloves vanilla -daemon collector </p>
<p> To shut down daemons within a pool of machines other than the local pool, use the <code>-pool</code> option. The argument is the name of the central manager for the pool. Note that one or more machines within the pool must be specified as the targets for the command. This command shuts down all daemons except the <i>condor_master</i> on the single machine named <code>cae17</code> within the pool of machines that has <code>condor.cae.wisc.edu</code> as its central manager: </p>
<p> % condor_off -pool condor.cae.wisc.edu -name cae17 </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
