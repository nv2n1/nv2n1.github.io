---
title: "pbs_job_attributes(7)"
name: "pbs_job_attributes"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pbs_job_attributes/"
description: "pbs_job_attributes – pbs job attributes"
---

<p>pbs_job_attributes &#8211; pbs job attributes</p>
<h2>Description</h2>
<p>A batch job has the following public attributes shown in the following list. The attributes marked with the section symbol &#167; are required by POSIX 1003.2d: If an attribute is unset, the indicated default value is assumed. <i></p>
<dl>
<dt>Account_Name &#167;</i><font SIZE="+1"><i></i></p>
<dd>Used for accounting on some hosts. Format: string; default value: none, not used. <i></p>
<dt>Checkpoint &#167;</i></font><font SIZE="+2"><i></i></p>
<dd>If supported by the server implementation and the host operating system, the checkpoint attribute determines when checkpointing will be performed by PBS on behalf of the job. The legal values for checkpoint are described under the <code>qalter</code> and <code>qsub</code> commands. Format: the strings &quot;n&quot;, &quot;s&quot;, &quot;c&quot;, &quot;c=mmmm&quot;; default value: &quot;u&quot;, which is unspecified. <i></p>
<dt>depend</i></font><font SIZE="+3"><i></i></p>
<dd>The type of inter-job dependencies specified by the job owner. Format: &quot;type:jobid[,jobid&#8230;]&quot;; default value: no dependencies. <i></p>
<dt>Error_Path &#167;</i></font><font SIZE="+4"><i></i></p>
<dd>The final path name for the file containing the job&#8217;s standard error stream. See the <code>qsub</code> and <code>qalter</code> command description for more detail. Format: &quot;[hostname:]pathname&quot;; default value: (job_name).e(job_number). <i></p>
<dt>Execution_Time &#167;</i></font><font SIZE="+5"><i></i></p>
<dd>The time after which the job may execute. The time is maintained in seconds since Epoch. If this time has not yet been reached, the job will not be scheduled for execution and the job is said to be in <code>wait</code> state. Format: &quot;[[CCwYY]MMDDhhmm[.ss]&quot;; default value: time 0, no delay. <i></p>
<dt>group_list &#167;</i></font><font SIZE="+6"><i></i></p>
<dd>A list of <code> which determines the group under which the job is run on a given host. [internal type: array of strings] When a job is to be placed into execution, the server will select a group name according to the following ordered set of rules:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Select the group name from the list for which the associated host name matches the name of the execution host.</p>
<dt>2.</p>
<dd>Select the group name which has no associated host name, the wild card name.</p>
<dt>3.</p>
<dd>Use the login group for the user name under which the job will be run.</dl>
</dl>
<dd>Format: &quot;group_name[@host][,group_name[@host]&#8230;]&quot;. </code><i></p>
<dt>Hold_Types &#167;</i></font><font SIZE="+7"><i></i></p>
<dd>The set of holds currently applied to the job. If the set is not null, the job will not be scheduled for execution and is said to be in the <code>hold</code> state. Note, the <code>hold</code> state takes precedence over the <code>wait</code> state. Format: string made up of the letters &#8216;u&#8217;, &#8216;s&#8217;, &#8216;o&#8217;; default value: no hold. <i></p>
<dt>Job_Name &#167;</i></font><font SIZE="+8"><i></i></p>
<dd>The name assigned to the job by the <code>qsub</code> or <code>qalter</code> command. Format: string up to 15 characters, first character must be alphabetic; default value: the base name of the job script or STDIN. <i></p>
<dt>Join_Path &#167;</i></font><font SIZE="+9"><i></i></p>
<dd>If the <i> </i></font><font SIZE="+8"><i> attribute is </i></font><font SIZE="+7"><code>{TRUE}</code></font><font SIZE="+8">, then the job&#8217;s standard error stream will be merged, inter-mixed, with the job&#8217;s standard output stream and placed in the file determined by the <i> </i></font><font SIZE="+7"><i> attribute. The </i></font><font SIZE="+6"><i> attribute is maintained, but ignored. Format: boolean, values accepted are &quot;True&quot;, &quot;TRUE&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;False&quot;, &quot;FALSE&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false.</p>
<dt>Keep_Files &#167;</i></font><font SIZE="+7"><i></i></p>
<dd>If <i> </i></font><font SIZE="+6"><i> contains the values &quot;o&quot; and/or &quot;e&quot; the corresponding streams of the batch job will be retained on the execution host upon job termination. </i></font><font SIZE="+5"><i> overrides the </i></font><font SIZE="+4"><i> and </i></font><font SIZE="+3"><i> attributes. Format: &quot;o&quot;, &quot;e&quot;, &quot;oe&quot; or &quot;eo&quot;; default value: no keep, return files to submission host.</p>
<dt>Mail_Points &#167;</i></font><font SIZE="+4"><i></i></p>
<dd>Identifies at which state changes the server will send mail about the job. Format: string made up of the letters &#8216;a&#8217; for abort, &#8216;b&#8217; for beginning, and default value: &#8216;a&#8217;, send on job abort. <i></p>
<dt>Mail_Users &#167;</i></font><font SIZE="+5"><i></i></p>
<dd>The set of users to whom mail may be sent when the job makes certain state changes. Format: &quot;user [at] host[,user [at] host]&quot;; default value: job owner only. <i></p>
<dt>Output_Path &#167;</i></font><font SIZE="+6"><i></i></p>
<dd>The final path name for the file containing the job&#8217;s standard output stream. See the <code>qsub</code> and <code>qalter</code> command description for more detail. Format: see error_path, default value: (job_name).o(job_number). <i></p>
<dt>Priority &#167;</i></font><font SIZE="+7"><i></i></p>
<dd>The job scheduling priority assigned by the user. Format: &quot;[+|-]nnnnn&quot;; default value: undefined. <i></p>
<dt>Rerunable &#167;</i></font><font SIZE="+8"><i></i></p>
<dd>The rerunable flag given by the user. Format: &quot;y&quot; or &quot;n&quot;, see Join_Path; default value: y, job is rerunable. <i></p>
<dt>Resource_List &#167;</i></font><font SIZE="+9"><i></i></p>
<dd>The list of resources required by the job. The resource list is a set of <code> strings. The meaning of and is server dependent. The value also establishes the limit of usage of that resource. If not set, the value for a resource may be determined by a queue or server default established by the administrator. Default value: no usage or no limit depending on specific resource. </code><i></p>
<dt>Shell_Path_List &#167;</i></p>
<dd>A set of absolute paths of the program to process the job&#8217;s script file. The list is in the format: &quot;path[@host][,path[@host]&#8230;]&quot;. If this is null, then the user&#8217;s login shell on the host of execution will be used. Default value: null, login shell. <i></p>
<dt>stagein</i></p>
<dd>The list of files to be staged in prior to job execution. Format: local_path [at] remote_host:remote_path <i></p>
<dt>stageout</i></p>
<dd>The list of files to be staged out after job execution. Format: local_path [at] remote_host:remote_path <i></p>
<dt>User_List &#167;</i></p>
<dd>The list of <code> which determines the user name under which the job is run on a given host. [internal type: array of strings] When a job is to be placed into execution, the server will select a user name from the list according to the following ordered set of rules:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Select the user name from the list for which the associated host name matches the name of the execution host.</p>
<dt>2.</p>
<dd>Select the user name which has no associated host name, the wild card name.</p>
<dt>3.</p>
<dd>Use the </code><i> </i></font><font SIZE="+8"><i> as the user name.</dl>
</dl>
<dd>Default value: job owner name.</p>
<dt>Variable_List &#167;</i></font><font SIZE="+9"><i></i></p>
<dd>This is the list of environment variables passed with the <i>Queue Job</i> batch request. Format: &quot;name=value[,name=value&#8230;]&quot;.</dl>
<p> The following attributes require system, manager, or operator privilege to set. They are visible to clients depending on privilege as noted. <i></p>
<dl>
<dt>comment</i></p>
<dd>An attribute for displaying comments about the job from the system. Visible to any client. Format: any string; default value: none. <i></p>
<dt>sched_hint</i></p>
<dd>This attribute is present when the job is a member of a synchronous dependency set. It is set when the hold is released on the job. The value is </font><font SIZE="+8"><code>{SYNC_SCHED_HINT_FIRST}</code></font><font SIZE="+9"> (1) when the first job of the set is released for scheduling. This is a hint that may be used by the scheduler to decrease the priority of the job. This keeps a user from attempting to game the scheduler. The attribute is set to </font><font SIZE="+8"><code>{SYNC_SCHED_HINT_OTHER}</code></font><font SIZE="+9"> (2) for all other jobs in the set as they become schedulable. This should be taken as a hint by the scheduler to increase their priority to insure they will run at the same time as the earlier scheduled jobs in the set. [This attribute is viewable only by the batch administrator.] [type: integer]</dl>
<p> The following attributes are read-only, they are established by the server and are visible to the client but cannot be set by a client. Certain ones are only visible to privileged clients (those run by the batch administrator). <i></p>
<dl>
<dt>alt_id</i></p>
<dd>For a few systems, such as Irix 6.x running Array Services, the session id is insufficient to track which processes belong to the job. Where a different identifier is required, it is recorded in this attribute. If set, it will also be recorded in the end-of-job accounting record.</p>
<dd>For Irix 6.x running Array Services, the alt_id attribute is set to the Array Session Handle (ASH) assigned to the job. <i></p>
<dt>ctime&nbsp;<wbr></i></p>
<dd>The time that the job was created. <i></p>
<dt>etime</i></p>
<dd>The time that the job became eligible to run, i.e. in a queued state while residing in an execution queue. <i></p>
<dt>exec_host</i></p>
<dd>If the job is running, this is set to the name of the host on which the job is executing. <i></p>
<dt>exit_status</i></p>
<dd>The exit status of the job. This is only set on receipt of a job obituary notice from MOM, and probably only useful if the &quot;keep_completed&quot; server attribute is set. Note that negative values are generated internally by PBS to indicate system errors and are listed as the JOB_EXEC_* defines in pbs_job.h. Positive values are returned from the user script and cannot be interpreted by PBS. <i></p>
<dt>egroup</i></p>
<dd>If the job is queued in an execution queue, this attribute is set to the group name under which the job is to be run. [This attribute is available only to the batch administrator.] <i></p>
<dt>euser</i></p>
<dd>If the job is queued in an execution queue, this attribute is set to the user name under which the job is to be run. [This attribute is available only to the batch administrator.] <i></p>
<dt>hashname</i></p>
<dd>The name used as a basename for various files, such as the job file, script file, and the standard output and error of the job. [This attribute is available only to the batch administrator.] <i></p>
<dt>interactive</i></p>
<dd>True if the job is an interactive PBS job. Format: boolean, see Join_Paths; default value: false. <i></p>
<dt>Job_Owner &#167;</i></p>
<dd>The login name on the submitting host of the user who submitted the batch job. <i></p>
<dt>job_state</i></p>
<dd>The state of the job.</p>
<dl>
<dd>
<dl>
<dt>E</p>
<dd>for exiting, the job has completed execution, with or without errors, and the batch system is doing post-execution clean-up.</p>
<dt>H</p>
<dd>for Held, one or more holds have been applied to the job.</p>
<dt>Q</p>
<dd>for Queued, the job resides in a execution or routing queue pending execution or routing. It is not in <code>held</code> or <code>waiting</code> state.</p>
<dt>R</p>
<dd>for Running, the job resides in a execution queue and has been placed into execution.</p>
<dt>S</p>
<dd>for Suspend (Job running on Unicos only), the job was executing and has been suspended. The job retains its assigned resources but does not use cpu cycle or walltime.</p>
<dt>T</p>
<dd>for Transiting, the job is in process of being routed or moved to a new destination.</p>
<dt>W</p>
<dd>for Waiting, the job is not held but the <i> </i></font><font SIZE="+8"><i> attribute contains a time which has not yet been reached.</dl>
</dl>
<dt>mtime&nbsp;<wbr></i></font><font SIZE="+9"><i></i></p>
<dd>The time that the job was last modified, changed state, or changed locations. <i></p>
<dt>qtime&nbsp;<wbr></i></p>
<dd>The time that the job entered the current queue. <i></p>
<dt>queue&nbsp;<wbr></i></p>
<dd>The name of the queue in which the job currently resides. <i></p>
<dt>queue_rank</i></p>
<dd>An ordered, non-sequential number indicating the job&#8217;s position with in the queue. This is provided as an aid to the scheduler. [This attribute is available to the batch manager only.] <i></p>
<dt>queue_type</i></p>
<dd>An identification of the the type of queue in which the job is currently residing. This is provided as an aid to the scheduler. [This attribute is available to the batch manager only.] Format: The letter E or the letter r. <i></p>
<dt>resources_used &#167;</i></p>
<dd>The amount of resources used by the job. This is provided as part of job status information if the job is running. <i></p>
<dt>server&nbsp;<wbr></i></p>
<dd>The name of the server which is currently managing the job. <i></p>
<dt>session_id</i></p>
<dd>If the job is running, this is set to the session id of the first executing task. <i></p>
<dt>substate</i></p>
<dd>A numerical indicator of the substate of the job. The substate is used by the PBS job server internally. The attribute is visible to privileged clients, such as the scheduler. Format: integer.</dl>
<p> </font></p>
<h2>See Also</h2>
<p>PBS ERS, <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources/">pbs_resources</a>(7B) </p>
