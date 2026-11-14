---
title: "arm_discard_transaction(3)"
name: "arm_discard_transaction"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_discard_transaction/"
description: "arm_discard_transaction – discard transaction"
---

<h2>NAME</h2>
<p> arm_discard_transaction &#8211; discard transaction</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_discard_transaction( </p>
<p>&nbsp;<wbr>const arm_tran_start_handle_t&nbsp;<wbr></code><i>tran_handle</i><code>, </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_discard_transaction()</code> signals that the <code>referenced arm_start_transaction()</code> should be ignored and treated as if it never happened. Measurements associated with a transaction that is processing should be discarded. Either <code>arm_discard_transaction()</code> or <code>arm_stop_transaction()</code> is used &#8211; never both. </p>
<p> An example of when a transaction would be discarded could happen is if proxy instrumentation believes a transaction is starting, but then learns that it did not. It can be called from any thread in the process that executed the <code>arm_start_transaction()</code>. In general, the use of <code>arm_discard_transaction()</code> is discouraged, but experience has shown a few use cases that require the functionality. </p>
<p> <code>arm_discard_transaction()</code> clears any thread bindings [<code>arm_bind_thread()</code>] and blocking conditions [<code>arm_block_transaction()</code>]. </p>
<p> <i>tran_handle</i> is a handle returned from an <code>arm_start_transaction()</code> call in the same process. </p>
<p> No sub-buffer types are currently valid with this function call, so the <i>buffer4</i> pointer should be null (<code>ARM_BUF4_NONE</code>). </p>
<p> No values are currently defined for <i>flags</i>. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
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
<p> <code><a href="/docs/linux/man/3-arm_bind_thread/">arm_bind_thread</a></code>(3), <code><a href="/docs/linux/man/3-arm_block_transaction/">arm_block_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
