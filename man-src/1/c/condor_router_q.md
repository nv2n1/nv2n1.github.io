---
title: "condor_router_q(1)"
name: "condor_router_q"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_router_q/"
description: "condor_router_q Display information about routed jobs in the queue"
---

<h2>Name</h2>
<p> <i>condor_router_q</i> Display information about routed jobs in the queue </p>
<h2>Synopsis</h2>
<p> <i>condor_router_q</i> [ <code>-S</code> ] [ <code>-R</code> ] [ <code>-I</code> ] [ <code>-H</code> ] [ <code>-route </code> <i>name</i> ] [ <code>-idle</code> ] [ <code>-held</code> ] [ <code>-constraint </code> <i>X</i> ] [ <code>condor_q options</code> ] </p>
<h2>Description</h2>
<p> <i>condor_router_q</i> displays information about jobs managed by the <i>condor_job_router</i> that are in the HTCondor job queue. The functionality of this tool is that of <i>condor_q</i> , with additional options specialized for routed jobs. Therefore, any of the options for <i>condor_q</i> may also be used with <i>condor_router_q</i> . </p>
<h2>Options</h2>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> Summarize the state of the jobs on each route.</p>
<dt>
<dd></dl>
<p> <code>-R</code></p>
<dl>
<dt>
<dd> Summarize the running jobs on each route.</p>
<dt>
<dd></dl>
<p> <code>-I</code></p>
<dl>
<dt>
<dd> Summarize the idle jobs on each route.</p>
<dt>
<dd></dl>
<p> <code>-H</code></p>
<dl>
<dt>
<dd> Summarize the held jobs on each route.</p>
<dt>
<dd></dl>
<p> <code>-route </code> <i>name</i></p>
<dl>
<dt>
<dd> Display only the jobs on the route identified by <i>name</i> .</p>
<dt>
<dd></dl>
<p> <code>-idle</code></p>
<dl>
<dt>
<dd> Display only the idle jobs.</p>
<dt>
<dd></dl>
<p> <code>-held</code></p>
<dl>
<dt>
<dd> Display only the held jobs.</p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>X</i></p>
<dl>
<dt>
<dd> Display only the jobs matching constraint <i>X</i> .</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_router_q</i> will exit with a status of 0 (zero) upon success, and non-zero otherwise. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
