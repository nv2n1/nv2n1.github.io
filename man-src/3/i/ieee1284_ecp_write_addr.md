---
title: "ieee1284_ecp_write_addr(3)"
name: "ieee1284_ecp_write_addr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_ecp_write_addr/"
description: "ieee1284_nibble_read, ieee1284_compat_write, ieee1284_byte_read, ieee1284_epp_read_data, ieee1284_epp_write_data, ieee1284_epp_read_addr, ieee1284_epp_write_addr, ieee1284_ecp_read_data, ieee1284_e..."
---

<h2 class="name">NAME</h2>
<p> ieee1284_nibble_read, ieee1284_compat_write, ieee1284_byte_read, ieee1284_epp_read_data, ieee1284_epp_write_data, ieee1284_epp_read_addr, ieee1284_epp_write_addr, ieee1284_ecp_read_data, ieee1284_ecp_write_data, ieee1284_ecp_read_addr, ieee1284_ecp_write_addr &#8211; data transfer functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>ssize_t ieee1284_nibble_read(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_compat_write(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, const char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_byte_read(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_epp_read_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_epp_write_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, const char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_epp_read_addr(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_epp_write_addr(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, const char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_ecp_read_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_ecp_write_data(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, const char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_ecp_read_addr(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>ssize_t ieee1284_ecp_write_addr(struct parport&nbsp;<wbr>*</code><i>port</i><code>, int&nbsp;<wbr></code><i>flags</i><code>, const char&nbsp;<wbr>*</code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>This set of functions is for tranferring bytes in the relevant transfer mode. For ECP and EPP modes two types of transfer are possible: data and address (usually referred to as channel in ECP). </p>
<p> The supplied <i>port</i> must be a claimed port. </p>
<p> The supplied <i>buffer</i> must be at least <i>len</i> bytes long. When reading, the transferred data is stored in the buffer; when writing the data to be transferred is taken from the buffer. </p>
<p> For reads (peripheral to host): if no data is available and <code>F1284_NONBLOCK</code> is not in effect, the inactivity timer is started. If data becomes available before the inactivity time-out elapses it is read; otherwise the return value will be <code>E1284_TIMEDOUT</code>. </p>
<p> For writes (host to peripheral): if the peripheral is not willing to accept data and <code>F1284_NONBLOCK</code> is not in effect, the inactivity timer is started. If the peripheral indicates that it is willing to accept data before the inactivity time-out elapses it is sent; otherwise the return value will be <code>E1284_TIMEDOUT</code> </p>
<p> The <i>flags</i> may alter the behaviour slightly: </p>
<p> <code>F1284_NONBLOCK</code></p>
<dl>
<dt>
<dd> For reads (peripheral to host): if no data is available, return immediately (with <code>E1284_TIMEDOUT</code>). </p>
<p> For writes (host to peripheral): if the peripheral is not willing to accept data, return immediately (with <code>E1284_TIMEDOUT</code>).</dl>
<p> <code>F1284_SWE</code></p>
<dl>
<dt>
<dd> Don&#8217;t use hardware assistance for the transfer, but instead set the parallel port pins according to the wire protocol.</dl>
<p> <code>F1284_RLE</code> (for ECP only)</p>
<dl>
<dt>
<dd> Use run length encoding. If the peripheral is in ECP mode with RLE, calls to <code>ieee1284_ecp_read_data</code><i>must</i> set this flag in order for the RLE from the peripheral to be interpreted correctly, and calls to <code>ieee1284_ecp_write_data</code><i>may</i> set this flag in order to take advantage of RLE.</dl>
<p> <code>F1284_FASTEPP</code> (for EPP only)</p>
<dl>
<dt>
<dd> Use multi-byte transfers. Several bytes at a time are transferred using hardware assistance, if supporting hardware is present. The price of this increased speed is that the return value will be less reliable when this flag is used.</dl>
<p> For ECP mode, a given direction is in force at any particular time, and it is up to the application to ensure that it is only writing when in forward mode, and reading when in reverse mode.</p>
<h2>RETURN VALUE</h2>
<p> The return value is the number of bytes successfully transferred or, if negative, one of: </p>
<p> <code>E1284_NOTIMPL</code></p>
<dl>
<dt>
<dd> This transfer mode and flags combination is not yet implemented in libieee1284.</dl>
<p> <code>E1284_TIMEDOUT</code></p>
<dl>
<dt>
<dd> Timed out waiting for peripheral to handshake.</dl>
<p> <code>E1284_NOMEM</code></p>
<dl>
<dt>
<dd> Not enough memory is available.</dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
<dd> There was a problem at the operating system level. The global variable <i>errno</i> has been set appropriately.</dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
<dd> The <i>port</i> parameter is invalid (for instance, perhaps the <i>port</i> is not claimed).</dl>
<p> If any bytes are successfully transferred, that number is returned. An error is returned only if no bytes are transferred. </p>
<p> For host-to-peripheral transfers, all data is at the peripheral by the time the call returns.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ieee1284_ecp_fwd_to_rev/">ieee1284_ecp_fwd_to_rev</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
<h2>Index</h2>
