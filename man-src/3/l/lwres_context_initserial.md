---
title: "lwres_context_initserial(3)"
name: "lwres_context_initserial"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_context_initserial/"
description: "lwres_context_create, lwres_context_destroy, lwres_context_nextserial, lwres_context_initserial, lwres_context_freemem, lwres_context_allocmem, lwres_context_sendrecv – lightweight resolver context..."
---

<h2 class="name">NAME</h2>
<p> lwres_context_create, lwres_context_destroy, lwres_context_nextserial, lwres_context_initserial, lwres_context_freemem, lwres_context_allocmem, lwres_context_sendrecv &#8211; lightweight resolver context management </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<dl>
<dt> <code>lwres_result_t lwres_context_create(lwres_context_t&nbsp;<wbr>**</code><i>contextp</i><code>, void&nbsp;<wbr>*</code><i>arg</i><code>, lwres_malloc_t&nbsp;<wbr></code><i>malloc_function</i><code>, lwres_free_t&nbsp;<wbr></code><i>free_function</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_context_destroy(lwres_context_t&nbsp;<wbr>**</code><i>contextp</i><code>);</code></p>
<dt> <code>void lwres_context_initserial(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, lwres_uint32_t&nbsp;<wbr></code><i>serial</i><code>);</code></p>
<dt> <code>lwres_uint32_t lwres_context_nextserial(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>);</code></p>
<dt> <code>void lwres_context_freemem(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, void&nbsp;<wbr>*</code><i>mem</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>void lwres_context_allocmem(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></p>
<dt> <code>void * lwres_context_sendrecv(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, void&nbsp;<wbr>*</code><i>sendbase</i><code>, int&nbsp;<wbr></code><i>sendlen</i><code>, void&nbsp;<wbr>*</code><i>recvbase</i><code>, int&nbsp;<wbr></code><i>recvlen</i><code>, int&nbsp;<wbr>*</code><i>recvd_len</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_context_create()</code></p>
<dd>creates a <code>lwres_context_t</code> structure for use in lightweight resolver operations. It holds a socket and other data needed for communicating with a resolver daemon. The new <code>lwres_context_t</code> is returned through <i>contextp</i>, a pointer to a <code>lwres_context_t</code> pointer. This <code>lwres_context_t</code> pointer must initially be NULL, and is modified to point to the newly created <code>lwres_context_t</code>. </p>
<p> When the lightweight resolver needs to perform dynamic memory allocation, it will call <i>malloc_function</i> to allocate memory and <i>free_function</i> to free it. If <i>malloc_function</i> and <i>free_function</i> are NULL, memory is allocated using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). and <code><a href="/docs/linux/man/3-free/">free</a></code>(3). It is not permitted to have a NULL <i>malloc_function</i> and a non-NULL <i>free_function</i> or vice versa. <i>arg</i> is passed as the first parameter to the memory allocation functions. If <i>malloc_function</i> and <i>free_function</i> are NULL, <i>arg</i> is unused and should be passed as NULL. </p>
<p> Once memory for the structure has been allocated, it is initialized using <code><a href="/docs/linux/man/3-lwres_conf_init/">lwres_conf_init</a></code>(3) and returned via <i>*contextp</i>. </p>
<p> <code>lwres_context_destroy()</code> destroys a <code>lwres_context_t</code>, closing its socket. <i>contextp</i> is a pointer to a pointer to the context that is to be destroyed. The pointer will be set to NULL when the context has been destroyed. </p>
<p> The context holds a serial number that is used to identify resolver request packets and associate responses with the corresponding requests. This serial number is controlled using <code>lwres_context_initserial()</code> and <code>lwres_context_nextserial()</code>. <code>lwres_context_initserial()</code> sets the serial number for context <i>*ctx</i> to <i>serial</i>. <code>lwres_context_nextserial()</code> increments the serial number and returns the previous value. </p>
<p> Memory for a lightweight resolver context is allocated and freed using <code>lwres_context_allocmem()</code> and <code>lwres_context_freemem()</code>. These use whatever allocations were defined when the context was created with <code>lwres_context_create()</code>. <code>lwres_context_allocmem()</code> allocates <i>len</i> bytes of memory and if successful returns a pointer to the allocated storage. <code>lwres_context_freemem()</code> frees <i>len</i> bytes of space starting at location <i>mem</i>. </p>
<p> <code>lwres_context_sendrecv()</code> performs I/O for the context <i>ctx</i>. Data are read and written from the context&#8217;s socket. It writes data from <i>sendbase</i> &#8212; typically a lightweight resolver query packet &#8212; and waits for a reply which is copied to the receive buffer at <i>recvbase</i>. The number of bytes that were written to this receive buffer is returned in <i>*recvd_len</i>.</p>
<h2>RETURN VALUES</h2>
<p> <code>lwres_context_create()</code> returns <code>LWRES_R_NOMEMORY</code> if memory for the <code>struct lwres_context</code> could not be allocated, <code>LWRES_R_SUCCESS</code> otherwise. </p>
<p> Successful calls to the memory allocator <code>lwres_context_allocmem()</code> return a pointer to the start of the allocated space. It returns NULL if memory could not be allocated. </p>
<p> <code>LWRES_R_SUCCESS</code> is returned when <code>lwres_context_sendrecv()</code> completes successfully. <code>LWRES_R_IOERROR</code> is returned if an I/O error occurs and <code>LWRES_R_TIMEOUT</code> is returned if <code>lwres_context_sendrecv()</code> times out waiting for a response.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres_conf_init/">lwres_conf_init</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001, 2003 Internet Software Consortium. </p>
<h2>Index</h2>
