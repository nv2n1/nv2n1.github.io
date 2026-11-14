---
title: "arm_report_transaction(3)"
name: "arm_report_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_report_transaction/"
description: "arm_report_transaction – report transaction statistics"
---

<h2>NAME</h2>
<p> arm_report_transaction &#8211; report transaction statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_report_transaction( </p>
<p>&nbsp;<wbr>const arm_app_start_handle_t&nbsp;<wbr></code><i>app_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>tran_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_tran_status_t&nbsp;<wbr></code><i>tran_status</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_response_time_t&nbsp;<wbr></code><i>response_time</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_stop_time_t&nbsp;<wbr></code><i>stop_time</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>parent_correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>current_correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_report_transaction()</code> is used to report statistics about a transaction that has already completed.<br />
&nbsp;<wbr> <code>arm_report_transaction()</code> may be used instead of a paired <code>arm_start_transaction()</code> and <code>arm_stop_transaction()</code> call. The application would have measured the response time. The transaction could have executed on the local system or on a remote system. If it executes on a remote system, the system address sub-buffer passed on the <code>arm_start_application()</code> provides the addressing information for the remote system. </p>
<p> If the transaction represented by the <code>arm_report_transaction()</code> call is the correlation parent of another transaction, <code>arm_generate_correlator()</code> must be used to get a parent correlator, prior to invoking the child transaction (because it must be passed to the child). In this case, the sequence is the following: </p>
<dl>
<dt>1.</p>
<dd> Call <code>arm_generate_correlator()</code> to get a correlator for this transaction.</p>
<dt>2.</p>
<dd> Invoke the child transaction, passing the correlator returned in step (1) to the child.</p>
<dt>3.</p>
<dd> When this transaction is complete, invoke <code>arm_report_transaction()</code> to report the statistics about the transaction. When used, it prevents certain types of proactive management, such as monitoring for hung transactions or adjusting priorities, because the ARM implementation is not invoked when the transaction is started. Because of this, the use of <code>arm_start_transction()</code> and <code>arm_stop_transaction()</code> is preferred over <code>arm_report_transaction()</code>.<br />
&nbsp;<wbr> The intended use is to report status and response time about transactions that recently completed (typically several seconds ago) in the absence of an ARM-enabled application and/or ARM implementation on the system on which the transaction executed. </p>
<p> <i>app_handle</i> is a handle returned in an out parameter from an <code>arm_start_application()</code> call in the same process. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffers that may be used are <code>arm_subbuffer_diag_detail_t</code>, <code>arm_subbuffer_metric_values_t</code>, <code>arm_subbuffer_tran_context_t</code>, and <code>arm_subbuffer_user_t</code>. </p>
<p> <i>current_correlator</i> is a pointer to the correlator for the transaction that has completed, if any. If the pointer is null (<code>ARM_CORR_NONE</code>), there is no current correlator.<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. In the least significant byte, 0x00000001 (<code>ARM_FLAG_TRACE_REQUEST</code>) is set if the application requests/suggests a trace. </p>
<p> <i>parent_correlator</i> is a pointer to a parent correlator, if any. If the pointer is null (<code>ARM_CORR_NONE</code>), there is no parent correlator. </p>
<p> <i>response_time</i> is the response time in nanoseconds.<br />
&nbsp;<wbr> <i>stop_time</i> is an <code>arm_int64_t</code> that contains the number of milliseconds since Jan 1, 1970 using the Gregorian calendar. The time base is GMT (Greenwich Mean Time). There is one special value, -1 (<code>ARM_USE_CURRENT_TIME</code>), which means use the current time. </p>
<p> <i>tran_id</i> is a transaction ID returned in an out parameter from an <code>arm_register_transaction()</code> call in the same process. </p>
<p> <i>tran_status</i> indicates the status of the transaction. The following values are allowed:<br />
&nbsp;<wbr></p>
<dt>0</p>
<dd> (<code>ARM_STATUS_GOOD</code>) = transaction completed successfully</p>
<dt>1</p>
<dd> (<code>ARM_STATUS_ABORTED</code>) = transaction was aborted before it completed. For example, the user might have pressed &quot;Stop&quot; or &quot;Back&quot; on a browser while a transaction was in process, causing the transaction, as measured at the browser, to be aborted.</p>
<dt>2</p>
<dd> (<code>ARM_STATUS_FAILED</code>) = transaction completed in error</p>
<dt>3</p>
<dd> (<code>ARM_STATUS_UNKNOWN</code>) = transaction completed but the status was unknown. This would most likely occur if middleware or some other form of proxy instrumentation measured the transaction. This instrumentation may know enough to know when the transaction starts and stops, but does not understand the application-specific semantics sufficiently well to know whether the transaction was successful.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>tran_id</i> must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> The <i>app_handle</i> provided is invalid.</p>
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_generate_correlator/">arm_generate_correlator</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_transaction/">arm_register_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_application/">arm_start_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
