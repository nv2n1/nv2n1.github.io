---
title: "condor_reschedule(1)"
name: "condor_reschedule"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_reschedule/"
description: "condor_reschedule Update scheduling information to the central manager"
---

<h2>Name</h2>
<p> <i>condor_reschedule</i> Update scheduling information to the central manager </p>
<h2>Synopsis</h2>
<p> <i>condor_reschedule</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_reschedule</i> [ <code>-debug</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>hostname</i> <i>hostname</i> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> <i>&lt;a.b.c.d:port&gt;</i> <code>-constraint </code> <i>expression</i> <code>-all</code> ] </p>
<h2>Description</h2>
<p> <i>condor_reschedule</i> updates the information about a set of machines&#8217; resources and jobs to the central manager. This command is used to force an update before viewing the current status of a machine. Viewing the status of a machine is done with the <i>condor_status</i> command. <i>condor_reschedule</i> also starts a new negotiation cycle between resource owners and resource providers on the central managers, so that jobs can be matched with machines right away. This can be useful in situations where the time between negotiation cycles is somewhat long, and an administrator wants to see if a job in the queue will get matched without waiting for the next negotiation cycle. </p>
<p> A new negotiation cycle cannot occur more frequently than every 20 seconds. Requests for new negotiation cycle within that 20 second window will be deferred until 20 seconds have passed since that last cycle. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display version information</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>hostname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>hostname</i></p>
<dt>
<dd></dl>
<p> <i>hostname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>hostname</i></p>
<dt>
<dd></dl>
<p> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine&#8217;s master located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> Apply this command only to machines matching the given ClassAd <i>expression</i></p>
<dt>
<dd></dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> Send the command to all machines in the pool</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_reschedule</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To update the information on three named machines: </p>
<p> % condor_reschedule robin cardinal bluejay </p>
<p> To reschedule on a machine within a pool other than the local pool, use the <code>-pool</code> option. The argument is the name of the central manager for the pool. Note that one or more machines within the pool must be specified as the targets for the command. This command reschedules the single machine named <code>cae17</code> within the pool of machines that has <code>condor.cae.wisc.edu</code> as its central manager: </p>
<p> % condor_reschedule -pool condor.cae.wisc.edu -name cae17 </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
