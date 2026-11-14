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
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;clear</code></p>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-cj</code> or <code>-cq</code> switch instead.<br />
 Clears the error state of the specified jobs(s)/queue(s).</p>
<dt><code>-cj</code></p>
<dd>
<dt><code>&#8211;clearjob</code></p>
<dd> Clears the error state of the specified jobs(s).</p>
<dt><code>-cq</code></p>
<dd>
<dt><code>&#8211;clearqueue</code></p>
<dd> Clears the error state of the specified queue(s).</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;disable</code></p>
<dd> Disables the queue(s), i.e. no further jobs are dispatched to disabled queues while jobs already executing in these queues are allowed to finish.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;enable</code></p>
<dd> Enables the queue(s).</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;force</code></p>
<dd> Force the modification action for the queue despite the apparent current state of the queue. For example if a queue appears to be suspended but the job execution seems to be continuing, the manager/operator can force a suspend operation on the jobs. In any case, the queue or job status will be set, even if the controlling the queues/jobs cannot be reached. Requires manager/operator privileges.</p>
<dt><code>-help</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;reschedule</code></p>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-rj</code> or <code>-rq</code> switch instead.<br />
 If applied to queues, reschedules all jobs currently running in this queue. If applied to running jobs, reschedules the jobs. Requires root or manager privileges. In order for a job to be rescheduled, it, or the queue in which it is executing must have the rerun flag activated. (See -r option in the man page and the <i>rerun</i> option in the man page for more information.) Additional restrictions apply for parallel and checkpointing jobs. (See the <i>reschedule_unknown</i> description in the man page for details).</p>
<dt><code>-rj</code></p>
<dd>
<dt><code>&#8211;reschedulejob</code></p>
<dd> If applied to running jobs, reschedules the jobs. Requires root or manager privileges.</p>
<dt><code>-rq</code></p>
<dd>
<dt><code>&#8211;reschedulequeue</code></p>
<dd> Reschedules all jobs currently running in the specified queues. Requires root or manager privileges.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;suspend</code></p>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-sj</code> or <code>-sq</code> switch instead.<br />
 If applied to queues, suspends the queues and any jobs which might be active in them. If applied to running jobs, suspends the jobs.</p>
<dt><code>-sj</code></p>
<dd>
<dt><code>&#8211;suspendjob</code></p>
<dd> If applied to running jobs, suspends the jobs. If a job is both suspended explicitly and via suspension of its queue, a subsequent unsuspend of the queue will not release the suspension state on the job.</p>
<dt><code>-sq</code></p>
<dd>
<dt><code>&#8211;suspendqueue</code></p>
<dd> Suspends the specified queues and any jobs which might be active in them.</p>
<dt><code>-us</code></p>
<dd>
<dt><code>&#8211;unsuspend</code></p>
<dd> <code>Note:</code> Deprecated, may be removed in future release. Please use the <code>-usj</code> or <code>-usq</code> switch instead.<br />
 If applied to queues, unsuspends the queues and any jobs which might be active in them. If applied to jobs, unsuspends the jobs.</p>
<dt><code>-usj</code></p>
<dd>
<dt><code>&#8211;unsuspendjob</code></p>
<dd> Unsuspends the specified jobs. If a job is both suspended explicitly and via suspension of its queue, a subsequent unsuspend of the queue will not release the suspension state on the job.</p>
<dt><code>-usq</code></p>
<dd>
<dt><code>&#8211;unsuspendqueue</code></p>
<dd> Unsuspends the specified queues and any jobs which might be active in them.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qmod</i> uses (in the order of precedence): </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
