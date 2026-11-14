---
title: "filemap_fdatawait_range(9)"
name: "filemap_fdatawait_range"
section: "9"
letter: "f"
url: "/docs/linux/man/9-filemap_fdatawait_range/"
---

filemap_fdatawait_range - wait for writeback to complete

<h2>Synopsis</h2>

<pre><code>int filemap_fdatawait_range(struct address_space *mapping, loff_t start_byte, loff_t end_byte);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>address space structure to wait for</dl>
 

 <i>start_byte</i>
<dl><dd>offset in bytes where the range starts</dl>
 

 <i>end_byte</i>
<dl><dd>offset in bytes where the range ends (inclusive)</dl>

<h2>Description</h2>

Walk the list of under-writeback pages of the given address space in the given range and wait for all of them. Check error status of the address space and return it. 

 Since the error status of the address space is cleared by this function, callers are responsible for checking the return value and handling and/or reporting the error.

<h2>Copyright</h2>


