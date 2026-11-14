---
title: "condor_master(1)"
name: "condor_master"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_master/"
description: "condor_master The master HTCondor Daemon"
---

<h2>Name</h2>
<p> <i>condor_master</i> The master HTCondor Daemon </p>
<h2>Synopsis</h2>
<p> <i>condor_master</i> </p>
<h2>Description</h2>
<p> This daemon is responsible for keeping all the rest of the HTCondor daemons running on each machine in your pool. It spawns the other daemons, and periodically checks to see if there are new binaries installed for any of them. If there are, the <i>condor_master</i> will restart the affected daemons. In addition, if any daemon crashes, the <i>condor_master</i> will send e-mail to the HTCondor Administrator of your pool and restart the daemon. The <i>condor_master</i> also supports various administrative commands that let you start, stop or reconfigure daemons remotely. The <i>condor_master</i> will run on every machine in your HTCondor pool, regardless of what functions each machine are performing. Additionally, on Linux platforms, if you start the <i>condor_master</i> as root, it will tune (but never decrease) certain kernel parameters important to HTCondor&#8217;s performance. </p>
<p> The DAEMON_LIST configuration macro is used by the <i>condor_master</i> to provide a per-machine list of daemons that should be started and kept running. For daemons that are specified in the DC_DAEMON_LIST configuration macro, the <i>condor_master</i> daemon will spawn them automatically appending a <i>-f</i> argument. For those listed in DAEMON_LIST , but not in DC_DAEMON_LIST , there will be no <i>-f</i> argument. </p>
<h2>Options</h2>
<p> <code>-n </code> <i>name</i></p>
<dl>
<dt>
<dd> Provides an alternate name for the <i>condor_master</i> to override that given by the MASTER_NAME configuration variable.</p>
<dt>
<dd></dl>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
