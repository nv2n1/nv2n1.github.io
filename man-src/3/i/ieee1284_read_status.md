---
title: "ieee1284_read_status(3)"
name: "ieee1284_read_status"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_read_status/"
description: "ieee1284_read_status, ieee1284_wait_status – analyse status lines"
---

<h2 class="name">NAME</h2>
<p> ieee1284_read_status, ieee1284_wait_status &#8211; analyse status lines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_read_status(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>int ieee1284_wait_status(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>mask</i><code>, unsigned char&nbsp;<wbr></code><i>val</i><code>, struct timeval&nbsp;<wbr>*</code><i>timeout</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>There are five status lines, one of which is usually inverted on PC-style ports. Where they differ, libieee1284 operates on the IEEE 1284 values, not the PC-style inverted values. The status lines are represented by the following enumeration: </p>
<dl>
<dt>
<dd>
<pre><code>
enum ieee1284_status_bits {
    S1284_NFAULT = 0x08,
    S1284_SELECT = 0x10,
    S1284_PERROR = 0x20,
    S1284_NACK = 0x40,
    S1284_BUSY = 0x80,
    /* To convert those values into PC-style register values, use this: */
    S1284_INVERTED = S1284_BUSY,
};
</code></pre>
</dl>
<p> These functions all act on the parallel port associated with <i>port</i>, which must be claimed. </p>
<p> The purpose of <code>ieee1284_wait_status</code> is to wait until particular status lines have specified values. Its <i>timeout</i> parameter may be modified on return.</p>
<h2>RETURN VALUE</h2>
<p> For <code>ieee1284_read_status</code>, the return value is a non-negative integer with bits set as appropriate representing the status lines. A negative result indicates an error. </p>
<p> For <code>ieee1284_wait_status</code>, the return value is <code>E1284_OK</code> if the status lines now reflect the desired values (i.e. status &amp; <i>mask</i> is <i>val</i>), or a negative result indicating an error. </p>
<p> Possible error codes: </p>
<p> <code>E1284_NOTIMPL</code></p>
<dl>
<dt>
<dd> The <i>port</i> lacks the required capability. This could be due to a limitation of this version of libieee1284, or a hardware limitation.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> Access to the status lines is not available on this port type.</dl>
<p> <code>E1284_TIMEDOUT</code></p>
<dl>
<dt>
<dd> The <i>timeout</i> has elapsed.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps the <i>port</i> is not claimed).</dl>
<h2>NOTES</h2>
<p> The nAck pin is often able to trigger interrupts on the host machine. With operating system help these interrupts may be visible to the application via the file descriptor returned by <code>ieee1284_get_irq_fd</code>. </p>
<p> Under Linux, the conditions are that the parallel port driver knows which interrupt line to use and is using it, and that the relevant /dev/parport device node is accessible and backed by a device driver.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
