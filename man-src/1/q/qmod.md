---
title: "qmod(1)"
name: "qmod"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmod/"
description: "qmod – modify a xxQS_NAMExx queue and running job"
---

<h2 class="name">NAME</h2>
<p> qmod &#8211; modify a xxQS_NAMExx queue and running job </p>
<h2>SYNTAX</h2>
<p> <code>qmod</code> [<i>options</i>] [<i>wc_job_range_list</i>|<i>wc_queue_list</i>] </p>
<h2>DESCRIPTION</h2>
<p> <i>Qmod</i> enables users classified as <i>owners</i> (see for details) of a workstation to modify the state of xxQS_NAMExx queues for their machine as well as the state of their own jobs. A manager/operator, or root, can execute <i>qmod</i> for any queue and job in a cluster, but only from administrative hosts. Find additional information concerning <i>wc_queue_list</i> and <i>wc_job_list</i> in</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;clear</code></dt>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-cj</code> or <code>-cq</code> switch instead.<br />
 Clears the error state of the specified jobs(s)/queue(s).</dd>
<dt><code>-cj</code></dt>
<dd>
</dd><dt><code>&#8211;clearjob</code></dt>
<dd> Clears the error state of the specified jobs(s).</dd>
<dt><code>-cq</code></dt>
<dd>
</dd><dt><code>&#8211;clearqueue</code></dt>
<dd> Clears the error state of the specified queue(s).</dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;disable</code></dt>
<dd> Disables the queue(s), i.e. no further jobs are dispatched to disabled queues while jobs already executing in these queues are allowed to finish.</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>&#8211;enable</code></dt>
<dd> Enables the queue(s).</dd>
<dt><code>-f</code></dt>
<dd>
</dd><dt><code>&#8211;force</code></dt>
<dd> Force the modification action for the queue despite the apparent current state of the queue. For example if a queue appears to be suspended but the job execution seems to be continuing, the manager/operator can force a suspend operation on the jobs. In any case, the queue or job status will be set, even if the controlling the queues/jobs cannot be reached. Requires manager/operator privileges.</dd>
<dt><code>-help</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Prints a listing of all options.</dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;reschedule</code></dt>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-rj</code> or <code>-rq</code> switch instead.<br />
 If applied to queues, reschedules all jobs currently running in this queue. If applied to running jobs, reschedules the jobs. Requires root or manager privileges. In order for a job to be rescheduled, it, or the queue in which it is executing must have the rerun flag activated. (See -r option in the man page and the <i>rerun</i> option in the man page for more information.) Additional restrictions apply for parallel and checkpointing jobs. (See the <i>reschedule_unknown</i> description in the man page for details).</dd>
<dt><code>-rj</code></dt>
<dd>
</dd><dt><code>&#8211;reschedulejob</code></dt>
<dd> If applied to running jobs, reschedules the jobs. Requires root or manager privileges.</dd>
<dt><code>-rq</code></dt>
<dd>
</dd><dt><code>&#8211;reschedulequeue</code></dt>
<dd> Reschedules all jobs currently running in the specified queues. Requires root or manager privileges.</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;suspend</code></dt>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-sj</code> or <code>-sq</code> switch instead.<br />
 If applied to queues, suspends the queues and any jobs which might be active in them. If applied to running jobs, suspends the jobs.</dd>
<dt><code>-sj</code></dt>
<dd>
</dd><dt><code>&#8211;suspendjob</code></dt>
<dd> If applied to running jobs, suspends the jobs. If a job is both suspended explicitly and via suspension of its queue, a subsequent unsuspend of the queue will not release the suspension state on the job.</dd>
<dt><code>-sq</code></dt>
<dd>
</dd><dt><code>&#8211;suspendqueue</code></dt>
<dd> Suspends the specified queues and any jobs which might be active in them.</dd>
<dt><code>-us</code></dt>
<dd>
</dd><dt><code>&#8211;unsuspend</code></dt>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-usj</code> or <code>-usq</code> switch instead.<br />
 If applied to queues, unsuspends the queues and any jobs which might be active in them. If applied to jobs, unsuspends the jobs.</dd>
<dt><code>-usj</code></dt>
<dd>
</dd><dt><code>&#8211;unsuspendjob</code></dt>
<dd> Unsuspends the specified jobs. If a job is both suspended explicitly and via suspension of its queue, a subsequent unsuspend of the queue will not release the suspension state on the job.</dd>
<dt><code>-usq</code></dt>
<dd>
</dd><dt><code>&#8211;unsuspendqueue</code></dt>
<dd> Unsuspends the specified queues and any jobs which might be active in them.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></dt>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</dd>
<dt><code>xxQS_NAME_Sxx_CELL</code></dt>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qmod</i> uses (in the order of precedence): </dd>
<dl>
<dl>
<dt>
</dt><dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </dd>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></dt>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</dd>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></dt>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dd></dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
