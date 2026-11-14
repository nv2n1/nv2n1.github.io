---
title: "pbs_server_attributes(7)"
name: "pbs_server_attributes"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pbs_server_attributes/"
description: "pbs_server_attributes – pbs server attributes"
---

<p>pbs_server_attributes &#8211; pbs server attributes</p>
<h2>Description</h2>
<p>Server attributes can be read by any client; privilege is not required. Most server attributes are alterable by a privileged client, run by a user with administrator or operator privilege. Certain attributes require the user to have full administrator privilege. The following is a list of the server attributes.</p>
<dl>
<dd><i></p>
<dl>
<dt>accounting_keep_days</i><font SIZE="+1"><i></i></p>
<dd>This defines the number of days that accounting files will be kept. Default value: unset &#8211; pbs_server will never delete accounting files Format: integer <i></p>
<dt>acl_group_sloppy</i></font><font SIZE="+2"><i></i></p>
<dd>This is a default value for the queue attribute of the same name. Format: boolean, &quot;TRUE&quot;, &quot;True&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;FALSE&quot;, &quot;False&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false = disabled. <i></p>
<dt>acl_host_enable</i></font><font SIZE="+3"><i></i></p>
<dd>Attribute which when true directs the server to use the <i>acl_hosts</i> access control lists. Requires full manager privilege to set or alter. Format: boolean, &quot;TRUE&quot;, &quot;True&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;FALSE&quot;, &quot;False&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false = disabled. <i></p>
<dt>acl_hosts</i></font><font SIZE="+4"><i></i></p>
<dd>List of hosts which may request services from this server. This list contains the network name of the hosts. Local requests, i.e. from the server&#8217;s host itself, are aways accepted even if the host is not included in the list. See section 10.1, Authorization, in the PBS External Reference Specification. Requires full manager privilege to set or alter. Format: &quot;[+|-]hostname.domain[,&#8230;]&quot;; default value: all hosts. <i></p>
<dt>acl_logic_or</i></font><font SIZE="+5"><i></i></p>
<dd>This is a default value for the queue attribute of the same name. Format: boolean, &quot;TRUE&quot;, &quot;True&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;FALSE&quot;, &quot;False&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false = disabled. <i></p>
<dt>acl_user_enable</i></font><font SIZE="+6"><i></i></p>
<dd>Attribute which when true directs the server to use the server level <i>acl_users</i> access list. Requires full manager privilege to set or alter. Format: boolean (see acl_group_enable); default value: disabled. <i></p>
<dt>acl_users</i></font><font SIZE="+7"><i></i></p>
<dd>List of users allowed or denied the ability to make any requests of this server. See section 10.1, Authorization, in the PBS External Reference Specification. If acl_user_enable is set to true, only users listed in acl_users may submit to or execute jobs in the queue. Requires full manager privilege to set or alter. Format: &quot;[+|-]user[@host][,&#8230;]&quot;; default value: all users allowed. <i></p>
<dt>acl_roots</i></font><font SIZE="+8"><i></i></p>
<dd>List of super users who may submit to and execute jobs at this server. If the job execution id would be zero (0), then the job owner, root [at] host, must be listed in this access control list or the job is rejected. Format: &quot;[+|-]user[@host][,&#8230;]&quot;; default value: no root jobs allowed. <i></p>
<dt>allow_node_submit</i></font><font SIZE="+9"><i></i></p>
<dd>Allow job submissions from compute nodes regardless of ruserok(). Requires full manager privilege to set or alter. Format: boolean; default value: disabled. <i></p>
<dt>allow_proxy_user</i></p>
<dd>Specifies users can proxy from one user to another. Proxy requests will be either validated by ruserok() or by the scheduler. Format: boolean; default value: false. <i></p>
<dt>auto_node_np</i></p>
<dd>Automatically configure a node&#8217;s np value based on the ncpus value from the status update. Requires full manager privilege to set or alter. Format: boolean; default value: disabled. <i></p>
<dt>clone_batch_delay</i></p>
<dd>Number of seconds to delay between cloning a batch for a job array. Format: integer; default value: 1. <i></p>
<dt>clone_batch_size</i></p>
<dd>Number of jobs to clone in a batch for a job array. Format: integer; default value: 256. <i></p>
<dt>credential_lifetime</i></p>
<dd>The number of a seconds that a client connection may stay connected without re-authenticating. Default is 3600 seconds. <i></p>
<dt>comment</i></p>
<dd>A text string which may be set by the scheduler or other privileged client to provide information to the batch system users. Format: any string; default value: none. <i></p>
<dt>default_node</i></p>
<dd>A node specification to use if there is no other supplied specification. This attribute is only used by servers where a <i>nodes</i> file exist in the server_priv directory providing a list of nodes to the server. If the nodes file does not exist, this attribute is not set by default and is ignored if set. The default value allows for jobs to share a single node. Format: a node specification string; default value: 1#shared. <i></p>
<dt>default_queue</i></p>
<dd>The queue which is the target queue when a request does not specify a queue name. Format: a queue name; default value: none, must be set to an existing queue. <i></p>
<dt>down_on_error</i></p>
<dd>Set a node&#8217;s state to &quot;down&quot; if MOM reports a message beginning with the string &quot;ERROR&quot;. This might interfere with moab&#8217;s node error handling. See the HEALTH CHECK section in <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B). This is an EXPERIMENTAL feature and may be removed in the future. Format: boolean; default value: false. <i></p>
<dt>disable_server_id_check</i></p>
<dd>Makes it so the user for the job doesn&#8217;t have to exist on the server. The user must still exist on all the compute nodes or the job will fail when it tries to execute. Format: boolean; default value: false <i></p>
<dt>extra_resc</i></p>
<dd>Add additional string-type job resources. They have no effect within TORQUE and are only advisible to the scheduler. They can not be used for resources_default/min/max. Format: list; default value: none. <i></p>
<dt>job_force_cancel_time</i></p>
<dd>If configured, number of seconds after a delete where a job will be purged by the server. If not configured, no such thing happens. Format: integer; default value: not used. <i></p>
<dt>job_nanny</i></p>
<dd>Enables the &quot;job deletion nanny&quot; feature. All job cancels will create a repeating task that will resend KILL signals if the initial job cancel failed. Further job cancels will be rejected with the message &quot;job cancel in progress.&quot; This is useful for temporary failures with a job&#8217;s execution node during a job delete request. It is possible that the job nanny might interfere with job restarts, migrations, and checkpointing. Format: boolean; default value: false. <i></p>
<dt>job_start_timeout</i></p>
<dd>Specifies the pbs_server to pbs_mom TCP socket timeout in seconds that is used when the pbs_server sends a job start to the pbs_mom. It is useful when the mom has extra overhead involved in starting jobs. If not specified then the tcp_timeout value is used. <i></p>
<dt>job_stat_rate</i></p>
<dd>Moderates how often job stat requests will be issued from pbs_server to the MOM daemons. If poll_jobs is unset or false, then all jobs that haven&#8217;t been updated in job_stat_rate seconds will trigger a stat request. If poll_jobs is true, then all jobs will be updated every job_stat_rate.<br />
&nbsp;<wbr>(see poll_jobs)&nbsp;<wbr>&nbsp;<wbr>On active clusters, 60 or 120 might be reasonable. Default value: 45 seconds (PBS_RESTAT_JOB in server_limits.h) Minimum value: 4 seconds (PBS_JOBSTAT_MIN in server_limits.h) <i></p>
<dt>keep_completed</i></p>
<dd>Number of seconds to retain completed jobs in the C state. This is overridden by the execution queue attribute of the same name. Format: integer; default value: 0. <i></p>
<dt>kill_delay</i></p>
<dd>The amount of the time delay between the sending of SIGTERM and SIGKILL when a qdel command is issued against a running job. This is overridden by the execution queue attribute of the same name. Format: integer seconds; default value: 2 seconds. <i></p>
<dt>lock_file</i></p>
<dd>Specifies the name and location of the lock file used to determine which high availability server should be active.<br />
 If a full path is specified, it is used verbatim by TORQUE. If a relative path is specified, TORQUE will prefix it with $TORQUE_HOME/server_priv. Format: string; default value: $TORQUE_HOME/server_priv/server.lock <i></p>
<dt>lock_file_update_time</i></p>
<dd>Specifies how often (in seconds) the thread will update the lockfile. (for threaded high availability) Format: integer; default value: 3 <i></p>
<dt>lock_file_check_time</i></p>
<dd>Specifies how often (in seconds) a high availability server will check to see if it should become active. (for threaded high availability) Must be greater than lock_file_update_time. Format: integer; default value: 9 <i></p>
<dt>log_events</i></p>
<dd>A bit string which specifies the type of events which are logged, see the section on Event Logging in chapter 3 of the ERS. Format: integer; default value: 511, all events. <i></p>
<dt>log_file_max_size</i></p>
<dd>If this is set to a value &gt; 0 then pbs_server will roll the current log file to logfile.1 when its size is greater than or equal to the value of log_file_max_size. This value is interpreted as kilobytes. <i></p>
<dt>log_file_roll_depth</i></p>
<dd>If this is set to a value &gt;=1 and log_file_max_size is set then pbs_server will continue rolling the log files to logfile.log_file_roll_depth. <i></p>
<dt>log_keep_days</i></p>
<dd>If this is set then logs older than X days will be removed by the server. Format: integer; default value: not enforced; <i></p>
<dt>log_level</i></p>
<dd>Controls the verbosity of server logs. This value ranges from 0 to 7 with 7 representing maximum verbosity. Format: integer; default value: 0, minimum verbosity. <i></p>
<dt>mail_body_fmt</i></p>
<dd>Override the default format for the body of outgoing mail messages. A number of printf-like format specifiers and escape sequences can be used:</p>
<dt>
</p>
<dd>new line</p>
<dt>	</p>
<dd>horizontal tab</p>
<dt>\</p>
<dd>backslash</p>
<dt>\&#8217;</p>
<dd>single quote</p>
<dt>\&quot;</p>
<dd>double quote</p>
<dt>%d</p>
<dd>details concerning the message</p>
<dt>%h</p>
<dd>PBS host name</p>
<dt>%i</p>
<dd>PBS job identifier</p>
<dt>%j</p>
<dd>PBS job name</p>
<dt>%m</p>
<dd>long reason for message</p>
<dt>%r</p>
<dd>short reason for message</p>
<dt>%%</p>
<dd>a single %</dl>
<p> Format: a printf-like format string; Default value: &quot;PBS Job Id: %i
Job Name: %j
Exec host: %h
%m
%d
&quot;. <i></p>
<dl>
<dt>mail_domain</i></p>
<dd>Override the default domain for outgoing mail messages. If set, emails will be addressed to &quot;euser [at] mail_domain&quot;. If unset, the job&#8217;s Job_Owner attribute will be used. If set to &quot;never&quot;, TORQUE will never send emails. Format: a domain name; Default value: none. <i></p>
<dt>mail_from</i></p>
<dd>Set the From: header for all outgoing emails from pbs_server. Format: an email address; Default value: &quot;adm&quot;. <i></p>
<dt>mail_subject_fmt</i></p>
<dd>Override the default format for the subject of outgoing mail messages. A number of printf-like format specifiers and escape sequences can be used:</p>
<dt>
</p>
<dd>new line</p>
<dt>	</p>
<dd>horizontal tab</p>
<dt>\</p>
<dd>backslash</p>
<dt>\&#8217;</p>
<dd>single quote</p>
<dt>\&quot;</p>
<dd>double quote</p>
<dt>%d</p>
<dd>details concerning the message</p>
<dt>%h</p>
<dd>PBS host name</p>
<dt>%i</p>
<dd>PBS job identifier</p>
<dt>%j</p>
<dd>PBS job name</p>
<dt>%m</p>
<dd>long reason for message</p>
<dt>%r</p>
<dd>short reason for message</p>
<dt>%%</p>
<dd>a single %</dl>
<p> Format: a printf-like format string; Default value: &quot;PBS JOB %i&quot;. <i></p>
<dl>
<dt>mail_uid</i></p>
<dd>The uid from which server generated mail is sent to users. Format: integer uid; default value: 0 for root. <i></p>
<dt>managers</i></p>
<dd>List of users granted batch administrator privileges. Format: <code> The host, sub-domain, or domain name may be wild carded by the use of an * character, see the description of user access control lists in chapter 10.1.1 of the ERS. Requires full manager privilege to set or alter. Default value: root on the local host. </code><i></p>
<dt>max_job_array_size</i></p>
<dd>Specifies the maximum number of jobs that can be in any requested job array. Arrays requesting more jobs than configured will be rejected. Format: integer; default value: Unlimited. <i></p>
<dt>max_slot_limit</i></p>
<dd>No array can request a slot limit greater than 10. Any array that does not request a slot limit receives a slot limit of 10. Using the example above, slot requests greater than 10 are rejected. A slot limit is the maximum number of jobs from an array that can run concurrently. Format: integer; default value: Unlimited. <i></p>
<dt>max_running</i></p>
<dd>The maximum number of jobs allowed to be selected for execution at any given time. Advisory to the Scheduler, not enforced by the server. Format: integer. <i></p>
<dt>max_user_run</i></p>
<dd>The maximum number of jobs owned by a single user that are allowed to be running from this queue at one time. This attribute is advisory to the Scheduler, it is not enforced by the server. Format: integer; default value: none. <i></p>
<dt>max_group_run</i></p>
<dd>The maximum number of jobs owned by any users in a single group that are allowed to be running from this queue at one time. This attribute is advisory to the Scheduler, it is not enforced by the server. Format: integer; default value: none. <i></p>
<dt>mom_job_sync</i></p>
<dd>Enables the &quot;job sync on MOM&quot; feature. When MOMs send a status update, and it includes a list of jobs, server will issue job deletes for any jobs that don&#8217;t actually exist. Format: boolean; default value: true. <i></p>
<dt>next_job_number</i></p>
<dd>This hidden attribute is used to allow a manager to set the value of the next job ID via qmgr. This attribute should rarely be modified. Some sites may find it useful if they need to recreate their pbs_server database (perhaps due to a format change between major TORQUE versions) and they keep a database of job information indexed by the job ID. The manager should be careful to avoid setting the value to something that would allow the next job number to conflict with a job already queued, however Torque will handle this in a sane manner: the job submission will be rejected and the next job number will be incremented. <i></p>
<dt>net_counter</i></p>
<dd>Lists the 3 numbers representing the number of connections in the last 5 seconds, 30 seconds, and 60 seconds. This is a read-only attribute. Format: string; default value: none. <i></p>
<dt>no_mail_force</i></p>
<dd>This attribute can be set by a manager via qmgr. When set true, Torque will not force mail to be sent to the user when the jobs mail_points is set to &quot;<code>n</code>&quot;. User will not receive notice of job failures or deletions. Format: boolean; default value: false. <i></p>
<dt>node_check_rate</i></p>
<dd>In OpenPBS, this was the rate at which pbs_server would poll each node. In TORQUE, nodes periodically send updates without solicitation from pbs_server; this attribute is now used as the maximum number of seconds allowed without an update before pbs_server will consider the node down. Format: integer; default value: 150 <i></p>
<dt>node_ping_rate</i></p>
<dd>Specifies the maximum interval (in seconds) between successive pings sent from the pbs_server daemon to the pbs_mom daemon to determine node/daemon health. Format: integer; default value: 300 <i></p>
<dt>node_pack</i></p>
<dd>Controls how multiple processor nodes are allocated to jobs. If this attribute is set to true, jobs will be assigned to the multiple processor nodes with the fewest free processors. This packs jobs into the fewest possible nodes leaving multiple processor nodes free for jobs which need many processors on a node. If set to false, jobs will be scattered across nodes reducing conflicts over memory between jobs. If unset, the jobs are packed on nodes in the order that the nodes are declared to the server (in the nodes file). Default value: unset &#8211; assigned to nodes as nodes in order that were declared. <i></p>
<dt>node_suffix</i></p>
<dd>Adds a domainname to node names before IP lookups. Format: string; default value: none. <i></p>
<dt>np_default</i></p>
<dd>np_default allows the administrator to unify the number of processors (np) on all nodes. The value can be dynamically changed. A value of 0 tells pbs_server to use the value of np found in the nodes file. The maximum value is 32767. Format: integer; default value: not used. <i></p>
<dt>operators</i></p>
<dd>List of users granted batch operator privileges. Format of the list is identical with <i> </i></font><font SIZE="+8"><i> above. Requires full manager privilege to set or alter. Default value: root on the local host.</p>
<dt>owner_purge</i></font><font SIZE="+9"><i></i></p>
<dd>Allows job owners to forcibly purge their own jobs from the server. This short-circuits the normal flow of events and is hightly discouraged. Default value: unset <i></p>
<dt>poll_jobs</i></p>
<dd>Controls how pbs_server will send job status requests to MOMs. When unset or false, statjob requests from clients (ie: <a href="//www.systutorials.com/docs/linux/man/1B-qstat/">qstat</a>(1B) or the scheduler) may trigger job status requests to MOMs and and must wait until the MOMs have replied; this is suitable for small to medium sized clusters. When set to true, pbs_server will send periodic job status requests; this is suitable for busy clusters with lots of jobs, lots of clients, <a href="//www.systutorials.com/docs/linux/man/1B-qstat/">qstat</a>(1B) is too slow, or your scheduler times out. (see job_stat_rate) Default value: TRUE <i></p>
<dt>query_other_jobs</i></p>
<dd>The setting of this attribute controls if general users, other than the job owner, are allowed to query the status of or select the job. Format: boolean (see acl_host_enable); Requires full manager privilege to set or alter. default value: false &#8211; users may not query or select jobs owned by other users. <i></p>
<dt>resources_available</i></p>
<dd>The list of resource and amounts available to jobs run by this server. The sum of the resource of each type used by all jobs running by this server cannot exceed the total amount listed here. Advisory to the Scheduler, not enforced by the server. Format: &quot;resources_available.resource_name=value[,&#8230;]&quot;. <i></p>
<dt>resources_cost</i></p>
<dd>The cost factors of various types of resources. These values are used in determining the order of releasing members of synchronous job sets, see the section on Synchronize Job Starts. For the most part, these value are purely arbitrary and have meaning only in the relative values between systems. The cost of the resources requested by a job is the sum of the products of the various <i>resources_cost s</i> and the amount of each resource requested by the job. It is not necessary to assign a cost for each possible resource, only those which the site wishes to be considered in synchronous job scheduling. Format: &quot;resources_cost.resource_name=value[,&#8230;]&quot;; default value: none, cost of resource is not computed. <i></p>
<dt>resources_default</i></p>
<dd>The list of default resource values that are set as limits for a job executing on this server when the job does not specify a limit, and there is no queue default. Format: &quot;resources_default.resource_name=value[,&#8230;]&quot;; default value: no limit. <i></p>
<dt>resources_max</i></p>
<dd>The maximum amount of each resource which can be requested by a single job executing on this server if there is not a resources_max valued defined for the queue in which the job resides. Format: &quot;resources_max.resource_name=value[,&#8230;]&quot;; default value: infinite usage. <i></p>
<dt>sched_version</i></p>
<dd>A string specifying the scheduler version. Schedulers should check this string when starting and not become active if the wrong string is found. This is ignored by pbs_server. <i></p>
<dt>scheduler_iteration</i></p>
<dd>The time, in seconds, between iterations of attempts by the batch server to schedule jobs. On each iteration, the server examines the available resources and runnable jobs to see if a job can be initiated. This examination also occurs whenever a running batch job terminates or a new job is placed in the queued state in an execution queue. Format: integer seconds; default value: 10 minutes, set by </font><font SIZE="+8"><code>{PBS_SCHEDULE_CYCLE}</code></font><font SIZE="+9"> in server_limits.h. <i></p>
<dt>scheduling</i></p>
<dd>Controls if the server will request job scheduling by the PBS job scheduler. If true, the scheduler will be called as required; if false, the scheduler will not be called and no job will be placed into execution unless the server is directed to do so by an operator or administrator. Setting or resetting this attribute to true results in an immediate call to the scheduler. For more information, see the section <code>Scheduler &#8211; Server Interaction</code> in the PBS Administrator Guide. Format: boolean (see acl_host_enable); default value: value of -a option when server is invoked, if -a is not specified, the value is recovered from the prior server run. If it has never been set, the value is &quot;false&quot;. <i></p>
<dt>server_name</i></p>
<dd>The name of the server which is the same as the host name. If the hostname resolves to an external IP address, then set this to a name that resolves to the internal IP. <i></p>
<dt>submit_hosts</i></p>
<dd>A list of hostnames allowed to submit jobs to this batch server regardless of ruserok(). <i></p>
<dt>system_cost</i></p>
<dd>An arbitrary value factored into the resource cost of any job managed by this server for the purpose of selecting which member of synchronous set is released first, see resources_cost and section 3.2.2, Synchronize Job Starts. [default value: none, cost of resource is not computed] <i></p>
<dt>tcp_timeout</i></p>
<dd>Specifies the pbs_server to pbs_mom TCP socket timeout in seconds. Format: integer; default value: 6.</dl>
</dl>
<p> The following attributes are read-only, they are maintained by the server and cannot be changed by a client.</p>
<dl>
<dd><i></p>
<dl>
<dt>pbs_version</i></p>
<dd>The release version number of the server. <i></p>
<dt>resources_assigned</i></p>
<dd>The total amount of certain types of resources allocated to running jobs. <i></p>
<dt>server_state</i></p>
<dd>The current state of the server:</p>
<dl>
<dd>
<dl>
<dt>Active</p>
<dd>The server is running and will invoke the job scheduler as required to schedule jobs for execution.</p>
<dt>Idle</p>
<dd>The server is running but will not invoke the job scheduler.</p>
<dt>Scheduling</p>
<dd>The server is running and there is an outstanding request to the job scheduler.</p>
<dt>Terminating</p>
<dd>The server is terminating. No additional jobs will be scheduled.</p>
<dt>Terminating, Delayed</p>
<dd>The server is terminating in delayed mode. The server will not run any new jobs and will shutdown when the last currently executing job completes.</dl>
</dl>
<dd><i></p>
<dt>state_count</i></p>
<dd>The total number of jobs managed by the server currently in each state. <i></p>
<dt>total_jobs</i></p>
<dd>The total number of jobs currently managed by the server.</dl>
</dl>
<p> </font></p>
<h2>See Also</h2>
<p>the PBS ERS, <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources/">pbs_resources</a>(7B) </p>
