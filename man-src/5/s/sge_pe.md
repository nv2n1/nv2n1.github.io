---
title: "sge_pe(5)"
name: "sge_pe"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_pe/"
description: "xxqs_name_sxx_pe – xxQS_NAMExx parallel environment configuration file format"
---

<p>xxqs_name_sxx_pe &#8211; xxQS_NAMExx parallel environment configuration file format</p>
<h2>Description</h2>
<p>Parallel environments are parallel programming and runtime environments supporting the execution of shared memory or distributed memory parallelized applications. Parallel environments usually require some kind of setup to be operational before starting parallel applications. Examples of common parallel environments are OpenMP on shared memory multiprocessor systems, and Message Passing Interface (MPI) on shared memory or distributed systems. </p>
<p> <i>xxqs_name_sxx_pe</i> allows for the definition of interfaces to arbitrary parallel environments. Once a parallel environment is defined or modified with the <code>-ap</code> or <code>-mp</code> options to and linked with one or more queues via <i>pe_list</i> in the environment can be requested for a job via the <code>-pe</code> switch to together with a request for a numeric range of parallel processes to be allocated by the job. Additional <code>-l</code> options may be used to specify more detailed job requirements. </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The format of a <i>xxqs_name_sxx_pe</i> file is defined as follows:</p>
<h3><code>pe_name</code></h3>
<p>The name of the parallel environment in the format for <i>pe_name</i> in To be used in the <code>-pe</code> switch.</p>
<h3><code>slots</code></h3>
<p>The total number of slots (normally one per parallel process or thread) allowed to be filled concurrently under the parallel environment. Type is integer, valid values are 0 to 9999999.</p>
<h3><code>user_lists</code></h3>
<h3><code>xuser_lists</code></h3>
<p>A comma-separated list of user access list names (see </p>
<p> Each user contained in at least one of the <code>user_lists</code> access lists has access to the parallel environment. If the <code>user_lists</code> parameter is set to NONE (the default) any user has access if not explicitly excluded via the <code>xuser_lists</code> parameter. </p>
<p> Each user contained in at least one of the <code>xuser_lists</code> access lists is not allowed to access the parallel environment. If the <code>xuser_lists</code> parameter is set to NONE (the default) any user has access. </p>
<p> If a user is contained both in an access list in <code>xuser_lists</code> and <code>user_lists</code> the user is denied access to the parallel environment.</p>
<h3><code>start_proc_args</code></h3>
<h3><code>stop_proc_args</code></h3>
<p>The command line respectively of a startup or shutdown procedure (an executable command, plus possible arguments) for the parallel environment, or &quot;none&quot; for no procedure (typically for tightly integrated PEs). The command line is started directly, not in a shell. An optional prefix &quot;<i>user</i><code>@</code>&quot; specifies the username under which the procedure is to be started. In that case see the SECURITY section below concerning security issues running as a privileged user. </p>
<p> The startup procedure is invoked by on the master node of the job prior to executing the job script. Its purpose is to setup the parallel environment according to its needs. The shutdown procedure is invoked by after the job script has finished. Its purpose is to stop the parallel environment and to remove it from all participating systems. The standard output of the procedure is redirected to the file <i>REQUEST</i>.po<i>JID</i> in the job&#8217;s working directory (see with <i>REQUEST</i> being the name of the job as displayed by and <i>JID</i> being the job&#8217;s identification number. Likewise, the standard error output is redirected to <i>REQUEST</i>.pe<i>JID</i>. If the <code>-e</code> or <code>-o</code> options are given on job submission, the PE error and standard output is merged into the paths specified. </p>
<p> The following special variables, expanded at runtime, can be used (besides any other strings which have to be interpreted by the start and stop procedures) to constitute a command line:</p>
<dl>
<dt><i>$pe_hostfile</i></p>
<dd>The pathname of a file containing a detailed description of the layout of the parallel environment to be setup by the start-up procedure. Each line of the file refers to a host on which parallel processes are to be run. The first entry of each line denotes the hostname, the second entry the number of parallel processes to be run on the host, the third entry the name of the queue. The entries are separated by spaces. If <code>-binding pe</code> is specified on job submission, the fourth column is the core binding specification as colon-separated socket-core pairs, like &quot;0,0:0,1&quot;, meaning the first core on the first socket and the second core on the first socket can be used for binding. Otherwise it will be &quot;UNDEFINED&quot;. With the obsolete queue <code>processors</code> specification the fourth entry could be a multi-processor configuration (or &quot;&lt;NULL&gt;&quot;).</p>
<dt><i>$host</i></p>
<dd>The name of the host on which the startup or stop procedures are run.</p>
<dt><i>$ja_task_id</i></p>
<dd>The array job task index (0 if not an array job).</p>
<dt><i>$job_owner</i></p>
<dd>The user name of the job owner.</p>
<dt><i>$job_id</i></p>
<dd>xxQS_NAMExx&#8217;s unique job identification number.</p>
<dt><i>$job_name</i></p>
<dd>The name of the job.</p>
<dt><i>$pe</i></p>
<dd>The name of the parallel environment in use.</p>
<dt><i>$pe_slots</i></p>
<dd>Number of slots granted for the job.</p>
<dt><i>$queue</i></p>
<dd>The cluster queue of the master queue instance.</p>
<dt><i>$sge_cell</i></p>
<dd>The SGE_CELL environment variable (useful for locating files).</p>
<dt><i>$sge_root</i></p>
<dd>The SGE_ROOT environment variable (useful for locating files).</p>
<dt><i>$stdin_path</i></p>
<dd>The standard input path.</p>
<dt><i>$stderr_path</i></p>
<dd>The standard error path.</p>
<dt><i>$stdout_path</i></p>
<dd>The standard output path.</p>
<dt><i>$merge_stderr</i></p>
<dd>
<dt><i>$fs_stdin_host</i></p>
<dd>
<dt><i>$fs_stdin_path</i></p>
<dd>
<dt><i>$fs_stdin_tmp_path</i></p>
<dd>
<dt><i>$fs_stdin_file_staging</i></p>
<dd>
<dt><i>$fs_stdout_host</i></p>
<dd>
<dt><i>$fs_stdout_path</i></p>
<dd>
<dt><i>$fs_stdout_tmp_path</i></p>
<dd>
<dt><i>$fs_stdout_file_staging</i></p>
<dd>
<dt><i>$fs_stderr_host</i></p>
<dd>
<dt><i>$fs_stderr_path</i></p>
<dd>
<dt><i>$fs_stderr_tmp_path</i></p>
<dd>
<dt><i>$fs_stderr_file_staging</i></p>
<dd></dl>
<p> The start and stop commands are run with the same environment setting as that of the job to be started afterwards (see</p>
<h3><code>allocation_rule</code></h3>
<p>The allocation rule is interpreted by the scheduler thread and helps the scheduler to decide how to distribute parallel processes among the available machines. If, for instance, a parallel environment is built for shared memory applications only, all parallel processes have to be assigned to a single machine, no matter how many suitable machines are available. If, however, the parallel environment follows the distributed memory paradigm, an even distribution of processes among machines may be favorable, as may packing processes onto the minimum number of machines. </p>
<p> The current version of the scheduler only understands the following allocation rules:</p>
<dl>
<dt><i>int</i></p>
<dd>An integer, fixing the number of processes per host. If it is 1, all processes have to reside on different hosts. If the special name <code>$pe_slots</code> is used, the full range of processes as specified with the <code>-pe</code> switch has to be allocated on a single host (no matter what value belonging to the range is finally chosen for the job to be allocated).</p>
<dt><code>$fill_up</code></p>
<dd>Starting from the best suitable host/queue, all available slots are allocated. Further hosts and queues are &quot;filled up&quot; as long as a job still requires slots for parallel tasks.</p>
<dt><code>$round_robin</code></p>
<dd>From all suitable hosts, a single slot is allocated until all tasks requested by the parallel job are dispatched. If more tasks are requested than suitable hosts are found, allocation starts again from the first host. The allocation scheme walks through suitable hosts in a most-suitable-first order.</dl>
<h3><code>control_slaves</code></h3>
<p>This parameter can be set to TRUE or FALSE (the default). It indicates whether xxQS_NAMExx is the creator of the slave tasks of a parallel application via and and thus has full control over all processes in a parallel application (&quot;tight integration&quot;). This enables:</p>
<dl>
<dt>&bull;</p>
<dd>resource limits are enforced for all tasks, even on slave hosts;</p>
<dt>&bull;</p>
<dd>resource consumption is properly accounted on all hosts;</p>
<dt>&bull;</p>
<dd>proper control of tasks, with no need to write a customized terminate method to ensure that whole job is finished on <i>qdel</i> and that tasks are properly reaped in the case of abnormal job termination;</p>
<dt>&bull;</p>
<dd>all tasks are started with the appropriate nice value which was configured as <code>priority</code> in the queue configuration;</p>
<dt>&bull;</p>
<dd>propagation of the job environment to slave hosts, e.g. so that they write into the appropriate per-job temporary directory specified by TMPDIR, which is created on each host and properly cleaned up.</dl>
<p> To gain control over the slave tasks of a parallel application, a sophisticated PE interface is required, which works closely together with xxQS_NAMExx facilities, typically interpreting the xxQS_NAMExx hostfile and starting remote tasks with and its <code>-inherit</code> option. See, for instance, the <code>$SGE_ROOT/mpi</code> directory and the howto pages &lt;URL: <a rel="nofollow" href="https://gridengine.sourceforge.io/SGE/howto/#Tight%20Integration%20of%20Parallel%20Libraries">https://gridengine.sourceforge.io/SGE/howto/#Tight%20Integration%20of%20Parallel%20Libraries</a> &gt;. </p>
<p> Please set the <code>control_slaves</code> parameter to false for all other PE interfaces.</p>
<h3><code>job_is_first_task</code></h3>
<p>The <code>job_is_first_task</code> parameter can be set to TRUE or FALSE. A value of TRUE indicates that the xxQS_NAMExx job script already contains one of the tasks of the parallel application (and the number of slots reserved for the job is the number of slots requested with the -pe switch). FALSE indicates that the job script (and its child processes) is not part of the parallel program, just being used to kick off the tasks that do the work; then the number of slots reserved for the job in the master queue is increased by 1, as indicated by <i>qstat</i>/<i>qhost</i>. </p>
<p> This should be TRUE for the common modern MPI implementations with tight integration. Consider if the allocation rule is <code>$fill_up</code>, and a job is allocated only a single slot on the master host; then one of the MPI processes actually runs in that slot, and should be accounted as such, so the job is the first task. </p>
<p> If wallclock accounting is used (<code>execd_params</code> <code>ACCT_RESERVED_USAGE</code><br />
&nbsp;and/or <code>SHARETREE_RESERVED_USAGE</code> Is <code>TRUE</code>) and <code>control_slaves</code> is set to FALSE, the <code>job_is_first_task</code> parameter influences the accounting for the job: A value of TRUE means that accounting for CPU and requested memory gets multiplied by the number of slots requested with the -pe switch. FALSE means the accounting information gets multiplied by number of slots + 1. Otherwise, the only significant effect of the parameter is on the display of the job.</p>
<h3><code>urgency_slots</code></h3>
<p>For pending jobs with a slot range PE request with different minimum and maximum, the number of slots they will actually use is not determined. This setting specifies the method to be used by xxQS_NAMExx to assess the number of slots such jobs might finally get. </p>
<p> The assumed slot allocation has a meaning when determining the resource-request-based priority contribution for numeric resources as described in and is displayed when is run without <code>-g t</code> option. </p>
<p> The following methods are supported:</p>
<dl>
<dt><i>int</i></p>
<dd>The specified integer number is directly used as prospective slot amount.</p>
<dt><code>min</code></p>
<dd>The slot range minimum is used as prospective slot amount. If no lower bound is specified with the range, 1 is assumed.</p>
<dt><code>max</code></p>
<dd>The slot range maximum is used as prospective slot amount. If no upper bound is specified with the range, the absolute maximum possible due to the PE&#8217;s <code>slots</code> setting is assumed.</p>
<dt><code>avg</code></p>
<dd>The average of all numbers occurring within the job&#8217;s PE range request is assumed.</dl>
<h3><code>accounting_summary</code></h3>
<p>This parameter is only checked if <code>control_slaves</code> (see above) is set to TRUE and thus xxQS_NAMExx is the creator of the slave tasks of a parallel application via and In this case, accounting information is available for every single slave task started by xxQS_NAMExx. </p>
<p> The <code>accounting_summary</code> parameter can be set to TRUE or FALSE. A value of TRUE indicates that only a single accounting record is written to the file, containing the accounting summary of the whole job, including all slave tasks, while a value of FALSE indicates an individual record is written for every slave task, as well as for the master task. </p>
<p> <code>Note:</code> When running tightly integrated jobs with <i>SHARETREE_RESERVED_USAGE</i> set, and <i>accounting_summary</i> enabled in the parallel environment, reserved usage will only be reported by the master task of the parallel job. No per-parallel task usage records will be sent from execd to qmaster, which can significantly reduce load on the qmaster when running large, tightly integrated parallel jobs. However, this removes the only post-hoc information about which hosts a job used.</p>
<h3><code>qsort_args </code><i>library qsort-function </i>[arg1 &#8230;]</h3>
<p>Specifies a method for specifying the queues/hosts and order that should be used to schedule a parallel job. For details, and the API, consult the header file <i>$SGE_ROOT/include/sge_pqs_api.h</i>. <i>library</i> is the path to the qsort dynamic library, <i>qsort-function</i> is the name of the qsort function implemented by the library, and the <i>arg</i>s are arguments passed to <i>qsort</i>. Substitutions from the hard requested resource list for the job are made for any strings of the form $<i>resource</i>, where <i>resource</i> is the full name of the resource as defined in the list. If <i>resource</i> is not requested in the job, a null string is substituted.</p>
<h2>Restrictions</h2>
<p><code>Note</code> that the functionality of the start and stop procedures remains the full responsibility of the administrator configuring the parallel environment. xxQS_NAMExx will invoke these procedures and evaluate their exit status. A non-zero exit status will put the queue into an error state. If the start procedure has a non-zero exit status, the job will be re-queued.</p>
<h2>Security</h2>
<p>If <code>start_proc_args</code>, or <code>stop_proc_args</code> is specified with a <i>user</i><code>@</code> prefix, the same considerations apply as for the prolog and epilog, as described in the SECURITY section of</p>
<h2>See Also</h2>
<h2>Files</h2>
<p><i>$SGE_ROOT/include/sge_pqs_api.h</i></p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
