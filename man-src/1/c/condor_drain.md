---
title: "condor_drain(1)"
name: "condor_drain"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_drain/"
description: "condor_drain Control draining of an execute machine"
---

<h2>Name</h2>
<p> <i>condor_drain</i> Control draining of an execute machine </p>
<h2>Synopsis</h2>
<p> <i>condor_drain</i> [ <code>-help</code> ] </p>
<p> <i>condor_drain</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>pool-name</i> ] [ <code>-graceful | -quick | -fast</code> ] [ <code>-resume-on-completion</code> ] [ <code>-check </code> <i>expr</i> ] <i>machine-name </i> </p>
<p> <i>condor_drain</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>pool-name</i> ] <code>-cancel</code> [ <code>-request-id </code> <i>id</i> ] <i>machine-name </i> </p>
<h2>Description</h2>
<p> <i>condor_drain</i> is an administrative command used to control the draining of all slots on an execute machine. When a machine is draining, it will not accept any new jobs. Which machine to drain is specified by the argument <i>machine-name</i> , and will be the same as the machine ClassAd attribute Machine . </p>
<p> How currently running jobs are treated depends on the draining schedule that is chosen with a command-line option: </p>
<p> <code>-graceful</code></p>
<dl>
<dt>
<dd> Initiate a graceful eviction of the job. This means all promises that have been made to the job are honored, including MaxJobRetirementTime . The eviction of jobs is coordinated to reduce idle time. This means that if one slot has a job with a long retirement time and the other slots have jobs with shorter retirement times, the effective retirement time for all of the jobs is the longer one. If no draining schedule is specified, <code>-graceful</code> is chosen by default.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-quick</code></p>
<dl>
<dt>
<dd>
&nbsp;<wbr>MaxJobRetirementTime is not honored. Eviction of jobs is immediately initiated. Jobs are given time to shut down and produce checkpoints, according to the usual policy, that is, given by&nbsp;<wbr>&nbsp;<wbr>MachineMaxVacateTime .&nbsp;<wbr></p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
<dd> Jobs are immediately hard-killed, with no chance to gracefully shut down or produce a checkpoint.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> Once draining is complete, the machine will enter the Drained/Idle state. To resume normal operation (negotiation) at that time or any previous time during draining, the <code>-cancel</code> option may be used. The <code>-resume-on-completion</code> option results in automatic resumption of normal operation once draining has completed, and may be used when initiating draining. This is useful for forcing a machine with a partitionable slots to join all of the resources back together into one machine, facilitating de-fragmentation and whole machine negotiation. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display brief usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>pool-name</i></p>
<dl>
<dt>
<dd> Specify an alternate HTCondor pool, if the default one is not desired.</p>
<dt>
<dd></dl>
<p> <code>-graceful</code></p>
<dl>
<dt>
<dd> (the default) Honor the maximum vacate and retirement time policy.</p>
<dt>
<dd></dl>
<p> <code>-quick</code></p>
<dl>
<dt>
<dd> Honor the maximum vacate time, but not the retirement time policy.</p>
<dt>
<dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
<dd> Honor neither the maximum vacate time policy nor the retirement time policy.</p>
<dt>
<dd></dl>
<p> <code>-resume-on-completion</code></p>
<dl>
<dt>
<dd> When done draining, resume normal operation, such that potentially the whole machine could be claimed.</p>
<dt>
<dd></dl>
<p> <code>-check </code> <i>expr</i></p>
<dl>
<dt>
<dd> Abort draining, if expr is not true for all slots to be drained.</p>
<dt>
<dd></dl>
<p> <code>-cancel</code></p>
<dl>
<dt>
<dd> Cancel a prior draining request, to permit the <i>condor_negotiator</i> to use the machine again.</p>
<dt>
<dd></dl>
<p> <code>-request-id </code> <i>id</i></p>
<dl>
<dt>
<dd> Specify a specific draining request to cancel, where <i>id</i> is given by the DrainingRequestId machine ClassAd attribute.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_drain</i> will exit with a non-zero status value if it fails and zero status if it succeeds. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
