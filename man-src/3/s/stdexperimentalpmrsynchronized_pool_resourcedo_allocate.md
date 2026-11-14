---
title: "stdexperimentalpmrsynchronized_pool_resourcedo_allocate(3)"
name: "stdexperimentalpmrsynchronized_pool_resourcedo_allocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrsynchronized_pool_resourcedo_allocate/"
description: "std::experimental::pmr::synchronized_pool_resource::do_allocate – std::experimental::pmr::synchronized_pool_resource::do_allocate"
---

<p>std::experimental::pmr::synchronized_pool_resource::do_allocate &#8211; std::experimental::pmr::synchronized_pool_resource::do_allocate</p>
<h2>Synopsis</h2>
<p>virtual void* do_allocate(std::size_t bytes, std::size_t alignment); (library fundamentals TS)<br />
Allocates storage.<br />
If the pool selected for a block of size bytes is unable to satisfy the request from its internal data structures, calls allocate() on the upstream memory resource to obtain memory.<br />
If the size requested is larger than what the largest pool can handle, memory is allocated by calling allocate() on the upstream memory resource. </p>
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
