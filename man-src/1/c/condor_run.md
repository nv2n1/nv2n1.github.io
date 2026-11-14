---
title: "condor_run(1)"
name: "condor_run"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_run/"
description: "condor_run Submit a shell command-line as an HTCondor job"
---

<h2>Name</h2>
<p> <i>condor_run</i> Submit a shell command-line as an HTCondor job </p>
<h2>Synopsis</h2>
<p> <i>condor_run</i> [ <code>-u </code> <i>universe</i> ] [ <code>-a </code> <i>submitcmd</i> ] <i>shell command</i> </p>
<h2>Description</h2>
<p> <i>condor_run</i> bundles a shell command line into an HTCondor job and submits the job. The <i>condor_run</i> command waits for the HTCondor job to complete, writes the job&#8217;s output to the terminal, and exits with the exit status of the HTCondor job. No output appears until the job completes. </p>
<p> Enclose the shell command line in double quote marks, so it may be passed to <i>condor_run</i> without modification. <i>condor_run</i> will not read input from the terminal while the job executes. If the shell command line requires input, redirect the input from a file, as illustrated by the example </p>
<p> % condor_run &quot;myprog &lt; input.data&quot; </p>
<p> <i>condor_run</i> jobs rely on a shared file system for access to any necessary input files. The current working directory of the job must be accessible to the machine within the HTCondor pool where the job runs. </p>
<p> Specialized environment variables may be used to specify requirements for the machine where the job may run. </p>
<p> <code>CONDOR_ARCH</code></p>
<dl>
<dt>
<dd> Specifies the architecture of the required platform. Values will be the same as the Arch machine ClassAd attribute.</p>
<dt>
<dd></dl>
<p> <code>CONDOR_OPSYS</code></p>
<dl>
<dt>
<dd> Specifies the operating system of the required platform. Values will be the same as the OpSys machine ClassAd attribute.</p>
<dt>
<dd></dl>
<p> <code>CONDOR_REQUIREMENTS</code></p>
<dl>
<dt>
<dd> Specifies any additional requirements for the HTCondor job. It is recommended that the value defined for CONDOR_REQUIREMENTS be enclosed in parenthesis.</p>
<dt>
<dd></dl>
<p> When one or more of these environment variables is specified, the job is submitted with: </p>
<p> Requirements = $CONDOR_REQUIREMENTS &amp;&amp; Arch == $CONDOR_ARCH &amp;&amp; \ </p>
<p>OpSys&nbsp;<wbr>==&nbsp;<wbr>$CONDOR_OPSYS </p>
<p> Without these environment variables, the job receives the default requirements expression, which requests a machine of the same platform as the machine on which <i>condor_run</i> is executed. </p>
<p> All environment variables set when <i>condor_run</i> is executed will be included in the environment of the HTCondor job. </p>
<p> <i>condor_run</i> removes the HTCondor job from the queue and deletes its temporary files, if <i>condor_run</i> is killed before the HTCondor job completes. </p>
<h2>Options</h2>
<p> <code>-u </code> <i>universe</i></p>
<dl>
<dt>
<dd> Submit the job under the specified universe. The default is vanilla. While any universe may be specified, only the vanilla, standard, scheduler, and local universes result in a submit description file that may work properly.</p>
<dt>
<dd></dl>
<p> <code>-a </code> <i>submitcmd</i></p>
<dl>
<dt>
<dd> Add the specified submit command to the implied submit description file for the job. To include spaces within <i>submitcmd</i> , enclose the submit command in double quote marks. And, to include double quote marks within <i>submitcmd</i> , enclose the submit command in single quote marks.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> <i>condor_run</i> may be used to compile an executable on a different platform. As an example, first set the environment variables for the required platform: </p>
<p> % setenv CONDOR_ARCH &quot;SUN4u&quot;<br />
 % setenv CONDOR_OPSYS &quot;SOLARIS28&quot; </p>
<p> Then, use <i>condor_run</i> to submit the compilation as in the following three examples. </p>
<p> % condor_run &quot;f77 -O -o myprog myprog.f&quot; </p>
<p> or </p>
<p> % condor_run &quot;make&quot; </p>
<p> or </p>
<p> % condor_run &quot;condor_compile cc -o myprog.condor myprog.c&quot; </p>
<h2>Files</h2>
<p> <i>condor_run</i> creates the following temporary files in the user&#8217;s working directory. The placeholder &lt;pid&gt; is replaced by the process id of <i>condor_run</i> . </p>
<p> <code>.condor_run.&lt;pid&gt; </code></p>
<dl>
<dt>
<dd> A shell script containing the shell command line.</p>
<dt>
<dd></dl>
<p> <code>.condor_submit.&lt;pid&gt; </code></p>
<dl>
<dt>
<dd> The submit description file for the job.</p>
<dt>
<dd></dl>
<p> <code>.condor_log.&lt;pid&gt; </code></p>
<dl>
<dt>
<dd> The HTCondor job&#8217;s log file; it is monitored by <i>condor_run</i> , to determine when the job exits.</p>
<dt>
<dd></dl>
<p> <code>.condor_out.&lt;pid&gt; </code></p>
<dl>
<dt>
<dd> The output of the HTCondor job before it is output to the terminal.</p>
<dt>
<dd></dl>
<p> <code>.condor_error.&lt;pid&gt; </code></p>
<dl>
<dt>
<dd> Any error messages for the HTCondor job before they are output to the terminal.</p>
<dt>
<dd> <i>condor_run</i> removes these files when the job completes. However, if <i>condor_run</i> fails, it is possible that these files will remain in the user&#8217;s working directory, and the HTCondor job may remain in the queue.</dl>
<h2>General Remarks</h2>
<p> <i>condor_run</i> is intended for submitting simple shell command lines to HTCondor. It does not provide the full functionality of <i>condor_submit</i> . Therefore, some <i>condor_submit</i> errors and system failures may not be handled correctly. </p>
<p> All processes specified within the single shell command line will be executed on the single machine matched with the job. HTCondor will not distribute multiple processes of a command line pipe across multiple machines. </p>
<p> <i>condor_run</i> will use the shell specified in the SHELL environment variable, if one exists. Otherwise, it will use <i>/bin/sh</i> to execute the shell command-line. </p>
<p> By default, <i>condor_run</i> expects Perl to be installed in /usr/bin/perl . If Perl is installed in another path, ask the Condor administrator to edit the path in the <i>condor_run</i> script, or explicitly call Perl from the command line: </p>
<p> % perl path-to-condor/bin/condor_run &quot;shell-cmd&quot; </p>
<h2>Exit Status</h2>
<p> <i>condor_run</i> exits with a status value of 0 (zero) upon complete success. The exit status of <i>condor_run</i> will be non-zero upon failure. The exit status in the case of a single error due to a system call will be the error number ( errno ) of the failed call. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
