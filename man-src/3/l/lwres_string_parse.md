---
title: "lwres_string_parse(3)"
name: "lwres_string_parse"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_string_parse/"
description: "lwres_string_parse, lwres_addr_parse, lwres_getaddrsbyname, lwres_getnamebyaddr – lightweight resolver utility functions"
---

<h2 class="name">NAME</h2>
<p> lwres_string_parse, lwres_addr_parse, lwres_getaddrsbyname, lwres_getnamebyaddr &#8211; lightweight resolver utility functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<dl>
<dt> <code>lwres_result_t lwres_string_parse(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, char&nbsp;<wbr>**</code><i>c</i><code>, lwres_uint16_t&nbsp;<wbr>*</code><i>len</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_addr_parse(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_addr_t&nbsp;<wbr>*</code><i>addr</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_getaddrsbyname(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, const char&nbsp;<wbr>*</code><i>name</i><code>, lwres_uint32_t&nbsp;<wbr></code><i>addrtypes</i><code>, lwres_gabnresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_getnamebyaddr(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_uint32_t&nbsp;<wbr></code><i>addrtype</i><code>, lwres_uint16_t&nbsp;<wbr></code><i>addrlen</i><code>, const unsigned char&nbsp;<wbr>*</code><i>addr</i><code>, lwres_gnbaresponse_t&nbsp;<wbr>**</code><i>structp</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_string_parse()</code></p>
<dd>retrieves a DNS-encoded string starting the current pointer of lightweight resolver buffer <i>b</i>: i.e. <code>b-&gt;current</code>. When the function returns, the address of the first byte of the encoded string is returned via <i>*c</i> and the length of that string is given by <i>*len</i>. The buffer&#8217;s current pointer is advanced to point at the character following the string length, the encoded string, and the trailing <code>NULL</code> character. </p>
<p> <code>lwres_addr_parse()</code> extracts an address from the buffer <i>b</i>. The buffer&#8217;s current pointer <code>b-&gt;current</code> is presumed to point at an encoded address: the address preceded by a 32-bit protocol family identifier and a 16-bit length field. The encoded address is copied to <code>addr-&gt;address</code> and <code>addr-&gt;length</code> indicates the size in bytes of the address that was copied. <code>b-&gt;current</code> is advanced to point at the next byte of available data in the buffer following the encoded address. </p>
<p> <code>lwres_getaddrsbyname()</code> and <code>lwres_getnamebyaddr()</code> use the <code>lwres_gnbaresponse_t</code> structure defined below: </p>
<dl>
<dt>
<dd>
<pre><code>
typedef struct {
    lwres_uint32_t flags;
    lwres_uint16_t naliases;
    lwres_uint16_t naddrs;
    char *realname;
    char **aliases;
    lwres_uint16_t realnamelen;
    lwres_uint16_t *aliaslen;
    lwres_addrlist_t addrs;
    void *base;
    size_t baselen;
} lwres_gabnresponse_t;
</code></pre>
</dl>
<p> The contents of this structure are not manipulated directly but they are controlled through the <code><a href="/docs/linux/man/3-lwres_gabn/">lwres_gabn</a></code>(3) functions. </p>
<p> The lightweight resolver uses <code>lwres_getaddrsbyname()</code> to perform foward lookups. Hostname <i>name</i> is looked up using the resolver context <i>ctx</i> for memory allocation. <i>addrtypes</i> is a bitmask indicating which type of addresses are to be looked up. Current values for this bitmask are <code>LWRES_ADDRTYPE_V4</code> for IPv4 addresses and <code>LWRES_ADDRTYPE_V6</code> for IPv6 addresses. Results of the lookup are returned in <i>*structp</i>. </p>
<p> <code>lwres_getnamebyaddr()</code> performs reverse lookups. Resolver context <i>ctx</i> is used for memory allocation. The address type is indicated by <i>addrtype</i>: <code>LWRES_ADDRTYPE_V4</code> or <code>LWRES_ADDRTYPE_V6</code>. The address to be looked up is given by <i>addr</i> and its length is <i>addrlen</i> bytes. The result of the function call is made available through <i>*structp</i>.</p>
<h2>RETURN VALUES</h2>
<p> Successful calls to <code>lwres_string_parse()</code> and <code>lwres_addr_parse()</code> return <code>LWRES_R_SUCCESS.</code> Both functions return <code>LWRES_R_FAILURE</code> if the buffer is corrupt or <code>LWRES_R_UNEXPECTEDEND</code> if the buffer has less space than expected for the components of the encoded string or address. </p>
<p> <code>lwres_getaddrsbyname()</code> returns <code>LWRES_R_SUCCESS</code> on success and it returns <code>LWRES_R_NOTFOUND</code> if the hostname <i>name</i> could not be found. </p>
<p> <code>LWRES_R_SUCCESS</code> is returned by a successful call to <code>lwres_getnamebyaddr()</code>. </p>
<p> Both <code>lwres_getaddrsbyname()</code> and <code>lwres_getnamebyaddr()</code> return <code>LWRES_R_NOMEMORY</code> when memory allocation requests fail and <code>LWRES_R_UNEXPECTEDEND</code> if the buffers used for sending queries and receiving replies are too small.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres_buffer/">lwres_buffer</a></code>(3), <code><a href="/docs/linux/man/3-lwres_gabn/">lwres_gabn</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
