---
title: "sge_accounting(5)"
name: "sge_accounting"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_accounting/"
description: "accounting – Grid Engine accounting file format"
---

<p>accounting &#8211; Grid Engine accounting file format</p>
<h2>Description</h2>
<p>An accounting record is written to the Grid Engine accounting file for each job having finished. The accounting file is processed by to derive accounting statistics.</p>
<h2>Format</h2>
<p>Each job is represented by a line in the accounting file. Empty lines and lines which contain one character or less are ignored. Accounting record entries are separated by colon (&#8216;:&#8217;) signs. The entries denote in their order of appearance:</p>
<h3><code>qname</code></h3>
<p>Name of the cluster queue in which the job has run.</p>
<h3><code>hostname</code></h3>
<p>Name of the execution host.</p>
<h3><code>group</code></h3>
<p>The effective group id of the job owner when executing the job.</p>
<h3><code>owner</code></h3>
<p>Owner of the Grid Engine job.</p>
<h3><code>job_name</code></h3>
<p>Job name.</p>
<h3><code>job_number</code></h3>
<p>Job identifier &#8211; job number.</p>
<h3><code>account</code></h3>
<p>An account string as specified by the or <code>-A</code> option.</p>
<dl>
<dt><code>priority</code></p>
<dd>Priority value assigned to the job corresponding to the <code>priority</code> parameter in the queue configuration (see</dl>
<h3><code>submission_time</code></h3>
<p>Submission time (GMT unix time stamp).</p>
<h3><code>start_time</code></h3>
<p>Start time (GMT unix time stamp).</p>
<h3><code>end_time</code></h3>
<p>End time (GMT unix time stamp).</p>
<h3><code>failed</code></h3>
<p>Indicates the problem which occurred in case a job could not be started on the execution host (e.g. because the owner of the job did not have a valid account on that machine). If Grid Engine tries to start a job multiple times, this may lead to multiple entries in the accounting file corresponding to the same job ID.</p>
<h3><code>exit_status</code></h3>
<p>Exit status of the job script (or Grid Engine specific status in case of certain error conditions). The exit status is determined by following the normal shell conventions. If the command terminates normally the value of the command is its exit status. However, in the case that the command exits abnormally, a value of 0200 (octal), 128 (decimal) is added to the value of the command to make up the exit status.</p>
<dl>
<dd>For example: If a job dies through signal 9 (SIGKILL) then the exit status becomes 128 + 9 = 137.</dl>
<h3><code>ru_wallclock</code></h3>
<p>Difference between <code>end_time</code> and <code>start_time</code> (see above). </p>
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
<h3><code>project</code></h3>
<p>The project which was assigned to the job.</p>
<h3><code>department</code></h3>
<p>The department which was assigned to the job.</p>
<h3><code>granted_pe</code></h3>
<p>The parallel environment which was selected for that job.</p>
<h3><code>slots</code></h3>
<p>The number of slots which were dispatched to the job by the scheduler.</p>
<h3><code>task_number</code></h3>
<p>Array job task index number.</p>
<h3><code>cpu</code></h3>
<p>The cpu time usage in seconds.</p>
<h3><code>mem</code></h3>
<p>The integral memory usage in Gbytes cpu seconds.</p>
<h3><code>io</code></h3>
<p>The amount of data transferred in input/output operations.</p>
<h3><code>category</code></h3>
<p>A string specifying the job category.</p>
<h3><code>iow</code></h3>
<p>The io wait time in seconds.</p>
<h3><code>pe_taskid</code></h3>
<p>If this identifier is set the task was part of a parallel job and was passed to Grid Engine via the qrsh -inherit interface.</p>
<h3><code>maxvmem</code></h3>
<p>The maximum vmem size in bytes.</p>
<h3><code>arid</code></h3>
<p>Advance reservation identifier. If the job used resources of an advance reservation then this field contains a positive integer identifier otherwise the value is &quot;<code>0</code>&quot; .</p>
<h3><code>ar_submission_time</code></h3>
<p>If the job used resources of an advance reservation then this field contains the submission time (GMT unix time stamp) of the advance reservation, otherwise the value is &quot;<code>0</code>&quot; .</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
