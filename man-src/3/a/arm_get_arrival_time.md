---
title: "arm_get_arrival_time(3)"
name: "arm_get_arrival_time"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_get_arrival_time/"
description: "arm_get_arrival_time – store current time"
---

<h2>NAME</h2>
<p> arm_get_arrival_time &#8211; store current time</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_get_arrival_time( </p>
<p>&nbsp;<wbr>arm_arrival_time_t&nbsp;<wbr>*</code><i>opaque_time</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_get_arrival_time()</code> stores a 64-bit integer representing the current time. </p>
<p> There are situations in which there is a significant delay between the time when processing of a transaction begins and when all the context property values that are needed before <code>arm_start_transaction()</code> can be executed are known. In order to get a more accurate response time, <code>arm_get_arrival_time()</code> can be used to capture an implementation-defined representation of the current time. This integer value is later stored in the arrival time sub-buffer when <code>arm_start_transaction()</code> executes. The ARM library will use the &quot;arrival time&quot; as the start time rather than the moment when the <code>arm_start_transaction()</code> executes. </p>
<p> <i>opaque_time</i> is a pointer to an <code>arm_int64_t</code> that will contain the arrival time value. Note that the value is implementation-defined so the application should not make any conclusions based on its contents.</p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>opaque_time</i> must not be null.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3) </p>
<h2>Index</h2>
