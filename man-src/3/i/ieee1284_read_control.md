---
title: "ieee1284_read_control(3)"
name: "ieee1284_read_control"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_read_control/"
description: "ieee1284_read_control, ieee1284_write_control, ieee1284_frob_control, ieee1284_do_nack_handshake – manipulate control lines"
---

<h2 class="name">NAME</h2>
<p> ieee1284_read_control, ieee1284_write_control, ieee1284_frob_control, ieee1284_do_nack_handshake &#8211; manipulate control lines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_read_control(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></p>
<dt> <code>void ieee1284_write_control(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>ct</i><code>);</code></p>
<dt> <code>void ieee1284_frob_control(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>mask</i><code>, unsigned char&nbsp;<wbr></code><i>val</i><code>);</code></p>
<dt> <code>int ieee1284_do_nack_handshake(struct parport&nbsp;<wbr>*</code><i>port</i><code>, unsigned char&nbsp;<wbr></code><i>ct_before</i><code>, unsigned char&nbsp;<wbr></code><i>ct_after</i><code>, struct timeval&nbsp;<wbr>*</code><i>timeout</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>There are four control lines, three of which are usually inverted on PC-style ports. Where they differ, libieee1284 operates on the IEEE 1284 values, not the PC-style inverted values. The control lines are represented by the following enumeration: </p>
<dl>
<dt>
<dd>
<pre><code>
enum ieee1284_control_bits {
    C1284_NSTROBE = 0x01,
    C1284_NAUTOFD = 0x02,
    C1284_NINIT = 0x04,
    C1284_NSELECTIN = 0x08,
    /* To convert those values into PC-style register values, use this: */
    C1284_INVERTED = (C1284_NSTROBE |
                      C1284_NAUTOFD |
                      C1284_NSELECTIN),
};
</code></pre>
</dl>
<p> These functions all act on the parallel port associated with <i>port</i>, which must be claimed. </p>
<p> The current values on the control lines are available by calling <code>ieee1284_read_control</code>, and may be set by calling <code>ieee1284_write_control</code>. </p>
<p> To adjust the values on a set of control lines, use <code>ieee1284_frob_control</code>. The effect of this can be expressed by: ctr = ((ctr &amp; ~mask) ^ val); that is, the bits in <i>mask</i> are unset, and then those in <i>val</i> are inverted. </p>
<p> The special function <code>ieee1284_do_nack_handshake</code> is for responding very quickly in a protocol where the peripheral sets nAck and the host must respond by setting a control line. Its operation, which relies on the host machine knowing which interrupt nAck generates, is as follows: </p>
<dl>
<dt>
<dd> 1. Set the control lines as indicated in <i>ct_before</i>.</dl>
<dl>
<dt>
<dd> 2. Wait for nAck interrupt. If <i>timeout</i> elapses, return <code>E1284_TIMEDOUT</code>.</dl>
<dl>
<dt>
<dd> 3. Set the control lines as indicated in <i>ct_after</i>.</dl>
<p> On Linux using the ppdev driver, this is performed by the device driver in the kernel, and so is faster than normally possible in a user-space library.</p>
<h2>RETURN VALUE</h2>
<p> The return value of <code>ieee1284_read_control</code>, if non-negative, is a number representing the value on the control lines. </p>
<p> Possible error codes for <code>ieee1284_read_control</code>: </p>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> The control lines of this port are not accessible by the application.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps it is not claimed).</dl>
<p> Possible error codes for <code>ieee1284_do_nack_handshake</code>: </p>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
<dd> The handshake was successful.</dl>
<p> <code>E1284_NOTAVAIL</code></p>
<dl>
<dt>
<dd> This operation is not available on this port type or system. This could be because port interrupts are not available, or because the underlying device driver does not support the operation.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps it is not claimed).</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
