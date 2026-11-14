---
title: "ldns_buffer_write_string_at(3)"
name: "ldns_buffer_write_string_at"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer_write_string_at/"
description: "ldns_buffer_write_at, ldns_buffer_write_at, ldns_buffer_write, ldns_buffer_write_string_at, ldns_buffer_write_string, ldns_buffer_write_u8_at, ldns_buffer_write_u8, ldns_buffer_write_u16_at, ldns_b..."
---

<h2>NAME</h2>
<p> ldns_buffer_write_at, ldns_buffer_write_at, ldns_buffer_write, ldns_buffer_write_string_at, ldns_buffer_write_string, ldns_buffer_write_u8_at, ldns_buffer_write_u8, ldns_buffer_write_u16_at, ldns_buffer_write_u16, ldns_buffer_read_at, ldns_buffer_read, ldns_buffer_read_u8_at, ldns_buffer_read_u8, ldns_buffer_read_u16_at, ldns_buffer_read_u16, ldns_buffer_read_u32_at, ldns_buffer_read_u32 </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_buffer_write_at(ldns_buffer *buffer, size_t at, const void *data, size_t count); </p>
<p> void ldns_buffer_write_at(ldns_buffer *buffer, size_t at, const void *data, size_t count); </p>
<p> void ldns_buffer_write(ldns_buffer *buffer, const void *data, size_t count); </p>
<p> void ldns_buffer_write_string_at(ldns_buffer *buffer, size_t at, const char *str); </p>
<p> void ldns_buffer_write_string(ldns_buffer *buffer, const char *str); </p>
<p> void ldns_buffer_write_u8_at(ldns_buffer *buffer, size_t at, uint8_t data); </p>
<p> void ldns_buffer_write_u8(ldns_buffer *buffer, uint8_t data); </p>
<p> void ldns_buffer_write_u16_at(ldns_buffer *buffer, size_t at, uint16_t data); </p>
<p> void ldns_buffer_write_u16(ldns_buffer *buffer, uint16_t data); </p>
<p> void ldns_buffer_read_at(ldns_buffer *buffer, size_t at, void *data, size_t count); </p>
<p> void ldns_buffer_read(ldns_buffer *buffer, void *data, size_t count); </p>
<p> uint8_t ldns_buffer_read_u8_at(ldns_buffer *buffer, size_t at); </p>
<p> uint8_t ldns_buffer_read_u8(ldns_buffer *buffer); </p>
<p> uint16_t ldns_buffer_read_u16_at(ldns_buffer *buffer, size_t at); </p>
<p> uint16_t ldns_buffer_read_u16(ldns_buffer *buffer); </p>
<p> uint32_t ldns_buffer_read_u32_at(ldns_buffer *buffer, size_t at); </p>
<p> uint32_t ldns_buffer_read_u32(ldns_buffer *buffer); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer_write_at</i>()</p>
<dd>writes the given data to the buffer at the specified position .br <code>buffer</code>: the buffer .br <code>at</code>: the position (in number of bytes) to write the data at .br <code>data</code>: pointer to the data to write to the buffer .br <code>count</code>: the number of bytes of data to write</dl>
<dl>
<dt> <i>ldns_buffer_write_at</i>()</p>
<dd>writes the given data to the buffer at the specified position .br <code>buffer</code>: the buffer .br <code>at</code>: the position (in number of bytes) to write the data at .br <code>data</code>: pointer to the data to write to the buffer .br <code>count</code>: the number of bytes of data to write</dl>
<dl>
<dt> <i>ldns_buffer_write</i>()</p>
<dd>writes count bytes of data to the current position of the buffer .br <code>buffer</code>: the buffer .br <code>data</code>: the data to write .br <code>count</code>: the lenght of the data to write</dl>
<dl>
<dt> <i>ldns_buffer_write_string_at</i>()</p>
<dd>copies the given (null-delimited) string to the specified position at the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: the position in the buffer .br <code>str</code>: the string to write</dl>
<dl>
<dt> <i>ldns_buffer_write_string</i>()</p>
<dd>copies the given (null-delimited) string to the current position at the buffer .br <code>buffer</code>: the buffer .br <code>str</code>: the string to write</dl>
<dl>
<dt> <i>ldns_buffer_write_u8_at</i>()</p>
<dd>writes the given byte of data at the given position in the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: the position in the buffer .br <code>data</code>: the 8 bits to write</dl>
<dl>
<dt> <i>ldns_buffer_write_u8</i>()</p>
<dd>writes the given byte of data at the current position in the buffer .br <code>buffer</code>: the buffer .br <code>data</code>: the 8 bits to write</dl>
<dl>
<dt> <i>ldns_buffer_write_u16_at</i>()</p>
<dd>writes the given 2 byte integer at the given position in the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: the position in the buffer .br <code>data</code>: the 16 bits to write</dl>
<dl>
<dt> <i>ldns_buffer_write_u16</i>()</p>
<dd>writes the given 2 byte integer at the current position in the buffer .br <code>buffer</code>: the buffer .br <code>data</code>: the 16 bits to write</dl>
<dl>
<dt> <i>ldns_buffer_read_at</i>()</p>
<dd>copies count bytes of data at the given position to the given data-array .br <code>buffer</code>: the buffer .br <code>at</code>: the position in the buffer to start .br <code>data</code>: buffer to copy to .br <code>count</code>: the length of the data to copy</dl>
<dl>
<dt> <i>ldns_buffer_read</i>()</p>
<dd>copies count bytes of data at the current position to the given data-array .br <code>buffer</code>: the buffer .br <code>data</code>: buffer to copy to .br <code>count</code>: the length of the data to copy</dl>
<dl>
<dt> <i>ldns_buffer_read_u8_at</i>()</p>
<dd>returns the byte value at the given position in the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: the position in the buffer .br Returns 1 byte integer</dl>
<dl>
<dt> <i>ldns_buffer_read_u8</i>()</p>
<dd>returns the byte value at the current position in the buffer .br <code>buffer</code>: the buffer .br Returns 1 byte integer</dl>
<dl>
<dt> <i>ldns_buffer_read_u16_at</i>()</p>
<dd>returns the 2-byte integer value at the given position in the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: position in the buffer .br Returns 2 byte integer</dl>
<dl>
<dt> <i>ldns_buffer_read_u16</i>()</p>
<dd>returns the 2-byte integer value at the current position in the buffer .br <code>buffer</code>: the buffer .br Returns 2 byte integer</dl>
<dl>
<dt> <i>ldns_buffer_read_u32_at</i>()</p>
<dd>returns the 4-byte integer value at the given position in the buffer .br <code>buffer</code>: the buffer .br <code>at</code>: position in the buffer .br Returns 4 byte integer</dl>
<dl>
<dt> <i>ldns_buffer_read_u32</i>()</p>
<dd>returns the 4-byte integer value at the current position in the buffer .br <code>buffer</code>: the buffer .br Returns 4 byte integer</dl>
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
