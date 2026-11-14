---
title: "accounting(5)"
name: "accounting"
section: "5"
letter: "a"
url: "/docs/linux/man/5-accounting/"
description: "accounting – xxQS_NAMExx accounting file format"
---

<p>accounting &#8211; xxQS_NAMExx accounting file format</p>
<h2>Description</h2>
<p>An accounting record is written to the xxQS_NAMExx accounting file <i>$SGE_ROOT/$SGE_CELL/common/reporting</i> for each finished job if <code>accounting=true</code> is specified in the <code>reporting_params</code>. This occurs at intervals of the <code>accounting_flush_time</code> specified in the same place. The accounting file is processed by to derive accounting statistics. </p>
<p> If output to the file is enabled, accounting records containing similar data are written there. They include &quot;intermediate&quot; records written at midnight for long-running jobs, not just ones written at the end of the jobs, and so may be more appropriate to process for some purposes than the accounting file.</p>
<h2>Format</h2>
<p>Each job is represented by a line in the accounting file. Empty lines, and lines which contain one character or less are ignored by <i>qacct</i>. Accounting record entries are separated by colon (&#8216;:&#8217;) characters. The entries denote in their order of appearance:</p>
<h3><code>1. qname</code></h3>
<p>Name of the cluster queue in which the job has run.</p>
<h3><code>2. hostname</code></h3>
<p>Name of the execution host.</p>
<h3><code>3. group</code></h3>
<p>The effective group id of the job owner when executing the job.</p>
<h3><code>4. owner</code></h3>
<p>Owner of the xxQS_NAMExx job.</p>
<h3><code>5. job_name</code></h3>
<p>Job name.</p>
<h3><code>6. job_number</code></h3>
<p>Job identifier (job number).</p>
<h3><code>7. account</code></h3>
<p>An account string as specified by the or <code>-A</code> option.</p>
<h3><code>8. priority</code></h3>
<p>Priority value assigned to the job, corresponding to the <code>priority</code> parameter in the queue configuration (see</p>
<h3><code>9. submission_time</code></h3>
<p>Submission time in seconds since the Unix epoch (1970-01-01 00:00:00 UTC).</p>
<h3><code>10. start_time</code></h3>
<p>Start time in seconds since the epoch.</p>
<h3><code>11. end_time</code></h3>
<p>End time in seconds since the epoch.</p>
<h3><code>12. failed</code></h3>
<p>Indicates the problem which occurred in case a job failed (at the system level, as opposed to the job script or binary having non-zero exit status, see below). Possibly the job could not be started on the execution host (e.g. because the owner of the job did not have a valid account on that machine), or didn&#8217;t finish successfully (e.g. because an execution host crashed). If xxQS_NAMExx tries to start a job multiple times, there may be multiple entries in the reporting file corresponding to the same job ID. See for a list.</p>
<h3><code>13. exit_status</code></h3>
<p>Exit status of the job script (or xxQS_NAMExx-specific status in case of certain error conditions). The exit status is determined by following the normal shell conventions. If the command terminates normally the value of the command is its exit status. However, in the case that the command exits abnormally, a value of 0200 (octal), 128 (decimal) is added to the value of the command to make up the exit status. </p>
<p> For example: If a job dies through signal 9 (SIGKILL) &#8211; probably issued by xxQS_NAMExx through or because the job exceeded time or memory hard limits &#8211; then the exit status is 128&nbsp;+&nbsp;9&nbsp;=&nbsp;137. The reason xxQS_NAMExx killed a job is recorded in the execd <i>messages</i> file at &quot;W&quot; or &quot;I&quot; level, depending on why it was killed.</p>
<h3><code>14. ru_wallclock</code></h3>
<p>Difference between <code>end_time</code> and <code>start_time</code> (see above), except that if the job fails, it is zero.</p>
<h3><code>15. ru_utime</code></h3>
<h3><code>16. ru_stime</code></h3>
<h3><code>17. ru_maxrss</code></h3>
<h3><code>18. ru_ixrss</code></h3>
<h3><code>19. ru_ismrss</code></h3>
<h3><code>20. ru_idrss</code></h3>
<h3><code>21. ru_isrss</code></h3>
<h3><code>22. ru_minflt</code></h3>
<h3><code>23. ru_majflt</code></h3>
<h3><code>24. ru_nswap</code></h3>
<h3><code>25. ru_inblock</code></h3>
<h3><code>26. ru_oublock</code></h3>
<h3><code>27. ru_msgsnd</code></h3>
<h3><code>28. ru_msgrcv</code></h3>
<h3><code>29. ru_nsignals</code></h3>
<h3><code>30. ru_nvcsw</code></h3>
<h3><code>31. ru_nivcsw</code></h3>
<p>These entries follow the contents of the standard Unix rusage structure as described in Depending on the operating system where the job was executed, some of the fields may be 0.</p>
<h3><code>32. project</code></h3>
<p>The project which was assigned to the job.</p>
<h3><code>33. department</code></h3>
<p>The department which was assigned to the job.</p>
<h3><code>34. granted_pe</code></h3>
<p>The parallel environment which was selected for the job.</p>
<h3><code>35. slots</code></h3>
<p>The number of slots which were dispatched to the job by the scheduler.</p>
<h3><code>36. task_number</code></h3>
<p>Array job task index number, or 0 for non-array jobs.</p>
<h3><code>37. cpu</code></h3>
<p>The CPU time usage in seconds. The value may be affected by the ACCT_RESERVED_USAGE execd parameter (see</p>
<h3><code>38. mem</code></h3>
<p>The integral memory usage in Gbytes seconds. The value may be affected by the ACCT_RESERVED_USAGE execd parameter (see</p>
<h3><code>39. io</code></h3>
<p>The amount of data transferred in input/output operations in GB (if available, otherwise 0). On Linux, this is summed over calls to <i><a href="/docs/linux/man/2-read/">read</a></i>(2), <i><a href="/docs/linux/man/2-pread/">pread</a></i>(2), <i><a href="/docs/linux/man/2-write/">write</a></i>(2), and <i><a href="/docs/linux/man/2-pwrite/">pwrite</a></i>(2); thus it includes i/o via cache, and may not reflect data actually written to file system. Your mileage may vary similarly on other systems.</p>
<h3><code>40. category</code></h3>
<p>A string specifying the job category. This contains a space-separated pseudo options list for the job, with components as follows:</p>
<dl>
<dt><code>-U</code> <i>user_list</i></p>
<dd>An owner/group ACL list composed from And <code>user_lists</code>/<code>xuser_lists</code> entries. Entries from are not considered since they can only cause a job to be accepted/rejected at submit time. Omitted if there are no such configuration entries.</p>
<dt><code>-P</code> <i>project_list</i></p>
<dd>Like <code>-U</code>, but for <code>project</code>/<code>xproject</code> entries.</p>
<dt><code>-u</code> <i>owner</i></p>
<dd>The owner&#8217;s user name, if it was referenced in any RQS (see Omitted if there was no such reference.</p>
<dt><code>-q</code> <i>queue_list</i></p>
<dd>The hard queue list (only if one was specified).</p>
<dt><code>-masterq</code> <i>queue_list</i></p>
<dd>The master queue list (only if one was specified).</p>
<dt><code>-l</code> <i>resource_list</i></p>
<dd>The hard resource list (only if hard resources were specified).</p>
<dt><code>-soft -l</code> <i>resource_list</i></p>
<dd>The soft resource list (only if soft resources were specified).</p>
<dt><code>-pe</code> <i>pe_name pe_range</i></p>
<dd>The parallel environment specified for the job (only for parallel jobs).</p>
<dt><code>-ckpt </code><i>ckpt_name</i></p>
<dd>The job&#8217;s checkpointing environment (only if one was specified).</p>
<dt><code>-I </code><i>y</i></p>
<dd>Present only for interactive jobs.</p>
<dt><code>-ar </code><i>ar_id</i></p>
<dd>The advance reservation into which the job was submitted (only if one was specified).</dl>
<h3><code>41. iow</code></h3>
<p>The input/output wait time in seconds (if available, otherwise 0).</p>
<h3><code>42. pe_taskid</code></h3>
<p>If this identifier is not equal to <code>NONE</code>, the task was part of a parallel job, and was passed to xxQS_NAMExx via the <code>qrsh -inherit</code> interface. Such records are not produced if the PE&#8217;s <code>accounting_summary</code> parameter is false (see</p>
<h3><code>43. maxvmem</code></h3>
<p>The maximum vmem size in bytes. The value may be affected by the ACCT_RESERVED_USAGE execd parameter (see</p>
<h3><code>44. arid</code></h3>
<p>Advance reservation identifier. If the job used the resources of an advance reservation, then this field contains a positive integer identifier; otherwise the value is &quot;<code>0</code>&quot;.</p>
<h3><code>45. ar_sub_time</code></h3>
<p>Advance reservation submission time if the job uses the resources of an advance reservation; otherwise &quot;<code>0</code>&quot;.</p>
<h2>Files</h2>
<p><i>$SGE_ROOT/$SGE_CELL/common/accounting</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/2-getrusage/">getrusage</a></i>(2),</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
