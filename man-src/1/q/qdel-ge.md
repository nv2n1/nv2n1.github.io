---
title: "qdel-ge(1)"
name: "qdel-ge"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qdel-ge/"
description: "qdel – delete Grid Engine jobs from queues"
---

<h2>NAME</h2>
<p> qdel &#8211; delete Grid Engine jobs from queues</p>
<h2>SYNTAX</h2>
<p> <code>qdel</code> [ <code>-f</code> ] [ <code>-help</code> ] [ <code>-u wc_user_list</code> ] [ <code>wc_job_range_list</code> ] [ <code>-t task_id_range</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qdel</i> provides a means for a user/operator/manager to delete one or more jobs. A manager/operator can delete jobs belonging to any user, while a regular user can only delete his or her own jobs. If a manager wants to delete another user&#8217;s job, the manager can specify the job id. If the manager is using a job name or pattern, he or she must also specify the user&#8217;s name via &quot;-u wc_user_list&quot;. A &quot;qdel wc_job_name&quot; will delete only the jobs of the calling user by default. <i>Qdel</i> deletes jobs in the order in which their job identifiers are presented. Find additional information concerning <i>wc_user_list</i> and <i>wc_job_list</i> in</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Force deletion of job(s). The job(s) are deleted from the list of jobs registered at even if the controlling the job(s) does not respond to the delete request sent by </p>
<p> Users which are neither Grid Engine managers nor operators can only use the <code>-f</code> option (for their own jobs) if the cluster configuration entry <code>qmaster_params</code> contains the flag ENABLE_FORCED_QDEL (see However, behavior for administrative and non-administrative users differs. Jobs are deleted from the Grid Engine database immediately in case of administrators. Otherwise, a regular deletion is attempted first and a forced cancellation is only executed if the regular deletion was unsuccessful. </p>
<p> Additionally regular qdel requests can result in a forced deletion of a job if <code>ENABLE_FORCED_QDEL_IF_UNKNOWN</code> is set in the <code>qmaster_params</code> (see</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-t</code></p>
<dd> Deletes specified tasks of array job. It means tasks created by qsub -t command. For example after creating array job by command &quot;qsub -t 1-100 $SGE_ROOT/examples/sleeper.sh&quot; it is possible to delete tasks 5-10 from job array by command &quot;qdel job_id -t 5-10&quot;. All other tasks (1-4 and 11-100) will be executed.</p>
<dt><code>-u wc_user_list</code></p>
<dd> Deletes only those jobs which were submitted by users specified in the list of usernames. For managers it is possible to use <code>qdel -u &quot;*&quot;</code> to delete all jobs of all users. If a manager wants to delete a specific job of a user, he has to specify the user and the job. If no job is specified all jobs from that user are deleted.</p>
<dt><code>wc_job_range_list</code></p>
<dd> A list of jobs, which should be deleted</dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>GE_ROOT</code></p>
<dd> Specifies the location of the Grid Engine standard configuration files.</p>
<dt><code>GE_CELL</code></p>
<dd> If set, specifies the default Grid Engine cell. To address a Grid Engine cell <i>qdel</i> uses (in the order of precedence): </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;ge_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
               Grid Engine master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
