---
title: "condor_wait(1)"
name: "condor_wait"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_wait/"
description: "condor_wait Wait for jobs to finish"
---

<h2>Name</h2>
<p> <i>condor_wait</i> Wait for jobs to finish </p>
<h2>Synopsis</h2>
<p> <i>condor_wait</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_wait</i> [ <code>-debug</code> ] [ <code>-status</code> ] [ <code>-echo</code> ] [ <code>-wait </code> <i>seconds</i> ] [ <code>-num </code> <i>number-of-jobs</i> ] <i>log-file</i> [ <code>job ID</code> ] </p>
<h2>Description</h2>
<p> <i>condor_wait</i> watches a job event log file (created with the <code>log</code> command within a submit description file) and returns when one or more jobs from the log have completed or aborted. </p>
<p> Because <i>condor_wait</i> expects to find at least one job submitted event in the log file, at least one job must have been successfully submitted with <i>condor_submit</i> before <i>condor_wait</i> is executed. </p>
<p> <i>condor_wait</i> will wait forever for jobs to finish, unless a shorter wait time is specified. </p>
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
<dd> Show extra debugging information.</p>
<dt>
<dd></dl>
<p> <code>-status</code></p>
<dl>
<dt>
<dd> Show job start and terminate information.</p>
<dt>
<dd></dl>
<p> <code>-echo</code></p>
<dl>
<dt>
<dd> Print the events out to stdout .</p>
<dt>
<dd></dl>
<p> <code>-wait </code> <i>seconds</i></p>
<dl>
<dt>
<dd> Wait no more than the integer number of <i>seconds</i> . The default is unlimited time.</p>
<dt>
<dd></dl>
<p> <code>-num </code> <i>number-of-jobs</i></p>
<dl>
<dt>
<dd> Wait for the integer <i>number-of-jobs</i> jobs to end. The default is all jobs in the log file.</p>
<dt>
<dd></dl>
<p> <code>log file</code></p>
<dl>
<dt>
<dd> The name of the log file to watch for information about the job.</p>
<dt>
<dd></dl>
<p> <code>job ID</code></p>
<dl>
<dt>
<dd> A specific job or set of jobs to watch. If the <code>job ID</code> is only the job ClassAd attribute ClusterId , then <i>condor_wait</i> waits for all jobs with the given ClusterId . If the <code>job ID</code> is a pair of the job ClassAd attributes, given by ClusterId . ProcId , then <i>condor_wait</i> waits for the specific job with this <code>job ID</code> . If this option is not specified, all jobs that exist in the log file when <i>condor_wait</i> is invoked will be watched.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> <i>condor_wait</i> is an inexpensive way to test or wait for the completion of a job or a whole cluster, if you are trying to get a process outside of HTCondor to synchronize with a job or set of jobs. </p>
<p> It can also be used to wait for the completion of a limited subset of jobs, via the <code>-num</code> option. </p>
<h2>Examples</h2>
<p> condor_wait logfile </p>
<p> This command waits for all jobs that exist in logfile to complete. </p>
<p> condor_wait logfile 40 </p>
<p> This command waits for all jobs that exist in logfile with a job ClassAd attribute ClusterId of 40 to complete. </p>
<p> condor_wait -num 2 logfile </p>
<p> This command waits for any two jobs that exist in logfile to complete. </p>
<p> condor_wait logfile 40.1 </p>
<p> This command waits for job 40.1 that exists in logfile to complete. </p>
<p> condor_wait -wait 3600 logfile 40.1 </p>
<p> This waits for job 40.1 to complete by watching logfile , but it will not wait more than one hour (3600 seconds). </p>
<h2>Exit Status</h2>
<p> <i>condor_wait</i> exits with 0 if and only if the specified job or jobs have completed or aborted. <i>condor_wait</i> returns 1 if unrecoverable errors occur, such as a missing log file, if the job does not exist in the log file, or the user-specified waiting time has expired. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
