---
title: "condor_tail(1)"
name: "condor_tail"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_tail/"
description: "condor_tail Display the last contents of a running job’s standard output or file"
---

<h2>Name</h2>
<p> <i>condor_tail</i> Display the last contents of a running job&#8217;s standard output or file </p>
<h2>Synopsis</h2>
<p> <i>condor_tail</i> [ <code>-help</code> ] | [ <code>-version</code> ] </p>
<p> <i>condor_tail</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>-name </code> <i>name</i> ] [ <code>-debug</code> ] [ <code>-maxbytes </code> <i>numbytes</i> ] [ <code>-auto-retry</code> ] [ <code>-follow</code> ] [ <code>-no-stdout</code> ] [ <code>-stderr</code> ] <i>job-ID</i> [ <i>-filename1</i> ] [ <i>, -filename2 &#8230; </i> ] </p>
<h2>Description</h2>
<p> <i>condor_tail</i> displays the last bytes of a file in the sandbox of a running job identified by the command line argument <i>job-ID</i> . stdout is tailed by default. The number of bytes displayed is limited to 1024, unless changed by specifying the <code>-maxbytes</code> option. This limit is applied for each individual tail of a file; for example, when following a file, the limit is applied each subsequent time output is obtained. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number.</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>name</i></p>
<dl>
<dt>
<dd> Query the <i>condor_schedd</i> daemon identified with <i>name</i> .</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Display extra debugging information.</p>
<dt>
<dd></dl>
<p> <code>-maxbytes </code> <i>numbytes</i></p>
<dl>
<dt>
<dd> Limits the maximum number of bytes transferred per tail access. If not specified, the maximum number of bytes is 1024.</p>
<dt>
<dd></dl>
<p> <code>-auto-retry</code></p>
<dl>
<dt>
<dd> Retry the tail of the file(s) every 2 seconds, if the job is not yet running.</p>
<dt>
<dd></dl>
<p> <code>-follow</code></p>
<dl>
<dt>
<dd> Repetitively tail the file(s), until interrupted.</p>
<dt>
<dd></dl>
<p> <code>-no-stdout</code></p>
<dl>
<dt>
<dd> Do not tail stdout .</p>
<dt>
<dd></dl>
<p> <code>-stderr</code></p>
<dl>
<dt>
<dd> Tail stderr instead of stdout .</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> The exit status of <i>condor_tail</i> is zero on success. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
