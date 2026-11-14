---
title: "condor_procd(1)"
name: "condor_procd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_procd/"
description: "condor_procd Track and manage process families"
---

<h2>Name</h2>
<p> <i>condor_procd</i> Track and manage process families </p>
<h2>Synopsis</h2>
<p> <i>condor_procd</i> <code>-h</code> </p>
<p> <i>condor_procd</i> <code>-A </code> <i>address-file</i> [ <code>options</code> ] </p>
<h2>Description</h2>
<p> <i>condor_procd</i> tracks and manages process families on behalf of the HTCondor daemons. It may track families of PIDs via relationships such as: direct parent/child, environment variables, UID, and supplementary group IDs. Management of the PID families include</p>
<dl>
<dt>
<dd> * registering new families or new members of existing families</p>
<dt>
<dd> * getting usage information</p>
<dt>
<dd> * signaling families for operations such as suspension, continuing, or killing the family</p>
<dt>
<dd> * getting a snapshot of the tree of families In a regular HTCondor installation, this program is not intended to be used or executed by any human.</dl>
<p> The required argument, <code>-A </code> <i>address-file</i> , is the path and file name of the address file which is the named pipe that clients must use to speak with the <i>condor_procd</i> . </p>
<h2>Options</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print out usage information and exit.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> Wait for the debugger. Initially sleep 30 seconds before beginning normal function.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-C </code> <i>principal</i></p>
<dl>
<dt>
<dd> The <i>principal</i> is the UID of the owner of the named pipe that clients must use to speak to the <i>condor_procd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-L </code> <i>log-file</i></p>
<dl>
<dt>
<dd> A file the <i>condor_procd</i> will use to write logging information.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-E</code></p>
<dl>
<dt>
<dd> When specified, another tool such as the <i>procd_ctl</i> tool must allocate the GID associated with a process. When this option is <i>not</i> specified, the <i>condor_procd</i> will allocate the GID itself.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-P </code> <i>PID</i></p>
<dl>
<dt>
<dd> If not specified, the <i>condor_procd</i> will use the <i>condor_procd</i> <i>condor_procd</i> and the root of the tracking family. When not specified, if the <i>condor_procd</i> <i>condor_procd</i> exits. When specified, the <i>condor_procd</i> will track this <i>PID</i> family in question and not also exit if the PID exits.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-S </code> <i>seconds</i></p>
<dl>
<dt>
<dd> The maximum number of seconds the <i>condor_procd</i> will wait between taking snapshots of the tree of families. Different clients to the <i>condor_procd</i> can specify different snapshot times. The quickest snapshot time is the one performed by the <i>condor_procd</i> . When this option is not specified, a default value of 60 seconds is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-G </code> <i>min-gid max-gid</i></p>
<dl>
<dt>
<dd> If the <code>-E</code> option is <i>not</i> specified, then track process families using a self-allocated, free GID out of the inclusive range specified by <i>min-gid</i> and <i>max-gid</i> . This means that if a new process shows up using a previously known GID, the new process will automatically associate into the process family assigned that GID. If the <code>-E</code> option <i>is</i> specified, then instead of self-allocating the GID, the <i>procd_ctl</i> tool must be used to associate the GID with the PID root of the family. The associated GID must still be in the range specified. This is a Linux-only feature.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-K </code> <i>windows-softkill-binary</i></p>
<dl>
<dt>
<dd> This is the path and executable name of the <i>condor_softkill.exe</i> binary. It is used to send softkill signals to process families. This is a Windows-only feature.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-I </code> <i>glexec-kill-path glexec-path</i></p>
<dl>
<dt>
<dd> Specifies, with <i>glexec-kill-path</i> , the path and executable name of a binary used to send a signal to a PID. The <i>glexec</i> binary, specified by <i>glexec-path</i> , executes the program specified with <i>glexec-kill-path</i> under the right privileges to send the signal.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> This program may be used in a stand alone mode, independent of HTCondor, to track process families. The programs <i>procd_ctl</i> and <i>gidd_alloc</i> are used with the <i>condor_procd</i> in stand alone mode to interact with the daemon and to inquire about certain state of running processes on the machine, respectively. </p>
<h2>Exit Status</h2>
<p> <i>condor_procd</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
