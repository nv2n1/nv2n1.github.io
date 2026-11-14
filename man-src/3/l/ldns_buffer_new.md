---
title: "ldns_buffer_new(3)"
name: "ldns_buffer_new"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer_new/"
description: "ldns_buffer_new, ldns_buffer_new_frm_data, ldns_buffer_clear, ldns_buffer_printf, ldns_buffer_free, ldns_buffer_export"
---

<h2>NAME</h2>
<p> ldns_buffer_new, ldns_buffer_new_frm_data, ldns_buffer_clear, ldns_buffer_printf, ldns_buffer_free, ldns_buffer_export </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_buffer* ldns_buffer_new(size_t capacity); </p>
<p> void ldns_buffer_new_frm_data(ldns_buffer *buffer, void *data, size_t size); </p>
<p> void ldns_buffer_clear(ldns_buffer *buffer); </p>
<p> int ldns_buffer_printf(ldns_buffer *buffer, const char *format, &#8230;); </p>
<p> void ldns_buffer_free(ldns_buffer *buffer); </p>
<p> void* ldns_buffer_export(ldns_buffer *buffer); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer_new</i>()</p>
<dd>creates a new buffer with the specified capacity. </p>
<p> .br <code>capacity</code>: the size (in bytes) to allocate for the buffer .br Returns the created buffer</dl>
<dl>
<dt> <i>ldns_buffer_new_frm_data</i>()</p>
<dd>creates a buffer with the specified data. The data IS copied and MEMORY allocations are done. The buffer is not fixed and can be resized using buffer_reserve(). </p>
<p> .br <code>buffer</code>: pointer to the buffer to put the data in .br <code>data</code>: the data to encapsulate in the buffer .br <code>size</code>: the size of the data</dl>
<dl>
<dt> <i>ldns_buffer_clear</i>()</p>
<dd>clears the buffer and make it ready for writing. The buffer&#8217;s limit is set to the capacity and the position is set to 0. .br <code>buffer</code>: the buffer to clear</dl>
<dl>
<dt> <i>ldns_buffer_printf</i>()</p>
<dd>prints to the buffer, increasing the capacity if required using buffer_reserve(). The buffer&#8217;s position is set to the terminating &#8216;\0&#8217; Returns the number of characters written (not including the terminating &#8216;\0&#8217;) or -1 on failure.</dl>
<dl>
<dt> <i>ldns_buffer_free</i>()</p>
<dd>frees the buffer. .br <code>*buffer</code>: the buffer to be freed .br Returns void</dl>
<dl>
<dt> <i>ldns_buffer_export</i>()</p>
<dd>Makes the buffer fixed and returns a pointer to the data. The caller is responsible for free&#8217;ing the result. .br <code>*buffer</code>: the buffer to be exported .br Returns void</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_buffer</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
