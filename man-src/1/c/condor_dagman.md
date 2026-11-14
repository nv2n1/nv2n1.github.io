---
title: "condor_dagman(1)"
name: "condor_dagman"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_dagman/"
description: "condor_dagman meta scheduler of the jobs submitted as the nodes of a DAG or DAGs"
---

<h2>Name</h2>
<p> <i>condor_dagman</i> meta scheduler of the jobs submitted as the nodes of a DAG or DAGs </p>
<h2>Synopsis</h2>
<p> <i>condor_dagman</i> <i>-f</i> <i>-t</i> <i>-l .</i> <code>-help</code> </p>
<p> <i>condor_dagman</i> <code>-version</code> </p>
<p> <i>condor_dagman</i> <i>-f</i> <i>-l .</i> <code>-csdversion </code> <i>version_string</i> [ <code>-debug </code> <i>level</i> ] [ <code>-maxidle </code> <i>numberOfJobs</i> ] [ <code>-maxjobs </code> <i>numberOfJobs</i> ] [ <code>-maxpre </code> <i>NumberOfPREscripts</i> ] [ <code>-maxpost </code> <i>NumberOfPOSTscripts</i> ] [ <code>-noeventchecks</code> ] [ <code>-allowlogerror</code> ] [ <code>-usedagdir</code> ] <code>-lockfile </code> <i>filename</i> [ <code>-waitfordebug</code> ] [ <code>-autorescue </code> <i>0|1</i> ] [ <code>-dorescuefrom </code> <i>number</i> ] [ <code>-allowversionmismatch</code> ] [ <code>-DumpRescue</code> ] [ <code>-verbose</code> ] [ <code>-force</code> ] [ <code>-notification </code> <i>value</i> ] [ <code>-suppress_notification</code> ] [ <code>-dont_suppress_notification</code> ] [ <code>-dagman </code> <i>DagmanExecutable</i> ] [ <code>-outfile_dir </code> <i>directory</i> ] [ <code>-update_submit</code> ] [ <code>-import_env</code> ] [ <code>-priority </code> <i>number</i> ] [ <code>-dont_use_default_node_log</code> ] [ <code>-DontAlwaysRunPost</code> ] [ <code>-DoRecovery</code> ] <code>-dag </code> <i>dag_file</i> [ <i></i><code>-dag </code> <i>dag_file_2</i> &#8230; <code>-dag </code> <i>dag_file_n</i> ] </p>
<h2>Description</h2>
<p> <i>condor_dagman</i> is a meta scheduler for the HTCondor jobs within a DAG (directed acyclic graph) (or multiple DAGs). In typical usage, a submitter of jobs that are organized into a DAG submits the DAG using <i>condor_submit_dag</i> . <i>condor_submit_dag</i> does error checking on aspects of the DAG and then submits <i>condor_dagman</i> as an HTCondor job. <i>condor_dagman</i> uses log files to coordinate the further submission of the jobs within the DAG. </p>
<p> All command line arguments to the <i>DaemonCore</i> library functions work for <i>condor_dagman</i> . When invoked from the command line, <i>condor_dagman</i> requires the arguments <i>-f -l .</i> to appear first on the command line, to be processed by <i>DaemonCore</i> . The <code>csdversion</code> must also be specified; at start up, <i>condor_dagman</i> checks for a version mismatch with the <i>condor_submit_dag</i> version in this argument. The <i>-t</i> argument must also be present for the <code>-help</code> option, such that output is sent to the terminal. </p>
<p> Arguments to <i>condor_dagman</i> are either automatically set by <i>condor_submit_dag</i> or they are specified as command-line arguments to <i>condor_submit_dag</i> and passed on to <i>condor_dagman</i> . The method by which the arguments are set is given in their description below. </p>
<p> <i>condor_dagman</i> can run multiple, independent DAGs. This is done by specifying multiple <code>-dag </code> <i>a</i> rguments. Pass multiple DAG input files as command-line arguments to <i>condor_submit_dag</i> . </p>
<p> Debugging output may be obtained by using the <code>-debug </code> <i>level</i> option. Level values and what they produce is described as</p>
<dl>
<dt>
<dd> * level = 0; never produce output, except for usage info</p>
<dt>
<dd> * level = 1; very quiet, output severe errors</p>
<dt>
<dd> * level = 2; normal output, errors and warnings</p>
<dt>
<dd> * level = 3; output errors, as well as all warnings</p>
<dt>
<dd> * level = 4; internal debugging output</p>
<dt>
<dd> * level = 5; internal debugging output; outer loop debugging</p>
<dt>
<dd> * level = 6; internal debugging output; inner loop debugging; output DAG input file lines as they are parsed</p>
<dt>
<dd> * level = 7; internal debugging output; rarely used; output DAG input file lines as they are parsed</dl>
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
<p> <code>-debug </code> <i>level</i></p>
<dl>
<dt>
<dd> An integer level of debugging output. <i>level</i> is an integer, with values of 0-7 inclusive, where 7 is the most verbose output. This command-line option to <i>condor_submit_dag</i> is passed to <i>condor_dagman</i> or defaults to the value 3.</p>
<dt>
<dd></dl>
<p> <code>-maxidle </code> <i>NumberOfJobs</i></p>
<dl>
<dt>
<dd> Sets the maximum number of idle jobs allowed before <i>condor_dagman</i> stops submitting more jobs. If DAG nodes have a cluster with more than one job in it, each job in the cluster is counted individually. Once idle jobs start to run, <i>condor_dagman</i> will resume submitting jobs. <i>NumberOfJobs</i> is a positive integer. This command-line option to <i>condor_submit_dag</i> is passed to <i>condor_dagman</i> . If not specified, the number of idle jobs is defined by configuration variable DAGMAN_MAX_JOBS_IDLE , which defaults to 1000. Note that nothing special is done to the submit description file. Setting queue 5000 in the submit description file, where <i>-maxidle</i> is set to 250 will result in a cluster of 5000 new jobs being submitted to the <i>condor_schedd</i> . In this case, <i>condor_dagman</i> will resume submitting jobs when the number of idle jobs falls below 250.</p>
<dt>
<dd></dl>
<p> <code>-maxjobs </code> <i>numberOfJobs</i></p>
<dl>
<dt>
<dd> Sets the maximum number of clusters within the DAG that will be submitted to HTCondor at one time. <i>numberOfJobs</i> is a positive integer. This command-line option to <i>condor_submit_dag</i> is passed to <i>condor_dagman</i> . If not specified, the default number of clusters is unlimited. If a cluster contains more than one job, only the cluster is counted for purposes of <code>maxjobs</code> .</p>
<dt>
<dd></dl>
<p> <code>-maxpre </code> <i>NumberOfPREscripts</i></p>
<dl>
<dt>
<dd> Sets the maximum number of PRE scripts within the DAG that may be running at one time. <i>NumberOfPREScripts</i> is a positive integer. This command-line option to <i>condor_submit_dag</i> is passed to <i>condor_dagman</i> . If not specified, the default number of PRE scripts is unlimited.</p>
<dt>
<dd></dl>
<p> <code>-maxpost </code> <i>NumberOfPOSTscripts</i></p>
<dl>
<dt>
<dd> Sets the maximum number of POST scripts within the DAG that may be running at one time. <i>NumberOfPOSTScripts</i> is a positive integer. This command-line option to <i>condor_submit_dag</i> is passed to <i>condor_dagman</i> . If not specified, the default number of POST scripts is unlimited.</p>
<dt>
<dd></dl>
<p> <code>-noeventchecks</code></p>
<dl>
<dt>
<dd> This argument is no longer used; it is now ignored. Its functionality is now implemented by the DAGMAN_ALLOW_EVENTS configuration variable.</p>
<dt>
<dd></dl>
<p> <code>-allowlogerror</code></p>
<dl>
<dt>
<dd> This optional argument has <i>condor_dagman</i> try to run the specified DAG, even in the case of detected errors in the job event log specification. As of version 7.3.2, this argument has an effect only on DAGs containing Stork job nodes.</p>
<dt>
<dd></dl>
<p> <code>-usedagdir</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to run each specified DAG as if the directory containing that DAG file was the current working directory. This option is most useful when running multiple DAGs in a single <i>condor_dagman</i> .</p>
<dt>
<dd></dl>
<p> <code>-lockfile </code> <i>filename</i></p>
<dl>
<dt>
<dd> Names the file created and used as a lock file. The lock file prevents execution of two of the same DAG, as defined by a DAG input file. A default lock file ending with the suffix .dag.lock is passed to <i>condor_dagman</i> by <i>condor_submit_dag</i> .</p>
<dt>
<dd></dl>
<p> <code>-waitfordebug</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to wait at startup until someone attaches to the process with a debugger and sets the wait_for_debug variable in main_init() to false.</p>
<dt>
<dd></dl>
<p> <code>-autorescue </code> <i>0|1</i></p>
<dl>
<dt>
<dd> Whether to automatically run the newest rescue DAG for the given DAG file, if one exists (0 = false , 1 = true ).</p>
<dt>
<dd></dl>
<p> <code>-dorescuefrom </code> <i>number</i></p>
<dl>
<dt>
<dd> Forces <i>condor_dagman</i> to run the specified rescue DAG number for the given DAG. A value of 0 is the same as not specifying this option. Specifying a nonexistent rescue DAG is a fatal error.</p>
<dt>
<dd></dl>
<p> <code>-allowversionmismatch</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to allow a version mismatch between <i>condor_dagman</i> itself and the .condor.sub file produced by <i>condor_submit_dag</i> (or, in other words, between <i>condor_submit_dag</i> and <i>condor_dagman</i> ). WARNING! This option should be used only if absolutely necessary. Allowing version mismatches can cause subtle problems when running DAGs. (Note that, starting with version 7.4.0, <i>condor_dagman</i> no longer requires an exact version match between itself and the .condor.sub file. Instead, a &quot;minimum compatible version&quot; is defined, and any .condor.sub file of that version or newer is accepted.)</p>
<dt>
<dd></dl>
<p> <code>-DumpRescue</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to immediately dump a Rescue DAG and then exit, as opposed to actually running the DAG. This feature is mainly intended for testing. The Rescue DAG file is produced whether or not there are parse errors reading the original DAG input file. The name of the file differs if there was a parse error.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) Cause <i>condor_submit_dag</i> to give verbose error messages.</p>
<dt>
<dd></dl>
<p> <code>-force</code></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) Require <i>condor_submit_dag</i> to overwrite the files that it produces, if the files already exist. Note that dagman.out will be appended to, not overwritten. If new-style rescue DAG mode is in effect, and any new-style rescue DAGs exist, the <code>-force</code> flag will cause them to be renamed, and the original DAG will be run. If old-style rescue DAG mode is in effect, any existing old-style rescue DAGs will be deleted, and the original DAG will be run. See the HTCondor manual section on Rescue DAGs for more information.</p>
<dt>
<dd></dl>
<p> <code>-notification </code> <i>value</i></p>
<dl>
<dt>
<dd> This argument is only included to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs. Sets the e-mail notification for DAGMan itself. This information will be used within the HTCondor submit description file for DAGMan. This file is produced by <i>condor_submit_dag</i> . The <code>notification</code> option is described in the <i>condor_submit</i> manual page.</p>
<dt>
<dd></dl>
<p> <code>-suppress_notification</code></p>
<dl>
<dt>
<dd> Causes jobs submitted by <i>condor_dagman</i> to not send email notification for events. The same effect can be achieved by setting the configuration variable DAGMAN_SUPPRESS_NOTIFICATION to True . This command line option is independent of the <code>-notification</code> command line option, which controls notification for the <i>condor_dagman</i> job itself. This flag is generally superfluous, as DAGMAN_SUPPRESS_NOTIFICATION defaults to True .</p>
<dt>
<dd></dl>
<p> <code>-dont_suppress_notification</code></p>
<dl>
<dt>
<dd> Causes jobs submitted by <i>condor_dagman</i> to defer to content within the submit description file when deciding to send email notification for events. The same effect can be achieved by setting the configuration variable DAGMAN_SUPPRESS_NOTIFICATION to False . This command line flag is independent of the <code>-notification</code> command line option, which controls notification for the <i>condor_dagman</i> job itself. If both <code>-dont_suppress_notification</code> and <code>-suppress_notification</code> are specified within the same command line, the last argument is used.</p>
<dt>
<dd></dl>
<p> <code>-dagman </code> <i>DagmanExecutable</i></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) Allows the specification of an alternate <i>condor_dagman</i> executable to be used instead of the one found in the user&#8217;s path. This must be a fully qualified path.</p>
<dt>
<dd></dl>
<p> <code>-outfile_dir </code> <i>directory</i></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) Specifies the directory in which the .dagman.out file will be written. The <i>directory</i> may be specified relative to the current working directory as <i>condor_submit_dag</i> is executed, or specified with an absolute path. Without this option, the .dagman.out file is placed in the same directory as the first DAG input file listed on the command line.</p>
<dt>
<dd></dl>
<p> <code>-update_submit</code></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) This optional argument causes an existing .condor.sub file to not be treated as an error; rather, the .condor.sub file will be overwritten, but the existing values of <code>-maxjobs</code> , <code>-maxidle</code> , <code>-maxpre</code> , and <code>-maxpost</code> will be preserved.</p>
<dt>
<dd></dl>
<p> <code>-import_env</code></p>
<dl>
<dt>
<dd> (This argument is included only to be passed to <i>condor_submit_dag</i> if lazy submit file generation is used for nested DAGs.) This optional argument causes <i>condor_submit_dag</i> to import the current environment into the <code>environment</code> command of the .condor.sub file it generates.</p>
<dt>
<dd></dl>
<p> <code>-priority </code> <i>number</i></p>
<dl>
<dt>
<dd> Sets the minimum job priority of node jobs submitted and running under this <i>condor_dagman</i> job.</p>
<dt>
<dd></dl>
<p> <code>-dont_use_default_node_log</code></p>
<dl>
<dt>
<dd> <code>This option is disabled as of HTCondor version 8.3.1.</code> Tells <i>condor_dagman</i> to use the file specified by the job ClassAd attribute UserLog to monitor job status. If this command line argument is used, then the job event log file cannot be defined with a macro.</p>
<dt>
<dd></dl>
<p> <code>-DontAlwaysRunPost</code></p>
<dl>
<dt>
<dd> This option causes <i>condor_dagman</i> to observe the exit status of the PRE script when deciding whether or not to run the POST script. Versions of <i>condor_dagman</i> previous to HTCondor version 7.7.2 would not run the POST script if the PRE script exited with a nonzero status, but this default has been changed such that the POST script will run, regardless of the exit status of the PRE script. Using this option restores the previous behavior, in which <i>condor_dagman</i> will not run the POST script if the PRE script fails.</p>
<dt>
<dd></dl>
<p> <code>-DoRecovery</code></p>
<dl>
<dt>
<dd> Causes <i>condor_dagman</i> to start in recovery mode. This means that it reads the relevant job user log(s) and catches up to the given DAG&#8217;s previous state before submitting any new jobs.</p>
<dt>
<dd></dl>
<p> <code>-dag </code> <i>filename</i></p>
<dl>
<dt>
<dd> <i>filename</i> is the name of the DAG input file that is set as an argument to <i>condor_submit_dag</i> , and passed to <i>condor_dagman</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_dagman</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> <i>condor_dagman</i> is normally not run directly, but submitted as an HTCondor job by running condor_submit_dag. See the condor_submit_dag manual page for examples. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
