---
title: "globus_gram_protocol_job_signal_commit_request(3)"
name: "globus_gram_protocol_job_signal_commit_request"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_job_signal_commit_request/"
description: "GRAM Signals –"
---

<p>GRAM Signals &#8211; </p>
<p> GRAM Signals.</p>
<h3>Enumerations</h3>
<p>enum <code>globus_gram_protocol_job_signal_t</code> { <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_CANCEL</code> =1, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_SUSPEND</code> =2, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_RESUME</code> =3, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_PRIORITY</code> =4, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_REQUEST</code> =5, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_EXTEND</code> =6, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_UPDATE</code> =7, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_SIZE</code> =8, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STOP_MANAGER</code> =9, <code>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_END</code> =10 } </p>
<h2>Detailed Description</h2>
<p>GRAM Signals. </p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gram_protocol_job_signal_t</code></h3>
<p>GRAM Signals </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_CANCEL </i></p>
<dd>Cancel a job</p>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_SUSPEND </i></p>
<dd>Suspend a job</p>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_RESUME </i></p>
<dd>Resume a previously suspended job</p>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_PRIORITY </i></p>
<dd>Change the priority of a job</p>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_REQUEST </i></p>
<dd></dl>
<pre> Signal the job manager to commence with a job submission if the job</pre>
<p>&nbsp;<wbr>request was accompanied by the&nbsp;<wbr>(two_state=yes)&nbsp;<wbr>RSL attribute.&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_EXTEND </i></p>
<dd></dl>
<pre> Signal the job manager to wait an additional number of seconds</pre>
<p>&nbsp;<wbr>(specified by an integer value string as the signal&#8217;s argument)&nbsp;<wbr>before timing out a two-phase job commit.&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_UPDATE </i></p>
<dd></dl>
<pre> Signal the job manager to change the way it is currently handling</pre>
<p>&nbsp;<wbr>standard output and/or standard error. The argument for this signal is an RSL containing new&nbsp;<wbr><i>stdout</i>,&nbsp;<wbr><i>stderr</i>,&nbsp;<wbr><i>stdout_position</i>,&nbsp;<wbr><i>stderr_position</i>, or&nbsp;<wbr><i>remote_io_url</i>&nbsp;<wbr>relations.&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STDIO_SIZE </i></p>
<dd></dl>
<pre> Signal the job manager to verify that streamed I/O has been completely</pre>
<p>&nbsp;<wbr>received. The argument to this signal contains the number of bytes of stdout and stderr received, separated by a space. The reply to this signal will be a SUCCESS message if these matched the amount sent by the job manager. Otherwise, an error reply indicating GLOBUS_GRAM_PROTOCOL_ERROR_STDIO_SIZE is returned. If standard output and standard error are merged, only one number should be sent as an argument to this signal. An argument of -1 for either stream size indicates that the client is not interested in the size of that stream.&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_STOP_MANAGER </i></p>
<dd></dl>
<pre> Signal the job manager to stop managing the current job and terminate.</pre>
<p>&nbsp;<wbr>The job continues to run as normal. The job manager will send a state change callback with the job status being FAILED and the error GLOBUS_GRAM_PROTOCOL_ERROR_JM_STOPPED.&nbsp;<wbr></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_PROTOCOL_JOB_SIGNAL_COMMIT_END </i></p>
<dd></dl>
<pre> Signal the job manager to clean up after the completion of the job if</pre>
<p>&nbsp;<wbr>the job RSL contained the&nbsp;<wbr>(two-phase&nbsp;<wbr>=&nbsp;<wbr>yes)&nbsp;<wbr>relation.&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gram_protocol from the source code.</p>
