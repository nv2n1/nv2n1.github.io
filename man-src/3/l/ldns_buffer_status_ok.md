---
title: "ldns_buffer_status_ok(3)"
name: "ldns_buffer_status_ok"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer_status_ok/"
description: "ldns_buffer_remaining_at, ldns_buffer_remaining, ldns_buffer_available_at, ldns_buffer_available, ldns_buffer_status, ldns_buffer_status_ok"
---

<h2>NAME</h2>
<p> ldns_buffer_remaining_at, ldns_buffer_remaining, ldns_buffer_available_at, ldns_buffer_available, ldns_buffer_status, ldns_buffer_status_ok </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> size_t ldns_buffer_remaining_at(ldns_buffer *buffer, size_t at); </p>
<p> size_t ldns_buffer_remaining(ldns_buffer *buffer); </p>
<p> int ldns_buffer_available_at(ldns_buffer *buffer, size_t at, size_t count); </p>
<p> int ldns_buffer_available(ldns_buffer *buffer, size_t count); </p>
<p> ldns_status ldns_buffer_status(ldns_buffer *buffer); </p>
<p> bool ldns_buffer_status_ok(ldns_buffer *buffer); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer_remaining_at</i>()</p>
<dd>returns the number of bytes remaining between the indicated position and the limit. .br <code>buffer</code>: the buffer .br <code>at</code>: indicated position .br Returns number of bytes</dl>
<dl>
<dt> <i>ldns_buffer_remaining</i>()</p>
<dd>returns the number of bytes remaining between the buffer&#8217;s position and limit. .br <code>buffer</code>: the buffer .br Returns the number of bytes</dl>
<dl>
<dt> <i>ldns_buffer_available_at</i>()</p>
<dd>checks if the buffer has at least COUNT more bytes available. Before reading or writing the caller needs to ensure enough space is available! .br <code>buffer</code>: the buffer .br <code>at</code>: indicated position .br <code>count</code>: how much is available .br Returns true or false (as int?)</dl>
<dl>
<dt> <i>ldns_buffer_available</i>()</p>
<dd>checks if the buffer has count bytes available at the current position .br <code>buffer</code>: the buffer .br <code>count</code>: how much is available .br Returns true or false (as int?)</dl>
<dl>
<dt> <i>ldns_buffer_status</i>()</p>
<dd>returns the status of the buffer \param[in] buffer .br Returns the status</dl>
<dl>
<dt> <i>ldns_buffer_status_ok</i>()</p>
<dd>returns true if the status of the buffer is LDNS_STATUS_OK, false otherwise .br <code>buffer</code>: the buffer .br Returns true or false</dl>
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
