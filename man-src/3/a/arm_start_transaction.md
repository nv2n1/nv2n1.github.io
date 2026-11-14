---
title: "arm_start_transaction(3)"
name: "arm_start_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_start_transaction/"
description: "arm_start_transaction – start transaction"
---

<h2>NAME</h2>
<p> arm_start_transaction &#8211; start transaction</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_start_transaction( </p>
<p>&nbsp;<wbr>const arm_app_start_handle_t&nbsp;<wbr></code><i>app_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>tran_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>parent_correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_tran_start_handle_t&nbsp;<wbr>*</code><i>tran_handle</i><code>, </p>
<p>&nbsp;<wbr>arm_correlator_t&nbsp;<wbr>*</code><i>current_correlator</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_start_transaction()</code> is used to indicate that a transaction is beginning execution. </p>
<p> Call <code>arm_start_transaction()</code> just prior to a transaction beginning execution. <code>arm_start_transaction()</code> signals the ARM library to start timing the transaction response time. There is one exception: when <code>arm_get_arrival_time()</code> is used to get a start time before <code>arm_start_transaction()</code> executes. See <code>arm_get_arrival_time()</code> to understand this usage.<br />
&nbsp;<wbr> <code>arm_start_transaction()</code> is also the means to pass to ARM the correlation token (called a &quot;correlator&quot; in ARM) from a caller &#8211; the &quot;parent&quot; &#8211; and to request a correlator that can be passed to transactions called by this transaction. The correlation token may be used to establish a calling hierarchy across processes and systems. A correlator contains a two-byte length field, a one-byte format ID, a one-byte flag field, plus it may contain other data that is used to uniquely identify an instance of a transaction. Applications do not need to understand correlator internals. The maximum length of a correlator is 512 (<code>ARM_CORR_MAX_LENGTH</code>) bytes. (In ARM 2.0 it was 168 bytes.) </p>
<p> <i>app_handle</i> is a handle returned in an out parameter from an <code>arm_start_application()</code> call in the same process. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffers that may be used are <code>arm_subbuffer_arrival_time_t</code>, <code>arm_subbuffer_metric_values_t</code>, <code>arm_subbuffer_tran_context_t</code>, and <code>arm_subbuffer_user_t</code>. </p>
<p> <i>current_correlator</i> is a pointer to a buffer into which the ARM implementation will store a correlator for the transaction instance, if any. The length of the buffer should be (at least) 512 (<code>ARM_CORR_MAX_LENGTH</code>) bytes.<br />
&nbsp;<wbr> If the pointer is null (<code>ARM_CORR_NONE</code>), the application is not requesting that a correlator be created. </p>
<p> If the pointer is not null, the application is requesting that a correlator be created. In this case the ARM implementation may (but need not) create a correlator in the buffer. It may not create a correlator if it does not support the function or if it is configured to not create a correlator.<br />
&nbsp;<wbr> After <code>arm_start_transaction()</code> completes, the application tests the length field using <code>arm_get_correlator_length()</code> to determine whether a correlator has been stored. If the length is still zero, no correlator has been stored. The ARM implementation must store zero in the length field if it does not generate a correlator. </p>
<p> <i>flags</i> contains 32-bit flags. These may be combined using a binary or (|) operation. Three flags are defined:<br />
&nbsp;<wbr></p>
<dl>
<dt>0x00000001</p>
<dd> (<code>ARM_FLAG_TRACE_REQUEST</code>) is set if the application requests/suggests a trace.<br />
&nbsp;<wbr></p>
<dt>0x00000002</p>
<dd> (<code>ARM_FLAG_BIND_THREAD</code>) is set if the started transaction is bound to this thread. Setting this flag is equivalent to immediately calling <code>arm_bind_thread()</code> after the <code>arm_start_transaction()</code> completes, except the timing is a little more accurate and the extra call is avoided.<br />
&nbsp;<wbr></p>
<dt>0x00000004</p>
<dd> (<code>ARM_FLAG_CORR_IN_PROCESS</code>) is set if the application is stating that it will not send the correlator outside the current process. An ARM implementation may be able to optimize correlator handling if it knows this, because it may be able to avoid serialization to create the correlator. <i>parent_correlator</i> is a pointer to the parent correlator, if any. The pointer may be null (<code>ARM_CORR_NONE</code>). </p>
<p> <i>tran_handle</i> is a pointer to an <code>arm_int64_t</code> into which the ARM library will store the value of the handle that will represent the transaction instance in all calls, up to and including the <code>arm_stop_transaction()</code> that indicates that the instance has completed executing. The scope of the handle is the process in which the <code>arm_start_transaction()</code> is executed.<br />
&nbsp;<wbr> There are no defined behaviors for the value returned &#8211; it is implementation defined. Note that the returned value will always be a value that the application can use in future calls that take a handle [<code>arm_bind_thread()</code>, <code>arm_block_transaction()</code>, <code>arm_stop_transaction()</code>, <code>arm_unbind_thread()</code>, <code>arm_unblock_transaction()</code>, and <code>arm_update()</code>].<br />
&nbsp;<wbr> <i>tran_id</i> is a transaction ID returned in an out parameter from an <code>arm_register_transaction()</code> call in the same process. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>tran_handle</i> pointer must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> A valid <i>tran_id</i> and <i>app_handle</i> must be provided.</p>
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_bind_thread/">arm_bind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_block_transaction/">arm_block_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_get_arrival_time/">arm_get_arrival_time</a></code>(3), <code><a href="/docs/linux/man/3-arm_get_correlator_length/">arm_get_correlator_length</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_transaction/">arm_register_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_application/">arm_start_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_unbind_thread/">arm_unbind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_unblock_transaction/">arm_unblock_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_update_transaction/">arm_update_transaction</a></code>(3) </p>
<h2>Index</h2>
