---
title: "qdel(1)"
name: "qdel"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qdel/"
description: "qdel – delete xxQS_NAMExx jobs from queues"
---

<h2 class="name">NAME</h2>
<p> qdel &#8211; delete xxQS_NAMExx jobs from queues </p>
<h2>SYNTAX</h2>
<p> <code>qdel</code> [<code>-f</code>] [<code>-help</code>] [<code>-u</code> <i>wc_user_list</i>] [<i>wc_job_range_list</i>] [<code>-t</code> <i>task_id_range</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qdel</i> provides a means for a user/operator/manager to delete one or more jobs. A manager/operator can delete jobs belonging to any user, while a regular user can only delete his or her own jobs. If a manager wants to delete another user&#8217;s job, the manager can specify the job id. A manager using a job name or pattern must also specify the user&#8217;s name via &quot;-u wc_user_list&quot;. A &quot;qdel wc_job_name&quot; will delete only the jobs of the calling user by default. <i>Qdel</i> deletes jobs in the order in which their job identifiers are presented. Find additional information concerning <i>wc_user_list</i> and <i>wc_job_list</i> in</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Force deletion of job(s). The job(s) are deleted from the list of jobs registered at even if the controlling the job(s) does not respond to the delete request sent by </p>
<p> Users who are neither xxQS_NAMExx managers nor operators can only use the <code>-f</code> option (for their own jobs) if the cluster configuration entry <code>qmaster_params</code> contains the flag ENABLE_FORCED_QDEL (see However, the behavior for administrative and non-administrative users differs. Jobs are deleted from the xxQS_NAMExx database immediately in the case of administrators. Otherwise, a regular deletion is attempted first and a forced cancellation is only executed if the regular deletion was unsuccessful. </p>
<p> Additionally, regular qdel requests can result in a forced deletion of a job if <code>ENABLE_FORCED_QDEL_IF_UNKNOWN</code> is set in the <code>qmaster_params</code> (see</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-t</code></p>
<dd> Deletes specified tasks of an array job. It means tasks created by the <i>qsub -t</i> command. For example, after creating an array job with the command &quot;qsub -t 1-100 $SGE_ROOT/examples/sleeper.sh&quot; it is possible to delete tasks 5-10 from the job array with the command &quot;qdel job_id -t 5-10&quot;. All other tasks (1-4 and 11-100) will be executed.</p>
<dt><code>-u wc_user_list</code></p>
<dd> Deletes only those jobs which were submitted by users specified in the list of usernames. For managers it is possible to use <code>qdel -u &quot;*&quot;</code> to delete all jobs of all users. If a manager wants to delete a specific job of a user, he has to specify the user and the job. If no job is specified, all jobs from that user are deleted.</p>
<dt><code>wc_job_range_list</code></p>
<dd> A list of jobs which should be deleted.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qdel</i> uses (in the order of precedence): </p>
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
