---
title: "condor_urlfetch(1)"
name: "condor_urlfetch"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_urlfetch/"
description: "condor_urlfetch fetch configuration given a URL"
---

<h2>Name</h2>
<p> <i>condor_urlfetch</i> fetch configuration given a URL </p>
<h2>Synopsis</h2>
<p> <i>condor_urlfetch</i> [ <code>-&lt;daemon&gt;</code> ] <i>url</i> <i>local-url-cache-file</i> </p>
<h2>Description</h2>
<p> Depending on the command line arguments, <i>condor_urlfetch</i> sends the result of a query from the <i>url</i> to both standard output and to a file specified by <i>local-url-cache-file</i> , or it sends the contents of the file specified by <i>local-url-cache-file</i> to standard output. </p>
<p> <i>condor_urlfetch</i> is intended to be used as the program to run when defining configuration, such as in the nonfunctional example: </p>
<p> LOCAL_CONFIG_FILE = $(LIBEXEC)/condor_urlfetch -$(SUBSYSTEM) \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.example.com/htcondor-baseconfig">http://www.example.com/htcondor-baseconfig</a>&nbsp;<wbr>&nbsp;<wbr>local.config | </p>
<p> The pipe character (| ) at the end of this definition of the location of a configuration file changes the use of the definition. It causes the command listed on the right hand side of this assignment statement to be invoked, and standard output becomes the configuration. The value of $(SUBSYSTEM) becomes the daemon that caused this configuration to be read. If $(SUBSYSTEM) evaluates to MASTER , then the URL query always occurs, and the result is sent to standard output as well as written to the file specified by argument <i>local-url-cache-file</i> . When $(SUBSYSTEM) evaluates to a daemon other than MASTER , then the URL query only occurs if the file specified by <i>local-url-cache-file</i> does <i>not</i> exist. If the file specified by <i>local-url-cache-file</i> does exist, then the contents of this file is sent to standard output. </p>
<p> Note that if the configuration kept at the URL site changes, and reconfiguration is requested, the <code>-&lt;daemon&gt;</code> argument needs to be -MASTER . This is the only way to guarantee that there will be a query of the changed URL contents, such that they will make their way into the configuration. </p>
<h2>Options</h2>
<p> <code>-&lt;daemon&gt;</code></p>
<dl>
<dt>
<dd> The upper case name of the daemon issuing the request for the configuration output. If -MASTER , then the URL query always occurs. If a daemon other than -MASTER , for example STARTD or SCHEDD , then the URL query only occurs if the file defined by <i>local-url-cache-file</i> does not exist.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_urlfetch</i> will exit with a status value of 0 (zero) upon success and non zero otherwise. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
