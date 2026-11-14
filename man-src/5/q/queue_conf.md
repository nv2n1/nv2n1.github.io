---
title: "queue_conf(5)"
name: "queue_conf"
section: "5"
letter: "q"
url: "/docs/linux/man/5-queue_conf/"
description: "queue_conf – xxQS_NAMExx queue configuration file format"
---

<p>queue_conf &#8211; xxQS_NAMExx queue configuration file format</p>
<h2>Description</h2>
<p>This manual page describes the format of the template file for the cluster queue configuration. Via the <code>-aq</code> and <code>-mq</code> options of the command, you can add cluster queues and modify the configuration of any queue in the cluster. Any of these change operations can be rejected as a result of a failed integrity verification. </p>
<p> The queue configuration parameters take as values strings, integer decimal numbers, booleans, or time and memory specifiers (see <i>time_specifier</i> and <i>memory_specifier</i> in as well as comma-separated lists. </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The list of parameters below specifies the queue configuration file content. </p>
<p> For each parameter except <code>qname</code> and <code>hostlist</code>, it is possible to specify host-dependent values instead of a single value. This &quot;enhanced queue configuration specifier syntax&quot; takes the form</p>
<dl>
<dd>
<pre><i>parameter parameter_value</i>[<code>,[</code><i>host_id</i><code>=</code><i>parameter_value</i><code>]</code>]...</pre>
</dl>
<p> where <i>host_id</i> is a <code>host_identifier</code>, as defined in and <i>parameter_value</i> is of the correct form for each parameter, as described below. Spaces are allowed around &quot;<code>,</code>&quot; but not inside &quot;<code>[]</code>&quot;, except within list-valued <i>parameter_value</i>s. </p>
<p> An entry without brackets is always required as the default setting for all queue instances which don&#8217;t override it. Tuples with a <code>hostgroup_name</code> (see <i>host_id</i> override the default setting. Tuples with a <code>host_name</code> <i>host_id</i> override both the default and the host group setting. As an example, PEs with different allocation rules may be specified according to the core count of different node types:</p>
<dl>
<dd>
<pre>pe_list NONE,[@dual=all-mpi mpi-4],[@quad=all-mpi mpi-8]</pre>
</dl>
<p> The queue configuration is rejected if a default setting is absent. </p>
<p> Ambiguous configurations (those with more than one attribute setting for a particular host) cause the relevant queue instances to go into a &quot;configuration ambiguous&quot; state and not accept jobs. This is reported as &quot;<code>c</code>&quot; by and and may be diagnosed with <code>qstat -explain c</code>. Configurations containing override values for hosts not in the execution host list are accepted as &quot;detached&quot;, as indicated by the <code>-sds</code> argument of</p>
<h3><code>qname</code></h3>
<p>The name of the cluster queue in the format for <i>queue_name</i> in As template default &quot;template&quot; is used.</p>
<h3><code>hostlist</code></h3>
<p>A list of host identifiers in the format for <i>host_identifier</i> in For each host xxQS_NAMExx maintains a queue instance for running jobs on that particular host. Large numbers of hosts can easily be managed by using host groups rather than single host names. Both white-space and &quot;,&quot; can be used as list separators. (Template default: NONE, i.e. no hosts support the queue.)</p>
<h3><code>seq_no</code></h3>
<p>In conjunction with the hosts load situation at some time, this parameter specifies this queue&#8217;s position in the scheduling order within the suitable queues for a job to be dispatched according to the <code>queue_sort_method</code> (see </p>
<p> Regardless of the <code>queue_sort_method</code> setting, reports queue information in the order defined by the value of the <code>seq_no</code>. Set this parameter to a monotonically increasing sequence. (Type: number; template default: 0.)</p>
<h3><code>load_thresholds</code></h3>
<p><code>load_thresholds</code> is a list of load thresholds. When one of the thresholds is exceeded no further jobs will be scheduled to the queues and the relevant queue instance will be put into the &quot;alarm&quot; state by the overload condition. Arbitrary load values defined in the &quot;host&quot; and &quot;global&quot; complexes (see for details) can be used. </p>
<p> The syntax is that of a comma-separated list, with each list element consisting of the <i>complex_name</i> (see of a load value, an equal sign and the threshold value intended to trigger the overload situation (e.g. <code>load_avg=1.75,users_logged_in=5</code>). </p>
<p> <code>Note:</code> Load values as well as consumable resources may be scaled differently for different hosts if specified in the corresponding execution host definitions (refer to for more information). Load thresholds are compared against the scaled load and consumable values. Boolean complexes can be used to set an alarm state with the value <code>false</code>, typically from a load sensor which checks a host&#8217;s &quot;health&quot;, e.g. <code>load_avg=1.75,health=false</code>.</p>
<h3><code>suspend_thresholds</code></h3>
<p>A list of load thresholds with the same semantics as the <code>load_thresholds</code> parameter (see above), except that exceeding one of these thresholds initiates suspension of one of multiple jobs in the queue. See the <code>nsuspend</code> parameter below for details on the number of jobs which are suspended. There is an important relationship between the <code>suspend_threshold</code> and the <code>scheduler_interval</code>. If you have for example a suspend threshold on the np_load_avg, and the load exceeds the threshold, this does not have immediate effect. Jobs continue running until the next scheduling run, where the scheduler detects the threshold has been exceeded and sends an order to qmaster to suspend the job. The same applies for unsuspending.</p>
<h3><code>nsuspend</code></h3>
<p>The number of jobs which are suspended/enabled per time interval if at least one of the load thresholds in the <code>suspend_thresholds</code> list is exceeded or if no <code>suspend_threshold</code> is violated anymore, respectively. <code>Nsuspend</code> jobs are suspended in each time interval until no <code>suspend_thresholds</code> are exceeded anymore or all jobs in the queue are suspended. Jobs are enabled in the corresponding way if the <code>suspend_thresholds</code> are no longer exceeded. The time interval in which the suspensions of the jobs occur is defined in <code>suspend_interval</code> below.</p>
<h3><code>suspend_interval</code></h3>
<p>The time interval in which further <code>nsuspend</code> jobs are suspended if one of the <code>suspend_thresholds</code> (see above for both) is exceeded by the current load on the host on which the queue is located. The time interval is also used when enabling the jobs. The syntax is that of a <i>time_specifier</i> in</p>
<h3><code>priority</code></h3>
<p>The <code>priority</code> parameter specifies the <i><a href="/docs/linux/man/2-nice/">nice</a></i>(2) value at which jobs in this queue will be run. It is of type &quot;number&quot; and the default is zero (which means no nice value is set explicitly). Negative values (up to -20) correspond to a higher scheduling priority; positive values (up to +20) correspond to a lower scheduling priority. </p>
<p> Note, the value of <code>priority</code> has no effect if xxQS_NAMExx adjusts priorities dynamically to implement ticket-based entitlement policy goals. Dynamic priority adjustment is switched off by default due to <code>reprioritize</code> being set to false.</p>
<h3><code>min_cpu_interval</code></h3>
<p>The time between two automatic checkpoints in case of transparently checkpointing jobs. The maximum of the time requested by the user via and the time defined by the queue configuration is used as the checkpoint interval. Since checkpoint files may be quite large, and thus writing them to the file system may become expensive, users and administrators are advised to choose sufficiently large time intervals. <code>min_cpu_interval</code> is of type &quot;time&quot; and the default is 5 minutes (which usually is suitable for test purposes only). The syntax is that of a <i>time_specifier</i> in</p>
<h3><code>qtype</code></h3>
<p>The type of queue. Currently <code>BATCH</code>, <code>INTERACTIVE</code>, a combination in a comma-separated list of both, or <code>NONE</code>. </p>
<p> Jobs submitted with option <code>-now y</code> can only be scheduled on <i>interactive</i> queues, and <code>-now n</code> targets <i>batch</i> queues. <code>-now y</code> is the default for <i>qsh</i>, <i>qrsh</i>, and <i>qlogin</i>, while <code>-now n</code> is the default for <i>qsub</i>. Nevertheless, the option can be applied to all commands, with either argument, to direct jobs to specific queue types. </p>
<p> The formerly supported types <code>PARALLEL</code> and <code>CHECKPOINTING</code> are not allowed anymore. A queue instance is implicitly of type parallel/checkpointing if there is a parallel environment or a checkpointing interface specified for this queue instance in <code>pe_list</code>/<code>ckpt_list</code>, and is implicitly <code>BATCH</code><br />
&nbsp;if it has a parallel environment attached. Formerly possible settings e.g. </p>
<pre>qtype PARALLEL</pre>
<p>could be changed to </p>
<pre>qtype NONE
pe_list pe_name</pre>
<p>(Type string; default: batch interactive.)</p>
<h3><code>pe_list</code></h3>
<p>The list of administrator-defined parallel environment (see names to be associated with the queue. The default is <i>NONE</i>.</p>
<h3><code>ckpt_list</code></h3>
<p>The list of administrator-defined checkpointing interface names (see <i>ckpt_name</i> in to be associated with the queue. The default is <i>NONE</i>.</p>
<h3><code>rerun</code></h3>
<p>Defines a default behavior for jobs which are aborted by system crashes or manual &quot;violent&quot; (via <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)) shutdown of the complete xxQS_NAMExx system (including the of the jobs and their process hierarchy) on the queue host. As soon as is restarted and detects that a job has been aborted for such reasons it can be restarted if the jobs are restartable. A job may not be restartable, for example, if it updates databases (first reads then writes to the same record of a database/file), because aborting the job may have left the database in an inconsistent state. If the owner of a job wants to overrule the default behavior for the jobs in the queue the <code>-r</code> option of can be used. </p>
<p> The type of this parameter is boolean, thus either TRUE or FALSE can be specified. The default is FALSE, i.e. do not restart jobs automatically.</p>
<h3><code>slots</code></h3>
<p>The maximum number of slots that may be scheduled concurrently in instances of the queue. Type is number, valid values are 0 to 9999999. </p>
<p> If there are multiple queues defined on a host and they are not mutually suspendable, the host <code>slots</code> value should be set to the processor count on the host if you want to avoid potential over-subscription due to scheduling to more than one queue at a time.</p>
<h3><code>tmpdir</code></h3>
<p>The <code>tmpdir</code> parameter specifies the absolute path to the base of the temporary directory filesystem. When launches a job, it creates a uniquely-named directory in this filesystem for the purpose of holding scratch files during job execution. At job completion, this directory and its contents are removed automatically. The environment variables TMPDIR and TMP are set to the path of each job&#8217;s scratch directory. (Type string; default: /tmp.)</p>
<h3><code>shell</code></h3>
<p>If either <i>posix_compliant</i> or <i>script_from_stdin</i> is specified as the <code>shell_start_mode</code> parameter in the <code>shell</code> parameter specifies the executable path of the command interpreter (e.g. <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) or <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1)) to be used to process the job scripts executed in the queue. The definition of <code>shell</code> can be overruled by the job owner via the <code>-S</code> option. </p>
<p> The type of the parameter is string. The default is <code>/bin/sh</code>.</p>
<h3><code>shell_start_mode</code></h3>
<p>This parameter defines the mechanisms which are used to actually invoke the job scripts on the execution hosts. The following values are recognized:</p>
<dl>
<dt><i>unix_behavior</i></p>
<dd>If a user starts a job shell script under UNIX interactively by invoking it just with the script name, the operating system&#8217;s executable loader uses the information provided in a comment such as `#!/bin/csh&#8217; in the first line of the script to detect which command interpreter to start to interpret the script. This mechanism is used by xxQS_NAMExx when starting jobs if <i>unix_behavior</i> is defined as <code>shell_start_mode</code>.</p>
<dt><i>posix_compliant</i></p>
<dd>POSIX does not consider first script line comments such as `#!/bin/csh&#8217; significant. The POSIX standard for batch queuing systems (P1003.2d) therefore requires a compliant queuing system to ignore such lines and to use user specified or configured default command interpreters instead. Thus, if <code>shell_start_mode</code> is set to <i>posix_compliant</i> xxQS_NAMExx will either use the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see above).</p>
<dt><i>script_from_stdin</i></p>
<dd>Setting the <code>shell_start_mode</code> parameter either to <i>posix_compliant</i> or <i>unix_behavior</i> requires you to set the umask in use for such that every user has read access to the active_jobs directory in the spool directory of the corresponding execution daemon. In case you have <code>prolog</code> and <code>epilog</code> scripts configured, they also need to be readable by any user who may execute jobs.<br />
 If this violates your site&#8217;s security policies you may want to set <code>shell_start_mode</code> to <i>script_from_stdin</i>. This will force xxQS_NAMExx to open the job script, as well as the epilogue and prologue scripts, for reading into STDIN as root (if was started as root) before changing to the job owner&#8217;s user account. The script is then fed into the STDIN stream of the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see above).<br />
 Thus setting <code>shell_start_mode</code> to <i>script_from_stdin</i> also implies <i>posix_compliant</i> behavior. <code>Note</code>, however, that feeding scripts into the STDIN stream of a command interpreter may cause trouble if commands like <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1) are invoked inside a job script as they also process the STDIN stream of the command interpreter. These problems can usually be resolved by redirecting the STDIN channel of those commands to come from /dev/null (e.g. rsh host date &lt; /dev/null). <code>Note also</code>, that any command-line options associated with the job are passed to the executing shell. The shell will only forward them to the job if they are not recognized as valid shell options.</dl>
<p> The default for <code>shell_start_mode</code> is <i>posix_compliant</i>. Note, though, that the <code>shell_start_mode</code> can only be used for batch jobs submitted by and can&#8217;t be used for interactive jobs submitted by</p>
<h3><code>prolog</code></h3>
<p>This queue configuration entry overwrites cluster global or execution host-specific <code>prolog</code> definitions (see</p>
<h3><code>epilog</code></h3>
<p>This queue configuration entry overwrites cluster global or execution host-specific <code>epilog</code> definitions (see</p>
<h3><code>starter_method</code></h3>
<p>The specified executable path will be used as a job starter facility responsible for starting batch jobs instead of the built-in starter (which typically passes the job to a shell). The starter method is passed as arguments the command to run. This is typically the name of a copy of the batch script file, followed by any arguments supplied at job submission. However, depending on how the job was submitted, it might be a binary (with arguments), or a more general shell command line, e.g. supplied to <i>qrsh</i>. The following environment variables are used to pass information to the job starter concerning the shell environment which was configured or requested to start the job.</p>
<dl>
<dt><i>SGE_STARTER_SHELL_PATH</i></p>
<dd>The name of the requested shell to start the job</p>
<dt><i>SGE_STARTER_SHELL_START_MODE</i></p>
<dd>The configured <code>shell_start_mode</code></p>
<dt><i>SGE_STARTER_USE_LOGIN_SHELL</i></p>
<dd>Set to &quot;true&quot; if the shell is supposed to be used as a login shell (see <code>login_shells</code> in</dl>
<p> Ignoring those, a trivial starter method could be </p>
<pre> #!/bin/sh
 # set the environment somehow
 exec &quot;$@&quot;</pre>
<p>It is, at best, tricky to write a proper substitute for the builtin method as a shell script, taking account of the variables above. It is probably best to do so in a non-macro expanded scripting language (or a compiled language, as appropriate). </p>
<p> The starter_method will not be invoked for qsh, qlogin, or qrsh acting as rlogin. </p>
<p> The same pseudo-variables can be expanded to compose the command as for the following methods.</p>
<h3><code>suspend_method</code></h3>
<h3><code>resume_method</code></h3>
<h3><code>terminate_method</code></h3>
<p>These parameters can be used for overwriting the default method used by xxQS_NAMExx for suspension, release of a suspension and for termination of a job. Per default, the signals SIGSTOP, SIGCONT and SIGKILL are delivered to the job to perform these actions. However, for some applications this is not appropriate. </p>
<p> If no executable path is given, xxQS_NAMExx takes the specified parameter entries as the signal to be delivered instead of the default signal. A signal must be either a positive number or a signal name with the <code>SIG</code> prefix, as printed by <i>kill -l</i> (e.g. <code>SIGTERM</code>). </p>
<p> If an executable path is given (it must be an <i>absolute path</i> starting with a &quot;<code>/</code>&quot;); then this command, together with its arguments, is started by xxQS_NAMExx to perform the appropriate action. The following special variables are expanded at runtime, and can be used (besides any other strings which have to be interpreted by the procedures) to compose a command line:</p>
<dl>
<dt><i>$host</i></p>
<dd>The name of the host on which the procedure is started.</p>
<dt><i>$ja_task_id</i></p>
<dd>The array job task index (0 if not an array job).</p>
<dt><i>$job_owner</i></p>
<dd>The user name of the job owner.</p>
<dt><i>$job_id</i></p>
<dd>xxQS_NAMExx&#8217;s unique job identification number.</p>
<dt><i>$job_name</i></p>
<dd>The name of the job.</p>
<dt><i>$queue</i></p>
<dd>The name of the queue.</p>
<dt><i>$job_pid</i></p>
<dd>The pid of the job.</p>
<dt><i>$sge_cell</i></p>
<dd>The SGE_CELL environment variable (useful for locating files).</p>
<dt><i>$sge_root</i></p>
<dd>The SGE_ROOT environment variable (useful for locating files).</dl>
<p> Note that a method is only executed on the master node of a parallel job, so it may be necessary to propagate the necessary action to slave nodes explicitly. (However, MPI implementations may, for instance, respond to SIGTSTP sent to the master process by stopping all the distributed processes.) If an executable is used for a method, it is started in the same environment as for the job concerned (see</p>
<h3><code>notify</code></h3>
<p>The time to wait between delivery of SIGUSR1/SIGUSR2 notification signals and suspend/kill signals if the job was submitted with the <i>-notify</i> option.</p>
<h3><code>owner_list</code></h3>
<p>The <code>owner_list</code> comprises comma-separated <i><a href="/docs/linux/man/1-login/">login</a></i>(1) user names (see <i>user_name</i> in of those users who are authorized to disable and suspend this queue through (xxQS_NAMExx operators and managers can do this by default.) It is customary to set this field for queues on interactive workstations where the computing resources are shared between interactive sessions and xxQS_NAMExx jobs, allowing the workstation owner to have priority access. Owners can be managers, operators, or users. Owner privileges are necessary to use <code>qidle</code> (see (Default: NONE.)</p>
<h3><code>user_lists</code></h3>
<p>The <code>user_lists</code> parameter contains a comma-separated list of xxQS_NAMExx user access list names as described in Each user contained in at least one of the given access lists has access to the queue. If the <code>user_lists</code> parameter is set to NONE (the default) any user has access if not explicitly excluded via the <code>xuser_lists</code> parameter described below. If a user is contained both in an access list in <code>xuser_lists</code> and <code>user_lists</code>, the user is denied access to the queue.</p>
<h3><code>xuser_lists</code></h3>
<p>The <code>xuser_lists</code> parameter contains a comma-separated list of xxQS_NAMExx user access list names as described in Each user contained in at least one of the given access lists is not allowed to access the queue. If the <code>xuser_lists</code> parameter is set to NONE (the default) any user has access. If a user is contained both in an access list in <code>xuser_lists</code> and <code>user_lists</code>, the user is denied access to the queue.</p>
<h3><code>projects</code></h3>
<p>The <code>projects</code> parameter contains a comma-separated list of xxQS_NAMExx projects (see that have access to the queue. Any project not in this list is denied access to the queue. If set to NONE (the default), any project has access that is not specifically excluded via the <code>xprojects</code> parameter described below. If a project is in both the <code>projects</code> and <code>xprojects</code> parameters, the project is denied access to the queue.</p>
<h3><code>xprojects</code></h3>
<p>The <code>xprojects</code> parameter contains a comma-separated list of xxQS_NAMExx projects (see that are denied access to the queue. If set to NONE (the default), no projects are denied access other than those denied access based on the <code>projects</code> parameter described above. If a project is in both the <code>projects</code> and <code>xprojects</code> parameters, the project is denied access to the queue.</p>
<h3><code>subordinate_list</code></h3>
<p>There are two different types of subordination: </p>
<p> <code>1. Queuewise subordination</code> </p>
<p> A list of xxQS_NAMExx queue names in the format for <i>queue_name</i> in Subordinate relationships are in effect only between queue instances residing at the same host. The relationship does not apply and is ignored when jobs are running in queue instances on other hosts. Queue instances residing on the same host will be suspended when a specified count of jobs is running in this queue instance. The list specification is the same as that of the <code>load_thresholds</code> parameter above, e.g. low_pri_q=5,small_q. The numbers denote the job slots of the queue that have to be filled in the superordinated queue to trigger the suspension of the subordinated queue. If no value is assigned, a suspension is triggered if all slots of the queue are filled. </p>
<p> On nodes which host more than one queue, you might wish to accord better service to certain classes of jobs (e.g., queues that are dedicated to parallel processing might need priority over low priority production queues). The default is NONE. </p>
<p> <code>2. Slotwise preemption</code> </p>
<p> Slotwise preemption provides a means to ensure that high priority jobs get the resources they need, while at the same time low priority jobs on the same host are not unnecessarily preempted, maximizing the host utilization. Slotwise preemption is designed to provide different preemption actions, but with the current implementation only suspension is provided. This means there is a subordination relationship defined between queues similar to the queue-wise subordination, but if the suspend threshold is exceeded, the whole subordinated queue is not suspended, only single tasks running in single slots. </p>
<p> As with queue-wise subordination, the subordination relationships are in effect only between queue instances residing at the same host. The relationship does not apply and is ignored when jobs and tasks are running in queue instances on other hosts. </p>
<p> The syntax is: </p>
<p> slots=<i>threshold</i>(<i>queue_list</i>) </p>
<p> where</p>
<dl>
<dt> <i>threshold</i> =a positive integer number</p>
<dt> <i>queue_list</i>=<i>queue_def</i>[,<i>queue_list</i>]</p>
<dt> <i>queue_def</i> =<i>queue</i>[:<i>seq_no</i>][:<i>action</i>]</p>
<dt> <i>queue</i> =a xxQS_NAMExx queue name in the format for <i>queue_name</i> in</p>
<dt> &quot;<i>seq_no</i>&quot; =sequence number among all subordinated queues</p>
<dd>of the same depth in the tree.<br />
 The higher the sequence number, the lower is the priority of the queue. Default is 0, which is the highest priority.</p>
<dt> <i>action</i> =the action to be taken if the threshold is</p>
<dd>exceeded.<br />
 Supported are:<br />
 &quot;sr&quot;: Suspend the task with the shortest run time.<br />
 &quot;lr&quot;: Suspend the task with the longest run time.<br />
 Default is &quot;sr&quot;.</dl>
<p> Some examples of possible configurations and their functionalities: </p>
<p> a) The simplest configuration </p>
<p> subordinate_list slots=2(B.q) </p>
<p> which means the queue &quot;B.q&quot; is subordinated to the current queue (let&#8217;s call it &quot;A.q&quot;), the suspend threshold for all tasks running in &quot;A.q&quot; and &quot;B.q&quot; on the current host is two, the sequence number of &quot;B.q&quot; is &quot;0&quot; and the action is &quot;suspend task with shortest run time first&quot;. This subordination relationship looks like this: </p>
<pre> A.q
 |
 B.q</pre>
<p>This could be a typical configuration for a host with a dual core CPU. This subordination configuration ensures that tasks that are scheduled to &quot;A.q&quot; always get a CPU core for themselves, while jobs in &quot;B.q&quot; are not preempted as long as there are no jobs running in &quot;A.q&quot;. </p>
<p> If there is no task running in &quot;A.q&quot;, two tasks are running in &quot;B.q&quot; and a new task is scheduled to &quot;A.q&quot;, the sum of tasks running in &quot;A.q&quot; and &quot;B.q&quot; is three. Three is greater than two, so this triggers the defined action. This causes the task with the shortest run time in the subordinated queue &quot;B.q&quot; to be suspended. After suspension, there is one task running in &quot;A.q&quot;, one task running in &quot;B.q&quot;, and one task suspended in &quot;B.q&quot;. </p>
<p> b) A simple tree </p>
<p> subordinate_list slots=2(B.q:1, C.q:2) </p>
<p> This defines a small tree that looks like this: </p>
<pre> A.q
 / \
 B.q C.q</pre>
<p>A use case for this configuration could be a host with a dual core CPU and queue &quot;B.q&quot; and &quot;C.q&quot; for jobs with different requirements, e.g. &quot;B.q&quot; for interactive jobs, &quot;C.q&quot; for batch jobs. Again, the tasks in &quot;A.q&quot; always get a CPU core, while tasks in &quot;B.q&quot; and &quot;C.q&quot; are suspended only if the threshold of running tasks is exceeded. Here the sequence number among the queues of the same depth comes into play. Tasks scheduled to &quot;B.q&quot; can&#8217;t directly trigger the suspension of tasks in &quot;C.q&quot;, but if there is a task to be suspended, first &quot;C.q&quot; will be searched for a suitable task. </p>
<p> If there is one task running in &quot;A.q&quot;, one in &quot;C.q&quot; and a new task is scheduled to &quot;B.q&quot;, the threshold of &quot;2&quot; in &quot;A.q&quot;, &quot;B.q&quot; and &quot;C.q&quot; is exceeded. This triggers the suspension of one task in either &quot;B.q&quot; or &quot;C.q&quot;. The sequence number gives &quot;B.q&quot; a higher priority than &quot;C.q&quot;, therefore the task in &quot;C.q&quot; is suspended. After suspension, there is one task running in &quot;A.q&quot;, one task running in &quot;B.q&quot; and one task suspended in &quot;C.q&quot;. </p>
<p> c) More than two levels </p>
<p> Configuration of A.q: subordinate_list slots=2(B.q)<br />
 Configuration of B.q: subordinate_list slots=2(C.q) </p>
<p> looks like this: </p>
<pre> A.q
 |
 B.q
 |
 C.q</pre>
<p>These are three queues with high, medium and low priority. If a task is scheduled to &quot;C.q&quot;, first the subtree consisting of &quot;B.q&quot; and &quot;C.q&quot; is checked, the number of tasks running there is counted. If the threshold which is defined in &quot;B.q&quot; is exceeded, the job in &quot;C.q&quot; is suspended. Then the whole tree is checked, if the number of tasks running in &quot;A.q&quot;, &quot;B.q&quot; and &quot;C.q&quot; exceeds the threshold defined in &quot;A.q&quot; the task in &quot;C.q&quot; is suspended. This means, the effective threshold of any subtree is not higher than the threshold of the root node of the tree. If in this example a task is scheduled to &quot;A.q&quot;, immediately the number of tasks running in &quot;A.q&quot;, &quot;B.q&quot; and &quot;C.q&quot; is checked against the threshold defined in &quot;A.q&quot;. </p>
<p> d) Any tree </p>
<pre> A.q
 / \
 B.q C.q
 / / \
 D.q E.q F.q
 \
 G.q </pre>
<p>The computation of the tasks that are to be (un)suspended always starts at the queue instance that is modified, i.e. a task is scheduled to, a task ends at, the configuration is modified, a manual or other automatic (un)suspend is issued, except when it is a leaf node, like &quot;D.q&quot;, &quot;E.q&quot; and &quot;G.q&quot; in this example. Then the computation starts at its parent queue instance (like &quot;B.q&quot;, &quot;C.q&quot; or &quot;F.q&quot; in this example). From there first all running tasks in the whole subtree of this queue instance are counted. If the sum exceeds the threshold configured in the subordinate_list, in this subtree a task is sought to be suspended. Then the algorithm proceeds to the parent of this queue instance, counts all running tasks in the whole subtree below the parent, and checks if the number exceeds the threshold configured in the parent&#8217;s subordinate_list. If so, it searches for a task to suspend in the whole subtree below the parent. And so on, until it did this computation for the root node of the tree.</p>
<h3><code>complex_values</code></h3>
<p><code>complex_values</code> defines quotas for resource attributes managed via this queue. The syntax is the same as for <code>load_thresholds</code> (see above). The quotas are related to the resource consumption of all jobs in a queue in the case of consumable resources (see for details on consumable resources) or they are interpreted on a per queue slot (see <code>slots</code> above) basis in the case of non-consumable resources. Consumable resource attributes are commonly used to manage free memory, free disk space or available floating software licenses, while non-consumable attributes usually define distinctive characteristics, like the type of hardware installed. </p>
<p> For consumable resource attributes an available resource amount is determined by subtracting the current resource consumption of all running jobs in the queue from the quota in the <code>complex_values</code> list. Jobs can only be dispatched to a queue if no resource requests exceed any corresponding resource availability obtained by this scheme. The quota definition in the <code>complex_values</code> list is automatically replaced by the current load value reported for this attribute if load is monitored for this resource and if the reported load value is more stringent than the quota. This effectively avoids oversubscription of resources. </p>
<p> <code>Note:</code> Load values replacing the quota specifications may have become more stringent because they have been scaled (see and/or load adjusted (see The <i>-F</i> option of and the load display in the queue control dialog (activated by clicking on a queue icon while the &quot;Shift&quot; key is pressed) provide detailed information on the actual availability of consumable resources and on the origin of the values taken into account currently. </p>
<p> <code>Note also:</code> The resource consumption of running jobs (used for the availability calculation) as well as the resource requests of the jobs waiting to be dispatched either may be derived from explicit user requests during job submission (see the <i>-l</i> option to or from a &quot;default&quot; value configured for an attribute by the administrator (see The <i>-r</i> option to can be used for retrieving full detail on the actual resource requests of all jobs in the system. </p>
<p> For non-consumable resources xxQS_NAMExx simply compares the job&#8217;s attribute requests with the corresponding specification in <code>complex_values</code>, taking the relation operator of the complex attribute definition into account (see If the result of the comparison is &quot;true&quot;, the queue is suitable for the job with respect to the particular attribute. For parallel jobs each queue slot to be occupied by a parallel task is meant to provide the same resource attribute value. </p>
<p> <code>Note:</code> Only numeric complex attributes can be defined as consumable resources, hence non-numeric attributes are always handled on a per queue slot basis. </p>
<p> The default value for this parameter is NONE, i.e. no administrator defined resource attribute quotas are associated with the queue.</p>
<h3><code>calendar</code></h3>
<p>specifies the <code>calendar</code> to be valid for this queue or contains NONE (the default). A calendar defines the availability of a queue depending on time of day, week and year. Please refer to for details on the xxQS_NAMExx calendar facility. </p>
<p> <code>Note:</code> Jobs can request queues with a certain calendar model via a &quot;-l c=<i>cal_name</i>&quot; option to</p>
<h3><code>initial_state</code></h3>
<p>defines an initial state for the queue, either when adding the queue to the system for the first time or on start-up of the on the host on which the queue resides. Possible values are:</p>
<dl>
<dt>default</p>
<dd>The queue is enabled when adding the queue, or is reset to the previous status when comes up (this corresponds to the behavior in earlier xxQS_NAMExx releases not supporting initial_state).</p>
<dt>enabled</p>
<dd>The queue is enabled in either case. This is equivalent to a manual and explicit &#8216;<i>qmod -e</i>&#8216; command (see</p>
<dt>disabled</p>
<dd>The queue is disabled in either case. This is equivalent to a manual and explicit &#8216;<i>qmod -d</i>&#8216; command (see</dl>
<h2>Resource Limits</h2>
<p>The first two resource limit parameters, <code>s_rt</code> and <code>h_rt</code>, are implemented by xxQS_NAMExx. They define the &quot;real time&quot; (also called &quot;elapsed&quot; or &quot;wall clock&quot; time) passed since the start of the job. If <code>h_rt</code> is exceeded by a job running in the queue, it is aborted via the SIGKILL signal (see <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)). If <code>s_rt</code> is exceeded, the job is first &quot;warned&quot; via the SIGUSR1 signal (which can be caught by the job) and finally aborted after the notification time defined in the queue configuration parameter <code>notify</code> (see above) has passed. In cases when <code>s_rt</code> is used in combination with job notification it might be necessary to configure a signal other than SIGUSR1 using the NOTIFY_KILL and NOTIFY_SUSP execd_params (see so that the jobs&#8217; signal-catching mechanism can differ in each case and react accordingly. </p>
<p> The resource limit parameters <code>s_cpu</code> and <code>h_cpu</code> are implemented by xxQS_NAMExx as a job limit. They impose a limit on the amount of combined CPU time consumed by all the processes in the job. If <code>h_cpu</code> is exceeded by a job running in the queue, it is aborted via a SIGKILL signal (see <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)). If <code>s_cpu</code> is exceeded, the job is sent a SIGXCPU signal which can be caught by the job. If you wish to allow a job to be &quot;warned&quot; so it can exit gracefully before it is killed, then you should set the <code>s_cpu</code> limit to a lower value than <code>h_cpu</code>. For parallel processes, the limit is applied per slot, which means that the limit is multiplied by the number of slots being used by the job before being applied. </p>
<p> The resource limit parameters <code>s_vmem</code> and <code>h_vmem</code> are implemented by xxQS_NAMExx as a job limit. They impose a limit on the amount of combined virtual memory consumed by all the processes in the job. If <code>h_vmem</code> is exceeded by a job running in the queue, it is aborted via a SIGKILL signal (see <a href="/docs/linux/man/1-kill/">kill</a>(1)). If <code>s_vmem</code> is exceeded, the job is sent a SIGXCPU signal which can be caught by the job. If you wish to allow a job to be &quot;warned&quot; so it can exit gracefully before it is killed, then you should set the <code>s_vmem</code> limit to a lower value than <code>h_vmem</code>. For parallel processes, the limit is applied per slot which means that the limit is multiplied by the number of slots being used by the job before being applied. </p>
<p> The remaining parameters in the queue configuration template specify per-job soft and hard resource limits as implemented by the <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2) system call. See this manual page on your system for more information. By default, each limit field is set to infinity (which means RLIM_INFINITY as described in the <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2) manual page). The value type for the CPU-time limits <code>s_cpu</code> and <code>h_cpu</code> is time. The value type for the other limits is memory. <code>Note:</code> Not all systems support <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2). </p>
<p> <code>Note also:</code> s_vmem and h_vmem (virtual memory) are only available on systems supporting RLIMIT_VMEM (see <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2) on your operating system).</p>
<h2>Security</h2>
<p>See for security considerations when specifying <code>prolog</code> and <code>epilog</code> with a <i>user</i><code>@</code> prefix.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/2-nice/">nice</a></i>(2), <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2),</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
