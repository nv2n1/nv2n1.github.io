---
title: "condor_rmdir(1)"
name: "condor_rmdir"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_rmdir/"
description: "condor_rmdir Windows-only no-fail deletion of directories"
---

<h2>Name</h2>
<p> <i>condor_rmdir</i> Windows-only no-fail deletion of directories </p>
<h2>Synopsis</h2>
<p> <i>condor_rmdir</i> [ <code>/HELP | /?</code> ] </p>
<p> <i>condor_rmdir</i> <i>@filename</i> </p>
<p> <i>condor_rmdir</i> [ <code>/VERBOSE</code> ] [ <code>/DIAGNOSTIC</code> ] [ <code>/PATH:&lt;path&gt;</code> ] [ <code>/S</code> ] [ <code>/C</code> ] [ <code>/Q</code> ] [ <code>/NODEL</code> ] <i>directory</i> </p>
<h2>Description</h2>
<p> <i>condor_rmdir</i> can delete a specified <i>directory</i> , and will not fail if the directory contains files that have ACLs that deny the SYSTEM process delete access, unlike the built-in Windows <i>rmdir</i> command. </p>
<p> The directory to be removed together with other command line arguments may be specified within a file named <i>filename</i> , prefixing this argument with an @ character. </p>
<p> The <i>condor_rmdir.exe</i> executable is is intended to be used by HTCondor with the <code>/S</code> <code>/C</code> options, which cause it to recurse into subdirectories and continue on errors. </p>
<h2>Options</h2>
<p> <code>/HELP</code></p>
<dl>
<dt>
<dd> Print usage information.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/?</code></p>
<dl>
<dt>
<dd> Print usage information.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/VERBOSE</code></p>
<dl>
<dt>
<dd> Print detailed output.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/DIAGNOSTIC</code></p>
<dl>
<dt>
<dd> Print out the internal flow of control information.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/PATH:&lt;path&gt;</code></p>
<dl>
<dt>
<dd> Remove the directory given by <code>&lt;path&gt;</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/S</code></p>
<dl>
<dt>
<dd> Include subdirectories in those removed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/C</code></p>
<dl>
<dt>
<dd> Continue even if access is denied.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/Q</code></p>
<dl>
<dt>
<dd> Print error output only.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>/NODEL</code></p>
<dl>
<dt>
<dd> Do not remove directories. ACLs may still be changed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_rmdir</i> will exit with a status value of 0 (zero) upon success, and it will exit with the standard HRESULT error code upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
