---
title: "condor_qedit(1)"
name: "condor_qedit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_qedit/"
description: "condor_qedit modify job attributes"
---

<h2>Name</h2>
<p> <i>condor_qedit</i> modify job attributes </p>
<h2>Synopsis</h2>
<p> <i>condor_qedit</i> [ <code>-debug</code> ] [ <code>-n </code> <i>schedd-name</i> ] [ <code>-pool </code> <i>pool-name</i> ] <i>{cluster | cluster.proc | owner | -constraint constraint}</i> <i>attribute-name</i> <i>attribute-value</i> <i>&#8230; </i> </p>
<h2>Description</h2>
<p> <i>condor_qedit</i> modifies job ClassAd attributes of queued HTCondor jobs. The jobs are specified either by cluster number, job ID, owner, or by a ClassAd constraint expression. The <i>attribute-value</i> may be any ClassAd expression. String expressions must be surrounded by double quotes. Multiple attribute value pairs may be listed on the same command line. </p>
<p> To ensure security and correctness, <i>condor_qedit</i> will not allow modification of the following ClassAd attributes:</p>
<dl>
<dt>
<dd> * Owner</p>
<dt>
<dd> * ClusterId</p>
<dt>
<dd> * ProcId</p>
<dt>
<dd> * MyType</p>
<dt>
<dd> * TargetType</p>
<dt>
<dd> * JobStatus</dl>
<p> Since JobStatus may not be changed with <i>condor_qedit</i> , use <i>condor_hold</i> to place a job in the hold state, and use <i>condor_release</i> to release a held job, instead of attempting to modify JobStatus directly. </p>
<p> If a job is currently running, modified attributes for that job will not affect the job until it restarts. As an example, for PeriodicRemove to affect when a currently running job will be removed from the queue, that job must first be evicted from a machine and returned to the queue. The same is true for other periodic expressions, such as PeriodicHold and PeriodicRelease . </p>
<p> <i>condor_qedit</i> validates both attribute names and attribute values, checking for correct ClassAd syntax. An error message is printed, and no attribute is set or changed if the name or value is invalid. </p>
<h2>Options</h2>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-n </code> <i>schedd-name</i></p>
<dl>
<dt>
<dd> Modify job attributes in the queue of the specified schedd</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>pool-name</i></p>
<dl>
<dt>
<dd> Modify job attributes in the queue of the schedd specified in the specified pool</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> % condor_qedit -name north.cs.wisc.edu -pool condor.cs.wisc.edu 249.0 answer 42<br />
 Set attribute &quot;answer&quot;.<br />
 % condor_qedit -name perdita 1849.0 In &#8216;&quot;myinput&quot;&#8217;<br />
 Set attribute &quot;In&quot;.<br />
 % condor_qedit jbasney NiceUser TRUE<br />
 Set attribute &quot;NiceUser&quot;.<br />
 % condor_qedit -constraint &#8216;JobUniverse == 1&#8217; Requirements &#8216;(Arch == &quot;INTEL&quot;) &amp;&amp; (OpSys == &quot;SOLARIS26&quot;) &amp;&amp; (Disk &gt;= ExecutableSize) &amp;&amp; (VirtualMemory &gt;= ImageSize)&#8217;<br />
 Set attribute &quot;Requirements&quot;. </p>
<h2>General Remarks</h2>
<p> A job&#8217;s ClassAd attributes may be viewed with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>condor_q -long </p>
<h2>Exit Status</h2>
<p> <i>condor_qedit</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
