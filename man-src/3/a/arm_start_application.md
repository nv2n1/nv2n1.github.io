---
title: "arm_start_application(3)"
name: "arm_start_application"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_start_application/"
description: "arm_start_application – check application is running"
---

<h2>NAME</h2>
<p> arm_start_application &#8211; check application is running</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_start_application( </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>app_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_char_t&nbsp;<wbr>*</code><i>app_group</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_char_t&nbsp;<wbr>*</code><i>app_instance</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_app_start_handle_t&nbsp;<wbr>*</code><i>app_handle</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_start_application()</code> indicates that an instance of an application has started running and is prepared to make ARM calls. In many cases, there will be only one application instance in a process, but there are cases in which there could be multiple instances. An example of multiple application instances in the same process is if several Java applications run in the same JVM (Java Virtual Machine) in the same process, and they each call the ARM 4.0 C interface (either directly, or indirectly via an implementation of the ARM 4.0 Java interface). They might share the same application ID or they might be separately registered. </p>
<p> Application context properties may be used to differentiate between instances. The values do not have to be different from other instances, though making them unique is suggested. The context properties are provided through function parameters and/or a sub-buffer. </p>
<p> The group and instance names are provided as function parameters. </p>
<p> Up to twenty (name,value) pairs of context properties may be provided in a sub-buffer. </p>
<p> There is a special case in which a system address sub-buffer is provided. The system address sub-buffer is provided when <code>arm_report_transaction()</code> will be used to report data about transactions that executed on a different system. In this case, the <code>arm_start_application()</code> provides a scoping context for the transaction instances, but does not indicate that the application instance is running on the local system. </p>
<p> The combination of <code>arm_register_application()</code> and <code>arm_start_application()</code> is equivalent to the ARM 2.0 call <code>arm_init()</code>. </p>
<p> <i>app_group</i> is a pointer to a null-terminated string containing the identity of a group of application instances, if any. Application instances for a given software product that are started for a common runtime purpose are typically very good candidates for using the same group name. For example, identical replica instances of a product started across multiple processes or servers to address a specific transaction workload objective can be, advantageously to the ARM agent, commonly identified by the group name. The maximum length of the string is 256 (<code>ARM_PROPERTY_VALUE_MAX_CHARS</code>) characters, including the termination character. A null pointer (<code>ARM_STRING_NONE</code>) indicates that there is no group. </p>
<p> <i>app_handle</i> is a pointer to an <code>arm_int64_t</code> into which the ARM library will store the value of the handle that will represent the application instance in all calls, up to and including the <code>arm_stop_application()</code> that indicates that the instance has completed executing. The scope of the handle is the process in which the <code>arm_start_application()</code> is executed. There are no requirements on the value it is set to, except that it must be possible to pass it on other calls, such as <code>arm_start_transaction()</code>, without the application needing to do any error checking. Whether the data is meaningful, or partially meaningful, is at the discretion of the ARM implementation. </p>
<p> <i>app_id</i> is a pointer to a 16-byte ID returned by an <code>arm_register_application()</code> call.<br />
&nbsp;<wbr> <i>app_instance</i> is a pointer to a null-terminated string containing the identity of this instance of the application. It might contain the process ID, or a UUID in printable characters, for example. The maximum length of the string is 256 (<code>ARM_PROPERTY_VALUE_MAX_CHARS</code>) characters, including the termination character. A null pointer (<code>ARM_STRING_NONE</code>) indicates that there is no instance value. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffer formats that might be used are <code>arm_subbuffer_app_context_t</code> and <code>arm_subbuffer_system_address_t</code>.<br />
&nbsp;<wbr> If no system address sub-buffer is provided on <code>arm_start_application()</code>, all transactions reported by this application instance execute in the current process.<br />
&nbsp;<wbr> If a system address sub-buffer is provided on <code>arm_start_application()</code>, all transactions execute in a different process.<br />
&nbsp;<wbr> If a system address sub-buffer is provided in which the system address length is zero, or the system address pointer is null, the system is the &quot;local&quot; system, as determined by the ARM implementation.<br />
&nbsp;<wbr> If a system address sub-buffer is provided in which there is a non-null system address and length, the system may be the local system or a remote system. Interpretation of what is local versus remote is at the discretion of the ARM implementation. </p>
<p> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>app_handle</i> pointer must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> One or both of <i>app_group</i> or <i>app_instance</i> are non-null and invalid strings.</p>
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_register_application/">arm_register_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_report_transaction/">arm_report_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_stop_application/">arm_stop_application</a></code>(3) </p>
<h2>Index</h2>
