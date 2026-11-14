---
title: "condor_userlog(1)"
name: "condor_userlog"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_userlog/"
description: "condor_userlog Display and summarize job statistics from job log files."
---

<h2>Name</h2>
<p> <i>condor_userlog</i> Display and summarize job statistics from job log files. </p>
<h2>Synopsis</h2>
<p> <i>condor_userlog</i> [ <code>-help</code> ] [ <code>-total | -raw</code> ] [ <code>-debug</code> ] [ <code>-evict</code> ] [ <code>-j </code> <i>cluster | cluster.proc</i> ] [ <code>-all</code> ] [ <code>-hostname</code> ] <i>logfile &#8230; </i> </p>
<h2>Description</h2>
<p> <i>condor_userlog</i> parses the information in job log files and displays summaries for each workstation allocation and for each job. See the <i>condor_submit</i> manual page for instructions for specifying that HTCondor write a log file for your jobs. </p>
<p> If <code>-total</code> is not specified, <i>condor_userlog</i> will first display a record for each workstation allocation, which includes the following information: </p>
<p> <code>Job</code></p>
<dl>
<dt>
<dd> The cluster/process id of the HTCondor job.</p>
<dt>
<dd></dl>
<p> <code>Host</code></p>
<dl>
<dt>
<dd> The host where the job ran. By default, the host&#8217;s IP address is displayed. If <code>-hostname</code> is specified, the host name will be displayed instead.</p>
<dt>
<dd></dl>
<p> <code>Start Time</code></p>
<dl>
<dt>
<dd> The time (month/day hour:minute) when the job began running on the host.</p>
<dt>
<dd></dl>
<p> <code>Evict Time</code></p>
<dl>
<dt>
<dd> The time (month/day hour:minute) when the job was evicted from the host.</p>
<dt>
<dd></dl>
<p> <code>Wall Time</code></p>
<dl>
<dt>
<dd> The time (days+hours:minutes) for which this workstation was allocated to the job.</p>
<dt>
<dd></dl>
<p> <code>Good Time</code></p>
<dl>
<dt>
<dd> The allocated time (days+hours:min) which contributed to the completion of this job. If the job exited during the allocation, then this value will equal &#8220;Wall Time.&#8221; If the job performed a checkpoint, then the value equals the work saved in the checkpoint during this allocation. If the job did not exit or perform a checkpoint during this allocation, the value will be 0+00:00. This value can be greater than 0 and less than &#8220;Wall Time&#8221; if the application completed a periodic checkpoint during the allocation but failed to checkpoint when evicted.</p>
<dt>
<dd></dl>
<p> <code>CPU Usage</code></p>
<dl>
<dt>
<dd> The CPU time (days+hours:min) which contributed to the completion of this job.</p>
<dt>
<dd></dl>
<p> <i>condor_userlog</i> will then display summary statistics per host: </p>
<p> <code>Host/Job</code></p>
<dl>
<dt>
<dd> The IP address or host name for the host.</p>
<dt>
<dd></dl>
<p> <code>Wall Time</code></p>
<dl>
<dt>
<dd> The workstation time (days+hours:minutes) allocated by this host to the jobs specified in the query. By default, all jobs in the log are included in the query.</p>
<dt>
<dd></dl>
<p> <code>Good Time</code></p>
<dl>
<dt>
<dd> The time (days+hours:minutes) allocated on this host which contributed to the completion of the jobs specified in the query.</p>
<dt>
<dd></dl>
<p> <code>CPU Usage</code></p>
<dl>
<dt>
<dd> The CPU time (days+hours:minutes) obtained from this host which contributed to the completion of the jobs specified in the query.</p>
<dt>
<dd></dl>
<p> <code>Avg Alloc</code></p>
<dl>
<dt>
<dd> The average length of an allocation on this host (days+hours:minutes).</p>
<dt>
<dd></dl>
<p> <code>Avg Lost</code></p>
<dl>
<dt>
<dd> The average amount of work lost (days+hours:minutes) when a job was evicted from this host without successfully performing a checkpoint.</p>
<dt>
<dd></dl>
<p> <code>Goodput</code></p>
<dl>
<dt>
<dd> This percentage is computed as Good Time divided by Wall Time.</p>
<dt>
<dd></dl>
<p> <code>Util.</code></p>
<dl>
<dt>
<dd> This percentage is computed as CPU Usage divided by Good Time.</p>
<dt>
<dd></dl>
<p> <i>condor_userlog</i> will then display summary statistics per job: </p>
<p> <code>Host/Job</code></p>
<dl>
<dt>
<dd> The cluster/process id of the HTCondor job.</p>
<dt>
<dd></dl>
<p> <code>Wall Time</code></p>
<dl>
<dt>
<dd> The total workstation time (days+hours:minutes) allocated to this job.</p>
<dt>
<dd></dl>
<p> <code>Good Time</code></p>
<dl>
<dt>
<dd> The total time (days+hours:minutes) allocated to this job which contributed to the job&#8217;s completion.</p>
<dt>
<dd></dl>
<p> <code>CPU Usage</code></p>
<dl>
<dt>
<dd> The total CPU time (days+hours:minutes) which contributed to this job&#8217;s completion.</p>
<dt>
<dd></dl>
<p> <code>Avg Alloc</code></p>
<dl>
<dt>
<dd> The average length of a workstation allocation obtained by this job in minutes (days+hours:minutes).</p>
<dt>
<dd></dl>
<p> <code>Avg Lost</code></p>
<dl>
<dt>
<dd> The average amount of work lost (days+hours:minutes) when this job was evicted from a host without successfully performing a checkpoint.</p>
<dt>
<dd></dl>
<p> <code>Goodput</code></p>
<dl>
<dt>
<dd> This percentage is computed as Good Time divided by Wall Time.</p>
<dt>
<dd></dl>
<p> <code>Util.</code></p>
<dl>
<dt>
<dd> This percentage is computed as CPU Usage divided by Good Time.</p>
<dt>
<dd></dl>
<p> Finally, <i>condor_userlog</i> will display a summary for all hosts and jobs. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Get a brief description of the supported options</p>
<dt>
<dd></dl>
<p> <code>-total</code></p>
<dl>
<dt>
<dd> Only display job totals</p>
<dt>
<dd></dl>
<p> <code>-raw</code></p>
<dl>
<dt>
<dd> Display raw data only</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Debug mode</p>
<dt>
<dd></dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Select a specific cluster or cluster.proc</p>
<dt>
<dd></dl>
<p> <code>-evict</code></p>
<dl>
<dt>
<dd> Select only allocations which ended due to eviction</p>
<dt>
<dd></dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Select all clusters and all allocations</p>
<dt>
<dd></dl>
<p> <code>-hostname</code></p>
<dl>
<dt>
<dd> Display host name instead of IP address</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> Since the HTCondor job log file format does not contain a year field in the timestamp, all entries are assumed to occur in the current year. Allocations which begin in one year and end in the next will be silently ignored. </p>
<h2>Exit Status</h2>
<p> <i>condor_userlog</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
