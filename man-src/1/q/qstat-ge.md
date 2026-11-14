---
title: "qstat-ge(1)"
name: "qstat-ge"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qstat-ge/"
description: "qstat – show the status of Grid Engine jobs and queues"
---

<h2>NAME</h2>
<p> qstat &#8211; show the status of Grid Engine jobs and queues</p>
<h2>SYNTAX</h2>
<p> <code>qstat</code> [ <code>-ext</code> ] [ <code>-f</code> ] [ <code>-F</code> [<code>resource_name,&#8230;</code>] ] [ <code>-g {c|d|t}[+]</code> ] [ <code>-help</code> ] [ <code>-j [job_list]</code> ] [ <code>-l resource=val,&#8230;</code> ] [ <code>-ne</code> ] [ <code>-pe pe_name,&#8230;</code> ] [ <code>-pri </code> ] [ <code>-q wc_queue_list</code> ] [ <code>-qs {a|c|d|o|s|u|A|C|D|E|S}</code> ] [ <code>-r</code> ] [ <code>-s {r|p|s|z|hu|ho|hs|hd|hj|ha|h|a}[+]</code> ] [ <code>-t</code> ] [ <code>-U user,&#8230;</code> ] [ <code>-u user,&#8230;</code> ] [ <code>-urg</code> ] [ <code>-xml</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>qstat</i> shows the current status of the available Grid Engine queues and the jobs associated with the queues. Selection options allow you to get information about specific jobs, queues or users. If multiple selections are done a queue is only displayed if all selection criteria for a queue instance are met. Without any option <i>qstat</i> will display only a list of jobs with no queue status information. </p>
<p> The administrator and the user may define files (see which can contain any of the options described below. A cluster-wide sge_qstat file may be placed under $GE_ROOT/$GE_CELL/common/sge_qstat The user private file is searched at the location $HOME/.sge_qstat. The home directory request file has the highest precedence over the cluster global file. Command line can be used to override the flags contained in the files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-explain a|A|c|E</code></p>
<dd> &#8216;c&#8217; displays the reason for the c(onfiguration ambiguous) state of a queue instance. &#8216;a&#8217; shows the reason for the alarm state. Suspend alarm state reasons will be displayed by &#8216;A&#8217;. &#8216;E&#8217; displays the reason for a queue instance error state. </p>
<p> The output format for the alarm reasons is one line per reason containing the resource value and threshold. For details about the resource value please refer to the description of the <code>Full Format</code> in section <code>OUTPUT FORMATS</code> below.</p>
<dt><code>-ext</code></p>
<dd> Displays additional information for each job related to the job ticket policy scheme (see OUTPUT FORMATS below).</p>
<dt><code>-f</code></p>
<dd> Specifies a &quot;full&quot; format display of information. The <code>-f</code> option causes summary information on all queues to be displayed along with the queued job list.</p>
<dt><code>-F</code> [ <code>resource_name,&#8230;</code> ]</p>
<dd> Like in the case of <code>-f</code> information is displayed on all jobs as well as queues. In addition, <i>qstat</i> will present a detailed listing of the current resource availability per queue with respect to all resources (if the option argument is omitted) or with respect to those resources contained in the resource_name list. Please refer to the description of the <code>Full Format</code> in section <code>OUTPUT FORMATS</code> below for further detail.</p>
<dt><code>-g {c|d|t}[+]</code></p>
<dd> The <code>-g</code> option allows for controlling grouping of displayed objects. </p>
<p> With <code>-g c</code> a cluster queue summary is displayed. Find more information in the section <code>OUTPUT FORMATS</code>. </p>
<p> With <code>-g d</code> array jobs are displayed verbosely in a one line per job task fashion. By default, array jobs are grouped and all tasks with the same status (for pending tasks only) are displayed in a single line. The array job task id range field in the output (see section <code>OUTPUT FORMATS</code>) specifies the corresponding set of tasks. </p>
<p> With <code>-g t</code> parallel jobs are displayed verbosely in a one line per parallel job task fashion. By default, parallel job tasks are displayed in a single line. Also with <code>-g t</code> option the function of each parallel task is displayed rather than the jobs slot amount (see section <code>OUTPUT FORMATS</code>). </p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-j [job_list]</code></p>
<dd> Prints either for all pending jobs or the jobs contained in job_list various information. The job_list can contain job_ids, job_names, or wildcard expression </p>
<p> For jobs in E(rror) state the error reason is displayed. For jobs that could not be dispatched during in the last scheduling interval the obstacles are shown, if &#8216;schedd_job_info&#8217; in is configured accordingly. </p>
<p> For running jobs available information on resource utilization is shown about consumed cpu time in seconds, integral memory usage in Gbytes seconds, amount of data transferred in io operations, current virtual memory utilization in Mbytes, and maximum virtual memory utilization in Mbytes. This information is not available if resource utilization retrieval is not supported for the OS platform where the job is hosted.</p>
<dt><code>-l resource</code>[<code>=value</code>],&#8230;</p>
<dd> Defines the resources required by the jobs or granted by the queues on which information is requested. Matching is performed on queues based on non-mutable resource availability information only. That means load values are always ignored except the so-called static load values (i.e. &quot;arch&quot;, &quot;num_proc&quot;, &quot;mem_total&quot;, &quot;swap_total&quot; and &quot;virtual_total&quot;). Consumable utilization is also ignored. The pending jobs are restricted to jobs that might run in one of the above queues. In a similar fashion also the queue-job matching bases only on non-mutable resource availability information. If there are multiple -l resource requests they will be concatenated by a logical AND: a queue needs to match all resources to be displayed.</p>
<dt><code>-ne</code></p>
<dd> In combination with <code>-f</code> the option suppresses the display of empty queues. This means all queues where actually no jobs are running are not displayed.</p>
<dt><code>-pe pe_name,&#8230;</code></p>
<dd> Displays status information with respect to queues which are attached to at least one of the parallel environments enlisted in the comma separated option argument. Status information for jobs is displayed either for those which execute in one of the selected queues or which are pending and might get scheduled to those queues in principle.</p>
<dt><code>-pri</code></p>
<dd> Displays additional information for each job related to the job priorities in general. (see OUTPUT FORMATS below).</p>
<dt><code>-q wc_queue_list</code></p>
<dd> Specifies a wildcard expression queue list to which job information is to be displayed. Find the definition of <code>wc_queue_list</code> in</p>
<dt><code>-qs {a|c|d|o|s|u|A|C|D|E|S}</code></p>
<dd> Allows for the filtering of queue instances according to state.</p>
<dt><code>-r</code></p>
<dd> Prints extended information about the resource requirements of the displayed jobs. Please refer to the <code>OUTPUT FORMATS</code> sub-section <code>Expanded Format</code> below for detailed information.</p>
<dt><code>-s {p|r|s|z|hu|ho|hs|hd|hj|ha|h|a}[+]</code></p>
<dd>
<p> Prints only jobs in the specified state, any combination of states is possible. <code>-s prs</code> corresponds to the regular <i>qstat</i> output without <code>-s</code> at all. To show recently finished jobs, use <code>-s z</code>. To display jobs in user/operator/system/array-dependency hold, use the <code>-s hu/ho/hs/hd</code> option. The <code>-s ha</code> option shows jobs which where submitted with the <i>qsub </i> <code>-a</code> command. <i>qstat </i> <code>-s hj</code> displays all jobs which are not eligible for execution unless the job has entries in the job dependency list. <i>qstat </i> <code>-s h</code> is an abbreviation for <i>qstat </i> <code>-s huhohshdhjha</code> and <i>qstat </i> <code>-s a</code> is an abbreviation for <i>qstat </i> <code>-s psr</code> (see <code>-a</code>, <code>-hold_jid</code> and <code>-hold_jid_ad</code> options to</p>
<dt><code>-t</code></p>
<dd> Prints extended information about the controlled sub-tasks of the displayed parallel jobs. Please refer to the <code>OUTPUT FORMATS</code> sub-section <code>Reduced Format</code> below for detailed information. Sub-tasks of parallel jobs should not be confused with array job tasks (see <code>-g</code> option above and <code>-t</code> option to</p>
<dt><code>-U user,&#8230;</code></p>
<dd> Displays status information with respect to queues to which the specified users have access. Status information for jobs is displayed either for those which execute in one of the selected queues or which are pending and might get scheduled to those queues in principle.</p>
<dt><code>-u user,&#8230;</code></p>
<dd> Display information only on those jobs and queues being associated with the users from the given user list. Queue status information is displayed if the <code>-f</code> or <code>-F</code> options are specified additionally and if the user runs jobs in those queues. </p>
<p> The string <code>&nbsp;<wbr>$user</code> is a placeholder for the current username. An asterisk &quot;*&quot; can be used as username wildcard to request any users&#8217; jobs be displayed. The default value for this switch is <code>-u $user</code>.</p>
<dt><code>-urg</code></p>
<dd> Displays additional information for each job related to the job urgency policy scheme (see OUTPUT FORMATS below).</p>
<dt><code>-xml</code></p>
<dd> This option can be used with all other options and changes the output to XML. The used schemas are referenced in the XML output. The output is printed to stdout. For more detailed information, the schemas for the qstat command can be found in $SGE_ROOT/util/resources/schemas/qstat
</dl>
<h2>OUTPUT FORMATS</h2>
<p> Depending on the presence or absence of the <code>-explain</code>, <code>-f</code>, <code>-F</code>, or <code>-qs</code> and <code>-r</code> and <code>-t</code> option three output formats need to be differentiated. </p>
<p> The <code>-ext</code> and <code>-urg</code> options may be used to display additional information for each job.</p>
<h3><code>Cluster Queue Format (with -g c)</code></h3>
<p> Following the header line a section for each cluster queue is provided. When queue instances selection are applied (-l -pe, -q, -U) the cluster format contains only cluster queues of the corresponding queue instances.</p>
<dl>
<dt>*</p>
<dd> the cluster queue name.</p>
<dt>*</p>
<dd> an average of the normalized load average of all queue hosts. In order to reflect each hosts different significance the number of configured slots is used as a weighting factor when determining cluster queue load. Please note that only hosts with a np_load_value are considered for this value. When queue selection is applied only data about selected queues is considered in this formula. If the load value is not available at any of the hosts &#8216;-NA-&#8216; is printed instead of the value from the complex attribute definition.</p>
<dt>*</p>
<dd> the number of currently used slots.</p>
<dt>*</p>
<dd> the number of slots reserved in advance.</p>
<dt>*</p>
<dd> the number of currently available slots.</p>
<dt>*</p>
<dd> the total number of slots.</p>
<dt>*</p>
<dd> the number of slots which is in at least one of the states &#8216;aoACDS&#8217; and in none of the states &#8216;cdsuE&#8217;</p>
<dt>*</p>
<dd> the number of slots which are in one of these states or in any combination of them: &#8216;cdsuE&#8217;</p>
<dt>*</p>
<dd> the <code>-g c</code> option can be used in combination with <code>-ext</code>. In this case, additional columns are added to the output. Each column contains the slot count for one of the available queue states.</dl>
<h3><code>Reduced Format (without -f, -F, and -qs)</code></h3>
<p> Following the header line a line is printed for each job consisting of</p>
<dl>
<dt>*</p>
<dd> the job ID.</p>
<dt>*</p>
<dd> the priority of the job determining its position in the pending jobs list. The priority value is determined dynamically based on ticket and urgency policy set-up (see also ).</p>
<dt>*</p>
<dd> the name of the job.</p>
<dt>*</p>
<dd> the user name of the job owner.</p>
<dt>*</p>
<dd> the status of the job &#8211; one of d(eletion), E(rror), h(old), r(unning), R(estarted), s(uspended), S(uspended), t(ransfering), T(hreshold) or w(aiting). </p>
<p> The state d(eletion) indicates that a has been used to initiate job deletion. The states t(ransfering) and r(unning) indicate that a job is about to be executed or is already executing, whereas the states s(uspended), S(uspended) and T(hreshold) show that an already running jobs has been suspended. The s(uspended) state is caused by suspending the job via the command, the S(uspended) state indicates that the queue containing the job is suspended and therefore the job is also suspended and the T(hreshold) state shows that at least one suspend threshold of the corresponding queue was exceeded (see and that the job has been suspended as a consequence. The state R(estarted) indicates that the job was restarted. This can be caused by a job migration or because of one of the reasons described in the -r section of the command. </p>
<p> The states w(aiting) and h(old) only appear for pending jobs. The h(old) state indicates that a job currently is not eligible for execution due to a hold state assigned to it via or the <code>-h</code> option or that the job is waiting for completion of the jobs to which job dependencies have been assigned to the job via the <code>-hold_jid</code> or <code>-hold_jid-ad</code> options of or </p>
<p> The state E(rror) appears for pending jobs that couldn&#8217;t be started due to job properties. The reason for the job error is shown by the <code>-j job_list</code> option.</p>
<dt>*</p>
<dd> the submission or start time and date of the job.</p>
<dt>*</p>
<dd> the queue the job is assigned to (for running or suspended jobs only).</p>
<dt>*</p>
<dd> the number of job slots or the function of parallel job tasks if <code>-g t</code> is specified. </p>
<p> Without <code>-g t</code> option the total number of slots occupied resp. requested by the job is displayed. For pending parallel jobs with a PE slot range request, the assumed future slot allocation is displayed. With <code>-g t</code> option the function of the running jobs (MASTER or SLAVE &#8211; the latter for parallel jobs only) is displayed.</p>
<dt>*</p>
<dd> the array job task id. Will be empty for non-array jobs. See the <code>-t</code> option to and the <code>-g</code> above for additional information.</dl>
<p> If the <code>-t</code> option is supplied, each status line always contains parallel job task information as if <code>-g t</code> were specified and each line contains the following parallel job subtask information:</p>
<dl>
<dt>*</p>
<dd> the parallel task ID (do not confuse parallel tasks with array job tasks),</p>
<dt>*</p>
<dd> the status of the parallel task &#8211; one of r(unning), R(estarted), s(uspended), S(uspended), T(hreshold), w(aiting), h(old), or x(exited).</p>
<dt>*</p>
<dd> the cpu, memory, and I/O usage,</p>
<dt>*</p>
<dd> the exit status of the parallel task,</p>
<dt>*</p>
<dd> and the failure code and message for the parallel task.</dl>
<h3><code>Full Format (with -f and -F)</code></h3>
<p> Following the header line a section for each queue separated by a horizontal line is provided. For each queue the information printed consists of</p>
<dl>
<dt>*</p>
<dd> the queue name,</p>
<dt>*</p>
<dd> the queue type &#8211; one of B(atch), I(nteractive), C(heckpointing), P(arallel), T(ransfer) or combinations thereof or N(one),</p>
<dt>*</p>
<dd> the number of used and available job slots,</p>
<dt>*</p>
<dd> the load average of the queue host,</p>
<dt>*</p>
<dd> the architecture of the queue host and</p>
<dt>*</p>
<dd> the state of the queue &#8211; one of u(nknown) if the corresponding cannot be contacted, a(larm), A(larm), C(alendar suspended), s(uspended), S(ubordinate), d(isabled), D(isabled), E(rror) or combinations thereof.</dl>
<p> If the state is a(larm) at least on of the load thresholds defined in the <i>load_thresholds</i> list of the queue configuration (see is currently exceeded, which prevents from scheduling further jobs to that queue. </p>
<p> As opposed to this, the state A(larm) indicates that at least one of the suspend thresholds of the queue (see is currently exceeded. This will result in jobs running in that queue being successively suspended until no threshold is violated. </p>
<p> The states s(uspended) and d(isabled) can be assigned to queues and released via the command. Suspending a queue will cause all jobs executing in that queue to be suspended. </p>
<p> The states D(isabled) and C(alendar suspended) indicate that the queue has been disabled or suspended automatically via the calendar facility of Grid Engine (see while the S(ubordinate) state indicates, that the queue has been suspend via subordination to another queue (see for details). When suspending a queue (regardless of the cause) all jobs executing in that queue are suspended too. </p>
<p> If an E(rror) state is displayed for a queue, on that host was unable to locate the executable on that host in order to start a job. Please check the error logfile of that for leads on how to resolve the problem. Please enable the queue afterwards via the <code>-c</code> option of the command manually. </p>
<p> If the c(onfiguration ambiguous) state is displayed for a queue instance this indicates that the configuration specified for this queue instance in is ambiguous. This state is cleared when the configuration becomes unambiguous again. This state prevents further jobs from being scheduled to that queue instance. Detailed reasons why a queue instance entered the c(onfiguration ambiguous) state can be found in the messages file and are shown by the qstat -explain switch. For queue instances in this state the cluster queue&#8217;s default settings are used for the ambiguous attribute. </p>
<p> If an o(rphaned) state is displayed for a queue instance, it indicates that the queue instance is no longer demanded by the current cluster queue&#8217;s configuration or the host group configuration. The queue instance is kept because jobs which not yet finished jobs are still associated with it, and it will vanish from qstat output when these jobs have finished. To quicken vanishing of an orphaned queue instance associated job(s) can be deleted using A queue instance in (o)rphaned state can be revived by changing the cluster queue configuration accordingly to cover that queue instance. This state prevents from scheduling further jobs to that queue instance. </p>
<p> If the <code>-F</code> option was used, resource availability information is printed following the queue status line. For each resource (as selected in an option argument to <code>-F</code> or for all resources if the option argument was omitted) a single line is displayed with the following format:</p>
<dl>
<dt>*</p>
<dd> a one letter specifier indicating whether the current resource availability value was dominated by either<br />
 `<code>g</code>&#8216; &#8211; a cluster global,<br />
 `<code>h</code>&#8216; &#8211; a host total or<br />
 `<code>q</code>&#8216; &#8211; a queue related resource consumption.</p>
<dt>*</p>
<dd> a second one letter specifier indicating the source for the current resource availability value, being one of<br />
 `<code>l</code>&#8216; &#8211; a load value reported for the resource,<br />
 `<code>L</code>&#8216; &#8211; a load value for the resource after administrator defined load scaling has been applied,<br />
 `<code>c</code>&#8216; &#8211; availability derived from the consumable resources facility (see<br />
 `<code>f</code>&#8216; &#8211; a fixed availability definition derived from a non-consumable complex attribute or a fixed resource limit.</p>
<dt>*</p>
<dd> after a colon the name of the resource on which information is displayed.</p>
<dt>*</p>
<dd> after an equal sign the current resource availability value.</dl>
<p> The displayed availability values and the sources from which they derive are always the minimum values of all possible combinations. Hence, for example, a line of the form &quot;qf:h_vmem=4G&quot; indicates that a queue currently has a maximum availability in virtual memory of 4 Gigabyte, where this value is a fixed value (e.g. a resource limit in the queue configuration) and it is queue dominated, i.e. the host in total may have more virtual memory available than this, but the queue doesn&#8217;t allow for more. Contrarily a line &quot;hl:h_vmem=4G&quot; would also indicate an upper bound of 4 Gigabyte virtual memory availability, but the limit would be derived from a load value currently reported for the host. So while the queue might allow for jobs with higher virtual memory requirements, the host on which this particular queue resides currently only has 4 Gigabyte available. </p>
<p> If the <code>-explain</code> option was used with the character &#8216;a&#8217; or &#8216;A&#8217;, information about resources is displayed, that violate load or suspend thresholds.<br />
 The same format as with the <code>-F</code> option is used with following extensions:</p>
<dl>
<dt>*</p>
<dd> the line starts with the keyword `alarm&#8217; </p>
<dt>*</p>
<dd> appended to the resource value is the type and value of the appropriate threshold</dl>
<p> After the queue status line (in case of <code>-f</code>) or the resource availability information (in case of <code>-F</code>) a single line is printed for each job running currently in this queue. Each job status line contains</p>
<dl>
<dt>*</p>
<dd> the job ID,</p>
<dt>*</p>
<dd> the priority of the job determining its position in the pending jobs list. The priority value is determined dynamically based on ticket and urgency policy set-up (see also ).</p>
<dt>*</p>
<dd> the job name,</p>
<dt>*</p>
<dd> the job owner name,</p>
<dt>*</p>
<dd> the status of the job &#8211; one of t(ransfering), r(unning), R(estarted), s(uspended), S(uspended) or T(hreshold) (see the <code>Reduced Format</code> section for detailed information),</p>
<dt>*</p>
<dd> the submission or start time and date of the job.</p>
<dt>*</p>
<dd> the number of job slots or the function of parallel job tasks if <code>-g t</code> is specified. </p>
<p> Without <code>-g t</code> option the number of slots occupied per queue resp. requested by the job is displayed. For pending parallel jobs with a PE slot range request, the assumed future slot allocation is displayed. With <code>-g t</code> option the function of the running jobs (MASTER or SLAVE &#8211; the latter for parallel jobs only) is displayed.</dl>
<p> If the <code>-t</code> option is supplied, each job status line also contains</p>
<dl>
<dt>*</p>
<dd> the task ID,</p>
<dt>*</p>
<dd> the status of the task &#8211; one of r(unning), R(estarted), s(uspended), S(uspended), T(hreshold), w(aiting), h(old), or x(exited) (see the <code>Reduced Format</code> section for detailed information),</p>
<dt>*</p>
<dd> the cpu, memory, and I/O usage,</p>
<dt>*</p>
<dd> the exit status of the task,</p>
<dt>*</p>
<dd> and the failure code and message for the task.</dl>
<p> Following the list of queue sections a <i>PENDING JOBS</i> list may be printed in case jobs are waiting for being assigned to a queue. A status line for each waiting job is displayed being similar to the one for the running jobs. The differences are that the status for the jobs is w(aiting) or h(old), that the submit time and date is shown instead of the start time and that no function is displayed for the jobs. </p>
<p> In very rare cases, e.g. if starts up from an inconsistent state in the job or queue spool files or if the <code>clean queue</code> (<code>-cq</code>) option of is used, <i>qstat</i> cannot assign jobs to either the running or pending jobs section of the output. In this case as job status inconsistency (e.g. a job has a running status but is not assigned to a queue) has been detected. Such jobs are printed in an <i>ERROR JOBS</i> section at the very end of the output. The ERROR JOBS section should disappear upon restart of Please contact your Grid Engine support representative if you feel uncertain about the cause or effects of such jobs.</p>
<h3><code>Expanded Format (with -r)</code></h3>
<p> If the <code>-r</code> option was specified together with <i>qstat</i>, the following information for each displayed job is printed (a single line for each of the following job characteristics):</p>
<dl>
<dt>*</p>
<dd> The job and master queue name.</p>
<dt>*</p>
<dd> The hard and soft resource requirements of the job as specified with the <code>-l</code> option. The per resource addend when determining the jobs urgency contribution value is printed (see also</p>
<dt>*</p>
<dd> The requested parallel environment including the desired queue slot range (see <code>-pe</code> option of</p>
<dt>*</p>
<dd> The requested checkpointing environment of the job (see the <code>-ckpt</code> option).</p>
<dt>*</p>
<dd> In case of running jobs, the granted parallel environment with the granted number of queue slots.</dl>
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
<dd> The current accumulated CPU usage of the job in seconds.</p>
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
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>GE_ROOT</code></p>
<dd> Specifies the location of the Grid Engine standard configuration files.</p>
<dt><code>GE_CELL</code></p>
<dd> If set, specifies the default Grid Engine cell. To address a Grid Engine cell <i>qstat</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable GE_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>GE_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>GE_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>SGE_LONG_QNAMES</code></p>
<dd> Qstat does display queue names up to 30 characters. If that is to much or not enough, one can set a custom length with this variable. The minimum display length is 10 characters. If one does not know the best display length, one can set SGE_LONG_QNAMES to -1 and qstat will figure out the best length.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;ge_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
               Grid Engine master host file
<i>&lt;ge_root&gt;/&lt;cell&gt;/common/ge_qstat</i>
               cluster qstat default options
<i>$HOME/.ge_qstat</i>
               user qstat default options
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbAN">ENVIRONMENTAL VARIABLES</a></p>
<dd>
<dt><a href="#lbAO">FILES</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd></dl>
