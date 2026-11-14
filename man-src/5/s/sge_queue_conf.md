---
title: "sge_queue_conf(5)"
name: "sge_queue_conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_queue_conf/"
description: "queue_conf – Grid Engine queue configuration file format"
---

<p>queue_conf &#8211; Grid Engine queue configuration file format</p>
<h2>Description</h2>
<p>This manual page describes the format of the template file for the cluster queue configuration. Via the <code>-aq</code> and <code>-mq</code> options of the command, you can add cluster queues and modify the configuration of any queue in the cluster. Any of these change operations can be rejected, as a result of a failed integrity verification. </p>
<p> The queue configuration parameters take as values strings, integer decimal numbers or boolean, time and memory specifiers (see <i>time_specifier</i> and <i>memory_specifier</i> in as well as comma separated lists. </p>
<p> Note, Grid Engine allows backslashes (\) be used to escape newline (
ewline) characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>The following list of parameters specifies the queue configuration file content:</p>
<h3><code>qname</code></h3>
<p>The name of the cluster queue as defined for <i>queue_name</i> in As template default &quot;template&quot; is used.</p>
<h3><code>hostlist</code></h3>
<p>A list of host identifiers as defined for <i>host_identifier</i> in For each host Grid Engine maintains a queue instance for running jobs on that particular host. Large amounts of hosts can easily be managed by using host groups rather than by single host names. As list separators white-spaces and &quot;,&quot; can be used. (template default: NONE). </p>
<p> If more than one host is specified it can be desirable to specify divergences with the further below parameter settings for certain hosts. These divergences can be expressed using the enhanced queue configuration specifier syntax. This syntax builds upon the regular parameter specifier syntax separately for each parameter: </p>
<p> &quot;[&quot;<i>host_identifier</i>=&lt;parameters_specifier_syntax&gt;&quot;]&quot; [,&quot;[&quot;<i>host_identifier</i>=&lt;parameters_specifier_syntax&gt;&quot;]&quot; ] </p>
<p> note, even in the enhanced queue configuration specifier syntax an entry without brackets denoting the default setting is required and used for all queue instances where no divergences are specified. Tuples with a host group <i>host_identifier</i> override the default setting. Tuples with a host name host_identifier override both the default and the host group setting. </p>
<p> Note that also with the enhanced queue configuration specifier syntax a default setting is always needed for each configuration attribute; otherwise the queue configuration gets rejected. Ambiguous queue configurations with more than one attribute setting for a particular host are rejected. Configurations containing override values for hosts not enlisted under &#8216;hostname&#8217; are accepted but are indicated by <code>-sds</code> of The cluster queue should contain an unambiguous specification for each configuration attribute of each queue instance specified under hostname in the queue configuration. Ambiguous configurations with more than one attribute setting resulting from overlapping host groups are indicated by <code>-explain c</code> of and cause the queue instance with ambiguous configurations to enter the c(onfiguration ambiguous) state.</p>
<h3><code>seq_no</code></h3>
<p>In conjunction with the hosts load situation at a time this parameter specifies this queue&#8217;s position in the scheduling order within the suitable queues for a job to be dispatched under consideration of the <code>queue_sort_method</code> (see ). </p>
<p> Regardless of the <code>queue_sort_method</code> setting, reports queue information in the order defined by the value of the <code>seq_no</code>. Set this parameter to a monotonically increasing sequence. (type number; template default: 0).</p>
<h3><code>load_thresholds</code></h3>
<p><code>load_thresholds</code> is a list of load thresholds. Already if one of the thresholds is exceeded no further jobs will be scheduled to the queues and will signal an overload condition for this node. Arbitrary load values being defined in the &quot;host&quot; and &quot;global&quot; complexes (see for details) can be used. </p>
<p> The syntax is that of a comma separated list with each list element consisting of the <i>complex_name</i> (see of a load value, an equal sign and the threshold value being intended to trigger the overload situation (e.g. load_avg=1.75,users_logged_in=5). </p>
<p> <code>Note:</code> Load values as well as consumable resources may be scaled differently for different hosts if specified in the corresponding execution host definitions (refer to for more information). Load thresholds are compared against the scaled load and consumable values.</p>
<h3><code>suspend_thresholds</code></h3>
<p>A list of load thresholds with the same semantics as that of the <code>load_thresholds</code> parameter (see above) except that exceeding one of the denoted thresholds initiates suspension of one of multiple jobs in the queue. See the <code>nsuspend</code> parameter below for details on the number of jobs which are suspended.</p>
<h3><code>nsuspend</code></h3>
<p>The number of jobs which are suspended/enabled per time interval if at least one of the load thresholds in the <code>suspend_thresholds</code> list is exceeded or if no <code>suspend_threshold</code> is violated anymore respectively. <code>Nsuspend</code> jobs are suspended in each time interval until no <code>suspend_thresholds</code> are exceeded anymore or all jobs in the queue are suspended. Jobs are enabled in the corresponding way if the <code>suspend_thresholds</code> are no longer exceeded. The time interval in which the suspensions of the jobs occur is defined in <code>suspend_interval</code> below.</p>
<h3><code>suspend_interval</code></h3>
<p>The time interval in which further <code>nsuspend</code> jobs are suspended if one of the <code>suspend_thresholds</code> (see above for both) is exceeded by the current load on the host on which the queue is located. The time interval is also used when enabling the jobs. The syntax is that of a <i>time_specifier</i> in</p>
<h3><code>priority</code></h3>
<p>The <code>priority</code> parameter specifies the value at which jobs in this queue will be run. The type is number and the default is zero (which means no nice value is set explicitly). Negative values (up to -20) correspond to a higher scheduling priority, positive values (up to +20) correspond to a lower scheduling priority. </p>
<p> Note, the value of priority has no effect, if Grid Engine adjusts priorities dynamically to implement ticket-based entitlement policy goals. Dynamic priority adjustment is switched off by default due to <code>reprioritize</code> being set to false.</p>
<h3><code>min_cpu_interval</code></h3>
<p>The time between two automatic checkpoints in case of transparently checkpointing jobs. The maximum of the time requested by the user via and the time defined by the queue configuration is used as checkpoint interval. Since checkpoint files may be considerably large and thus writing them to the file system may become expensive, users and administrators are advised to choose sufficiently large time intervals. <code>min_cpu_interval</code> is of type time and the default is 5 minutes (which usually is suitable for test purposes only). The syntax is that of a <i>time_specifier</i> in</p>
<h3><code>processors</code></h3>
<p>A set of processors in case of a multiprocessor execution host can be defined to which the jobs executing in this queue are bound. The value type of this parameter is a range description like that of the <code>-pe</code> option of (e.g. 1-4,8,10) denoting the processor numbers for the processor group to be used. Obviously the interpretation of these values relies on operating system specifics and is thus performed inside running on the queue host. Therefore, the parsing of the parameter has to be provided by the execution daemon and the parameter is only passed through as a string. </p>
<p> Currently, support is only provided for multiprocessor machines running Solaris, SGI multiprocessor machines running IRIX 6.2 and Digital UNIX multiprocessor machines. In the case of Solaris the processor set must already exist, when this processors parameter is configured. So the processor set has to be created manually. In the case of Digital UNIX only one job per processor set is allowed to execute at the same time, i.e. <code>slots</code> (see above) should be set to 1 for this queue.</p>
<h3><code>qtype</code></h3>
<p>The type of queue. Currently <i>batch, interactive</i> or a combination in a comma separated list or <i>NONE.</i> </p>
<p> The formerly supported types parallel and checkpointing are not allowed anymore. A queue instance is implicitly of type parallel/checkpointing if there is a parallel environment or a checkpointing interface specified for this queue instance in <code>pe_list</code>/<code>ckpt_list</code>. Formerly possible settings e.g. </p>
<pre>qtype PARALLEL</pre>
<p>could be transferred into </p>
<pre>qtype NONE
pe_list pe_name</pre>
<p>(type string; default: batch interactive).</p>
<h3><code>pe_list</code></h3>
<p>The list of administrator-defined parallel environment (see names to be associated with the queue. The default is <i>NONE.</i></p>
<h3><code>ckpt_list</code></h3>
<p>The list of administrator-defined checkpointing interface names (see <i>ckpt_name</i> in to be associated with the queue. The default is <i>NONE.</i></p>
<h3><code>rerun</code></h3>
<p>Defines a default behavior for jobs which are aborted by system crashes or manual &quot;violent&quot; (via shutdown of the complete Grid Engine system (including the of the jobs and their process hierarchy) on the queue host. As soon as is restarted and detects that a job has been aborted for such reasons it can be restarted if the jobs are restartable. A job may not be restartable, for example, if it updates databases (first reads then writes to the same record of a database/file) because the abortion of the job may have left the database in an inconsistent state. If the owner of a job wants to overrule the default behavior for the jobs in the queue the <code>-r</code> option of can be used. </p>
<p> The type of this parameter is boolean, thus either TRUE or FALSE can be specified. The default is FALSE, i.e. do not restart jobs automatically.</p>
<h3><code>slots</code></h3>
<p>The maximum number of concurrently executing jobs allowed in the queue. Type is number, valid values are 0 to 9999999.</p>
<h3><code>tmpdir</code></h3>
<p>The <code>tmpdir</code> parameter specifies the absolute path to the base of the temporary directory filesystem. When launches a job, it creates a uniquely-named directory in this filesystem for the purpose of holding scratch files during job execution. At job completion, this directory and its contents are removed automatically. The environment variables TMPDIR and TMP are set to the path of each jobs scratch directory (type string; default: /tmp).</p>
<h3><code>shell</code></h3>
<p>If either <i>posix_compliant</i> or <i>script_from_stdin</i> is specified as the <code>shell_start_mode</code> parameter in the <code>shell</code> parameter specifies the executable path of the command interpreter (e.g. or to be used to process the job scripts executed in the queue. The definition of <code>shell</code> can be overruled by the job owner via the <code>-S</code> option. </p>
<p> The type of the parameter is string. The default is /bin/csh.</p>
<h3><code>shell_start_mode</code></h3>
<p>This parameter defines the mechanisms which are used to actually invoke the job scripts on the execution hosts. The following values are recognized:</p>
<dl>
<dt><i>unix_behavior</i></p>
<dd>If a user starts a job shell script under UNIX interactively by invoking it just with the script name the operating system&#8217;s executable loader uses the information provided in a comment such as `#!/bin/csh&#8217; in the first line of the script to detect which command interpreter to start to interpret the script. This mechanism is used by Grid Engine when starting jobs if <i>unix_behavior</i> is defined as <code>shell_start_mode</code>.</p>
<dt><i>posix_compliant</i></p>
<dd>POSIX does not consider first script line comments such a `#!/bin/csh&#8217; as being significant. The POSIX standard for batch queuing systems (P1003.2d) therefore requires a compliant queuing system to ignore such lines but to use user specified or configured default command interpreters instead. Thus, if <code>shell_start_mode</code> is set to <i>posix_compliant</i> Grid Engine will either use the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see above).</p>
<dt><i>script_from_stdin</i></p>
<dd>Setting the <code>shell_start_mode</code> parameter either to <i>posix_compliant</i> or <i>unix_behavior</i> requires you to set the umask in use for such that every user has read access to the active_jobs directory in the spool directory of the corresponding execution daemon. In case you have <code>prolog</code> and <code>epilog</code> scripts configured, they also need to be readable by any user who may execute jobs.<br />
 If this violates your site&#8217;s security policies you may want to set <code>shell_start_mode</code> to <i>script_from_stdin</i>. This will force Grid Engine to open the job script as well as the epilogue and prologue scripts for reading into STDIN as root (if was started as root) before changing to the job owner&#8217;s user account. The script is then fed into the STDIN stream of the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see above).<br />
 Thus setting <code>shell_start_mode</code> to <i>script_from_stdin</i> also implies <i>posix_compliant</i> behavior. <code>Note</code>, however, that feeding scripts into the STDIN stream of a command interpreter may cause trouble if commands like are invoked inside a job script as they also process the STDIN stream of the command interpreter. These problems can usually be resolved by redirecting the STDIN channel of those commands to come from /dev/null (e.g. rsh host date &lt; /dev/null). <code>Note also</code>, that any command-line options associated with the job are passed to the executing shell. The shell will only forward them to the job if they are not recognized as valid shell options.</dl>
<p> The default for <code>shell_start_mode</code> is <i>posix_compliant</i>. Note, though, that the <code>shell_start_mode</code> can only be used for batch jobs submitted by and can&#8217;t be used for interactive jobs submitted by</p>
<h3><code>prolog</code></h3>
<p>The executable path of a shell script that is started before execution of Grid Engine jobs with the same environment setting as that for the Grid Engine jobs to be started afterwards. An optional prefix &quot;user@&quot; specifies the user under which this procedure is to be started. The procedures standard output and the error output stream are written to the same file used also for the standard output and error output of each job. This procedure is intended as a means for the Grid Engine administrator to automate the execution of general site specific tasks like the preparation of temporary file systems with the need for the same context information as the job. This queue configuration entry overwrites cluster global or execution host specific <code>prolog</code> definitions (see </p>
<p> The default for <code>prolog</code> is the special value NONE, which prevents from execution of a prologue script. The special variables for constituting a command line are the same like in <code>prolog</code> definitions of the cluster configuration (see </p>
<p> Exit codes for the prolog attribute can be interpreted based on the following exit values:</p>
<dl>
<dd>0: Success<br />
 99: Reschedule job<br />
 100: Put job in error state<br />
 Anything else: Put queue in error state</dl>
<h3><code>epilog</code></h3>
<p>The executable path of a shell script that is started after execution of Grid Engine jobs with the same environment setting as that for the Grid Engine jobs that has just completed. An optional prefix &quot;user@&quot; specifies the user under which this procedure is to be started. The procedures standard output and the error output stream are written to the same file used also for the standard output and error output of each job. This procedure is intended as a means for the Grid Engine administrator to automate the execution of general site specific tasks like the cleaning up of temporary file systems with the need for the same context information as the job. This queue configuration entry overwrites cluster global or execution host specific <code>epilog</code> definitions (see </p>
<p> The default for <code>epilog</code> is the special value NONE, which prevents from execution of a epilogue script. The special variables for constituting a command line are the same like in <code>prolog</code> definitions of the cluster configuration (see </p>
<p> Exit codes for the epilog attribute can be interpreted based on the following exit values:</p>
<dl>
<dd>0: Success<br />
 99: Reschedule job<br />
 100: Put job in error state<br />
 Anything else: Put queue in error state</dl>
<h3><code>starter_method</code></h3>
<p>The specified executable path will be used as a job starter facility responsible for starting batch jobs. The executable path will be executed instead of the configured shell to start the job. The job arguments will be passed as arguments to the job starter. The following environment variables are used to pass information to the job starter concerning the shell environment which was configured or requested to start the job. </p>
<dl>
<dt><i>SGE_STARTER_SHELL_PATH</i></p>
<dd>The name of the requested shell to start the job</p>
<dt><i>SGE_STARTER_SHELL_START_MODE</i></p>
<dd>The configured <code>shell_start_mode</code></p>
<dt><i>SGE_STARTER_USE_LOGIN_SHELL</i></p>
<dd>Set to &quot;true&quot; if the shell is supposed to be used as a login shell (see <code>login_shells</code> in</dl>
<p> The starter_method will not be invoked for qsh, qlogin or qrsh acting as rlogin.</p>
<h3><code>suspend_method</code></h3>
<h3><code>resume_method</code></h3>
<h3><code>terminate_method</code></h3>
<p>These parameters can be used for overwriting the default method used by Grid Engine for suspension, release of a suspension and for termination of a job. Per default, the signals SIGSTOP, SIGCONT and SIGKILL are delivered to the job to perform these actions. However, for some applications this is not appropriate. </p>
<p> If no executable path is given, Grid Engine takes the specified parameter entries as the signal to be delivered instead of the default signal. A signal must be either a positive number or a signal name with <code>&quot;SIG&quot;</code> as prefix and the signal name as printed by <i>kill -l</i> (e.g. SIGTERM). </p>
<p> If an executable path is given (it must be an <i>absolute path</i> starting with a &quot;/&quot;) then this command together with its arguments is started by Grid Engine to perform the appropriate action. The following special variables are expanded at runtime and can be used (besides any other strings which have to be interpreted by the procedures) to constitute a command line: </p>
<dl>
<dt><i>$host</i></p>
<dd>The name of the host on which the procedure is started.</p>
<dt><i>$job_owner</i></p>
<dd>The user name of the job owner.</p>
<dt><i>$job_id</i></p>
<dd>Grid Engine&#8217;s unique job identification number.</p>
<dt><i>$job_name</i></p>
<dd>The name of the job.</p>
<dt><i>$queue</i></p>
<dd>The name of the queue.</p>
<dt><i>$job_pid</i></p>
<dd>The pid of the job. </p>
</dl>
<h3><code>notify</code></h3>
<p>The time waited between delivery of SIGUSR1/SIGUSR2 notification signals and suspend/kill signals if job was submitted with the <i>-notify</i> option.</p>
<h3><code>owner_list</code></h3>
<p>The <code>owner_list</code> enlists comma separated the user names (see <i>user_name</i> in of those users who are authorized to disable and suspend this queue through (Grid Engine operators and managers can do this by default). It is customary to set this field for queues on interactive workstations where the computing resources are shared between interactive sessions and Grid Engine jobs, allowing the workstation owner to have priority access. (default: NONE).</p>
<h3><code>user_lists</code></h3>
<p>The <code>user_lists</code> parameter contains a comma separated list of Grid Engine user access list names as described in Each user contained in at least one of the enlisted access lists has access to the queue. If the <code>user_lists</code> parameter is set to NONE (the default) any user has access being not explicitly excluded via the <code>xuser_lists</code> parameter described below. If a user is contained both in an access list enlisted in <code>xuser_lists</code> and <code>user_lists</code> the user is denied access to the queue.</p>
<h3><code>xuser_lists</code></h3>
<p>The <code>xuser_lists</code> parameter contains a comma separated list of Grid Engine user access list names as described in Each user contained in at least one of the enlisted access lists is not allowed to access the queue. If the <code>xuser_lists</code> parameter is set to NONE (the default) any user has access. If a user is contained both in an access list enlisted in <code>xuser_lists</code> and <code>user_lists</code> the user is denied access to the queue.</p>
<h3><code>projects</code></h3>
<p>The <code>projects</code> parameter contains a comma separated list of Grid Engine projects (see that have access to the queue. Any project not in this list are denied access to the queue. If set to NONE (the default), any project has access that is not specifically excluded via the <code>xprojects</code> parameter described below. If a project is in both the <code>projects</code> and <code>xprojects</code> parameters, the project is denied access to the queue.</p>
<h3><code>xprojects</code></h3>
<p>The <code>xprojects</code> parameter contains a comma separated list of Grid Engine projects (see that are denied access to the queue. If set to NONE (the default), no projects are denied access other than those denied access based on the <code>projects</code> parameter described above. If a project is in both the <code>projects</code> and <code>xprojects</code> parameters, the project is denied access to the queue.</p>
<h3><code>subordinate_list</code></h3>
<p>A list of Grid Engine queue names as defined for <i>queue_name</i> in Subordinate relationships are in effect only between queue instances residing at the same host. The relationship does not apply and is ignored when jobs are running in queue instances on other hosts. Queue instances residing on the same host will be suspended when a specified count of jobs is running in this queue instance. The list specification is the same as that of the <code>load_thresholds</code> parameter above, e.g. low_pri_q=5,small_q. The numbers denote the job slots of the queue that have to be filled in the superordinated queue to trigger the suspension of the subordinated queue. If no value is assigned a suspension is triggered if all slots of the queue are filled. </p>
<p> On nodes which host more than one queue, you might wish to accord better service to certain classes of jobs (e.g., queues that are dedicated to parallel processing might need priority over low priority production queues; default: NONE).</p>
<h3><code>complex_values</code></h3>
<p><code>complex_values</code> defines quotas for resource attributes managed via this queue. The syntax is the same as for <code>load_thresholds</code> (see above). The quotas are related to the resource consumption of all jobs in a queue in the case of consumable resources (see for details on consumable resources) or they are interpreted on a per queue slot (see <code>slots</code> above) basis in the case of non-consumable resources. Consumable resource attributes are commonly used to manage free memory, free disk space or available floating software licenses while non-consumable attributes usually define distinctive characteristics like type of hardware installed. </p>
<p> For consumable resource attributes an available resource amount is determined by subtracting the current resource consumption of all running jobs in the queue from the quota in the <code>complex_values</code> list. Jobs can only be dispatched to a queue if no resource requests exceed any corresponding resource availability obtained by this scheme. The quota definition in the <code>complex_values</code> list is automatically replaced by the current load value reported for this attribute, if load is monitored for this resource and if the reported load value is more stringent than the quota. This effectively avoids oversubscription of resources. </p>
<p> <code>Note:</code> Load values replacing the quota specifications may have become more stringent because they have been scaled (see and/or load adjusted (see The <i>-F</i> option of and the load display in the queue control dialog (activated by clicking on a queue icon while the &quot;Shift&quot; key is pressed) provide detailed information on the actual availability of consumable resources and on the origin of the values taken into account currently. </p>
<p> <code>Note also:</code> The resource consumption of running jobs (used for the availability calculation) as well as the resource requests of the jobs waiting to be dispatched either may be derived from explicit user requests during job submission (see the <i>-l</i> option to or from a &quot;default&quot; value configured for an attribute by the administrator (see The <i>-r</i> option to can be used for retrieving full detail on the actual resource requests of all jobs in the system. </p>
<p> For non-consumable resources Grid Engine simply compares the job&#8217;s attribute requests with the corresponding specification in <code>complex_values</code> taking the relation operator of the complex attribute definition into account (see If the result of the comparison is &quot;true&quot;, the queue is suitable for the job with respect to the particular attribute. For parallel jobs each queue slot to be occupied by a parallel task is meant to provide the same resource attribute value. </p>
<p> <code>Note:</code> Only numeric complex attributes can be defined as consumable resources and hence non-numeric attributes are always handled on a per queue slot basis. </p>
<p> The default value for this parameter is NONE, i.e. no administrator defined resource attribute quotas are associated with the queue.</p>
<h3><code>calendar</code></h3>
<p>specifies the <code>calendar</code> to be valid for this queue or contains NONE (the default). A calendar defines the availability of a queue depending on time of day, week and year. Please refer to for details on the Grid Engine calendar facility. </p>
<p> <code>Note:</code> Jobs can request queues with a certain calendar model via a &quot;<i>-l c=&lt;cal_name&gt;</i>&quot; option to</p>
<h3><code>initial_state</code></h3>
<p>defines an initial state for the queue either when adding the queue to the system for the first time or on start-up of the on the host on which the queue resides. Possible values are:</p>
<dl>
<dt>default</p>
<dd>The queue is enabled when adding the queue or is reset to the previous status when comes up (this corresponds to the behavior in earlier Grid Engine releases not supporting initial_state).</p>
<dt>enabled</p>
<dd>The queue is enabled in either case. This is equivalent to a manual and explicit &#8216;<i>qmod -e</i>&#8216; command (see</p>
<dt>disabled</p>
<dd>The queue is disable in either case. This is equivalent to a manual and explicit &#8216;<i>qmod -d</i>&#8216; command (see</dl>
<h2>Resource Limits</h2>
<p>The first two resource limit parameters, <code>s_rt</code> and <code>h_rt</code>, are implemented by Grid Engine. They define the &quot;real time&quot; or also called &quot;elapsed&quot; or &quot;wall clock&quot; time having passed since the start of the job. If <code>h_rt</code> is exceeded by a job running in the queue, it is aborted via the SIGKILL signal (see If <code>s_rt</code> is exceeded, the job is first &quot;warned&quot; via the SIGUSR1 signal (which can be caught by the job) and finally aborted after the notification time defined in the queue configuration parameter <code>notify</code> (see above) has passed. In cases when <code>s_rt</code> is used in combination with job notification it might be necessary to configure a signal other than SIGUSR1 using the NOTIFY_KILL and NOTIFY_SUSP execd_params (see so that the jobs&#8217; signal-catching mechanism can &quot;differ&quot; the cases and react accordingly. </p>
<p> The resource limit parameters <code>s_cpu</code> and <code>h_cpu</code> are implemented by Grid Engine as a job limit. They impose a limit on the amount of combined CPU time consumed by all the processes in the job. If <code>h_cpu</code> is exceeded by a job running in the queue, it is aborted via a SIGKILL signal (see If <code>s_cpu</code> is exceeded, the job is sent a SIGXCPU signal which can be caught by the job. If you wish to allow a job to be &quot;warned&quot; so it can exit gracefully before it is killed then you should set the <code>s_cpu</code> limit to a lower value than <code>h_cpu</code>. For parallel processes, the limit is applied per slot which means that the limit is multiplied by the number of slots being used by the job before being applied. </p>
<p> The resource limit parameters <code>s_vmem</code> and <code>h_vmem</code> are implemented by Grid Engine as a job limit. They impose a limit on the amount of combined virtual memory consumed by all the processes in the job. If <code>h_vmem</code> is exceeded by a job running in the queue, it is aborted via a SIGKILL signal (see <a href="/docs/linux/man/1-kill/">kill</a>(1)). If <code>s_vmem</code> is exceeded, the job is sent a SIGXCPU signal which can be caught by the job. If you wish to allow a job to be &quot;warned&quot; so it can exit gracefully before it is killed then you should set the <code>s_vmem</code> limit to a lower value than <code>h_vmem</code>. For parallel processes, the limit is applied per slot which means that the limit is multiplied by the number of slots being used by the job before being applied. </p>
<p> The remaining parameters in the queue configuration template specify per job soft and hard resource limits as implemented by the system call. See this manual page on your system for more information. By default, each limit field is set to infinity (which means RLIM_INFINITY as described in the manual page). The value type for the CPU-time limits <code>s_cpu</code> and <code>h_cpu</code> is time. The value type for the other limits is memory. <code>Note:</code> Not all systems support </p>
<p> <code>Note also:</code> s_vmem and h_vmem (virtual memory) are only available on systems supporting RLIMIT_VMEM (see on your operating system). </p>
<p> The UNICOS operating system supplied by SGI/Cray does not support the system call, using their own resource limit-setting system call instead. For UNICOS systems only, the following meanings apply:</p>
<dl>
<dt>s_cpu</p>
<dd>The per-process CPU time limit in seconds.</p>
<dt>s_core</p>
<dd>The per-process maximum core file size in bytes.</p>
<dt>s_data</p>
<dd>The per-process maximum memory limit in bytes.</p>
<dt>s_vmem</p>
<dd>The same as s_data (if both are set the minimum is used).</p>
<dt>h_cpu</p>
<dd>The per-job CPU time limit in seconds.</p>
<dt>h_data</p>
<dd>The per-job maximum memory limit in bytes.</p>
<dt>h_vmem</p>
<dd>The same as h_data (if both are set the minimum is used).</p>
<dt>h_fsize</p>
<dd>The total number of disk blocks that this job can create.</dl>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
