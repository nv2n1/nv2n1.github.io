---
title: "lwres_nooprequest_render(3)"
name: "lwres_nooprequest_render"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_nooprequest_render/"
description: "lwres_nooprequest_render, lwres_noopresponse_render, lwres_nooprequest_parse, lwres_noopresponse_parse, lwres_noopresponse_free, lwres_nooprequest_free – lightweight resolver no-op message handling"
---

<h2 class="name">NAME</h2>
<p> lwres_nooprequest_render, lwres_noopresponse_render, lwres_nooprequest_parse, lwres_noopresponse_parse, lwres_noopresponse_free, lwres_nooprequest_free &#8211; lightweight resolver no-op message handling </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<dl>
<dt> <code>lwres_result_t lwres_nooprequest_render(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_nooprequest_t&nbsp;<wbr>*</code><i>req</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_noopresponse_render(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_noopresponse_t&nbsp;<wbr>*</code><i>req</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_nooprequest_parse(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_nooprequest_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_noopresponse_parse(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_lwpacket_t&nbsp;<wbr>*</code><i>pkt</i><code>, lwres_noopresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>void lwres_noopresponse_free(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_noopresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>void lwres_nooprequest_free(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_nooprequest_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These are low-level routines for creating and parsing lightweight resolver no-op request and response messages. </p>
<p> The no-op message is analogous to a <code>ping</code> packet: a packet is sent to the resolver daemon and is simply echoed back. The opcode is intended to allow a client to determine if the server is operational or not. </p>
<p> There are four main functions for the no-op opcode. One render function converts a no-op request structure &#8212; <code>lwres_nooprequest_t</code> &#8212; to the lighweight resolver&#8217;s canonical format. It is complemented by a parse function that converts a packet in this canonical format to a no-op request structure. Another render function converts the no-op response structure &#8212; <code>lwres_noopresponse_t</code> to the canonical format. This is complemented by a parse function which converts a packet in canonical format to a no-op response structure. </p>
<p> These structures are defined in <i>lwres/lwres.h</i>. They are shown below. </p>
<dl>
<dt>
<dd>
#define LWRES_OPCODE_NOOP 0x00000000U
</dl>
<dl>
<dt>
<dd>
typedef struct {<br />
    lwres_uint16_t datalength;<br />
    unsigned char *data;<br />
} lwres_nooprequest_t;
</dl>
<dl>
<dt>
<dd>
<pre><code>
typedef struct {
    lwres_uint16_t datalength;
    unsigned char *data;
} lwres_noopresponse_t;
</code></pre>
</dl>
<p> Although the structures have different types, they are identical. This is because the no-op opcode simply echos whatever data was sent: the response is therefore identical to the request. </p>
<p> <code>lwres_nooprequest_render()</code> uses resolver context <i>ctx</i> to convert no-op request structure <i>req</i> to canonical format. The packet header structure <i>pkt</i> is initialised and transferred to buffer <i>b</i>. The contents of <i>*req</i> are then appended to the buffer in canonical format. <code>lwres_noopresponse_render()</code> performs the same task, except it converts a no-op response structure <code>lwres_noopresponse_t</code> to the lightweight resolver&#8217;s canonical format. </p>
<p> <code>lwres_nooprequest_parse()</code> uses context <i>ctx</i> to convert the contents of packet <i>pkt</i> to a <code>lwres_nooprequest_t</code> structure. Buffer <i>b</i> provides space to be used for storing this structure. When the function succeeds, the resulting <code>lwres_nooprequest_t</code> is made available through <i>*structp</i>. <code>lwres_noopresponse_parse()</code> offers the same semantics as <code>lwres_nooprequest_parse()</code> except it yields a <code>lwres_noopresponse_t</code> structure. </p>
<p> <code>lwres_noopresponse_free()</code> and <code>lwres_nooprequest_free()</code> release the memory in resolver context <i>ctx</i> that was allocated to the <code>lwres_noopresponse_t</code> or <code>lwres_nooprequest_t</code> structures referenced via <i>structp</i>.</p>
<h2>RETURN VALUES</h2>
<p> The no-op opcode functions <code>lwres_nooprequest_render()</code>, <code>lwres_noopresponse_render()</code> <code>lwres_nooprequest_parse()</code> and <code>lwres_noopresponse_parse()</code> all return <code>LWRES_R_SUCCESS</code> on success. They return <code>LWRES_R_NOMEMORY</code> if memory allocation fails. <code>LWRES_R_UNEXPECTEDEND</code> is returned if the available space in the buffer <i>b</i> is too small to accommodate the packet header or the <code>lwres_nooprequest_t</code> and <code>lwres_noopresponse_t</code> structures. <code>lwres_nooprequest_parse()</code> and <code>lwres_noopresponse_parse()</code> will return <code>LWRES_R_UNEXPECTEDEND</code> if the buffer is not empty after decoding the received packet. These functions will return <code>LWRES_R_FAILURE</code> if <code>pktflags</code> in the packet header structure <code>lwres_lwpacket_t</code> indicate that the packet is not a response to an earlier query.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres_packet/">lwres_packet</a></code>(3)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
