---
title: "stdpmrmemory_resourcedo_deallocate(3)"
name: "stdpmrmemory_resourcedo_deallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmemory_resourcedo_deallocate/"
---

std::pmr::memory_resource::do_deallocate - std::pmr::memory_resource::do_deallocate

<h2>Synopsis</h2>

<pre><code>virtual void do_deallocate(void *p, std::size_t bytes, std::size_t alignment) = 0;
(since C++ 17)</code></pre> 
Deallocates the storage pointed to by p. 
p must have been returned by a prior call to allocate(bytes, alignment) on a memory_resource that compares equal to *this, and the storage it points to must not yet have been deallocated, otherwise the behavior is undefined. 

<h2>Exceptions</h2>

Throws nothing.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocates memory 
deallocate <i>(public member function)</i> 
