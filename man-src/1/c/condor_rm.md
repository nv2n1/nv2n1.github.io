---
title: "condor_rm(1)"
name: "condor_rm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_rm/"
description: "condor_rm remove jobs from the HTCondor queue"
---

<h2>Name</h2>
<p> <i>condor_rm</i> remove jobs from the HTCondor queue </p>
<h2>Synopsis</h2>
<p> <i>condor_rm</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_rm</i> [ <code>-debug</code> ] [ <code>-forcex</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <i>cluster&#8230; cluster.process&#8230; user&#8230; </i> <code>-constraint </code> <i>expression</i> &#8230; </p>
<p> <i>condor_rm</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <code>-all</code> </p>
<h2>Description</h2>
<p> <i>condor_rm</i> removes one or more jobs from the HTCondor job queue. If the <code>-name</code> option is specified, the named <i>condor_schedd</i> is targeted for processing. Otherwise, the local <i>condor_schedd</i> is targeted. The jobs to be removed are identified by one or more job identifiers, as described below. For any given job, only the owner of the job or one of the queue super users (defined by the QUEUE_SUPER_USERS macro) can remove the job. </p>
<p> When removing a grid job, the job may remain in the &#8220;X&#8221; state for a very long time. This is normal, as HTCondor is attempting to communicate with the remote scheduling system, ensuring that the job has been properly cleaned up. If it takes too long, or in rare circumstances is never removed, the job may be forced to leave the job queue by using the <code>-forcex</code> option. This forcibly removes jobs that are in the &#8220;X&#8221; state without attempting to finish any clean up at the remote scheduler. </p>
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
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>scheddname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>scheddname</i></p>
<dt>
<dd></dl>
<p> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-forcex</code></p>
<dl>
<dt>
<dd> Force the immediate local removal of jobs in the &#8216;X&#8217; state (only affects jobs already being removed)</p>
<dt>
<dd></dl>
<p> <i>cluster</i></p>
<dl>
<dt>
<dd> Remove all jobs in the specified cluster</p>
<dt>
<dd></dl>
<p> <i>cluster.process</i></p>
<dl>
<dt>
<dd> Remove the specific job in the cluster</p>
<dt>
<dd></dl>
<p> <i>user</i></p>
<dl>
<dt>
<dd> Remove jobs belonging to specified user</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Remove all jobs which match the job ClassAd expression constraint</p>
<dt>
<dd></dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Remove all the jobs in the queue</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> Use the <i>-forcex</i> argument with caution, as it will remove jobs from the local queue immediately, but can orphan parts of the job that are running remotely and have not yet been stopped or removed. </p>
<h2>Examples</h2>
<p> For a user to remove all their jobs that are not currently running: </p>
<p> % condor_rm -constraint &#8216;JobStatus =!= 2&#8217; </p>
<h2>Exit Status</h2>
<p> <i>condor_rm</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
