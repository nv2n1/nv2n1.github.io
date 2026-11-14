---
title: "sge_reporting(5)"
name: "sge_reporting"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_reporting/"
description: "reporting – Grid Engine reporting file format"
---

<p>reporting &#8211; Grid Engine reporting file format</p>
<h2>Description</h2>
<p>A Grid Engine system writes a reporting file to $SGE_ROOT/default/common/reporting. The reporting file contains data that can be used for accounting, monitoring and analysis purposes. It contains information about the cluster (hosts, queues, load values, consumables, etc.), about the jobs running in the cluster and about sharetree configuration and usage. All information is time related, events are dumped to the reporting file in a configurable interval. It allows to monitor a &quot;real time&quot; status of the cluster as well as historical analysis.</p>
<h2>Format</h2>
<p>The reporting file is an ASCII file. Each line contains one record, and the fields of a record are separated by a delimiter (:). The reporting file contains records of different type. Each record type has a specific record structure. </p>
<p> The first two fields are common to all reporting records:</p>
<dl>
<dt><code>time</code></p>
<dd>Time (GMT unix timestamp) when the record was created.</p>
<dt><code>record type</code></p>
<dd>Type of the accounting record. The different types of records and their structure are described in the following text.</dl>
<h3>new_job</h3>
<p>The new_job record is written whenever a new job enters the system (usually by a submitting command). It has the following fields:</p>
<dl>
<dt><code>submission_time</code></p>
<dd>Time (GMT unix time stamp) when the job was submitted.</p>
<dt><code>job_number</code></p>
<dd>The job number.</p>
<dt><code>task_number</code></p>
<dd>The array task id. Always has the value -1 for new_job records (as we don&#8217;t have array tasks yet).</p>
<dt><code>pe_taskid</code></p>
<dd>The task id of parallel tasks. Always has the value &quot;none&quot; for new_job records.</p>
<dt><code>job_name</code></p>
<dd>The job name (from -N submission option)</p>
<dt><code>owner</code></p>
<dd>The job owner.</p>
<dt><code>group</code></p>
<dd>The unix group of the job owner.</p>
<dt><code>project</code></p>
<dd>The project the job is running in.</p>
<dt><code>department</code></p>
<dd>The department the job owner is in.</p>
<dt><code>account</code></p>
<dd>The account string specified for the job (from -A submission option).</p>
<dt><code>priority</code></p>
<dd>The job priority (from -p submission option).</dl>
<h3>job_log</h3>
<p>The job_log record is written whenever a job, an array task or a pe tasks is changing status. A status change can be the transition from pending to running, but can also be triggered by user actions like suspension of a job. It has the following fields:</p>
<dl>
<dt><code>event_time</code></p>
<dd>Time (GMT unix time stamp) when the event was generated.</p>
<dt><code>event</code></p>
<dd>A one word description of the event.</p>
<dt><code>job_number</code></p>
<dd>The job number.</p>
<dt><code>task_number</code></p>
<dd>The array task id. Always has the value -1 for new_job records (as we don&#8217;t have array tasks yet).</p>
<dt><code>pe_taskid</code></p>
<dd>The task id of parallel tasks. Always has the value &quot;none&quot; for new_job records.</p>
<dt><code>state</code></p>
<dd>The state of the job after the event was processed.</p>
<dt><code>user</code></p>
<dd>The user who initiated the event (or special usernames &quot;qmaster&quot;, &quot;scheduler&quot; and &quot;execd&quot; for actions of the system itself like scheduling jobs, executing jobs etc.).</p>
<dt><code>host</code></p>
<dd>The host from which the action was initiated (e.g. the submit host, the qmaster host, etc.).</p>
<dt><code>state_time</code></p>
<dd>Reserved field for later use.</p>
<dt><code>submission_time</code></p>
<dd>Time (GMT unix time stamp) when the job was submitted.</p>
<dt><code>job_name</code></p>
<dd>The job name (from -N submission option)</p>
<dt><code>owner</code></p>
<dd>The job owner.</p>
<dt><code>group</code></p>
<dd>The unix group of the job owner.</p>
<dt><code>project</code></p>
<dd>The project the job is running in.</p>
<dt><code>department</code></p>
<dd>The department the job owner is in.</p>
<dt><code>account</code></p>
<dd>The account string specified for the job (from -A submission option).</p>
<dt><code>priority</code></p>
<dd>The job priority (from -p submission option).</p>
<dt><code>message</code></p>
<dd>A message describing the reported action.</dl>
<h3>acct</h3>
<p>Records of type acct are accounting records. Normally, they are written whenever a job, a task of an array job, or the task of a parallel job terminates. However, for long running jobs an intermediate acct record is created once a day after a midnight. This results in multiple accounting records for a particular job and allows for a fine-grained resource usage monitoring over time. Accounting records comprise the following fields:</p>
<dl>
<dt><code>qname</code></p>
<dd>Name of the cluster queue in which the job has run.</p>
<dt><code>hostname</code></p>
<dd>Name of the execution host.</p>
<dt><code>group</code></p>
<dd>The effective group id of the job owner when executing the job.</p>
<dt><code>owner</code></p>
<dd>Owner of the Grid Engine job.</p>
<dt><code>job_name</code></p>
<dd>Job name.</p>
<dt><code>job_number</code></p>
<dd>Job identifier &#8211; job number.</p>
<dt><code>account</code></p>
<dd>An account string as specified by the or <code>-A</code> option.</p>
<dt><code>priority</code></p>
<dd>Priority value assigned to the job corresponding to the <code>priority</code> parameter in the queue configuration (see</p>
<dt><code>submission_time</code></p>
<dd>Submission time (GMT unix time stamp).</p>
<dt><code>start_time</code></p>
<dd>Start time (GMT unix time stamp).</p>
<dt><code>end_time</code></p>
<dd>End time (GMT unix time stamp).</p>
<dt><code>failed</code></p>
<dd>Indicates the problem which occurred in case a job could not be started on the execution host (e.g. because the owner of the job did not have a valid account on that machine). If Grid Engine tries to start a job multiple times, this may lead to multiple entries in the accounting file corresponding to the same job ID.</p>
<dt><code>exit_status</code></p>
<dd>Exit status of the job script (or Grid Engine specific status in case of certain error conditions).</p>
<dt><code>ru_wallclock</code></p>
<dd>Difference between <code>end_time</code> and <code>start_time</code> (see above).</dl>
<p> The remainder of the accounting entries follows the contents of the standard UNIX rusage structure as described in Depending on the operating system where the job was executed some of the fields may be 0. The following entries are provided: </p>
<pre><dl><dt><dd><code>ru_utime</code>
<code>ru_stime</code>
<code>ru_maxrss</code>
<code>ru_ixrss</code>
<code>ru_ismrss</code>
<code>ru_idrss</code>
<code>ru_isrss</code>
<code>ru_minflt</code>
<code>ru_majflt</code>
<code>ru_nswap</code>
<code>ru_inblock</code>
<code>ru_oublock</code>
<code>ru_msgsnd</code>
<code>ru_msgrcv</code>
<code>ru_nsignals</code>
<code>ru_nvcsw</code>
<code>ru_nivcsw</code>
</dl></pre>
<dl>
<dt><code>project</code></p>
<dd>The project which was assigned to the job.</p>
<dt><code>department</code></p>
<dd>The department which was assigned to the job.</p>
<dt><code>granted_pe</code></p>
<dd>The parallel environment which was selected for that job.</p>
<dt><code>slots</code></p>
<dd>The number of slots which were dispatched to the job by the scheduler.</p>
<dt><code>task_number</code></p>
<dd>Array job task index number.</p>
<dt><code>cpu</code></p>
<dd>The cpu time usage in seconds.</p>
<dt><code>mem</code></p>
<dd>The integral memory usage in Gbytes seconds.</p>
<dt><code>io</code></p>
<dd>The amount of data transferred in input/output operations.</p>
<dt><code>category</code></p>
<dd>A string specifying the job category.</p>
<dt><code>iow</code></p>
<dd>The io wait time in seconds.</p>
<dt><code>pe_taskid</code></p>
<dd>If this identifier is set the task was part of a parallel job and was passed to Grid Engine via the qrsh -inherit interface.</p>
<dt><code>maxvmem</code></p>
<dd>The maximum vmem size in bytes.</p>
<dt><code>arid</code></p>
<dd>Advance reservation identifier. If the job used resources of an advance reservation then this field contains a positive integer identifier otherwise the value is &quot;<code>0</code>&quot; .</dl>
<h3>queue</h3>
<p>Records of type queue contain state information for queues (queue instances). A queue record has the following fields:</p>
<dl>
<dt><code>qname</code></p>
<dd>The cluster queue name.</p>
<dt><code>hostname</code></p>
<dd>The hostname of a specific queue instance.</p>
<dt><code>report_time</code></p>
<dd>The time (GMT unix time stamp) when a state change was triggered.</p>
<dt><code>state</code></p>
<dd>The new queue state.</dl>
<h3>queue_consumable</h3>
<p>A queue_consumable record contains information about queue consumable values in addition to queue state information:</p>
<dl>
<dt><code>qname</code></p>
<dd>The cluster queue name.</p>
<dt><code>hostname</code></p>
<dd>The hostname of a specific queue instance.</p>
<dt><code>report_time</code></p>
<dd>The time (GMT unix time stamp) when a state change was triggered.</p>
<dt><code>state</code></p>
<dd>The new queue state.</p>
<dt><code>consumables</code></p>
<dd>Description of consumable values. Information about multiple consumables is separated by space. A consumable description has the format &lt;name&gt;=&lt;actual_value&gt;=&lt;configured value&gt;.</dl>
<h3>host</h3>
<p>A host record contains information about hosts and host load values. It contains the following information:</p>
<dl>
<dt><code>hostname</code></p>
<dd>The name of the host.</p>
<dt><code>report_time</code></p>
<dd>The time (GMT unix time stamp) when the reported information was generated.</p>
<dt><code>state</code></p>
<dd>The new host state. Currently, Grid Engine doesn&#8217;t track a host state, the field is reserved for future use. Always contains the value X.</p>
<dt><code>load values</code></p>
<dd>Description of load values. Information about multiple load values is separated by space. A load value description has the format &lt;name&gt;=&lt;actual_value&gt;.</dl>
<h3>host_consumable</h3>
<p>A host_consumable record contains information about hosts and host consumables. Host consumables can for example be licenses. It contains the following information:</p>
<dl>
<dt><code>hostname</code></p>
<dd>The name of the host.</p>
<dt><code>report_time</code></p>
<dd>The time (GMT unix time stamp) when the reported information was generated.</p>
<dt><code>state</code></p>
<dd>The new host state. Currently, Grid Engine doesn&#8217;t track a host state, the field is reserved for future use. Always contains the value X.</p>
<dt><code>consumables</code></p>
<dd>Description of consumable values. Information about multiple consumables is separated by space. A consumable description has the format &lt;name&gt;=&lt;actual_value&gt;=&lt;configured value&gt;.</dl>
<h3>sharelog</h3>
<p>The Grid Engine qmaster can dump information about sharetree configuration and use to the reporting file. The parameter <i>sharelog</i> sets an interval in which sharetree information will be dumped. It is set in the format HH:MM:SS. A value of 00:00:00 configures qmaster not to dump sharetree information. Intervals of several minutes up to hours are sensible values for this parameter. The record contains the following fields</p>
<dl>
<dt><code>current time</code></p>
<dd>The present time</p>
<dt><code>usage time</code></p>
<dd>The time used so far</p>
<dt><code>node name</code></p>
<dd>The node name</p>
<dt><code>user name</code></p>
<dd>The user name</p>
<dt><code>project name</code></p>
<dd>The project name</p>
<dt><code>shares </code></p>
<dd>The total shares</p>
<dt><code>job count </code></p>
<dd>The job count</p>
<dt><code>level </code></p>
<dd>The percentage of shares used</p>
<dt><code>total </code></p>
<dd>The adjusted percentage of shares used</p>
<dt><code>long target share </code></p>
<dd>The long target percentage of resource shares used</p>
<dt><code>short target share </code></p>
<dd>The short target percentage of resource shares used</p>
<dt><code>actual share </code></p>
<dd>The actual percentage of resource shares used</p>
<dt><code>usage </code></p>
<dd>The combined shares used</p>
<dt><code>cpu </code></p>
<dd>The cpu used</p>
<dt><code>mem </code></p>
<dd>The memory used</p>
<dt><code>io </code></p>
<dd>The IO used</p>
<dt><code>long target cpu </code></p>
<dd>The long target cpu used</p>
<dt><code>long target mem </code></p>
<dd>The long target memory used</p>
<dt><code>long target io </code></p>
<dd>The long target IO used</dl>
<h3>new_ar</h3>
<p>A new_ar record contains information about advance reservation objects. Entries of this type will be added if an advance reservation is created. It contains the following information:</p>
<dl>
<dt><code>submission_time</code></p>
<dd>The time (GMT unix time stamp) when the advance reservation was created.</p>
<dt><code>ar_number</code></p>
<dd>The advance reservation number identifying the reservation.</p>
<dt><code>ar_owner</code></p>
<dd>The owner of the advance reservation.</dl>
<h3>ar_attribute</h3>
<p>The ar_attribute record is written whenever a new advance reservation was added or the attribute of an existing advance reservation has changed. It has following fields.</p>
<dl>
<dt><code>event_time</code></p>
<dd>The time (GMT unix time stamp) when the event was generated.</p>
<dt><code>submission_time</code></p>
<dd>The time (GMT unix time stamp) when the advance reservation was created.</p>
<dt><code>ar_number</code></p>
<dd>The advance reservation number identifying the reservation.</p>
<dt><code>ar_name</code></p>
<dd>Name of the advance reservation.</p>
<dt><code>ar_account</code></p>
<dd>An account string which was specified during the creation of the advance reservation.</p>
<dt><code>ar_start_time</code></p>
<dd>Start time.</p>
<dt><code>ar_end_time</code></p>
<dd>End time.</p>
<dt><code>ar_granted_pe</code></p>
<dd>The parallel environment which was selected for an advance reservation.</p>
<dt><code>ar_granted_resources</code></p>
<dd>The granted resources which were selected for an advance reservation.</dl>
<h3>ar_log</h3>
<p>The ar_log record is written whenever a advance reservation is changing status. A status change can be from pending to active, but can also be triggered by system events like host outage. It has following fields.</p>
<dl>
<dt><code>ar_state_change_time</code></p>
<dd>The time (GMT unix time stamp) when the event occurred which caused a state change.</p>
<dt><code>submission_time</code></p>
<dd>The time (GMT unix time stamp) when the advance reservation was created.</p>
<dt><code>ar_number</code></p>
<dd>The advance reservation number identifying the reservation.</p>
<dt><code>ar_state</code></p>
<dd>The new state.</p>
<dt><code>ar_event</code></p>
<dd>An event id identifying the event which caused the state change.</p>
<dt><code>ar_message</code></p>
<dd>A message describing the event which caused the state change.</dl>
<h3>ar_acct</h3>
<p>The ar_acct records are accounting records which are written for every queue instance whenever a advance reservation terminates. Advance reservation accounting records comprise following fields.</p>
<dl>
<dt><code>ar_termination_time</code></p>
<dd>The time (GMT unix time stamp) when the advance reservation terminated.</p>
<dt><code>submission_time</code></p>
<dd>The time (GMT unix time stamp) when the advance reservation was created.</p>
<dt><code>ar_number</code></p>
<dd>The advance reservation number identifying the reservation.</p>
<dt><code>ar_qname</code></p>
<dd>Cluster queue name which the advance reservation reserved.</p>
<dt><code>ar_hostname</code></p>
<dd>The name of the execution host.</p>
<dt><code>ar_slots</code></p>
<dd>The number of slots which were reserved.</dl>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
