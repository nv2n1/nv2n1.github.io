---
title: "sge_conf(5)"
name: "sge_conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_conf/"
description: "xxqs_name_sxx_conf – xxQS_NAMExx configuration files"
---

<p>xxqs_name_sxx_conf &#8211; xxQS_NAMExx configuration files</p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_conf</i> defines the global and local xxQS_NAMExx configurations and can be shown/modified by using the -sconf/-mconf options. Only root or the cluster administrator may modify <i>xxqs_name_sxx_conf.</i> </p>
<p> At its initial start-up, checks to see if a valid xxQS_NAMExx configuration is available at a well known location in the xxQS_NAMExx internal directory hierarchy. If so, it loads that configuration information and proceeds. If not, writes a generic configuration containing default values to that same location. The xxQS_NAMExx execution daemons upon start-up retrieve their configuration from </p>
<p> The actual configuration for both and is a superposition of a <i>global</i> configuration and a <i>local</i> configuration pertinent for the host on which a master or execution daemon resides. If a local configuration is available, its entries overwrite the corresponding entries of the global configuration. <code>Note:</code> The local configuration does not have to contain all valid configuration entries, but only those which need to be modified against the global entries. </p>
<p> Note: xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>The paragraphs that follow provide brief descriptions of the individual parameters that compose the global and local configurations for a xxQS_NAMExx cluster:</p>
<h3><code>execd_spool_dir</code></h3>
<p>The execution daemon spool directory path. Again, a feasible spool directory requires read/write access permission for root. The entry in the global configuration for this parameter can be overwritten by execution host local configurations, i.e. each may have a private spool directory with a different path, in which case it needs to provide read/write permission for the root account of the corresponding execution host only. </p>
<p> Under <code>execd_spool_dir</code> a directory named corresponding to the unqualified hostname of the execution host is opened and contains all information spooled to disk. Thus, it is possible for the <code>execd_spool_dir</code>s of all execution hosts to physically reference the same directory path (the root access restrictions mentioned above need to be met, however). </p>
<p> Changing the global <code>execd_spool_dir</code> parameter set at installation time is not supported in a running system. If the change should still be done it is required to restart all affected execution daemons. Please make sure running jobs have finished before doing so, otherwise running jobs will be lost. </p>
<p> The default location for the execution daemon spool directory is $xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/spool. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>mailer</code></h3>
<p><code>mailer</code> is the absolute pathname to the electronic mail delivery agent on your system. An optional prefix &quot;user@&quot; specifies the user under which this procedure is to be started; the default is root. The mailer must accept the following syntax: </p>
<dl>
<dd>mailer -s <i>subject-of-mail-message</i> <i>recipient</i></dl>
<p> Each may use a private mail agent. Changing <code>mailer</code> will take immediate effect. </p>
<p> The default for <code>mailer</code> depends on the operating system of the host on which the xxQS_NAMExx master installation was run. Common values are /bin/mail or /usr/bin/Mail. Note that since the mail is sent by compute hosts, not the master, it may be necessary to take steps to route it appropriately, e.g. by using a cluster head node as a &quot;smart host&quot; for the private network. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>xterm</code></h3>
<p><code>xterm</code> is the absolute pathname to the X Window System terminal emulator, <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1). </p>
<p> Changing <code>xterm</code> will take immediate effect. </p>
<p> The default for <code>xterm</code> is system-dependent. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>load_sensor</code></h3>
<p>A comma-separated list of executable shell script paths or programs to be started by and to be used in order to retrieve site-configurable load information (e.g. free space on a certain disk partition). </p>
<p> Each may use a set of private <code>load_sensor</code> programs or scripts. Changing <code>load_sensor</code> will take effect after on load report interval (see <code>load_report_time</code>), or two if <code>DEMAND_LS</code> is 0 in <code>execd_params</code>. A load sensor will be restarted automatically if the file modification time of the load sensor executable changes. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration. </p>
<p> In addition to the load sensors configured via <code>load_sensor</code>, searches for an executable file named <i>qloadsensor</i> in the execution host&#8217;s xxQS_NAMExx binary directory path. If such a file is found, it is treated like the configurable load sensors defined in <code>load_sensor</code>. This facility is intended for pre-installing a default load sensor. </p>
<p> See for information on writing load sensors.</p>
<h3><code>prolog</code></h3>
<p>The path of an executable, with optional arguments, that is started before execution of xxQS_NAMExx jobs with the same environment setting as that for the xxQS_NAMExx jobs to be started afterwards (see The prolog command is started directly, not in a shell. An optional prefix &quot;user@&quot; specifies the user under which this procedure is to be started. In that case see the SECURITY section below concerning security issues running as a privileged user. The procedure&#8217;s standard output and the error output stream are written to the same file as used for the standard output and error output of each job. </p>
<p> This procedure is intended as a means for the xxQS_NAMExx administrator to automate the execution of general site-specific tasks, like the preparation of temporary file systems, with a need for the same context information as the job. For a parallel job, only a single instance of the prolog is run, on the master node. Each may use a private prolog. Correspondingly, the global or execution host local configuration can be overwritten by the queue configuration (see Changing <code>prolog</code> will take immediate effect. </p>
<p> The default for <code>prolog</code> is the special value NONE, which prevents execution of a prolog. </p>
<p> The following special variables, expanded at runtime, can be used (besides any other strings which have to be interpreted by the procedure) to compose a command line:</p>
<dl>
<dt><i>$host</i></p>
<dd>The name of the host on which the prolog or epilog procedures are started.</p>
<dt><i>$ja_task_id</i></p>
<dd>The array job task index (0 if not an array job).</p>
<dt><i>$job_owner</i></p>
<dd>The user name of the job owner.</p>
<dt><i>$job_id</i></p>
<dd>xxQS_NAMExx&#8217;s unique job identification number.</p>
<dt><i>$job_name</i></p>
<dd>The name of the job.</p>
<dt><i>$queue</i></p>
<dd>The cluster queue name of the master queue instance, i.e. the cluster queue in which the prolog and epilog procedures are started.</p>
<dt><i>$stdin_path</i></p>
<dd>The pathname of the stdin file. This is always /dev/null for prolog, pe_start, pe_stop and epilog. It is the pathname of the stdin file for the job in the job script. When delegated file staging is enabled, this path is set to $fs_stdin_tmp_path. When delegated file staging is not enabled, it is the stdin pathname given via DRMAA or qsub.</p>
<dt><i>$stdout_path</i></p>
<dd>
<dt><i>$stderr_path</i></p>
<dd>The pathname of the stdout/stderr file. This always points to the output/error file. When delegated file staging is enabled, this path is set to $fs_stdout_tmp_path/$fs_stderr_tmp_path. When delegated file staging is not enabled, it is the stdout/stderr pathname given via DRMAA or qsub.</p>
<dt><i>$merge_stderr</i></p>
<dd>If this flag is 1, stdout and stderr are merged in one file, the stdout file. Otherwise (the default), no merging is done. Merging of stderr and stdout can be requested via the DRMAA job template attribute &#8216;drmaa_join_files&#8217; (see or the qsub parameter &#8216;-j y&#8217; (see</p>
<dt><i>$fs_stdin_host</i></p>
<dd>When delegated file staging is requested for the stdin file, this is the name of the host where the stdin file has to be copied from before the job is started.</p>
<dt><i>$fs_stdout_host</i></p>
<dd>
<dt><i>$fs_stderr_host</i></p>
<dd>When delegated file staging is requested for the stdout/stderr file, this is the name of the host where the stdout/stderr file has to be copied to after the job has run.</p>
<dt><i>$fs_stdin_path</i></p>
<dd>When delegated file staging is requested for the stdin file, this is the pathname of the stdin file on the host $fs_stdin_host.</p>
<dt><i>$fs_stdout_path</i></p>
<dd>
<dt><i>$fs_stderr_path</i></p>
<dd>When delegated file staging is requested for the stdout/stderr file, this is the pathname of the stdout/stderr file on the host $fs_stdout_host/$fs_stderr_host.</p>
<dt><i>$fs_stdin_tmp_path</i></p>
<dd>When delegated file staging is requested for the stdin file, this is the destination pathname of the stdin file on the execution host. The prolog must copy the stdin file from $fs_stdin_host:$fs_stdin_path to localhost:$fs_stdin_tmp_path to establish delegated file staging of the stdin file.</p>
<dt><i>$fs_stdout_tmp_path</i></p>
<dd>
<dt><i>$fs_stderr_tmp_path</i></p>
<dd>When delegated file staging is requested for the stdout/stderr file, this is the source pathname of the stdout/stderr file on the execution host. The epilog must copy the stdout file from localhost:$fs_stdout_tmp_path to $fs_stdout_host:$fs_stdout_path (the stderr file from localhost:$fs_stderr_tmp_path to $fs_stderr_host:$fs_stderr_path) to establish delegated file staging of the stdout/stderr file.</p>
<dt><i>$fs_stdin_file_staging</i></p>
<dd>
<dt><i>$fs_stdout_file_staging</i></p>
<dd>
<dt><i>$fs_stderr_file_staging</i></p>
<dd>When delegated file staging is requested for the stdin/stdout/stderr file, the flag is set to &quot;1&quot;, otherwise it is set to &quot;0&quot; (see in <code>delegated_file_staging</code> how to enable delegated file staging). These three flags correspond to the DRMAA job template attribute &#8216;drmaa_transfer_files&#8217; (see</dl>
<p> If the prolog is written in shell script, the usual care must be exercised, e.g. when expanding such values from the command line or the environment which are user-supplied. In particular, note that the job name could be of the form &quot;; evil doings;&quot;. Also, use absolute path names for commands if inheriting the user&#8217;s environment. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration. </p>
<p> See for the significance of exit codes returned by the prolog.</p>
<h3><code>epilog</code></h3>
<p>The path of an executable, with optional argument, that is started after execution of xxQS_NAMExx jobs with the same environment setting as that for the xxQS_NAMExx job that has just completed (see with the addition of the variable named <code>SGE_JOBEXIT_STAT</code> which holds the exit status of the job. The epilog command is started directly, not in a shell. An optional prefix &quot;user@&quot; specifies the user under which this procedure is to be started. In that case see the SECURITY section below concerning security issues running as a privileged user. The procedure&#8217;s standard output and the error output stream are written to the same file used for the standard output and error output of each job. </p>
<p> The same special variables can be used to compose a command line as for the prolog. </p>
<p> This procedure is intended as a means for the xxQS_NAMExx administrator to automate the execution of general site-specific tasks, like the cleaning up of temporary file systems with the need for the same context information as the job. For a parallel job, only a single instance of the epilog is run, on the master node. Each may use a private epilog. Correspondingly, the global or execution host local configurations can be overwritten by the queue configuration (see Changing <code>epilog</code> will take immediate effect. </p>
<p> The default for <code>epilog</code> is the special value NONE, which prevents execution of an epilog. The same special variables as for <code>prolog</code> can be used to constitute a command line. </p>
<p> The same considerations (above) apply as for a prolog when an epilog is written in shell script. </p>
<p> See for the significance of exit codes returned by the epilog.</p>
<h3><code>shell_start_mode</code></h3>
<p><code>Note:</code> Deprecated, may be removed in future release.<br />
 This parameter defines the mechanisms which are used to actually invoke the job scripts on the execution hosts. The following values are recognized:</p>
<dl>
<dt><i>unix_behavior</i></p>
<dd>If a user starts a job shell script under UNIX interactively by invoking it just with the script name the operating system&#8217;s executable loader uses the information provided in a comment such as `#!/bin/csh&#8217; in the first line of the script to detect which command interpreter to start to interpret the script. This mechanism is used by xxQS_NAMExx when starting jobs if <i>unix_behavior</i> is defined as <code>shell_start_mode</code>.</p>
<dt><i>posix_compliant</i></p>
<dd>POSIX does not consider first script line comments such a `#!/bin/csh&#8217; as significant. The POSIX standard for batch queueing systems (P1003.2d) therefore requires a compliant queueing system to ignore such lines, but to use user-specified or configured default command interpreters instead. Thus, if <code>shell_start_mode</code> is set to <i>posix_compliant</i> xxQS_NAMExx will either use the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see for details).</p>
<dt><i>script_from_stdin</i></p>
<dd>Setting the <code>shell_start_mode</code> parameter either to <i>posix_compliant</i> or <i>unix_behavior</i> requires you to set the umask in use for such that every user has read access to the active_jobs directory in the spool directory of the corresponding execution daemon. In case you have <code>prolog</code> and <code>epilog</code> scripts configured, they also need to be readable by any user who may execute jobs.<br />
 If this violates your site&#8217;s security policies you may want to set <code>shell_start_mode</code> to <i>script_from_stdin</i>. This will force xxQS_NAMExx to open the job script as well as the epilog and prolog scripts for reading into STDIN as root (if was started as root) before changing to the job owner&#8217;s user account. The script is then fed into the STDIN stream of the command interpreter indicated by the <code>-S</code> option of the command or the <code>shell</code> parameter of the queue to be used (see for details).<br />
 Thus setting <code>shell_start_mode</code> to <i>script_from_stdin</i> also implies <i>posix_compliant</i> behavior. <code>Note</code>, however, that feeding scripts into the STDIN stream of a command interpreter may cause trouble if commands like <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1) are invoked inside a job script as they also process the STDIN stream of the command interpreter. These problems can usually be resolved by redirecting the STDIN channel of those commands to come from /dev/null (e.g. rsh host date &lt; /dev/null). <code>Note also</code>, that any command-line options associated with the job are passed to the executing shell. The shell will only forward them to the job if they are not recognized as valid shell options.</dl>
<p> Changes to <code>shell_start_mode</code> will take immediate effect. The default for <code>shell_start_mode</code> is <i>posix_compliant</i>. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>login_shells</code></h3>
<p>UNIX command interpreters like the Bourne-Shell (see <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1)) or the C-Shell (see <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1)) can be used by xxQS_NAMExx to start job scripts. The command interpreters can either be started as login-shells (i.e. all system and user default resource files like .login or .profile will be executed when the command interpreter is started, and the environment for the job will be set up as if the user has just logged in) or just for command execution (i.e. only shell-specific resource files like .cshrc will be executed and a minimal default environment is set up by xxQS_NAMExx &#8211; see The parameter <code>login_shells</code> contains a comma-separated list of the executable names of the command interpreters to be started as login shells. Shells in this list are only started as login shells if the parameter <code>shell_start_mode</code> (see above) is set to <i>posix_compliant</i>. </p>
<p> Changes to <code>login_shells</code> will take immediate effect. The default for <code>login_shells</code> is sh,bash,csh,tcsh,ksh. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>min_uid</code></h3>
<p><code>min_uid</code> places a lower bound on user IDs that may use the cluster. Users whose user ID (as returned by <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3)) is less than <code>min_uid</code> will not be allowed to run jobs on the cluster. </p>
<p> Changes to <code>min_uid</code> will take immediate effect. The default is 0 but, if CSP or MUNGE security is not in use, the installation script sets it to 100 to prevent unauthorized access by root or system accounts. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>min_gid</code></h3>
<p>This parameter sets the lower bound on group IDs that may use the cluster. Users whose default group ID (as returned by <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3)) is less than <code>min_gid</code> will not be allowed to run jobs on the cluster. </p>
<p> Changes to <code>min_gid</code> will take immediate effect. The default is 0 but, if CSP security is not in use, the installation script sets it to 100 to prevent unauthorized access by root or system accounts. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>user_lists </code></h3>
<p>The <code>user_lists</code> parameter contains a comma-separated list of user access lists as described in Each user contained in at least one of the access lists has access to the cluster. If the <code>user_lists</code> parameter is set to NONE (the default) any user has access if not explicitly excluded via the <code>xuser_lists</code> parameter described below. If a user is contained both in an access list <code>xuser_lists</code> and <code>user_lists</code>, the user is denied access to the cluster. </p>
<p> Changes to <code>user_lists</code> will take immediate effect. </p>
<p> This value is a global configuration parameter insofar as it restricts access to the whole cluster, but the execution host local configuration may define a value to restrict access to that host further.</p>
<h3><code>xuser_lists </code></h3>
<p>The <code>xuser_lists</code> parameter contains a comma-separated list of user access lists as described in Each user contained in at least one of the access lists is denied access to the cluster. If the <code>xuser_lists</code> parameter is set to NONE (the default) any user has access. If a user is contained both in an access list in <code>xuser_lists</code> and <code>user_lists</code> (see above) the user is denied access to the cluster. </p>
<p> Changes to <code>xuser_lists</code> will take immediate effect. </p>
<p> This value is a global configuration parameter insofar as it restricts access to the whole cluster, but the execution host local configuration may define a value to restrict access to that host further.</p>
<h3><code>administrator_mail</code></h3>
<p><code>administrator_mail</code> specifies a comma-separated list of the electronic mail address(es) of the cluster administrator(s) to whom internally-generated problem reports are sent. The mail address format depends on your electronic mail system and how it is configured; consult your system&#8217;s configuration guide for more information. </p>
<p> Changing <code>administrator_mail</code> takes immediate effect. The default for <code>administrator_mail</code> is an empty mail list. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>projects</code></h3>
<p>The <code>projects</code> list contains all projects which are granted access to xxQS_NAMExx. Users not belonging to one of these projects cannot submit jobs. If users belong to projects in the <code>projects</code> list and the <code>xprojects</code> list (see below), they also cannot submit jobs. </p>
<p> Changing <code>projects</code> takes immediate effect. The default for <code>projects</code> is none. </p>
<p> While globally-configured projects affect job submission, projects configured for queues or hosts affect job execution in the appropriate context.</p>
<h3><code>xprojects</code></h3>
<p>The <code>xprojects</code> list contains all projects that are denied access to xxQS_NAMExx. Users belonging to one of these projects cannot use xxQS_NAMExx. If users belong to projects in the <code>projects</code> list (see above) and the <code>xprojects</code> list, they also cannot use the system. </p>
<p> Changing <code>xprojects</code> takes immediate effect. The default for <code>xprojects</code> is none. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>load_report_time</code></h3>
<p>System load is reported periodically by the execution daemons to The parameter <code>load_report_time</code> defines the time interval between load reports. </p>
<p> Each may use a different load report time. Changing <code>load_report_time</code> will take immediate effect. </p>
<p> <code>Note:</code> Be careful when modifying <code>load_report_time</code>. Reporting load too frequently might block especially if the number of execution hosts is large. Moreover, since the system load typically increases and decreases smoothly, frequent load reports hardly offer any benefit. </p>
<p> The default for <code>load_report_time</code> is 40 seconds. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>reschedule_unknown</code></h3>
<p>Determines whether jobs on hosts in an unknown state are rescheduled, and thus sent to other hosts. Hosts are registered as unknown if cannot establish contact to the on those hosts (see <code>max_unheard</code>). Likely reasons are a breakdown of the host or a breakdown of the network connection in between, but also may not be executing on such hosts. </p>
<p> In any case, xxQS_NAMExx can reschedule jobs running on such hosts to another system. <code>reschedule_unknown</code> controls the time which xxQS_NAMExx will wait before jobs are rescheduled after a host became unknown. The time format specification is hh:mm:ss. If the special value 00:00:00 is set, then jobs will not be rescheduled from this host. </p>
<p> Rescheduling is only initiated for jobs which have activated the rerun flag (see the <code>-r y</code> option of and the <code>rerun</code> option of Parallel jobs are only rescheduled if the host on which their master task executes is in unknown state. The behavior of <code>reschedule_unknown</code> for parallel jobs and for jobs without the rerun flag set can be adjusted using the <code>qmaster_params</code> settings <code>ENABLE_RESCHEDULE_KILL</code> and <code>ENABLE_RESCHEDULE_SLAVE.</code> </p>
<p> Checkpointing jobs will only be rescheduled when the <code>when</code> option of the corresponding checkpointing environment contains an appropriate flag. (see Interactive jobs (see are not rescheduled. </p>
<p> The default for <code>reschedule_unknown</code> is 00:00:00 </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>max_unheard</code></h3>
<p>If could not contact, or was not contacted by, the execution daemon of a host for <code>max_unheard</code> seconds, all queues residing on that particular host are set to status unknown. at least, should be contacted by the execution daemons in order to get the load reports. Thus, <code>max_unheard</code> should be greater than the <code>load_report_time</code> (see above). </p>
<p> Changing <code>max_unheard</code> takes immediate effect. The default for <code>max_unheard</code> is 5 minutes. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>loglevel</code></h3>
<p>This parameter specifies the level of detail that xxQS_NAMExx components such as or use to produce informative, warning or error messages which are logged to the <i>messages</i> files in the master and execution daemon spool directories (see the description of the <code>execd_spool_dir</code> parameter above). The following message levels are available:</p>
<dl>
<dt><i>log_err</i></p>
<dd>All error events recognized are logged.</p>
<dt><i>log_warning</i></p>
<dd>All error events recognized, and all detected signs of potentially erroneous behavior, are logged.</p>
<dt><i>log_info</i></p>
<dd>All error events recognized, all detected signs of potentially erroneous behavior, and a variety of informative messages are logged.</dl>
<p> Changing <code>loglevel</code> will take immediate effect. </p>
<p> The default for <code>loglevel</code> is <i>log_warning</i>. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>max_aj_instances</code></h3>
<p>This parameter defines the maximum number of array tasks to be scheduled to run simultaneously per array job. An instance of an array task will be created within the master daemon when it gets a start order from the scheduler. The instance will be destroyed when the array task finishes. Thus the parameter provides control mainly over the memory consumption of array jobs in the master daemon. It is most useful for very large clusters and very large array jobs. The default for this parameter is 2000. The value 0 will deactivate this limit and will allow the scheduler to start as many array job tasks as suitable resources are available in the cluster. </p>
<p> Changing <code>max_aj_instances</code> will take immediate effect. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>max_aj_tasks</code></h3>
<p>This parameter defines the maximum number of array job tasks within an array job. will reject all array job submissions which request more than <code>max_aj_tasks</code> array job tasks. The default for this parameter is 75000. The value 0 will deactivate this limit. </p>
<p> Changing <code>max_aj_tasks</code> will take immediate effect. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>max_u_jobs</code></h3>
<p>The number of active (not finished) jobs which each xxQS_NAMExx user can have in the system simultaneously is controlled by this parameter. A value greater than 0 defines the limit. The default value 0 means &quot;unlimited&quot;. If the <code>max_u_jobs</code> limit is exceeded by a job submission then the submission command exits with exit status 25 and an appropriate error message. </p>
<p> Changing <code>max_u_jobs</code> will take immediate effect. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>max_jobs</code></h3>
<p>The number of active (not finished) jobs simultaneously allowed in xxQS_NAMExx is controlled by this parameter. A value greater than 0 defines the limit. The default value 0 means &quot;unlimited&quot;. If the <code>max_jobs</code> limit is exceeded by a job submission then the submission command exits with exit status 25 and an appropriate error message. </p>
<p> Changing <code>max_jobs</code> will take immediate effect. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>max_advance_reservations</code></h3>
<p>The number of active (not finished) Advance Reservations simultaneously allowed in xxQS_NAMExx is controlled by this parameter. A value greater than 0 defines the limit. The default value 0 means &quot;unlimited&quot;. If the <code>max_advance_reservations</code> limit is exceeded by an Advance Reservation request then the submission command exits with exit status 25 and an appropriate error message. </p>
<p> Changing <code>max_advance_reservations</code> will take immediate effect. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>enforce_project</code></h3>
<p>If set to <i>true</i>, users are required to request a project whenever submitting a job. See the <code>-P</code> option to for details. </p>
<p> Changing <code>enforce_project</code> will take immediate effect. The default for <code>enforce_project</code> is <i>false</i>. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>enforce_user</code></h3>
<p>If set to <i>true</i>, a must exist to allow for job submission. Jobs are rejected if no corresponding user exists. </p>
<p> If set to <i>auto</i>, a object for the submitting user will automatically be created during job submission, if one does not already exist. The <code>auto_user_oticket</code>, <code>auto_user_fshare</code>, <code>auto_user_default_project</code>, and <code>auto_user_delete_time</code> configuration parameters will be used as default attributes of the new object. </p>
<p> Changing <code>enforce_user</code> will take immediate effect. The default for <code>enforce_user</code> is <i>auto</i>. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>auto_user_oticket</code></h3>
<p>The number of override tickets to assign to automatically created objects. User objects are created automatically if the <code>enforce_user</code> attribute is set to <i>auto</i>. </p>
<p> Changing <code>auto_user_oticket</code> will affect any newly created user objects, but will not change user objects created in the past. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>auto_user_fshare</code></h3>
<p>The number of functional shares to assign to automatically created objects. User objects are created automatically if the <code>enforce_user</code> attribute is set to <i>auto</i>. </p>
<p> Changing <code>auto_user_fshare</code> will affect any newly created user objects, but will not change user objects created in the past. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>auto_user_default_project</code></h3>
<p>The default project to assign to automatically created objects. User objects are created automatically if the <code>enforce_user</code> attribute is set to <i>auto</i>. </p>
<p> Changing <code>auto_user_default_project</code> will affect any newly created user objects, but will not change user objects created in the past. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>auto_user_delete_time</code></h3>
<p>The number of seconds of inactivity after which automatically created objects will be deleted. User objects are created automatically if the <code>enforce_user</code> attribute is set to <i>auto</i>. If the user has no active or pending jobs for the specified amount of time, the object will automatically be deleted. A value of 0 can be used to indicate that the automatically created user object is permanent and should not be automatically deleted. </p>
<p> Changing <code>auto_user_delete_time</code> will affect the deletion time for all users with active jobs. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>set_token_cmd</code></h3>
<p><code>NB. If the qmaster spool area is world-readable for non-admin users, you must take steps to encrypt the credentials, since they are stored there after job submission.</code><br />
 <code>Set_token_cmd</code> points to a command which sets and extends AFS tokens for xxQS_NAMExx jobs. It is run by It expects two command line parameters: </p>
<dl>
<dd>
<pre><i>set_token_cmd</i> <i>user</i> <i>token_extend_after_seconds</i></pre>
</dl>
<p> It reads the token from STDIN, extends its expiration time, and re-sets the token. As a shell script this command will call the programs: </p>
<dl>
<dd>
<pre>- SetToken
- forge</pre>
</dl>
<p> which are provided by your distributor as source code. The script looks as follows: </p>
<dl>
<dd>
<pre>--------------------------------
#!/bin/sh
# set_token_cmd
forge -u $1 -t $2 | SetToken
--------------------------------</pre>
</dl>
<p> Since it is necessary for <i>forge</i> to read the secret AFS server key, a site might wish to replace the <code>set_token_cmd</code> script by a command, which connects to a custom daemon at the AFS server. The token must be forged at the AFS server and returned to the local machine, where <i>SetToken</i> is executed. </p>
<p> Changing <code>set_token_cmd</code> will take immediate effect. The default for <code>set_token_cmd</code> is none. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>pag_cmd</code></h3>
<p>The path to your <i>pagsh</i> is specified via this parameter. The process and the job run in a <i>pagsh</i>. Please ask your AFS administrator for details. </p>
<p> Changing <code>pag_cmd</code> will take immediate effect. The default for <code>pag_cmd</code> is none. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>token_extend_time</code></h3>
<p>The <code>token_extend_time</code> is the time period for which AFS tokens are periodically extended. xxQS_NAMExx will call the token extension 30 minutes before the tokens expire until jobs have finished and the corresponding tokens are no longer required. </p>
<p> Changing <code>token_extend_time</code> will take immediate effect. The default for <code>token_extend_time</code> is 24:0:0, i.e. 24 hours. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>shepherd_cmd</code></h3>
<p>Alternative path to the <code>shepherd_cmd</code> binary. Typically used to call the shepherd binary by a wrapper script or command. If used in production, this must take care to handle signals the way the shepherd would or, for instance, jobs will not be killed correctly. </p>
<p> Changing <code>shepherd_cmd</code> will take immediate effect. The default for <code>shepherd_cmd</code> is none. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>gid_range</code></h3>
<p>The <code>gid_range</code> is a comma-separated list of range expressions of the form <i>m</i><code>&#8211;</code><i>n</i>, where <i>m</i> and <i>n</i> are integer numbers greater than 99, and <i>m</i> is an abbreviation for <i>m</i><code>&#8211;</code><i>m</i>. These numbers are used in to identify processes belonging to the same job. </p>
<p> Each may use a separate set of group ids for this purpose. All numbers in the group id range have to be unused supplementary group ids on the system, where the is started. </p>
<p> Changing <code>gid_range</code> will take immediate effect. There is no default for <code>gid_range</code>. The administrator will have to assign a value for <code>gid_range</code> during installation of xxQS_NAMExx. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>qmaster_params</code></h3>
<p>A list of additional parameters can be passed to the xxQS_NAMExx qmaster. The following values are recognized:</p>
<dl>
<dt><i>ENABLE_ENFORCE_MASTER_LIMIT</i></p>
<dd>If this parameter is set then the <code>s_rt</code>, <code>h_rt</code> limits of a running job are tested and acted on by the when the where the job was run is in an unknown state. </p>
<p> After the <code>s_rt</code> or <code>h_rt</code> limit of a job is expired, the master daemon will wait additional time defined by <code>DURATION_OFFSET</code> (see If the execution daemon still cannot be contacted when this additional time is elapsed, then the master daemon will force the deletion of the job (see <code>-f</code> of </p>
<p> For jobs which will be deleted that way, an accounting record will be created. For usage, the record will contain the last reported online value when the execution daemon could contact qmaster. The <code>failed</code> state in the record will be set to 37 to indicate that the job was terminated by a limit enforced by the master daemon. </p>
<p> After the restart of the limit enforcement will be triggered after twice the biggest <code>load_report_interval</code> interval defined in has elapsed. This will give the execution daemons enough time to re-register with the master daemon.</p>
<dt><i>ENABLE_FORCED_QDEL_IF_UNKNOWN</i></p>
<dd>If this parameter is set then a deletion request for a job is automatically interpreted as a forced deletion request (see <code>-f</code> of if the host where the job is running is in an unknown state.</p>
<dt><i>ENABLE_FORCED_QDEL</i></p>
<dd>If this parameter is set, non-administrative users can force deletion of their own jobs via the <i>-f</i> option of Without this parameter, forced deletion of jobs is only allowed by the xxQS_NAMExx manager or operator. </p>
<p> <code>Note:</code> Forced deletion for jobs is executed differently, depending on whether users are xxQS_NAMExx administrators or not. In the case of administrative users, the jobs are removed from the internal database of xxQS_NAMExx immediately. For regular users, the equivalent of a normal is executed first, and deletion is forced only if the normal cancellation was unsuccessful.</p>
<dt><i>FORBID_RESCHEDULE</i></p>
<dd>If this parameter is set, re-queueing of jobs cannot be initiated by the job script which is under control of the user. Without this parameter, jobs returning the value 99 are rescheduled. This can be used to cause the job to be restarted on a different machine, for instance if there are not enough resources on the current one.</dl>
<dl>
<dt><i>FORBID_APPERROR</i></p>
<dd>If this parameter is set, the application cannot set itself to the error state. Without this parameter jobs returning the value 100 are set to the error state (and therefore can be manually rescheduled by clearing the error state). This can be used to set the job to the error state when a starting condition of the application is not fulfilled before the application itself has been started, or when a clean up procedure (e.g. in the epilog) decides that it is necessary to run the job again. To do so, return 100 in the prolog, pe_start, job script, pe_stop or epilog script.</dl>
<dl>
<dt><i>DISABLE_AUTO_RESCHEDULING</i></p>
<dd><code>Note:</code> Deprecated, may be removed in future release.<br />
 If set to &quot;true&quot; or &quot;1&quot;, the <i>reschedule_unknown</i> parameter is not taken into account.</dl>
<dl>
<dt><i>ENABLE_RESCHEDULE_KILL</i></p>
<dd>If set to &quot;true&quot; or &quot;1&quot;, the <i>reschedule_unknown</i> parameter affects also jobs which have the rerun flag not activated (see the <code>-r y</code> option of and the <code>rerun</code> option of but they are just finished as they can&#8217;t be rescheduled.</dl>
<dl>
<dt><i>ENABLE_RESCHEDULE_SLAVE</i></p>
<dd>If set to &quot;true&quot; or &quot;1&quot; xxQS_NAMExx triggers job rescheduling also when the host where the slave tasks of a parallel job executes is in unknown state, if the <i>reschedule_unknown</i> parameter is activated.</dl>
<dl>
<dt><i>MAX_DYN_EC</i></p>
<dd>Sets the max number of dynamic event clients (as used by <code>qsub -sync y</code> and by xxQS_NAMExx DRMAA API library sessions). The default is 1000. The number of dynamic event clients should not be bigger than half of the number of file descriptors the system has. The file descriptors are shared among the connections to all exec hosts, all event clients, and file handles that the qmaster needs.</dl>
<dl>
<dt><i>MONITOR_TIME</i></p>
<dd>Specifies the time interval when the monitoring information should be printed. The monitoring is disabled by default and can be enabled by specifying an interval. The monitoring is per-thread and is written to the messages file or displayed by with option <code>-f</code>. Example: MONITOR_TIME=0:0:10 generates and prints the monitoring information approximately every 10 seconds. The specified time is a guideline only and not a fixed interval. The interval that is actually used is printed. In this example, the interval could be anything between 9 seconds and 20 seconds.</dl>
<dl>
<dt><i>LOG_MONITOR_MESSAGE</i></p>
<dd>Monitoring information is logged into the messages files by default. This information can be accessed via by If monitoring is always enabled, the messages files can become quite large. This switch disables logging into the messages files, making <i>qping -f</i> the only source of monitoring data.</dl>
<p> Profiling provides the user with the possibility to get system measurements. This can be useful for debugging or optimization of the system. The profiling output will be done within the messages file.</p>
<dl>
<dt><i>PROF_SIGNAL</i></p>
<dd>Enables profiling for the qmaster signal thread (e.g. PROF_SIGNAL=true).</dl>
<dl>
<dt><i>PROF_WORKER</i></p>
<dd>Enables profiling for the qmaster worker threads (e.g. PROF_WORKER=true).</dl>
<dl>
<dt><i>PROF_LISTENER</i></p>
<dd>Enables profiling for the qmaster listener threads (e.g. PROF_LISTENER=true).</dl>
<dl>
<dt><i>PROF_DELIVER</i></p>
<dd>Enables profiling for the qmaster event deliver thread (e.g. PROF_DELIVER=true).</dl>
<dl>
<dt><i>PROF_TEVENT</i></p>
<dd>Enables the profiling for the qmaster timed event thread (e.g. PROF_TEVENT=true).</p>
<dt><i>PROF_SCHEDULER</i></p>
<dd>Enables profiling for the qmaster scheduler thread (e.g. PROF_SCHEDULER=true).</dl>
<p> Please note that the CPU utime and stime values contained in the profiling output are not per-thread CPU times. These CPU usage statistics are per-process statistics. So the printed profiling values for CPU mean &quot;CPU time consumed by sge_qmaster (all threads) while the reported profiling level was active&quot;.</p>
<dl>
<dt><i>STREE_SPOOL_INTERVAL</i></p>
<dd>Sets the time interval for spooling the sharetree usage. The default is set to 00:04:00. The setting accepts colon-separated string or seconds. There is no setting to turn the sharetree spooling off. (e.g. STREE_SPOOL_INTERVAL=00:02:00)</dl>
<dl>
<dt><i>MAX_JOB_DELETION_TIME</i></p>
<dd>Sets the value of how long the qmaster will spend deleting jobs. After this time, the qmaster will continue with other tasks and schedule the deletion of remaining jobs at a later time. The default value is 3 seconds, and will be used if no value is entered. The range of valid values is &gt; 0 and &lt;= 5. (e.g. MAX_JOB_DELETION_TIME=1)</dl>
<dl>
<dt><i>gdi_timeout</i></p>
<dd>Sets how long the communication will wait for GDI send/receive operations. (GDI is the Grid Engine Database Interface for interacting with objects managed by the qmaster.) The default value is set to 60 seconds. After this time, the communication library will retry, if &quot;gdi_retries&quot; is configured, receiving the GDI request. If not configured the communication will return with a &quot;gdi receive failure&quot; (e.g. gdi_timeout=120 will set the timeout time to 120 sec). Configuring no gdi_timeout value, the value defaults to 60 sec.</dl>
<dl>
<dt><i>gdi_retries</i></p>
<dd>Sets how often the GDI receive call will be repeated until the GDI receive error appears. The default is set to 0. In this case the call will be done 1 time with no retry. Setting the value to -1 the call will be done permanently. In combination with the gdi_timeout parameter it is possible to configure a system with, e.g. slow NFS, to make sure that all jobs will be submitted. (E.g. gdi_retries=4.)</dl>
<dl>
<dt><i>cl_ping</i></p>
<dd>Turns on/off a communication library ping. This parameter will create additional debug output. This output shows information about the error messages which are returned by communication and it will give information about the application status of the qmaster. For example, if it&#8217;s unclear what&#8217;s the reason for gdi timeouts, this may show you some useful messages. The default value is false (off) (i.e. cl_ping=false).</dl>
<dl>
<dt><i>SCHEDULER_TIMEOUT</i></p>
<dd>Setting this parameter allows the scheduler GDI event acknowledge timeout to be manually configured to a specific value. Currently the default value is 10 minutes with the default scheduler configuration and limited between 600 and 1200 seconds. Value is limited only in case of default value. The default value depends on the current scheduler configuration. The <i>SCHEDULER_TIMEOUT</i> value is specified in seconds.</dl>
<dl>
<dt><i>jsv_timeout</i></p>
<dd>This parameter measures the response time of the server JSV. In the event that the response time of the JSV is longer than the timeout value specified, this will cause the JSV to be re-started. The default value for the timeout is 10 seconds and if modified, must be greater than 0. If the timeout is reached, the JSV will only try to re-start once; if the timeout is reached again, an error will occur.</dl>
<dl>
<dt><i>jsv_threshold</i></p>
<dd>The threshold of a JSV is measured as the time it takes to perform a server job verification. If this value is greater than the user-defined value, it will cause logging to appear in the qmaster messages file at the INFO level. By setting this value to 0, all jobs will be logged in the qmaster messages file. This value is specified in milliseconds and has a default value of 5000.</p>
<dt><i>OLD_RESCHEDULE_BEHAVIOR</i></p>
<dd>Beginning with version 8.0.0 of xxQS_NAMExx the scheduling behavior changed for jobs that are rescheduled by users. Rescheduled jobs will not be put at the beginning of the pending job list anymore. The submit time of those jobs is set to the end time of the previous run. Due to that, those rescheduled jobs will be appended to the pending job list as if a new job had been submitted. To achieve the old behaviour, set the parameter <i>OLD_RESCHEDULE_BEHAVIOR</i>. Please note that this parameter is deprecated, so it might be removed with the next minor release.</p>
<dt><i>OLD_RESCHEDULE_BEHAVIOR_ARRAY_JOB</i></p>
<dd>Beginning with version 8.0.0 of xxQS_NAMExx the scheduling behavior changed for array job tasks that are rescheduled by users. As soon as an array job task gets rescheduled, all remaining pending tasks of that job will be put at the end of the pending job list. To achieve the old scheduling behaviour set the parameter <i>OLD_RESCHEDULE_BEHAVIOR_ARRAY_JOB</i>. Please note that this parameter is deprecated, so it might be removed with the next minor release.</p>
<dt><i>SIMULATE_EXECDS</i></p>
<dd>Bypass execd communication in qmaster for (e.g. for throughput tests with fake hosts). &quot;Unknown&quot; queue states are suppressed, but <code>load_thresholds=none</code> must be used to avoid queues going into an alarm state since load values are not simulated. Submitted jobs are dispatched, and act as if they are run for a time determined by the job&#8217;s first argument, after 3s spent in the &quot;transferring&quot; state. I.e. there is a simulated 10s runtime for a command such as </p>
<pre> qsub -b y sleep 10</pre>
<p>In this condition, job deletion works, but at least interactive jobs, tightly-integrated parallel ones, and job suspension don&#8217;t. The execution hosts configured need not exist, but must have resolvable network names.</p>
<dt><i>NO_AUTHENTICATION</i></p>
<dd>Don&#8217;t do authentication when GSSAPI security is enabled. This, and the following parameter, determine the GSS global configuration, which can be overridden with the execd_params of the global or host-specific configuration.</p>
<dt><i>NO_SECURITY</i></p>
<dd>Don&#8217;t store and forward credentials if GSSAPI security is enabled.</p>
<dt><i>ENABLE_MTRACE</i></p>
<dd>If GNU malloc is in use (rather then jemalloc, which is usually used on GNU/Linux) enable the facility for recording all memory allocation/deallocation. Requires <i>MALLOC_TRACE</i> to be set in the environment (see</p>
<dt><i>__TEST_SLEEP_AFTER_REQUEST</i></p>
<dd>Used by the test suite to block the worker thread for five seconds after handling a request to ensure another worker thread will handle a subsequent request.</p>
<dt><i>print_malloc_info</i><code></p>
<dd>Allow monitoring statistics if xxQS_NAMExx is built to use the allocator. The information is usually obtained with the -info</code> option of but is generated by the daemons and can&#8217;t be controlled by the client. The default is false since the output is verbose and might confuse programs parsing the traditional format. The parameter can also be set in <code>execd_params</code> and affects both qmaster and execd daemons.</dl>
<p> Changing <code>qmaster_params</code> will take immediate effect, except that gdi_timeout, gdi_retries, and cl_ping will take effect only for new connections. The default for <code>qmaster_params</code> is none. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>execd_params</code></h3>
<p>This is used for passing additional parameters to the xxQS_NAMExx execution daemon. The following values are recognized:</p>
<dl>
<dt><i>ACCT_RESERVED_USAGE</i></p>
<dd>If this parameter is set to true, the usage of &quot;reserved&quot; (allocated) resources is reported in the accounting entries <code>cpu</code>, <code>mem</code>, and <code>maxvmem</code> instead of the measured usage. The live usage values reported by are affected similarly. This means that the &quot;wall clock&quot; time (end-start) is reported instead of CPU time, memory usage is memory allocation times wall clock time (which is only computable if the job requests h_vmem or s_vmem), and maxvmem is the requested h_vmem or s_vmem; the same scaling by slots is done as without this option.<br />
 Note that both the wall clock and CPU times are normally available (see so this option loses information, and &quot;reserved&quot; here has nothing to do with advance/resource reservation. See also <i>SHARETREE_RESERVED_USAGE</i> below.</dl>
<dl>
<dt><i>ENABLE_WINDOMACC</i></p>
<dd>If this parameter is set to true, Windows Domain accounts (WinDomAcc) are used on Windows hosts. These accounts require the use of (See also If this parameter is set to false, or is not set, local Windows accounts are used. On non-Windows hosts, this parameter is ignored.</dl>
<dl>
<dt><i>IGNORE_NGROUPS_MAX_LIMIT</i></p>
<dd>If a user is assigned to NGROUPS_MAX-1 supplementary groups, so that xxQS_NAMExx is not able to add one for job tracking, then the job will go into an error state when it is started. (NGROUPS_MAX is the system limit on supplementary groups; see Administrators that want to prevent the system doing so can set this parameter. In this case the NGROUPS_MAX limit is ignored and the additional group (see <i>gid_range</i>) is not set. As a result for those jobs no online usage will be available. Also the parameter <i>ENABLE_ADDGRP_KILL</i> will have no effect. Please note that it is not recommended to use this parameter. Instead the group membership of the submit user should be reduced.</dl>
<dl>
<dt><i>KEEP_ACTIVE</i></p>
<dd>This value should only be set for debugging purposes. If set to true, the execution daemon will not remove the spool directory maintained by for a job, or cgroup directories if cgroups are in use under Linux.</dl>
<dl>
<dt><i>PTF_MIN_PRIORITY</i>, <i>PTF_MAX_PRIORITY</i></p>
<dd>The maximum/minimum priority which xxQS_NAMExx will assign to a job. Typically this is a negative/positive value in the range of -20 (maximum) to 19 (minimum) for systems which allow setting of priorities with the <i><a href="/docs/linux/man/2-nice/">nice</a></i>(2) system call. Other systems may provide different ranges.<br />
 The default priority range (which varies from system to system) is installed either by removing the parameters, or by setting a value of -999.<br />
 See the &quot;messages&quot; file of the execution daemon for the predefined default value on your hosts. The values are logged during the startup of the execution daemon.</dl>
<dl>
<dt><i>PROF_EXECD</i></p>
<dd>Enables the profiling for the execution daemon (e.g. PROF_EXECD=true).</dl>
<dl>
<dt><i>NOTIFY_KILL</i></p>
<dd>This parameter allows you to change the notification signal for the signal SIGKILL (see the <i>-notify</i> option of The parameter either accepts signal names (use the <i>-l</i> option of <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)) or the special value <i>none</i>. If set to <i>none</i>, no notification signal will be sent. If it is set to <i>TERM</i>, for instance, or another signal name, then this signal will be sent as the notification signal.</dl>
<dl>
<dt><i>NOTIFY_SUSP</i></p>
<dd>With this parameter it is possible to modify the notification signal for the signal SIGSTOP (see the <i>-notify</i> parameter of The parameter either accepts signal names (use the <i>-l</i> option of <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)) or the special value <i>none</i>. If set to <i>none</i>, no notification signal will be sent. If it is set to <i>TSTP</i>, for instance, or another signal name, then this signal will be sent as notification signal.</dl>
<dl>
<dt><i>SHARETREE_RESERVED_USAGE</i></p>
<dd>If this parameter is set to true, the usage of &quot;reserved&quot; resources is taken for the xxQS_NAMExx share tree consumption instead of measured usage. See the description of <i>ACCT_RESERVED_USAGE</i> above for details.<br />
 <code>Note:</code> When running tightly integrated jobs with <i>SHARETREE_RESERVED_USAGE</i> set, and with <i>accounting_summary</i> enabled in the parallel environment, reserved usage will only be reported by the master task of the parallel job. No per-parallel task usage records will be sent from execd to qmaster, which can significantly reduce load on qmaster when running large tightly integrated parallel jobs.</dl>
<dl>
<dt><i>USE_QSUB_GID</i></p>
<dd>If this parameter is set to true, the primary group id active when a job was submitted will be set to become the primary group id for job execution. If the parameter is not set, the primary group id as defined for the job owner in the execution host passwd database is used.<br />
 The feature is only available for jobs submitted via and Also, it only works for jobs (and thus also for and if builtin communication is used, or the rsh and rshd components which are provided with xxQS_NAMExx (see</dl>
<dl>
<dt><i>S_DESCRIPTORS</i>, <i>H_DESCRIPTORS</i>, <i>S_MAXPROC</i>, <i>H_MAXPROC</i>, <i>S_MEMORYLOCKED</i>, <i>H_MEMORYLOCKED</i>, <i>S_LOCKS</i>, <i>H_LOCKS</i></p>
<dd>Specifies soft and hard resource limits as implemented by the <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2) system call. See that manual page on your system for more information. These parameters complete the list of limits set by the RESOURCE LIMITS parameter of the queue configuration as described in Unlike the resource limits in the queue configuration, these resource limits are set for every job on this execution host. If a value is not specified, the resource limit is inherited from the execution daemon process. Because this would lead to unpredictable results if only one limit of a resource is set (soft or hard), the corresponding other limit is set to the same value.<br />
 <i>S_DESCRIPTORS</i> and <i>H_DESCRIPTORS</i> specify a value one greater than the maximum file descriptor number that can be opened by any process of a job.<br />
 <i>S_MAXPROC</i> and <i>H_MAXPROC</i> specify the maximum number of processes that can be created by the job user on this execution host.<br />
 <i>S_MEMORYLOCKED</i> and <i>H_MEMORYLOCKED</i> specify the maximum number of bytes of virtual memory that may be locked into RAM. This typically needs to be set to &quot;unlimited&quot; for use with openib Infiniband, and possibly similar transports.<br />
 <i>S_LOCKS</i> and <i>H_LOCKS</i> specify the maximum number of file locks any process of a job may establish.<br />
 All of these values can be specified using the multiplier letters k, K, m, M, g and G; see for details. Limits can be specified as &quot;infinity&quot; to remove limits (if possible), per <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2).</p>
<dt><i>INHERIT_ENV</i></p>
<dd>This parameter indicates whether the shepherd should allow the environment inherited by the execution daemon from the shell that started it to be inherited by the job it&#8217;s starting. When true, any environment variable that is set in the shell which starts the execution daemon at the time the execution daemon is started will be set in the environment of any jobs run by that execution daemon, unless the environment variable is explicitly overridden, such as PATH or LOGNAME. If set to false, each job starts with only the environment variables that are explicitly passed on by the execution daemon, such as PATH and LOGNAME. The default value is true.</dl>
<dl>
<dt><i>SET_LIB_PATH</i></p>
<dd>This parameter tells the execution daemon whether to add the xxQS_NAMExx shared library directory to the library path of executed jobs. If set to true, and INHERIT_ENV is also set to true, the xxQS_NAMExx shared library directory will be prepended to the library path which is inherited from the shell which started the execution daemon. If INHERIT_ENV is set to false, the library path will contain only the xxQS_NAMExx shared library directory. If set to false, and INHERIT_ENV is set to true, the library path exported to the job will be the one inherited from the shell which started the execution daemon. If INHERIT_ENV is also set to false, the library path will be empty. After the execution daemon has set the library path, it may be further altered by the shell in which the job is executed, or by the job script itself. The default value for SET_LIB_PATH is false.</dl>
<dl>
<dt><i>ENABLE_ADDGRP_KILL</i></p>
<dd>If this parameter is set then xxQS_NAMExx uses the supplementary group ids (see <i>gid_range</i>) to identify all processes which are to be terminated when a job is deleted, or when cleans up after job termination. This currently only works under GNU/Linux, Solaris, Tru64, FreeBSD, and Darwin. The default value is on. Irrelevant with cpuset support (see USE_CGROUPS below).</dl>
<dl>
<dt><i>PDC_INTERVAL</i></p>
<dd>This parameter defines the interval (default 1s) between runs of the PDC (Portable Data Collector) by the execution daemon. The PDC is responsible for enforcing the resource limits s_cpu, h_cpu, s_vmem and h_vmem (see and job usage collection. The parameter can be set to a time_specifier (see to <code>PER_LOAD_REPORT</code> or to <code>NEVER</code>.<br />
 If this parameter is set to <code>PER_LOAD_REPORT</code> the PDC is triggered in the same interval as <code>load_report_time</code> (see above). If this parameter is set to <code>NEVER</code> the PDC run is never triggered. The default is 1 second.<br />
 <code>Note:</code> A PDC run is quite compute intensive, and may degrade the performance of the running jobs. However, if the PDC runs less often, or never, the online usage can be incomplete or totally missing (for example online usage of very short running jobs might be missing) and the resource limit enforcement is less accurate or would not happen if PDC is turned off completely.</dl>
<dl>
<dt><i>ENABLE_BINDING</i></p>
<dd>If this parameter is set, then xxQS_NAMExx enables the core binding module within the execution daemon to apply binding parameters that are specified at submission time of a job. This parameter is set by default if xxQS_NAMExx was compiled with support for core binding. Find more information for job to core binding in the section <i>-binding</i> of</p>
<dt><i>SIMULATE_JOBS</i></p>
<dd>Allow the simulation of jobs. (Job spooling and execution on the execd side is disabled.)</p>
<dt><i>NO_AUTHENTICATION</i></p>
<dd>Turn off authentication for the relevant host(s) when the authentication GSSAPI security feature is enabled globally.</p>
<dt><i>DO_AUTHENTICATION</i></p>
<dd>Turn on authentication for the relevant host(s) when the authentication GSSAPI security feature is enabled globally.</p>
<dt><i>NO_SECURITY</i></p>
<dd>Turn off storing and forwarding of credentials when the GSSAPI security feature is enabled globally.</p>
<dt><i>USE_SYSLOG</i></p>
<dd>Write messages to the system logger (see <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3)) rather than into the spool directory.</p>
<dt><i>USE_QIDLE</i></p>
<dd>Automatically start any executable named <i>qidle</i> present in the architecture-dependent binary directory as a load sensor, similarly to <i>qloadsensor</i> (which is run unconditionally). It is intended to determine whether a workstation is &quot;idle&quot; or not, i.e. whether it has an interactive load. See e.g. the idle time HOWTO &lt;URL: <a rel="nofollow" href="https://gridengine.sourceforge.io/SGE/howto/idle.html">https://gridengine.sourceforge.io/SGE/howto/idle.html</a> &gt; or <i>sources/experimental/qidle</i> in the source repository, but it may be better to check the the screensaver state.</p>
<dt><i>USE_CGROUPS</i></p>
<dd>[Linux only.] Use cgroups/cpusets for resource management if the system supports them and the necessary directories exist in the relevant filesystems (possibly created by <i>util/resources/scripts/setup-cgroups-etc</i>). Makes ENABLE_ADDGRP_KILL irrelevant. This option is experimental, and at least the default is likely to change in future. Default is no.</p>
<dt><i>USE_SMAPS</i></p>
<dd>[Linux only.] Read processes&#8217; <i>smaps</i> file in the <i><a href="/docs/linux/man/5-proc/">proc</a></i>(5) filesystem to obtain PSS usage for most accurate memory accounting, or to obtain the swap usage on older systems which don&#8217;t report PSS. That can be slow when processes have very many maps (observed with an FEM code), significantly increasing the load from execd, so the default is no. Without <i>smaps</i>, usage is reported as RSS+swap, instead of PSS+swap, or simply as the VMsize if the swap value isn&#8217;t available.</p>
<dt><i>RLIMIT_VMEM</i></p>
<dd>Use <i><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></i>(2) to limit the amount of memory address space usable by each process in the job. Available on systems where <i>RLIMIT_VMEM</i> or <i>RLIMIT_AS</i> exists ( <i>RLIMIT_VMEM</i> used preferentially). When a requested memory limit is exhausted, will tend to result in job termination during memory allocation (if true) or memory initialisation (if false). Default is true.</dl>
<dl>
<dt><i>print_malloc_info</i></p>
<dd>See <code>qmaster_params</code> above.</p>
<dt><code>DEMAND_LS</code></p>
<dd>If true, generate load sensor reports just before sending them, making the data fresher. The default is true. The switch is provided in case slow sensors are found to have a bad effect on the execd.</dl>
<p> Changing <code>execd_params</code> will take effect after it is propagated to the execution daemons. The propagation is done in one load report interval. The default for <code>execd_params</code> is none. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>reporting_params</code></h3>
<p>Used to define the behavior of reporting modules in the xxQS_NAMExx qmaster. Changes to the <code>reporting_params</code> take immediate effect. The following values are recognized:</p>
<dl>
<dt><i>accounting</i></p>
<dd>If this parameter is set to true, the accounting file is written. The accounting file is a prerequisite for</dl>
<dl>
<dt><i>reporting</i></p>
<dd>If this parameter is set to true, the reporting file is written. The reporting file contains data that can be used for monitoring and analysis, like job accounting, job log, host load and consumables, queue status and consumables, and sharetree configuration and usage. Attention: Depending on the size and load of the cluster, the reporting file can become quite large. Only activate the reporting file if you have a process running that will consume the reporting file! See for further information about the format and contents of the reporting file.</dl>
<dl>
<dt><i>flush_time</i></p>
<dd>The contents of the reporting file are buffered in the xxQS_NAMExx qmaster and flushed at a fixed interval. This interval can be configured with the <i>flush_time</i> parameter. It is specified as a time value in the format HH:MM:SS or a number of seconds. Sensible values range from a few seconds to a minute. Setting it too low may slow down the qmaster. Setting it too high will make the qmaster consume large amounts of memory for buffering data. The reporting file is opened and closed for each flush. Default 15s.</dl>
<dl>
<dt><i>accounting_flush_time</i></p>
<dd>The contents of the accounting file are buffered in the xxQS_NAMExx qmaster and flushed at a fixed interval. This interval can be configured with the <i>accounting_flush_time</i> parameter. It is specified as a time value in the format HH:MM:SS. Sensible values range from a few seconds to one minute. Setting it too low may slow down the qmaster. Setting it too high will make the qmaster consume large amounts of memory for buffering data. Setting it to 0 disables buffering; as soon as a record is generated, it will be written to the accounting file. If this parameter is not set, the accounting data flush interval will default to the value of the <i>flush_time</i> parameter. The accounting file is opened and closed for each flush.</dl>
<dl>
<dt><i>joblog</i></p>
<dd>If this parameter is set to true, the reporting file will contain job logging information. See for more information about job logging.</dl>
<dl>
<dt><i>sharelog</i></p>
<dd>The xxQS_NAMExx qmaster can dump information about sharetree configuration and use to the reporting file. The parameter <i>sharelog</i> sets an interval in which sharetree information will be dumped. It is set in the format HH:MM:SS or a number of seconds. A value of 0 (default) configures qmaster not to dump sharetree information. Intervals of several minutes up to hours are sensible values for this parameter. See for further information about sharelog.</dl>
<dl>
<dt><i>log_consumables</i></p>
<dd>This parameter controls writing of consumable resources to the reporting file. When set to <code>log_consumables=true</code> information about all consumable resources (their current usage and their capacity) will be written to the reporting file, whenever a consumable resource changes either in definition, or in capacity, or when the usage of an arbitrary consumable resource changes. When <code>log_consumables</code> is set to <code>false</code> (default), only those variables will be written to the reporting file that are configured in the <code>report_variables</code> in the exec host configuration and whose definition or value actually changed. This parameter is deprecated and will get removed in the next major release. See for further information about <code>report_variables</code>.</dl>
<h3><code>finished_jobs</code></h3>
<p><code>Note:</code> Deprecated, may be removed in a future release.<br />
 xxQS_NAMExx stores a certain number of <i>just finished</i> jobs to provide post mortem status information via <i>qstat -s z</i>. The <code>finished_jobs</code> parameter defines the number of finished (&quot;zombie&quot;) jobs stored. If this maximum number is reached, the eldest finished job will be discarded for every new job added to the finished job list. (The zombie list is not spooled, and so will be lost by a qmaster re-start.) </p>
<p> Changing <code>finished_jobs</code> will take immediate effect. The default for <code>finished_jobs</code> is 100. </p>
<p> This value is a global configuration parameter only. It cannot be overwritten by the execution host local configuration.</p>
<h3><code>qlogin_daemon</code></h3>
<h3><code>qlogin_command</code></h3>
<h3><code>rlogin_daemon</code></h3>
<h3><code>rlogin_command</code></h3>
<h3><code>rsh_daemon</code></h3>
<h3><code>rsh_command</code></h3>
<p>These three pairs of entries are responsible for defining a remote startup method for either interactive jobs by or <code>without</code> a command, or an interactive request <code>with</code> a command. The last startup method is also used to startup tasks on a slave exechost of a tightly integrated parallel job. Each pair for one startup method must contain matching communication methods. All entries can contain the value <code>builtin</code> (which is the default) or a full path to a binary which should be used, and additional arguments to this command if necessary. </p>
<p> The entries for the three <code>&#8230;_command</code> definitions can, in addition, contain the value <code>NONE</code> in case a particular startup method should be disabled. </p>
<p> Changing any of these entries will take immediate effect. </p>
<p> The global configuration entries for these values may be overwritten by a execution host local configuration. </p>
<p> See for a detailed explanation of these settings.</p>
<h3><code>delegated_file_staging</code></h3>
<p>This flag must be set to &quot;true&quot; when the prolog and epilog are ready for delegated file staging, so that the DRMAA attribute &#8216;drmaa_transfer_files&#8217; is supported. To establish delegated file staging, use the variables beginning with &quot;$fs_&#8230;&quot; in prolog and epilog to move the input, output and error files from one host to the other. When this flag is set to &quot;false&quot;, no file staging is available for the DRMAA interface. File staging is currently implemented only via the DRMAA interface. When an error occurs while moving the input, output and error files, return error code 100 so that the error handling mechanism can handle the error correctly. (See also FORBID_APPERROR.)</p>
<h3><code>reprioritize</code></h3>
<p><code>Note:</code> Deprecated, may be removed in future release.<br />
 This flag enables or disables the reprioritization of jobs based on their ticket amount. The <code>reprioritize_interval</code> in takes effect only if <code>reprioritize</code> is set to true. To turn off job reprioritization, the <code>reprioritize</code> flag must be set to false and the <code>reprioritize_interval</code> to 0, which is the default. </p>
<p> This value is a global configuration parameter only. It cannot be overridden by the execution host local configuration.</p>
<h3><code>jsv_url</code></h3>
<p>This setting defines a server JSV instance which will be started and triggered by the process. This JSV instance will be used to verify job specifications of jobs before they are accepted and stored in the internal master database. The global configuration entry for this value cannot be overwritten by execution host local configurations. </p>
<p> Find more details concerning JSV in and </p>
<p> The syntax of the <code>jsv_url</code> is specified in</p>
<h3><code>jsv_allowed_mod</code></h3>
<p>If there is a server JSV script defined with the <code>jsv_url</code> parameter, then all or modification requests for jobs are rejected by qmaster. With the <code>jsv_allowed_mod</code> parameter an administrator has the possibility to allow a set of switches which can then be used with clients to modify certain job attributes. The value for this parameter has to be a comma-separated list of JSV job parameter names as documented in or the value <code>none</code> to indicate that no modification should be allowed. Please note that even if <code>none</code> is specified, the switches <code>-w</code> and <code>-t</code> are allowed for qalter.</p>
<h3><code>libjvm_path</code></h3>
<p><code>libjvm_path</code> is usually set during qmaster installation and points to the absolute path of libjvm.so (or the corresponding library depending on your architecture &#8211; e.g. /usr/java/jre/lib/i386/server/libjvm.so). The referenced libjvm version must be at least 1.5. It is needed by the JVM qmaster thread only. If the Java VM needs additional starting parameters they can be set in <code>additional_jvm_args</code>. Whether the JVM thread is started at all can be defined in the file. If libjvm_path is empty, or an incorrect path, the JVM thread fails to start. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h3><code>additional_jvm_args</code></h3>
<p><code>additional_jvm_args</code> is usually set during qmaster installation. Details about possible values <code>additional_jvm_args</code> can be found in the help output of the accompanying Java command. This setting is normally not needed. </p>
<p> The global configuration entry for this value may be overwritten by the execution host local configuration.</p>
<h2>Security</h2>
<p>If <code>prolog</code> or <code>epilog</code> is specified with a <i>user</i><code>@</code> prefix, security considerations apply. The methods are run in a user-supplied environment (via <code>-V</code> or <code>-v</code>) which provides a mechanism to run arbitrary code as <i>user</i> (which might well be root) by setting variables such as <code>LD_LIBRARY_PATH</code> and <code>LD_PRELOAD</code> to affect the running of the dynamically linked programs, such as shells, which are used to implement the methods. </p>
<p> To combat this, known problematic variables are removed from the environment before starting the methods other than as the job owner, but this may not be foolproof on arbitrary systems with obscure variables. The environment can be safely controlled by running the methods under a statically-linked version of <i><a href="/docs/linux/man/1-env/">env</a></i>(1), such as typically available using <i><a href="/docs/linux/man/1-busybox/">busybox</a></i>(1), for example. Use</p>
<dl>
<dd><code>/bin/busybox env -u </code>&#8230;</dl>
<p> to unset sensitive variables, or</p>
<dl>
<dd><code>/bin/busybox env -i name=value</code>&#8230;</dl>
<p> to set only specific variables. On some systems, such as recent Solaris, it is essentially impossible to build static binaries. In that case it is typically possible to use a setuid wrapper, relying on the dynamic linker to do the right thing. An example is the <i>safe_exec</i> wrapper which is available from &lt;URL: <a rel="nofollow" href="https://sourceforge.net/projects/gridengine/files/SGE/support/">https://sourceforge.net/projects/gridengine/files/SGE/support/</a> &gt; at the time of writing. When using a non-shell scripting language wrapper for the method daemon, try to use options which avoid interpreter-specific environmental damage, such as Perl&#8217;s <code>-T</code> and Python&#8217;s <code>-E</code>. Privileged shell script wrappers should be avoided if possible, and should be written carefully if they are used &#8211; e.g. invoke programs with full file names &#8211; but if is used, it should be run with the <code>-p</code> option. </p>
<p> It is not currently possible to specify the variables unset, e.g. as a host-dependent execd parameter, but certain system-dependent ones are selected. The list of sensitive variables is taken mostly from GNU libc and It includes known system-dependent dynamic linker ones, sensitive locale ones and others, like TMPDIR, but does not attempt to deal interpreter-specific variables such as PYTHONPATH. The locale specification is also sanitized. See the source file <i>source/libs/uti2/sge_execvlp.c</i> for details. Note that TMPDIR is one of the variables affected, and may need to be recreated (typically as <code>/tmp/$JOB_ID.$TASK_ID.$SGE_CELL</code>).</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-csh/">csh</a></i>(1), <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></i>(3), <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8),</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
