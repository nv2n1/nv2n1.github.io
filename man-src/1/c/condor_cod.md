---
title: "condor_cod(1)"
name: "condor_cod"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_cod/"
description: "condor_cod manage COD machines and jobs"
---

<h2>Name</h2>
<p> <i>condor_cod</i> manage COD machines and jobs </p>
<h2>Synopsis</h2>
<p> <i>condor_cod</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_cod</i> <i>request</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> <code>-name </code> <i>scheddname</i> ][ <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i> ] [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] [ <code>-requirements expr</code> ] [ <code>-lease N</code> ] </p>
<p> <i>condor_cod</i> <i>release</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] [ <code>-fast</code> ] </p>
<p> <i>condor_cod</i> <i>activate</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] [ <code>-keyword string -jobad filename -cluster N -proc N -requirements expr</code> ] </p>
<p> <i>condor_cod</i> <i>deactivate</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] [ <code>-fast</code> ] </p>
<p> <i>condor_cod</i> <i>suspend</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] </p>
<p> <i>condor_cod</i> <i>renew</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] </p>
<p> <i>condor_cod</i> <i>resume</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] </p>
<p> <i>condor_cod</i> <i>delegate_proxy</i> <code>-id </code> <i>ClaimID</i> [[ <code>-help -version</code> ] [ <code>-debug -timeout N -classad file</code> ] ] [ <code>-x509proxy </code> <i>ProxyFile</i> ] </p>
<h2>Description</h2>
<p> <i>condor_cod</i> issues commands that manage and use COD claims on machines, given proper authorization. </p>
<p> Instead of specifying an argument of <i>request</i> , <i>release</i> , <i>activate</i> , <i>deactivate</i> , <i>suspend</i> , <i>renew</i> , or <i>resume</i> , the user may invoke the <i>condor_cod</i> tool by appending an underscore followed by one of these arguments. As an example, the following two commands are equivalent: </p>
<p>&nbsp;<wbr>condor_cod release -id&nbsp;<wbr>&quot;&lt;128.105.121.21:49973&gt;#1073352104#4&quot; </p>
<p>&nbsp;<wbr>condor_cod_release -id&nbsp;<wbr>&quot;&lt;128.105.121.21:49973&gt;#1073352104#4&quot; </p>
<p> To make these extended-name commands work, hard link the extended name to the <i>condor_cod</i> executable. For example on a Unix machine: </p>
<p> ln condor_cod_request condor_cod </p>
<p> The <i>request</i> argument gives a claim ID, and the other commands ( <i>release</i> , <i>activate</i> , <i>deactivate</i> , <i>suspend</i> , and <i>resume</i> ) use the claim ID. The claim ID is given as the last line of output for a <i>request</i> , and the output appears of the form: </p>
<p> ID of new claim is: &quot;&lt;a.b.c.d:portnumber&gt;#x#y&quot; </p>
<p> An actual example of this line of output is </p>
<p> ID of new claim is: &quot;&lt;128.105.121.21:49973&gt;#1073352104#4&quot; </p>
<p> The HTCondor manual has a complete description of COD. </p>
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
<p> <code>-name </code> <i>scheddname</i></p>
<dl>
<dt>
<dd> Send the command to a machine identified by <i>scheddname</i></p>
<dt>
<dd></dl>
<p> <code>-addr </code> <i>&lt;a.b.c.d:port&gt;</i></p>
<dl>
<dt>
<dd> Send the command to a machine located at <i>&lt;a.b.c.d:port&gt;</i></p>
<dt>
<dd></dl>
<p> <code>-lease </code> <i>N</i></p>
<dl>
<dt>
<dd> For the <code>request</code> of a new claim, automatically release the claim after <i>N</i> seconds.</p>
<dt>
<dd></dl>
<p> <code>request</code></p>
<dl>
<dt>
<dd> Create a new COD claim</p>
<dt>
<dd></dl>
<p> <code>release</code></p>
<dl>
<dt>
<dd> Relinquish a claim and kill any running job</p>
<dt>
<dd></dl>
<p> <code>activate</code></p>
<dl>
<dt>
<dd> Start a job on a given claim</p>
<dt>
<dd></dl>
<p> <code>deactivate</code></p>
<dl>
<dt>
<dd> Kill the current job, but keep the claim</p>
<dt>
<dd></dl>
<p> <code>suspend</code></p>
<dl>
<dt>
<dd> Suspend the job on a given claim</p>
<dt>
<dd></dl>
<p> <code>renew</code></p>
<dl>
<dt>
<dd> Renew the lease to the COD claim</p>
<dt>
<dd></dl>
<p> <code>resume</code></p>
<dl>
<dt>
<dd> Resume the job on a given claim</p>
<dt>
<dd></dl>
<p> <code>delegate_proxy</code></p>
<dl>
<dt>
<dd> Delegate an X509 proxy for the given claim</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<h2>Examples</h2>
<h2>Exit Status</h2>
<p> <i>condor_cod</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
