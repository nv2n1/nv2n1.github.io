---
title: "arm_register_application(3)"
name: "arm_register_application"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_register_application/"
description: "arm_register_application – describe application"
---

<h2>NAME</h2>
<p> arm_register_application &#8211; describe application</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_register_application( </p>
<p>&nbsp;<wbr>const arm_char_t&nbsp;<wbr>*</code><i>app_name</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>input_app_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>, </p>
<p>&nbsp;<wbr>arm_id_t&nbsp;<wbr>*</code><i>output_app_id</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_register_application()</code> describes metadata about an application. </p>
<p> The application uses <code>arm_register_application()</code> to inform the ARM library of metadata about the application. This metadata does not change from one application instance to another. It contains part of the function of the ARM 2.0 call <code>arm_init()</code>; <code>arm_start_application()</code> contains the other part. </p>
<p> ARM generates an ID that is passed in <code>arm_register_transaction()</code> and <code>arm_start_application()</code>. </p>
<p> <i>app_name</i> is a pointer to a null-terminated string containing the name of the application. The maximum length of the name is 128 characters, including the termination character. It serves no purpose and is illegal to make this call if the pointer is null. A name should be chosen that is unique, so generic names that might be used by a different development team, such as &quot;Payroll Application&quot;, should not be used. The name should not contain trailing blank characters or consist of only blank characters. If the application has a copyrighted product name, the copyrighted name would be a good choice. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null (<code>ARM_BUF4_NONE</code>), there is no buffer. The sub-buffer formats that might be used are <code>arm_subbuffer_app_identity_t</code> and <code>arm_subbuffer_encoding_t</code>.<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>). </p>
<p> <i>input_app_id</i> is a pointer to an optional 128-bit ID (16 bytes) that is unique and that can be treated as an alias for the other metadata. It can be any value except all zeros or all ones. If the pointer is null (<code>ARM_ID_NONE</code>), no ID is provided.<br />
&nbsp;<wbr> An ID is unique if the probability of the ID being associated with more than one set of metadata is vanishingly small. The selection of 128-bit IDs yields 3.4 x 10**38 unique IDs, so the objective is to select an ID that makes use of all 128 bits and is reasonably likely to not be selected by another person creating an ID of the same form. Two suggested algorithms that generate 128-bit values with these characteristics are:<br />
&nbsp;<wbr></p>
<dl>
<dt>1.</p>
<dd> The Universal Unique Identifier (UUID) algorithm that is part of The Open Group specification: DCE 1.1: Remote Procedure Call. A developer could use the algorithm at the time the application is developed using a utility on his or her system, and be reasonably certain that nobody else would generate the same 128-bit ID.<br />
&nbsp;<wbr></p>
<dt>2.</p>
<dd> The MD5 Message-Digest Algorithm, described in IETF RFC 1321. Applying this algorithm to a concatenation of all the metadata properties would almost certainly result in a value that would not collide with any other ID created with a different set of metadata properties. If an ARM implementation is passed an ID that was previously registered within this process, the implementation can ignore the other metadata parameters and assume they are identical to the previously registered metadata. The application metadata consists of the following fields: <i>app_name</i> and the <code>arm_subbuffer_app_identity_t</code> sub-buffer passed in <i>buffer4</i>. </p>
<p> <i>output_app_id</i> is a pointer to a 16-byte field. ARM will store a 16-byte value. There are no requirements on what value it is set to, except that it must be possible to pass it on other calls, such as <code>arm_start_application()</code>, without the application needing to do any error checking.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>output_app_id</i> must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> The <i>app_name</i> parameter is invalid.</p>
<dt><code>ARM_FAILURE_UNSUPPORTED_CHARSET</code></p>
<dd> The character set value passed in as a <code>arm_subbuffer_encoding_t</code> isn&#8217;t supported.</p>
<dt><code>ARM_FAILURE_BAD_ALIAS</code></p>
<dd> The alias provided contains all 0&#8217;s or all 1&#8217;s.</p>
<dt><code>ARM_FAILURE_DUPLICATE_ALIAS</code></p>
<dd> The alias provided already refers to an application with different metadata.</p>
<dt><code>ARM_FAILURE_INTERNAL_ERROR</code></p>
<dd> An internal error has occurred that prevented the application from being registered. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_destroy_application/">arm_destroy_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_transaction/">arm_register_transaction</a></code>(3), <code><a href="/docs/linux/man/3-arm_start_application/">arm_start_application</a></code>(3) </p>
<h2>Index</h2>
