---
title: "lwres_buffer_back(3)"
name: "lwres_buffer_back"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_buffer_back/"
description: "lwres_buffer_init, lwres_buffer_invalidate, lwres_buffer_add, lwres_buffer_subtract, lwres_buffer_clear, lwres_buffer_first, lwres_buffer_forward, lwres_buffer_back, lwres_buffer_getuint8, lwres_bu..."
---

<h2 class="name">NAME</h2>
<p> lwres_buffer_init, lwres_buffer_invalidate, lwres_buffer_add, lwres_buffer_subtract, lwres_buffer_clear, lwres_buffer_first, lwres_buffer_forward, lwres_buffer_back, lwres_buffer_getuint8, lwres_buffer_putuint8, lwres_buffer_getuint16, lwres_buffer_putuint16, lwres_buffer_getuint32, lwres_buffer_putuint32, lwres_buffer_putmem, lwres_buffer_getmem &#8211; lightweight resolver buffer management </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwbuffer.h&gt;
</code></pre>
<dl>
<dt> <code>void lwres_buffer_init(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, void&nbsp;<wbr>*</code><i>base</i><code>, unsigned int&nbsp;<wbr></code><i>length</i><code>);</code></p>
<dt> <code>void lwres_buffer_invalidate(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_add(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, unsigned int&nbsp;<wbr></code><i>n</i><code>);</code></p>
<dt> <code>void lwres_buffer_subtract(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, unsigned int&nbsp;<wbr></code><i>n</i><code>);</code></p>
<dt> <code>void lwres_buffer_clear(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_first(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_forward(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, unsigned int&nbsp;<wbr></code><i>n</i><code>);</code></p>
<dt> <code>void lwres_buffer_back(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, unsigned int&nbsp;<wbr></code><i>n</i><code>);</code></p>
<dt> <code>lwres_uint8_t lwres_buffer_getuint8(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_putuint8(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_uint8_t&nbsp;<wbr></code><i>val</i><code>);</code></p>
<dt> <code>lwres_uint16_t lwres_buffer_getuint16(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_putuint16(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_uint16_t&nbsp;<wbr></code><i>val</i><code>);</code></p>
<dt> <code>lwres_uint32_t lwres_buffer_getuint32(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>);</code></p>
<dt> <code>void lwres_buffer_putuint32(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, lwres_uint32_t&nbsp;<wbr></code><i>val</i><code>);</code></p>
<dt> <code>void lwres_buffer_putmem(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, const unsigned char&nbsp;<wbr>*</code><i>base</i><code>, unsigned int&nbsp;<wbr></code><i>length</i><code>);</code></p>
<dt> <code>void lwres_buffer_getmem(lwres_buffer_t&nbsp;<wbr>*</code><i>b</i><code>, unsigned char&nbsp;<wbr>*</code><i>base</i><code>, unsigned int&nbsp;<wbr></code><i>length</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions provide bounds checked access to a region of memory where data is being read or written. They are based on, and similar to, the isc_buffer_ functions in the ISC library. </p>
<p> A buffer is a region of memory, together with a set of related subregions. The <i>used region</i> and the <i>available</i> region are disjoint, and their union is the buffer&#8217;s region. The used region extends from the beginning of the buffer region to the last used byte. The available region extends from one byte greater than the last used byte to the end of the buffer&#8217;s region. The size of the used region can be changed using various buffer commands. Initially, the used region is empty. </p>
<p> The used region is further subdivided into two disjoint regions: the <i>consumed region</i> and the <i>remaining region</i>. The union of these two regions is the used region. The consumed region extends from the beginning of the used region to the byte before the <i>current</i> offset (if any). The <i>remaining</i> region the current pointer to the end of the used region. The size of the consumed region can be changed using various buffer commands. Initially, the consumed region is empty. </p>
<p> The <i>active region</i> is an (optional) subregion of the remaining region. It extends from the current offset to an offset in the remaining region. Initially, the active region is empty. If the current offset advances beyond the chosen offset, the active region will also be empty. </p>
<dl>
<dt>
<dd>
/ &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;entire length&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -\ / &#8212; &#8212; -used region&#8211; &#8212; -\/ &#8211;available&#8211;\ + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | consumed | remaining | |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+a b c d e
</dl>
<dl>
<dt>
<dd>
a == base of buffer.b == current pointer.Can be anywhere between a and d.c == active pointer.Meaningful between b and d.d == used pointer.e == length of buffer.
</dl>
<dl>
<dt>
<dd>
<pre><code>
a - e == entire length of buffer.a - d == used region.a - b == consumed region.b - d == remaining region.b - c == optional active region.
</code></pre>
</dl>
<p> <code>lwres_buffer_init()</code> initializes the <code>lwres_buffer_t</code> <i>*b</i> and assocates it with the memory region of size <i>length</i> bytes starting at location <i>base.</i> </p>
<p> <code>lwres_buffer_invalidate()</code> marks the buffer <i>*b</i> as invalid. Invalidating a buffer after use is not required, but makes it possible to catch its possible accidental use. </p>
<p> The functions <code>lwres_buffer_add()</code> and <code>lwres_buffer_subtract()</code> respectively increase and decrease the used space in buffer <i>*b</i> by <i>n</i> bytes. <code>lwres_buffer_add()</code> checks for buffer overflow and <code>lwres_buffer_subtract()</code> checks for underflow. These functions do not allocate or deallocate memory. They just change the value of used. </p>
<p> A buffer is re-initialised by <code>lwres_buffer_clear()</code>. The function sets used, current and active to zero. </p>
<p> <code>lwres_buffer_first</code> makes the consumed region of buffer <i>*p</i> empty by setting current to zero (the start of the buffer). </p>
<p> <code>lwres_buffer_forward()</code> increases the consumed region of buffer <i>*b</i> by <i>n</i> bytes, checking for overflow. Similarly, <code>lwres_buffer_back()</code> decreases buffer <i>b</i>&#8216;s consumed region by <i>n</i> bytes and checks for underflow. </p>
<p> <code>lwres_buffer_getuint8()</code> reads an unsigned 8-bit integer from <i>*b</i> and returns it. <code>lwres_buffer_putuint8()</code> writes the unsigned 8-bit integer <i>val</i> to buffer <i>*b</i>. </p>
<p> <code>lwres_buffer_getuint16()</code> and <code>lwres_buffer_getuint32()</code> are identical to <code>lwres_buffer_putuint8()</code> except that they respectively read an unsigned 16-bit or 32-bit integer in network byte order from <i>b</i>. Similarly, <code>lwres_buffer_putuint16()</code> and <code>lwres_buffer_putuint32()</code> writes the unsigned 16-bit or 32-bit integer <i>val</i> to buffer <i>b</i>, in network byte order. </p>
<p> Arbitrary amounts of data are read or written from a lightweight resolver buffer with <code>lwres_buffer_getmem()</code> and <code>lwres_buffer_putmem()</code> respectively. <code>lwres_buffer_putmem()</code> copies <i>length</i> bytes of memory at <i>base</i> to <i>b</i>. Conversely, <code>lwres_buffer_getmem()</code> copies <i>length</i> bytes of memory from <i>b</i> to <i>base</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
