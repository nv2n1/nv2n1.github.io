---
title: "drmaa_jobcontrol(3)"
name: "drmaa_jobcontrol"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_jobcontrol/"
description: "drmaa_job_ps, drmaa_control, – Monitor and control jobs"
---

<h2 class="name">NAME</h2>
<p> drmaa_job_ps, drmaa_control, &#8211; Monitor and control jobs</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
int drmaa_job_ps(
const char *job_id,
int *remote_ps,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<pre><code>
int drmaa_control(
const char *jobid,
int&amp;nbsp;action,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The drmaa_job_ps() function returns the status of the xxQS_NAMExx job <i>job_id</i> into the integer pointed to by <i>remote_ps</i>. Possible return values are listed below. See for the correspondence between them and the xxQS_NAMExx status. </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>DRMAA_PS_UNDETERMINED </td>
<td> job status cannot be determined
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_QUEUED_ACTIVE </td>
<td> job is queued and active
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_SYSTEM_ON_HOLD </td>
<td> job is queued and in system hold
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_USER_ON_HOLD </td>
<td> job is queued and in user hold
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_USER_SYSTEM_ON_HOLD </td>
<td> job is queued and in user and system hold
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_RUNNING </td>
<td> job is running
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_SYSTEM_SUSPENDED </td>
<td> job is system suspended
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_USER_SUSPENDED </td>
<td> job is user suspended
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_DONE </td>
<td> job finished normally
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_PS_FAILED </td>
<td> job finished, but failed
</td>
</tr>
</table>
</dl>
<p> Jobs&#8217; user hold and user suspend states can be controlled via For affecting system hold and system suspend states the appropriate xxQS_NAMExx interfaces must be used.</p>
<h3>drmaa_control()</h3>
<p> The drmaa_control() function applies control operations on xxQS_NAMExx jobs. <i>jobid</i> may contain either an xxQS_NAMExx jobid or `DRMAA_JOB_IDS_SESSION_ALL&#8217; to refer to all jobs submitted during the DRMAA session opened using Legal values for <i>action</i> and their meanings are: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>DRMAA_CONTROL_SUSPEND </td>
<td> suspend the job
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_CONTROL_RESUME </td>
<td> resume the job
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_CONTROL_HOLD </td>
<td> put the job on-hold
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_CONTROL_RELEASE </td>
<td> release the hold on the job
</td>
</tr>
<tr VALIGN=top>
<td>DRMAA_CONTROL_TERMINATE </td>
<td> kill the job
</td>
</tr>
</table>
</dl>
<p> The DRMAA suspend/resume operations are equivalent to the use of <code>-sj&nbsp;</code><i>jobid</i> and <code>-usj&nbsp;</code><i>jobid</i> options with xxQS_NAMExx The DRMAA hold/release operations are equivalent to the use of xxQS_NAMExx and The DRMAA terminate operation is equivalent to the use of xxQS_NAMExx Only user hold and user suspend can be controlled via For affecting system hold and system suspend states the appropriate xxQS_NAMExx interfaces must be used. </p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell to be used. To address a xxQS_NAMExx cell xxQS_NAMExx uses (in the order of precedence): </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_job_ps(), and drmaa_control() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer, <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_job_ps() and drmaa_control() functions may fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INTERNAL_ERROR</code></p>
<dd> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<dt><code>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</code></p>
<dd> Could not contact DRM system for this request.</p>
<dt><code>DRMAA_ERRNO_AUTH_FAILURE</code></p>
<dd> The specified request was not processed successfully due to authorization failure.</p>
<dt><code>DRMAA_ERRNO_INVALID_ARGUMENT</code></p>
<dd> The input value for an argument is invalid.</p>
<dt><code>DRMAA_ERRNO_NO_ACTIVE_SESSION</code></p>
<dd> Failed because there is no active session.</p>
<dt><code>DRMAA_ERRNO_NO_MEMORY</code></p>
<dd> Failed allocating memory.</p>
<dt><code>DRMAA_ERRNO_INVALID_JOB</code></p>
<dd> The specified job does not exist.</dl>
<p> The drmaa_control() function may fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_RESUME_INCONSISTENT_STATE</code></p>
<dd> The job is not suspended. The resume request will not be processed.</p>
<dt><code>DRMAA_ERRNO_SUSPEND_INCONSISTENT_STATE</code></p>
<dd> The job is not running and thus cannot be suspended.</p>
<dt><code>DRMAA_ERRNO_HOLD_INCONSISTENT_STATE</code></p>
<dd> The job cannot be moved to a hold state.</p>
<dt><code>DRMAA_ERRNO_RELEASE_INCONSISTENT_STATE</code></p>
<dd> The job is not in a hold state.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
