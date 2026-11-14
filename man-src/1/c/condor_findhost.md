---
title: "condor_findhost(1)"
name: "condor_findhost"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_findhost/"
description: "condor_findhost find machine(s) in the pool that can be used with minimal impact on currently running HTCondor jobs and best meet any specified constraints"
---

<h2>Name</h2>
<p> <i>condor_findhost</i> find machine(s) in the pool that can be used with minimal impact on currently running HTCondor jobs and best meet any specified constraints </p>
<h2>Synopsis</h2>
<p> <i>condor_findhost</i> [ <code>-help</code> ] [ <code>-m</code> ] [ <code>-n </code> <i>num</i> ] [ <code>-c </code> <i>c_expr</i> ] [ <code>-r </code> <i>r_expr</i> ] [ <code>-p </code> <i>centralmanagerhostname</i> ] </p>
<h2>Description</h2>
<p> <i>condor_findhost</i> searches an HTCondor pool of machines for the best machine or machines that will have the minimum impact on running HTCondor jobs if the machine or machines are taken out of the pool. The search may be limited to the machine or machines that match a set of constraints and rank expression. </p>
<p> <i>condor_findhost</i> returns a fully-qualified domain name for each machine. The search is limited (constrained) to a specific set of machines using the <i>-c</i> option. The search can use the <i>-r</i> option for rank, the criterion used for selecting a machine or machines from the constrained list. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit</p>
<dt>
<dd></dl>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> Only search for entire machines. Slots within an entire machine are not considered.</p>
<dt>
<dd></dl>
<p> <code>-n </code> <i>num</i></p>
<dl>
<dt>
<dd> Find and list up to <i>num</i> machines that fulfill the specification. <i>num</i> is an integer greater than zero.</p>
<dt>
<dd></dl>
<p> <code>-c </code> <i>c_expr</i></p>
<dl>
<dt>
<dd> Constrain the search to only consider machines that result from the evaluation of <i>c_expr</i> . <i>c_expr</i> is a ClassAd expression.</p>
<dt>
<dd></dl>
<p> <code>-r </code> <i>r_expr</i></p>
<dl>
<dt>
<dd> <i>r_expr</i> is the rank expression evaluated to use as a basis for machine selection. <i>r_expr</i> is a ClassAd expression.</p>
<dt>
<dd></dl>
<p> <code>-p </code> <i>centralmanagerhostname</i></p>
<dl>
<dt>
<dd> Specify the pool to be searched by giving the central manager&#8217;s host name. Without this option, the current pool is searched.</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> <i>condor_findhost</i> is used to locate a machine within a pool that can be taken out of the pool with the least disturbance of the pool. </p>
<p> An administrator should set preemption requirements for the HTCondor pool. The expression </p>
<p> (Interactive =?= TRUE ) </p>
<p> will let <i>condor_findhost</i> know that it can claim a machine even if HTCondor would not normally preempt a job running on that machine. </p>
<h2>Exit Status</h2>
<p> The exit status of <i>condor_findhost</i> is zero on success. If not able to identify as many machines as requested, it returns one more than the number of machines identified. For example, if 8 machines are requested, and <i>condor_findhost</i> only locates 6, the exit status will be 7. If not able to locate any machines, or an error is encountered, <i>condor_findhost</i> will return the value 1. </p>
<h2>Examples</h2>
<p> To find and list four machines, preferring those with the highest mips (on Drystone benchmark) rating: </p>
<p> condor_findhost -n 4 -r &quot;mips&quot; </p>
<p> To find and list 24 machines, considering only those where the kflops attribute is not defined: </p>
<p> condor_findhost -n 24 -c &quot;kflops=?=undefined&quot; </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
