---
title: "drmaa_wait(3)"
name: "drmaa_wait"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_wait/"
description: "drmaa_synchronize, drmaa_wait, drmaa_wifexited, drmaa_wexitstatus, drmaa_wifsignaled, drmaa_wtermsig, drmaa_wcoredump, drmaa_wifaborted – Waiting for jobs to finish"
---

<h2 class="name">NAME</h2>
<p> drmaa_synchronize, drmaa_wait, drmaa_wifexited, drmaa_wexitstatus, drmaa_wifsignaled, drmaa_wtermsig, drmaa_wcoredump, drmaa_wifaborted &#8211; Waiting for jobs to finish</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
int drmaa_synchronize(
const char *job_ids[],
signed long timeout,
int&amp;nbsp;dispose,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<p>int drmaa_wait(<br />
const char *job_id,<br />
char *job_id_out,<br />
size_t job_id_out_len,<br />
int *stat,<br />
signed long timeout,<br />
drmaa_attr_values_t **rusage,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diagnois_len<br />
 <code>);</code> </p>
<p>int drmaa_wifaborted(<br />
int *aborted,<br />
int&amp;nbsp;stat,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_wifexited(<br />
int *exited,<br />
int&amp;nbsp;stat,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_wifsignaled(<br />
int *signaled,<br />
int&amp;nbsp;stat,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_wcoredump(<br />
int *core_dumped,<br />
int&amp;nbsp;stat,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_wexitstatus(<br />
int *exit_status,<br />
int&amp;nbsp;stat,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<pre><code>
int drmaa_wtermsig(
char *signal,
size_t&amp;nbsp;signal_len,
int&amp;nbsp;stat,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The drmaa_synchronize() function blocks the calling thread until all jobs specified in <i>job_ids</i> have failed or finished execution. If <i>job_ids</i> contains &#8216;DRMAA_JOB_IDS_SESSION_ALL&#8217;, then this function waits for all jobs submitted during this DRMAA session. The <i>job_ids</i> pointer array must be NULL terminated. </p>
<p> To prevent blocking indefinitely in this call, the caller may use the <i>timeout</i>, specifying how many seconds to wait for this call to complete before timing out. The special value DRMAA_TIMEOUT_WAIT_FOREVER can be used to wait indefinitely for a result. The special value DRMAA_TIMEOUT_NO_WAIT can be used to return immediately. If the call exits before <i>timeout</i> seconds, all the specified jobs have completed or the calling thread received an interrupt. In both cases, the return code is DRMAA_ERRNO_EXIT_TIMEOUT. </p>
<p> The <i>dispose</i> parameter specifies how to treat reaping information. If &#8216;0&#8217; is passed to this parameter, job finish information will still be available when is used. If &#8216;1&#8217; is passed, will be unable to access this job&#8217;s finish information.</p>
<h3>drmaa_wait()</h3>
<p> The drmaa_wait() function blocks the calling thread until a job fails or finishes execution. This routine is modeled on the routine. If the special string &#8216;DRMAA_JOB_IDS_SESSION_ANY&#8217; is passed as <i>job_id</i>, this routine will wait for any job from the session. Otherwise the <i>job_id</i> must be the job identifier of a job or array job task that was submitted during the session. </p>
<p> To prevent blocking indefinitely in this call, the caller may use <i>timeout</i>, specifying how many seconds to wait for this call to complete before timing out. The special value DRMAA_TIMEOUT_WAIT_FOREVER can be to wait indefinitely for a result. The special value DRMAA_TIMEOUT_NO_WAIT can be used to return immediately. If the call exits before <i>timeout</i> seconds have passed, all the specified jobs have completed or the calling thread received an interrupt. In both cases, the return code is DRMAA_ERRNO_EXIT_TIMEOUT. </p>
<p> The routine reaps jobs on a successful call, so any subsequent calls to will fail returning a DRMAA_ERRNO_INVALID_JOB error, meaning that the job has already been reaped. This error is the same as if the job were unknown. Returning due to an elapsed timeout or an interrupt does not cause the job information to be reaped. This means that, in this case, it is possible to issue multiple times for the same <i>job_id</i>. </p>
<p> If <i>job_id_out</i> is not a null pointer, then on return from a successful call, up to <i>job_id_out_len</i> characters from the job id of the failed or finished job are returned. </p>
<p> If <i>stat</i> is not a null pointer, then on return from a successful call, the status of the job is stored in the integer pointed to by <i>stat</i>. <i>stat</i> indicates whether job failed or finished and other information. The information encoded in the integer value can be accessed via and </p>
<p> If <i>rusage</i> is not a null pointer, then on return from a successful call, a summary of the resources used by the terminated job is returned in form of a DRMAA values string vector. The entries in the DRMAA values string vector can be extracted using Each string returned by will be of the format <i>name</i><code>=</code><i>value</i>, where <i>name</i> and <i>value</i> specify name and amount of resources consumed by the job, respectively. See for an explanation of the resource information. </p>
<h3>drmaa_wifaborted()</h3>
<p> The drmaa_wifaborted() function evaluates into the integer pointed to by <i>aborted</i> a non-zero value if <i>stat</i> was returned from a job that ended before entering the running state. </p>
<h3>drmaa_wifexited()</h3>
<p> The drmaa_wifexited() function evaluates into the integer pointed to by <i>exited</i> a non-zero value if <i>stat</i> was returned from a job that terminated normally. A zero value can also indicate that although the job has terminated normally, an exit status is not available, or that it is not known whether the job terminated normally. In both cases will not provide exit status information. A non-zero value returned in <i>exited</i> indicates more detailed diagnosis can be provided by means of and </p>
<h3>drmaa_wifsignaled()</h3>
<p> The drmaa_wifsignaled() function evaluates into the integer pointed to by <i>signaled</i> a non-zero value if <i>stat</i> was returned for a job that terminated due to the receipt of a signal. A zero value can also indicate that although the job has terminated due to the receipt of a signal, the signal is not available, or it is not known whether the job terminated due to the receipt of a signal. In both cases will not provide signal information. A non-zero value returned in <i>signaled</i> indicates signal information can be retrieved by means of </p>
<h3>drmaa_wcoredump()</h3>
<p> If returned a non-zero value in the <i>signaled</i> parameter, the drmaa_wcoredump() function evaluates into the integer pointed to by <i>core_dumped</i> a non-zero value if a core image of the terminated job was created. </p>
<h3>drmaa_wexitstatus()</h3>
<p> If returned a non-zero value in the <i>exited</i> parameter, the drmaa_wexitstatus() function evaluates into the integer pointed to by <i>exit_code</i> the exit code that the job passed to or the value that the child process returned from main. </p>
<h3>drmaa_wtermsig()</h3>
<p> If returned a non-zero value in the <i>signaled</i> parameter, the drmaa_wtermsig() function evaluates into <i>signal</i> up to <i>signal_len</i> characters of a string representation of the signal that caused the termination of the job. For signals declared by POSIX.1, the symbolic names are returned (e.g., SIGABRT, SIGALRM). For signals not declared by POSIX, any other string may be returned. </p>
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
<p> Upon successful completion, drmaa_run_job(), drmaa_run_bulk_jobs(), and drmaa_get_next_job_id() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_synchronize(), drmaa_wait(), drmaa_wifexited(), drmaa_wexitstatus(), drmaa_wifsignaled(), drmaa_wtermsig(), drmaa_wcoredump(), and drmaa_wifaborted() functions can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INTERNAL_ERROR</code></p>
<dd> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<dt><code>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</code></p>
<dd> Could not contact DRM system for this request.</p>
<dt><code>DRMAA_ERRNO_AUTH_FAILURE</code></p>
<dd> The specified request is not processed successfully due to authorization failure.</p>
<dt><code>DRMAA_ERRNO_INVALID_ARGUMENT</code></p>
<dd> The input value for an argument is invalid.</p>
<dt><code>DRMAA_ERRNO_NO_ACTIVE_SESSION</code></p>
<dd> Failed because there is no active session.</p>
<dt><code>DRMAA_ERRNO_NO_MEMORY</code></p>
<dd> Failed allocating memory.</dl>
<p> The drmaa_synchronize() and drmaa_wait() functions can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_EXIT_TIMEOUT</code></p>
<dd> Time-out condition.</p>
<dt><code>DRMAA_ERRNO_INVALID_JOB</code></p>
<dd> The job specified by the does not exist.</dl>
<p> The drmaa_wait() can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_NO_RUSAGE</code></p>
<dd> This error code is returned by drmaa_wait() when a job has finished but no rusage and stat data could be provided.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
