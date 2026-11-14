---
title: "arm_get_correlator_flags(3)"
name: "arm_get_correlator_flags"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_get_correlator_flags/"
description: "arm_get_correlator_flags – get value of flag"
---

<h2>NAME</h2>
<p> arm_get_correlator_flags &#8211; get value of flag</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_get_correlator_flags( </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>corr_flag_num</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_boolean_t&nbsp;<wbr>*</code><i>flag</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_get_correlator_flags()</code> returns the value of a specified flag in the correlator header. </p>
<p> A correlator header contains bit flags. <code>arm_get_correlator_flags()</code> is used to test the value of those flags. See <code>arm_generate_correlator()</code> for a description of a correlator. </p>
<p> <i>corr_flag_num</i> is an enumerated value that indicates which flag&#8217;s value is requested. The enumerated values are:</p>
<dl>
<dt>
<dd> 1 (<code>ARM_CORR_FLAGNUM_APP_TRACE</code>) = Application trace flag</p>
<dt>
<dd> 2 (<code>ARM_CORR_FLAGNUM_AGENT_TRACE</code>) = Agent trace flag <i>correlator</i> is a pointer to a buffer containing a correlator. It serves no purpose to make the call if the pointer is null. </p>
<p> <i>flag</i> is a pointer to a boolean that is output indicating whether the flag is set.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>correlator</i> and <i>flag</i> arguments must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> An unknown flag value has been specified.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_generate_correlator/">arm_generate_correlator</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3) </p>
<h2>Index</h2>
