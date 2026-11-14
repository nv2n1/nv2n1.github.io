---
title: "condor_fetchlog(1)"
name: "condor_fetchlog"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_fetchlog/"
description: "condor_fetchlog Retrieve a daemon’s log file that is located on another computer"
---

<h2>Name</h2>
<p> <i>condor_fetchlog</i> Retrieve a daemon&#8217;s log file that is located on another computer </p>
<h2>Synopsis</h2>
<p> <i>condor_fetchlog</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_fetchlog</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-master -startd -schedd -collector -negotiator -kbdd</code> ] <i>machine-name</i> <i>subsystem[.extension]</i> </p>
<h2>Description</h2>
<p> <i>condor_fetchlog</i> contacts HTCondor running on the machine specified by <i>machine-name</i> , and asks it to return a log file from that machine. Which log file is determined from the <i>subsystem[.extension]</i> argument. The log file is printed to standard output. This command eliminates the need to remotely log in to a machine in order to retrieve a daemon&#8217;s log file. </p>
<p> For security purposes of authentication and authorization, this command requires ADMINISTRATOR level of access. </p>
<p> The <i>subsystem[.extension]</i> argument is utilized to construct the log file&#8217;s name. Without an optional <i>.extension</i> , the value of the configuration variable named <i>subsystem</i> _LOG defines the log file&#8217;s name. When specified, the <i>.extension</i> is appended to this value. </p>
<p> The <i>subsystem</i> argument is any value $(SUBSYSTEM) that has a defined configuration variable of $(SUBSYSTEM)_LOG , or any of</p>
<dl>
<dt>
<dd> * NEGOTIATOR_MATCH</p>
<dt>
<dd> * HISTORY</p>
<dt>
<dd> * STARTD_HISTORY</dl>
<p> A value for the optional <i>.extension</i> to the <i>subsystem</i> argument is typically one of the three strings:</p>
<dl>
<dt>
<dd> 1. .old</p>
<dt>
<dd> 2. .slot&lt;X&gt;</p>
<dt>
<dd> 3. .slot&lt;X&gt;.old Within these strings, &lt;X&gt; is substituted with the slot number.</dl>
<p> A <i>subsystem</i> argument of STARTD_HISTORY fetches all <i>condor_startd</i> history by concatenating all instances of log files resulting from rotation. </p>
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
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number</p>
<dt>
<dd></dl>
<p> <code>-master</code></p>
<dl>
<dt>
<dd> Send the command to the <i>condor_master</i> daemon (default)</p>
<dt>
<dd></dl>
<p> <code>-startd</code></p>
<dl>
<dt>
<dd> Send the command to the <i>condor_startd</i> daemon</p>
<dt>
<dd></dl>
<p> <code>-schedd</code></p>
<dl>
<dt>
<dd> Send the command to the <i>condor_schedd</i> daemon</p>
<dt>
<dd></dl>
<p> <code>-collector</code></p>
<dl>
<dt>
<dd> Send the command to the <i>condor_collector</i> daemon</p>
<dt>
<dd></dl>
<p> <code>-kbdd</code></p>
<dl>
<dt>
<dd> Send the command to the <i>condor_kbdd</i> daemon</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> To get the <i>condor_negotiator</i> daemon&#8217;s log from a host named head.example.com from within the current pool: </p>
<p> condor_fetchlog head.example.com NEGOTIATOR </p>
<p> To get the <i>condor_startd</i> daemon&#8217;s log from a host named execute.example.com from within the current pool: </p>
<p> condor_fetchlog execute.example.com STARTD </p>
<p> This command requested the <i>condor_startd</i> daemon&#8217;s log from the <i>condor_master</i> . If the <i>condor_master</i> has crashed or is unresponsive, ask another daemon running on that computer to return the log. For example, ask the <i>condor_startd</i> daemon to return the <i>condor_master</i> </p>
<p> condor_fetchlog -startd execute.example.com MASTER </p>
<h2>Exit Status</h2>
<p> <i>condor_fetchlog</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
