---
title: "condor_router_rm(1)"
name: "condor_router_rm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_router_rm/"
description: "condor_router_rm Remove jobs being managed by the HTCondor Job Router"
---

<h2>Name</h2>
<p> <i>condor_router_rm</i> Remove jobs being managed by the HTCondor Job Router </p>
<h2>Synopsis</h2>
<p> <i>condor_router_rm</i> [ <i>router_rm options</i> ] [ <i>condor_rm options</i> ] </p>
<h2>Description</h2>
<p> <i>condor_router_rm</i> is a script that provides additional features above those offered by <i>condor_rm</i> , for removing jobs being managed by the HTCondor Job Router. </p>
<p> The options that may be supplied to <i>condor_router_rm</i> belong to two groups:</p>
<dl>
<dt>
<dd> * <code>router_rm options</code> provide the additional features</p>
<dt>
<dd> * <code>condor_rm options</code> are those options already offered by <i>condor_rm</i> . See the <i>condor_rm</i> manual page for specification of these options.</dl>
<h2>Options</h2>
<p> <code>-constraint </code> <i>X</i></p>
<dl>
<dt>
<dd> (router_rm option) Remove jobs matching the constraint specified by <i>X</i></p>
<dt>
<dd></dl>
<p> <code>-held</code></p>
<dl>
<dt>
<dd> (router_rm option) Remove only jobs in the hold state</p>
<dt>
<dd></dl>
<p> <code>-idle</code></p>
<dl>
<dt>
<dd> (router_rm option) Remove only idle jobs</p>
<dt>
<dd></dl>
<p> <code>-route </code> <i>name</i></p>
<dl>
<dt>
<dd> (router_rm option) Remove only jobs on specified route</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_router_rm</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
