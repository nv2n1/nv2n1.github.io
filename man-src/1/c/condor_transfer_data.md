---
title: "condor_transfer_data(1)"
name: "condor_transfer_data"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_transfer_data/"
description: "condor_transfer_data transfer spooled data"
---

<h2>Name</h2>
<p> <i>condor_transfer_data</i> transfer spooled data </p>
<h2>Synopsis</h2>
<p> <i>condor_transfer_data</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_transfer_data</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <i>cluster&#8230; cluster.process&#8230; user&#8230; </i> <code>-constraint </code> <i>expression</i> &#8230; </p>
<p> <i>condor_transfer_data</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] <code>-all</code> </p>
<h2>Description</h2>
<p> <i>condor_transfer_data</i> causes HTCondor to transfer spooled data. It is meant to be used in conjunction with the <code>-spool</code> option of <i>condor_submit</i> , as in </p>
<p> condor_submit -spool mysubmitfile </p>
<p> Submission of a job with the <code>-spool</code> option causes HTCondor to spool all input files, the job event log, and any proxy across a connection to the machine where the <i>condor_schedd</i> daemon is running. After spooling these files, the machine from which the job is submitted may disconnect from the network or modify its local copies of the spooled files. </p>
<p> When the job finishes, the job has JobStatus = 4, meaning that the job has completed. The output of the job is spooled, and <i>condor_transfer_data</i> retrieves the output of the completed job. </p>
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
<dd> Transfer spooled data belonging to the specified cluster</p>
<dt>
<dd></dl>
<p> <i>cluster.process</i></p>
<dl>
<dt>
<dd> Transfer spooled data belonging to a specific job in the cluster</p>
<dt>
<dd></dl>
<p> <i>user</i></p>
<dl>
<dt>
<dd> Transfer spooled data belonging to the specified user</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Transfer spooled data for jobs which match the job ClassAd expression constraint</p>
<dt>
<dd></dl>
<p> <i>-all</i></p>
<dl>
<dt>
<dd> Transfer all spooled data</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_transfer_data</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
