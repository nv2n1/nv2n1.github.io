---
title: "ieee1284_get_deviceid(3)"
name: "ieee1284_get_deviceid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_get_deviceid/"
description: "ieee1284_get_deviceid – retrieve an IEEE 1284 Device ID"
---

<h2 class="name">NAME</h2>
<p> ieee1284_get_deviceid &#8211; retrieve an IEEE 1284 Device ID </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>ssize_t ieee1284_get_deviceid(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>daisy</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This function is for retrieving the IEEE 1284 Device ID of the specified device. The device is specified by the <i>port</i> to which it is attached, and optionally an address (<i>daisy</i>) on the daisy chain of devices on that port. </p>
<p> <i>daisy</i> should be -1 to indicate that the device is not participating in a IEEE 1284.3 daisy chain, meaning it is the last (or only) device on the port, or should be a number from 0 to 3 inclusive to indicate that it has the specified daisy chain address (0 is next to the port). </p>
<p> The <i>flags</i> parameter should be a bitwise union of any flags that the program wants to use. Available flags are: </p>
<p> <code>F1284_FRESH</code></p>
<dl>
<dt>
<dd> Guarantee a fresh Device ID. A cached or OS-provided ID will not be used.</dl>
<p> The provided <i>buffer</i> must be at least <i>len</i> bytes long, and will contain the Device ID including the initial two-byte length field and a terminating zero byte on successful return, or as much of the above as will fit into the buffer.</p>
<h2>RETURN VALUE</h2>
<p> A return value less than zero indicates an error as below. Otherwise, the return value is the number of bytes of <i>buffer</i> that have been filled. A return value equal to the length of the buffer indicates that the Device ID may be longer than the buffer will allow. </p>
<p> <code>E1284_NOID</code></p>
<dl>
<dt>
<dd> The device did not provide an IEEE 1284 Device ID when interrogated (perhaps by the operating system if <code>F1284_FRESH</code> was not specified).</dl>
<p> <code>E1284_NOTIMPL</code></p>
<dl>
<dt>
<dd> One or more of the supplied flags is not supported in this implementation, or if no flags were supplied then this function is not implemented for this type of port or this type of system. This can also be returned if a daisy chain address is specified but daisy chain Device IDs are not yet supported.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> <code>F1284_FRESH</code> was specified and the library is unable to access the port to interrogate the device.</dl>
<p> <code>E1284_NOMEM</code></p>
<dl>
<dt>
<dd> There is not enough memory.</dl>
<p> <code>E1284_INIT</code></p>
<dl>
<dt>
<dd> There was a problem initializing the port.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid.</dl>
<h2>NOTES</h2>
<p> Unless the <code>F1284_FRESH</code> flag is given, the library will try to find the device&#8217;s ID as unobtrusively as possible. First it will ask the operating system if it knows it, and then it will try actually asking the device for it. Because of this, the Device ID may be partially computed (the length field, for example) or even partially missing if the operating system has only remembered some parts of the ID. To guarantee that you are getting the bytes that the device sent, use <code>F1284_FRESH</code>. Be aware that the operating system may allow any user to inspect the Device IDs that it provides, whereas device access is normally more restricted. </p>
<p> The initial two-byte length field is a big-endian 16 bit unsigned integer provided by the device and may not be accurate. In particular, it is meant to indicate the length of the entire string including the length field itself; however, some manufacturers exclude the length field or just set the length field to some arbitrary number greater than the ID length.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
