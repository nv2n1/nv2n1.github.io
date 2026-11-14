---
title: "condor_vacate(1)"
name: "condor_vacate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_vacate/"
description: "condor_vacate Vacate jobs that are running on the specified hosts"
---

<h2>Name</h2>
<p> <i>condor_vacate</i> Vacate jobs that are running on the specified hosts </p>
<h2>Synopsis</h2>
<p> <i>condor_vacate</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_vacate</i> [ <code>-graceful -fast</code> ] [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>hostname</i> <i>hostname</i> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> <i>&lt;a.b.c.d:port&gt;</i> <code>-constraint </code> <i>expression</i> <code>-all</code> ] </p>
<h2>Description</h2>
<p> <i>condor_vacate</i> causes HTCondor to checkpoint any running jobs on a set of machines and force the jobs to vacate the machine. The job(s) remains in the submitting machine&#8217;s job queue. </p>
<p> Given the (default) <code>-graceful</code> option, a job running under the standard universe will first produce a checkpoint and then the job will be killed. HTCondor will then restart the job somewhere else, using the checkpoint to continue from where it left off. A job running under the vanilla universe is killed, and HTCondor restarts the job from the beginning somewhere else. <i>condor_vacate</i> has no effect on a machine with no HTCondor job currently running. </p>
<p> There is generally no need for the user or administrator to explicitly run <i>condor_vacate</i> . HTCondor takes care of jobs in this way automatically following the policies given in configuration files. </p>
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
<dd> Inform the job to checkpoint, then soft-kill it.</p>
<dt>
<dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
<dd> Hard-kill jobs instead of checkpointing them</p>
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
<h2>Exit Status</h2>
<p> <i>condor_vacate</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To send a <i>condor_vacate</i> command to two named machines: </p>
<p> % condor_vacate robin cardinal </p>
<p> To send the <i>condor_vacate</i> command to a machine within a pool of machines other than the local pool, use the <code>-pool</code> option. The argument is the name of the central manager for the pool. Note that one or more machines within the pool must be specified as the targets for the command. This command sends the command to a the single machine named <code>cae17</code> within the pool of machines that has <code>condor.cae.wisc.edu</code> as its central manager: </p>
<p> % condor_vacate -pool condor.cae.wisc.edu -name cae17 </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
