---
title: "condor_vacate_job(1)"
name: "condor_vacate_job"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_vacate_job/"
description: "condor_vacate_job vacate jobs in the HTCondor queue from the hosts where they are running"
---

<h2>Name</h2>
<p> <i>condor_vacate_job</i> vacate jobs in the HTCondor queue from the hosts where they are running </p>
<h2>Synopsis</h2>
<p> <i>condor_vacate_job</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_vacate_job</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] [ <code>-fast</code> ] <i>cluster&#8230; cluster.process&#8230; user&#8230; </i> <code>-constraint </code> <i>expression</i> &#8230; </p>
<p> <i>condor_vacate_job</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] [ <code>-fast</code> ] <code>-all</code> </p>
<h2>Description</h2>
<p> <i>condor_vacate_job</i> finds one or more jobs from the HTCondor job queue and vacates them from the host(s) where they are currently running. The jobs remain in the job queue and return to the idle state. </p>
<p> A job running under the standard universe will first produce a checkpoint and then the job will be killed. HTCondor will then restart the job somewhere else, using the checkpoint to continue from where it left off. A job running under any other universe will be sent a soft kill signal (SIGTERM by default, or whatever is defined as the SoftKillSig in the job ClassAd), and HTCondor will restart the job from the beginning somewhere else. </p>
<p> If the <code>-fast</code> option is used, the job(s) will be immediately killed, meaning that standard universe jobs will not be allowed to checkpoint, and the job will have to revert to the last checkpoint or start over from the beginning. </p>
<p> If the <code>-name</code> option is specified, the named <i>condor_schedd</i> is targeted for processing. If the <code>-addr</code> option is used, the <i>condor_schedd</i> at the given address is targeted for processing. Otherwise, the local <i>condor_schedd</i> is targeted. The jobs to be vacated are identified by one or more job identifiers, as described below. For any given job, only the owner of the job or one of the queue super users (defined by the QUEUE_SUPER_USERS macro) can vacate the job. </p>
<p> Using <i>condor_vacate_job</i> on jobs which are not currently running has no effect. </p>
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
<p> <i>cluster</i></p>
<dl>
<dt>
<dd> Vacate all jobs in the specified cluster</p>
<dt>
<dd></dl>
<p> <i>cluster.process</i></p>
<dl>
<dt>
<dd> Vacate the specific job in the cluster</p>
<dt>
<dd></dl>
<p> <i>user</i></p>
<dl>
<dt>
<dd> Vacate jobs belonging to specified user</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Vacate all jobs which match the job ClassAd expression constraint</p>
<dt>
<dd></dl>
<p> <i>-all</i></p>
<dl>
<dt>
<dd> Vacate all the jobs in the queue</p>
<dt>
<dd></dl>
<p> <i>-fast</i></p>
<dl>
<dt>
<dd> Perform a fast vacate and hard kill the jobs</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> Do not confuse <i>condor_vacate_job</i> with <i>condor_vacate</i> . <i>condor_vacate</i> is given a list of hosts to vacate, regardless of what jobs happen to be running on them. Only machine owners and administrators have permission to use <i>condor_vacate</i> to evict jobs from a given host. <i>condor_vacate_job</i> is given a list of job to vacate, regardless of which hosts they happen to be running on. Only the owner of the jobs or queue super users have permission to use <i>condor_vacate_job</i> . </p>
<h2>Examples</h2>
<p> To vacate job 23.0: </p>
<p> % condor_vacate_job 23.0 </p>
<p> To vacate all jobs of a user named Mary: </p>
<p> % condor_vacate_job mary </p>
<p> To vacate all standard universe jobs owned by Mary: </p>
<p> % condor_vacate_job -constraint &#8216;JobUniverse == 1 &amp;&amp; Owner == &quot;mary&quot;&#8217; </p>
<p> Note that the entire constraint, including the quotation marks, must be enclosed in single quote marks for most shells. </p>
<h2>Exit Status</h2>
<p> <i>condor_vacate_job</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
