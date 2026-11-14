---
title: "glite-lb-mon(1)"
name: "glite-lb-mon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-mon/"
description: "glite-lb-mon – program for monitoring the number of jobs on the LB server and their several statistics"
---

<h2 class="name">NAME</h2>
<p> glite-lb-mon &#8211; program for monitoring the number of jobs on the LB server and their several statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-mon</code> <code>[-t time -h]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-mon</code> is a low-level program for monitoring the the number of jobs on the LB server and their several statistics. Values like minimum, average and maximum time spent in the system are calulated for jobs that entered the final state (Aborted, Cleared, Cancelled) in specific time (default last hour). Also number of jobs that entered the system during this time is calculated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t time, &#8211;time=time</code></p>
<dd> Querying time in seconds from now to the past [deault 3600]. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>EDG_WL_QUERY_SERVER</code></p>
<dd> set this environment variable to specify the LB server address to query </p>
</dl>
<h2>FILES</h2>
<p> A special bkindex configuration needed. The following time indices must be defined: </p>
<pre><code>
[type = "time"; name = "submitted"],
    [type = "time"; name = "cleared"],
    [type = "time"; name = "aborted"],
    [type = "time"; name = "cancelled"],
</code></pre>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkindex/">glite-lb-bkindex</a></code>(8), <code><a href="/docs/linux/man/1-glite-lb-mon/">glite-lb-mon</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> EU EGEE JRA1, CESNET group. </p>
<h2>Index</h2>
