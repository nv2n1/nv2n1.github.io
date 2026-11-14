---
title: "arm_generate_correlator(3)"
name: "arm_generate_correlator"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_generate_correlator/"
description: "arm_generate_correlator – generate a correlator"
---

<h2>NAME</h2>
<p> arm_generate_correlator &#8211; generate a correlator</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_generate_correlator( </p>
<p>&nbsp;<wbr>const arm_app_start_handle_t&nbsp;<wbr></code><i>app_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>tran_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>parent_correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_correlator_t&nbsp;<wbr>*</code><i>current_correlator</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_generate_correlator()</code> is used to generate a correlator for use with <code>arm_report_transaction()</code>.<br />
&nbsp;<wbr> A correlator is a correlation token passed from a calling transaction to a called transaction. The correlation token may be used to establish a calling hierarchy across processes and systems. A correlator contains a two-byte length field, a one-byte format ID, a one-byte flag field, plus it may contain other data that is used to uniquely identify an instance of a transaction. Applications do not need to understand correlator internals. The maximum length is 512 (<code>ARM_CORR_MAX_LENGTH</code>) bytes. </p>
<p> It is useful to think about its use in the context of what <code>arm_start_transaction()</code> and <code>arm_stop_transaction()</code> do:</p>
<dl>
<dt>*</p>
<dd> <code>arm_start_transaction()</code> performs two functions. It establishes the identity of a transaction instance (encapsulated in the current correlator) and begins the measurements of the instance. <code>arm_stop_transaction()</code> causes the measurements to be captured. The start handle links an <code>arm_start_transaction()</code> and an <code>arm_stop_transaction()</code>.</p>
<dt>*</p>
<dd> <code>arm_generate_correlator()</code> establishes the identity of a transaction instance, like <code>arm_start_transaction()</code>, also encapsulating it in a correlator. It has no relationship to measurements about the transaction instance. <code>arm_report_transaction()</code> combines the measurement function of both <code>arm_start_transaction()</code> and <code>arm_stop_transaction()</code>. Based on this positioning, it should be clear that <code>arm_generate_correlator()</code> can be used whenever an <code>arm_start_transaction()</code> can be used. More specifically, the following calls must have been executed first: <code>arm_register_application()</code>, <code>arm_register_transaction()</code>, and <code>arm_start_application()</code>. The same parameters are also used, except there&#8217;s no need for a start handle, and there&#8217;s no need for the arrival time or metric values sub-buffers. The other sub- buffers may be used. The correlator that is output can be used in the same way that a correlator output from <code>arm_start_transaction()</code> is used. </p>
<p> <i>app_handle</i> is a value returned from an <code>arm_start_application()</code> call in the same process. The ARM implementation may use this handle to access application instance data that may become part of the correlator; e.g., the <code>arm_subbuffer_system_address_t</code>. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffers that may be used are <code>arm_subbuffer_trancontext_t</code>, and <code>arm_subbuffer_user_t</code>. </p>
<p> <i>current_correlator</i> is a pointer to a buffer into which the ARM implementation will store a correlator for the transaction instance, if any. The length of the buffer should be (at least) 512 (<code>ARM_CORR_MAX_LENGTH</code>). The value must be non-null. </p>
<p> <i>flags</i> Contains 32-bit flags. These values may be combined using a binary or (|) operation.</p>
<dt>
<dd> 0x00000001 (<code>ARM_FLAG_TRACE_REQUEST</code>) is present if the application requests/suggests a trace.</p>
<dt>
<dd> 0x00000004 (<code>ARM_FLAG_CORR_IN_PROCESS</code>) is present if the application is stating that it will not send the correlator outside the current process. An ARM implementation may be able to optimize correlator handling if it knows this, because it may be able to avoid serialization to create the correlator. <i>parent_correlator</i> is a pointer to the parent correlator, if any. The pointer may be null (<code>ARM_CORR_NONE</code>). </p>
<p> <i>tran_id</i> is a transaction ID returned in an out parameter from an <code>arm_register_transaction()</code> call in the same process.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>current_correlator</i> must not be null.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_register_application/">arm_register_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_transaction/">arm_register_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_report_transaction/">arm_report_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_application/">arm_start_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
