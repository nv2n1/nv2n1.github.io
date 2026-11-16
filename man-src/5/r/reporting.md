---
title: "reporting(5)"
name: "reporting"
section: "5"
letter: "r"
url: "/docs/linux/man/5-reporting/"
description: "reporting – xxQS_NAMExx reporting file format"
---

<p>reporting &#8211; xxQS_NAMExx reporting file format</p>
<h2>Description</h2>
<p>A xxQS_NAMExx system writes a reporting file <i>$SGE_ROOT/$SGE_CELL/common/reporting</i> if <code>reporting=true</code> is specified in the <code>reporting_params</code>. This occurs intervals of the <code>flush_time</code> specified in the same place. The reporting file contains data that can be used for accounting, monitoring and analysis purposes. It contains information about the cluster (hosts, queues, load values, consumables, etc.), about the jobs running in the cluster and about sharetree configuration and usage. All information is time-related and events are dumped to the reporting file in a configurable interval. It allows &quot;real time&quot; monitoring of the cluster status as well as historical analysis.</p>
<h2>Format</h2>
<p>The reporting file is an ASCII file. Each line contains one record, and the fields of a record are separated by a delimiter (:). The reporting file contains records of different type. Each record type has a specific record structure. </p>
<p> The first two fields are common to all reporting records:</p>
<dl>
<dt><code>time</code></dt>
<dd>The time when the record was created. All time values described here are the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).</dd>
<dt><code>record type</code></dt>
<dd>Type of the accounting record.</dd></dl>
<p> The different types of records and their structure are described below, eliding the leading <code>time</code> and <code>record type</code> fields in each case.</p>
<h3>new_job</h3>
<p>The new_job record is written whenever a new job enters the system (usually by a submission command). It has the following fields:</p>
<dl>
<dt><code>submission_time</code></dt>
<dd>Time when the job was submitted.</dd>
<dt><code>job_number</code></dt>
<dd>The job number.</dd>
<dt><code>task_number</code></dt>
<dd>The array task id. Always has the value -1 for new_job records (as array tasks haven&#8217;t been created at that stage).</dd>
<dt><code>pe_taskid</code></dt>
<dd>The task id of parallel tasks. Always has the value &quot;none&quot; for new_job records.</dd>
<dt><code>job_name</code></dt>
<dd>The job name (from <code>-N</code> submission option).</dd>
<dt><code>owner</code></dt>
<dd>The job owner.</dd>
<dt><code>group</code></dt>
<dd>The Unix group of the job owner.</dd>
<dt><code>project</code></dt>
<dd>The project the job is running in.</dd>
<dt><code>department</code></dt>
<dd>The department the job owner is in.</dd>
<dt><code>account</code></dt>
<dd>The account string specified for the job (from the <code>-A</code> submission option).</dd>
<dt><code>priority</code></dt>
<dd>The job priority (from the <code>-p</code> submission option).</dd></dl>
<h3>job_log</h3>
<p>If <code>joblog=true</code> is specified in the <code>reporting_params</code>, a job_log record is written whenever a job, an array task or a PE task changes status. A status change can be the transition from pending to running, but can also be triggered by user actions, like suspension of a job. It has the following fields:</p>
<dl>
<dt><code>event_time</code></dt>
<dd>Time when the event was generated.</dd>
<dt><code>event</code></dt>
<dd>A one word description of the event.</dd>
<dt><code>job_number</code></dt>
<dd>The job number.</dd>
<dt><code>task_number</code></dt>
<dd>The PE task id. Always has the value -1 for new_job records (as parallel tasks haven&#8217;t been created at that stage).</dd>
<dt><code>pe_taskid</code></dt>
<dd>The task id of parallel tasks. Always has the value &quot;none&quot; for new_job records.</dd>
<dt><code>state</code></dt>
<dd>The state of the job after the event was processed.</dd>
<dt><code>user</code></dt>
<dd>The user who initiated the event (or special usernames &quot;qmaster&quot;, &quot;scheduler&quot; and &quot;execd&quot; for actions of the system itself like scheduling jobs, executing jobs etc.).</dd>
<dt><code>host</code></dt>
<dd>The host from which the action was initiated (e.g. the submit host, the qmaster host, etc.).</dd>
<dt><code>state_time</code></dt>
<dd>Reserved field for later use.</dd>
<dt><code>submission_time</code></dt>
<dd>Time when the job was submitted.</dd>
<dt><code>job_name</code></dt>
<dd>The job name (from the <code>-N</code> submission option).</dd>
<dt><code>owner</code></dt>
<dd>The job owner.</dd>
<dt><code>group</code></dt>
<dd>The Unix group of the job owner.</dd>
<dt><code>project</code></dt>
<dd>The project the job is running in.</dd>
<dt><code>department</code></dt>
<dd>The department the job owner is in.</dd>
<dt><code>account</code></dt>
<dd>The account string specified for the job (from the <code>-A</code> submission option).</dd>
<dt><code>priority</code></dt>
<dd>The job priority (from the <code>-p</code> submission option).</dd>
<dt><code>message</code></dt>
<dd>A message describing the reported action.</dd></dl>
<h3>acct</h3>
<p>Records of type acct are accounting records. Normally, they are written whenever a job, a task of an array job, or a task of a parallel job terminates. However, for long running jobs an intermediate acct record is created once a day after midnight. This results in multiple accounting records for a particular job and allows for fine-grained resource usage monitoring over time. </p>
<p> Accounting records have the structure described in with the addition of leading time and type fields (which are not used in the accounting file).</p>
<h3>queue</h3>
<p>Records of type queue contain state information for queues (queue instances). A queue record has the following fields:</p>
<dl>
<dt><code>qname</code></dt>
<dd>The cluster queue name.</dd>
<dt><code>hostname</code></dt>
<dd>The hostname of a specific queue instance.</dd>
<dt><code>report_time</code></dt>
<dd>The time when a state change was triggered.</dd>
<dt><code>state</code></dt>
<dd>The new queue state. The possible states are single-letter values, as reported by with the <code>-q</code> option.</dd></dl>
<h3>queue_consumable</h3>
<p>A queue_consumable record contains information about queue consumable values in addition to queue state information:</p>
<dl>
<dt><code>qname</code></dt>
<dd>The cluster queue name.</dd>
<dt><code>hostname</code></dt>
<dd>The hostname of a specific queue instance.</dd>
<dt><code>report_time</code></dt>
<dd>The time when a state change was triggered.</dd>
<dt><code>state</code></dt>
<dd>The new queue state.</dd>
<dt><code>consumables</code></dt>
<dd>Description of consumable values. Information about multiple consumables is separated by space. A consumable description has the format <i>name</i>=<i>actual_value</i>=<i>configured_value</i>.</dd></dl>
<p> Consumables are only logged if <code>log_consumables=true</code> is specified in the <code>reporting_params</code>, or the consumable is specified in the local or global <code>report_variables</code>.</p>
<h3>host</h3>
<p>A host record contains information about hosts and host load values. It contains the following information:</p>
<dl>
<dt><code>hostname</code></dt>
<dd>The name of the host.</dd>
<dt><code>report_time</code></dt>
<dd>The time when the reported information was generated.</dd>
<dt><code>state</code></dt>
<dd>The new host state. Currently, xxQS_NAMExx doesn&#8217;t track a host state; the field is reserved for future use. Always contains the value X.</dd>
<dt><code>load values</code></dt>
<dd>Description of load values. Information about multiple load values is separated by space. A load value description has the format <i>name</i>=<i>actual_value</i>.</dd></dl>
<h3>host_consumable</h3>
<p>A host_consumable record contains information about hosts and host consumables. Host consumables can, for example, be licenses. It contains the following information:</p>
<dl>
<dt><code>hostname</code></dt>
<dd>The name of the host.</dd>
<dt><code>report_time</code></dt>
<dd>The time when the reported information was generated.</dd>
<dt><code>state</code></dt>
<dd>The new host state. Currently, xxQS_NAMExx doesn&#8217;t track a host state; the field is reserved for future use. Always contains the value X.</dd>
<dt><code>consumables</code></dt>
<dd>Description of consumable values. Information about multiple consumables is separated by space. A consumable description has the format <i>name</i>=<i>actual_value</i>=<i>configured_value</i>.</dd></dl>
<p> Consumables are only logged if <code>log_consumables=true</code> is specified in the <code>reporting_params</code>, or the consumable is specified in the local or global <code>report_variables</code>.</p>
<h3>sharelog</h3>
<p>The xxQS_NAMExx qmaster can dump information about sharetree configuration and use to the reporting file. The <code>reporting_params</code> can specify <code>sharelog</code>, which sets an interval in which sharetree information will be dumped. It is set in the format HH:MM:SS. A value of 00:00:00 configures qmaster not to dump sharetree information. Intervals of several minutes up to hours are sensible values for this parameter. The record contains the following fields</p>
<dl>
<dt><code>current time</code></dt>
<dd>The present time</dd>
<dt><code>usage time</code></dt>
<dd>The time used so far</dd>
<dt><code>node name</code></dt>
<dd>The node name</dd>
<dt><code>user name</code></dt>
<dd>The user name</dd>
<dt><code>project name</code></dt>
<dd>The project name</dd>
<dt><code>shares</code></dt>
<dd>The total shares</dd>
<dt><code>job count</code></dt>
<dd>The job count</dd>
<dt><code>level</code></dt>
<dd>The percentage of shares used</dd>
<dt><code>total</code></dt>
<dd>The adjusted percentage of shares used</dd>
<dt><code>long target share</code></dt>
<dd>The long target percentage of resource shares used</dd>
<dt><code>short target share</code></dt>
<dd>The short target percentage of resource shares used</dd>
<dt><code>actual share</code></dt>
<dd>The actual percentage of resource shares used</dd>
<dt><code>usage</code></dt>
<dd>The combined shares used</dd>
<dt><code>cpu</code></dt>
<dd>The number of CPU seconds used</dd>
<dt><code>mem</code></dt>
<dd>The time integral of memory used (in GB seconds)</dd>
<dt><code>io</code></dt>
<dd>The IO done (in GB)</dd>
<dt><code>long target cpu</code></dt>
<dd>The long target cpu used</dd>
<dt><code>long target mem</code></dt>
<dd>The long target memory used</dd>
<dt><code>long target io</code></dt>
<dd>The long target IO used</dd></dl>
<h3>new_ar</h3>
<p>A new_ar record contains information about advance reservation objects. Entries of this type will be added if an advance reservation is created. It contains the following information:</p>
<dl>
<dt><code>submission_time</code></dt>
<dd>The time when the advance reservation was created.</dd>
<dt><code>ar_number</code></dt>
<dd>The advance reservation number identifying the reservation.</dd>
<dt><code>ar_owner</code></dt>
<dd>The owner of the advance reservation.</dd></dl>
<h3>ar_attribute</h3>
<p>The ar_attribute record is written whenever a new advance reservation was added or the attribute of an existing advance reservation has changed. It has the following fields.</p>
<dl>
<dt><code>event_time</code></dt>
<dd>The time when the event was generated.</dd>
<dt><code>submission_time</code></dt>
<dd>The time when the advance reservation was created.</dd>
<dt><code>ar_number</code></dt>
<dd>The advance reservation number identifying the reservation.</dd>
<dt><code>ar_name</code></dt>
<dd>Name of the advance reservation.</dd>
<dt><code>ar_account</code></dt>
<dd>An account string which was specified during the creation of the advance reservation.</dd>
<dt><code>ar_start_time</code></dt>
<dd>Start time.</dd>
<dt><code>ar_end_time</code></dt>
<dd>End time.</dd>
<dt><code>ar_granted_pe</code></dt>
<dd>The parallel environment which was selected for an advance reservation.</dd>
<dt><code>ar_granted_resources</code></dt>
<dd>The granted resources which were selected for an advance reservation.</dd></dl>
<h3>ar_log</h3>
<p>The ar_log record is written whenever an advance reservation changes status. A status change can be from pending to active, but can also be triggered by system events like host outage. It has the following fields.</p>
<dl>
<dt><code>ar_state_change_time</code></dt>
<dd>The time when the event occurred which caused a state change.</dd>
<dt><code>submission_time</code></dt>
<dd>The time when the advance reservation was created.</dd>
<dt><code>ar_number</code></dt>
<dd>The advance reservation number identifying the reservation.</dd>
<dt><code>ar_state</code></dt>
<dd>The new state.</dd>
<dt><code>ar_event</code></dt>
<dd>An event id identifying the event which caused the state change.</dd>
<dt><code>ar_message</code></dt>
<dd>A message describing the event which caused the state change.</dd></dl>
<h3>ar_acct</h3>
<p>The ar_acct records are accounting records which are written for every queue instance whenever an advance reservation terminates. Advance reservation accounting records comprise following fields.</p>
<dl>
<dt><code>ar_termination_time</code></dt>
<dd>The time when the advance reservation terminated.</dd>
<dt><code>submission_time</code></dt>
<dd>The time when the advance reservation was created.</dd>
<dt><code>ar_number</code></dt>
<dd>The advance reservation number identifying the reservation.</dd>
<dt><code>ar_qname</code></dt>
<dd>Cluster queue name which the advance reservation reserved.</dd>
<dt><code>ar_hostname</code></dt>
<dd>The name of the execution host.</dd>
<dt><code>ar_slots</code></dt>
<dd>The number of slots which were reserved.</dd></dl>
<h2>Files</h2>
<p><i>$SGE_ROOT/$SGE_CELL/common/reporting</i></p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
