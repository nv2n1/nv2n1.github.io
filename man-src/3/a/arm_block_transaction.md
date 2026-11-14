---
title: "arm_block_transaction(3)"
name: "arm_block_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_block_transaction/"
description: "arm_block_transaction – mark a transaction as blocked"
---

<h2>NAME</h2>
<p> arm_block_transaction &#8211; mark a transaction as blocked</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_block_transaction( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>, </p>
<p>&nbsp;<wbr>arm_tran_block_handle_t&nbsp;<wbr>*</code><i>block_handle</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_block_transaction()</code> is used to indicate that the transaction instance is blocked waiting on an external transaction (which may or may not be instrumented with ARM) or some other event to complete. It has been found useful to separate out this &quot;blocked&quot; time from the elapsed time between the <code>arm_start_transaction()</code> and <code>arm_stop_transaction()</code>. </p>
<p> A transaction remains blocked until <code>arm_unblock_transaction()</code> is executed passing the same <i>block_handle</i>, or either an <code>arm_discard_transaction()</code> or <code>arm_stop_transaction()</code> is executed passing the same <i>tran_handle</i>. </p>
<p> The blocking conditions of most interest are those that could result in a significant and/or variable length delay relative to the response time of the transaction. For example, a remote procedure call would be a good situation to indicate with <code>arm_block_transaction()</code> or <code>arm_unblock_transaction()</code>, whereas a disk I/O would not. </p>
<p> A transaction may be blocked by multiple conditions simultaneously. In many application architectures <code>arm_block_transaction()</code> would be called just prior to a thread suspending, because the thread is waiting to be signaled that an event has occurred. In other application architectures there would not be a tight relationship between the thread behavior and the blocking conditions. <code>arm_bind_thread()</code> and <code>arm_block_transaction()</code> are used independently of each other. </p>
<p> <i>tran_handle</i> is a handle returned from an <code>arm_start_transaction()</code> call in the same process. </p>
<p> <i>block_handle</i> is a pointer to a handle that is passed on <code>arm_unblock_transaction()</code> calls in the same process. There are no requirements on what value it is set to, except that it must be possible to pass it on <code>arm_unblock_transaction()</code> without the application needing to do any error checking. </p>
<p> No sub-buffer types are currently valid with this function call, so the <i>buffer4</i> pointer should be null (<code>ARM_BUF4_NONE</code>). </p>
<p> No values are currently defined for <i>flags</i>. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>block_handle</i> must not be null.</p>
<dt><code>ARM_FAILURE_TRANSACTION_BLOCKED</code></p>
<dd> The transaction has already been blocked by a previous call to <code>arm_block_transaction()</code>.</p>
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_unblock_transaction/">arm_unblock_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_bind_thread/">arm_bind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_discard_transaction/">arm_discard_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
