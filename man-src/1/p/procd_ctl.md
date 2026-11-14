---
title: "procd_ctl(1)"
name: "procd_ctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-procd_ctl/"
description: "procd_ctl command line interface to the condor_procd"
---

<h2>Name</h2>
<p> procd_ctl command line interface to the <i>condor_procd</i> </p>
<h2>Synopsis</h2>
<p> <code>procd_ctl</code> <code>-h</code> </p>
<p> <code>procd_ctl</code> <code>-A </code> <i>address-file</i> [ <code>command</code> ] </p>
<h2>Description</h2>
<p> This is a programmatic interface to the <i>condor_procd</i> daemon. It may be used to cause the <i>condor_procd</i> to do anything that the <i>condor_procd</i> is capable of doing, such as tracking and managing process families. </p>
<p> This is a program only available for the Linux ports of HTCondor. </p>
<p> The <code>-h</code> option prints out usage information and exits. The <i>address-file</i> specification within the <code>-A</code> argument specifies the path and file name of the address file which the named pipe clients must use to speak with the <i>condor_procd</i> . </p>
<p> One command is given to the <i>condor_procd</i> . The choices for the command are defined by the Options. </p>
<h2>Options</h2>
<p> <code>TRACK_BY_ASSOCIATED_GID</code> <i>GID</i> [ <i>PID</i> ]</p>
<dl>
<dt>
<dd> Use the specified <i>GID</i> to track the specified family rooted at <i>PID</i> . If the optional <i>PID</i> is not specified, then the PID used is the one given or assumed by <i>condor_procd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>GET_USAGE</code> [ <i>PID</i> ]</p>
<dl>
<dt>
<dd> Get the total usage information about the PID family at <i>PID</i> . If the optional <i>PID</i> is not specified, then the PID used is the one given or assumed by <i>condor_procd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>DUMP</code> [ <i>PID</i> ]</p>
<dl>
<dt>
<dd> Print out information about both the root <i>PID</i> being watched and the tree of processes under this root <i>PID</i> . If the optional <i>PID</i> is not specified, then the PID used is the one given or assumed by <i>condor_procd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>LIST</code> [ <i>PID</i> ]</p>
<dl>
<dt>
<dd> With no <i>PID</i> given, print out information about all the watched processes. If the optional <i>PID</i> is specified, print out information about the process specified by <i>PID</i> and all its child processes.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>SIGNAL_PROCESS</code> <i>signal</i> [ <i>PID</i> ]</p>
<dl>
<dt>
<dd> Send the <i>signal</i> to the process specified by <i>PID</i> . If the optional <i>PID</i> is not specified, then the PID used is the one given or assumed by <i>condor_procd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>SUSPEND_FAMILY</code> <i>PID</i></p>
<dl>
<dt>
<dd> Suspend the process family rooted at <i>PID</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>CONTINUE_FAMILY</code> <i>PID</i></p>
<dl>
<dt>
<dd> Continue execution of the process family rooted at <i>PID</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>KILL_FAMILY</code> <i>PID</i></p>
<dl>
<dt>
<dd> Kill the process family rooted at <i>PID</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UNREGISTER_FAMILY</code> <i>PID</i></p>
<dl>
<dt>
<dd> Stop tracking the process family rooted at <i>PID</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>SNAPSHOT</code></p>
<dl>
<dt>
<dd> Perform a snapshot of the tracked family tree.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>QUIT</code></p>
<dl>
<dt>
<dd> Disconnect from the <i>condor_procd</i> and exit.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> This program may be used in a standalone mode, independent of HTCondor, to track process families. The programs <i>procd_ctl</i> and <i>gidd_alloc</i> are used with the <i>condor_procd</i> in standalone mode to interact with the daemon and inquire about certain state of running processes on the machine, respectively. </p>
<h2>Exit Status</h2>
<p> <i>procd_ctl</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
