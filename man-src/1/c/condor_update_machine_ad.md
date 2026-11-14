---
title: "condor_update_machine_ad(1)"
name: "condor_update_machine_ad"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_update_machine_ad/"
description: "condor_update_machine_ad update a machine ClassAd"
---

<h2>Name</h2>
<p> <i>condor_update_machine_ad</i> update a machine ClassAd </p>
<h2>Synopsis</h2>
<p> <i>condor_update_machine_ad</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_update_machine_ad</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>startdname</i> ] <i>path/to/update-ad</i> </p>
<h2>Description</h2>
<p> <i>condor_update_machine_ad</i> modifies the specified <i>condor_startd</i> daemon&#8217;s machine ClassAd. The ClassAd in the file given by path/to/update-ad represents the changed attributes. The changes persists until the <i>condor_startd</i> restarts. If no file is specified on the command line, <i>condor_update_machine_ad</i> reads the update ClassAd from stdin . </p>
<p> Contents of the file or stdin must contain a complete ClassAd. Each line <i>must</i> be terminated by a newline character, including the last line of the file. Lines are of the form </p>
<p> &lt;attribute&gt; = &lt;value&gt; </p>
<p> Changes to certain ClassAd attributes will cause the <i>condor_startd</i> to regenerate values for other ClassAd attributes. An example of this is setting HasVM . This will cause OfflineUniverses , VMOfflineTime , and VMOfflineReason to change. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the HTCondor version and exit</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>startdname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>startdname</i></p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> This tool is intended for the use of system administrators when dealing with offline universes. </p>
<h2>Examples</h2>
<p> To re-enable matching with the VM universe jobs, place on stdin a complete ClassAd (including the ending newline character) to change the value of ClassAd attribute HasVM : </p>
<p> echo &quot;HasVM = True<br />
 &quot; | condor_update_machine_ad </p>
<p> To prevent vm universe jobs from matching with the machine: </p>
<p> echo &quot;HasVM = False<br />
 &quot; | condor_update_machine_ad </p>
<p> To prevent vm universe jobs from matching with the machine and specify a reason: </p>
<p> echo &quot;HasVM = False<br />
 VMOfflineReason = \&quot;Cosmic rays.\&quot;<br />
 &quot; | condor_update_machine_ad </p>
<p> Note that the quotes around the reason are required by ClassAds, and they must be escaped because of the shell. Using a file instead of stdin may be preferable in these situations, because neither quoting nor escape characters are needed. </p>
<h2>Exit Status</h2>
<p> <i>condor_update_machine_ad</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
