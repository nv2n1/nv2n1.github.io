---
title: "condor_pool_job_report(1)"
name: "condor_pool_job_report"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_pool_job_report/"
---

<h2>Name</h2>

 

 <i>condor_pool_job_report</i> generate report about all jobs that have run in the last 24 hours on all execute hosts 

 

<h2>Synopsis</h2>

 

 <i>condor_pool_job_report</i> 

<h2>Description</h2>

 

 <i>condor_pool_job_report</i> is a Linux-only tool that is designed to be run nightly using <i>cron</i> . It is intended to be run on the central manager, or another machine that has administrative permissions, and is able to fetch the <i>condor_startd</i> history logs from all of the <i>condor_startd</i> daemons in the pool. After fetching these logs, <i>condor_pool_job_report</i> then generates a report about job run times and mails it to administrators, as defined by configuration variable CONDOR_ADMIN . 

<h2>Exit Status</h2>

 

 <i>condor_pool_job_report</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. 

<h2>Author</h2>

 Center for High Throughput Computing, University of Wisconsin-Madison

<h2>Copyright</h2>

 Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. 

<h2>Index</h2>


