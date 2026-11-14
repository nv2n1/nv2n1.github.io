---
title: "condor_version(1)"
name: "condor_version"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_version/"
description: "condor_version print HTCondor version and platform information"
---

<h2>Name</h2>
<p> <i>condor_version</i> print HTCondor version and platform information </p>
<h2>Synopsis</h2>
<p> <i>condor_version</i> [ <code>-help</code> ] </p>
<p> <i>condor_version</i> [ <code>-arch</code> ] [ <code>-opsys</code> ] [ <code>-syscall</code> ] </p>
<h2>Description</h2>
<p> With no arguments, <i>condor_version</i> prints the currently installed HTCondor version number and platform information. The version number includes a build identification number, as well as the date built. </p>
<h2>Options</h2>
<p> <code>help</code></p>
<dl>
<dt>
<dd> Print usage information</p>
<dt>
<dd></dl>
<p> <code>arch</code></p>
<dl>
<dt>
<dd> Print this machine&#8217;s ClassAd value for Arch</p>
<dt>
<dd></dl>
<p> <code>opsys</code></p>
<dl>
<dt>
<dd> Print this machine&#8217;s ClassAd value for OpSys</p>
<dt>
<dd></dl>
<p> <code>syscall</code></p>
<dl>
<dt>
<dd> Get any requested version and/or platform information from the libcondorsyscall.a that this HTCondor pool is configured to use, instead of using the values that are compiled into the tool itself. This option may be used in combination with any other options to modify where the information is coming from.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_version</i> will exit with a status value of 0 (zero) upon success, and it should never exit with a failing value. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
