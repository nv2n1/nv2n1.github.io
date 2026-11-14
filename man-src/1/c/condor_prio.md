---
title: "condor_prio(1)"
name: "condor_prio"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_prio/"
description: "condor_prio change priority of jobs in the HTCondor queue"
---

<h2>Name</h2>
<p> <i>condor_prio</i> change priority of jobs in the HTCondor queue </p>
<h2>Synopsis</h2>
<p> <i>condor_prio</i> <code>-p </code> <i>priority</i> <code>+ </code> <i>value</i> <code>&#8211; </code> <i>value</i> [ <code>-n </code> <i>schedd_name</i> ] <i>cluster | cluster.process | username | -a</i> </p>
<p> <i>condor_prio</i> <code>-p </code> <i>priority</i> <code>+ </code> <i>value</i> <code>&#8211; </code> <i>value</i> [ <code>-pool </code> <i>pool_name</i> <code>-n </code> <i>schedd_name</i> ] <i>cluster | cluster.process | username | -a</i> </p>
<h2>Description</h2>
<p> <i>condor_prio</i> changes the priority of one or more jobs in the HTCondor queue. If the job identification is given by <i>cluster.process</i> , <i>condor_prio</i> attempts to change the priority of the single job with job ClassAd attributes ClusterId and ProcId . If described by <i>cluster</i> , <i>condor_prio</i> attempts to change the priority of all processes with the given ClusterId job ClassAd attribute. If <i>username</i> is specified, <i>condor_prio</i> attempts to change priority of all jobs belonging to that user. For <i>-a</i> , <i>condor_prio</i> attempts to change priority of all jobs in the queue. </p>
<p> The user must set a new priority with the <code>-p</code> option, or specify a priority adjustment. The priority of a job can be any integer, with higher numbers corresponding to greater priority. For adjustment of the current priority, <code>+ </code> <i>value</i> increases the priority by the amount given with <i>value</i> . <code>&#8211; </code> <i>value</i> decreases the priority by the amount given with <i>value</i> . </p>
<p> Only the owner of a job or the super user can change the priority. </p>
<p> The priority changed by <i>condor_prio</i> is only used when comparing to the priority jobs owned by the same user and submitted from the same machine. </p>
<h2>Options</h2>
<p> <code>-n </code> <i>schedd_name</i></p>
<dl>
<dt>
<dd> Change priority of jobs queued at the specified <i>condor_schedd</i> in the local pool.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>pool_name</i> <code>-n </code> <i>schedd_name</i></p>
<dl>
<dt>
<dd> Change priority of jobs queued at the specified <i>condor_schedd</i> in the specified pool.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_prio</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
