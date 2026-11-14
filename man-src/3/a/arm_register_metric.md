---
title: "arm_register_metric(3)"
name: "arm_register_metric"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_register_metric/"
description: "arm_register_metric – describe metrics"
---

<h2>NAME</h2>
<p> arm_register_metric &#8211; describe metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_register_metric( </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>app_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_char_t&nbsp;<wbr>*</code><i>name</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_metric_format_t&nbsp;<wbr></code><i>format</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_metric_usage_t&nbsp;<wbr></code><i>usage</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_char_t&nbsp;<wbr>*</code><i>unit</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_id_t&nbsp;<wbr>*</code><i>input_metric_id</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>const arm_int32_t&nbsp;<wbr></code><i>flags</i><code>, </p>
<p>&nbsp;<wbr>const arm_buffer4_t&nbsp;<wbr>*</code><i>buffer4</i><code>, </p>
<p>&nbsp;<wbr>arm_id_t&nbsp;<wbr>*</code><i>output_metric_id</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_register_metric()</code> describes metadata about a metric. </p>
<p> The application uses <code>arm_register_metric()</code> to inform the ARM library of metadata about each metric the application provides. </p>
<p> ARM generates an ID that is passed in the metric binding sub-buffer to <code>arm_register_transaction()</code>. </p>
<p> <i>app_id</i> is an application ID returned from an <code>arm_register_application()</code> call in the same process. </p>
<p> <i>buffer4</i> is a pointer to the user data buffer, if any. If the pointer is null, there is no buffer. No sub-buffer types are currently valid with this function call, so the pointer should be null (<code>ARM_BUF4_NONE</code>).<br />
&nbsp;<wbr> <i>flags</i> contains 32-bit flags. No values are currently defined. The field should be zero (<code>ARM_FLAG_NONE</code>).<br />
&nbsp;<wbr> <i>format</i> describes the data type. The value must be one of the following values:<br />
&nbsp;<wbr></p>
<dl>
<dt>1</p>
<dd> (<code>ARM_METRIC_FORMAT_COUNTER32</code>) = arm_int32_t counter</p>
<dt>2</p>
<dd> (<code>ARM_METRIC_FORMAT_COUNTER64</code>) = arm_int64_t counter</p>
<dt>3</p>
<dd> (<code>ARM_METRIC_FORMAT_CNTRDIVR</code>) = arm_int32_t counter + arm_int32_t divisor</p>
<dt>4</p>
<dd> (<code>ARM_METRIC_FORMAT_GAUGE32</code>) = arm_int32_t gauge</p>
<dt>5</p>
<dd> (<code>ARM_METRIC_FORMAT_GAUGE64</code>) = arm_int64_t gauge</p>
<dt>6</p>
<dd> (<code>ARM_METRIC_FORMAT_GAUGEDIVR32</code>) = arm_int32_t gauge + arm_int32_t divisor</p>
<dt>7</p>
<dd> (<code>ARM_METRIC_FORMAT_NUMERICID32</code>) = arm_int32_t numeric ID</p>
<dt>8</p>
<dd> (<code>ARM_METRIC_FORMAT_NUMERICID64</code>) = arm_int64_t numeric ID</p>
<dt>9</p>
<dd> deprecated</p>
<dt>10</p>
<dd> (<code>ARM_METRIC_FORMAT_STRING32</code>) = string (null-terminated) of a maximum length of 32 characters (33 including the null termination character) <i>input_metric_id</i> is a pointer to an optional 128-bit ID (16 bytes) that is unique and that can be treated as an alias for the other metadata. It can be any value except all zeros or all ones. If the pointer is null (<code>ARM_ID_NONE</code>), no ID is provided.<br />
&nbsp;<wbr> An ID is unique if the probability of the ID being associated with more than one set of metadata is vanishingly small. The selection of 128-bit IDs yields 3.4 x 10**38 unique IDs, so the objective is to select an ID that makes use of all 128 bits and is reasonably likely to not be selected by another person creating an ID of the same form. Two suggested algorithms that generate 128-bit values with these characteristics are:<br />
&nbsp;<wbr></p>
<dt>1.</p>
<dd> The Universal Unique Identifier (UUID) algorithm that is part of The Open Group specification: DCE 1.1: Remote Procedure Call. A developer could use the algorithm at the time the application is developed using a utility on his or her system, and be reasonably certain that nobody else would generate the same 128-bit ID.<br />
&nbsp;<wbr></p>
<dt>2.</p>
<dd> The MD5 Message-Digest Algorithm, described in IETF RFC 1321. Applying this algorithm to a concatenation of all the metadata properties would almost certainly result in a value that would not collide with any other ID created with a different set of metadata properties. If an ARM implementation is passed an ID that was previously registered within this process, the implementation can ignore the other metadata parameters and assume they are identical to the previously registered metadata. The metric metadata consists of the following fields: <i>app_id</i>, <i>name</i>, <i>format</i>, <i>usage</i>, and <i>unit</i>.<br />
&nbsp;<wbr> <i>name</i> is a pointer to a null-terminated string containing the name of the metric. The maximum length of the string is 128 characters, including the termination character. It serves no purpose and is illegal to make this call if the pointer is null. The name should not contain trailing blank characters or consist of only blank characters.<br />
&nbsp;<wbr> The name can be any string, with one exception. Strings beginning with the four characters &quot;ARM:&quot; are reserved for the ARM specification. The specification will define names with known semantics using this prefix. One name format is currently defined. Any name beginning with the eight character prefix &quot;ARM:CIM:&quot; represents a name defined using the DMTF CIM (Distributed Management Task Force Common Information Model) naming rules. For example, &quot;ARM:CIM:CIM_SoftwareElement.Name&quot; indicates that the metric value has the semantics of the Name property of the CIM_SoftwareElement class. It is anticipated that additional naming semantics are likely to be added in the future. </p>
<p> <i>output_metric_id</i> is a pointer to a 16-byte field. ARM will store a 16-byte value. There are no requirements on the value it is set to, except that it must be possible to pass it in the metric binding sub-buffer on the <code>arm_register_transaction()</code> call, without the application needing to do any error checking. </p>
<p> <i>unit</i> is a pointer to a null-terminated string containing the units (such as &quot;files transferred&quot;) of the metric. The maximum length of the string is 128 characters, including the termination character. The pointer may be null. </p>
<p> <i>usage</i> describes how the metric is used. The value must be one of the following values, or a negative value (any negative value is specific to the application; the negative values are not expected to be widely used).<br />
&nbsp;<wbr></p>
<dt>0</p>
<dd> (<code>ARM_METRIC_USE_GENERAL</code>) = a metric without a specified usage. Most metrics are described with a GENERAL usage.</p>
<dt>1</p>
<dd> (<code>ARM_METRIC_USE_TRAN_SIZE</code>) = a metric that indicates the &quot;size&quot; of a transaction. The &quot;size&quot; is something that would be expected to affect the response time, such as the number of bytes in a file transfer or the number of files backed up by a &quot;backup&quot; transaction. ARM implementations can use this knowledge to better interpret the response time.</p>
<dt>2</p>
<dd> (<code>ARM_METRIC_USE_TRAN_STATUS</code>) = a metric that further explains the transaction status passed on <code>arm_stop_transaction()</code>, such as a sense code that explains why a transaction failed.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>output_metric_id</i> pointer must not be null.</p>
<dt><code>ARM_FAILURE_INVALID_ARGUMENT</code></p>
<dd> One of <i>name</i> or <i>unit</i> is invalid.</p>
<dt>
<dt><code>ARM_FAILURE_BAD_ALIAS</code></p>
<dd>
<dd> The alias provided contains all 0&#8217;s or all 1&#8217;s.</p>
<dt><code>ARM_FAILURE_DUPLICATE_ALIAS</code></p>
<dd> The alias provided already refers to a metric with different metadata. <code>ARM_FAILURE_INTERNAL_ERROR</code> An internal error has occurred that prevented the operation from completing. Check your system log for more details.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_register_application/">arm_register_application</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_transaction/">arm_register_transaction</a></code>(3) </p>
<h2>Index</h2>
