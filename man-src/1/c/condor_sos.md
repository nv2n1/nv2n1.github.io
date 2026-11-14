---
title: "condor_sos(1)"
name: "condor_sos"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_sos/"
description: "condor_sos Issue a command that will be service with a higher priority"
---

<h2>Name</h2>
<p> <i>condor_sos</i> Issue a command that will be service with a higher priority </p>
<h2>Synopsis</h2>
<p> <i>condor_sos</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_sos</i> [ <code>-debug</code> ] [ <code>-timeoutmult </code> <i>value</i> ] <i>condor_command</i> </p>
<h2>Description</h2>
<p> <i>condor_sos</i> sends the <i>condor_command</i> in such a way that the command is serviced ahead of other waiting commands. It appears to have a higher priority than other waiting commands. </p>
<p> <i>condor_sos</i> is intended to give administrators a way to query the <i>condor_schedd</i> and <i>condor_collector</i> daemons when they are under such a heavy load that they are not responsive. </p>
<p> There must be a special command port configured, in order for a command to be serviced with priority. The <i>condor_schedd</i> and <i>condor_collector</i> always have the special command port. Other daemons require configuration by setting configuration variable &lt;SUBSYS&gt;_SUPER_ADDRESS_FILE . </p>
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
<dd> Print extra debugging information as the command executes.</p>
<dt>
<dd></dl>
<p> <code>-timeoutmult </code> <i>value</i></p>
<dl>
<dt>
<dd> Multiply any timeouts set for the command by the integer <i>value</i> .</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> The example command </p>
<p>&nbsp;<wbr>&nbsp;<wbr>condor_sos -timeoutmult 5 condor_hold -all </p>
<p> causes the condor_hold -all command to be handled by the <i>condor_schedd</i> with priority over any other commands that the <i>condor_schedd</i> has waiting to be serviced. It also extends any set timeouts by a factor of 5. </p>
<h2>Exit Status</h2>
<p> <i>condor_sos</i> will exit with the value 1 on error and with the exit value of the invoked command when the command is successfully invoked. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
