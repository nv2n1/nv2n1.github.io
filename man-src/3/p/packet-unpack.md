---
title: "packet-unpack(3)"
name: "packet-unpack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-unpack/"
description: "packet.unpack – Unpack module"
---

<p>packet.unpack &#8211; Unpack module</p>
<h2>Description</h2>
<p>Provides the object for managing and unpacking raw data from a working buffer.</p>
<h2>Classes</h2>
<h3>class Unpack(__builtin__.object)</h3>
<pre>Unpack object
Usage:
 from packet.unpack import Unpack
 x = Unpack(buffer)
 # Get 32 bytes from the working buffer and move the offset pointer
 data = x.read(32)
 # Get all the unprocessed bytes from the working buffer
 # (all bytes starting from the offset pointer)
 # Do not move the offset pointer
 data = x.getbytes()
 # Get all bytes from the working buffer from the given offset
 # Do not move the offset pointer
 data = x.getbytes(offset)
 # Return the number of unprocessed bytes left in the working buffer
 size = x.size()
 size = len(x)
 # Get the offset pointer
 offset = x.tell()
 # Set the offset pointer
 x.seek(offset)
 # Append the given data to the working buffer
 x.append(data)
 # Insert the given data to the working buffer right before the
 # offset pointer. This resets the working buffer completely
 # and the offset pointer is initialized to zero. It is like
 # re-instantiating the object like:
 # x = Unpack(data + x.getbytes())
 x.insert(data)
 # Save state
 sid = x.save_state()
 # Restore state
 x.restore_state(sid)
 # Unpack an 'unsigned short' (2 bytes in network order)
 short_int = x.unpack(2, '!H')[0]
 # Unpack different basic types
 char = x.unpack_char()
 uchar = x.unpack_uchar()
 short = x.unpack_short()
 ushort = x.unpack_ushort()
 int = x.unpack_int()
 uint = x.unpack_uint()
 int64 = x.unpack_int64()
 uint64 = x.unpack_uint64()
 data1 = x.unpack_opaque()
 data2 = x.unpack_opaque(64) # Length of opaque must be &lt;= 64
 data3 = x.unpack_fopaque(32)
 # Get string where length is given as an unsigned integer
 buffer = x.unpack_string()
 # Get string of fixed length
 buffer = x.unpack_string(32)
 # Get string where length is given as a short integer
 buffer = x.unpack_string(Unpack.unpack_short)
 buffer = x.unpack_string(ltype=Unpack.unpack_short)
 # Get string padded to a 4 byte boundary, discard padding bytes
 buffer = x.unpack_string(pad=4)
 # Get an array of unsigned integers
 alist = x.unpack_array()
 # Get a fixed length array of unsigned integers
 alist = x.unpack_array(ltype=10)
 # Get an array of short integers
 alist = x.unpack_array(Unpack.unpack_short)
 # Get an array of strings, the length of the array is given
 # by a short integer
 alist = x.unpack_array(Unpack.unpack_string, Unpack.unpack_short)
 # Get an array of strings, the length of each string is given by
 # a short integer and each string is padded to a 4 byte boundary
 alist = x.unpack_array(Unpack.unpack_string, uargs={'ltype':Unpack.unpack_short, 'pad':4})
 # Get an array of objects decoded by item_obj where the first
 # argument to item_obj is the unpack object, e.g., item = item_obj(x)
 alist = x.unpack_array(item_obj)
 # Get a list of unsigned integers
 alist = x.unpack_list()
 # Get a list of short integers
 alist = x.unpack_list(Unpack.unpack_short)
 # Get a list of strings, the next item flag is given
 # by a short integer
 alist = x.unpack_list(Unpack.unpack_string, Unpack.unpack_short)
 # Get a list of strings, the length of each string is given by
 # a short integer and each string is padded to a 4 byte boundary
 alist = x.unpack_list(Unpack.unpack_string, uargs={'ltype':Unpack.unpack_short, 'pad':4})
 # Unpack a conditional, it unpacks a conditional flag first and
 # if it is true it unpacks the item given and returns it. If the
 # conditional flag decoded is false, the method returns None
 buffer = x.unpack_conditional(Unpack.unpack_opaque)
 # Unpack an array of unsigned integers and convert array into
 # a single long integer
 bitmask = unpack_bitmap()
<code>Methods defined here:</code>
---------------------
<code>__init__(self, data)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>data:</code>
<dd>Raw packet data
</dl></dl>
<code>__len__ = size(self)</code>
<code>append(self, data)</code>
Append data to the working buffer.
<code>getbytes(self, offset=None)</code>
Get the number of bytes given from the working buffer.
Do not move the offset pointer.
<dl><dt><dd><dl><dt><code>offset:</code>
<dd>Starting offset of data to return [default: current offset]
</dl></dl>
<code>insert(self, data)</code>
Insert data to the beginning of the current working buffer.
<code>read(self, size, pad=0)</code>
Get the number of bytes given from the working buffer.
Move the offset pointer.
<dl><dt><dd><dl><dt><code>size:</code>
<dd>Length of data to get
<dt><code>pad:</code>
<dd>Get and discard padding bytes [default: 0]
If given, data is padded to this byte boundary
</dl></dl>
<code>restore_state(self, sid)</code>
Restore state given by the state id
<code>save_state(self)</code>
Save state and return the state id
<code>seek(self, offset)</code>
Set the offset pointer.
<code>size(self)</code>
Return the number of unprocessed bytes left in the working buffer
<code>tell(self)</code>
Get the offset pointer.
<code>unpack(self, size, fmt)</code>
Get the number of bytes given from the working buffer and process
it according to the given format.
Return a tuple of unpack items, see struct.unpack.
<dl><dt><dd><dl><dt><code>size:</code>
<dd>Length of data to process
<dt><code>fmt:</code>
<dd>Format string on how to process data
</dl></dl>
<code>unpack_array(self, unpack_item=&lt;function unpack_uint&gt;, ltype=&lt;function unpack_uint&gt;, uargs={}, maxcount=0, islist=False)</code>
Get a variable length array, the type of objects in the array
is given by the unpacking function unpack_item and the type
to decode the length of the array is given by ltype
<dl><dt><dd><dl><dt><code>unpack_item:</code>
<dd>Unpack function for each item in the array [default: unpack_uint]
<dt><code>ltype:</code>
<dd>Function to decode length of array [default: unpack_uint]
Could also be given as an integer to have a fixed length array
<dt><code>uargs:</code>
<dd>Named arguments to pass to unpack_item function [default: {}]
<dt><code>maxcount:</code>
<dd>Maximum length of array [default: any length]
</dl></dl>
<code>unpack_bitmap(self)</code>
Unpack an array of unsigned integers and convert array into
a single long integer
<code>unpack_char(self)</code>
Get a signed char
<code>unpack_conditional(self, unpack_item=&lt;function unpack_uint&gt;, ltype=&lt;function unpack_uint&gt;, uargs={})</code>
Get an item if condition flag given by ltype is true, if condition
flag is false then return None
<dl><dt><dd><dl><dt><code>unpack_item:</code>
<dd>Unpack function for item if condition is true [default: unpack_uint]
<dt><code>ltype:</code>
<dd>Function to decode the condition flag [default: unpack_uint]
<dt><code>uargs:</code>
<dd>Named arguments to pass to unpack_item function [default: {}]
</dl></dl>
<code>unpack_fopaque(self, size)</code>
Get a fixed length opaque
<code>unpack_int(self)</code>
Get a signed integer
<code>unpack_int64(self)</code>
Get a signed 64 bit integer
<code>unpack_list(self, *kwts, **kwds)</code>
Get an indeterminate size list, the type of objects in the list
is given by the unpacking function unpack_item and the type
to decode the next item flag is given by ltype
<dl><dt><dd><dl><dt><code>unpack_item:</code>
<dd>Unpack function for each item in the list [default: unpack_uint]
<dt><code>ltype:</code>
<dd>Function to decode the next item flag [default: unpack_uint]
<dt><code>uargs:</code>
<dd>Named arguments to pass to unpack_item function [default: {}]
</dl></dl>
<code>unpack_opaque(self, maxcount=0)</code>
Get a variable length opaque up to a maximum length of maxcount
<code>unpack_short(self)</code>
Get a signed short integer
<code>unpack_string(self, ltype=&lt;function unpack_uint&gt;, pad=0, maxcount=0)</code>
Get a variable length string
<dl><dt><dd><dl><dt><code>ltype:</code>
<dd>Function to decode length of string [default: unpack_uint]
Could also be given as an integer to have a fixed length string
<dt><code>pad:</code>
<dd>Get and discard padding bytes [default: 0]
If given, string is padded to this byte boundary
<dt><code>maxcount:</code>
<dd>Maximum length of string [default: any length]
</dl></dl>
<code>unpack_uchar(self)</code>
Get an unsigned char
<code>unpack_uint(self)</code>
Get an unsigned integer
<code>unpack_uint64(self)</code>
Get an unsigned 64 bit integer
<code>unpack_ushort(self)</code>
Get an unsigned short integer</pre>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
