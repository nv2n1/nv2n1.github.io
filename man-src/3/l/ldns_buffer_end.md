---

title: "ldns_buffer_end(3)"
name: "ldns_buffer_end"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer_end/"
description: "ldns_buffer_limit, ldns_buffer_set_limit, ldns_buffer_capacity, ldns_buffer_set_capacity, ldns_buffer_reserve, ldns_buffer_at, ldns_buffer_begin, ldns_buffer_end, ldns_buffer_current"
---

<p> ldns_buffer_limit, ldns_buffer_set_limit, ldns_buffer_capacity, ldns_buffer_set_capacity, ldns_buffer_reserve, ldns_buffer_at, ldns_buffer_begin, ldns_buffer_end, ldns_buffer_current </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br/>
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> size_t ldns_buffer_limit(ldns_buffer *buffer); </p>
<p> void ldns_buffer_set_limit(ldns_buffer *buffer, size_t limit); </p>
<p> size_t ldns_buffer_capacity(ldns_buffer *buffer); </p>
<p> bool ldns_buffer_set_capacity(ldns_buffer *buffer, size_t capacity); </p>
<p> bool ldns_buffer_reserve(ldns_buffer *buffer, size_t amount); </p>
<p> uint8_t * ldns_buffer_at(const ldns_buffer *buffer, size_t at); </p>
<p> uint8_t * ldns_buffer_begin(const ldns_buffer *buffer); </p>
<p> uint8_t * ldns_buffer_end(ldns_buffer *buffer); </p>
<p> uint8_t * ldns_buffer_current(ldns_buffer *buffer); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer_limit</i>()</dt>
<dd>returns the maximum size of the buffer \param[in] buffer .br Returns the size</dd></dl>
<dl>
<dt> <i>ldns_buffer_set_limit</i>()</dt>
<dd>changes the buffer&#8217;s limit. If the buffer&#8217;s position is greater than the new limit the position is set to the limit. .br <code>buffer</code>: the buffer .br <code>limit</code>: the new limit</dd></dl>
<dl>
<dt> <i>ldns_buffer_capacity</i>()</dt>
<dd>returns the number of bytes the buffer can hold. .br <code>buffer</code>: the buffer .br Returns the number of bytes</dd></dl>
<dl>
<dt> <i>ldns_buffer_set_capacity</i>()</dt>
<dd>changes the buffer&#8217;s capacity. The data is reallocated so any pointers to the data may become invalid. The buffer&#8217;s limit is set to the buffer&#8217;s new capacity. .br <code>buffer</code>: the buffer .br <code>capacity</code>: the capacity to use .br Returns whether this failed or succeeded</dd></dl>
<dl>
<dt> <i>ldns_buffer_reserve</i>()</dt>
<dd>ensures BUFFER can contain at least AMOUNT more bytes. The buffer&#8217;s capacity is increased if necessary using buffer_set_capacity(). </dd>
<p> The buffer&#8217;s limit is always set to the (possibly increased) capacity. .br <code>buffer</code>: the buffer .br <code>amount</code>: amount to use .br Returns whether this failed or succeeded</dl>
<dl>
<dt> <i>ldns_buffer_at</i>()</dt>
<dd>returns a pointer to the data at the indicated position. .br <code>buffer</code>: the buffer .br <code>at</code>: position .br Returns the pointer to the data</dd></dl>
<dl>
<dt> <i>ldns_buffer_begin</i>()</dt>
<dd>returns a pointer to the beginning of the buffer (the data at position 0). .br <code>buffer</code>: the buffer .br Returns the pointer</dd></dl>
<dl>
<dt> <i>ldns_buffer_end</i>()</dt>
<dd>returns a pointer to the end of the buffer (the data at the buffer&#8217;s limit). .br <code>buffer</code>: the buffer .br Returns the pointer</dd></dl>
<dl>
<dt> <i>ldns_buffer_current</i>()</dt>
<dd>returns a pointer to the data at the buffer&#8217;s current position. .br <code>buffer</code>: the buffer .br Returns the pointer</dd></dl>
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
