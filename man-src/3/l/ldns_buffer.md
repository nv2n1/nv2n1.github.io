---
title: "ldns_buffer(3)"
name: "ldns_buffer"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer/"
description: "ldns_buffer"
---

<h2>NAME</h2>
<p> ldns_buffer </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer</i></p>
<dd>
<dd>implementation of buffers to ease operations </p>
<p> ldns_buffers can contain arbitrary information, per octet. You can write<br />
 to the current end of a buffer, read from the current position, and<br />
 access any data within it. </p>
<p> Example use of buffers is in the source code of ef host2str.c<br />
 struct ldns_struct_buffer<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The current position used for reading/writing:</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size_t _position;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The read/write limit:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size_t _limit;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The amount of data the buffer can contain:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size_t _capacity;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The data contained in the buffer:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t *_data;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>If the buffer is fixed it cannot be resized:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>unsigned _fixed : 1;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/** The current state of the buffer. If writing to the buffer fails</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * for any reason, this value is changed. This way, you can perform</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * multiple writes in sequence and check for success afterwards. */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_status _status;</p>
<p> };<br />
 typedef struct ldns_struct_buffer ldns_buffer;</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_buffer_new</i>, <i>ldns_buffer_new_frm_data</i>, <i>ldns_buffer_clear</i>, <i>ldns_buffer_printf</i>, <i>ldns_buffer_free</i>, <i>ldns_buffer_export</i>, <i>ldns_buffer_flip</i>, <i>ldns_buffer_rewind</i>, <i>ldns_buffer_position</i>, <i>ldns_buffer_set_position</i>, <i>ldns_buffer_skip</i>, <i>ldns_buffer_limit</i>, <i>ldns_buffer_set_limit</i>, <i>ldns_buffer_capacity</i>, <i>ldns_buffer_set_capacity</i>, <i>ldns_buffer_reserve</i>, <i>ldns_buffer_at</i>, <i>ldns_buffer_begin</i>, <i>ldns_buffer_end</i>, <i>ldns_buffer_current</i>, <i>ldns_buffer_remaining_at</i>, <i>ldns_buffer_remaining</i>, <i>ldns_buffer_available_at</i>, <i>ldns_buffer_available</i>, <i>ldns_buffer_status</i>, <i>ldns_buffer_status_ok</i>, <i>ldns_buffer_write_at</i>, <i>ldns_buffer_write_at</i>, <i>ldns_buffer_write</i>, <i>ldns_buffer_write_string_at</i>, <i>ldns_buffer_write_string</i>, <i>ldns_buffer_write_u8_at</i>, <i>ldns_buffer_write_u8</i>, <i>ldns_buffer_write_u16_at</i>, <i>ldns_buffer_write_u16</i>, <i>ldns_buffer_read_at</i>, <i>ldns_buffer_read</i>, <i>ldns_buffer_read_u8_at</i>, <i>ldns_buffer_read_u8</i>, <i>ldns_buffer_read_u16_at</i>, <i>ldns_buffer_read_u16</i>, <i>ldns_buffer_read_u32_at</i>, <i>ldns_buffer_read_u32</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
