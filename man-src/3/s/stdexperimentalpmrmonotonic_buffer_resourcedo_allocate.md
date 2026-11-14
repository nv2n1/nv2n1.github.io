---
title: "stdexperimentalpmrmonotonic_buffer_resourcedo_allocate(3)"
name: "stdexperimentalpmrmonotonic_buffer_resourcedo_allocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrmonotonic_buffer_resourcedo_allocate/"
description: "std::experimental::pmr::monotonic_buffer_resource::do_allocate – std::experimental::pmr::monotonic_buffer_resource::do_allocate"
---

<p>std::experimental::pmr::monotonic_buffer_resource::do_allocate &#8211; std::experimental::pmr::monotonic_buffer_resource::do_allocate</p>
<h2>Synopsis</h2>
<p>virtual void* do_allocate(std::size_t bytes, std::size_t alignment); (library fundamentals TS)<br />
Allocates storage.<br />
If the current buffer has sufficient unused space to fit a block with the specified size and alignment, allocates the return block from the current buffer.<br />
Otherwise, this function allocates a new buffer by calling upstream_resource()-&gt;allocate(n, m), where n is not less than the greater of bytes and the next buffer size and m is not less than alignment. It sets the new buffer as the current buffer, increases the next buffer size by an implementation-defined growth factor (which is not necessarily integral), and then allocates the return block from the newly allocated buffer. </p>
<h2>Return value</h2>
<p>A pointer to allocated storage of at least bytes bytes in size, aligned to the specified alignment if such alignment is supported, and to alignof(std::max_align_t) otherwise. </p>
<h2>Exceptions</h2>
<p>Throws nothing unless calling allocate() on the upstream memory resource throws.</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory<br />
allocate <i>(public member function of std::experimental::pmr::memory_resource)</i><br />
do_allocate allocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::experimental::pmr::memory_resource)</i><br />
<code>[virtual]</code> </p>
