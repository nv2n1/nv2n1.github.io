---
title: "condor_gather_info(1)"
name: "condor_gather_info"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_gather_info/"
description: "condor_gather_info Gather information about an HTCondor installation and a queued job"
---

<h2>Name</h2>
<p> <i>condor_gather_info</i> Gather information about an HTCondor installation and a queued job </p>
<h2>Synopsis</h2>
<p> <i>condor_gather_info</i> [ &#8212; <code>jobid</code> <i>ClusterId.ProcId</i> ] [ &#8212; <code>scratch</code> <i>/path/to/directory</i> ] </p>
<h2>Description</h2>
<p> <i>condor_gather_info</i> is a Linux-only tool that will collect and output information about the machine it is run upon, about the HTCondor installation local to the machine, and optionally about a specified HTCondor job. The information gathered by this tool is most often used as a debugging aid for the developers of HTCondor. </p>
<p> Without the &#8212; <code>jobid</code> option, information about the local machine and its HTCondor installation is gathered and placed into the file called condor-profile.txt , in the current working directory. The information gathered is under the category of Identity. </p>
<p> With the &#8212; <code>jobid</code> option, additional information is gathered about the job given in the command line argument and identified by its ClusterId and ProcId ClassAd attributes. The information includes both categories, Identity and Job information. As the quantity of information can be extensive, this information is placed into a compressed tar file. The file is placed into the current working directory, and it is named using the format </p>
<p> cgi-&lt;username&gt;-jid&lt;ClusterId&gt;.&lt;ProcId&gt;-&lt;year&gt;-&lt;month&gt;-&lt;day&gt;-&lt;hour&gt;_&lt;minute&gt;_&lt;second&gt;-&lt;TZ&gt;.tar.gz </p>
<p> All values within &lt;&gt; are substituted with current values. The building of this potentially large tar file can require a fair amount of temporary space. If the &#8212; <code>scratch</code> option is specified, it identifies a directory in which to build the tar file. If the &#8212; <code>scratch</code> option is <i>not</i> specified, then the directory will be /tmp/cgi-&lt;PID&gt; , where the process ID is that of the <i>condor_gather_info</i> executable. </p>
<p> The information gathered by this tool:</p>
<dl>
<dt>
<dd> 1. Identity</p>
<dt>
<dd> * User name who generated the report</p>
<dt>
<dd> * Script location and machine name</p>
<dt>
<dd> * Date of report creation</p>
<dt>
<dd> * uname -a</p>
<dt>
<dd> * Contents of /etc/issue</p>
<dt>
<dd> * Contents of /etc/redhat-release</p>
<dt>
<dd> * Contents of /etc/debian_version</p>
<dt>
<dd> * Contents of $(LOG)/MasterLog</p>
<dt>
<dd> * Contents of $(LOG)/ShadowLog</p>
<dt>
<dd> * Contents of $(LOG)/SchedLog</p>
<dt>
<dd> * Output of ps -auxww -forest</p>
<dt>
<dd> * Output of df -h</p>
<dt>
<dd> * Output of iptables -L</p>
<dt>
<dd> * Output of ls `condor_config_val LOG`</p>
<dt>
<dd> * Output of ldd `condor_config_val SBIN`/condor_schedd</p>
<dt>
<dd> * Contents of /etc/hosts</p>
<dt>
<dd> * Contents of /etc/nsswitch.conf</p>
<dt>
<dd> * Output of ulimit -a</p>
<dt>
<dd> * Output of uptime</p>
<dt>
<dd> * Output of free</p>
<dt>
<dd> * Network interface configuration ( ifconfig )</p>
<dt>
<dd> * HTCondor version</p>
<dt>
<dd> * Location of HTCondor configuration files</p>
<dt>
<dd> * HTCondor configuration variables</p>
<dt>
<dd> * All variables and values</p>
<dt>
<dd> * Definition locations for each configuration variable</p>
<dt>
<dd> 2. Job Information</p>
<dt>
<dd> * Output of condor_q jobid</p>
<dt>
<dd> * Output of condor_q -l jobid</p>
<dt>
<dd> * Output of condor_q -analyze jobid</p>
<dt>
<dd> * Job event log, if it exists</p>
<dt>
<dd> * Only events pertaining to the job ID</p>
<dt>
<dd> * If <i>condor_gather_info</i> has the proper permissions, it runs <i>condor_fetchlog</i> on the machine where the job most recently ran, and includes the contents of the logs from the <i>condor_master</i> , <i>condor_startd</i> , and <i>condor_starter</i> .</dl>
<h2>Options</h2>
<p> <code>&#8211;jobid </code> <i>&lt;ClusterId.ProcId&gt;</i></p>
<dl>
<dt>
<dd> Data mine information about this HTCondor job from the local HTCondor installation and <i>condor_schedd</i> .</p>
<dt>
<dd></dl>
<p> <code>&#8211;scratch </code> <i>/path/to/directory</i></p>
<dl>
<dt>
<dd> A path to temporary space needed when building the output tar file. Defaults to /tmp/cgi-&lt;PID&gt; , where &lt;PID&gt; is replaced by the process ID of <i>condor_gather_info</i> .</p>
<dt>
<dd></dl>
<h2>Files</h2>
<dl>
<dt>
<dd> * condor-profile.txt The Identity portion of the information gathered when <i>condor_gather_info</i> is run without arguments.</p>
<dt>
<dd>
<dt>
<dd> * cgi-&lt;username&gt;-jid&lt;cluster&gt;.&lt;proc&gt;-&lt;year&gt;-&lt;month&gt;-&lt;day&gt;-&lt;hour&gt;_&lt;minute&gt;_&lt;second&gt;-&lt;TZ&gt;.tar.gz The output file which contains all of the information produced by this tool.</dl>
<h2>Exit Status</h2>
<p> <i>condor_gather_info</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
