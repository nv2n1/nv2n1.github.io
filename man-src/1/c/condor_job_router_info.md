---
title: "condor_job_router_info(1)"
name: "condor_job_router_info"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_job_router_info/"
description: "condor_job_router_info Discover and display information related to job routing"
---

<h2>Name</h2>
<p> <i>condor_job_router_info</i> Discover and display information related to job routing </p>
<h2>Synopsis</h2>
<p> <i>condor_job_router_info</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_job_router_info</i> <code>-config</code> </p>
<p> <i>condor_job_router_info</i> <code>-match-jobs </code> <code>-jobads </code> <i>filename</i> [ <code>-ignore-prior-routing</code> ] </p>
<h2>Description</h2>
<p> <i>condor_job_router_info</i> displays information about job routing. The information will be either the available, configured routes or the routes for specified jobs. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display HTCondor version information and exit.</p>
<dt>
<dd></dl>
<p> <code>-config</code></p>
<dl>
<dt>
<dd> Display configured routes.</p>
<dt>
<dd></dl>
<p> <code>-match-jobs</code></p>
<dl>
<dt>
<dd> For each job listed in the file specified by the <code>-jobads</code> option, display the first route found.</p>
<dt>
<dd></dl>
<p> <code>-ignore-prior-routing</code></p>
<dl>
<dt>
<dd> For each job, remove any existing routing ClassAd attributes, and set attribute JobStatus to the Idle state before finding the first route.</p>
<dt>
<dd></dl>
<p> <code>-jobads </code> <i>filename</i></p>
<dl>
<dt>
<dd> Read job ClassAds from file <i>filename</i> . If <i>filename</i> is &#8211; , then read from stdin .</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_job_router_info</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
