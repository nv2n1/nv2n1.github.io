---
title: "condor_hold(1)"
name: "condor_hold"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_hold/"
description: "condor_hold put jobs in the queue into the hold state"
---

<h2>Name</h2>
<p> <i>condor_hold</i> put jobs in the queue into the hold state </p>
<h2>Synopsis</h2>
<p> <i>condor_hold</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_hold</i> [ <code>-debug</code> ] [ <code>-reason </code> <i>reasonstring</i> ] [ <code>-subcode </code> <i>number</i> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <i>cluster&#8230; cluster.process&#8230; user&#8230; </i> <code>-constraint </code> <i>expression</i> &#8230; </p>
<p> <i>condor_hold</i> [ <code>-debug</code> ] [ <code>-reason </code> <i>reasonstring</i> ] [ <code>-subcode </code> <i>number</i> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <code>-all</code> </p>
<h2>Description</h2>
<p> <i>condor_hold</i> places jobs from the HTCondor job queue in the hold state. If the <code>-name</code> option is specified, the named <i>condor_schedd</i> is targeted for processing. Otherwise, the local <i>condor_schedd</i> is targeted. The jobs to be held are identified by one or more job identifiers, as described below. For any given job, only the owner of the job or one of the queue super users (defined by the QUEUE_SUPER_USERS macro) can place the job on hold. </p>
<p> A job in the hold state remains in the job queue, but the job will not run until released with <i>condor_release</i> . </p>
<p> A currently running job that is placed in the hold state by <i>condor_hold</i> is sent a hard kill signal. For a standard universe job, this means that the job is removed from the machine without allowing a checkpoint to be produced first. </p>
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
<p> <code>-reason </code> <i>reasonstring</i></p>
<dl>
<dt>
<dd> Sets the job ClassAd attribute HoldReason to the value given by <i>reasonstring</i> . <i>reasonstring</i> will be delimited by double quote marks on the command line, if it contains space characters.</p>
<dt>
<dd></dl>
<p> <code>-subcode </code> <i>number</i></p>
<dl>
<dt>
<dd> Sets the job ClassAd attribute HoldReasonSubCode to the integer value given by <i>number</i> .</p>
<dt>
<dd></dl>
<p> <i>cluster</i></p>
<dl>
<dt>
<dd> Hold all jobs in the specified cluster</p>
<dt>
<dd></dl>
<p> <i>cluster.process</i></p>
<dl>
<dt>
<dd> Hold the specific job in the cluster</p>
<dt>
<dd></dl>
<p> <i>user</i></p>
<dl>
<dt>
<dd> Hold all jobs belonging to specified user</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Hold all jobs which match the job ClassAd expression constraint (within quotation marks). Note that quotation marks must be escaped with the backslash characters for most shells.</p>
<dt>
<dd></dl>
<p> <i>-all</i></p>
<dl>
<dt>
<dd> Hold all the jobs in the queue</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>See Also</h2>
<p> <i>condor_release</i> </p>
<h2>Examples</h2>
<p> To place on hold all jobs (of the user that issued the <i>condor_hold</i> command) that are not currently running: </p>
<p> % condor_hold -constraint &quot;JobStatus!=2&quot; </p>
<p> Multiple options within the same command cause the union of all jobs that meet either (or both) of the options to be placed in the hold state. Therefore, the command </p>
<p> % condor_hold Mary -constraint &quot;JobStatus!=2&quot; </p>
<p> places all of Mary&#8217;s queued jobs into the hold state, and the constraint holds all queued jobs not currently running. It also sends a hard kill signal to any of Mary&#8217;s jobs that are currently running. Note that the jobs specified by the constraint will also be Mary&#8217;s jobs, if it is Mary that issues this example <i>condor_hold</i> command. </p>
<h2>Exit Status</h2>
<p> <i>condor_hold</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
