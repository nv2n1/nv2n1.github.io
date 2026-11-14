---
title: "pbs_queue_attributes(7)"
name: "pbs_queue_attributes"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pbs_queue_attributes/"
description: "pbs_queue_attributes – pbs queue attributes"
---

<p>pbs_queue_attributes &#8211; pbs queue attributes</p>
<h2>Description</h2>
<p>Queue public attributes are alterable on request by a client. The client must be acting for a user with administrator (manager) or operator privilege. Certain attributes require the user to have full administrator privilege before they can be modified. The following attributes apply to both queue types:</p>
<dl>
<dd><i></p>
<dl>
<dt>acl_group_enable</i><font SIZE="+1"><i></i></p>
<dd>Attribute which when true directs the server to use the queue group access control list <i>acl_groups .</i> Format: boolean, &quot;TRUE&quot;, &quot;True&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;FALSE&quot;, &quot;False&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false = disabled. <i></p>
<dt>acl_group_sloppy</i></font><font SIZE="+2"><i></i></p>
<dd>Search a job user&#8217;s secondary groups if the effective group doesn&#8217;t match the group acl. Warning, this can be very slow and expensive. Format: boolean, &quot;TRUE&quot;, &quot;True&quot;, &quot;true&quot;, &quot;Y&quot;, &quot;y&quot;, &quot;1&quot;, &quot;FALSE&quot;, &quot;False&quot;, &quot;false&quot;, &quot;N&quot;, &quot;n&quot;, &quot;0&quot;; default value: false = disabled. <i></p>
<dt>acl_groups</i></font><font SIZE="+3"><i></i></p>
<dd>List which allows or denies enqueuing of jobs owned by members of the listed groups. The groups in the list are groups on the server host, not submitting hosts. If acl_group_enable is set to true, only groups listed in the acl_groups attribute will be allowed access to the queue. See section 10.1, Authorization, in the PBS External Reference Specification. Format: &quot;[+|-]group_name[,&#8230;]&quot;; default value: all groups allowed. <i></p>
<dt>acl_host_enable</i></font><font SIZE="+4"><i></i></p>
<dd>Attribute which when true directs the server to use the <i>acl_hosts</i> access list. Format: boolean (see acl_group_enable); default value: disabled. <i></p>
<dt>acl_hosts</i></font><font SIZE="+5"><i></i></p>
<dd>List of hosts which may enqueue jobs in the queue. See section 10.1, Authorization, in the PBS External Reference Specification. Format: &quot;[+|-]hostname[&#8230;]&quot;; default value: all hosts allowed. <i></p>
<dt>acl_logic_or</i></font><font SIZE="+6"><i></i></p>
<dd>Modifies the way acls are applied if both <i>acl_user_enable</i> and <i>acl_group_enable</i> are set to true. If <i>acl_logic_or</i> is true, then user and group acls are logically OR&#8217;ed together (a job can pass either the user or group acl lists to be allowed access to the queue). If I acl_logic_or is false, then user and group acls are logically AND&#8217;ed together (a job would have to pass both user and group acl lists). Format: boolean (see acl_group_enable and acl_user_enable); default value: disabled. <i></p>
<dt>acl_user_enable</i></font><font SIZE="+7"><i></i></p>
<dd>Attribute which when true directs the server to use the the <i>acl_users</i> access list for this queue. Format: boolean (see acl_group_enable); default value: disabled. <i></p>
<dt>acl_users</i></font><font SIZE="+8"><i></i></p>
<dd>List of users allowed or denied the ability to enqueue jobs in this queue. See section 10.1, Authorization, in the PBS External Reference Specification. If acl_user_enable is set to true, only users listed in the acl_groups attribute will be allowed access to the queue. </p>
<p> Format: &quot;[+|-]user[@host][,&#8230;]&quot;; default value: all users allowed. <i></p>
<dt>disallowed_types</i></font><font SIZE="+9"><i></i></p>
<dd>List of job &quot;types&quot; (interactive,batch,rerunable,nonrerunable,fault_tolerant,fault_intolerant) that are not allowed in this queue. </p>
<p> default value: all types allowed. <i></p>
<dt>enabled</i></p>
<dd>Queue will or will not accept new jobs. When false the queue is disabled and will not accept jobs. Format: boolean (see acl_group_enable); default value: disabled. <i></p>
<dt>from_route_only</i></p>
<dd>When true, this queue will not accept jobs except when being routed by the server from a local routing queue. This is used to force user to submit jobs into a routing queue used to distribute jobs to other queues based on job resource limits. Format: boolean; default value: disabled. <i></p>
<dt>is_transit</i></p>
<dd>When true, jobs will be allowed into this queue that do not fit server resource limitations. This is to allow the jobs to be routed to a server that does have the appropriate resources. Any queue limits are checked. <i></p>
<dt>max_queuable</i></p>
<dd>The maximum number of jobs allowed to reside in the queue at any given time. Format: integer; default value: infinite. <i></p>
<dt>max_user_queuable</i></p>
<dd>The maximum number of jobs owned by a single user that are allowed to reside in the queue at any given time. Format: integer; default value: infinite. <i></p>
<dt>max_running</i></p>
<dd>The maximum number of jobs allowed to be selected from this queue for routing or execution at any given time. For a routing queue, this is enforced, if set, by the server. For an execution queue, this attribute is advisory to the Scheduler, it is not enforced by the server. Format: integer. <i></p>
<dt>Priority</i></p>
<dd>The priority of this queue against other queues of the same type on this server. May affect job selection for execution/routing. Advisory to the Scheduler, not used by the server. Format: integer. <i></p>
<dt>queue_type</i></p>
<dd>The type of the queue: execution or route. Format: &quot;execution&quot;, &quot;e&quot;, &quot;route&quot;, &quot;r&quot;. This attribute must be explicitly set. <i></p>
<dt>resources_max</i></p>
<dd>The maximum amount of each resource which can be requested by a single job in this queue. The queue value supersedes any server wide maximum limit. Format: &quot;resources_max.resource_name=value&quot;, see <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B); default value: infinite usage. <i></p>
<dt>resources_min</i></p>
<dd>The minimum amount of each resource which can be requested by a single job in this queue. Format: see resources_max, default value: zero usage. <i></p>
<dt>resources_default</i></p>
<dd>The list of default resource values which are set as limits for a job residing in this queue and for which the job did not specify a limit. Format: &quot;resources_default.resource_name=value&quot;, see <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B); default value: none; if not set, the default limit for a job is determined by the first of the following attributes which is set: server&#8217;s resources_default, queue&#8217;s resources_max, server&#8217;s resources_max. If none of these are set, the job will unlimited resource usage. <i></p>
<dt>started&nbsp;<wbr></i></p>
<dd>Jobs may be scheduled for execution from this queue. When false, the queue is considered stopped. Advisory to the Scheduler, not enforced by the server. [default value: false, but depends on scheduler interpretation] Format: boolean (see acl_group_enable).</dl>
</dl>
<p> The following attributes apply only to execution queues:</p>
<dl>
<dd><i></p>
<dl>
<dt>checkpoint_defaults</i></p>
<dd>Specifies the queues default checkpointing values to be used for a job that does not have any checkpointing specified. Format: string; default value: none. <i></p>
<dt>checkpoint_min</i></p>
<dd>Specifies the minimum interval of cpu time, in minutes, which is allowed between checkpoints of a job. If a user specifies a time less than this value, this value is used instead. Format: integer; default value: no minimum. <i></p>
<dt>resources_available</i></p>
<dd>The list of resource and amounts available to jobs running in this queue. The sum of the resource of each type used by all jobs running from this queue cannot exceed the total amount listed here. Advisory to the Scheduler, not enforced by the server. Format: &quot;resources_available.resource_name=value&quot;, see <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B). <i></p>
<dt>keep_completed</i></p>
<dd>Number of seconds to retain completed jobs in the C state. This overrides the server attribute of the same name. EXPERIMENTAL Format: integer; default value: 0. <i></p>
<dt>kill_delay</i></p>
<dd>The amount of the time delay between the sending of SIGTERM and SIGKILL when a qdel command is issued against a running job. This overrides the server attribute of the same name. Format: integer seconds; default value: 2 seconds. <i></p>
<dt>max_user_run</i></p>
<dd>The maximum number of jobs owned by a single user that are allowed to be running from this queue at one time. This attribute is advisory to the Scheduler, it is not enforced by the server. Format: integer; default value: none. <i></p>
<dt>max_group_run</i></p>
<dd>The maximum number of jobs owned by any users in a single group that are allowed to be running from this queue at one time. This attribute is advisory to the Scheduler, it is not enforced by the server. Format: integer; default value: none.</dl>
</dl>
<p> The following attributes apply only to routing queues:</p>
<dl>
<dd><i></p>
<dl>
<dt>route_destinations</i></p>
<dd>The list of destinations to which jobs may be routed. [default value: none, should be set to at least one valid destination] <i></p>
<dt>alt_router</i></p>
<dd>If true, an site supplied, alternative job router function is used to determine the destination for routing jobs from this queue. Otherwise, the default, round-robin router is used. Format: boolean (see acl_group_enable); default value: false. <i></p>
<dt>route_held_jobs</i></p>
<dd>If true, jobs with a hold type set may be routed from this queue. If false, held jobs are not to be routed. Format: boolean (see acl_group_enable); default value: false. <i></p>
<dt>route_waiting_jobs</i></p>
<dd>If true, jobs with a future <i> </i></font><font SIZE="+8"><i> attribute may be routed from this queue. If false, they are not to be routed. Format: boolean (see acl_group_enable); default value: false.</p>
<dt>route_retry_time</i></font><font SIZE="+9"><i></i></p>
<dd>Time delay between route retries. Typically used when the network between servers is down. Format: integer seconds; default value: </font><font SIZE="+8"><code>{PBS_NET_RETRY_TIME}</code></font><font SIZE="+9"> (30 seconds). <i></p>
<dt>route_lifetime</i></p>
<dd>The maximum time a job is allowed to exist in a routing queue. If the job cannot be routed in this amount of time, the job is aborted. If unset or set to a value of zero (0), the lifetime is infinite. Format: integer seconds; default infinite.</dl>
</dl>
<p> The following data items are read-only attributes of the queue. They are visible to but cannot be changed by clients. </p>
<p> Items which apply to all types of queues are:</p>
<dl>
<dd><i></p>
<dl>
<dt>total_jobs</i></p>
<dd>The number of jobs currently residing in the queue. <i></p>
<dt>state_count</i></p>
<dd>The total number of jobs currently residing in the queue in each state.</dl>
</dl>
<p> These read-only attributes only apply to execution queues:</p>
<dl>
<dd><i></p>
<dl>
<dt>resources_assigned</i></p>
<dd>The total amount of certain types of resources allocated to jobs running from this queue.</dl>
</dl>
<p> </font></p>
<h2>See Also</h2>
<p>the PBS ERS, <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources/">pbs_resources</a>(7B) </p>
