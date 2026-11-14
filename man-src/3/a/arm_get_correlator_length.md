---
title: "arm_get_correlator_length(3)"
name: "arm_get_correlator_length"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_get_correlator_length/"
description: "arm_get_correlator_length – get length of correlator"
---

<h2>NAME</h2>
<p> arm_get_correlator_length &#8211; get length of correlator</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_get_correlator_length( </p>
<p>&nbsp;<wbr>const arm_correlator_t&nbsp;<wbr>*</code><i>correlator</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_correlator_length_t&nbsp;<wbr>*</code><i>length</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_get_correlator_length()</code> returns the length of a correlator, based on the length field within the correlator header. Note that this length is not necessarily the length of the buffer containing the correlator. </p>
<p> A correlator header contains a length field. <code>arm_get_correlator_length()</code> is used to return the length. The function handles any required conversion from the network byte order used in the header and the endian (big versus little) of the platform. See <code>arm_generate_correlator()</code> for a description of a correlator. </p>
<p> <i>correlator</i> is a pointer to a buffer containing a correlator. It serves no purpose to make the call if the pointer is null. </p>
<p> <i>length</i> is a pointer to an <code>arm_correlator_length_t</code> (a 16-bit integer) into which the ARM implementation will store the length. It serves no purpose to make the call if the pointer is null. The stored value will be the actual value if the value is apparently correct; otherwise, it will be zero. Examples of when zero would be stored are when the input correlator pointer is null or the length field is invalid, such as being greater than 512 (<code>ARM_CORR_MAX_LENGTH</code>) bytes.</p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>length</i> must not be null.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_generate_correlator/">arm_generate_correlator</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_transaction/">arm_start_transaction</a></code>(3) </p>
<h2>Index</h2>
