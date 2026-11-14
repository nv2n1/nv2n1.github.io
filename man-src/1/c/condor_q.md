---
title: "condor_q(1)"
name: "condor_q"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_q/"
description: "condor_q Display information about jobs in queue"
---

<h2>Name</h2>
<p> <i>condor_q</i> Display information about jobs in queue </p>
<h2>Synopsis</h2>
<p> <i>condor_q</i> [ <code>-help [Universe | State]</code> ] </p>
<p> <i>condor_q</i> [ <code>-debug</code> ] [ <i>general options</i> ] [ <i>restriction list</i> ] [ <i>output options</i> ] [ <i>analyze options</i> ] </p>
<h2>Description</h2>
<p> <i>condor_q</i> displays information about jobs in the HTCondor job queue. By default, <i>condor_q</i> queries the local job queue, but this behavior may be modified by specifying one of the general options. </p>
<p> To restrict the display to jobs of interest, a list of zero or more restriction options may be supplied. Each restriction may be one of:</p>
<dl>
<dt>
<dd> * a <i>cluster</i> and a <i>process</i> matches jobs which belong to the specified cluster and have the specified process number</p>
<dt>
<dd> * a <i>cluster</i> without a <i>process</i> matches all jobs belonging to the specified cluster</p>
<dt>
<dd> * an <i>owner</i> matches all jobs owned by the specified owner</p>
<dt>
<dd> * a <code>-constraint </code> <i>expression</i> which matches all jobs that satisfy the specified ClassAd expression. If no restrictions are present in the list to specify an <i>owner</i> , the job matches the restriction list if it matches at least one restriction in the list. If <i>owner</i> restrictions are present, the job matches the list if it matches one of the <i>owner</i> restrictions <i>and</i> at least one non- <i>owner</i> restriction.</dl>
<p> If the <code>-long</code> option is specified, <i>condor_q</i> displays a long description of the queried jobs by printing the entire job ClassAd. The attributes of the job ClassAd may be displayed by means of the <code>-format</code> option, which displays attributes with a <a href="/docs/linux/man/3-printf/">printf</a>(3) format. Multiple <code>-format</code> options may be specified in the option list to display several attributes of the job. If neither <code>-long</code> or <code>-format</code> are specified, <i>condor_q</i> displays a one line summary of information as follows: </p>
<p> <code>ID</code></p>
<dl>
<dt>
<dd> The cluster/process id of the condor job.</p>
<dt>
<dd></dl>
<p> <code>OWNER</code></p>
<dl>
<dt>
<dd> The owner of the job.</p>
<dt>
<dd></dl>
<p> <code>SUBMITTED</code></p>
<dl>
<dt>
<dd> The month, day, hour, and minute the job was submitted to the queue.</p>
<dt>
<dd></dl>
<p> <code>RUN_TIME</code></p>
<dl>
<dt>
<dd> Wall-clock time accumulated by the job to date in days, hours, minutes, and seconds.</p>
<dt>
<dd></dl>
<p> <code>ST</code></p>
<dl>
<dt>
<dd> Current status of the job, which varies somewhat according to the job universe and the timing of updates. H = on hold, R = running, I = idle (waiting for a machine to execute on), C = completed, X = removed, &lt; = transferring input (or queued to do so), and &gt; = transferring output (or queued to do so).</p>
<dt>
<dd></dl>
<p> <code>PRI</code></p>
<dl>
<dt>
<dd> User specified priority of the job, displayed as an integer, with higher numbers corresponding to greater priority.</p>
<dt>
<dd></dl>
<p> <code>SIZE</code></p>
<dl>
<dt>
<dd> The peak amount of memory in Mbytes consumed by the job; note this value is only refreshed periodically. The actual value reported is taken from the job ClassAd attribute MemoryUsage if this attribute is defined, and from job attribute ImageSize otherwise.</p>
<dt>
<dd></dl>
<p> <code>CMD</code></p>
<dl>
<dt>
<dd> The name of the executable.</p>
<dt>
<dd></dl>
<p> If the output option <code>-dag</code> is specified, the OWNER column is replaced with NODENAME for jobs started by the <i>condor_dagman</i> instance. </p>
<p> If the output option <code>-run</code> is specified, the ST, PRI, SIZE, and CMD columns are replaced with: </p>
<p> <code>HOST(S)</code></p>
<dl>
<dt>
<dd> The host where the job is running.</p>
<dt>
<dd></dl>
<p> If the output option <code>-globus</code> is specified, the ST, PRI, SIZE, and CMD columns are replaced with: </p>
<p> <code>STATUS</code></p>
<dl>
<dt>
<dd> The state that HTCondor believes the job is in. Possible values are</p>
<dt>
<dd> <code>PENDING</code></p>
<dt>
<dd> The job is waiting for resources to become available in order to run.</p>
<dt>
<dd>
<dt>
<dd> <code>ACTIVE</code></p>
<dt>
<dd> The job has received resources, and the application is executing.</p>
<dt>
<dd>
<dt>
<dd> <code>FAILED</code></p>
<dt>
<dd> The job terminated before completion because of an error, user-triggered cancel, or system-triggered cancel.</p>
<dt>
<dd>
<dt>
<dd> <code>DONE</code></p>
<dt>
<dd> The job completed successfully.</p>
<dt>
<dd>
<dt>
<dd> <code>SUSPENDED</code></p>
<dt>
<dd> The job has been suspended. Resources which were allocated for this job may have been released due to a scheduler-specific reason.</p>
<dt>
<dd>
<dt>
<dd> <code>UNSUBMITTED</code></p>
<dt>
<dd> The job has not been submitted to the scheduler yet, pending the reception of the GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_REQUEST signal from a client.</p>
<dt>
<dd>
<dt>
<dd> <code>STAGE_IN</code></p>
<dt>
<dd> The job manager is staging in files, in order to run the job.</p>
<dt>
<dd>
<dt>
<dd> <code>STAGE_OUT</code></p>
<dt>
<dd> The job manager is staging out files generated by the job.</p>
<dt>
<dd>
<dt>
<dd> <code>UNKNOWN</code></p>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MANAGER</code></p>
<dl>
<dt>
<dd> A guess at what remote batch system is running the job. It is a guess, because HTCondor looks at the Globus jobmanager contact string to attempt identification. If the value is fork, the job is running on the remote host without a jobmanager. Values may also be condor, lsf, or pbs.</p>
<dt>
<dd></dl>
<p> <code>HOST</code></p>
<dl>
<dt>
<dd> The host to which the job was submitted.</p>
<dt>
<dd></dl>
<p> <code>EXECUTABLE</code></p>
<dl>
<dt>
<dd> The job as specified as the executable in the submit description file.</p>
<dt>
<dd></dl>
<p> If the output option <code>-goodput</code> is specified, the ST, PRI, SIZE, and CMD columns are replaced with: </p>
<p> <code>GOODPUT</code></p>
<dl>
<dt>
<dd> The percentage of RUN_TIME for this job which has been saved in a checkpoint. A low GOODPUT value indicates that the job is failing to checkpoint. If a job has not yet attempted a checkpoint, this column contains [?????] .</p>
<dt>
<dd></dl>
<p> <code>CPU_UTIL</code></p>
<dl>
<dt>
<dd> The ratio of CPU_TIME to RUN_TIME for checkpointed work. A low CPU_UTIL indicates that the job is not running efficiently, perhaps because it is I/O bound or because the job requires more memory than available on the remote workstations. If the job has not (yet) checkpointed, this column contains [??????] .</p>
<dt>
<dd></dl>
<p> <code>Mb/s</code></p>
<dl>
<dt>
<dd> The network usage of this job, in Megabits per second of run-time.</p>
<dt>
<dd></dl>
<p> If the output option <code>-io</code> is specified, the ST, PRI, SIZE, and CMD columns are replaced with: </p>
<dl>
<dt>
<dd> READ The total number of bytes the application has read from files and sockets.</p>
<dt>
<dd></dl>
<dl>
<dt>
<dd> WRITE The total number of bytes the application has written to files and sockets.</p>
<dt>
<dd></dl>
<dl>
<dt>
<dd> SEEK The total number of seek operations the application has performed on files.</p>
<dt>
<dd></dl>
<dl>
<dt>
<dd> XPUT The effective throughput (average bytes read and written per second) from the application&#8217;s point of view.</p>
<dt>
<dd></dl>
<dl>
<dt>
<dd> BUFSIZE The maximum number of bytes to be buffered per file.</p>
<dt>
<dd></dl>
<dl>
<dt>
<dd> BLOCKSIZE The desired block size for large data transfers.</p>
<dt>
<dd></dl>
<p> These fields are updated when a job produces a checkpoint or completes. If a job has not yet produced a checkpoint, this information is not available. </p>
<p> If the output option <code>-cputime</code> is specified, the RUN_TIME column is replaced with: </p>
<p> <code>CPU_TIME</code></p>
<dl>
<dt>
<dd> The remote CPU time accumulated by the job to date (which has been stored in a checkpoint) in days, hours, minutes, and seconds. (If the job is currently running, time accumulated during the current run is <i>not</i> shown. If the job has not produced a checkpoint, this column contains 0+00:00:00.)</p>
<dt>
<dd></dl>
<p> The <code>-analyze</code> or <code>-better-analyze</code> options may be used to determine why certain jobs are not running by performing an analysis on a per machine basis for each machine in the pool. The reasons may vary among failed constraints, insufficient priority, resource owner preferences and prevention of preemption by the PREEMPTION_REQUIREMENTS expression. If the analyze option <code>-verbose</code> is specified along with the <code>-analyze</code> option, the reason for failure is displayed on a per machine basis. <code>-better-analyze</code> differs from <code>-analyze</code> in that it will do matchmaking analysis on jobs even if they are currently running, or if the reason they are not running is not due to matchmaking. <code>-better-analyze</code> also produces more thorough analysis of complex Requirements and shows the values of relevant job ClassAd attributes. When only a single machine is being analyzed via <code>-machine</code> or <code>-mconstraint</code> , the values of relevant attributes of the machine ClassAd are also displayed. </p>
<h2>Options</h2>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-global</code></p>
<dl>
<dt>
<dd> (general option) Queries all job queues in the pool.</p>
<dt>
<dd></dl>
<p> <code>-submitter </code> <i>submitter</i></p>
<dl>
<dt>
<dd> (general option) List jobs of a specific submitter.</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>name</i></p>
<dl>
<dt>
<dd> (general option) Query only the job queue of the named <i>condor_schedd</i> daemon.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> (general option) Use the <i>centralmanagerhostname</i> as the central manager to locate <i>condor_schedd</i> daemons. The default is the COLLECTOR_HOST , as specified in the configuration.</p>
<dt>
<dd></dl>
<p> <code>-jobads </code> <i>file</i></p>
<dl>
<dt>
<dd> (general option) Display jobs from a list of ClassAds from a file, instead of the real ClassAds from the <i>condor_schedd</i> daemon. This is most useful for debugging purposes. The ClassAds appear as if <i>condor_q</i> <code>-long</code> is used with the header stripped out.</p>
<dt>
<dd></dl>
<p> <code>-userlog </code> <i>file</i></p>
<dl>
<dt>
<dd> (general option) Display jobs, with job information coming from a job event log, instead of from the real ClassAds from the <i>condor_schedd</i> daemon. This is most useful for automated testing of the status of jobs known to be in the given job event log, because it reduces the load on the <i>condor_schedd</i> . A job event log does not contain all of the job information, so some fields in the normal output of <i>condor_q</i> will be blank.</p>
<dt>
<dd></dl>
<p> <code>-autocluster</code></p>
<dl>
<dt>
<dd> (output option) Output <i>condor_schedd</i> daemon auto cluster information. For each auto cluster, output the unique ID of the auto cluster along with the number of jobs in that auto cluster. This option is intended to be used together with the <code>-long</code> option to output the ClassAds representing auto clusters. The ClassAds can then be used to identify or classify the demand for sets of machine resources, which will be useful in the on-demand creation of execute nodes for glidein services.</p>
<dt>
<dd></dl>
<p> <code>-cputime</code></p>
<dl>
<dt>
<dd> (output option) Instead of wall-clock allocation time (RUN_TIME), display remote CPU time accumulated by the job to date in days, hours, minutes, and seconds. If the job is currently running, time accumulated during the current run is <i>not</i> shown.</p>
<dt>
<dd></dl>
<p> <code>-currentrun</code></p>
<dl>
<dt>
<dd> (output option) Normally, RUN_TIME contains all the time accumulated during the current run plus all previous runs. If this option is specified, RUN_TIME only displays the time accumulated so far on this current run.</p>
<dt>
<dd></dl>
<p> <code>-dag </code> <i>&lt;DAG-ID&gt;</i></p>
<dl>
<dt>
<dd> (output option) Display DAG node jobs under their DAGMan instance. Child nodes are listed using indentation to show the structure of the DAG. When the optional <i>DAG-ID</i> is specified, display all jobs in the DAG.</p>
<dt>
<dd></dl>
<p> <code>-expert</code></p>
<dl>
<dt>
<dd> (output option) Display shorter error messages.</p>
<dt>
<dd></dl>
<p> <code>-globus</code></p>
<dl>
<dt>
<dd> (output option) Get information only about jobs submitted to grid resources described as <code>gt2</code> or <code>gt5</code> .</p>
<dt>
<dd></dl>
<p> <code>-goodput</code></p>
<dl>
<dt>
<dd> (output option) Display job goodput statistics.</p>
<dt>
<dd></dl>
<p> <code>-help [Universe | State]</code></p>
<dl>
<dt>
<dd> (output option) Print usage info, and additionally print job universes or job states.</p>
<dt>
<dd></dl>
<p> <code>-hold</code></p>
<dl>
<dt>
<dd> (output option) Get information about jobs in the hold state. Also displays the time the job was placed into the hold state and the reason why the job was placed in the hold state.</p>
<dt>
<dd></dl>
<p> <code>-limit </code> <i>Number</i></p>
<dl>
<dt>
<dd> (output option) Limit the number of items output to <i>Number</i> .</p>
<dt>
<dd></dl>
<p> <code>-io</code></p>
<dl>
<dt>
<dd> (output option) Display job input/output summaries.</p>
<dt>
<dd></dl>
<p> <code>-long</code></p>
<dl>
<dt>
<dd> (output option) Display entire job ClassAds in long format.</p>
<dt>
<dd></dl>
<p> <code>-run</code></p>
<dl>
<dt>
<dd> (output option) Get information about running jobs.</p>
<dt>
<dd></dl>
<p> <code>-stream-results</code></p>
<dl>
<dt>
<dd> (output option) Display results as jobs are fetched from the job queue rather than storing results in memory until all jobs have been fetched. This can reduce memory consumption when fetching large numbers of jobs, but if <i>condor_q</i> is paused while displaying results, this could result in a timeout in communication with <i>condor_schedd</i> .</p>
<dt>
<dd></dl>
<p> <code>-totals</code></p>
<dl>
<dt>
<dd> (output option) Display only the totals.</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> (output option) Print the HTCondor version and exit.</p>
<dt>
<dd></dl>
<p> <code>-wide</code></p>
<dl>
<dt>
<dd> (output option) If this option is specified, and the command portion of the output would cause the output to extend beyond 80 columns, display beyond the 80 columns.</p>
<dt>
<dd></dl>
<p> <code>-xml</code></p>
<dl>
<dt>
<dd> (output option) Display entire job ClassAds in XML format. The XML format is fully defined in the reference manual, obtained from the ClassAds web page, with a link at <a rel="nofollow" href="http://research.cs.wisc.edu/htcondor/research.html.">http://research.cs.wisc.edu/htcondor/research.html.</a></p>
<dt>
<dd></dl>
<p> <code>-attributes </code> <i>Attr1[,Attr2 &#8230; ]</i></p>
<dl>
<dt>
<dd> (output option) Explicitly list the attributes, by name in a comma separated list, which should be displayed when using the <code>-xml</code> or <code>-long</code> options. Limiting the number of attributes increases the efficiency of the query.</p>
<dt>
<dd></dl>
<p> <code>-format </code> <i>fmt attr</i></p>
<dl>
<dt>
<dd> (output option) Display attribute or expression <i>attr</i> in format <i>fmt</i> . To display the attribute or expression the format must contain a single <a href="/docs/linux/man/3-printf/">printf</a>(3) -style conversion specifier. Attributes must be from the job ClassAd. Expressions are ClassAd expressions and may refer to attributes in the job ClassAd. If the attribute is not present in a given ClassAd and cannot be parsed as an expression, then the format option will be silently skipped. %r prints the unevaluated, or raw values. The conversion specifier must match the type of the attribute or expression. %s is suitable for strings such as Owner , %d for integers such as ClusterId , and %f for floating point numbers such as RemoteWallClockTime . %v identifies the type of the attribute, and then prints the value in an appropriate format. %V identifies the type of the attribute, and then prints the value in an appropriate format as it would appear in the <code>-long</code> format. As an example, strings used with %V will have quote marks. An incorrect format will result in undefined behavior. Do not use more than one conversion specifier in a given format. More than one conversion specifier will result in undefined behavior. To output multiple attributes repeat the <code>-format</code> option once for each desired attribute. Like <a href="/docs/linux/man/3-printf/">printf</a>(3) style formats, one may include other text that will be reproduced directly. A format without any conversion specifiers may be specified, but an attribute is still required. Include n to specify a line break.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-autoformat[:tn,lVh] </code> <i>attr1 [attr2 &#8230;]</i> or <code>-af[:tn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> (output option) Display attribute(s) or expression(s) formatted in a default way according to attribute types. This option takes an arbitrary number of attribute names as arguments, and prints out their values, with a space between each value and a newline character after the last value. It is like the <code>-format</code> option without format strings. This output option does <i>not</i> work in conjunction with any of the options <code>-run</code> , <code>-currentrun</code> , <code>-hold</code> , <code>-globus</code> , <code>-goodput</code> , or <code>-io</code> .</p>
<dt>
<dd> It is assumed that no attribute names begin with a dash character, so that the next word that begins with dash is the start of the next option. The <code>autoformat</code> option may be followed by a colon character and formatting qualifiers to deviate the output formatting from the default:</p>
<dt>
<dd> <code>r</code> print unevaluated, or raw values,</p>
<dt>
<dd> <code>t</code> add a tab character before each field instead of the default space character,</p>
<dt>
<dd> <code>n</code> add a newline character after each field,</p>
<dt>
<dd> <code>,</code> add a comma character after each field,</p>
<dt>
<dd> <code>l</code> label each field,</p>
<dt>
<dd> <code>V</code> use %V rather than %v for formatting,</p>
<dt>
<dd> <code>h</code> print headings before the first line of output.</p>
<dt>
<dd> The newline and comma characters may <i>not</i> be used together.</p>
<dt>
<dd></dl>
<p> <code>-analyze[:&lt;qual&gt;]</code></p>
<dl>
<dt>
<dd> (analyze option) Perform a matchmaking analysis on why the requested jobs are not running. First a simple analysis determines if the job is not running due to not being in a runnable state. If the job is in a runnable state, then this option is equivalent to <code>-better-analyze</code> . <code>&lt;qual&gt;</code> is a comma separated list containing one or more of</p>
<dt>
<dd> <code>priority</code> to consider user priority during the analysis</p>
<dt>
<dd> <code>summary</code> to show a one line summary for each job or machine</p>
<dt>
<dd> <code>reverse</code> to analyze machines, rather than jobs</p>
<dt>
<dd></dl>
<p> <code>-better-analyze[:&lt;qual&gt;]</code></p>
<dl>
<dt>
<dd> (analyze option) Perform a more detailed matchmaking analysis to determine how many resources are available to run the requested jobs. This option is never meaningful for Scheduler universe jobs and only meaningful for grid universe jobs doing matchmaking. <code>&lt;qual&gt;</code> is a comma separated list containing one or more of</p>
<dt>
<dd> <code>priority</code> to consider user priority during the analysis</p>
<dt>
<dd> <code>summary</code> to show a one line summary for each job or machine</p>
<dt>
<dd> <code>reverse</code> to analyze machines, rather than jobs</p>
<dt>
<dd></dl>
<p> <code>-machine </code> <i>name</i></p>
<dl>
<dt>
<dd> (analyze option) When doing matchmaking analysis, analyze only machine ClassAds that have slot or machine names that match the given name.</p>
<dt>
<dd></dl>
<p> <code>-mconstraint </code> <i>expression</i></p>
<dl>
<dt>
<dd> (analyze option) When doing matchmaking analysis, match only machine ClassAds which match the ClassAd expression constraint.</p>
<dt>
<dd></dl>
<p> <code>-slotads </code> <i>file</i></p>
<dl>
<dt>
<dd> (analyze option) When doing matchmaking analysis, use the machine ClassAds from the file instead of the ones from the <i>condor_collector</i> daemon. This is most useful for debugging purposes. The ClassAds appear as if <i>condor_status</i> <code>-long</code> is used.</p>
<dt>
<dd></dl>
<p> <code>-userprios </code> <i>file</i></p>
<dl>
<dt>
<dd> (analyze option) When doing matchmaking analysis with priority, read user priorities from the file rather than the ones from the <i>condor_negotiator</i> daemon. This is most useful for debugging purposes or to speed up analysis in situations where the <i>condor_negotiator</i> daemon is slow to respond to <i>condor_userprio</i> requests. The file should be in the format produced by <i>condor_userprio</i> <code>-long</code> .</p>
<dt>
<dd></dl>
<p> <code>-nouserprios</code></p>
<dl>
<dt>
<dd> (analyze option) Do not consider user priority during the analysis.</p>
<dt>
<dd></dl>
<p> <code>-reverse</code></p>
<dl>
<dt>
<dd> (analyze option) Analyze machine requirements against jobs.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> (analyze option) When doing analysis, show progress and include the names of specific machines in the output.</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> The default output from <i>condor_q</i> is formatted to be human readable, not script readable. In an effort to make the output fit within 80 characters, values in some fields might be truncated. Furthermore, the HTCondor Project can (and does) change the formatting of this default output as we see fit. Therefore, any script that is attempting to parse data from <i>condor_q</i> is strongly encouraged to use the <code>-format</code> option (described above, examples given below). </p>
<p> Although <i>-analyze</i> provides a very good first approximation, the analyzer cannot diagnose all possible situations, because the analysis is based on instantaneous and local information. Therefore, there are some situations such as when several submitters are contending for resources, or if the pool is rapidly changing state which cannot be accurately diagnosed. </p>
<p> Options <code>-goodput</code> , <code>-cputime</code> , and <code>-io</code> are most useful for standard universe jobs, since they rely on values computed when a job produces a checkpoint. </p>
<p> It is possible to to hold jobs that are in the X state. To avoid this it is best to construct a <code>-constraint </code> <i>expression</i> that option contains JobStatus != 3 if the user wishes to avoid this condition. </p>
<h2>Examples</h2>
<p> The <code>-format</code> option provides a way to specify both the job attributes and formatting of those attributes. There must be only one conversion specification per <code>-format</code> option. As an example, to list only Jane Doe&#8217;s jobs in the queue, choosing to print and format only the owner of the job, the command line arguments for the job, and the process ID of the job: </p>
<p> %condor_q -submitter jdoe -format &quot;%s&quot; Owner -format &quot; %s &quot; Args -format &quot;ProcId = %d
&quot; ProcId<br />
 jdoe 16386 2800 ProcId = 0<br />
 jdoe 16386 3000 ProcId = 1<br />
 jdoe 16386 3200 ProcId = 2<br />
 jdoe 16386 3400 ProcId = 3<br />
 jdoe 16386 3600 ProcId = 4<br />
 jdoe 16386 4200 ProcId = 7 </p>
<p> To display only the JobID&#8217;s of Jane Doe&#8217;s jobs you can use the following. </p>
<p> %condor_q -submitter jdoe -format &quot;%d.&quot; ClusterId -format &quot;%d
&quot; ProcId<br />
 27.0<br />
 27.1<br />
 27.2<br />
 27.3<br />
 27.4<br />
 27.7 </p>
<p> An example that shows the difference (first set of output) between not using an option to <i>condor_q</i> and (second set of output) using the <code>-globus</code> option: </p>
<p>&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OWNER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SUBMITTED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>RUN_TIME ST PRI SIZE CMD </p>
<p>&nbsp;<wbr>100.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>smith&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12/11 13:20&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0+00:00:02 R&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.0&nbsp;<wbr>&nbsp;<wbr>sleep 10 </p>
<p> 1 jobs; 0 idle, 1 running, 0 held </p>
<p>&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OWNER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>STATUS&nbsp;<wbr>&nbsp;<wbr>MANAGER&nbsp;<wbr>&nbsp;<wbr>HOST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EXECUTABLE </p>
<p>&nbsp;<wbr>100.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>smith&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ACTIVE fork&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>grid.example.com&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/bin/sleep </p>
<p> An example that shows the analysis in summary format: </p>
<p> $ condor_q -analyze:summary </p>
<p> &#8212; Submitter: submit-1.chtc.wisc.edu : &lt;192.168.100.43:9618?sock=11794_95bb_3&gt; : </p>
<p>&nbsp;<wbr>submit-1.chtc.wisc.edu<br />
 Analyzing matches for 5979 slots </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Autocluster&nbsp;<wbr>&nbsp;<wbr>Matches&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Machine&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Running&nbsp;<wbr>&nbsp;<wbr>Serving </p>
<p>&nbsp;<wbr>JobId&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Members/Idle&nbsp;<wbr>&nbsp;<wbr>Reqmnts&nbsp;<wbr>&nbsp;<wbr>Rejects Job&nbsp;<wbr>&nbsp;<wbr>Users Job Other User Avail Owner<br />
 &#8212;&#8212;&#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8211; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;- &#8212;&#8212;&#8212;- &#8212;&#8211; &#8212;&#8211;<br />
 25764522.0 7/0 5910 820 7/10 5046 34 smith<br />
 25764682.0 9/0 2172 603 9/9 1531 29 smith<br />
 25765082.0 18/0 2172 603 18/9 1531 29 smith<br />
 25765900.0 1/0 2172 603 1/9 1531 29 smith </p>
<p> An example that shows summary information by machine: </p>
<p> $ condor_q -ana:sum,rev </p>
<p> &#8212; Submitter: s-1.chtc.wisc.edu : &lt;192.168.100.43:9618?sock=11794_95bb_3&gt; : s-1.chtc.wisc.edu<br />
 Analyzing matches for 2885 jobs </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Slot&nbsp;<wbr>&nbsp;<wbr>Slot&#8217;s Req&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Job&#8217;s Req&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Both<br />
 Name Type Matches Job Matches Slot Match %<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; &#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;-<br />
 slot1 [at] INFO.wisc.edu Stat 2729 0 0.00<br />
 slot2 [at] INFO.wisc.edu Stat 2729 0 0.00<br />
 slot1 [at] aci-001.chtc.wisc.edu Part 0 2793 0.00<br />
 slot1_1 [at] a-001.chtc.wisc.edu Dyn 2644 2792 91.37<br />
 slot1_2 [at] a-001.chtc.wisc.edu Dyn 2623 2601 85.10<br />
 slot1_3 [at] a-001.chtc.wisc.edu Dyn 2644 2632 85.82<br />
 slot1_4 [at] a-001.chtc.wisc.edu Dyn 2644 2792 91.37<br />
 slot1 [at] a-002.chtc.wisc.edu Part 0 2633 0.00<br />
 slot1_10 [at] a-002.chtc.wisc.edu Den 2623 2601 85.10 </p>
<h2>Exit Status</h2>
<p> <i>condor_q</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
