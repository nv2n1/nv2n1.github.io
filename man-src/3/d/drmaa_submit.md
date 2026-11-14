---
title: "drmaa_submit(3)"
name: "drmaa_submit"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_submit/"
description: "drmaa_run_job, drmaa_run_bulk_jobs, drmaa_get_next_job_id, drmaa_get_num_job_ids, drmaa_release_job_ids – Job submission"
---

<h2 class="name">NAME</h2>
<p> drmaa_run_job, drmaa_run_bulk_jobs, drmaa_get_next_job_id, drmaa_get_num_job_ids, drmaa_release_job_ids &#8211; Job submission</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
int drmaa_run_job(
char *job_id,
size_t&amp;nbsp;job_id_len,
drmaa_job_template_t *jt,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<p>int drmaa_run_bulk_jobs(<br />
drmaa_job_ids_t **jobids,<br />
drmaa_job_template_t *jt,<br />
int&amp;nbsp;start,<br />
int&amp;nbsp;end,<br />
int&amp;nbsp;incr,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<pre><code>
int drmaa_get_next_job_id(
drmaa_job_ids_t *values,
char *value,
int&amp;nbsp;value_len
</code></pre>
<p> <code>);</code> </p>
<pre>
<code>int drmaa_get_num_job_ids(</code>
<dl><dt><dd><code>drmaa_job_ids_t *</code><i>values</i><code>,</code>
<code>int *</code><i>size</i>
</dl>
</pre>
<p> <code>);</code> </p>
<pre>
<code>void drmaa_release_job_ids(
<dl><dt><dd>drmaa_job_ids_t *</code><i>values</i>
</dl>
</pre>
<p> <code>);</code></p>
<h2>DESCRIPTION</h2>
<p> drmaa_run_job() submits an xxQS_NAMExx job with attributes defined in the DRMAA job template <i>jt</i>. On success up to <i>job_id_len</i> bytes of the job identifier are returned into the buffer, <i>job_id</i>. Note the effect of the <code>SGE_DRMAA_ALLOW_JOB_ERROR_STATE</code> environment variable, as below.</p>
<h3>drmaa_run_bulk_jobs()</h3>
<p> The drmaa_run_bulk_jobs() submits a xxQS_NAMExx array job very much as if the option `-t <i>start</i>&#8211;<i>end</i>:<i>incr</i>&#8216; had been used along with the additional attributes defined in the DRMAA job template, <i>jt</i>. The same constraints regarding value ranges are also in effect for the parameters <i>start</i>, <i>end</i>, and <i>incr</i> as for -t. On success a DRMAA job id string vector containing job identifiers for each array job task is returned into <i>jobids</i>. The job identifiers in the job id string vector can be extracted using The number of identifiers in the job id string vector can be determined using Note that this function is only available in the 1.0 implementation. The caller is responsible for releasing the job id string vector returned into <i>jobids</i> using </p>
<h3>drmaa_get_next_job_id()</h3>
<p> Each time drmaa_get_next_job_id() is called it returns into the buffer, <i>value</i>, up to <i>value_len</i> bytes of the next entry stored in the DRMAA job id string vector, <i>values</i>. Once the job ids list has been exhausted, DRMAA_ERRNO_NO_MORE_ELEMENTS is returned. </p>
<h3>drmaa_get_num_job_ids()</h3>
<p> The drmaa_get_num_job_ids() returns into <i>size</i> the number of entries in the DRMAA job ids string vector. This function is only available in the 1.0 implementation. </p>
<h3>drmaa_release_job_ids()</h3>
<p> The drmaa_release_attr_job_id() function releases all resources associated with the DRMAA job id string vector, <i>values</i>. This operation has no effect on the actual xxQS_NAMExx array job tasks. </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</p>
<dt><code>SGE_DRMAA_ALLOW_JOB_ERROR_STATE</code></p>
<dd> If set, in case of job errors the job will enter the error state. By default DRMAA jobs are not allowed to enter the job error state since an error state does not exist in DRMAA, so jobs with, say, a wrong input path specification, must fail when doing drmaa_wait().</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_run_job(), drmaa_run_bulk_jobs(), and drmaa_get_next_job_id() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_run_job(), drmaa_run_bulk_jobs(), and drmaa_get_next_job_id() functions can fail with:</p>
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
<p> The drmaa_run_job() and drmaa_run_bulk_jobs() functions can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_TRY_LATER </code></p>
<dd> The DRM system indicated that it is too busy to accept the job. A retry may succeed, however.</p>
<dt><code>DRMAA_ERRNO_DENIED_BY_DRM</code></p>
<dd> The DRM system rejected the job. The job will never be accepted due to DRM configuration or job template settings.</dl>
<p> The drmaa_get_next_job_id() function can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INVALID_ATTRIBUTE_VALUE</code></p>
<dd> When there are no more entries in the vector.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
