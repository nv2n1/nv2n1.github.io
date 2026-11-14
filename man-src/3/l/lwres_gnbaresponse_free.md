---
title: "lwres_gnbaresponse_free(3)"
name: "lwres_gnbaresponse_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_gnbaresponse_free/"
description: "lwres_gnbarequest_render, lwres_gnbaresponse_render, lwres_gnbarequest_parse, lwres_gnbaresponse_parse, lwres_gnbaresponse_free, lwres_gnbarequest_free – lightweight resolver getnamebyaddress messa..."
---

<h2 class="name">NAME</h2>
<p> lwres_gnbarequest_render, lwres_gnbaresponse_render, lwres_gnbarequest_parse, lwres_gnbaresponse_parse, lwres_gnbaresponse_free, lwres_gnbarequest_free &#8211; lightweight resolver getnamebyaddress message handling </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<dl>
<dt> <code>lwres_result_t lwres_gnbarequest_render(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_gnbarequest_t&nbsp;<wbr>*</code><i>req</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_gnbaresponse_render(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_gnbaresponse_t&nbsp;<wbr>*</code><i>req</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_gnbarequest_parse(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_gnbarequest_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_gnbaresponse_parse(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_gnbaresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>void lwres_gnbaresponse_free(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_gnbaresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>void lwres_gnbarequest_free(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_gnbarequest_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These are low-level routines for creating and parsing lightweight resolver address-to-name lookup request and response messages. </p>
<p> There are four main functions for the getnamebyaddr opcode. One render function converts a getnamebyaddr request structure &#8212; <code>lwres_gnbarequest_t</code> &#8212; to the lightweight resolver&#8217;s canonical format. It is complemented by a parse function that converts a packet in this canonical format to a getnamebyaddr request structure. Another render function converts the getnamebyaddr response structure &#8212; <code>lwres_gnbaresponse_t</code> to the canonical format. This is complemented by a parse function which converts a packet in canonical format to a getnamebyaddr response structure. </p>
<p> These structures are defined in <i>lwres/lwres.h</i>. They are shown below. </p>
<dl>
<dt>
<dd>
#define LWRES_OPCODE_GETNAMEBYADDR 0x00010002U
</dl>
<dl>
<dt>
<dd>
typedef struct {<br />
    lwres_uint32_t flags;<br />
    lwres_addr_t addr;<br />
} lwres_gnbarequest_t;
</dl>
<dl>
<dt>
<dd>
<pre><code>
typedef struct {
    lwres_uint32_t flags;
    lwres_uint16_t naliases;
    char *realname;
    char **aliases;
    lwres_uint16_t realnamelen;
    lwres_uint16_t *aliaslen;
    void *base;
    size_t baselen;
} lwres_gnbaresponse_t;
</code></pre>
</dl>
<p> <code>lwres_gnbarequest_render()</code> uses resolver context <i>ctx</i> to convert getnamebyaddr request structure <i>req</i> to canonical format. The packet header structure <i>pkt</i> is initialised and transferred to buffer <i>b</i>. The contents of <i>*req</i> are then appended to the buffer in canonical format. <code>lwres_gnbaresponse_render()</code> performs the same task, except it converts a getnamebyaddr response structure <code>lwres_gnbaresponse_t</code> to the lightweight resolver&#8217;s canonical format. </p>
<p> <code>lwres_gnbarequest_parse()</code> uses context <i>ctx</i> to convert the contents of packet <i>pkt</i> to a <code>lwres_gnbarequest_t</code> structure. Buffer <i>b</i> provides space to be used for storing this structure. When the function succeeds, the resulting <code>lwres_gnbarequest_t</code> is made available through <i>*structp</i>. <code>lwres_gnbaresponse_parse()</code> offers the same semantics as <code>lwres_gnbarequest_parse()</code> except it yields a <code>lwres_gnbaresponse_t</code> structure. </p>
<p> <code>lwres_gnbaresponse_free()</code> and <code>lwres_gnbarequest_free()</code> release the memory in resolver context <i>ctx</i> that was allocated to the <code>lwres_gnbaresponse_t</code> or <code>lwres_gnbarequest_t</code> structures referenced via <i>structp</i>. Any memory associated with ancillary buffers and strings for those structures is also discarded.</p>
<h2>RETURN VALUES</h2>
<p> The getnamebyaddr opcode functions <code>lwres_gnbarequest_render()</code>, <code>lwres_gnbaresponse_render()</code> <code>lwres_gnbarequest_parse()</code> and <code>lwres_gnbaresponse_parse()</code> all return <code>LWRES_R_SUCCESS</code> on success. They return <code>LWRES_R_NOMEMORY</code> if memory allocation fails. <code>LWRES_R_UNEXPECTEDEND</code> is returned if the available space in the buffer <i>b</i> is too small to accommodate the packet header or the <code>lwres_gnbarequest_t</code> and <code>lwres_gnbaresponse_t</code> structures. <code>lwres_gnbarequest_parse()</code> and <code>lwres_gnbaresponse_parse()</code> will return <code>LWRES_R_UNEXPECTEDEND</code> if the buffer is not empty after decoding the received packet. These functions will return <code>LWRES_R_FAILURE</code> if pktflags in the packet header structure <code>lwres_lwpacket_t</code> indicate that the packet is not a response to an earlier query.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres_packet/">lwres_packet</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
