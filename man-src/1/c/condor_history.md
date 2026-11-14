---
title: "condor_history(1)"
name: "condor_history"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_history/"
description: "condor_history View log of HTCondor jobs completed to date"
---

<h2>Name</h2>
<p> <i>condor_history</i> View log of HTCondor jobs completed to date </p>
<h2>Synopsis</h2>
<p> <i>condor_history</i> [ <code>-help</code> ] </p>
<p> <i>condor_history</i> [ <code>-name </code> <i>name</i> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-backwards</code> ] [ <code>-forwards</code> ] [ <code>-constraint </code> <i>expr</i> ] [ <code>-file </code> <i>filename</i> ] [ <code>-userlog </code> <i>filename</i> ] [ <code>-format </code> <i>formatString AttributeName</i> ] [ <code>-autoformat[:tn,lVh] </code> <i>attr1 [attr2 &#8230;]</i> ] [ <code>-l | -long | -xml</code> ] [ <code>-match | -limit </code> <i>number</i> ] [ <code>cluster | cluster.process | owner</code> ] </p>
<h2>Description</h2>
<p> <i>condor_history</i> displays a summary of all HTCondor jobs listed in the specified history files. If no history files are specified with the <code>-file</code> option, the local history file as specified in HTCondor&#8217;s configuration file ( $(SPOOL) /history by default) is read. The default listing summarizes in reverse chronological order each job on a single line, and contains the following items: </p>
<p> <code>ID</code></p>
<dl>
<dt>
<dd> The cluster/process id of the job.</p>
<dt>
<dd></dl>
<p> <code>OWNER</code></p>
<dl>
<dt>
<dd> The owner of the job.</p>
<dt>
<dd></dl>
<p> <code>SUBMITTED</code></p>
<dl>
<dt>
<dd> The month, day, hour, and minute the job was submitted to the queue.</p>
<dt>
<dd></dl>
<p> <code>RUN_TIME</code></p>
<dl>
<dt>
<dd> Remote wall clock time accumulated by the job to date in days, hours, minutes, and seconds, given as the job ClassAd attribute RemoteWallClockTime .</p>
<dt>
<dd></dl>
<p> <code>ST</code></p>
<dl>
<dt>
<dd> Completion status of the job (C = completed and X = removed).</p>
<dt>
<dd></dl>
<p> <code>COMPLETED</code></p>
<dl>
<dt>
<dd> The time the job was completed.</p>
<dt>
<dd></dl>
<p> <code>CMD</code></p>
<dl>
<dt>
<dd> The name of the executable.</p>
<dt>
<dd></dl>
<p> If a job ID (in the form of <i>cluster_id</i> or <i>cluster_id.proc_id</i> ) or an <i>owner</i> is provided, output will be restricted to jobs with the specified IDs and/or submitted by the specified owner. The <i>-constraint</i> option can be used to display jobs that satisfy a specified boolean expression. </p>
<p> The history file is kept in chronological order, implying that new entries are appended at the end of the file. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>name</i></p>
<dl>
<dt>
<dd> Query the named <i>condor_schedd</i> daemon.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Use the <i>centralmanagerhostname</i> as the central manager to locate <i>condor_schedd</i> daemons. The default is the COLLECTOR_HOST , as specified in the configuration.</p>
<dt>
<dd></dl>
<p> <code>-backwards</code></p>
<dl>
<dt>
<dd> List jobs in reverse chronological order. The job most recently added to the history file is first. This is the default ordering.</p>
<dt>
<dd></dl>
<p> <code>-forwards</code></p>
<dl>
<dt>
<dd> List jobs in chronological order. The job most recently added to the history file is last. At least 4 characters must be given to distinguish this option from the <code>-file</code> and <code>-format</code> options.</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expr</i></p>
<dl>
<dt>
<dd> Display jobs that satisfy the expression.</p>
<dt>
<dd></dl>
<p> <code>-file </code> <i>filename</i></p>
<dl>
<dt>
<dd> Use the specified file instead of the default history file.</p>
<dt>
<dd></dl>
<p> <code>-userlog </code> <i>filename</i></p>
<dl>
<dt>
<dd> Display jobs, with job information coming from a job event log, instead of from the default history file. A job event log does not contain all of the job information, so some fields in the normal output of <i>condor_history</i> will be blank.</p>
<dt>
<dd></dl>
<p> <code>-format </code> <i>formatString</i> AttributeName</p>
<dl>
<dt>
<dd> Display jobs with a custom format. See the <i>condor_q</i> man page <code>-format</code> option for details.</p>
<dt>
<dd></dl>
<p> <code>-autoformat[:tn,lVh] </code> <i>attr1 [attr2 &#8230;]</i> or <code>-af[:tn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> Display attribute(s) or expression(s) formatted in a default way according to attribute types. See the <i>condor_q</i> man page <code>-autoformat</code> option for details.</p>
<dt>
<dd></dl>
<p> <code>-l</code> or <code>-long</code></p>
<dl>
<dt>
<dd> Display job ClassAds in long format.</p>
<dt>
<dd></dl>
<p> <code>-limit </code> <i>Number</i></p>
<dl>
<dt>
<dd> Limit the number of jobs displayed to <i>Number</i> . Same option as <code>-match</code> .</p>
<dt>
<dd></dl>
<p> <code>-match </code> <i>Number</i></p>
<dl>
<dt>
<dd> Limit the number of jobs displayed to <i>Number</i> . Same option as <code>-limit</code> .</p>
<dt>
<dd></dl>
<p> <code>-xml</code></p>
<dl>
<dt>
<dd> Display job ClassAds in XML format. The XML format is fully defined in the reference manual, obtained from the ClassAds web page, with a link at <a rel="nofollow" href="http://research.cs.wisc.edu/htcondor/research.html.">http://research.cs.wisc.edu/htcondor/research.html.</a></p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_history</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
