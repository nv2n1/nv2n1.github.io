---
title: "stdexperimentalpmrmemory_resourcedo_allocate(3)"
name: "stdexperimentalpmrmemory_resourcedo_allocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrmemory_resourcedo_allocate/"
---

std::experimental::pmr::memory_resource::do_allocate - std::experimental::pmr::memory_resource::do_allocate

<h2>Synopsis</h2>

<pre><code>virtual void *do_allocate(std::size_t bytes, std::size_t alignment) = 0;
(library fundamentals TS)</code></pre> 
Allocates storage with a size of at least bytes bytes. The returned storage is aligned to the specified alignment if such alignment is supported, and to alignof(std::max_align_t) otherwise. 
alignment shall be a power of two. 

<h2>Exceptions</h2>

Throws an exception if storage of the requested size and alignment cannot be obtained.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory 
allocate <i>(public member function)</i> 
