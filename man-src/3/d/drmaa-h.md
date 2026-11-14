---
title: "drmaa-h(3)"
name: "drmaa-h"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa-h/"
description: "src/drmaa.h –"
---

<p>src/drmaa.h &#8211; </p>
<p> DRMAA library for Torque/PBS.</p>
<h2>Synopsis</h2>
<p>#include &lt;stddef.h&gt;<br />
 #include &lt;stdio.h&gt; </p>
<h3>Functions</h3>
<p>int <code>drmaa_init</code> (const char *contact, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_init()</code> function SHALL initialize DRMAA library and create a new DRMAA session, using the contact parameter, if provided, to determine to which DRMS to connect.<br />
 int <code>drmaa_exit</code> (char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_exit()</code> function SHALL disengage from DRMAA library and allow the DRMAA library to perform any necessary internal cleanup.<br />
 int <code>drmaa_get_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, char *value, size_t value_len, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_attribute()</code> SHALL fill the <i>value</i> buffer with up to <i>value_len</i> characters of the scalar attribute, <i>name&#8217;s</i>, value in the given job template.<br />
 int <code>drmaa_set_vector_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, const char *value[], char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_set_vector_attribute()</code> SHALL set the vector attribute, <i>name</i>, in the job template, <i>jt</i>, to the value(s), <i>value</i>.<br />
 int <code>drmaa_get_vector_attribute</code> (<code>drmaa_job_template_t</code> *jt, const char *name, <code>drmaa_attr_values_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_vector_attribute()</code> SHALL store in <i>values</i> an opaque values string vector containing the values of the vector attribute, <i>name&#8217;s</i>, value in the given job template.<br />
 int <code>drmaa_get_attribute_names</code> (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_attribute_names()</code> SHALL return the set of supported scalar attribute names in an opaque names string vector stored in <i>values</i>.<br />
 int <code>drmaa_get_vector_attribute_names</code> (<code>drmaa_attr_names_t</code> **values, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The function </i><code>drmaa_get_vector_attribute_names()</code> SHALL return the set of supported vector attribute names in an opaque names string vector stored in <i>values</i>.<br />
 int <code>drmaa_run_job</code> (char *job_id, size_t job_id_len, const <code>drmaa_job_template_t</code> *jt, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_run_job()</code> function submits a single job with the attributes defined in the job template, <i>jt</i>.<br />
 int <code>drmaa_run_bulk_jobs</code> (<code>drmaa_job_ids_t</code> **jobids, const <code>drmaa_job_template_t</code> *jt, int start, int end, int incr, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_run_bulk_jobs()</code> function submits a set of parametric jobs which can be run concurrently.<br />
 int <code>drmaa_control</code> (const char *job_id, int action, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_control()</code> function SHALL enact the action indicated by <i>action</i> on the job specified by the job identifier, <i>jobid</i>.<br />
 int <code>drmaa_job_ps</code> (const char *job_id, int *remote_ps, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_job_ps()</code> function SHALL store in <i>remote_ps</i> the program status of the job identified by <i>job_id</i>.<br />
 int <code>drmaa_synchronize</code> (const char *job_ids[], signed long timeout, int dispose, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_synchronize()</code> function SHALL cause the calling thread to block until all jobs specified by <i>job_ids</i> have finished execution.<br />
 int <code>drmaa_wait</code> (const char *job_id, char *job_id_out, size_t job_id_out_len, int *stat, signed long timeout, <code>drmaa_attr_values_t</code> **rusage, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_wait()</code> function SHALL wait for a job identified by <i>job_id</i> to finish execution or fail.<br />
 const char * <code>drmaa_strerror</code> (int drmaa_errno)<br />
 <i>The </i><code>drmaa_strerror()</code> function SHALL return the error string describing the DRMAA error number <i>drmaa_errno</i>.<br />
 int <code>drmaa_get_contact</code> (char *contact, size_t contact_len, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_get_contact()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of default DRMAA implementation contacts strings, one per DRM implementation provided.<br />
 int <code>drmaa_version</code> (unsigned int *major, unsigned int *minor, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_version()</code> function SHALL set major and minor to the major and minor versions of the DRMAA C binding specification implemented by the DRMAA implementation.<br />
 int <code>drmaa_get_DRM_system</code> (char *drm_system, size_t drm_system_len, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_get_DRM_system()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of DRM system identifiers, one per DRM system implementation provided.<br />
 int <code>drmaa_get_DRMAA_implementation</code> (char *drmaa_impl, size_t drmaa_impl_len, char *error_diagnosis, size_t error_diag_len)<br />
 <i>The </i><code>drmaa_get_DRMAA_implementation()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of DRMAA implementations, one per DRMAA implementation provided.<br />
 void <code>drmaa_set_logging_output</code> (FILE *file)<br />
 <i>Specify place where goes log messages from library when they were enabled at configure time. </i></p>
<h2>Detailed Description</h2>
<p>DRMAA library for Torque/PBS. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Lukasz Ciesnik lukasz.ciesnik [at] gmail.com</dl>
<p> Copyright (C) 2006 Poznan Supercomputing and Networking Center DSP team dsp-devel [at] hedera.man.poznan.pl </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA </p>
<p> Documentation taken from: </p>
<p> <i>Distributed Resource Management Application API C Bindings v1.0</i> </p>
<p> Copyright (C) Global Grid Forum (2003). All Rights Reserved. </p>
<p> This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this paragraph are included on all such copies and derivative works. However, this document itself may not be modified in any way, such as by removing the copyright notice or references to the GGF or other organizations, except as needed for the purpose of developing Grid Recommendations in which case the procedures for copyrights defined in the GGF Document process must be followed, or as required to translate it into languages other than English. </p>
<p> The limited permissions granted above are perpetual and will not be revoked by the GGF or its successors or assigns. This document and the information contained herein is provided on an &#8216;AS IS&#8217; basis and THE GLOBAL GRID FORUM DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>Function Documentation</h2>
<h3>int drmaa_run_job (char *job_id, size_tjob_id_len, const <code>drmaa_job_template_t</code> *jt, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_run_job()</code> function submits a single job with the attributes defined in the job template, <i>jt</i>. Upon success, up to <i>job_id_len</i> characters of the submitted job&#8217;s job identifier are stored in the buffer, <i>job_id</i>.</p>
<h3>int drmaa_run_bulk_jobs (<code>drmaa_job_ids_t</code> **jobids, const <code>drmaa_job_template_t</code> *jt, intstart, intend, intincr, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_run_bulk_jobs()</code> function submits a set of parametric jobs which can be run concurrently. The attributes defined in the job template, <i>jt</i> are used for every parametric job in the set. Each job in the set is identical except for it&#8217;s index. The first parametric job has an index equal to <i>start</i>. The next job has an index equal to <i>start</i> + <i>incr</i>, and so on. The last job has an index equal to start + n * incr, where n is equal to (end &#8211; start) / incr. Note that the value of the last job&#8217;s index may not be equal to end if the difference between <i>start</i> and <i>end</i> is not evenly divisble by <i>incr</i>. The smallest valid value for <i>start</i> is 1. The largest valid value for <i>end</i> is 2147483647 ( $2^{31}-1$). The <i>start</i> value must be less than or equal to the <i>end</i> value, and only positive index numbers are allowed. The index number can be determined by the job in an implementation specific fashion. On success, an opaque job id string vector containing job identifiers for all submitted jobs SHALL be returned into <i>job_ids</i>. The job identifiers in the opaque job id string vector can be extracted using the drmaa_get_next_job_id() function. The caller is responsible for releasing the opaque job id string vector returned into <i>job_ids</i> using the drmaa_release_job_ids() function.</p>
<h3>int drmaa_control (const char *job_id, intaction, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_control()</code> function SHALL enact the action indicated by <i>action</i> on the job specified by the job identifier, <i>jobid</i>. The action parameter&#8217;s value may be one of the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>DRMAA_CONTROL_SUSPEND</p>
<dt>&bull;</p>
<dd>DRMAA_CONTROL_RESUME</p>
<dt>&bull;</p>
<dd>DRMAA_CONTROL_HOLD</p>
<dt>&bull;</p>
<dd>DRMAA_CONTROL_RELEASE</p>
<dt>&bull;</p>
<dd>DRMAA_CONTROL_TERMINATE The <code>drmaa_control()</code> function SHALL return after the DRM system has acknowledged the command, not necessarily after the desired action has been performed. If <i>jobid</i> is DRMAA_JOB_IDS_SESSION_ALL, this function SHALL perform the specified action on all jobs submitted during this session as of this function is called.</dl>
<h3>int drmaa_job_ps (const char *job_id, int *remote_ps, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_job_ps()</code> function SHALL store in <i>remote_ps</i> the program status of the job identified by <i>job_id</i>. The possible values of a program&#8217;s staus are:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>DRMAA_PS_UNDETERMINED</p>
<dt>&bull;</p>
<dd>DRMAA_PS_QUEUED_ACTIVE</p>
<dt>&bull;</p>
<dd>DRMAA_PS_SYSTEM_ON_HOLD</p>
<dt>&bull;</p>
<dd>DRMAA_PS_USER_ON_HOLD</p>
<dt>&bull;</p>
<dd>DRMAA_PS_USER_SYSTEM_ON_HOLD</p>
<dt>&bull;</p>
<dd>DRMAA_PS_RUNNING</p>
<dt>&bull;</p>
<dd>DRMAA_PS_SYSTEM_SUSPENDED</p>
<dt>&bull;</p>
<dd>DRMAA_PS_USER_SUSPENDED</p>
<dt>&bull;</p>
<dd>DRMAA_PS_DONE</p>
<dt>&bull;</p>
<dd>DRMAA_PS_FAILED</dl>
<p> Terminated jobs have a status of DRMAA_PS_FAILED.</p>
<h3>int drmaa_synchronize (const char *job_ids[], signed longtimeout, intdispose, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_synchronize()</code> function SHALL cause the calling thread to block until all jobs specified by <i>job_ids</i> have finished execution. If <i>job_ids</i> contains DRMAA_JOB_IDS_SESSION_ALL, then this function SHALL wait for all jobs submitted during this DRMAA session as of the point in time when <code>drmaa_synchronize()</code> is called. To avoid thread race conditions in multithreaded applications, the DRMAA implementation user should explicitly synchronize this call with any other job submission calls or control calls that may change the number of remote jobs. </p>
<p> The <i>timeout</i> parameter value indicates how many seconds to remain blocked in this call waiting for results to become available, before returning with a DRMAA_ERRNO_EXIT_TIMEOUT error code. The value, DRMAA_TIMEOUT_WAIT_FOREVER, MAY be specified to wait indefinitely for a result. The value, DRMAA_TIMEOUT_NO_WAIT, MAY be specified to return immediately with a DRMAA_ERRNO_EXIT_TIMEOUT error code if no result is available. If the call exits before the timeout has elapsed, all the jobs have been waited on or there was an interrupt. The caller should check system time before and after this call in order to be sure of how much time has passed. The <i>dispose</i> parameter specifies how to treat the reaping of the remote job&#8217;s internal data record, which includes a record of the job&#8217;s consumption of system resources during its execution and other statistical information. If the <i>dispose</i> parameter&#8217;s value is 1, the DRMAA implementation SHALL dispose of the job&#8217;s data record at the end of the drmaa_synchroniize() call. If the <i>dispose</i> parameter&#8217;s value is 0, the data record SHALL be left for future access via the <code>drmaa_wait()</code> method.</p>
<h3>int drmaa_wait (const char *job_id, char *job_id_out, size_tjob_id_out_len, int *stat, signed longtimeout, <code>drmaa_attr_values_t</code> **rusage, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_wait()</code> function SHALL wait for a job identified by <i>job_id</i> to finish execution or fail. If the special string, JOB_IDS_SESSION_ANY, is provided as the job_id, this function will wait for any job from the session to finish execution or fail. In this case, any job for which exit status information is available will satisfy the requirement, including jobs which preivously finished but have never been the subject of a <code>drmaa_wait()</code> call. This routine is modeled on the wait3 POSIX routine. </p>
<p> The <i>timeout</i> parameter value indicates how many seconds to remain blocked in this call waiting for a result, before returning with a DRMAA_ERRNO_EXIT_TIMEOUT error code. The value, DRMAA_TIMEOUT_WAIT_FOREVER, MAY be specified to wait indefinitely for a result. The value, DRMAA_TIMEOUT_NO_WAIT, MAY be specified to return immediately with a DRMAA_ERRNO_EXIT_TIMEOUT error code if no result is available. If the call exits before the timeout has elapsed, the job has been successfully waited on or there was an interrupt. The caller should check system time before and after this call in order to be sure of how much time has passed. </p>
<p> Upon success, <code>drmaa_wait()</code> fills <i>job_id_out</i> with up to <i>job_id_out_len</i> characters of the waited job&#8217;s id, stat with the a code that includes information about the conditions under which the job terminated, and <i>rusage</i> with an array of &lt;name&gt;=&lt;value&gt; strings that describe the amount of resources consumed by the job and are implementation defined. The <i>stat</i> parameter is further described below. The <i>rusage</i> parameter&#8217;s values may be accessed via drmaa_get_next_attr_value(). </p>
<p> The <code>drmaa_wait()</code> function reaps job data records on a successful call, so any subsequent calls to <code>drmaa_wait()</code> will fail, returning a DRMAA_ERRNO_INVALID_JOB error code, meaning that the job&#8217;s data record has already been reaped. This error code is the same as if the job were unknown. If <code>drmaa_wait()</code> exists due to a timeout, DRMAA_ERRNO_EXIT_TIMEOUT is returned and no rusage information is reaped. (The only case where <code>drmaa_wait()</code> can be successfully called on a single job more than once is when the previous call(s) to <code>drmaa_wait()</code> returned DRMAA_ERRNO_EXIT_TIMEOUT.) </p>
<p> The stat parameter, set by a successful call to <code>drmaa_wait()</code>, is used to retrieve further input about the exit condition of the waited job, identified by job_id_out, through the following functions: drmaa_wifexited(), drmaa_wexitstatus(), drmaa_wifsignaled(), drmaa_wtermsig(),drmaa_wcoredump() and drmaa_wifaborted().</p>
<h3>int drmaa_get_contact (char *contact, size_tcontact_len, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_get_contact()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of default DRMAA implementation contacts strings, one per DRM implementation provided. If called after <code>drmaa_init()</code>, drmaa_get_contacts() SHALL return the contact string for the DRM system for which the library has been initialized.</p>
<h3>int drmaa_get_DRM_system (char *drm_system, size_tdrm_system_len, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_get_DRM_system()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of DRM system identifiers, one per DRM system implementation provided. If called after <code>drmaa_init()</code>, <code>drmaa_get_DRM_system()</code> SHALL return the selected DRM system.</p>
<h3>int drmaa_get_DRMAA_implementation (char *drmaa_impl, size_tdrmaa_impl_len, char *error_diagnosis, size_terror_diag_len)</h3>
<p>The <code>drmaa_get_DRMAA_implementation()</code> function, if called before <code>drmaa_init()</code>, SHALL return a string containing a comma-delimited list of DRMAA implementations, one per DRMAA implementation provided. If called after <code>drmaa_init()</code>, <code>drmaa_get_DRMAA_implementation()</code> SHALL return the selected DRMAA implementation.</p>
<h3>void drmaa_set_logging_output (FILE *file)</h3>
<p>Specify place where goes log messages from library when they were enabled at configure time. By default they are written to standard error stream. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> File to write to.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for torque from the source code.</p>
