---
title: "pbs_mom(8)"
name: "pbs_mom"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbs_mom/"
description: "pbs_mom – start a pbs batch execution mini-server"
---

<p>pbs_mom &#8211; start a pbs batch execution mini-server</p>
<h2>Synopsis</h2>
<p>pbs_mom [-a alarm] [-C chkdirectory] [-c config] [-d directory] [-h help] [-H hostname] [-L logfile] [-M MOMport] [-R RPPport] [-p|-q|-r] [-x]</p>
<h2>Description</h2>
<p>The <code>pbs_mom</code> command starts the operation of a batch <code>M</code>achine <code>O</code>riented <code>M</code>ini-server, MOM, on the local host. Typically, this command will be in a local boot file such as <i>/etc/rc.local .</i> To insure that the pbs_mom command is not runnable by the general user community, the server will only execute if its real and effective uid is zero. </p>
<p> One function of pbs_mom is to place jobs into execution as directed by the server, establish resource usage limits, monitor the job&#8217;s usage, and notify the server when the job completes. If they exist, pbs_mom will execute a prologue script before executing a job and an epilogue script after executing the job. The next function of pbs_mom is to respond to resource monitor requests. This was done by a separate process in previous versions of PBS but has now been combined into one process. The resource monitor function is provided mainly for the PBS scheduler. It provides information about the status of running jobs, memory available etc. The next function of pbs_mom is to respond to task manager requests. This involves communicating with running tasks over a tcp socket as well as communicating with other MOMs within a job (aka a &quot;sisterhood&quot;). </p>
<p> Pbs_mom will record a diagnostic message in a log file for any error occurrence. The log files are maintained in the <i>mom_logs</i> directory below the home directory of the server. If the log file cannot be opened, the diagnostic message is written to the system console.</p>
<h2>Options</h2>
<dl>
<dt>-A alias</p>
<dd>Used with -m (multi-mom option) to give the alias name of this instance of pbs_mom</p>
<dt>-a alarm</p>
<dd>Specifies the alarm timeout in seconds for computing a resource. Every time a resource request is processed, an alarm is set for the given amount of time. If the request has not completed before the given time, an alarm signal is generated. The default is 5 seconds.</p>
<dt>-C chkdirectory</p>
<dd>Specifies the path of the directory used to hold checkpoint files. [Currently this is only valid on Cray systems.] The default directory is PBS_HOME/spool/checkpoint, see the -d option. The directory specified with the -C option must be owned by root and accessible (rwx) only by root to protect the security of the checkpoint files.</p>
<dt>-c config</p>
<dd>Specifies an alternative configuration file, see description below. If this is a relative file name it will be relative to PBS_HOME/mom_priv, see the -d option. If the specified file cannot be opened, pbs_mom will abort. If the -c option is not supplied, pbs_mom will attempt to open the default<br />
&nbsp;<wbr>configuration file&nbsp;<wbr>&quot;config&quot;&nbsp;<wbr>in PBS_HOME/mom_priv.&nbsp;<wbr>&nbsp;<wbr>If this file is not present, pbs_mom will log the fact and continue.</p>
<dt>-h help</p>
<dd>Displays the help/usage message.</p>
<dt>-H hostname</p>
<dd>Sets the MOM&#8217;s hostname. This can be useful on multi-homed networks.</p>
<dt>-d directory</p>
<dd>Specifies the path of the directory which is the home of the servers working files, PBS_HOME. This option is typically used along with -M when debugging MOM. The default directory is given by $PBS_SERVER_HOME which is typically <code></p>
<dt>-L logfile</p>
<dd>Specifies an absolute path name for use as the log file. If not specified, MOM will open a file named for the current date in the PBS_HOME/mom_logs directory, see the </code><i> </i><font SIZE="-1"><i> option.</p>
<dt>-m</p>
<dd>Directs the MOM to start in multi-mom mode. In addition to using -m the -M, -R and -A options need to be used to properly start a MOM in multi-mom mode. For example </i><code>pbs_mom -m -M 30002 -R 30003 -A alias-host </code> will start pbs_mom with the service port on port 30002, the manager port at 30003 and with the name alias-host.</p>
<dt>-M port</p>
<dd>Specifies the port number on which the mini-server (MOM) will listen for batch requests.</p>
<dt>-R port</p>
<dd>Specifies the port number on which the mini-server (MOM) will listen for resource monitor requests, task manager requests and inter-MOM messages.</p>
<dt>-p</p>
<dd>(Default after version 2.4.0) (Preserve running jobs) &#8212; Specifies the impact on jobs which were in execution when the<tt>&nbsp;<wbr></tt>mini-server shut-down.<br />
 The -p option tries to preserve any running jobs when the MOM restarts. The new mini-server will not be the parent of any running jobs, MOM has lost control of her<tt>&nbsp;<wbr></tt>offspring (not a new situation for a mother).<br />
 The MOM will allow the jobs to continue to run and monitor them indirectly via polling. All recovered jobs will report an exit code of 0 when they are complete. The -p option is mutually exclusive with the -r, -P and -q options.</p>
<dt>-P</p>
<dd>(Terminate all jobs and remove them from the queue) &#8212; Specifies the impact on jobs which were in execution when the mini-server shut-down. With the -P option, it is assumed that either the entire system has been restarted or the MOM has been down so long that it can no longer guarantee that the pid of any running process is the same as the recorded job process pid of a recovering job. Unlike the -p option no attempt is made to try and preserve or recover running jobs. All jobs are terminated and removed from the queue. The -q option is mutually exclusive with the -p, -q and -r options.</p>
<dt>-q</p>
<dd>(Requeue all jobs &#8211; This is the default behavior in versions prior to 2.4.0) &#8212; Specifies the impact on jobs which were in execution when the mini-servershut-down. Do not terminate running processes. With the -q option, it is assumed that either the entire system has been restarted or the MOM has been down so long that it can no longer guarantee that the pid of any running process is the same as the recorded job process pid of a recovering job. No attempt is made to kill job processes. The MOM will mark the jobs as terminated and notify the batch server which owns the job. Re-runnable jobs will be requeued. The -q option is mutually exclusive with the -p, -P and -r options.</p>
<dt>-r</p>
<dd>(Terminate running processes and requeue all jobs) &#8212; Specifies the impact on jobs which were in execution when the mini-server shut-down. With the -r option, MOM will kill any processes belonging to running jobs, mark the jobs as terminated and notify the batch server that owns the job. Re-runnable jobs are reset to a queued state so they can be run again. The -r option is mutually exclusive with the -p, -P and -q options.</p>
<dd>If the -r option is used following a reboot, process IDs (pids) may be reused and MOM may kill a process that is not a batch session.</p>
<dt>-S port</p>
<dd>Specifies the port number on which the pbs_server is listening for requests. If pbs_server is started with a -p option, pbs_mom will need to use the -S option and match the port value which was used to start pbs_server.</p>
<dt>-x</p>
<dd>Disables the check for privileged port resource monitor connections. This is used mainly for testing since the privileged port is the only mechanism used to prevent any ordinary user from connecting.</dl>
<p> </font></p>
<h2>Configuration File</h2>
<p>The configuration file may be specified on the command line at program start with the -c flag. The use of this file is to provide several types of run time information to pbs_mom: static resource names and values, external resources provided by a program to be run on request via a shell escape, and values to pass to internal set up functions at initialization (and re-initialization). </p>
<p> Each item type is on a single line with the component parts separated by white space. If the line starts with a hash mark (pound sign, #), the line is considered to be a comment and is skipped.</p>
<dl>
<dt>Static Resources</p>
<dd>For static resource names and values, the configuration file contains a list of resource names/values pairs, one pair per line and separated by white space. An Example of static resource names and values could be the number of tape drives of different types and could be specified by</p>
<dd><code> </p>
<dt>Shell Commands</p>
<dd>If the first character of the value is an exclamation mark (!), the entire rest of the line is saved to be executed through the services of the <a href="/docs/linux/man/3-system/">system</a></code>(3) standard library routine.</p>
<dd>The shell escape provides a means for the resource monitor to yield arbitrary information to the scheduler. Parameter substitution is done such that the value of any qualifier sent with the query, as explained below, replaces a token with a percent sign (%) followed by the name of the qualifier. For example, here is a configuration file line which gives a resource name of &quot;escape&quot;:</p>
<dd><code></p>
<dd>If a query for &quot;escape&quot; is sent with no qualifiers, the command executed would be &quot;echo %xxx %yyy&quot;. If one qualifier is sent, &quot;escape[xxx=hi there]&quot;, the command executed would be &quot;echo hi there %yyy&quot;. If two qualifiers are sent, &quot;escape[xxx=hi][yyy=there]&quot;, the command executed would be &quot;echo hi there&quot;. If a qualifier is sent with no matching token in the command line, &quot;escape[zzz=snafu]&quot;, an error is reported.</p>
<dt>size[fs=&lt;FS&gt;]</p>
<dd>Specifies that the available and configured disk space in the &lt;FS&gt; filesystem is to be reported to the pbs_server and scheduler. NOTE: To request disk space on a per job basis, specify the file resource as in &#8216;qsub -l nodes=1,file=1000kb&#8217; For example, the available and configured disk space in the /localscratch filesystem will be reported:</p>
<dd>
<dt>Initialization Value</p>
<dd>An initialization value directive has a name which starts with a dollar sign ($) and must be known to MOM via an internal table. The entries in this table now are:</p>
<dl>
<dd>
<dl>
<dt>auto_ideal_load</p>
<dd>if jobs are running, sets idea_load based on a simple expression. The expressions start with the variable &#8216;t&#8217; (total assigned CPUs) or &#8216;c&#8217; (existing CPUs), an operator (+ &#8211; / *), and followed by a float constant.</p>
<dd>
<dt>auto_max_load</p>
<dd>if jobs are running, sets max_load based on a simple expression. The expressions start with the variable &#8216;t&#8217; (total assigned CPUs) or &#8216;c&#8217; (existing CPUs), an operator (+ &#8211; / *), and followed by a float constant.</p>
<dt>cputmult</p>
<dd>which sets a factor used to adjust cpu time used by a job. This is provided to allow adjustment of time charged and limits enforced where the job might run on systems with different cpu performance. If Mom&#8217;s system is faster than the reference system, set cputmult to a decimal value greater than 1.0. If Mom&#8217;s system is slower, set cputmult to a value between 1.0 and 0.0. For example:</p>
<dd>
<dt>configversion</p>
<dd>specifies the version of the config file data, a string.</p>
<dt>check_poll_time</p>
<dd>specifies the MOM interval in seconds. MOM checks each job for updated resource usages, exited processes, over-limit conditions, etc. once per interval. This value should be equal or lower to pbs_server&#8217;s job_stat_rate. High values result in stale information reported to pbs_server. Low values result in increased system usage by MOM. Default is 45 seconds.</p>
<dt>down_on_error</p>
<dd>causes MOM to report itself as state &quot;down&quot; to pbs_server in the event of a failed health check. This feature is EXPERIMENTAL and likely to be removed in the future. See HEALTH CHECK below.</p>
<dt>enablemomrestart</p>
<dd>enable automatic restarts of MOM. If enabled, MOM will check if its binary has been updated and restart itself at a safe point when no jobs are running; thus making upgrades easier. The check is made by comparing the mtime of the pbs_mom executable. Command-line args, the process name, and the PATH env variable are preserved across restarts. It is recommended that this not be enabled in the config file, but enabled when desired with momctl (see RESOURCES for more information.)</p>
<dt>ideal_load</p>
<dd>ideal processor load. Represents a low water mark for the load average. Nodes that are currently busy will consider itself free after falling below ideal_load.</p>
<dt>igncput</p>
<dd>Ignore cpu time violations on this mom, meaning jobs will not be cancelled due to exceeding their limits for cpu time.</p>
<dt>ignmem</p>
<dd>Ignore memory violations on this mom, meaning jobs will not be cancelled due to exceeding their memory limits.</p>
<dt>ignvmem</p>
<dd>If set to true, then pbs_mom will ignore vmem/pvmem limit enforcement.</p>
<dt>ignwalltime</p>
<dd>If set to true, then pbs_mom will ignore walltime limit enforcement.</p>
<dt>job_output_file_mask</p>
<dd>Specifies a mask for creating job output and error files. Values can be specified in base 8, 10, or 16; leading 0 implies octal and leading 0x or 0X hexadecimal. A value of &quot;userdefault&quot; will use the user&#8217;s default umask. </p>
<dt>log_directory</p>
<dd>Changes the log directory. Default is $TORQUEHOME/mom_logs/. $TORQUEHOME default is /var/spool/torque/ but can be changed in the ./configure script. The value is a string and should be the full path to the desired mom log directory. </p>
<dt>logevent</p>
<dd>which sets the mask that determines which event types are logged by pbs_mom. For example:</p>
<dd>
<dd>The first example would set the log event mask to 0x1ff (511) which enables logging of all events including debug events. The second example would set the mask to 0x0ff (255) which enables all events except debug events.</p>
<dt>log_file_suffix</p>
<dd>Optional suffix to append to log file names. If %h is the suffix, pbs_mom appends the hostname for where the log files are stored if it knows it, otherwise it will append the hostname where the mom is running. </p>
<dt>log_keep_days</p>
<dd>Specifies how many days to keep log files. pbs_mom deletes log files older than the specified number of days. If not specified, pbs_mom won&#8217;t delete log files based on their age.</p>
<dt>loglevel</p>
<dd>specifies the verbosity of logging with higher numbers specifying more verbose logging. Values may range between 0 and 7.</p>
<dt>log_file_max_size</p>
<dd>If this is set to a value &gt; 0 then pbs_mom will roll the current log file to log-file-name.1 when its size is greater than or equal to the value of log_file_max_size. This value is interpreted as kilobytes.</p>
<dt>log_file_roll_depth</p>
<dd>If this is set to a value &gt;=1 and log_file_max_size is set then pbs_mom will continue rolling the log files to log-file-name.log_file_roll_depth.</p>
<dt>max_load</p>
<dd>maximum processor load. Nodes over this load average are considered busy (see ideal_load above).</p>
<dt>memory_pressure_threshold</p>
<dd>The option is only available, if pbs_mom is enabled to use cpusets. If set to a value &gt; 0, a job gets killed if its memory pressure exceeds this value, and if $memory_pressure_duration is set. The default is 0 (memory pressure recording is off).<br />
 See <a href="/docs/linux/man/7-cpuset/">cpuset</a>(7) for more information about memory pressure.</p>
<dt>memory_pressure_duration</p>
<dd>The option is only available, if pbs_mom is enabled to use cpusets. Specifies the number of subsequent MOM intervals a job&#8217;s memory pressure must be above $memory_pressure_threshold to get killed. The default is 0 (jobs are never killed due to memory pressure). set<br />
 See <a href="/docs/linux/man/7-cpuset/">cpuset</a>(7) for more information about memory pressure.</p>
<dt>node_check_script</p>
<dd>specifies the fully qualified pathname of the health check script to run (see HEALTH CHECK for more information).</p>
<dt>node_check_interval</p>
<dd>specifies when to run the MOM health check. The check can be either periodic, event-driver, or both. The value starts with an integer specifying the number of MOM intervals between subsequent executions of the specified health check. After the integer is an optional comma-separated list of event names. Currently supported are &quot;jobstart&quot; and &quot;jobend&quot;. This value defaults to 1 with no events indicating the check is run every MOM interval. (see HEALTH CHECK for more information)</p>
<dd>
<dd>
<dt>nodefile_suffix</p>
<dd>Specifies the suffix to append to a host names to denote the data channel network adapter in a multihomed compute node. With the suffix of &#8216;i&#8217; and the control channel adapter with the name node01, the data channel would have a hostname of node01i.</p>
<dt>nospool_dir_list</p>
<dd>If the job&#8217;s output file should be in one of the paths specified here, then it will be spooled directly in that directory instead of the normal spool directory.<br />
 Specified in the format path1, path2, etc.</p>
<dt>pbsclient</p>
<dd>which causes a host name to be added to the list of hosts which will be allowed to connect to MOM as long as they are using a privilaged port for the purposes of resource monitor requests. For example, here are two configuration file lines which will allow the hosts &quot;fred&quot; and &quot;wilma&quot; to connect:</p>
<dd>
<dd>Two host name are always allowed to connection to pbs_mom, &quot;localhost&quot; and the name returned to pbs_mom by the system call gethostname(). These names need not be specified in the configuration file. The hosts listed as &quot;clients&quot; can issue Resource Monitor (RM) requests. Other MOM nodes and servers do not need to be listed as clients.</p>
<dt>pbsserver</p>
<dd>which defines hostnames running pbs_server that will be allowed to submit jobs, issue Resource Monitor (RM) requests, and get status updates. MOM will continually attempt to contact all server hosts for node status and state updates. Like $PBS_SERVER_HOME/server_name, the hostname may be followed by a colon and a port number. This parameter replaces the oft-confused $clienthost parameter from TORQUE 2.0.0p0 and earlier. Note that the hostname in $PBS_SERVER_HOME/server_name is used if no $pbsserver parameters are found</p>
<dt>prologalarm</p>
<dd>Specifies maximum duration (in seconds) which the MOM will wait for the job prolog or job job epilog to complete. This parameter default to 300 seconds (5 minutes)</p>
<dt>rcpcmd</p>
<dd>Specify the the full path and argument to be used for remote file copies. This overrides the compile-time default found in configure. This must contain 2 words: the full path to the command and the switches. The copy command must be able to recursively copy files to the remote host and accept arguments of the form &quot;user [at] host:files&quot; For example:</p>
<dd>
<dt>restricted</p>
<dd>which causes a host name to be added to the list of hosts which will be allowed to connect to MOM without needing to use a privilaged port. These names allow for wildcard matching. For example, here is a configuration file line which will allow queries from any host from the domain &quot;ibm.com&quot;.</p>
<dd>
<dd>The restriction which applies to these connections is that only internal queries may be made. No resources from a config file will be found. This is to prevent any shell commands from being run by a non-root process.<br />
 This parameter is generally not required except for some versions of OSX.</p>
<dt>remote_checkpoint_dirs</p>
<dd>Specifies what server checkpoint directories are remotely mounted. This directive is used to tell the MOM which directories are shared with the server. Using remote checkpoint directories eliminates the need to copy the checkpoint files back and forth between the MOM and the server. This parameter is available in 2.4.1 and later.</p>
<dd>
<dt>remote_reconfig</p>
<dd>Enables the ability to remotely reconfigure pbs_mom with a new config file. Default is disabled. This parameter accepts various forms of true, yes, and 1.</p>
<dt>source_login_batch</p>
<dd>Specifies whether or not mom will source the /etc/profile, etc. type files for batch jobs. Parameter accepts various forms of true, false, yes, no, 1 and 0. Default is True.</p>
<dt>source_login_interactive</p>
<dd>Specifies whether or not mom will source the /etc/profile, etc. type files for interactive jobs. Parameter accepts various forms of true, false, yes, no, 1 and 0. Default is True.</p>
<dt>spool_as_final_name</p>
<dd>If set to true, jobs will spool directly as their output files, with no intermediate locations or steps. This is mostly useful for shared filesystems with fast writing capability.</p>
<dt>status_update_time</p>
<dd>Specifies (in seconds) how often MOM updates its status information to pbs_server. This value should correlate with the server&#8217;s scheduling interval. High values increase the load of pbs_server and the network. Low values cause pbs_server to report stale information. Default is 45 seconds.</p>
<dt>tmpdir</p>
<dd>Sets the directory basename for a per-job temporary directory. Before job launch, MOM will append the jobid to the tmpdir basename and create the directory. After the job exit, MOM will recursively delete it. The env variable TMPDIR will be set for all pro/epilog scripts, the job script, and TM tasks.<br />
 Directory creation and removal is done as the job owner and group, so the owner must have write permission to create the directory. If the directory already exists and is owned by the job owner, it will not be deleted after the job. If the directory already exists and is NOT owned by the job owner, the job start will be rejected.</p>
<dt>timeout</p>
<dd>Specifies the number of seconds before TCP messages will time out. TCP messages include job obituaries, and TM requests if RPP is disabled. Default is 60 seconds.</p>
<dt>usecp</p>
<dd>specifies which directories should be staged with cp instead of rcp/scp. If a shared filesystem is available on all hosts in a cluster, this directive is used to make these filesystems known to MOM. For example, if /home is NFS mounted on all nodes in a cluster:</p>
<dd>
<dt>varattr</p>
<dd>This is similar to a shell escape above, but includes a TTL. The command will only be run every TTL seconds. A TTL of -1 will cause the command to be executed only once. A TTL of 0 will cause the command to be run everytime varattr is requested. This parameter may be used multiple times, but all output will be grouped into a single &quot;varattr&quot; attribute in the request and status output. The command should output data in the form of</p>
<dd>
<dt>use_smt</p>
<dd>This option is only available, if pbs_mom is enabled to use cpusets. It has only effect, if there are more that one logical processor per physical core in the system (simultaneous multithreading or hyperthreading is enabled via BIOS settings). If set to true, all logical processors of allocated cores are added to the cpuset of a job. If set to false, only the first logical processor per allocated core is contained in the cpuset of a job. The default is true.</p>
<dt>wallmult</p>
<dd>which sets a factor used to adjust wall time usage by to job to a common reference system. The factor is used for walltime calculations and limits the same as cputmult is used for cpu time.</dl>
</dl>
</dl>
<p> The configuration file must be executable and &quot;secure&quot;. It must be owned by a user id and group id less than 10 and not be world writable. Output from this file must be in the format $VAR=$VAL, i.e.,</p>
<dl>
<dd></dl>
<dl>
<dt>xauthpath</p>
<dd>Specifies the path to the xauth binary to enable X11 fowarding.</p>
<dt>mom_host</p>
<dd>Sets the local hostname as used by pbs_mom.
</dl>
<p> </code></p>
<h2>Layout File</h2>
<p>There is also an optional layout file for creating multiple moms on one box in a specified layout. In the file, each mom on the single box is given its own hostname, cpu indexes, memory nodes (a linux construct), and memory size. This is useful for NUMA systems. Each line in the file specifies one mom. The file follows the following format:</p>
<dl>
<dt>&lt;hostname&gt; cpus=&lt;X&gt; mem=&lt;Y&gt; memsize=&lt;Z&gt;</p>
<dd>cpus and mem can be comma separated lists, while memsize should be a memory size in the format:</p>
<dt>&lt;number&gt;&lt;units&gt;</p>
<dd>For example, a file could contain the following line:</p>
<dt>foohost-1 cpus=1,2 mem=1,2,3,4 memsize=8GB</p>
<dd>This would specify that foohost-1 has cpus 1 and 2, memory nodes 1-4, and a total of 8 GB of memory.</dl>
<h2>Resources</h2>
<p>Resource Monitor queries can be made with momctl&#8217;s -q option to retrieve and set pbs_mom options. Any configured static resource may be retrieved with a request of the same name. These are resource requests not otherwise documented in the PBS ERS.</p>
<dl>
<dt>cycle</p>
<dd>forces an immediate MOM cycle</p>
<dt>status_update_time</p>
<dd>retrieve or set the $status_update_time parameter</p>
<dt>check_poll_time</p>
<dd>retrieve or set the $check_poll_time parameter</p>
<dt>configversion</p>
<dd>retrieve the config version</p>
<dt>jobstartblocktime</p>
<dd>retrieve or set the $jobstartblocktime parameter</p>
<dt>enablemomrestart</p>
<dd>retrieve or set the $enablemomrestart parameter</p>
<dt>loglevel</p>
<dd>retrieve or set the $loglevel parameter</p>
<dt>down_on_error</p>
<dd>retrieve or set the EXPERIMENTAL $down_on_error parameter</p>
<dt>diag0 &#8211; diag4</p>
<dd>retrieves various diagnostic information</p>
<dt>rcpcmd</p>
<dd>retrieve or set the $rcpcmd parameter</p>
<dt>version</p>
<dd>retrieves the pbs_mom version</dl>
<h2>Health Check</h2>
<p>The health check script is executed directly by the pbs_mom daemon under the root user id. It must be accessible from the compute node and may be a script or compiled executable program. It may make any needed system calls and execute any combination of system utilities but should not execute resource manager client commands. Also, as of TORQUE 1.0.1, the pbs_mom daemon blocks until the health check is completed and does not possess a built-in timeout. Consequently, it is advisable to keep the launch script execution time short and verify that the script will not block even under failure conditions. </p>
<p> If the script detects a failure, it should return the keyword &#8216;ERROR&#8217; to stdout followed by an error message. The message (up to 256 characters) immediately following the ERROR string will be assigned to the node attribute &#8216;message&#8217; of the associated node. </p>
<p> If the script detects a failure when run from &quot;jobstart&quot;, then the job will be rejected. This should probably only be used with advanced schedulers like Moab so that the job can be routed to another node. </p>
<p> TORQUE currently ignores ERROR messages by default, but advanced schedulers like moab can be configured to react appropriately. </p>
<p> If the experimental $down_on_error MOM setting is enabled, MOM will set itself to state down and report to pbs_server; and pbs_server will report the node as &quot;down&quot;. Additionally, the experimental &quot;down_on_error&quot; server attribute can be enabled which has the same effect but moves the decision to pbs_server. It is redundant to have MOM&#8217;s $down_on_error and pbs_server&#8217;s down_on_error features enabled. See &quot;down_on_error&quot; in <a href="//www.systutorials.com/docs/linux/man/7B-pbs_server_attributes/">pbs_server_attributes</a>(7B).</p>
<h2>Files</h2>
<dl>
<dt>$PBS_SERVER_HOME/server_name</p>
<dd>contains the hostname running pbs_server.</p>
<dt>$PBS_SERVER_HOME/mom_priv</p>
<dd>the default directory for configuration files, typically (/usr/spool/pbs)/mom_priv.</p>
<dt>$PBS_SERVER_HOME/mom_logs</p>
<dd>directory for log files recorded by the server.</p>
<dt>$PBS_SERVER_HOME/mom_priv/prologue</p>
<dd>the administrative script to be run before job execution.</p>
<dt>$PBS_SERVER_HOME/mom_priv/epilogue</p>
<dd>the administrative script to be run after job execution.</dl>
<h2>Signal Handling</h2>
<p>pbs_mom handles the following signals:</p>
<dl>
<dt>SIGHUP</p>
<dd>causes pbs_mom to re-read its configuration file, close and reopen the log file, and reinitialize resource structures.</p>
<dt>SIGALRM</p>
<dd>results in a log file entry. The signal is used to limit the time taken by certain children processes, such as the prologue and epilogue.</p>
<dt>SIGINT and SIGTERM</p>
<dd>results in pbs_mom exiting without terminating any running jobs. This is the action for the following signals as well: SIGXCPU, SIGXFSZ, SIGCPULIM, and SIGSHUTDN.</p>
<dt>SIGUSR1, SIGUSR2</p>
<dd>causes MOM to increase and decrease logging levels, respectively.</p>
<dt>SIGPIPE, SIGINFO</p>
<dd>&nbsp;<wbr>are ignored.</p>
<dt>SIGBUS, SIGFPE, SIGILL, SIGTRAP, and SIGSYS</p>
<dd>cause a core dump if the PBSCOREDUMP environmental variable is defined.</dl>
<p> All other signals have their default behavior installed.</p>
<h2>Exit Status</h2>
<p>If the mini-server command fails to begin operation, the server exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_scheduler_basl/">pbs_scheduler_basl</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_scheduler_tcl/">pbs_scheduler_tcl</a>(8B), the PBS External Reference Specification, and the PBS Administrator&#8217;s Guide. </p>
