---
title: "stdpmrmemory_resourceallocate(3)"
name: "stdpmrmemory_resourceallocate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpmrmemory_resourceallocate/"
description: "std::pmr::memory_resource::allocate – std::pmr::memory_resource::allocate"
---

<p>std::pmr::memory_resource::allocate &#8211; std::pmr::memory_resource::allocate</p>
<h2>Synopsis</h2>
<pre><code>void *allocate(std::size_t bytes, (since C++ 17)

                                      std::size_t alignment = alignof(std::max_align_t));
(until C++ 20)

    [[nodiscard]] void *allocate(std::size_t bytes, (since C++ 20)

                                                        std::size_t alignment = alignof(std::max_align_t));
Allocates storage with a size of at least bytes bytes.The returned storage is aligned to the specified alignment if such alignment is supported, and to alignof(std::max_align_t) otherwise.

                                                                                                                                                     Equivalent to return do_allocate(bytes, alignment);
.
</code></pre>
<h2>Exceptions</h2>
<p>Throws an exception if storage of the requested size and alignment cannot be obtained.</p>
<h2>See also</h2>
<p>do_allocate allocates memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(virtual private member function)<br />
<code>[virtual]</code> </p>
