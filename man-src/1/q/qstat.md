---
title: "qstat(1)"
name: "qstat"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qstat/"
description: "qstat – show the status of xxQS_NAMExx jobs and queues"
---

<h2 class="name">NAME</h2>
<p> qstat &#8211; show the status of xxQS_NAMExx jobs and queues </p>
<h2>SYNTAX</h2>
<p> <code>qstat</code> [<code>-ext</code>] [<code>-f</code>] [<code>-F</code> [<i>resource_name</i>,&#8230;]] [<code>-g</code> <code>c</code>|<code>d</code>|<code>t</code>[<code>+</code>]] [<code>-help</code>] [<code>-j</code> [<i>job_list</i>]] [<code>-l</code> <i>resource</i>=<i>val</i>,&#8230;<i>]</i> [<code>-ne</code>] [<code>-pe</code> <i>pe_name</i>,&#8230;] [<code>-ncb</code>] [<code>-pri</code>] [<code>-q</code> <i>wc_queue_list</i>] [<code>-qs</code> <code>a</code>|<code>c</code>|<code>d</code>|<code>o</code>|<code>s</code>|<code>u</code>|<code>A</code>|<code>C</code>|<code>D</code>|<code>E</code>|<code>S</code>] [<code>-r</code>] [<code>-s</code> {<code>r</code>|<code>p</code>|<code>s</code>|<code>z</code>|<code>hu</code>|<code>ho</code>|<code>hs</code>|<code>hd</code>|<code>hj</code>|<code>ha</code>|<code>h</code>|<code>a</code>}[+]] [<code>-t</code>] [<code>-U</code> <i>user</i>,&#8230;] [<code>-u</code> <i>user</i>,&#8230;] [<code>-urg</code>] [<code>-xml</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>qstat</i> shows the current status of the available xxQS_NAMExx queues and the jobs associated with the queues. Selection options allow you to get information about specific jobs, queues or users. If multiple selections are done, a queue is only displayed if all selection criteria for a queue instance are met. Without any option <i>qstat</i> will display only a list of jobs, with no queue status information. </p>
<p> The administrator and the user may define files (see which can contain any of the options described below. A cluster-wide sge_qstat file may be placed under $xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common/sge_qstat. The user private file is searched for at the location $HOME/.sge_qstat. The home directory request file has higher precedence than the cluster global file. The command line can be used to override the flags contained in the files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-explain a</code>|<code>A</code>|<code>c</code>|<code>E</code></p>
<dd> &#8216;<code>c</code>&#8216; displays the reason for the c(onfiguration ambiguous) state of a queue instance. &#8216;<code>a</code>&#8216; shows the reason for the alarm state. Suspend alarm state reasons will be displayed by &#8216;<code>A</code>&#8216;. &#8216;<code>E</code>&#8216; displays the reason for a queue instance error state. </p>
<p> The output format for the alarm reasons is one line per reason, containing the resource value and threshold. For details about the resource value please refer to the description of the <code>Full Format</code> in section <code>OUTPUT FORMATS</code> below.</p>
<dt><code>-ext</code></p>
<dd> Displays additional information for each job related to the job ticket policy scheme (see OUTPUT FORMATS below).</p>
<dt><code>-f</code></p>
<dd> Specifies a &quot;full&quot; format display of information. The <code>-f</code> option causes summary information on all queues to be displayed along with the queued job list.</p>
<dt><code>-F</code> [ <i>resource_name</i>,&#8230; ]</p>
<dd> As for <code>-f</code>, information is displayed on all jobs as well as queues. In addition, <i>qstat</i> will present a detailed listing of the current resource availability per queue with respect to all resources (if the option argument is omitted) or with respect to those resources contained in the resource_name list. Please refer to the description of the <code>Full Format</code> in section <code>OUTPUT FORMATS</code> below for further detail.</p>
<dt><code>-g</code> {<code>c</code>|<code>d</code>|<code>t</code>}[<code>+</code>]</p>
<dd> The <code>-g</code> option allows for controlling grouping of displayed objects. </p>
<p> With <code>-g c</code> a cluster queue summary is displayed. Find more information in the section <code>OUTPUT FORMATS</code>. </p>
<p> With <code>-g d</code> array jobs are displayed verbosely in a one line per job task fashion. By default, array jobs are grouped and all tasks with the same status (for pending tasks only) are displayed in a single line. The array job task id range field in the output (see section <code>OUTPUT FORMATS</code>) specifies the corresponding set of tasks. </p>
<p> With <code>-g t</code> parallel jobs are displayed verbosely in a one line per parallel job task fashion. By default, parallel job tasks are displayed in a single line. Also with <code>-g t</code> option the function of each parallel task is displayed rather than the jobs slot amount (see section <code>OUTPUT FORMATS</code>). </p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-j</code> [<i>job_list</i>]</p>
<dd> Prints various information either (without an argument) for all pending jobs, or the jobs contained in <i>job_list</i>. The <i>job_list</i> can contain job_ids, job_names, or wildcard expressions matching jobs. </p>
<p> For jobs in E(rror) state the error reason is displayed. For jobs that could not be dispatched during in the last scheduling interval the obstacles are shown, if <code>schedd_job_info</code> in is configured accordingly. </p>
<p> For running jobs, the available information on resource utilization is shown for each task (see consumed cpu time in seconds, integral memory usage in Gbytes seconds, amount of data transferred in io operations in Gbytes, current virtual memory utilization in Mbytes, and maximum virtual memory utilization in Mbytes. This information is not available if resource utilization retrieval is not supported for the OS platform where the job is hosted. It is also not available immediately after a job has started, before a load report is received. </p>
<p> The resource usage reported is affected if <code>ACCT_RESERVED_USAGE</code> or <code>SHARETREE_RESERVED_USAGE</code> is specified in the configuration. Then the requested values are reported, not the actual usage (not multiplied by the slot count). If there is no memory request, &#8216;mem&#8217; is reported as zero, and the vmem values as &#8216;N/A&#8217;. </p>
<p> Unless <code>-ncb</code> is specified, the output contains information about a requested binding (see <code>-binding</code> of option and the changes that have been applied to the topology string (real binding) for the host where this job is running. The topology string will contain capital letters for all those cores that were not bound to the displayed job. Bound cores will be shown lowercase (e.g. &quot;SCCcCSCCcC&quot; means that core 2 on the two available sockets was bound to this job). </p>
<p> See for detailed information on the standard set of load values. </p>
<p> Note that a <code>version</code> <i>n</i> field in the output indicates <i>n</i> changes with</p>
<dt><code>-l resource</code>[<code>=value</code>],&#8230;</p>
<dd> Defines the resources required by the jobs or granted by the queues on which information is requested. Matching is performed on queues based on non-mutable resource availability information only. That means load values are always ignored except the so-called static load values listed in Consumable utilization is also ignored. The pending jobs are restricted to jobs that might run in one of the above queues. In a similar fashion also the queue-job matching bases only on non-mutable resource availability information. If there are multiple <code>-l</code> resource requests they will be concatenated by a logical AND: a queue needs to match all resources to be displayed.</p>
<dt><code>-ne</code></p>
<dd> In combination with <code>-f</code> the option suppresses the display of empty queues. This means all queues where actually no jobs are running are not displayed.</p>
<dt><code>-ncb</code></p>
<dd> In combination with <code>-ncb</code> the output of a command will omit information on any requested binding and changes that have been applied to the topology string (the real binding) for the host where the job is running. This information will disappear in combination with the parameters <code>-r</code> and <code>-j</code>. </p>
<p> Please note that this command line switch is intended to provide backward compatibility and will be removed in the next major release.</p>
<dt><code>-pe</code> <i>pe_name</i>,&#8230;</p>
<dd> Displays status information with respect to queues to which are attached to at least one of the parallel environments listed in the comma-separated option argument. Status information is displayed for jobs which are executing in one of the selected queues.</p>
<dt><code>-pri</code></p>
<dd> Displays additional information for each job related to the job priorities in general. (see OUTPUT FORMATS below).</p>
<dt><code>-q</code> <i>wc_queue_list</i></p>
<dd> Specifies a wildcard expression queue list for which job information is to be displayed. Find the definition of <i>wc_queue_list</i> in</p>
<dt><code>-qs</code> {<code>a</code>|<code>c</code>|<code>d</code>|<code>o</code>|<code>s</code>|<code>u</code>|<code>A</code>|<code>C</code>|<code>D</code>|<code>E</code>|<code>S</code>}</p>
<dd> Allows for the filtering of queue instances according to state.</p>
<dt><code>-r</code></p>
<dd> Prints extended information about the resource requirements of the displayed jobs. </p>
<p> Please refer to the <code>OUTPUT FORMATS</code> sub-section <code>Expanded Format</code> below for detailed information.</p>
<dt><code>-s</code> {<code>p</code>|<code>r</code>|<code>s</code>|<code>z</code>|<code>hu</code>|<code>ho</code>|<code>hs</code>|<code>hd</code>|<code>hj</code>|<code>ha</code>|<code>h</code>|<code>a</code>}[<code>+</code>]</p>
<dd> Prints only jobs in the specified state, any combination of states is possible. <code>-s prs</code> (pending, running, and stopped jobs) corresponds to the regular <i>qstat</i> output without <code>-s</code> at all. To show recently finished (&quot;zombie&quot;) jobs (according to the <code>finished_jobs</code> parameter) use <code>-s z</code>. (The zombie list is not spooled, and so will be lost by a qmaster re-start.) To display jobs in user/operator/system/array-dependency hold, use <code>-s</code> <code>hu</code>/<code>ho</code>/<code>hs</code>/<code>hd</code>. The <code>-s ha</code> option shows jobs which were submitted with the <code>qsub -a</code> command. <code>qstat -s hj</code> displays all jobs which are not eligible for execution unless the job has entries in the job dependency list. <code>qstat -s h</code> is an abbreviation for <code>qstat -s huhohshdhjha</code>, and <code>qstat -s a</code> is an abbreviation for <code>qstat -s psr</code> (see <code>-a</code>, <code>-hold_jid</code> and <code>-hold_jid_ad</code> options to</p>
<dt><code>-t</code></p>
<dd> Prints extended information about the controlled sub-tasks of the displayed parallel jobs. Please refer to the <code>OUTPUT FORMATS</code> sub-section <code>Reduced Format</code> below for detailed information. Sub-tasks of parallel jobs should not be confused with array job tasks (see <code>-g</code> option above and <code>-t</code> option to</p>
<dt><code>-U</code> <i>user</i>,&#8230;</p>
<dd> Displays status information with respect to queues to which the specified users have access. Status information for jobs is displayed either for those which execute in one of the selected queues or which are pending and might get scheduled to those queues in principle.</p>
<dt><code>-u</code> <i>user</i>,&#8230;</p>
<dd> Display information only on those jobs and queues associated with the users from the given user list. Queue status information is displayed if the <code>-f</code> or <code>-F</code> options are specified additionally and if the user runs jobs in those queues. </p>
<p> The string <code>&nbsp;$user</code> is a placeholder for the current username. An asterisk &quot;*&quot; can be used as username wildcard to request any users&#8217; jobs be displayed. The default value for this switch is <code>-u $user</code>.</p>
<dt><code>-urg</code></p>
<dd> Displays additional information for each job related to the job urgency policy scheme (see OUTPUT FORMATS below).</p>
<dt><code>-xml</code></p>
<dd> This option can be used with all other options and changes the output to XML. The used schemas are referenced in the XML output. The output is printed to stdout. For more detailed information, the schemas for the qstat command can be found in <i>$SGE_ROOT/util/resources/schemas/qstat</i>. </p>
<p> If the <code>-xml</code> parameter is combined with <code>-ncb</code> then the XML output does not contain tags with information about job to core binding.</dl>
<p> The following two debugging options are available only when the environment variable <code>MORE_INFO</code> is defined.</p>
<dl>
<dt><code>-dj</code></p>
<dd> Displays the full <code>global_job_list</code> internal state.</p>
<dt><code>-dq</code></p>
<dd> Displays the full <code>global_queue_list</code> internal state.</dl>
<h2>OUTPUT FORMATS</h2>
<p> Depending on the presence or absence of the <code>-explain</code>, <code>-f</code>, <code>-F</code>, or <code>-qs</code> and <code>-r</code> and <code>-t</code> option three output formats need to be differentiated. </p>
<p> The <code>-ext</code> and <code>-urg</code> options may be used to display additional information for each job.</p>
<h3><code>Cluster Queue Format (with -g c)</code></h3>
<p> Following the header line a section for each cluster queue is provided. When queue instances selection are applied (-l -pe, -q, -U) the cluster format contains only cluster queues of the corresponding queue instances.</p>
<dl>
<dt>&bull;</p>
<dd> the cluster queue name.</p>
<dt>&bull;</p>
<dd> an average of the normalized load average of all queue hosts. In order to reflect each hosts different significance the number of configured slots is used as a weighting factor when determining cluster queue load. Please note that only hosts with an np_load_value are considered for this value. When queue selection is applied, only data about selected queues is considered in this formula. If the load value is not available at any of the hosts &#8216;-NA-&#8216; is printed instead of the value from the complex attribute definition.</p>
<dt>&bull;</p>
<dd> the number of currently used slots.</p>
<dt>&bull;</p>
<dd> the number of slots reserved by advance reservation (not resource reservation).</p>
<dt>&bull;</p>
<dd> the number of currently available slots.</p>
<dt>&bull;</p>
<dd> the total number of slots.</p>
<dt>&bull;</p>
<dd> the number of slots which is in at least one of the states &#8216;aoACDS&#8217; and in none of the states &#8216;cdsuE&#8217;</p>
<dt>&bull;</p>
<dd> the number of slots which are in one of these states or in any combination of them: &#8216;cdsuE&#8217;</p>
<dt>&bull;</p>
<dd> the <code>-g c</code> option can be used in combination with <code>-ext</code>. In this case, additional columns are added to the output. Each column contains the slot count for one of the available queue states.</dl>
<h3><code>Reduced Format (without -f, -F, and -qs)</code></h3>
<p> Following the header line a line is printed for each job consisting of</p>
<dl>
<dt>&bull;</p>
<dd> the job ID.</p>
<dt>&bull;</p>
<dd> the priority of the job determining its position in the pending jobs list. The priority value is determined dynamically based on ticket and urgency policy set-up (see also</p>
<dt>&bull;</p>
<dd> the name of the job.</p>
<dt>&bull;</p>
<dd> the user name of the job owner.</p>
<dt>&bull;</p>
<dd> the status of the job &#8211; a combination of <code>d</code>(eletion), <code>E</code>(rror), <code>h</code>(old), <code>q</code>(ueued), <code>r</code>(unning), <code>R</code>(estarted), <code>s</code>(uspended), <code>S(uspended),</code> <code>t</code>(ransfering), <code>T</code>(hreshold), <code>w</code>(aiting), or <code>z</code>(ombie). </p>
<p> The state <code>d</code>(eletion) indicates that has been used to initiate job deletion. The states <code>t</code>(ransfering) and <code>r</code>(unning) indicate that a job is about to be executed or is already executing, whereas the states <code>s</code>(uspended), <code>S</code>(uspended) and <code>T</code>(hreshold) show that an already running jobs has been suspended. The <code>s</code>(uspended) state is caused by suspending the job via the command, the <code>S</code>(uspended) state indicates that the queue containing the job is suspended and therefore the job is also suspended and the <code>T</code>(hreshold) state shows that at least one suspend threshold of the corresponding queue was exceeded (see and that the job has been suspended as a consequence. The state <code>R</code>(estarted) indicates that the job was restarted. This can be caused by a job migration or for one of the reasons described in the <code>-r</code> section of </p>
<p> The states <code>q</code>(ueued)/<code>w</code>(aiting) and <code>h</code>(old) only appear for pending jobs. Pending, unheld jobs are displayed as <code>qw</code>. The <code>h</code>(old) state indicates that a job currently is not eligible for execution due to a hold state assigned to it via or the <code>-h</code> option, or that the job is waiting for completion of the jobs for which job dependencies have been assigned to it job via the <code>-hold_jid</code> or <code>-hold_jid_ad</code> options of or </p>
<p> The state <code>z</code>(ombie) appears for finished jobs when the <code>-s z</code> option is used. </p>
<p> The state <code>E</code>(rror) appears for pending jobs that couldn&#8217;t be started due to job properties. The reason for the job error is shown by the <code>-j</code>&nbsp;<i>job_list</i> option. </p>
<p> See also</p>
<dt>&bull;</p>
<dd> the submission or start time and date of the job.</p>
<dt>&bull;</p>
<dd> the queue the job is assigned to (for running or suspended jobs only).</p>
<dt>&bull;</p>
<dd> the number of job slots or the function of parallel job tasks if <code>-g t</code> is specified. </p>
<p> Without <code>-g t</code> option the total number of slots occupied or requested by the job is displayed. For pending parallel jobs with a PE slot range request, the assumed future slot allocation is displayed. With <code>-g t</code> option the function of the running jobs (MASTER or SLAVE &#8211; the latter for parallel jobs only) is displayed.</p>
<dt>&bull;</p>
<dd> the array job task id. Will be empty for non-array jobs. See the <code>-t</code> option to and the <code>-g</code> above for additional information.</dl>
<p> If the <code>-t</code> option is supplied, each status line always contains parallel job task information as if <code>-g t</code> were specified and each line contains the following parallel job subtask information:</p>
<dl>
<dt>&bull;</p>
<dd> the parallel task ID (do not confuse parallel tasks with array job tasks),</p>
<dt>&bull;</p>
<dd> the status of the parallel task &#8211; one of r(unning), R(estarted), s(uspended), S(uspended), T(hreshold), w(aiting), h(old), or x(exited).</p>
<dt>&bull;</p>
<dd> the cpu, memory, and I/O usage,</p>
<dt>&bull;</p>
<dd> the exit status of the parallel task,</p>
<dt>&bull;</p>
<dd> and the failure code and message for the parallel task.</dl>
<h3><code>Full Format (with -f and -F)</code></h3>
<p> Following the header line a section for each queue separated by a horizontal line is provided. For each queue the information printed consists of</p>
<dl>
<dt>&bull;</p>
<dd> the queue name;</p>
<dt>&bull;</p>
<dd> the queue type &#8211; one of <code>B</code>(atch), <code>I</code>(nteractive), <code>C</code>(heckpointing), <code>P</code>(arallel), combinations thereof, or <code>N</code>(one) (&quot;Type&quot; in the case of C and P, just means there is an entry in its ckpt_list or pe_list respectively;)</p>
<dt>&bull;</p>
<dd> the number of used and available job slots;</p>
<dt>&bull;</p>
<dd> the load average of the queue host or another load value &#8211; see SGE_LOAD_AVG in the ENVIRONMENT VARIABLES section below;</p>
<dt>&bull;</p>
<dd> the architecture of the queue host;</p>
<dt>&bull;</p>
<dd> the state of the queue &#8211; one of <code>u</code>(nknown), <code>a</code>(larm), <code>A</code>(larm), <code>C</code>(alendar suspended), <code>s</code>(uspended), <code>S</code>(ubordinate), <code>d</code>(isabled), <code>D</code>(isabled), <code>E</code>(rror), <code>c</code>(configuration ambiguous), <code>o</code>(rphaned), <code>P</code>(reempted), or some combination thereof.</dl>
<p> If the state is <code>u</code>, the corresponding cannot be contacted. </p>
<p> If the state is <code>a</code>(larm), at least one of the load thresholds defined in the <i>load_thresholds</i> list of the queue configuration (see is currently exceeded, which prevents scheduling further jobs to that queue. The state <code>A</code>(larm) indicates that at least one of the suspend thresholds of the queue (see is currently exceeded. This will result in jobs running in that queue being successively suspended until no threshold is violated. </p>
<p> The states <code>s</code>(uspended) And <code>d</code>(isabled) can be assigned to queues and released via the command. Suspending a queue will cause all jobs executing in that queue to be suspended. </p>
<p> The states <code>D</code>(isabled) And <code>C</code>(alendar suspended) indicate that the queue has been disabled, or suspended automatically via the xxQS_NAMExx calendar facility (see while the <code>S</code>(ubordinate) state indicates that the queue has been suspended via subordination to another queue (see for details). When suspending a queue (regardless of the cause) all jobs executing in that queue are suspended too. </p>
<p> The state <code>P</code>(reempted) indicates that the queue has been disabled via slotwise subordination to another queue, preventing it getting jobs which would simply be suspended. </p>
<p> An <code>E</code>(rror) state is displayed for a queue for various reasons such as failing to find executables or directories. Please check the error logfile of that for the reason, indicating how to resolve the problem. Please enable the queue afterwards via the <code>-c</code> option of the command manually. </p>
<p> If the <code>c</code>(onfiguration<code>ambiguous)</code> state is displayed for a queue instance, the configuration specified for this queue instance in is ambiguous. This state is cleared when the configuration becomes unambiguous again. This state prevents further jobs from being scheduled to that queue instance. Detailed reasons why a queue instance entered the <code>c</code> state can be found in the messages file and are shown by the <code>-explain</code> switch. For queue instances in this state the cluster queue&#8217;s default settings are used for the ambiguous attribute. </p>
<p> If an <code>o</code>(rphaned) state is displayed for a queue instance, it indicates that the queue instance is no longer demanded by the current cluster queue configuration or the host group configuration. The queue instance is kept because jobs which have not yet finished are still associated with it, and it will vanish from <i>qstat</i> output when these jobs have finished. To quicken vanishing of an orphaned queue instance, associated job(s) can be deleted using A queue instance in the orphaned state can be revived by changing the cluster queue configuration to cover that queue instance. This state prevents scheduling further jobs to that queue instance. </p>
<p> If the <code>-F</code> option was used, resource availability information is printed following the queue status line. For each resource (as selected in an option argument to <code>-F</code>, or for all resources if the option argument was omitted) a single line is displayed with the following format:</p>
<dl>
<dt>&bull;</p>
<dd> a one letter specifier indicating whether the current resource availability value was dominated by either<br />
 &#8216;<code>g</code>&#8216; &#8211; a cluster global,<br />
 &#8216;<code>h</code>&#8216; &#8211; a host total or<br />
 &#8216;<code>q</code>&#8216; &#8211; a queue related resource consumption.</p>
<dt>&bull;</p>
<dd> a second one letter specifier indicating the source for the current resource availability value, one of<br />
 &#8216;<code>l</code>&#8216; &#8211; a load value reported for the resource,<br />
 &#8216;<code>L</code>&#8216; &#8211; a load value for the resource after administrator defined load scaling has been applied,<br />
 &#8216;<code>c</code>&#8216; &#8211; availability derived from the consumable resources facility (see<br />
 &#8216;<code>f</code>&#8216; &#8211; a fixed availability definition derived from a non-consumable complex attribute or a fixed resource limit.</p>
<dt>&bull;</p>
<dd> after a colon the name of the resource on which information is displayed.</p>
<dt>&bull;</p>
<dd> after an equal sign the current resource availability value.</dl>
<p> The displayed availability values and the sources from which they derive are always the minimum values of all possible combinations. Hence, for example, a line of the form &quot;qf:h_vmem=4G&quot; indicates that a queue currently has a maximum availability in virtual memory of 4 Gigabyte, where this value is a fixed value (e.g. a resource limit in the queue configuration) and it is queue dominated, i.e. the host in total may have more virtual memory available than this, but the queue doesn&#8217;t allow for more. Contrarily a line &quot;hl:h_vmem=4G&quot; would also indicate an upper bound of 4 Gigabyte virtual memory availability, but the limit would be derived from a load value currently reported for the host. So while the queue might allow for jobs with higher virtual memory requirements, the host on which this particular queue resides currently only has 4 Gigabyte available. </p>
<p> If the <code>-explain</code> option was used with the character &#8216;a&#8217; or &#8216;A&#8217;, information about resources is displayed, that violate load or suspend thresholds.<br />
 The same format as with the <code>-F</code> option is used with following extensions:</p>
<dl>
<dt>&bull;</p>
<dd> the line starts with the keyword &#8216;alarm&#8217; </p>
<dt>&bull;</p>
<dd> appended to the resource value is the type and value of the appropriate threshold</dl>
<p> After the queue status line (in case of <code>-f</code>) or the resource availability information (in case of <code>-F</code>) a single line is printed for each job running currently in this queue. Each job status line contains</p>
<dl>
<dt>&bull;</p>
<dd> the job ID,</p>
<dt>&bull;</p>
<dd> the priority of the job determining its position in the pending jobs list. The priority value is determined dynamically based on ticket and urgency policy set-up (see also</p>
<dt>&bull;</p>
<dd> the job name,</p>
<dt>&bull;</p>
<dd> the job owner name,</p>
<dt>&bull;</p>
<dd> the status of the job; see the <code>Reduced Format</code> section for information,</p>
<dt>&bull;</p>
<dd> the submission or start time and date of the job.</p>
<dt>&bull;</p>
<dd> the number of job slots or the function of parallel job tasks if <code>-g t</code> is specified. </p>
<p> Without <code>-g t</code> option the number of slots occupied per queue resp. requested by the job is displayed. For pending parallel jobs with a PE slot range request, the assumed future slot allocation is displayed. With <code>-g t</code> option the function of the running jobs (MASTER or SLAVE &#8211; the latter for parallel jobs only) is displayed.</dl>
<p> If the <code>-t</code> option is supplied, each job status line also contains</p>
<dl>
<dt>&bull;</p>
<dd> the task ID,</p>
<dt>&bull;</p>
<dd> the status of the task &#8211; one of <code>r</code>(unning), <code>R</code>(estarted), <code>s</code>(uspended), <code>S</code>(uspended), <code>T</code>(hreshold), <code>w</code>(aiting), <code>h</code>(old), or (e)<code>x</code>(xited) (see the <code>Reduced Format</code> section for detailed information),</p>
<dt>&bull;</p>
<dd> the cpu, memory, and I/O usage,</p>
<dt>&bull;</p>
<dd> the exit status of the task,</p>
<dt>&bull;</p>
<dd> and the failure code and message for the task.</dl>
<p> Following the list of queue sections a <i>PENDING JOBS</i> list may be printed in case jobs are waiting to be assigned to a queue. A status line for each waiting job is displayed similar to the one for the running jobs. The differences are that the status for the jobs is w(aiting) or h(old), that the submit time and date is shown instead of the start time and that no function is displayed for the jobs. </p>
<p> In very rare cases, e.g. if starts up from an inconsistent state in the job or queue spool files or if the <code>clean queue</code> (<code>-cq</code>) option of is used, <i>qstat</i> cannot assign jobs to either the running or pending jobs section of the output. In this case as job status inconsistency (e.g. a job has a running status but is not assigned to a queue) has been detected. Such jobs are printed in an <i>ERROR JOBS</i> section at the very end of the output. The ERROR JOBS section should disappear upon restart of Please contact your xxQS_NAMExx support representative if you feel uncertain about the cause or effects of such jobs.</p>
<h3><code>Expanded Format (with -r)</code></h3>
<p> If the <code>-r</code> option was specified together with <i>qstat</i>, the following information for each displayed job is printed (a single line for each of the following job characteristics):</p>
<dl>
<dt>&bull;</p>
<dd> The job and master queue name.</p>
<dt>&bull;</p>
<dd> The hard and soft resource requirements of the job as specified with the <code>-l</code> option. The per-resource addend when determining the job&#8217;s urgency contribution value is printed (see also</p>
<dt>&bull;</p>
<dd> The requested parallel environment including the desired queue slot range (see <code>-pe</code> option of</p>
<dt>&bull;</p>
<dd> The requested checkpointing environment of the job (see the <code>-ckpt</code> option).</p>
<dt>&bull;</p>
<dd> In case of running jobs, the granted parallel environment with the granted number of queue slots.</p>
<dt>&bull;</p>
<dd> The requested job binding parameters.</dl>
<h3><code>Enhanced Output (with -ext)</code></h3>
<p> For each job the following additional items are displayed:</p>
<dl>
<dt><code>ntckts</code></p>
<dd> The total number of tickets in normalized fashion.</p>
<dt><code>project</code></p>
<dd> The project to which the job is assigned as specified in the <code>-P</code> option.</p>
<dt><code>department</code></p>
<dd> The department, to which the user belongs (use the <code>-sul</code> and <code>-su</code> options of to display the current department definitions).</p>
<dt><code>cpu</code></p>
<dd> The current accumulated CPU usage of the job in seconds. See concerning this and the next two items.</p>
<dt><code>mem</code></p>
<dd> The current accumulated memory usage of the job in Gbytes seconds.</p>
<dt><code>io</code></p>
<dd> The current accumulated IO usage of the job.</p>
<dt><code>tckts</code></p>
<dd> The total number of tickets assigned to the job currently</p>
<dt><code>ovrts</code></p>
<dd> The override tickets as assigned by the <code>-ot</code> option of</p>
<dt><code>otckt</code></p>
<dd> The override portion of the total number of tickets assigned to the job currently</p>
<dt><code>ftckt</code></p>
<dd> The functional portion of the total number of tickets assigned to the job currently</p>
<dt><code>stckt</code></p>
<dd> The share portion of the total number of tickets assigned to the job currently</p>
<dt><code>share</code></p>
<dd> The share of the total system to which the job is entitled currently.</dl>
<h3><code>Enhanced Output (with -urg)</code></h3>
<p> For each job the following additional urgency policy related items are displayed (see also</p>
<dl>
<dt><code>nurg</code></p>
<dd> The jobs total urgency value in normalized fashion.</p>
<dt><code>urg</code></p>
<dd> The jobs total urgency value.</p>
<dt><code>rrcontr</code></p>
<dd> The urgency value contribution that reflects the urgency that is related to the jobs overall resource requirement.</p>
<dt><code>wtcontr</code></p>
<dd> The urgency value contribution that reflects the urgency related to the jobs waiting time.</p>
<dt><code>dlcontr</code></p>
<dd> The urgency value contribution that reflects the urgency related to the jobs deadline initiation time.</p>
<dt><code>deadline</code></p>
<dd> The deadline initiation time of the job as specified with the <code>-dl</code> option.</dl>
<h3><code>Enhanced Output (with -pri)</code></h3>
<p> For each job, the following additional job priority related items are displayed (see also</p>
<dl>
<dt><code>nurg</code></p>
<dd> The job&#8217;s total urgency value in normalized fashion.</p>
<dt><code>npprior</code></p>
<dd> The job&#8217;s <code>-p</code> priority in normalized fashion.</p>
<dt><code>ntckts</code></p>
<dd> The job&#8217;s ticket amount in normalized fashion.</p>
<dt><code>ppri</code></p>
<dd> The job&#8217;s <code>-p</code> priority as specified by the user.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>MORE_INFO</code></p>
<dd> If defined, enable the debugging <code>-dj</code> and <code>-dq</code> options, as above.</p>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qstat</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>SGE_LONG_QNAMES</code></p>
<dd> Qstat displays queue names up to 30 characters. If that is too much or not enough, one can set a custom length with this variable. The minimum display length is 10 characters. If one does not know the best display length, one can set SGE_LONG_QNAMES to -1 and qstat will figure out the best length.</p>
<dt><code>SGE_LOAD_AVG</code></p>
<dd> Specify a load parameter (see to use instead of <code>load_avg</code> when displaying/selecting load values.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/xxqs_name_sxx_qstat</i>
                          cluster qstat default options
<i>$HOME/.xxqs_name_sxx_qstat</i>
                          user qstat default options
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbAN">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAO">FILES</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd></dl>
