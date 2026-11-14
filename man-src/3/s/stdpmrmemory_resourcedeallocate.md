---
title: "stdpmrmemory_resourcedeallocate(3)"
name: "stdpmrmemory_resourcedeallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmemory_resourcedeallocate/"
description: "std::pmr::memory_resource::deallocate – std::pmr::memory_resource::deallocate"
---

<p>std::pmr::memory_resource::deallocate &#8211; std::pmr::memory_resource::deallocate</p>
<h2>Synopsis</h2>
<pre><code>void deallocate(void *p,

                std::size_t bytes, (since C++ 17)

                                       std::size_t alignment = alignof(std::max_align_t));</code></pre>
<p>Deallocates the storage pointed to by p. p shall have been returned by a prior call to allocate(bytes, alignment) on a memory_resource that compares equal to *this, and the storage it points to shall not yet have been deallocated.<br />
Equivalent to do_deallocate(p, bytes, alignment);. </p>
<h2>Exceptions</h2>
<p>Throws nothing.</p>
<h2>See also</h2>
<p>do_deallocate deallocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(virtual private member function)<br />
<code>[virtual]</code> </p>
