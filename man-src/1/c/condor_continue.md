---
title: "condor_continue(1)"
name: "condor_continue"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_continue/"
description: "condor_continue continue suspended jobs from the HTCondor queue"
---

<h2>Name</h2>
<p> <i>condor_continue</i> continue suspended jobs from the HTCondor queue </p>
<h2>Synopsis</h2>
<p> <i>condor_continue</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_continue</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <i>cluster cluster.process user </i> <code>-constraint </code> <i>expression</i> -all </p>
<h2>Description</h2>
<p> <i>condor_continue</i> continues one or more suspended jobs from the HTCondor job queue. If the <code>-name</code> option is specified, the named <i>condor_schedd</i> is targeted for processing. Otherwise, the local <i>condor_schedd</i> is targeted. The job(s) to be continued are identified by one of the job identifiers, as described below. For any given job, only the owner of the job or one of the queue super users (defined by the QUEUE_SUPER_USERS macro) can continue the job. </p>
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
<p> <i>cluster</i></p>
<dl>
<dt>
<dd> Continue all jobs in the specified cluster</p>
<dt>
<dd></dl>
<p> <i>cluster.process</i></p>
<dl>
<dt>
<dd> Continue the specific job in the cluster</p>
<dt>
<dd></dl>
<p> <i>user</i></p>
<dl>
<dt>
<dd> Continue jobs belonging to specified user</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Continue all jobs which match the job ClassAd expression constraint</p>
<dt>
<dd></dl>
<p> <i>-all</i></p>
<dl>
<dt>
<dd> Continue all the jobs in the queue</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_continue</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To continue all jobs except for a specific user: </p>
<p> % condor_continue -constraint &#8216;Owner =!= &quot;foo&quot;&#8217; </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
