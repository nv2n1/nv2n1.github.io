---
title: "condor_preen(1)"
name: "condor_preen"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_preen/"
description: "condor_preen remove extraneous files from HTCondor directories"
---

<h2>Name</h2>
<p> <i>condor_preen</i> remove extraneous files from HTCondor directories </p>
<h2>Synopsis</h2>
<p> <i>condor_preen</i> [ <code>-mail</code> ] [ <code>-remove</code> ] [ <code>-verbose</code> ] [ <code>-debug</code> ] </p>
<h2>Description</h2>
<p> <i>condor_preen</i> examines the directories belonging to HTCondor, and removes extraneous files and directories which may be left over from HTCondor processes which terminated abnormally either due to internal errors or a system crash. The directories checked are the LOG , EXECUTE , and SPOOL directories as defined in the HTCondor configuration files. <i>condor_preen</i> is intended to be run as user root or user condor periodically as a backup method to ensure reasonable file system cleanliness in the face of errors. This is done automatically by default by the <i>condor_master</i> daemon. It may also be explicitly invoked on an as needed basis. </p>
<p> When <i>condor_preen</i> cleans the SPOOL directory, it always leaves behind the files specified in the configuration variables VALID_SPOOL_FILES and SYSTEM_VALID_SPOOL_FILES , as given by the configuration. For the LOG directory, the only files removed or reported are those listed within the configuration variable INVALID_LOG_FILES list. The reason for this difference is that, in general, the files in the LOG directory ought to be left alone, with few exceptions. An example of exceptions are core files. As there are new log files introduced regularly, it is less effort to specify those that ought to be removed than those that are not to be removed. </p>
<h2>Options</h2>
<p> <code>-mail</code></p>
<dl>
<dt>
<dd> Send mail to the user defined in the PREEN_ADMIN configuration variable, instead of writing to the standard output.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-remove</code></p>
<dl>
<dt>
<dd> Remove the offending files and directories rather than reporting on them.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> List all files found in the Condor directories, even those which are not considered extraneous.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Print extra debugging information as the command executes.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_preen</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
