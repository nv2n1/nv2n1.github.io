---
title: "arm_is_charset_supported(3)"
name: "arm_is_charset_supported"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arm_is_charset_supported/"
description: "arm_is_charset_supported – check character encoding"
---

<h2>NAME</h2>
<p> arm_is_charset_supported &#8211; check character encoding</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/arm4.h">arm4.h</a>&gt;</code> </p>
<p> <code>arm_error_t<br />
 arm_is_charset_supported( </p>
<p>&nbsp;<wbr>const arm_charset_t&nbsp;<wbr></code><i>charset</i><code>, </p>
<p>&nbsp;<wbr>arm_boolean_t&nbsp;<wbr>*</code><i>supported</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>arm_is_charset_supported()</code> indicates whether an ARM library supports a specified character encoding. </p>
<p> The default encoding for all strings provided by the application on all operating systems is UTF-8. An application may specify an alternate encoding when executing <code>arm_register_application()</code>, and then use it for all strings it provides on all calls including <code>arm_register_application()</code>, but should never do so without first issuing <code>arm_is_charset_supported()</code> to test whether the value is supported. </p>
<p> An ARM library on the operating systems listed in Table 1 must support the specified encodings. Applications are encouraged to use one of these encodings to ensure that any ARM implementation will support the application&#8217;s ARM instrumentation. Another alternative is to use one of these encodings along with a preferred encoding. If the ARM library supports the preferred encoding, it is used; otherwise, one of the mandatory encodings is used. </p>
<p> <code>Table 1: Mandatory Encodings by Platform</code> </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>IANA MIBenum</code></td>
<td ALIGN=center><code>Character</code></td>
<td ALIGN=center><code>UNIX</code></td>
<td ALIGN=center><code>Microsoft</code></td>
<td ALIGN=center><code>IBM</code></td>
<td ALIGN=center><code>IBM </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center><code>Set</code></td>
<td ALIGN=center><code>and</code></td>
<td ALIGN=center><code>Windows</code></td>
<td ALIGN=center><code>OS/400</code></td>
<td ALIGN=center><code>zOS</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center><code>Common Name</code></td>
<td ALIGN=center><code>Linux</code></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>3</td>
<td ALIGN=center>ASCII-7</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>ARM_CHARSET_ASCII</code></td>
<td ALIGN=center></td>
<td ALIGN=center>(US-ASCII)</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>106</td>
<td ALIGN=center>UTF-8</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes</td>
<td ALIGN=center>Yes
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>ARM_CHARSET_UTF8</code></td>
<td ALIGN=center></td>
<td ALIGN=center>(UCS-2</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>characters only)</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1014</td>
<td ALIGN=center>UTF-16</td>
<td ALIGN=center></td>
<td ALIGN=center>Yes</td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>ARM_CHARSET_UTF16LE</code></td>
<td ALIGN=center></td>
<td ALIGN=center>Little Endian</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>(UCS-2</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>characters only)</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2028</td>
<td ALIGN=center>IBM037</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>Yes </td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>ARM_CHARSET_IBM037</code></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2102</td>
<td ALIGN=center>IBM1047</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>Yes
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>ARM_CHARSET_IBM1047</code></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center>
</td>
</tr>
</table>
</table>
<p> <i>charset</i> is an IANA (Internet Assigned Numbers Authority &#8211; see <a rel="nofollow" href="http://www.iana.org">www.iana.org</a>) MIBenum value. Support for some values is mandatory by any ARM implementation on a specified platform, as shown in the table. </p>
<p> <i>supported</i> is a pointer to a boolean value that is set to true or false to indicate whether <i>charset</i> is a supported encoding.</p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns <code>ARM_SUCCESS</code>. A non-zero value indicates an error.</p>
<h2>ERRORS</h2>
<p> If the return code is negative, an error occurred. If the return code is not negative, an error may or may not have occurred &#8211; the determination of what is an error and whether an error code is returned is at the discretion of the ARM implementation. The application can test the return code if it wants to provide its own error logging. </p>
<p> The following errors are recognized by this implementation, but may not be portable to other implementations: </p>
<dl>
<dt><code>ARM_FAILURE_NULL_ARGUMENT</code></p>
<dd> The <i>supported</i> pointer must not be null.</dl>
<h2>CONFORMING TO</h2>
<p> ARM Issue 4.0 C Language Bindings, Version 2</p>
<h2>EXAMPLE</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-arm_get_error_message/">arm_get_error_message</a></code>(3), <code><a href="/docs/linux/man/3-arm_register_application/">arm_register_application</a></code>(3) </p>
<h2>Index</h2>
