---
title: "xdrrec_eof(3)"
name: "xdrrec_eof"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrrec_eof/"
description: "xdr – library routines for external data representation"
---

<p>xdr &#8211; library routines for external data representation</p>
<h2>Synopsis And Description</h2>
<p>These routines allow C programmers to describe arbitrary data structures in a machine-independent fashion. Data for remote procedure calls are transmitted using these routines. </p>
<p> The prototypes below are declared in <i>&lt;rpc/xdr.h&gt;</i> and make use of the following types: </p>
<dl>
<dd><code>typedef int </code><i>bool_t</i><code>;</code> </p>
<p> <code>typedef bool_t (*</code><i>xdrproc_t</i><code>) (XDR *, void *,&#8230;);</code></dl>
<p> For the declaration of the <i>XDR</i> type, see <i>&lt;rpc/xdr.h&gt;</i>. </p>
<pre><code>bool_t xdr_array(XDR *</code><i>xdrs</i><code>, char **</code><i>arrp</i><code>, unsigned int *</code><i>sizep</i><code>,</code>
<code> unsigned int </code><i>maxsize</i><code>, unsigned int </code><i>elsize</i><code>,</code>
<code> xdrproc_t </code><i>elproc</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between variable-length arrays and their corresponding external representations. The argument <i>arrp</i> is the address of the pointer to the array, while <i>sizep</i> is the address of the element count of the array; this element count cannot exceed <i>maxsize</i>. The argument <i>elsize</i> is the <i>sizeof</i> each of the array&#8217;s elements, and <i>elproc</i> is an XDR filter that translates between the array elements&#8217; C form, and their external representation. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_bool(XDR *</code><i>xdrs</i><code>, bool_t *</code><i>bp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between booleans (C integers) and their external representations. When encoding data, this filter produces values of either one or zero. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_bytes(XDR *</code><i>xdrs</i><code>, char **</code><i>sp</i><code>, unsigned int *</code><i>sizep</i><code>,</code>
<code> unsigned int </code><i>maxsize</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between counted byte strings and their external representations. The argument <i>sp</i> is the address of the string pointer. The length of the string is located at address <i>sizep</i>; strings cannot be longer than <i>maxsize</i>. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_char(XDR *</code><i>xdrs</i><code>, char *</code><i>cp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C characters and their external representations. This routine returns one if it succeeds, zero otherwise. Note: encoded characters are not packed, and occupy 4 bytes each. For arrays of characters, it is worthwhile to consider <code>xdr_bytes</code>(), <code>xdr_opaque</code>() or <code>xdr_string</code>().</dl>
<pre><code>void xdr_destroy(XDR *</code><i>xdrs</i><code>);</code></pre>
<dl>
<dd>A macro that invokes the destroy routine associated with the XDR stream, <i>xdrs</i>. Destruction usually involves freeing private data structures associated with the stream. Using <i>xdrs</i> after invoking <code>xdr_destroy</code>() is undefined.</dl>
<pre><code>bool_t xdr_double(XDR *</code><i>xdrs</i><code>, double *</code><i>dp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>double</i> precision numbers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_enum(XDR *</code><i>xdrs</i><code>, enum_t *</code><i>ep</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>enum</i>s (actually integers) and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_float(XDR *</code><i>xdrs</i><code>, float *</code><i>fp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>float</i>s and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>void xdr_free(xdrproc_t </code><i>proc</i><code>, char *</code><i>objp</i><code>);</code></pre>
<dl>
<dd>Generic freeing routine. The first argument is the XDR routine for the object being freed. The second argument is a pointer to the object itself. Note: the pointer passed to this routine is <i>not</i> freed, but what it points to <i>is</i> freed (recursively).</dl>
<pre><code>unsigned int xdr_getpos(XDR *</code><i>xdrs</i><code>);</code></pre>
<dl>
<dd>A macro that invokes the get-position routine associated with the XDR stream, <i>xdrs</i>. The routine returns an unsigned integer, which indicates the position of the XDR byte stream. A desirable feature of XDR streams is that simple arithmetic works with this number, although the XDR stream instances need not guarantee this.</dl>
<pre><code>long *xdr_inline(XDR *</code><i>xdrs</i><code>, int </code><i>len</i><code>);</code></pre>
<dl>
<dd>A macro that invokes the inline routine associated with the XDR stream, <i>xdrs</i>. The routine returns a pointer to a contiguous piece of the stream&#8217;s buffer; <i>len</i> is the byte length of the desired buffer. Note: pointer is cast to <i>long&nbsp;*</i>.</p>
<dd>Warning: <code>xdr_inline</code>() may return NULL (0) if it cannot allocate a contiguous piece of a buffer. Therefore the behavior may vary among stream instances; it exists for the sake of efficiency.</dl>
<pre><code>bool_t xdr_int(XDR *</code><i>xdrs</i><code>, int *</code><i>ip</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_long(XDR *</code><i>xdrs</i><code>, long *</code><i>lp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>long</i> integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>void xdrmem_create(XDR *</code><i>xdrs</i><code>, char *</code><i>addr</i><code>, unsigned int </code><i>size</i><code>,</code>
<code> enum xdr_op </code><i>op</i><code>);</code></pre>
<dl>
<dd>This routine initializes the XDR stream object pointed to by <i>xdrs</i>. The stream&#8217;s data is written to, or read from, a chunk of memory at location <i>addr</i> whose length is no more than <i>size</i> bytes long. The <i>op</i> determines the direction of the XDR stream (either <code>XDR_ENCODE</code>, <code>XDR_DECODE</code>, or <code>XDR_FREE</code>).</dl>
<pre><code>bool_t xdr_opaque(XDR *</code><i>xdrs</i><code>, char *</code><i>cp</i><code>, unsigned int </code><i>cnt</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between fixed size opaque data and its external representation. The argument <i>cp</i> is the address of the opaque object, and <i>cnt</i> is its size in bytes. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_pointer(XDR *</code><i>xdrs</i><code>, char **</code><i>objpp</i><code>,</code>
<code> unsigned int </code><i>objsize</i><code>, xdrproc_t </code><i>xdrobj</i><code>);</code></pre>
<dl>
<dd>Like <code>xdr_reference</code>() except that it serializes null pointers, whereas <code>xdr_reference</code>() does not. Thus, <code>xdr_pointer</code>() can represent recursive data structures, such as binary trees or linked lists.</dl>
<pre><code>void xdrrec_create(XDR *</code><i>xdrs</i><code>, unsigned int </code><i>sendsize</i><code>,</code>
<code> unsigned int </code><i>recvsize</i><code>, char *</code><i>handle</i><code>,</code>
<code> int (*</code><i>readit</i><code>) (char *, char *, int),</code>
<code> int (*</code><i>writeit</i><code>) (char *, char *, int));</code></pre>
<dl>
<dd>This routine initializes the XDR stream object pointed to by <i>xdrs</i>. The stream&#8217;s data is written to a buffer of size <i>sendsize</i>; a value of zero indicates the system should use a suitable default. The stream&#8217;s data is read from a buffer of size <i>recvsize</i>; it too can be set to a suitable default by passing a zero value. When a stream&#8217;s output buffer is full, <i>writeit</i> is called. Similarly, when a stream&#8217;s input buffer is empty, <i>readit</i> is called. The behavior of these two routines is similar to the system calls <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2), except that <i>handle</i> is passed to the former routines as the first argument. Note: the XDR stream&#8217;s <i>op</i> field must be set by the caller.</p>
<dd>Warning: to read from an XDR stream created by this API, you&#8217;ll need to call <code>xdrrec_skiprecord</code>() first before calling any other XDR APIs. This inserts additional bytes in the stream to provide record boundary information. Also, XDR streams created with different <code>xdr*_create</code> APIs are not compatible for the same reason.</dl>
<pre><code>bool_t xdrrec_endofrecord(XDR *</code><i>xdrs</i><code>, int </code><i>sendnow</i><code>);</code></pre>
<dl>
<dd>This routine can be invoked only on streams created by <code>xdrrec_create</code>(). The data in the output buffer is marked as a completed record, and the output buffer is optionally written out if <i>sendnow</i> is nonzero. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdrrec_eof(XDR *</code><i>xdrs</i><code>);</code></pre>
<dl>
<dd>This routine can be invoked only on streams created by <code>xdrrec_create</code>(). After consuming the rest of the current record in the stream, this routine returns one if the stream has no more input, zero otherwise.</dl>
<pre><code>bool_t xdrrec_skiprecord(XDR *</code><i>xdrs</i><code>);</code></pre>
<dl>
<dd>This routine can be invoked only on streams created by <code>xdrrec_create</code>(). It tells the XDR implementation that the rest of the current record in the stream&#8217;s input buffer should be discarded. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_reference(XDR *</code><i>xdrs</i><code>, char **</code><i>pp</i><code>, unsigned int </code><i>size</i><code>,</code>
<code> xdrproc_t </code><i>proc</i><code>);</code></pre>
<dl>
<dd>A primitive that provides pointer chasing within structures. The argument <i>pp</i> is the address of the pointer; <i>size</i> is the <i>sizeof</i> the structure that <i>*pp</i> points to; and <i>proc</i> is an XDR procedure that filters the structure between its C form and its external representation. This routine returns one if it succeeds, zero otherwise.</p>
<dd>Warning: this routine does not understand null pointers. Use <code>xdr_pointer</code>() instead.</dl>
<pre><code>xdr_setpos(XDR *</code><i>xdrs</i><code>, unsigned int </code><i>pos</i><code>);</code></pre>
<dl>
<dd>A macro that invokes the set position routine associated with the XDR stream <i>xdrs</i>. The argument <i>pos</i> is a position value obtained from <code>xdr_getpos</code>(). This routine returns one if the XDR stream could be repositioned, and zero otherwise.</p>
<dd>Warning: it is difficult to reposition some types of XDR streams, so this routine may fail with one type of stream and succeed with another.</dl>
<pre><code>bool_t xdr_short(XDR *</code><i>xdrs</i><code>, short *</code><i>sp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>short</i> integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>void xdrstdio_create(XDR *</code><i>xdrs</i><code>, FILE *</code><i>file</i><code>, enum xdr_op </code><i>op</i><code>);</code></pre>
<dl>
<dd>This routine initializes the XDR stream object pointed to by <i>xdrs</i>. The XDR stream data is written to, or read from, the <i>stdio</i> stream <i>file</i>. The argument <i>op</i> determines the direction of the XDR stream (either <code>XDR_ENCODE</code>, <code>XDR_DECODE</code>, or <code>XDR_FREE</code>).</p>
<dd>Warning: the destroy routine associated with such XDR streams calls <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3) on the <i>file</i> stream, but never <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3).</dl>
<pre><code>bool_t xdr_string(XDR *</code><i>xdrs</i><code>, char **</code><i>sp</i><code>, unsigned int </code><i>maxsize</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C strings and their corresponding external representations. Strings cannot be longer than <i>maxsize</i>. Note: <i>sp</i> is the address of the string&#8217;s pointer. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_u_char(XDR *</code><i>xdrs</i><code>, unsigned char *</code><i>ucp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between <i>unsigned</i> C characters and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_u_int(XDR *</code><i>xdrs</i><code>, unsigned *</code><i>up</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>unsigned</i> integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_u_long(XDR *</code><i>xdrs</i><code>, unsigned long *</code><i>ulp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>unsigned long</i> integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_u_short(XDR *</code><i>xdrs</i><code>, unsigned short *</code><i>usp</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between C <i>unsigned short</i> integers and their external representations. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_union(XDR *</code><i>xdrs</i><code>, int *</code><i>dscmp</i><code>, char *</code><i>unp</i><code>,</code>
<code> struct xdr_discrim *</code><i>choices</i><code>,</code>
<code> xdrproc_t </code><i>defaultarm</i><code>); /* may equal NULL */</code></pre>
<dl>
<dd>A filter primitive that translates between a discriminated C <i>union</i> and its corresponding external representation. It first translates the discriminant of the union located at <i>dscmp</i>. This discriminant is always an <i>enum_t</i>. Next the union located at <i>unp</i> is translated. The argument <i>choices</i> is a pointer to an array of <code>xdr_discrim</code>() structures. Each structure contains an ordered pair of [<i>value</i>,<i>proc</i>]. If the union&#8217;s discriminant is equal to the associated <i>value</i>, then the <i>proc</i> is called to translate the union. The end of the <code>xdr_discrim</code>() structure array is denoted by a routine of value NULL. If the discriminant is not found in the <i>choices</i> array, then the <i>defaultarm</i> procedure is called (if it is not NULL). Returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_vector(XDR *</code><i>xdrs</i><code>, char *</code><i>arrp</i><code>, unsigned int </code><i>size</i><code>,</code>
<code> unsigned int </code><i>elsize</i><code>, xdrproc_t </code><i>elproc</i><code>);</code></pre>
<dl>
<dd>A filter primitive that translates between fixed-length arrays and their corresponding external representations. The argument <i>arrp</i> is the address of the pointer to the array, while <i>size</i> is the element count of the array. The argument <i>elsize</i> is the <i>sizeof</i> each of the array&#8217;s elements, and <i>elproc</i> is an XDR filter that translates between the array elements&#8217; C form, and their external representation. This routine returns one if it succeeds, zero otherwise.</dl>
<pre><code>bool_t xdr_void(void);</code></pre>
<dl>
<dd>This routine always returns one. It may be passed to RPC routines that require a function argument, where nothing is to be done.</dl>
<pre><code>bool_t xdr_wrapstring(XDR *</code><i>xdrs</i><code>, char **</code><i>sp</i><code>);</code></pre>
<dl>
<dd>A primitive that calls <code>xdr_string(xdrs, sp,MAXUN.UNSIGNED );</code> where <code>MAXUN.UNSIGNED</code> is the maximum value of an unsigned integer. <code>xdr_wrapstring</code>() is handy because the RPC package passes a maximum of two XDR routines as arguments, and <code>xdr_string</code>(), one of the most frequently used primitives, requires three. Returns one if it succeeds, zero otherwise.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>xdr_array</code>(), <code>xdr_bool</code>(),<br />
 <code>xdr_bytes</code>(), <code>xdr_char</code>(),<br />
 <code>xdr_destroy</code>(), <code>xdr_double</code>(),<br />
 <code>xdr_enum</code>(), <code>xdr_float</code>(),<br />
 <code>xdr_free</code>(), <code>xdr_getpos</code>(),<br />
 <code>xdr_inline</code>(), <code>xdr_int</code>(),<br />
 <code>xdr_long</code>(), <code>xdrmem_create</code>(),<br />
 <code>xdr_opaque</code>(), <code>xdr_pointer</code>(),<br />
 <code>xdrrec_create</code>(), <code>xdrrec_eof</code>(),<br />
 <code>xdrrec_endofrecord</code>(),<br />
 <code>xdrrec_skiprecord</code>(),<br />
 <code>xdr_reference</code>(), <code>xdr_setpos</code>(),<br />
 <code>xdr_short</code>(), <code>xdrstdio_create</code>(),<br />
 <code>xdr_string</code>(), <code>xdr_u_char</code>(),<br />
 <code>xdr_u_int</code>(), <code>xdr_u_long</code>(),<br />
 <code>xdr_u_short</code>(), <code>xdr_union</code>(),<br />
 <code>xdr_vector</code>(), <code>xdr_void</code>(),<br />
 <code>xdr_wrapstring</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rpc/">rpc</a></code>(3) </p>
<p> The following manuals:</p>
<dl>
<dd>eXternal Data Representation Standard: Protocol Specification<br />
 eXternal Data Representation: Sun Technical Notes<br />
 <i>XDR: External Data Representation Standard</i>, RFC 1014, Sun Microsystems, Inc., USC-ISI.</dl>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
