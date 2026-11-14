---
title: "lwres_packet(3)"
name: "lwres_packet"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_packet/"
description: "lwres_lwpacket_renderheader, lwres_lwpacket_parseheader – lightweight resolver packet handling functions"
---

<h2 class="name">NAME</h2>
<p> lwres_lwpacket_renderheader, lwres_lwpacket_parseheader &#8211; lightweight resolver packet handling functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwpacket.h&gt;
</code></pre>
<dl>
<dt> <code>lwres_result_t lwres_lwpacket_renderheader(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_lwpacket_parseheader(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions rely on a <code>struct lwres_lwpacket</code> which is defined in <i>lwres/lwpacket.h</i>. </p>
<dl>
<dt>
<dd>
<pre>
typedef struct lwres_lwpacket lwres_lwpacket_t;
</pre>
</dl>
<dl>
<dt>
<dd>
<pre><code>
struct lwres_lwpacket {
    lwres_uint32_t length;
    lwres_uint16_t version;
    lwres_uint16_t pktflags;
    lwres_uint32_t serial;
    lwres_uint32_t opcode;
    lwres_uint32_t result;
    lwres_uint32_t recvlength;
    lwres_uint16_t authtype;
    lwres_uint16_t authlength;
};
</code></pre>
</dl>
<p> The elements of this structure are: </p>
<p> <code>length</code></p>
<dl>
<dt>
<dd> the overall packet length, including the entire packet header. This field is filled in by the lwres_gabn_*() and lwres_gnba_*() calls.</dl>
<p> <code>version</code></p>
<dl>
<dt>
<dd> the header format. There is currently only one format, <code>LWRES_LWPACKETVERSION_0</code>. This field is filled in by the lwres_gabn_*() and lwres_gnba_*() calls.</dl>
<p> <code>pktflags</code></p>
<dl>
<dt>
<dd> library-defined flags for this packet: for instance whether the packet is a request or a reply. Flag values can be set, but not defined by the caller. This field is filled in by the application wit the exception of the LWRES_LWPACKETFLAG_RESPONSE bit, which is set by the library in the lwres_gabn_*() and lwres_gnba_*() calls.</dl>
<p> <code>serial</code></p>
<dl>
<dt>
<dd> is set by the requestor and is returned in all replies. If two or more packets from the same source have the same serial number and are from the same source, they are assumed to be duplicates and the latter ones may be dropped. This field must be set by the application.</dl>
<p> <code>opcode</code></p>
<dl>
<dt>
<dd> indicates the operation. Opcodes between 0x00000000 and 0x03ffffff are reserved for use by the lightweight resolver library. Opcodes between 0x04000000 and 0xffffffff are application defined. This field is filled in by the lwres_gabn_*() and lwres_gnba_*() calls.</dl>
<p> <code>result</code></p>
<dl>
<dt>
<dd> is only valid for replies. Results between 0x04000000 and 0xffffffff are application defined. Results between 0x00000000 and 0x03ffffff are reserved for library use. This field is filled in by the lwres_gabn_*() and lwres_gnba_*() calls.</dl>
<p> <code>recvlength</code></p>
<dl>
<dt>
<dd> is the maximum buffer size that the receiver can handle on requests and the size of the buffer needed to satisfy a request when the buffer is too large for replies. This field is supplied by the application.</dl>
<p> <code>authtype</code></p>
<dl>
<dt>
<dd> defines the packet level authentication that is used. Authorisation types between 0x1000 and 0xffff are application defined and types between 0x0000 and 0x0fff are reserved for library use. Currently these are not used and must be zero.</dl>
<p> <code>authlen</code></p>
<dl>
<dt>
<dd> gives the length of the authentication data. Since packet authentication is currently not used, this must be zero.</dl>
<p> The following opcodes are currently defined: </p>
<p> <code>NOOP</code></p>
<dl>
<dt>
<dd> Success is always returned and the packet contents are echoed. The lwres_noop_*() functions should be used for this type.</dl>
<p> <code>GETADDRSBYNAME</code></p>
<dl>
<dt>
<dd> returns all known addresses for a given name. The lwres_gabn_*() functions should be used for this type.</dl>
<p> <code>GETNAMEBYADDR</code></p>
<dl>
<dt>
<dd> return the hostname for the given address. The lwres_gnba_*() functions should be used for this type.</dl>
<p> <code>lwres_lwpacket_renderheader()</code> transfers the contents of lightweight resolver packet structure <code>lwres_lwpacket_t</code> <i>*pkt</i> in network byte order to the lightweight resolver buffer, <i>*b</i>. </p>
<p> <code>lwres_lwpacket_parseheader()</code> performs the converse operation. It transfers data in network byte order from buffer <i>*b</i> to resolver packet <i>*pkt</i>. The contents of the buffer <i>b</i> should correspond to a <code>lwres_lwpacket_t</code>.</p>
<h2>RETURN VALUES</h2>
<p> Successful calls to <code>lwres_lwpacket_renderheader()</code> and <code>lwres_lwpacket_parseheader()</code> return <code>LWRES_R_SUCCESS</code>. If there is insufficient space to copy data between the buffer <i>*b</i> and lightweight resolver packet <i>*pkt</i> both functions return <code>LWRES_R_UNEXPECTEDEND</code>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
