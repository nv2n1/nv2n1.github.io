---
title: "stdpmrmemory_resourcedo_allocate(3)"
name: "stdpmrmemory_resourcedo_allocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmemory_resourcedo_allocate/"
---

std::pmr::memory_resource::do_allocate - std::pmr::memory_resource::do_allocate

<h2>Synopsis</h2>

<pre><code>virtual void *do_allocate(std::size_t bytes, std::size_t alignment) = 0;
(since C++ 17)</code></pre> 
Allocates storage with a size of at least bytes bytes, aligned to the specified alignment. 
alignment shall be a power of two. 

<h2>Exceptions</h2>

Throws an exception if storage of the requested size and alignment cannot be obtained. 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2843 C++17 handling of unsupported alignment contradictory throws an exception

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocates memory 
allocate <i>(public member function)</i> 
