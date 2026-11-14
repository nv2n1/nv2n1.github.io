---
title: "sge_shepherd(8)"
name: "sge_shepherd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_shepherd/"
description: "xxqs_name_sxx_shepherd – xxQS_NAMExx single job-controlling agent"
---

<p>xxqs_name_sxx_shepherd &#8211; xxQS_NAMExx single job-controlling agent</p>
<h2>Synopsis</h2>
<p><code>xxqs_name_sxx_shepherd</code></p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_shepherd</i> provides the parent process functionality for a single xxQS_NAMExx job. The parent functionality is necessary on UNIX systems to retrieve resource usage information (see after a job has finished. In addition, the <i>xxqs_name_sxx_shepherd</i> forwards signals to the job, such for suspension, enabling, termination, and the xxQS_NAMExx checkpointing signal (see and for details). </p>
<p> The <i>xxqs_name_sxx_shepherd</i> receives information about the job to be started from the During the execution of the job it actually starts up to 5 child processes. First a prolog script is run if this feature is enabled by the <code>prolog</code> parameter in the cluster configuration. (See Next a parallel environment startup procedure is run if the job is a parallel job. (See for more information.) After that, the job itself is run, followed by a parallel environment shutdown procedure for parallel jobs, and finally an epilog script if requested by the <code>epilog</code> parameter in the cluster configuration. The prolog and epilog scripts, as well as the parallel environment startup and shutdown procedures, are to be provided by the xxQS_NAMExx administrator and are intended for site-specific actions to be taken before and after execution of the actual user job. </p>
<p> After the job has finished and the epilog script is processed, <i>xxqs_name_sxx_shepherd</i> retrieves resource usage statistics about the job, places them in a job-specific subdirectory of the spool directory for reporting through and finishes. </p>
<p> <i>xxqs_name_sxx_shepherd</i> also places an exit status file in the spool directory. This exit status can be viewed with qacct -j JobId (see it is not the exit status of <i>xxqs_name_sxx_shepherd</i> itself but of one of the methods executed by <i>xxqs_name_sxx_shepherd.</i> This exit status can have several meanings, depending on the method in which an error occurred (if any). The possible methods are: prolog, parallel start, job, parallel stop, epilog, suspend, restart, terminate, clean, migrate, and checkpoint. </p>
<p> The following exit values are returned:</p>
<dl>
<dt>0</p>
<dd>All methods: Operation was executed successfully.</p>
<dt>99</p>
<dd>Job script, prolog and epilog: When <i>FORBID_RESCHEDULE </i> is not set in the configuration (see the job gets re-queued. Otherwise see &quot;Other&quot;.</p>
<dt>100</p>
<dd>Job script, prolog and epilog: When <i>FORBID_APPERROR</i> is not set in the configuration (see the job gets re-queued. Otherwise see &quot;Other&quot;.</p>
<dt>Other</p>
<dd>Job script: This is the exit status of the job itself. No action is taken upon this exit status because the meaning of this exit status is not known.<br />
 Prolog, epilog and parallel start: The queue is set to error state and the job is re-queued.<br />
 Parallel stop: The queue is set to error state, but the job is not re-queued. It is assumed that the job itself ran successfully and only the clean up script failed.<br />
 Suspend, restart, terminate, clean, and migrate: Always successful.<br />
 Checkpoint: Success, except for kernel checkpointing: checkpoint was not successful, did not happen (but migration will happen).</dl>
<p> For the meaning of the return codes of the shepherd itself (which are interpreted by see</p>
<h2>Restrictions</h2>
<p><i>xxqs_name_sxx_shepherd</i> should not be invoked manually, but only by</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd>Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd>If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>xxqs_name_sxx_execd</i> uses (in the order of precedence): </p>
<dl>
<dd>
<dl>
<dd>The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>SGE_ENABLE_COREDUMP</code></p>
<dd>If set, enable core dumps on Linux when the admin_user is not root. Linux normally disables core dumps when the daemon has changed uid or gid. Setting SGE_ENABLE_COREDUMP in xxqs_name_sxx_execd&#8217;s environment defeats that to enable core dumps for debugging if they are otherwise allowed. This is typically not a big hazard with xxQS_NAME_Sxx, since most information is exposed in the spool area anyhow. Dumps will appear in the qmaster spool directory, which need not be world-readable.<br />
 On Solaris, may be used to enable such dumps.</p>
<dt><code>SGE_CGROUP_DIR</code></p>
<dd>If Linux cgroups handling is enabled, this variable names a directory under the cgroup mount point in which to create job-specific directories. The default is <code>sge.</code><i>SGE_CELL</i> so, for instance, the cpuset cgroup for a job might be <code>/sys/fs/cgroup/cpuset/sge.default/123</code>.</dl>
<h2>Files</h2>
<p><code>sgepasswd</code> contains a list of user names and their corresponding encrypted passwords. If available, the password file will be used by <code>sge_shepherd</code>. To change the contents of this file please use the <code>sgepasswd</code> command. It is not advised to change that file manually. </p>
<pre><i>&lt;execd_spool&gt;/job_dir/&lt;job_id&gt;</i> job specific directory
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/sgepasswd</i>
 Password information used on Microsoft Windows hosts. See</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
