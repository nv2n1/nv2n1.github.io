---
title: "arm_destroy_application(3)"
name: "arm_destroy_application"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_destroy_application/"
description: "arm_destroy_application – destroy application data"
---

<h2>NAME</h2>
<p> arm_destroy_application &#8211; destroy application data</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_destroy_application( </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>app_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_destroy_application()</code> indicates that the registration data about an application previously registered with <code>arm_register_application()</code> is no longer needed.<br />
&nbsp;<wbr> The purpose of this call is to signal the ARM implementation so it can release any storage it is holding. Ending a process or unloading the ARM library results in an implicit <code>arm_destroy_application()</code> for any previously registered applications.<br />
&nbsp;<wbr> It is possible for multiple <code>arm_register_application()</code> calls to be made in the same process with identical identity data. When this is done, <code>arm_destroy_application()</code> is assumed to be paired with one <code>arm_register_application()</code>. For example, if <code>arm_register_application()</code> is executed twice with the same output ID, and <code>arm_destroy_application()</code> is executed once using this ID, it is assumed that an instance of the application is still active and it is not safe to discard the application registration data associated with the ID. </p>
<p> <i>app_id</i> is an application ID returned from an <code>arm_register_application()</code> call in the same process. </p>
<p> No sub-buffer types are currently valid with this function call, so the <i>buffer4</i> pointer should be null (<code>ARM_BUF4_NONE</code>). </p>
<p> No values are currently defined for <i>flags</i>. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> This implementation returns no errors for <code>arm_destroy_application()</code>.</p>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> .BR arm_register_application (3) </p>
<h2>Index</h2>
