---
title: "sge_sched_conf(5)"
name: "sge_sched_conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_sched_conf/"
description: "sched_conf – Grid Engine default scheduler configuration file"
---

<p>sched_conf &#8211; Grid Engine default scheduler configuration file</p>
<h2>Description</h2>
<p><i>sched_conf</i> defines the configuration file format for Grid Engine&#8217;s scheduler. In order to modify the configuration, use the graphical user&#8217;s interface or the <i>-msconf</i> option of the command. A default configuration is provided together with the Grid Engine distribution package. </p>
<p> Note, Grid Engine allows backslashes (\) be used to escape newline (
ewline) characters. The backslash and the newline are replaced with a space (&quot; &quot;) character before any interpretation.</p>
<h2>Format</h2>
<p>The following parameters are recognized by the Grid Engine scheduler if present in <i>sched_conf</i>:</p>
<h3><code>algorithm</code></h3>
<p><code>Note:</code> Deprecated, may be removed in future release.<br />
 Allows for the selection of alternative scheduling algorithms. </p>
<p> Currently <code>default</code> is the only allowed setting.</p>
<h3><code>load_formula</code></h3>
<p>A simple algebraic expression used to derive a single weighted load value from all or part of the load parameters reported by for each host and from all or part of the consumable resources (see being maintained for each host. The load formula expression syntax is that of a summation weighted load values, that is: </p>
<pre><dl><dt><dd>{w1|load_val1[*w1]}[{+|-}{w2|load_val2[*w2]}[{+|-}...]]
</dl></pre>
<p><code>Note</code>, no blanks are allowed in the load formula.<br />
 The load values and consumable resources (load_val1, &#8230;) are specified by the name defined in the complex (see<br />
 <code>Note:</code> Administrator defined load values (see the <code>load_sensor</code> parameter in for details) and consumable resources available for all hosts (see may be used as well as Grid Engine default load parameters.<br />
 The weighting factors (w1, &#8230;) are positive integers. After the expression is evaluated for each host the results are assigned to the hosts and are used to sort the hosts corresponding to the weighted load. The sorted host list is used to sort queues subsequently.<br />
 The default load formula is &quot;np_load_avg&quot;.</p>
<h3><code>job_load_adjustments</code></h3>
<p>The load, which is imposed by the Grid Engine jobs running on a system varies in time, and often, e.g. for the CPU load, requires some amount of time to be reported in the appropriate quantity by the operating system. Consequently, if a job was started very recently, the reported load may not provide a sufficient representation of the load which is already imposed on that host by the job. The reported load will adapt to the real load over time, but the period of time, in which the reported load is too low, may already lead to an oversubscription of that host. Grid Engine allows the administrator to specify <code>job_load_adjustments</code> which are used in the Grid Engine scheduler to compensate for this problem.<br />
 The <code>job_load_adjustments</code> are specified as a comma separated list of arbitrary load parameters or consumable resources and (separated by an equal sign) an associated load correction value. Whenever a job is dispatched to a host by the scheduler, the load parameter and consumable value set of that host is increased by the values provided in the <code>job_load_adjustments</code> list. These correction values are decayed linearly over time until after <code>load_adjustment_decay_time</code> from the start the corrections reach the value 0. If the <code>job_load_adjustments</code> list is assigned the special denominator NONE, no load corrections are performed.<br />
 The adjusted load and consumable values are used to compute the combined and weighted load of the hosts with the <code>load_formula</code> (see above) and to compare the load and consumable values against the load threshold lists defined in the queue configurations (see If the <code>load_formula</code> consists simply of the default CPU load average parameter <i>np_load_avg</i>, and if the jobs are very compute intensive, one might want to set the <code>job_load_adjustments</code> list to <i>np_load_avg=1.00</i>, which means that every new job dispatched to a host will require 100 % CPU time, and thus the machine&#8217;s load is instantly increased by 1.00.</p>
<h3><code>load_adjustment_decay_time</code></h3>
<p>The load corrections in the &quot;<code>job_load_adjustments</code>&quot; list above are decayed linearly over time from the point of the job start, where the corresponding load or consumable parameter is raised by the full correction value, until after a time period of &quot;<code>load_adjustment_decay_time</code>&quot;, where the correction becomes 0. Proper values for &quot;<code>load_adjustment_decay_time</code>&quot; greatly depend upon the load or consumable parameters used and the specific operating system(s). Therefore, they can only be determined on-site and experimentally. For the default <i>np_load_avg</i> load parameter a &quot;<code>load_adjustment_decay_time</code>&quot; of 7 minutes has proven to yield reasonable results.</p>
<h3><code>maxujobs</code></h3>
<p>The maximum number of jobs any user may have running in a Grid Engine cluster at the same time. If set to 0 (default) the users may run an arbitrary number of jobs.</p>
<h3><code>schedule_interval</code></h3>
<p>At the time the scheduler thread initially registers at the event master thread in <code>schedule_interval</code> is used to set the time interval in which the event master thread sends scheduling event updates to the scheduler thread. A scheduling event is a status change that has occurred within which may trigger or affect scheduler decisions (e.g. a job has finished and thus the allocated resources are available again).<br />
 In the Grid Engine default scheduler the arrival of a scheduling event report triggers a scheduler run. The scheduler waits for event reports otherwise.<br />
 <code>Schedule_interval</code> is a time value (see for a definition of the syntax of time values).</p>
<h3><code>queue_sort_method</code></h3>
<p>This parameter determines in which order several criteria are taken into account to product a sorted queue list. Currently, two settings are valid: <code>seqno</code> and <code>load</code>. However in both cases, Grid Engine attempts to maximize the number of soft requests (see <code>-s</code> option) being fulfilled by the queues for a particular as the primary criterion.<br />
 Then, if the <code>queue_sort_method</code> parameter is set to <code>seqno</code>, Grid Engine will use the <code>seq_no</code> parameter as configured in the current queue configurations (see as the next criterion to sort the queue list. The <code>load_formula</code> (see above) has only a meaning if two queues have equal sequence numbers. If <code>queue_sort_method</code> is set to <code>load</code> the load according the <code>load_formula</code> is the criterion after maximizing a job&#8217;s soft requests and the sequence number is only used if two hosts have the same load. The sequence number sorting is most useful if you want to define a fixed order in which queues are to be filled (e.g. the cheapest resource first). </p>
<p> The default for this parameter is <code>load</code>.</p>
<h3><code>halftime</code></h3>
<p>When executing under a share based policy, the scheduler &quot;ages&quot; (i.e. decreases) usage to implement a sliding window for achieving the share entitlements as defined by the share tree. The <code>halftime</code> defines the time interval in which accumulated usage will have been decayed to half its original value. Valid values are specified in hours or according to the time format as specified in<br />
 If the value is set to 0, the usage is not decayed.</p>
<h3><code>usage_weight_list</code></h3>
<p>Grid Engine accounts for the consumption of the resources CPU-time, memory and IO to determine the usage which is imposed on a system by a job. A single usage value is computed from these three input parameters by multiplying the individual values by weights and adding them up. The weights are defined in the <code>usage_weight_list</code>. The format of the list is </p>
<pre><dl><dt><dd>cpu=wcpu,mem=wmem,io=wio
</dl></pre>
<p>where wcpu, wmem and wio are the configurable weights. The weights are real number. The sum of all tree weights should be 1.</p>
<h3><code>compensation_factor</code></h3>
<p>Determines how fast Grid Engine should compensate for past usage below of above the share entitlement defined in the share tree. Recommended values are between 2 and 10, where 10 means faster compensation.</p>
<h3><code>weight_user</code></h3>
<p>The relative importance of the user shares in the functional policy. Values are of type real.</p>
<h3><code>weight_project</code></h3>
<p>The relative importance of the project shares in the functional policy. Values are of type real.</p>
<h3><code>weight_department</code></h3>
<p>The relative importance of the department shares in the functional policy. Values are of type real.</p>
<h3><code>weight_job</code></h3>
<p>The relative importance of the job shares in the functional policy. Values are of type real.</p>
<h3><code>weight_tickets_functional</code></h3>
<p>The maximum number of functional tickets available for distribution by Grid Engine. Determines the relative importance of the functional policy. See under for an overview on job priorities.</p>
<h3><code>weight_tickets_share</code></h3>
<p>The maximum number of share based tickets available for distribution by Grid Engine. Determines the relative importance of the share tree policy. See under for an overview on job priorities.</p>
<h3><code>weight_deadline</code></h3>
<p>The weight applied on the remaining time until a jobs latest start time. Determines the relative importance of the deadline. See under for an overview on job priorities.</p>
<h3><code>weight_waiting_time</code></h3>
<p>The weight applied on the jobs waiting time since submission. Determines the relative importance of the waiting time. See under for an overview on job priorities.</p>
<h3><code>weight_urgency</code></h3>
<p>The weight applied on jobs normalized urgency when determining priority finally used. Determines the relative importance of urgency. See under for an overview on job priorities.</p>
<h3><code>weight_priority</code></h3>
<p>The weight applied on jobs normalized POSIX priority when determining priority finally used. Determines the relative importance of POSIX priority. See under for an overview on job priorities.</p>
<h3><code>weight_ticket</code></h3>
<p>The weight applied on normalized ticket amount when determining priority finally used. Determines the relative importance of the ticket policies. See under for an overview on job priorities.</p>
<h3><code>flush_finish_sec</code></h3>
<p>The parameters are provided for tuning the system&#8217;s scheduling behavior. By default, a scheduler run is triggered in the scheduler interval. When this parameter is set to 1 or larger, the scheduler will be triggered x seconds after a job has finished. Setting this parameter to 0 disables the flush after a job has finished.</p>
<h3><code>flush_submit_sec</code></h3>
<p>The parameters are provided for tuning the system&#8217;s scheduling behavior. By default, a scheduler run is triggered in the scheduler interval. When this parameter is set to 1 or larger, the scheduler will be triggered x seconds after a job was submitted to the system. Setting this parameter to 0 disables the flush after a job was submitted.</p>
<h3><code>schedd_job_info</code></h3>
<p>The default scheduler can keep track why jobs could not be scheduled during the last scheduler run. This parameter enables or disables the observation. The value <code>true</code> enables the monitoring <code>false</code> turns it off. </p>
<p> It is also possible to activate the observation only for certain jobs. This will be done if the parameter is set to <code>job_list</code> followed by a comma separated list of job ids. </p>
<p> The user can obtain the collected information with the command qstat -j.</p>
<h3><code>params</code></h3>
<p>This is foreseen for passing additional parameters to the Grid Engine scheduler. The following values are recognized:</p>
<dl>
<dt><i>DURATION_OFFSET</i></p>
<dd>If set, overrides the default of value 60 seconds. This parameter is used by the Grid Engine scheduler when planning resource utilization as the delta between net job runtimes and total time until resources become available again. Net job runtime as specified with -l h_rt=&#8230; or -l s_rt=&#8230; or <code>default_duration</code> always differs from total job runtime due to delays before and after actual job start and finish. Among the delays before job start is the time until the end of a <code>schedule_interval</code>, the time it takes to deliver a job to and the delays caused by <code>prolog</code> in , <code>start_proc_args</code> in and <code>starter_method</code> in (<code>notify</code>, <code>terminate_method</code> or <code>checkpointing</code>), procedures run after actual job finish, such as <code>stop_proc_args</code> in or <code>epilog</code> in , and the delay until a new <code>schedule_interval</code>.<br />
 If the offset is too low, resource reservations (see <code>max_reservation</code>) can be delayed repeatedly due to an overly optimistic job circulation time.</p>
<dt><i>JC_FILTER</i></p>
<dd><code>Note:</code> Deprecated, may be removed in future release.<br />
 If set to true, the scheduler limits the number of jobs it looks at during a scheduling run. At the beginning of the scheduling run it assigns each job a specific category, which is based on the job&#8217;s requests, priority settings, and the job owner. All scheduling policies will assign the same importance to each job in one category. Therefore the number of jobs per category have a FIFO order and can be limited to the number of free slots in the system. </p>
<p> A exception are jobs, which request a resource reservation. They are included regardless of the number of jobs in a category. </p>
<p> This setting is turned off per default, because in very rare cases, the scheduler can make a wrong decision. It is also advised to turn report_pjob_tickets off. Otherwise qstat -ext can report outdated ticket amounts. The information shown with a qstat -j for a job, that was excluded in a scheduling run, is very limited.</p>
<dt><i>PROFILE</i></p>
<dd>If set equal to 1, the scheduler logs profiling information summarizing each scheduling run.</p>
<dt><i>MONITOR</i></p>
<dd>If set equal to 1, the scheduler records information for each scheduling run allowing to reproduce job resources utilization in the file <i>&lt;ge_root&gt;/&lt;cell&gt;/common/schedule</i>.</p>
<dt><i>PE_RANGE_ALG</i></p>
<dd>This parameter sets the algorithm for the pe range computation. The default is automatic, which means that the scheduler will select the best one, and it should not be necessary to change it to a different setting in normal operation. If a custom setting is needed, the following values are available:<br />
 auto : the scheduler selects the best algorithm<br />
 least : starts the resource matching with the lowest slot amount first<br />
 bin : starts the resource matching in the middle of the pe slot range<br />
 highest : starts the resource matching with the highest slot amount first</dl>
<p> Changing <code>params</code> will take immediate effect. The default for <code>params</code> is none.</p>
<h3><code>reprioritize_interval</code></h3>
<p>Interval (HH:MM:SS) to reprioritize jobs on the execution hosts based on the current ticket amount for the running jobs. If the interval is set to 00:00:00 the reprioritization is turned off. The default value is 00:00:00.</p>
<h3><code>report_pjob_tickets</code></h3>
<p>This parameter allows to tune the system&#8217;s scheduling run time. It is used to enable / disable the reporting of pending job tickets to the qmaster. It does not influence the tickets calculation. The sort order of jobs in qstat and qmon is only based on the submit time, when the reporting is turned off.<br />
 The reporting should be turned off in a system with a very large amount of jobs by setting this parameter to &quot;false&quot;.</p>
<h3><code>halflife_decay_list</code></h3>
<p>The halflife_decay_list allows to configure different decay rates for the &quot;finished_jobs usage types, which is used in the pending job ticket calculation to account for jobs which have just ended. This allows the user the pending jobs algorithm to count finished jobs against a user or project for a configurable decayed time period. This feature is turned off by default, and the halftime is used instead.<br />
 The halflife_decay_list also allows one to configure different decay rates for each usage type being tracked (cpu, io, and mem). The list is specified in the following format: </p>
<pre><dl><dt><dd><br>
&lt;USAGE_TYPE&gt;=&lt;TIME&gt;[:&lt;USAGE_TYPE&gt;=&lt;TIME&gt;[:&lt;USAGE_TYPE&gt;=&lt;TIME&gt;]]
</dl></pre>
<p>&lt;Usage_TYPE&gt; can be one of the following: cpu, io, or mem.<br />
 &lt;TIME&gt; can be -1, 0 or a timespan specified in minutes. If &lt;TIME&gt; is -1, only the usage of currently running jobs is used. 0 means that the usage is not decayed.</p>
<h3><code>policy_hierarchy</code></h3>
<p>This parameter sets up a dependency chain of ticket based policies. Each ticket based policy in the dependency chain is influenced by the previous policies and influences the following policies. A typical scenario is to assign precedence for the override policy over the share-based policy. The override policy determines in such a case how share-based tickets are assigned among jobs of the same user or project. Note that all policies contribute to the ticket amount assigned to a particular job regardless of the policy hierarchy definition. Yet the tickets calculated in each of the policies can be different depending on &quot;<i>POLICY_HIERARCHY</i>&quot;. </p>
<p> The &quot;<i>POLICY_HIERARCHY</i>&quot; parameter can be a up to 3 letter combination of the first letters of the 3 ticket based policies S(hare-based), F(unctional) and O(verride). So a value &quot;OFS&quot; means that the override policy takes precedence over the functional policy, which finally influences the share-based policy. Less than 3 letters mean that some of the policies do not influence other policies and also are not influenced by other policies. So a value of &quot;FS&quot; means that the functional policy influences the share-based policy and that there is no interference with the other policies. </p>
<p> The special value &quot;NONE&quot; switches off policy hierarchies.</p>
<h3><code>share_override_tickets</code></h3>
<p>If set to &quot;true&quot; or &quot;1&quot;, override tickets of any override object instance are shared equally among all running jobs associated with the object. The pending jobs will get as many override tickets, as they would have, when they were running. If set to &quot;false&quot; or &quot;0&quot;, each job gets the full value of the override tickets associated with the object. The default value is &quot;true&quot;.</p>
<h3><code>share_functional_shares</code></h3>
<p>If set to &quot;true&quot; or &quot;1&quot;, functional shares of any functional object instance are shared among all the jobs associated with the object. If set to &quot;false&quot; or &quot;0&quot;, each job associated with a functional object, gets the full functional shares of that object. The default value is &quot;true&quot;.</p>
<h3><code>max_functional_jobs_to_schedule</code></h3>
<p>The maximum number of pending jobs to schedule in the functional policy. The default value is 200.</p>
<h3><code>max_pending_tasks_per_job</code></h3>
<p>The maximum number of subtasks per pending array job to schedule. This parameter exists in order to reduce scheduling overhead. The default value is 50.</p>
<h3><code>max_reservation</code></h3>
<p>The maximum number of reservations scheduled within a schedule interval. When a runnable job can not be started due to a shortage of resources a reservation can be scheduled instead. A reservation can cover consumable resources with the global host, any execution host and any queue. For parallel jobs reservations are done also for slots resource as specified in As job runtime the maximum of the time specified with -l h_rt=&#8230; or -l s_rt=&#8230; is assumed. For jobs that have neither of them the default_duration is assumed. Reservations prevent jobs of lower priority as specified in from utilizing the reserved resource quota during the time of reservation. Jobs of lower priority are allowed to utilize those reserved resources only if their prospective job end is before the start of the reservation (backfilling). Reservation is done only for non-immediate jobs (-now no) that request reservation (-R y). If max_reservation is set to &quot;0&quot; no job reservation is done. </p>
<p> Note, that reservation scheduling can be performance consuming and hence reservation scheduling is switched off by default. Since reservation scheduling performance consumption is known to grow with the number of pending jobs, the use of -R y option is recommended only for those jobs actually queuing for bottleneck resources. Together with the max_reservation parameter this technique can be used to narrow down performance impacts.</p>
<h3><code>default_duration</code></h3>
<p>When job reservation is enabled through max_reservation parameter the default duration is assumed as runtime for jobs that have neither -l h_rt=&#8230; nor -l s_rt=&#8230; specified. In contrast to a h_rt/s_rt time limit the default_duration is not enforced.</p>
<h2>Files</h2>
<pre><i>&lt;ge_root&gt;/&lt;cell&gt;/common/sched_configuration</i>
 scheduler thread configuration</pre>
<h2>See Also</h2>
<p><i>Grid Engine Installation and Administration Guide</i></p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
