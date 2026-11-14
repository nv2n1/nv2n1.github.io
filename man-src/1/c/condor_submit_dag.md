---
title: "condor_submit_dag(1)"
name: "condor_submit_dag"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_submit_dag/"
description: "condor_submit_dag Manage and queue jobs within a specified DAG for execution on remote machines"
---

<h2>Name</h2>
<p> <i>condor_submit_dag</i> Manage and queue jobs within a specified DAG for execution on remote machines </p>
<h2>Synopsis</h2>
<p> <i>condor_submit_dag</i> [ <code>-help | -version</code> ] </p>
<p> <i>condor_submit_dag</i> [ <code>-no_submit</code> ] [ <code>-verbose</code> ] [ <code>-force</code> ] [ <code>-maxidle </code> <i>NumberOfJobs</i> ] [ <code>-maxjobs </code> <i>NumberOfJobs</i> ] [ <code>-dagman </code> <i>DagmanExecutable</i> ] [ <code>-maxpre </code> <i>NumberOfPREscripts</i> ] [ <code>-maxpost </code> <i>NumberOfPOSTscripts</i> ] [ <code>-notification </code> <i>value</i> ] [ <code>-noeventchecks</code> ] [ <code>-allowlogerror</code> ] [ <code>-r </code> <i>schedd_name</i> ] [ <code>-debug </code> <i>level</i> ] [ <code>-usedagdir</code> ] [ <code>-outfile_dir </code> <i>directory</i> ] [ <code>-config </code> <i>ConfigFileName</i> ] [ <code>-insert_sub_file </code> <i>FileName</i> ] [ <code>-append </code> <i>Command</i> ] [ <code>-autorescue </code> <i>0|1</i> ] [ <code>-dorescuefrom </code> <i>number</i> ] [ <code>-allowversionmismatch</code> ] [ <code>-no_recurse</code> ] [ <code>-do_recurse</code> ] [ <code>-update_submit</code> ] [ <code>-import_env</code> ] [ <code>-DumpRescue</code> ] [ <code>-valgrind</code> ] [ <code>-DontAlwaysRunPost</code> ] [ <code>-priority </code> <i>number</i> ] [ <code>-dont_use_default_node_log</code> ] [ <code>-schedd-daemon-ad-file </code> <i>FileName</i> ] [ <code>-schedd-address-file </code> <i>FileName</i> ] [ <code>-suppress_notification</code> ] [ <code>-dont_suppress_notification</code> ] [ <code>-DoRecovery</code> ] <i>DAGInputFile1</i> [ <i>DAGInputFile2 &#8230; DAGInputFileN </i> ] </p>
<h2>Description</h2>
<p> <i>condor_submit_dag</i> is the program for submitting a DAG (directed acyclic graph) of jobs for execution under HTCondor. The program enforces the job dependencies defined in one or more <i>DAGInputFile</i> s. Each <i>DAGInputFile</i> contains commands to direct the submission of jobs implied by the nodes of a DAG to HTCondor. Extensive documentation is in the HTCondor User Manual section on DAGMan. </p>
<p> Some options may be specified on the command line or in the configuration or in a node job&#8217;s submit description file. Precedence is given to command line options or configuration over settings from a submit description file. An example is e-mail notifications. When configuration variable DAGMAN_SUPPRESS_NOTIFICATION is its default value of True , and a node job&#8217;s submit description file contains </p>
<p>&nbsp;<wbr>&nbsp;<wbr>notification&nbsp;<wbr>=&nbsp;<wbr>Complete </p>
<p> e-mail will <i>not</i> be sent upon completion, as the value of DAGMAN_SUPPRESS_NOTIFICATION is enforced. </p>
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
<p> <code>-no_submit</code></p>
<dl>
<dt>
<dd> Produce the HTCondor submit description file for DAGMan, but do not submit DAGMan as an HTCondor job.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Cause <i>condor_submit_dag</i> to give verbose error messages.</p>
<dt>
<dd></dl>
<p> <code>-force</code></p>
<dl>
<dt>
<dd> Require <i>condor_submit_dag</i> to overwrite the files that it produces, if the files already exist. Note that dagman.out will be appended to, not overwritten. If new-style rescue DAG mode is in effect, and any new-style rescue DAGs exist, the <code>-force</code> flag will cause them to be renamed, and the original DAG will be run. If old-style rescue DAG mode is in effect, any existing old-style rescue DAGs will be deleted, and the original DAG will be run.</p>
<dt>
<dd></dl>
<p> <code>-maxidle </code> <i>NumberOfJobs</i></p>
<dl>
<dt>
<dd> Sets the maximum number of idle jobs allowed before <i>condor_dagman</i> stops submitting more jobs. Once idle jobs start to run, <i>condor_dagman</i> will resume submitting jobs. <i>NumberOfJobs</i> is a positive integer. If the option is omitted, the number of idle jobs is defined by configuration variable DAGMAN_MAX_JOBS_IDLE , which defaults to 1000. Note that for this argument, each individual process within a cluster counts as a job, which is inconsistent with <code>-maxjobs </code> <i>.</i> Nothing special is done to the submit description file. Setting queue 5000 in the submit description file, where <i>-maxidle</i> is set to 250 will result in a cluster of 5000 new jobs being submitted to the <i>condor_schedd</i> . In this case, <i>condor_dagman</i> will resume submitting jobs when the number of idle jobs falls below 250.</p>
<dt>
<dd></dl>
<p> <code>-maxjobs </code> <i>NumberOfJobs</i></p>
<dl>
<dt>
<dd> Sets the maximum number of jobs within the DAG that will be submitted to HTCondor at one time. <i>NumberOfJobs</i> is a positive integer. If the option is omitted, the default number of jobs is unlimited. Note that for this argument, each cluster counts as one job, no matter how many individual processes are in the cluster.</p>
<dt>
<dd></dl>
<p> <code>-dagman </code> <i>DagmanExecutable</i></p>
<dl>
<dt>
<dd> Allows the specification of an alternate <i>condor_dagman</i> executable to be used instead of the one found in the user&#8217;s path. This must be a fully qualified path.</p>
<dt>
<dd></dl>
<p> <code>-maxpre </code> <i>NumberOfPREscripts</i></p>
<dl>
<dt>
<dd> Sets the maximum number of PRE scripts within the DAG that may be running at one time. <i>NumberOfPREScripts</i> is a positive integer. If this option is omitted, the default number of PRE scripts is unlimited.</p>
<dt>
<dd></dl>
<p> <code>-maxpost </code> <i>NumberOfPOSTscripts</i></p>
<dl>
<dt>
<dd> Sets the maximum number of POST scripts within the DAG that may be running at one time. <i>NumberOfPOSTScripts</i> is a positive integer. If this option is omitted, the default number of POST scripts is unlimited.</p>
<dt>
<dd></dl>
<p> <code>-notification </code> <i>value</i></p>
<dl>
<dt>
<dd> Sets the e-mail notification for DAGMan itself. This information will be used within the HTCondor submit description file for DAGMan. This file is produced by <i>condor_submit_dag</i> . See the description of <code>notification</code> within <i>condor_submit</i> manual page for a specification of <i>value</i> .</p>
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
<p> <code>-r </code> <i>schedd_name</i></p>
<dl>
<dt>
<dd> Submit <i>condor_dagman</i> to a remote machine, specifically the <i>condor_schedd</i> daemon on that machine. The <i>condor_dagman</i> job will not run on the local <i>condor_schedd</i> (the submit machine), but on the specified one. This is implemented using the <code>-remote</code> option to <i>condor_submit</i> . Note that this option does not currently specify input files for <i>condor_dagman</i> , nor the individual nodes to be taken along! It is assumed that any necessary files will be present on the remote computer, possibly via a shared file system between the local computer and the remote computer. It is also necessary that the user has appropriate permissions to submit a job to the remote machine; the permissions are the same as those required to use <i>condor_submit</i> <code>-remote</code> option. If other options are desired, including transfer of other input files, consider using the <code>-no_submit</code> option, modifying the resulting submit file for specific needs, and then using <i>condor_submit</i> on that.</p>
<dt>
<dd></dl>
<p> <code>-debug </code> <i>level</i></p>
<dl>
<dt>
<dd> Passes the the <i>level</i> of debugging output desired to <i>condor_dagman</i> . <i>level</i> is an integer, with values of 0-7 inclusive, where 7 is the most verbose output. See the <i>condor_dagman</i> manual page for detailed descriptions of these values. If not specified, no <code>-debug </code> <i>v</i> alue is passed to <i>condor_dagman</i> .</p>
<dt>
<dd></dl>
<p> <code>-usedagdir</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to run each specified DAG as if <i>condor_submit_dag</i> had been run in the directory containing that DAG file. This option is most useful when running multiple DAGs in a single <i>condor_dagman</i> . Note that the <code>-usedagdir</code> flag must not be used when running an old-style Rescue DAG.</p>
<dt>
<dd></dl>
<p> <code>-outfile_dir </code> <i>directory</i></p>
<dl>
<dt>
<dd> Specifies the directory in which the .dagman.out file will be written. The <i>directory</i> may be specified relative to the current working directory as <i>condor_submit_dag</i> is executed, or specified with an absolute path. Without this option, the .dagman.out file is placed in the same directory as the first DAG input file listed on the command line.</p>
<dt>
<dd></dl>
<p> <code>-config </code> <i>ConfigFileName</i></p>
<dl>
<dt>
<dd> Specifies a configuration file to be used for this DAGMan run. Note that the options specified in the configuration file apply to all DAGs if multiple DAGs are specified. Further note that it is a fatal error if the configuration file specified by this option conflicts with a configuration file specified in any of the DAG files, if they specify one.</p>
<dt>
<dd></dl>
<p> <code>-insert_sub_file </code> <i>FileName</i></p>
<dl>
<dt>
<dd> Specifies a file to insert into the .condor.sub file created by <i>condor_submit_dag</i> . The specified file must contain only legal submit file commands. Only one file can be inserted. (If both the DAGMAN_INSERT_SUB_FILE configuration variable and <code>-insert_sub_file</code> are specified, <code>-insert_sub_file</code> overrides DAGMAN_INSERT_SUB_FILE.) The specified file is inserted into the .condor.sub file before the Queue command and before any commands specified with the <code>-append</code> option.</p>
<dt>
<dd></dl>
<p> <code>-append </code> <i>Command</i></p>
<dl>
<dt>
<dd> Specifies a command to append to the .condor.sub file created by <i>condor_submit_dag</i> . The specified command is appended to the .condor.sub file immediately before the Queue command. Multiple commands are specified by using the <code>-append</code> option multiple times. Each new command is given in a separate <code>-append</code> option. Commands with spaces in them must be enclosed in double quotes. Commands specified with the <code>-append</code> option are appended to the .condor.sub file <i>after</i> commands inserted from a file specified by the <code>-insert_sub_file</code> option or the DAGMAN_INSERT_SUB_FILE configuration variable, so the <code>-append</code> command(s) will override commands from the inserted file if the commands conflict.</p>
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
<dd> Forces <i>condor_dagman</i> to run the specified rescue DAG number for the given DAG. A value of 0 is the same as not specifying this option. Specifying a non-existent rescue DAG is a fatal error.</p>
<dt>
<dd></dl>
<p> <code>-allowversionmismatch</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_dagman</i> to allow a version mismatch between <i>condor_dagman</i> itself and the .condor.sub file produced by <i>condor_submit_dag</i> (or, in other words, between <i>condor_submit_dag</i> and <i>condor_dagman</i> ). WARNING! This option should be used only if absolutely necessary. Allowing version mismatches can cause subtle problems when running DAGs. (Note that, starting with version 7.4.0, <i>condor_dagman</i> no longer requires an exact version match between itself and the .condor.sub file. Instead, a &quot;minimum compatible version&quot; is defined, and any .condor.sub file of that version or newer is accepted.)</p>
<dt>
<dd></dl>
<p> <code>-no_recurse</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_submit_dag</i> to <i>not</i> run itself recursively on nested DAGs (this is now the default; this flag has been kept mainly for backwards compatibility).</p>
<dt>
<dd></dl>
<p> <code>-do_recurse</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_submit_dag</i> to run itself recursively on nested DAGs. The default is now that it does <i>not</i> run itself recursively; instead the .condor.sub files for nested DAGs are generated &quot;lazily&quot; by <i>condor_dagman</i> itself. DAG nodes specified with the <code>SUBDAG EXTERNAL</code> keyword or with submit file names ending in .condor.sub are considered nested DAGs. The DAGMAN_GENERATE_SUBDAG_SUBMITS configuration variable may be relevant.</p>
<dt>
<dd></dl>
<p> <code>-update_submit</code></p>
<dl>
<dt>
<dd> This optional argument causes an existing .condor.sub file to not be treated as an error; rather, the .condor.sub file will be overwritten, but the existing values of <code>-maxjobs</code> , <code>-maxidle</code> , <code>-maxpre</code> , and <code>-maxpost</code> will be preserved.</p>
<dt>
<dd></dl>
<p> <code>-import_env</code></p>
<dl>
<dt>
<dd> This optional argument causes <i>condor_submit_dag</i> to import the current environment into the <code>environment</code> command of the .condor.sub file it generates.</p>
<dt>
<dd></dl>
<p> <code>-DumpRescue</code></p>
<dl>
<dt>
<dd> This optional argument tells <i>condor_dagman</i> to immediately dump a rescue DAG and then exit, as opposed to actually running the DAG. This feature is mainly intended for testing. The Rescue DAG file is produced whether or not there are parse errors reading the original DAG input file. The name of the file differs if there was a parse error.</p>
<dt>
<dd></dl>
<p> <code>-valgrind</code></p>
<dl>
<dt>
<dd> This optional argument causes the submit description file generated for the submission of <i>condor_dagman</i> to be modified. The executable becomes <i>valgrind</i> run on <i>condor_dagman</i> , with a specific set of arguments intended for testing <i>condor_dagman</i> . Note that this argument is intended for testing purposes only. Using the <code>-valgrind</code> option without the necessary <i>valgrind</i> software installed will cause the DAG to fail. If the DAG does run, it will run much more slowly than usual.</p>
<dt>
<dd></dl>
<p> <code>-DontAlwaysRunPost</code></p>
<dl>
<dt>
<dd> This option causes the submit description file generated for the submission of <i>condor_dagman</i> to be modified. It causes the <code>-DontAlwaysRunPost</code> option to be in the arguments to <i>condor_dagman</i> in the submit description file, which causes <i>condor_dagman</i> to use the return value from a PRE script to determine whether or not a POST script will run. By default, <i>condor_dagman</i> runs the POST script regardless of the return value of the PRE script. Versions of <i>condor_dagman</i> prior to 7.7.2 did not ignore the return value and would not run the POST script if the PRE script failed.</p>
<dt>
<dd></dl>
<p> <code>-priority </code> <i>number</i></p>
<dl>
<dt>
<dd> Sets the minimum job priority of node jobs submitted and running under the <i>condor_dagman</i> job submitted by this <i>condor_submit_dag</i> command.</p>
<dt>
<dd></dl>
<p> <code>-dont_use_default_node_log</code></p>
<dl>
<dt>
<dd> <code>This option is disabled as of HTCondor version 8.3.1. This causes a compatibility error if the HTCondor version number of the </code> <i>condor_schedd</i> is 7.9.0 or older. Tells <i>condor_dagman</i> to use the file specified by the job ClassAd attribute UserLog to monitor job status. If this command line argument is used, then the job event log file cannot be defined with a macro.</p>
<dt>
<dd></dl>
<p> <code>-schedd-daemon-ad-file </code> <i>FileName</i></p>
<dl>
<dt>
<dd> Specifies a full path to a daemon ad file dropped by a <i>condor_schedd</i> . Therefore this allows submission to a specific scheduler if several are available without repeatedly querying the <i>condor_collector</i> . The value for this argument defaults to the configuration attribute SCHEDD_DAEMON_AD_FILE .</p>
<dt>
<dd></dl>
<p> <code>-schedd-address-file </code> <i>FileName</i></p>
<dl>
<dt>
<dd> Specifies a full path to an address file dropped by a <i>condor_schedd</i> . Therefore this allows submission to a specific scheduler if several are available without repeatedly querying the <i>condor_collector</i> . The value for this argument defaults to the configuration attribute SCHEDD_ADDRESS_FILE .</p>
<dt>
<dd></dl>
<p> <code>-suppress_notification</code></p>
<dl>
<dt>
<dd> Causes jobs submitted by <i>condor_dagman</i> to not send email notification for events. The same effect can be achieved by setting configuration variable DAGMAN_SUPPRESS_NOTIFICATION to True . This command line option is independent of the <code>-notification</code> command line option, which controls notification for the <i>condor_dagman</i> job itself.</p>
<dt>
<dd></dl>
<p> <code>-dont_suppress_notification</code></p>
<dl>
<dt>
<dd> Causes jobs submitted by <i>condor_dagman</i> to defer to content within the submit description file when deciding to send email notification for events. The same effect can be achieved by setting configuration variable DAGMAN_SUPPRESS_NOTIFICATION to False . This command line flag is independent of the <code>-notification</code> command line option, which controls notification for the <i>condor_dagman</i> job itself. If both <code>-dont_suppress_notification</code> and <code>-suppress_notification</code> are specified with the same command line, the last argument is used.</p>
<dt>
<dd></dl>
<p> <code>-DoRecovery</code></p>
<dl>
<dt>
<dd> Causes <i>condor_dagman</i> to start in recovery mode. (This means that it reads the relevant job user log(s) and &quot;catches up&quot; to the given DAG&#8217;s previous state before submitting any new jobs.)</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_submit_dag</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> To run a single DAG: </p>
<p> % condor_submit_dag diamond.dag </p>
<p> To run a DAG when it has already been run and the output files exist: </p>
<p> % condor_submit_dag -force diamond.dag </p>
<p> To run a DAG, limiting the number of idle node jobs in the DAG to a maximum of five: </p>
<p> % condor_submit_dag -maxidle 5 diamond.dag </p>
<p> To run a DAG, limiting the number of concurrent PRE scripts to 10 and the number of concurrent POST scripts to five: </p>
<p> % condor_submit_dag -maxpre 10 -maxpost 5 diamond.dag </p>
<p> To run two DAGs, each of which is set up to run in its own directory: </p>
<p> % condor_submit_dag -usedagdir dag1/diamond1.dag dag2/diamond2.dag </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
