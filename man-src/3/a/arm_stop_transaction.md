---
title: "arm_stop_transaction(3)"
name: "arm_stop_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_stop_transaction/"
description: "arm_stop_transaction – stop transaction"
---

<h2>NAME</h2>
<p> arm_stop_transaction &#8211; stop transaction</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_stop_transaction( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_tran_status_t&nbsp;<wbr></code><i>tran_status</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_stop_transaction()</code> signals the end of a transaction.<br />
&nbsp;<wbr> Call <code>arm_stop_transaction()</code> just after a transaction completes. <code>arm_start_transaction()</code> signals the ARM library to start timing the transaction response time. <code>arm_stop_transaction()</code> signals the ARM library to stop timing the transaction response time. It can be called from any thread in the process that executed the <code>arm_start_transaction()</code>.<br />
&nbsp;<wbr> Implicit <code>arm_unbind_thread()</code> and <code>arm_unblock_transaction()</code> calls are made for any pending <code>arm_bind_thread()</code> and <code>arm_block_transaction()</code> calls, respectively, that have not been explicitly unbound or unblocked with <code>arm_unbind_thread()</code> and <code>arm_unblock_transaction()</code>. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffers that may be used are <code>arm_subbuffer_diag_detail_t</code> and <code>arm_subbuffer_metric_values_t</code>.<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<p> <i>tran_handle</i> is a handle returned in an out parameter from an <code>arm_start_transaction()</code> call in the same process. </p>
<p> <i>tran_status</i> indicates the status of the transaction. The following values are allowed:<br />
&nbsp;<wbr></p>
<dl>
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
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_bind_thread/">arm_bind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_block_transaction/">arm_block_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_unbind_thread/">arm_unbind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_unblock_transaction/">arm_unblock_transaction</a></code>(3) </p>
<h2>Index</h2>
