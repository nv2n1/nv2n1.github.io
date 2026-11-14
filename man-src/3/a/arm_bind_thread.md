---
title: "arm_bind_thread(3)"
name: "arm_bind_thread"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_bind_thread/"
description: "arm_bind_thread – bind thread"
---

<h2>NAME</h2>
<p> arm_bind_thread &#8211; bind thread</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_bind_thread( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_bind_thread()</code> indicates that the thread from which it is called is performing on behalf of the transaction identified by the start handle. </p>
<p> The thread binding could be useful for managing computing resources at a finer level of granularity than a process. There can be any number of threads simultaneously bound to the same transaction. </p>
<p> A transaction remains bound to a thread until either an <code>arm_discard_transaction()</code>, <code>arm_stop_transaction()</code>, or <code>arm_unbind_thread()</code> is executed passing the same start handle. </p>
<p> <code>arm_bind_thread()</code> and <code>arm_block_transaction()</code> are used independently of each other. </p>
<p> <i>tran_handle</i> is a handle returned from an <code>arm_start_transaction()</code> call in the same process. </p>
<p> No sub-buffer types are currently valid with this function call, so the <i>buffer4</i> pointer should be null (<code>ARM_BUF4_NONE</code>). </p>
<p> No values are currently defined for <i>flags</i>. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> This implementation returns no errors for <code>arm_bind_thread()</code>.</p>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_unbind_thread/">arm_unbind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_block_transaction/">arm_block_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_discard_transaction/">arm_discard_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
