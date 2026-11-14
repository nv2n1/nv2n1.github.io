---
title: "globus-job-cancel(1)"
name: "globus-job-cancel"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-job-cancel/"
description: "globus-job-cancel – Cancel a GRAM batch job"
---

<h2 class="name">NAME</h2>
<p> globus-job-cancel &#8211; Cancel a GRAM batch job </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-job-cancel</code> [-f | -force] [-q | -quiet] <i>JOBID</i> </p>
<p> <code>globus-job-cancel</code> [-help | -usage ] [ -version | -versions ]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-globus-job-cancel/">globus-job-cancel</a>(1) program cancels the job named by <i>JOBID</i>. Any cached files associated with the job will remain until <a href="/docs/linux/man/1-globus-job-clean/">globus-job-clean</a>(1) is executed for the job. </p>
<p> By default, globus-job-cancel prompts the user prior to canceling the job. This behavior can be overridden by specifying the <i>-f</i> or <i>-force</i> command-line options.</p>
<h2>OPTIONS</h2>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display a help message to standard error and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of the globus-job-cancel program to standard output.</dl>
<p> <code>-versions</code></p>
<dl>
<dt>
<dd> Display the software version of the globus-job-cancel program including DiRT information to standard output.</dl>
<p> <code>-force, -f</code></p>
<dl>
<dt>
<dd> Do not prompt to confirm job cancel and clean-up.</dl>
<p> <code>-quiet, -q</code></p>
<dl>
<dt>
<dd> Do not print diagnostics for successful cancel. Implies <i>-f</i>.</dl>
<h2>ENVIRONMENT</h2>
<p> If the following variables affect the execution of globus-job-cancel. </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to proxy credential.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to trusted certificate directory.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
