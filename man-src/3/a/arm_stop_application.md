---
title: "arm_stop_application(3)"
name: "arm_stop_application"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_stop_application/"
description: "arm_stop_application – stop application"
---

<h2>NAME</h2>
<p> arm_stop_application &#8211; stop application</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_stop_application( </p>
<p>&nbsp;<wbr>const arm_app_start_handle_t&nbsp;<wbr></code><i>app_handle</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_stop_application()</code> indicates that the application instance has finished making ARM calls. It typically means that the instance is ending, such as just prior to the process exiting or a thread that represents an application instance terminating.<br />
&nbsp;<wbr> For any transactions that are still in-process [<code>arm_start_transaction()</code> executed without a matching <code>arm_stop_transaction()</code>], an implicit <code>arm_discard_transaction()</code> is executed. </p>
<p> If the <code>arm_start_application()</code> used the system address sub-buffer to indicate that the ARM calls would be about an application instance on a different system, <code>arm_stop_application()</code> indicates that no more calls about that application instance and its transactions will be made. </p>
<p> After executing <code>arm_stop_application()</code>, no further calls should be made for this application, including calls for transactions created by this application, until a new instance &quot;session&quot; is started using <code>arm_start_application()</code>. Data from any other calls that are made will be ignored. This function is the equivalent of the ARM 2.0 function <code>arm_end()</code>. </p>
<p> <i>app_handle</i> is a handle returned in an out parameter from an <code>arm_start_application()</code> call in the same process. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null, there is no buffer. No sub-buffer types are currently valid with this function call, so the pointer should be null (<code>ARM_BUF4_NONE</code>).<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
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
<p> <code><a href="/docs/linux/man/3-arm_discard_transaction/">arm_discard_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_application/">arm_start_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_transaction/">arm_stop_transaction</a></code>(3) </p>
<h2>Index</h2>
