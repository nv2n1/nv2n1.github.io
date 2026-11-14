---
title: "condor_router_history(1)"
name: "condor_router_history"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_router_history/"
description: "condor_router_history Display the history for routed jobs"
---

<h2>Name</h2>
<p> <i>condor_router_history</i> Display the history for routed jobs </p>
<h2>Synopsis</h2>
<p> <i>condor_router_history</i> [ &#8212; <code>h</code> ] </p>
<p> <i>condor_router_history</i> [ &#8212; <code>show_records</code> ] [ &#8212; <code>show_iwd</code> ] [ &#8212; <code>age</code> <i>days</i> ] [ &#8212; <code>days</code> <i>days</i> ] [ &#8212; <code>start</code> <i>YYYY-MM-DD HH:MM</i> ] </p>
<h2>Description</h2>
<p> <i>condor_router_history</i> summarizes statistics for routed jobs over the previous 24 hours. With no command line options, statistics for run time, number of jobs completed, and number of jobs aborted are listed per route (site). </p>
<h2>Options</h2>
<p> <code>&#8211;h</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>&#8211;show_records</code></p>
<dl>
<dt>
<dd> Displays individual records in addition to the summary.</p>
<dt>
<dd></dl>
<p> <code>&#8211;show_iwd</code></p>
<dl>
<dt>
<dd> Include working directory in displayed records.</p>
<dt>
<dd></dl>
<p> <code>&#8211;age </code> <i>days</i></p>
<dl>
<dt>
<dd> Set the ending time of the summary to be <i>days</i> days ago.</p>
<dt>
<dd></dl>
<p> <code>&#8211;days </code> <i>days</i></p>
<dl>
<dt>
<dd> Set the number of days to summarize.</p>
<dt>
<dd></dl>
<p> <code>&#8211;start </code> <i>YYYY-MM-DD HH:MM</i></p>
<dl>
<dt>
<dd> Set the start time of the summary.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_router_history</i> will exit with a status of 0 (zero) upon success, and non-zero otherwise. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
