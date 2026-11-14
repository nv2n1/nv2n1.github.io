---
title: "arm_unbind_thread(3)"
name: "arm_unbind_thread"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_unbind_thread/"
description: "arm_unbind_thread – unbind a thread"
---

<h2>NAME</h2>
<p> arm_unbind_thread &#8211; unbind a thread</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_unbind_thread( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_unbind_thread()</code> indicates that the thread from which it is called is no longer performing on behalf of the transaction identified by the start handle.<br />
&nbsp;<wbr> Call <code>arm_unbind_thread()</code> when a thread is no longer executing a transaction. The thread binding is useful for managing computing resources at a finer level of granularity than the process. It should be called when, for this transaction and this thread, either:</p>
<dl>
<dt>*</p>
<dd> <code>arm_bind_thread()</code> was previously called, or</p>
<dt>*</p>
<dd> The <code>ARM_FLAG_BIND_THREAD</code> flag was set in the <code>arm_start_transaction()</code> call. <code>arm_stop_transaction()</code> is an implicit <code>arm_unbind_thread()</code> for any threads still bound to the transaction instance [<code>arm_bind_thread()</code> issued without a matching <code>arm_unbind_thread()</code>]. As long as the transaction is bound to the thread when the <code>arm_stop_transaction()</code> executes, there is no need nor any value in calling <code>arm_unbind_thread()</code> before calling <code>arm_stop_transaction()</code>. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null, there is no buffer. No sub-buffer types are currently valid with this function call, so the pointer should be null (<code>ARM_BUF4_NONE</code>).<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>).<br />
&nbsp;<wbr> <i>tran_handle</i> is a handle returned in an out parameter from an <code>arm_start_transaction()</code> call in the same process.<br />
&nbsp;<wbr></dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> This implementation returns no errors for <code>arm_unbind_thread()</code>.</p>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_bind_thread/">arm_bind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
