---
title: "arm_get_error_message(3)"
name: "arm_get_error_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_get_error_message/"
description: "arm_get_error_message – get error message"
---

<h2>NAME</h2>
<p> arm_get_error_message &#8211; get error message</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_get_error_message( </p>
<p>&nbsp;<wbr>const arm_charset_t&nbsp;<wbr></code><i>charset</i><code>, </p>
<p>&nbsp;<wbr>const arm_error_t&nbsp;<wbr></code><i>code</i><code>,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>arm_message_buffer_t&nbsp;<wbr></code><i>msg</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_get_error_message()</code> stores a string containing an error message for the specified error code. </p>
<p> ARM implementations return values that are specific to the implementation. The only enforced convention is that a return code of zero indicates that no errors are reported (though an error could have occurred), and a negative return code indicates that some error occurred. Some implementations may report an error at times when another implementation would not. </p>
<p> To help an application developer or administrator understand what a negative error code means, <code>arm_get_error_message()</code> can be used to store a string containing an error message for the specified error code. The ARM library is not obliged to return a message, even if it returned a non-zero return code. </p>
<p> <i>charset</i> is an IANA (Internet Assigned Numbers Authority &#8211; see <a rel="nofollow" href="http://www.iana.org">www.iana.org</a>) MIBenum value [see <code>arm_is_charset_supported()</code>]. If a non-null message is returned, it will be in this encoding. It is strongly recommended that no value be used for <i>charset</i> that has not been tested for support by the library using <code>arm_is_charset_supported()</code>.<br />
&nbsp;<wbr> <i>code</i> is an error code returned as <code>arm_error_t</code> from an API call.<br />
&nbsp;<wbr> <i>msg</i> is a pointer to a buffer that can contain 256 characters (including the termination character) into which the null-terminated error message will be copied. The message will be in the encoding specified by the <i>charset</i> parameter. If the implementation cannot honor the request, the implementation must store at least the null termination character (e.g., which it would do if it does not return a message or does not recognize the error code or cannot return the message in the application&#8217;s encoding). The function is ignored if the pointer is null and an error status may be returned.</p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>msg</i> must not be null.</p>
<dt><code>ARM_FAILURE_UNSUPPORTED_CHARSET</code></p>
<dd> The <i>charset</i> requested isn&#8217;t supported.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_is_charset_supported/">arm_is_charset_supported</a></code>(3) </p>
<h2>Index</h2>
