---
title: "ldns_buffer_set_position(3)"
name: "ldns_buffer_set_position"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer_set_position/"
description: "ldns_buffer_flip, ldns_buffer_rewind, ldns_buffer_position, ldns_buffer_set_position, ldns_buffer_skip"
---

<h2>NAME</h2>
<p> ldns_buffer_flip, ldns_buffer_rewind, ldns_buffer_position, ldns_buffer_set_position, ldns_buffer_skip </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_buffer_flip(ldns_buffer *buffer); </p>
<p> void ldns_buffer_rewind(ldns_buffer *buffer); </p>
<p> size_t ldns_buffer_position(ldns_buffer *buffer); </p>
<p> void ldns_buffer_set_position(ldns_buffer *buffer, size_t mark); </p>
<p> void ldns_buffer_skip(ldns_buffer *buffer, ssize_t count); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer_flip</i>()</p>
<dd>makes the buffer ready for reading the data that has been written to the buffer. The buffer&#8217;s limit is set to the current position and the position is set to 0. </p>
<p> .br <code>buffer</code>: the buffer to flip .br Returns void</dl>
<dl>
<dt> <i>ldns_buffer_rewind</i>()</p>
<dd>make the buffer ready for re-reading the data. The buffer&#8217;s position is reset to 0. .br <code>buffer</code>: the buffer to rewind</dl>
<dl>
<dt> <i>ldns_buffer_position</i>()</p>
<dd>returns the current position in the buffer (as a number of bytes) .br <code>buffer</code>: the buffer .br Returns the current position</dl>
<dl>
<dt> <i>ldns_buffer_set_position</i>()</p>
<dd>sets the buffer&#8217;s position to MARK. The position must be less than or equal to the buffer&#8217;s limit. .br <code>buffer</code>: the buffer .br <code>mark</code>: the mark to use</dl>
<dl>
<dt> <i>ldns_buffer_skip</i>()</p>
<dd>changes the buffer&#8217;s position by COUNT bytes. The position must not be moved behind the buffer&#8217;s limit or before the beginning of the buffer. .br <code>buffer</code>: the buffer .br <code>count</code>: the count to use</dl>
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
