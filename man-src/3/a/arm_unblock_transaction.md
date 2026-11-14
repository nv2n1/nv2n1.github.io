---
title: "arm_unblock_transaction(3)"
name: "arm_unblock_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_unblock_transaction/"
description: "arm_unblock_transaction – unblock transaction"
---

<h2>NAME</h2>
<p> arm_unblock_transaction &#8211; unblock transaction</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_unblock_transaction( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_tran_block_handle_t&nbsp;<wbr></code><i>block_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_unblock_transaction()</code> indicates that the suspension indicated by the <i>block_handle</i> for the transaction identified by the start handle is no longer waiting for a downstream transaction to complete. </p>
<p> Call <code>arm_unblock_transaction()</code> when a transaction is no longer blocked on an external event. It should be called when <code>arm_block_transaction()</code> was previously called and the blocking condition no longer exists. Knowledge of when a transaction is blocked can be useful for better understanding response times. It is useful to separate out this &quot;blocked&quot; time from the elapsed start-to-stop time. The unblocked call is paired with a block call for finer grained analysis. </p>
<p> <code>arm_stop_transaction()</code> is an implicit <code>arm_unblock_transaction()</code> for any blocking condition for the transaction instance that has not been cleared yet [<code>arm_block_transaction()</code> issued without a matching <code>arm_unblock_transaction()</code>]. It should only be called without calling <code>arm_unblock_transaction()</code> first when the blocking condition ends immediately prior to the transaction ending. </p>
<p> <i>block_handle</i> is a handle returned in an out parameter from an <code>arm_block_transaction()</code> call in the same process. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null, there is no buffer. No sub-buffer types are currently valid with this function call, so the pointer should be null (<code>ARM_BUF4_NONE</code>).<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<p> <i>tran_handle</i> is a handle returned in an out parameter from an <code>arm_start_transaction()</code> call in the same process. </p>
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
<p> <code><a href="/docs/linux/man/3-arm_block_transaction/">arm_block_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
