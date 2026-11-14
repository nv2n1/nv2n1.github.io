---
title: "globus-job-run(1)"
name: "globus-job-run"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-job-run/"
description: "globus-job-run – Execute a job using GRAM"
---

<h2 class="name">NAME</h2>
<p> globus-job-run &#8211; Execute a job using GRAM </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-job-run</code> [-dumprsl|-dryrun|-verify] [-file ARGUMENT_FILE] <i>SERVICE-CONTACT</i> [OPTIONS] <i>EXECUTABLE</i> <i>ARGUMENT&#8230;</i> </p>
<p> <code>globus-job-run</code> [-help | -usage | -version | -versions]</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-job-run</code> program constructs a job description from its command-line options and then submits the job to the GRAM service running at <i>SERVICE_CONTACT</i>. The executable and arguments to the executable are provided on the command-line after all other options. Note that the <i>-dumprsl</i>, <i>-dryrun</i>, <i>-verify</i>, and <i>-file</i> command-line options must occur before the first non-option argument, the <i>SERVICE_CONTACT</i>. </p>
<p> The <code>globus-job-run</code> provides similar functionality to <code>globusrun</code> in that it allows interactive start-up of GRAM jobs. However, unlike <code>globusrun</code>, it uses command-line parameters to define the job instead of RSL expressions.</p>
<h2>OPTIONS</h2>
<p> The full set of options to <code>globus-job-run</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display a help message to standard error and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-run</code> program to standard output.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of the <code>globus-job-run</code> program including DiRT information to standard output.</dl>
<p> <code>-dumprsl</code></p>
<dl>
<dt>
<dd> Translate the command-line options to <code>globus-job-run</code> into an RSL expression that can be used with tools such as <code>globusrun</code>.</dl>
<p> <code>-dryrun</code></p>
<dl>
<dt>
<dd> Submit the job request to the GRAM service with the dryrun option enabled. When this option is used, the GRAM service prepares to execute the job but stops before submitting the job to the LRM. This can be used to diagnose some problems such as missing files.</dl>
<p> <code>-verify</code></p>
<dl>
<dt>
<dd> Submit the job request to the GRAM service with the dryrun option enabled and then without it enabled if the dryrun is successful.</dl>
<p> <code>-file </code><i>ARGUMENT_FILE</i></p>
<dl>
<dt>
<dd> Read additional command-line options from <i>ARGUMENT_FILE</i>.</dl>
<p> <code>-np </code><i>PROCESSES</i><code>, -count </code><i>PROCESSES</i></p>
<dl>
<dt>
<dd> Start <i>PROCESSES</i> instances of the executable as a single job.</dl>
<p> <code>-m </code><i>MAX_TIME</i><code>, -maxtime </code><i>MAX_TIME</i></p>
<dl>
<dt>
<dd> Schedule the job to run for a maximum of <i>MAX_TIME</i> minutes.</dl>
<p> <code>-p </code><i>PROJECT</i><code>, -project </code><i>PROJECT</i></p>
<dl>
<dt>
<dd> Request that the job use the allocation <i>PROJECT</i> when submitting the job to the LRM.</dl>
<p> <code>-q </code><i>QUEUE</i><code>, -queue </code><i>QUEUE</i></p>
<dl>
<dt>
<dd> Request that the job be submitted to the LRM using the named <i>QUEUE</i>.</dl>
<p> <code>-d </code><i>DIRECTORY</i><code>, -directory </code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Run the job in the directory named by <i>DIRECTORY</i>. Input and output files will be interpreted relative to this directory. This directory must exist on the file system on the LRM-managed resource. If not specified, the job will run in the home directory of the user the job is running as.</dl>
<p> <code>-env </code><i>NAME</i><code>=</code><i>VALUE</i></p>
<dl>
<dt>
<dd> Define an environment variable named by <i>NAME</i> with the value <i>VALUE</i> in the job environment. This option may be specified multiple times to define multiple environment variables.</dl>
<p> <code>-stdin [-l | -s] </code><i>STDIN_FILE</i></p>
<dl>
<dt>
<dd> Use the file named by <i>STDIN_FILE</i> as the standard input of the job. If the <i>-l</i> option is specified, then this file is interpreted to be on a file system local to the LRM. If the <i>-s</i> option is specified, then this file is interpreted to be on the file system where <code>globus-job-run</code> is being executed, and the file will be staged via GASS. If neither is specified, the local behavior is assumed.</dl>
<p> <code>-stdout [-l | -s] </code><i>STDOUT_FILE</i></p>
<dl>
<dt>
<dd> Use the file named by <i>STDOUT_FILE</i> as the destination for the standard output of the job. If the <i>-l</i> option is specified, then this file is interpreted to be on a file system local to the LRM. If the <i>-s</i> option is specified, then this file is interpreted to be on the file system where <code>globus-job-run</code> is being executed, and the file will be staged via GASS. If neither is specified, the local behavior is assumed.</dl>
<p> <code>-stderr [-l | -s] </code><i>STDERR_FILE</i></p>
<dl>
<dt>
<dd> Use the file named by <i>STDERR_FILE</i> as the destination for the standard error of the job. If the <i>-l</i> option is specified, then this file is interpreted to be on a file system local to the LRM. If the <i>-s</i> option is specified, then this file is interpreted to be on the file system where <code>globus-job-run</code> is being executed, and the file will be staged via GASS. If neither is specified, the local behavior is assumed.</dl>
<p> <code>-x </code><i>RSL_CLAUSE</i></p>
<dl>
<dt>
<dd> Add a set of custom RSL attributes described by <i>RSL_CLAUSE</i> to the job description. The clause must be an RSL conjunction and may contain one or more attributes. This can be used to include attributes which can not be defined by other command-line options of <code>globus-job-run</code>.</dl>
<p> <code>-l, -s</code></p>
<dl>
<dt>
<dd> When included outside the context of <i>-stdin</i>, <i>-stdout</i>, or <i>-stderr</i> command-line options, <i>-l</i> option alters the interpretation of the executable path. If the <i>-l</i> option is specified, then the executable is interpreted to be on a file system local to the LRM.</dl>
<h2>ENVIRONMENT</h2>
<p> The following variables affect the execution of <code>globus-job-run</code>: </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to proxy credential.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to trusted certificate directory.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-globusrun/">globusrun</a>(1), <a href="/docs/linux/man/1-globus-job-submit/">globus-job-submit</a>(1), <a href="/docs/linux/man/1-globus-job-clean/">globus-job-clean</a>(1), <a href="/docs/linux/man/1-globus-job-get-output/">globus-job-get-output</a>(1), <a href="/docs/linux/man/1-globus-job-cancel/">globus-job-cancel</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
