---
title: "globus-job-status(1)"
name: "globus-job-status"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-job-status/"
description: "globus-job-status – Check the status of a GRAM5 job"
---

<h2 class="name">NAME</h2>
<p> globus-job-status &#8211; Check the status of a GRAM5 job </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-job-status</code> <i>JOBID</i> </p>
<p> <code>globus-job-status</code> -help | -usage | -version | -versions</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-job-status</code> program checks the status of a GRAM job by sending a status request to the job manager contact for that job specified by the <i>JOBID</i> parameter. If successful, it will print the job status to standard output. The states supported by <code>globus-job-status</code> are: </p>
<p> <code>PENDING</code></p>
<dl>
<dt>
<dd> The job has been submitted to the LRM but has not yet begun execution.</dl>
<p> <code>ACTIVE</code></p>
<dl>
<dt>
<dd> The job has begun execution.</dl>
<p> <code>FAILED</code></p>
<dl>
<dt>
<dd> The job has failed.</dl>
<p> <code>SUSPENDED</code></p>
<dl>
<dt>
<dd> The job is currently suspended by the LRM.</dl>
<p> <code>DONE</code></p>
<dl>
<dt>
<dd> The job has completed.</dl>
<p> <code>UNSUBMITTED</code></p>
<dl>
<dt>
<dd> The job has been accepted by GRAM, but not yet submitted to the LRM.</dl>
<p> <code>STAGE_IN</code></p>
<dl>
<dt>
<dd> The job has been accepted by GRAM and is currently staging files prior to being submitted to the LRM.</dl>
<p> <code>STAGE_OUT</code></p>
<dl>
<dt>
<dd> The job has completed execution and is currently staging files from the service node to other http, GASS, or GridFTP servers.</dl>
<h2>OPTIONS</h2>
<p> The full set of options to <code>globus-job-status</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display a help message to standard error and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-status</code> program to standard output.</dl>
<p> <code>-versions</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-status</code> program including DiRT information to standard output.</dl>
<h2>ENVIRONMENT</h2>
<p> If the following variables affect the execution of <code>globus-job-status</code>. </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to proxy credential.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to trusted certificate directory.</dl>
<h2>BUGS</h2>
<p> The <code>globus-job-status</code> program can not distinguish between the case of the job manager terminating for any reason and the job being in the DONE state.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-globusrun/">globusrun</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
